"""Edit engine V2 — matched to the reference ad (text sizes, cards, rhythm, anatomy FX, music).

    python edit/engine2.py [--only 1-12] [--preview] [--out name.mp4]
Shot list: edit/edl2.py. Captions: edit/captions.py (measured from reference). FX: edit/fxlib.py.
"""
import argparse, hashlib, json, math, subprocess, sys
from concurrent.futures import ThreadPoolExecutor
from functools import lru_cache
from pathlib import Path
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = Path(__file__).resolve().parent; P = HERE.parent
sys.path.insert(0, str(HERE))
import assets, captions, fxlib, edl2
from engine import nerve_layer, lerp_kf
FONTS = Path("/home/user/claude_code_sam/ads/video/fonts")
FPS, W, H = 30, 1080, 1920
BUILD = P / "build" / "shots2"; BUILD.mkdir(parents=True, exist_ok=True)
BURG = (116, 61, 60)
def font(n, s): return ImageFont.truetype(str(FONTS / n), s)

timing = {r["row"]: r for r in json.load(open(HERE / "vo_timing.json"))}
END_PAD = 2.6
TOTAL = max(r["end"] for r in timing.values()) + END_PAD

def shot_start(s):
    r = timing[s["row"]]
    t = 0.0 if (s["row"] == 1 and s["w"] == 0) else r["words"][s["w"]]["s"] - 0.03
    return t + s.get("dt", 0.0)

def build_timeline(shots):
    out = []
    for i, s in enumerate(shots):
        t0 = shot_start(s); t1 = shot_start(shots[i + 1]) if i + 1 < len(shots) else TOTAL
        f0, f1 = round(t0 * FPS), round(t1 * FPS)
        if f1 <= f0: raise ValueError(f"shot {i} row {s['row']} w{s['w']}: no duration")
        out.append({**s, "i": i, "f0": f0, "f1": f1, "n": f1 - f0, "t0": f0 / FPS})
    return out

# ---------------------------------------------------------------- base clips
def base_clip(s):
    if "src" not in s: return None
    fx = s.get("fx", {}); src = assets.path(s["src"])
    keyd = [src, s.get("ss", 0), s["n"], {k: fx.get(k) for k in ("fx", "fy", "z", "speed", "bw", "hflip", "crop", "blur", "key")}]
    out = BUILD / (hashlib.md5(json.dumps(keyd, sort_keys=True, default=str).encode()).hexdigest()[:12] + ".mp4")
    if out.exists(): return out
    if fx.get("key"):   # green-screen product render keyed over a flat studio background
        vf = (f"[0:v]fps={FPS},chromakey=0x00FF00:0.32:0.08,scale={W}:-2[k];color=c={fx['key']}:s={W}x{H}:r={FPS}[bg];"
              f"[bg][k]overlay=0:(H-h)/2-120:shortest=1,tpad=stop_mode=clone:stop_duration=30,format=yuv420p[v]")
        cmd = ["ffmpeg", "-v", "error", "-y", "-ss", str(s.get("ss", 0)), "-i", src, "-filter_complex", vf, "-map", "[v]",
               "-frames:v", str(s["n"]), "-an", "-c:v", "libx264", "-preset", "veryfast", "-crf", "14", str(out)]
        r = subprocess.run(cmd, capture_output=True, text=True)
        if r.returncode: raise RuntimeError(r.stderr[-300:])
        return out
    z = fx.get("z", 1.0); chain = [f"setpts=PTS/{fx.get('speed', 1.0)}", f"fps={FPS}"]
    if fx.get("crop"): x, y, w, h = fx["crop"]; chain.append(f"crop=iw*{w}:ih*{h}:iw*{x}:ih*{y}")
    chain += [f"scale=w='if(gt(a,{W}/{H}),-2,{int(W*z)})':h='if(gt(a,{W}/{H}),{int(H*z)},-2)'",
              f"crop={W}:{H}:(iw-{W})*{fx.get('fx',0.5)}:(ih-{H})*{fx.get('fy',0.5)}"]
    if fx.get("hflip"): chain.append("hflip")
    if fx.get("bw"): chain.append("hue=s=0,eq=contrast=1.1")
    if fx.get("blur"): chain.append(f"gblur=sigma={fx['blur']}")
    chain += ["tpad=stop_mode=clone:stop_duration=30", "format=yuv420p"]
    cmd = ["ffmpeg", "-v", "error", "-y", "-ss", str(s.get("ss", 0)), "-i", src, "-vf", ",".join(chain),
           "-frames:v", str(s["n"]), "-an", "-c:v", "libx264", "-preset", "veryfast", "-crf", "14", str(out)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode or not out.exists(): raise RuntimeError(f"row {s['row']} src {s['src']}: {r.stderr[-300:]}")
    return out

def read_frames(path, n):
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-i", str(path), "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE)
    last = None
    for _ in range(n):
        b = p.stdout.read(W * H * 3)
        if len(b) == W * H * 3: last = np.frombuffer(b, np.uint8).reshape(H, W, 3)
        yield last.copy() if last is not None else np.zeros((H, W, 3), np.uint8)
    p.stdout.close(); p.wait()

