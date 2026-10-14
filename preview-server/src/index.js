// Divine Gifts preview server — Cloudflare Worker.
//
//   POST /api/preview        multipart: photo, style, category  → watermarked preview
//   GET  /p/<id>.jpg         public watermarked preview image
//   GET  /admin/job/<id>     job metadata                (Authorization: Bearer ADMIN_TOKEN)
//   GET  /admin/final/<id>   full-resolution, un-watermarked artwork
//   GET  /admin/upload/<id>  the customer's original photo
//   GET  /health
//
// Storage (R2 bucket bound as ART):
//   uploads/<id>   original photo      final/<id>.png  generated artwork
//   previews/<id>.jpg  watermarked     jobs/<id>.json  metadata

import { PhotonImage, resize, SamplingFilter, watermark } from '@cf-wasm/photon';
import WATERMARK_PNG from './assets/watermark.png';
import { lookupStyle } from './prompts.js';

const MAX_UPLOAD_BYTES = 15 * 1024 * 1024;
const ACCEPTED_TYPES = ['image/jpeg', 'image/png', 'image/webp'];

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const cors = corsHeaders(request, env);

    if (request.method === 'OPTIONS') return new Response(null, { status: 204, headers: cors });

    try {
      if (url.pathname === '/health') {
        return json({ ok: true, model: env.OPENAI_IMAGE_MODEL, mock: env.MOCK_OPENAI === '1' }, 200, cors);
      }
      if (url.pathname === '/api/preview' && request.method === 'POST') {
        return await createPreview(request, env, cors);
      }
      const preview = url.pathname.match(/^\/p\/([0-9a-f-]{36})\.jpg$/);
      if (preview && request.method === 'GET') {
        return await serveObject(env, `previews/${preview[1]}.jpg`, 'public, max-age=31536000, immutable');
      }
      const admin = url.pathname.match(/^\/admin\/(job|final|upload)\/([0-9a-f-]{36})$/);
      if (admin && request.method === 'GET') {
        if (!isAdmin(request, env)) return json({ error: 'unauthorized' }, 401);
        const [, kind, id] = admin;
        if (kind === 'job') return await serveObject(env, `jobs/${id}.json`, 'private, no-store');
        if (kind === 'final') return await serveObject(env, `final/${id}.png`, 'private, no-store', `divine-gifts-${id}.png`);
        return await serveObject(env, `uploads/${id}`, 'private, no-store');
      }
      return json({ error: 'not_found' }, 404, cors);
    } catch (err) {
      console.error('unhandled', err && err.stack ? err.stack : err);
      return json({ error: 'server_error', message: 'Something went wrong. Please try again.' }, 500, cors);
    }
  },
};

/* ------------------------------------------------------------------ preview */