# ---------------------------------------------------------------- text styles (measured from reference)
def tracked(d, xy, s, fnt, fill, track=0, stroke=0, stroke_fill=None):
    x, y = xy
    for c in s:
        d.text((x, y), c, font=fnt, fill=fill, stroke_width=stroke, stroke_fill=stroke_fill); x += d.textlength(c, font=fnt) + track
def tlen(s, fnt, track=0):
    d = ImageDraw.Draw(Image.new("RGB", (1, 1))); return sum(d.textlength(c, font=fnt) for c in s) + track * max(0, len(s) - 1)

@lru_cache(maxsize=64)
def hook_box(text):          # red box, white heavy caps, 824x104 at 1080w
    f = font("Montserrat-900.ttf", 60); w = tlen(text, f, -1) + 56; h = 104
    im = Image.new("RGBA", (int(w) + 4, h + 4), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle((2, 2, w + 2, h + 2), 12, fill=(237, 20, 30, 255))
    asc, desc = f.getmetrics(); tracked(d, (30, 2 + (h - asc - desc) / 2 + 3), text, f, (255, 255, 255), -1)
    return np.asarray(im, np.float32)

@lru_cache(maxsize=64)
def serif_line(text, red=False):   # 'TOP 3 SHOES / YOU SHOULD / NEVER / WEAR' build-up style
    f = font("PlayfairDisplay-900.ttf", 100); w = int(tlen(text, f, 2)) + 50; h = 160
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0)); sh = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    tracked(ImageDraw.Draw(sh), (27, 22), text, f, (0, 0, 0, 210), 2)
    im = Image.alpha_composite(im, sh.filter(ImageFilter.GaussianBlur(5)))
    tracked(ImageDraw.Draw(im), (22, 14), text, f, (230, 25, 25) if red else (255, 255, 255), 2, 3 if red else 0, (255, 255, 255) if red else None)
    return np.asarray(im, np.float32)

@lru_cache(maxsize=64)
def name_box(text):          # product name: caption box, bold caps (reference 'HF FLOW / BAREFOOT SHOES')
    f = font("TikTokSans-800.ttf", 46); lines = text.split("\n")
    ws = [tlen(l, f, -1) for l in lines]; Wb = int(max(ws) + 60); Hb = 66 * len(lines) + 40
    im = Image.new("RGBA", (Wb + 4, Hb + 4), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle((2, 2, Wb + 2, Hb + 2), 24, fill=(255, 255, 255, 255))
    for i, (l, w) in enumerate(zip(lines, ws)): tracked(d, ((Wb - w) / 2 + 2, 18 + i * 66), l, f, (0, 0, 0), -1)
    return np.asarray(im, np.float32)

@lru_cache(maxsize=64)
def spaced(text, color=(255, 255, 255)):   # diagram label 'Z E R O - D R O P   S O L E'
    f = font("Montserrat-800.ttf", 50); s = " ".join(text); w = int(tlen(s, f, 3)) + 50; h = 100
    if w > 1040: f = font("Montserrat-800.ttf", int(50 * 1000 / w)); w = int(tlen(s, f, 3)) + 50
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0)); sh = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    tracked(ImageDraw.Draw(sh), (25, 24), s, f, (0, 0, 0, 255), 3, 4, (0, 0, 0, 255)); im = Image.alpha_composite(im, sh.filter(ImageFilter.GaussianBlur(6)))
    tracked(ImageDraw.Draw(im), (25, 22), s, f, color, 3)
    return np.asarray(im, np.float32)

@lru_cache(maxsize=64)
def top_box(text, red_word=None):   # 'They just make the problem' white box + red 'WORSE' box (reference 4-6 s)
    f = font("TikTokSans-700.ttf", 46); w = tlen(text, f, -1.5) + 44; h = 76
    im = Image.new("RGBA", (int(w) + 4, h + (96 if red_word else 0) + 4), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle((2, 2, w + 2, h + 2), 12, fill=(255, 255, 255, 255)); tracked(d, (24, 12), text, f, (0, 0, 0), -1.5)
    if red_word:
        fw = font("Montserrat-900.ttf", 44); rw = tlen(red_word, fw) + 40; x0 = (w - rw) / 2
        d.rounded_rectangle((x0, h + 18, x0 + rw, h + 88), 10, fill=(237, 20, 30, 255)); d.text((x0 + 20, h + 26), red_word, font=fw, fill=(255, 255, 255))
    return np.asarray(im, np.float32)

def draw_tags(frame, tags, tl):
    for tg in tags:
        t0, t1 = tg.get("t0", 0.0), tg.get("t1", 99)
        if not (t0 <= tl < t1): continue
        kind = tg["kind"]; u = fxlib.ease((tl - t0) / 0.14)
        a = {"hook": lambda: hook_box(tg["text"]), "serif": lambda: serif_line(tg["text"], tg.get("red", False)),
             "name": lambda: name_box(tg["text"]), "spaced": lambda: spaced(tg["text"]),
             "top": lambda: top_box(tg["text"], tg.get("red_word")), "small": lambda: small_label(tg["text"])}[kind]()
        sc = (0.8 + 0.2 * u) if tg.get("pop", True) else 1.0
        fxlib.blit(frame, a, tg.get("x", W / 2), tg.get("y", 892), sc, min(1.0, u * 1.5))

# ---------------------------------------------------------------- cards
@lru_cache(maxsize=32)
def number_title(n):
    f = font("AlfaSlabOne-400.ttf", 112); text = f"NUMBER {n}"
    d0 = ImageDraw.Draw(Image.new("RGB", (1, 1))); b = d0.textbbox((0, 0), text, font=f, stroke_width=6)
    w, h = b[2] - b[0] + 40, b[3] - b[1] + 40
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0)); sh = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    ImageDraw.Draw(sh).text((24 - b[0], 26 - b[1]), text, font=f, fill=(0, 0, 0, 200), stroke_width=6, stroke_fill=(0, 0, 0, 200))
    im = Image.alpha_composite(im, sh.filter(ImageFilter.GaussianBlur(3)))
    ImageDraw.Draw(im).text((20 - b[0], 20 - b[1]), text, font=f, fill=(255, 0, 0), stroke_width=6, stroke_fill=(0, 0, 0))
    a = np.asarray(im, np.float32); s = 680 / a.shape[1]
    return cv2.resize(a, (int(a.shape[1] * s), int(a.shape[0] * s)), interpolation=cv2.INTER_AREA)

@lru_cache(maxsize=32)
def product(path, maxw, maxh):
    im = Image.open(path).convert("RGBA"); s = min(maxw / im.width, maxh / im.height)
    im = im.resize((int(im.width * s), int(im.height * s)), Image.LANCZOS)
    return np.asarray(im, np.float32)