async function createPreview(request, env, cors) {
  if (!originAllowed(request, env)) return json({ error: 'forbidden_origin' }, 403, cors);

  const form = await request.formData();
  const photo = form.get('photo');
  const style = String(form.get('style') || '');
  const category = String(form.get('category') || 'classic');

  if (!photo || typeof photo === 'string') return json({ error: 'missing_photo', message: 'Please choose a photo.' }, 400, cors);
  if (!ACCEPTED_TYPES.includes(photo.type)) {
    return json({ error: 'bad_type', message: 'Please upload a JPG, PNG or WebP photo.' }, 400, cors);
  }
  if (photo.size > MAX_UPLOAD_BYTES) return json({ error: 'too_large', message: 'That photo is over 15 MB. Please choose a smaller one.' }, 400, cors);

  const spec = lookupStyle(category, style);
  if (!spec) return json({ error: 'unknown_style', message: 'Please choose one of the styles shown.' }, 400, cors);

  // Daily per-visitor limit
  const limit = parseInt(env.DAILY_LIMIT || '6', 10);
  const rateKey = `rl:${await visitorKey(request)}:${new Date().toISOString().slice(0, 10)}`;
  const used = parseInt((await env.RATE.get(rateKey)) || '0', 10);
  if (used >= limit) {
    return json({ error: 'daily_limit', message: `You've reached today's limit of ${limit} free previews. Please come back tomorrow.`, remaining: 0 }, 429, cors);
  }
  await env.RATE.put(rateKey, String(used + 1), { expirationTtl: 60 * 60 * 26 });

  const id = crypto.randomUUID();
  const photoBytes = new Uint8Array(await photo.arrayBuffer());
  await env.ART.put(`uploads/${id}`, photoBytes, { httpMetadata: { contentType: photo.type } });

  let artwork;
  try {
    artwork = env.MOCK_OPENAI === '1'
      ? mockGenerate(photoBytes)
      : await openaiEdit(env, photoBytes, photo.type, spec);
  } catch (err) {
    // Give the attempt back if generation failed
    await env.RATE.put(rateKey, String(used), { expirationTtl: 60 * 60 * 26 });
    const blocked = err && err.code === 'moderation_blocked';
    console.error('generation failed', err && err.message);
    return json({
      error: blocked ? 'blocked' : 'generation_failed',
      message: blocked
        ? "We couldn't create a preview from this photo. Please try a different photo."
        : 'Our artist is busy right now. Please try again in a moment.',
    }, 502, cors);
  }

  await env.ART.put(`final/${id}.png`, artwork, { httpMetadata: { contentType: 'image/png' } });
  const previewJpg = makePreview(artwork, parseInt(env.PREVIEW_WIDTH || '768', 10));
  await env.ART.put(`previews/${id}.jpg`, previewJpg, { httpMetadata: { contentType: 'image/jpeg' } });

  const job = {
    id,
    created_at: new Date().toISOString(),
    category,
    style,
    size: spec.size,
    model: env.MOCK_OPENAI === '1' ? 'mock' : env.OPENAI_IMAGE_MODEL,
    upload: `uploads/${id}`,
    final: `final/${id}.png`,
    preview: `previews/${id}.jpg`,
  };
  await env.ART.put(`jobs/${id}.json`, JSON.stringify(job, null, 2), { httpMetadata: { contentType: 'application/json' } });

  const base = env.PUBLIC_BASE_URL || new URL(request.url).origin;
  return json({ id, previewUrl: `${base}/p/${id}.jpg`, style, remaining: limit - used - 1 }, 200, cors);
}

async function openaiEdit(env, bytes, type, spec) {
  if (!env.OPENAI_API_KEY) throw new Error('OPENAI_API_KEY is not set');
  const ext = type === 'image/png' ? 'png' : type === 'image/webp' ? 'webp' : 'jpg';
  const fd = new FormData();
  fd.append('model', env.OPENAI_IMAGE_MODEL || 'gpt-image-1');
  fd.append('image', new File([bytes], `photo.${ext}`, { type }));
  fd.append('prompt', spec.prompt);
  fd.append('size', spec.size);
  fd.append('quality', env.OPENAI_IMAGE_QUALITY || 'medium');
  fd.append('n', '1');
  if (env.OPENAI_INPUT_FIDELITY) fd.append('input_fidelity', env.OPENAI_INPUT_FIDELITY);

  const res = await fetch('https://api.openai.com/v1/images/edits', {
    method: 'POST',
    headers: { Authorization: `Bearer ${env.OPENAI_API_KEY}` },
    body: fd,
  });
  const body = await res.json().catch(() => ({}));
  if (!res.ok) {
    const e = new Error(`OpenAI ${res.status}: ${body.error ? body.error.message : 'unknown error'}`);
    e.code = body.error && body.error.code;
    throw e;
  }
  const b64 = body.data && body.data[0] && body.data[0].b64_json;
  if (!b64) throw new Error('OpenAI returned no image');
  return base64ToBytes(b64);
}

/** Local-testing stand-in for OpenAI: returns the photo re-encoded as PNG. */
function mockGenerate(bytes) {
  const img = PhotonImage.new_from_byteslice(bytes);
  try { return img.get_bytes(); } finally { img.free(); }
}