@lru_cache(maxsize=8)
def small_label(text):
    f = font("Montserrat-600.ttf", 34); lines = text.split("\n"); w = int(max(tlen(l, f) for l in lines)) + 20
    im = Image.new("RGBA", (w, 46 * len(lines) + 10), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    for i, l in enumerate(lines): d.text(((w - tlen(l, f)) / 2, 4 + i * 46), l, font=f, fill=(255, 255, 255))
    return np.asarray(im, np.float32)

@lru_cache(maxsize=2)
def vs_badge():
    im = Image.new("RGBA", (420, 420), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.line((140, 410, 280, 10), fill=(0, 0, 0, 255), width=7); d.ellipse((150, 150, 270, 270), fill=(10, 10, 10, 255))
    f = font("Montserrat-900.ttf", 52); d.text((210 - tlen("VS", f) / 2 - 2, 178), "VS", font=f, fill=(255, 255, 255))
    return np.asarray(im, np.float32)

def card_frame(c, tl, dur):
    f = np.zeros((H, W, 3), np.uint8); f[:] = BURG
    t = c["type"]
    if t == "pack":
        u = fxlib.ease(tl / 0.12)
        fxlib.blit(f, product(str(c["img"]), 960, 760), W / 2, 1000, (0.88 + 0.12 * u) * (1 + 0.03 * tl / dur), min(1, u * 2))
        return f
    if t == "number":
        title = number_title(c["n"]); ut = fxlib.ease(tl / 0.18)
        fxlib.blit(f, title, W / 2, 456, 1.12 - 0.12 * ut, min(1, ut * 2))
        imgs = c["imgs"]; at = c.get("at", 0.45)
        if len(imgs) == 1:
            u = fxlib.ease((tl - at) / 0.2)
            if u > 0: fxlib.blit(f, product(str(imgs[0][0]), 960, 640), W / 2 - (1 - u) * 120, 1130, 0.92 + 0.08 * u + 0.02 * max(0, tl - at) / dur, min(1, u * 1.6))
        else:
            for k, (p, lab) in enumerate(imgs):
                u = fxlib.ease((tl - at - 0.12 * k) / 0.2)
                if u <= 0: continue
                cx = 262 if k == 0 else 818
                fxlib.blit(f, product(str(p), 500, 430), cx, 1060, 0.9 + 0.1 * u, min(1, u * 1.6))
                if lab: fxlib.blit(f, small_label(lab), cx, 800, 1.0, min(1, u * 1.6))
            uv = fxlib.ease((tl - at - 0.3) / 0.15)
            if uv > 0: fxlib.blit(f, vs_badge(), W / 2, 1060, 0.9 + 0.1 * uv, uv)
        return f
    raise ValueError(t)

# ---------------------------------------------------------------- per-shot FX
def apply_fx(frame, s, tl):
    fx = s.get("fx", {})
    for band in fx.get("inpaint", []):   # remove burned-in source captions
        frame = fxlib.inpaint_band(frame, *band)
    if "zoom" in fx:
        z0, z1 = fx["zoom"]; dur = s["n"] / FPS; z = z0 + (z1 - z0) * min(1.0, tl / max(dur, 1e-3)); cx, cy = fx.get("zc", (W / 2, H / 2))
        M = np.float32([[z, 0, cx - z * cx], [0, z, cy - z * cy]]); frame = cv2.warpAffine(frame, M, (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
    f = frame.astype(np.float32)
    if "nerve" in fx:
        c = fx["nerve"]; pts = lerp_kf(c["kf"], tl + s.get("ss", 0)) if "kf" in c else c["pts"]
        lay, env = nerve_layer(pts, tl, c, seed=s["i"] * 1000)
        if env and c.get("darken", 0.22):
            g = f.mean(axis=2, keepdims=True); f = (f * 0.6 + g * 0.4) * (1 - c.get("darken", 0.22) * env)
        f += lay
    for gl in fx.get("glows", []):
        cc = lerp_kf(gl["kf"], tl + s.get("ss", 0)) if "kf" in gl else gl["c"]; r = gl.get("r", 140)
        m = np.zeros((H, W), np.float32); cv2.circle(m, (int(cc[0]), int(cc[1])), r, 1.0, -1, cv2.LINE_AA); m = cv2.GaussianBlur(m, (0, 0), r * 0.6)
        pulse = 0.7 + 0.3 * math.sin(tl * 2 * math.pi * 2.0); u = fxlib.ease((tl - gl.get("start", 0.08)) / 0.25)
        f += m[..., None] * np.array([255, 45, 5], np.float32) * pulse * u * gl.get("i", 1.0)
    for sp in fx.get("sparks", []):
        f += fxlib.sparks(tl, sp["c"], s["i"] * 77 + int(sp["c"][0]), start=sp.get("start", 0.05), R=sp.get("R", 260))
    if fx.get("x"): f = fxlib.red_x(f, tl, fx.get("x_at", 0.12))
    if fx.get("leak") is not None: f = fxlib.light_leak(f, tl, side=fx["leak"])
    if fx.get("zblur"): f = fxlib.zoom_blur(f, tl)
    if "flash" in fx and tl < 0.1: f = f + (255 - f) * (1 - tl / 0.1) * fx["flash"]
    frame = np.clip(f, 0, 255).astype(np.uint8)
    if "outline" in fx:
        o = fx["outline"]; pts = np.array(o["pts"], np.float32); u = fxlib.ease((tl - o.get("start", 0.2)) / o.get("dur", 0.7))
        if u > 0:
            seg = np.cumsum(np.r_[0, np.hypot(*np.diff(pts, axis=0).T)]); keep = [p for p, d in zip(pts, seg) if d <= seg[-1] * u]
            if len(keep) >= 2:
                arr = np.array(keep, np.int32); cv2.polylines(frame, [arr], False, (255, 255, 255), 14, cv2.LINE_AA)
                for a, b in zip(arr[::2], arr[1::2]): cv2.line(frame, tuple(a), tuple(b), (20, 20, 20), 6, cv2.LINE_AA)
    return frame

# ---------------------------------------------------------------- audio
SR = 48000
def whoosh(d=0.32, seed=1):
    rng = np.random.default_rng(seed); n = int(d * SR); x = rng.standard_normal(n)
    env = np.sin(np.pi * np.linspace(0, 1, n)) ** 2; out = np.zeros(n); y = 0.0
    for i in range(n): a = 0.02 + 0.3 * env[i]; y += a * (x[i] - y); out[i] = y
    return out * env * 0.6
def hit(d=0.5):
    t = np.arange(int(d * SR)) / SR; return np.sin(2 * np.pi * (60 + 50 * np.exp(-t * 20)) * t) * np.exp(-t * 8)
def zap(d=0.35, seed=5):
    rng = np.random.default_rng(seed); n = int(d * SR); t = np.arange(n) / SR
    return (np.diff(np.r_[0, rng.standard_normal(n)]) * 0.2 + (rng.random(n) < 0.015) * rng.standard_normal(n) * 2) * np.exp(-t * 9) * 0.3

def mix_audio(sfx, out_wav):
    import soundfile as sf
    n = int(TOTAL * SR); mix = np.zeros((n, 2))
    vo, _ = sf.read(HERE / "vo.wav"); vo = vo if vo.ndim == 1 else vo.mean(1)
    rms = lambda x: np.sqrt(np.mean(x[np.abs(x) > 1e-4] ** 2))
    vo = vo / rms(vo) * 0.12; L = min(n, len(vo)); mix[:L] += vo[:L, None]
    mpath = P / "build" / "music.wav"
    if mpath.exists():
        m, msr = sf.read(mpath); m = m if m.ndim == 2 else np.stack([m, m], 1)
        if len(m) < n: m = np.concatenate([m, m[: n - len(m)]])
        m = m[:n] / rms(m) * 0.12 * 10 ** (edl2.MUSIC_DB / 20)
        fade = np.ones(n); k = int(2.0 * SR); fade[-k:] = np.linspace(1, 0, k); mix += m * fade[:, None]
    for kind, t, g in sfx:
        x = {"whoosh": whoosh, "hit": hit, "zap": zap}[kind]() * g; s0 = int(t * SR); e = min(n, s0 + len(x))
        if s0 < n: mix[s0:e] += x[: e - s0, None]
    pk = np.abs(mix).max(); mix = mix / pk * 0.89 if pk > 0.89 else mix
    sf.write(out_wav, mix.astype(np.float32), SR)

# ---------------------------------------------------------------- render
def render(only=None, preview=False, out=None):
    tl = build_timeline(edl2.SHOTS)
    sel = [s for s in tl if only is None or only[0] <= s["row"] <= only[1]]
    with ThreadPoolExecutor(3) as ex: bases = dict(zip([s["i"] for s in sel], ex.map(base_clip, sel)))
    chunks = edl2.caption_chunks(timing)
    sfx = [(k, s["t0"] + dt, g) for s in tl for (k, dt, g) in s.get("sfx", [])]
    wav = P / "build" / "mix2.wav"; mix_audio(sfx, wav)
    f0, f1 = sel[0]["f0"], sel[-1]["f1"]
    out = Path(out) if out else P / "out" / ("preview2.mp4" if only else "ComfortWear_Sciatica_V2.mp4")
    enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                            "-ss", f"{f0 / FPS:.3f}", "-t", f"{(f1 - f0) / FPS:.3f}", "-i", str(wav),
                            "-c:v", "libx264", "-preset", "veryfast" if preview else "medium", "-crf", "21" if preview else "17",
                            "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", str(out)], stdin=subprocess.PIPE)
    for s in sel:
        frames = read_frames(bases[s["i"]], s["n"]) if bases[s["i"]] else (None for _ in range(s["n"]))
        for k, fr in enumerate(frames):
            tloc = k / FPS; gt = (s["f0"] + k) / FPS
            fr = card_frame(s["card"], tloc, s["n"] / FPS) if "card" in s else apply_fx(fr, s, tloc)
            draw_tags(fr, s.get("tags", []), tloc)
            if not s.get("nocap"):
                for c in chunks:
                    if c["s"] - 0.02 <= gt < c["e"]:
                        fxlib.blit(fr, np.asarray(captions.caption(c["text"]), np.float32), W / 2, s.get("cap_y", 1275)); break
            enc.stdin.write(np.ascontiguousarray(fr).tobytes())
        print(f"row {s['row']:02d} shot {s['i']:03d} {s['n']}f", flush=True)
    enc.stdin.close(); enc.wait(); print("wrote", out)

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--only"); ap.add_argument("--preview", action="store_true"); ap.add_argument("--out")
    a = ap.parse_args(); render(tuple(map(int, a.only.split("-"))) if a.only else None, a.preview, a.out)