/** Downscale and tile the watermark across the artwork. */
function makePreview(pngBytes, width) {
  const src = PhotonImage.new_from_byteslice(pngBytes);
  const wm = PhotonImage.new_from_byteslice(new Uint8Array(WATERMARK_PNG));
  try {
    const w = Math.min(width, src.get_width());
    const h = Math.round(src.get_height() * (w / src.get_width()));
    const out = resize(src, w, h, SamplingFilter.Lanczos3);
    try {
      const tw = wm.get_width();
      const th = wm.get_height();
      for (let y = -Math.floor(th / 3), row = 0; y < h; y += th, row++) {
        for (let x = row % 2 ? -Math.floor(tw / 2) : 0; x < w; x += tw) {
          if (x >= 0 && y >= 0 && x + tw <= w && y + th <= h) watermark(out, wm, BigInt(x), BigInt(y));
          else watermarkClipped(out, wm, x, y, w, h);
        }
      }
      return out.get_bytes_jpeg(82);
    } finally { out.free(); }
  } finally { src.free(); wm.free(); }
}

/** watermark() needs the overlay fully inside the image; crop it for edge tiles. */
function watermarkClipped(img, wm, x, y, w, h) {
  const x0 = Math.max(0, x), y0 = Math.max(0, y);
  const x1 = Math.min(w, x + wm.get_width()), y1 = Math.min(h, y + wm.get_height());
  if (x1 - x0 < 8 || y1 - y0 < 8) return;
  const raw = wm.get_raw_pixels();
  const cw = x1 - x0, ch = y1 - y0, sx = x0 - x, sy = y0 - y, ww = wm.get_width();
  const buf = new Uint8Array(cw * ch * 4);
  for (let r = 0; r < ch; r++) {
    const from = ((sy + r) * ww + sx) * 4;
    buf.set(raw.subarray(from, from + cw * 4), r * cw * 4);
  }
  const piece = new PhotonImage(buf, cw, ch);
  try { watermark(img, piece, BigInt(x0), BigInt(y0)); } finally { piece.free(); }
}

/* ------------------------------------------------------------------ helpers */

async function serveObject(env, key, cacheControl, downloadName) {
  const obj = await env.ART.get(key);
  if (!obj) return json({ error: 'not_found' }, 404);
  const headers = new Headers({ 'Cache-Control': cacheControl });
  obj.writeHttpMetadata(headers);
  headers.set('Access-Control-Allow-Origin', '*');
  if (downloadName) headers.set('Content-Disposition', `attachment; filename="${downloadName}"`);
  return new Response(obj.body, { headers });
}

function allowedOrigins(env) {
  return String(env.ALLOWED_ORIGINS || '').split(',').map((s) => s.trim()).filter(Boolean);
}

function originAllowed(request, env) {
  const origin = request.headers.get('Origin');
  return !!origin && allowedOrigins(env).includes(origin);
}

function corsHeaders(request, env) {
  const origin = request.headers.get('Origin');
  const h = { 'Access-Control-Allow-Methods': 'GET, POST, OPTIONS', 'Access-Control-Allow-Headers': 'Content-Type', 'Vary': 'Origin' };
  if (origin && allowedOrigins(env).includes(origin)) h['Access-Control-Allow-Origin'] = origin;
  return h;
}

function isAdmin(request, env) {
  if (!env.ADMIN_TOKEN) return false;
  const auth = request.headers.get('Authorization') || '';
  const token = auth.startsWith('Bearer ') ? auth.slice(7) : new URL(request.url).searchParams.get('token') || '';
  return timingSafeEqual(token, env.ADMIN_TOKEN);
}

function timingSafeEqual(a, b) {
  if (a.length !== b.length) return false;
  let diff = 0;
  for (let i = 0; i < a.length; i++) diff |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return diff === 0;
}

async function visitorKey(request) {
  const ip = request.headers.get('CF-Connecting-IP') || 'local';
  const digest = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(ip));
  return [...new Uint8Array(digest)].slice(0, 12).map((b) => b.toString(16).padStart(2, '0')).join('');
}

function base64ToBytes(b64) {
  const bin = atob(b64);
  const out = new Uint8Array(bin.length);
  for (let i = 0; i < bin.length; i++) out[i] = bin.charCodeAt(i);
  return out;
}

function json(data, status = 200, extra = {}) {
  return new Response(JSON.stringify(data), { status, headers: { 'Content-Type': 'application/json', ...extra } });
}
