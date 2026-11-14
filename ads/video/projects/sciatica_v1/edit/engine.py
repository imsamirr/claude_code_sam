"""Edit engine: EDL (edl.py) + VO timing -> 1080x1920 30fps MP4 with captions, cards, FX, SFX, music.

    python edit/engine.py [--only 1-12] [--preview]      # --only renders a row range (fast iteration)
Stages: 1) base shot clips via ffmpeg (trim/cover-crop/speed/key)  2) python compositor per frame
(zoom, nerve lightning, glows, labels, cards, captions)  3) audio mix (VO + SFX + pad) and mux.
"""
import argparse, io, json, math, random, subprocess, sys, hashlib
from concurrent.futures import ThreadPoolExecutor
from functools import lru_cache
from pathlib import Path
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = Path(__file__).resolve().parent; P = HERE.parent
sys.path.insert(0, str(HERE))
import assets, edl
FONTS = Path("/home/user/claude_code_sam/ads/video/fonts")
FPS, W, H = 30, 1080, 1920
BUILD = P / "build" / "shots"; BUILD.mkdir(parents=True, exist_ok=True)
BLUE, BURG, RED = (30, 111, 217), (116, 61, 60), (232, 20, 27)
PACK_BG = (224, 222, 223)

def font(name, size): return ImageFont.truetype(str(FONTS / name), size)

# ---------------------------------------------------------------- timeline
timing = {r["row"]: r for r in json.load(open(HERE / "vo_timing.json"))}
END_PAD = 3.4  # hold end card after VO
TOTAL = max(r["end"] for r in timing.values()) + END_PAD

def shot_start(s):
    r = timing[s["row"]]
    if s.get("w", 0) == 0: t = r["start"] if s["row"] != 1 else 0.0
    else: t = r["words"][s["w"]]["s"] - 0.04   # cut a hair before the word
    return t + s.get("dt", 0.0)

def build_timeline(shots):
    out = []
    for i, s in enumerate(shots):
        t0 = shot_start(s); t1 = shot_start(shots[i + 1]) if i + 1 < len(shots) else TOTAL
        f0, f1 = round(t0 * FPS), round(t1 * FPS)
        if f1 <= f0: raise ValueError(f"shot {i} row {s['row']} w{s.get('w')} has no duration")
        out.append({**s, "i": i, "f0": f0, "f1": f1, "n": f1 - f0, "t0": f0 / FPS})
    return out

# ---------------------------------------------------------------- stage 1: base clips
def base_clip(s):
    if "src" not in s: return None
    fx = s.get("fx", {}); src = assets.path(s["src"])
    key = hashlib.md5(json.dumps([src, s.get("ss", 0), s["n"], {k: fx.get(k) for k in ("fx", "fy", "z", "speed", "bw", "key", "hflip", "grade")}], sort_keys=True).encode()).hexdigest()[:12]
    out = BUILD / f"{key}.mp4"
    if out.exists(): return out
    sp = fx.get("speed", 1.0); z = fx.get("z", 1.0)
    if fx.get("key"):  # green-screen 3D render keyed over a flat background
        kc = fx["key"]; bg = kc.get("bg", "0xF1F4F8"); sc = kc.get("scale", 1.0)
        vf = (f"[0:v]fps={FPS},setpts=PTS/{sp},chromakey=0x00FF00:0.30:0.10,scale={int(W*sc)}:-2[k];"
              f"color=c={bg}:s={W}x{H}:r={FPS}[bg];[bg][k]overlay=(W-w)/2:(H-h)/2+{kc.get('dy',0)}:shortest=1,format=yuv420p[v]")
        cmd = ["ffmpeg", "-v", "error", "-y", "-ss", str(s.get("ss", 0)), "-i", src, "-filter_complex", vf, "-map", "[v]"]
    else:
        chain = [f"setpts=PTS/{sp}", f"fps={FPS}",
                 f"scale=w='if(gt(a,{W}/{H}),-2,{int(W*z)})':h='if(gt(a,{W}/{H}),{int(H*z)},-2)'",
                 f"crop={W}:{H}:(iw-{W})*{fx.get('fx',0.5)}:(ih-{H})*{fx.get('fy',0.5)}"]
        if fx.get("hflip"): chain.append("hflip")
        if fx.get("bw"): chain.append("hue=s=0,eq=contrast=1.08")
        if fx.get("grade"): chain.append(fx["grade"])
        chain += ["tpad=stop_mode=clone:stop_duration=30", "format=yuv420p"]
        cmd = ["ffmpeg", "-v", "error", "-y", "-ss", str(s.get("ss", 0)), "-i", src, "-vf", ",".join(chain)]
    cmd += ["-frames:v", str(s["n"]), "-an", "-c:v", "libx264", "-preset", "veryfast", "-crf", "14", str(out)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode or not out.exists(): raise RuntimeError(f"row {s['row']} src {s['src']}: {r.stderr[-400:]}")
    return out

def read_frames(path, n):
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-i", str(path), "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE)
    last = None
    for _ in range(n):
        b = p.stdout.read(W * H * 3)
        if len(b) == W * H * 3: last = np.frombuffer(b, np.uint8).reshape(H, W, 3)
        yield last.copy() if last is not None else np.zeros((H, W, 3), np.uint8)
    p.stdout.close(); p.wait()

# ---------------------------------------------------------------- helpers
def ease(x): x = min(max(x, 0.0), 1.0); return 1 - (1 - x) ** 3
def lerp_kf(kf, t):
    """kf: [(t, value)] where value is a point or list of points; linear interpolation."""
    if t <= kf[0][0]: return kf[0][1]
    for (ta, va), (tb, vb) in zip(kf, kf[1:]):
        if t <= tb:
            u = (t - ta) / (tb - ta)
            return [(a[0] + (b[0] - a[0]) * u, a[1] + (b[1] - a[1]) * u) for a, b in zip(va, vb)] if isinstance(va[0], (list, tuple)) else \
                   (va[0] + (vb[0] - va[0]) * u, va[1] + (vb[1] - va[1]) * u)
    return kf[-1][1]

def paste(frame, rgba, x, y, alpha=1.0):
    """Alpha-composite an RGBA PIL image (or float array) onto frame at (x, y)."""
    a = np.asarray(rgba, np.float32) if not isinstance(rgba, np.ndarray) else rgba
    h, w = a.shape[:2]; x0, y0 = max(0, x), max(0, y); x1, y1 = min(W, x + w), min(H, y + h)
    if x1 <= x0 or y1 <= y0: return
    sub = a[y0 - y:y1 - y, x0 - x:x1 - x]; al = sub[..., 3:4] / 255.0 * alpha
    reg = frame[y0:y1, x0:x1].astype(np.float32)
    frame[y0:y1, x0:x1] = (sub[..., :3] * al + reg * (1 - al)).astype(np.uint8)

def rounded_box(text_lines, fnt, fg, bg, pad=(26, 14), radius=18, line_gap=6, stroke=0, stroke_fill=None, shadow=True):
    d0 = ImageDraw.Draw(Image.new("RGB", (1, 1)))
    sizes = [d0.textbbox((0, 0), l, font=fnt, stroke_width=stroke) for l in text_lines]
    lh = max(b[3] - b[1] for b in sizes) if sizes else 0
    asc = fnt.getmetrics()[0]
    w = max(b[2] - b[0] for b in sizes) + 2 * pad[0]; hgt = len(text_lines) * (asc + 4) + (len(text_lines) - 1) * line_gap + 2 * pad[1]
    im = Image.new("RGBA", (w + 16, hgt + 16), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    if shadow: d.rounded_rectangle((10, 12, w + 8, hgt + 10), radius, fill=(0, 0, 0, 70))
    if bg: d.rounded_rectangle((4, 4, w + 4, hgt + 4), radius, fill=bg)
    if shadow: im = im.filter(ImageFilter.GaussianBlur(0)) if False else im
    y = 4 + pad[1]
    for l, b in zip(text_lines, sizes):
        tw = b[2] - b[0]; d.text((4 + (w - tw) / 2 - b[0], y), l, font=fnt, fill=fg, stroke_width=stroke, stroke_fill=stroke_fill)
        y += asc + 4 + line_gap
    return im

# ---------------------------------------------------------------- captions
def wrap(words, maxc=17):
    lines, cur = [], ""
    for w in words:
        if cur and len(cur) + 1 + len(w) > maxc: lines.append(cur); cur = w
        else: cur = (cur + " " + w).strip()
    if cur: lines.append(cur)
    return lines

def caption_chunks():
    """Chunk VO words into 2-6 word captions, max 2 lines, breaking on punctuation."""
    chunks = []
    for r in timing.values():
        cur = []
        ws = r["words"]
        for i, w in enumerate(ws):
            cur.append(w)
            punct = w["w"][-1] in ".,?!:;"
            nxt_len = len(" ".join(x["w"] for x in cur)) + (len(ws[i + 1]["w"]) + 1 if i + 1 < len(ws) else 0)
            if punct and len(cur) >= 2 or len(cur) >= 6 or nxt_len > 32 or i == len(ws) - 1:
                if len(cur) == 1 and chunks and chunks[-1]["row"] == r["row"] and not punct and False: pass
                chunks.append({"row": r["row"], "s": cur[0]["s"], "e": cur[-1]["e"], "text": " ".join(x["w"] for x in cur)})
                cur = []
    for a, b in zip(chunks, chunks[1:]):
        a["e"] = min(b["s"], a["e"] + 0.35) if b["s"] - a["e"] < 0.8 else a["e"] + 0.3
    chunks[-1]["e"] += 0.4
    return chunks

CAP_FONT = font("TikTokSans-700.ttf", 50)
@lru_cache(maxsize=512)
def caption_img(text):
    t = text.rstrip(".,;:")
    return rounded_box(wrap(t.split()), CAP_FONT, (0, 0, 0), (255, 255, 255, 255), pad=(22, 10), radius=16, line_gap=2)

# ---------------------------------------------------------------- overlays (tags / labels)
TAG_STYLES = {
    "hook": (font("Montserrat-900.ttf", 70), (255, 255, 255), RED + (255,)),
    "white": (font("Montserrat-900.ttf", 58), (17, 17, 17), (255, 255, 255, 255)),
    "blue": (font("Montserrat-800.ttf", 56), (255, 255, 255), BLUE + (255,)),
    "burg": (font("Montserrat-900.ttf", 56), (255, 255, 255), BURG + (255,)),
    "dark": (font("Montserrat-900.ttf", 56), (255, 255, 255), (20, 20, 22, 235)),
    "small": (font("Inter-600.ttf", 34), (255, 255, 255), (0, 0, 0, 120)),
}
@lru_cache(maxsize=256)
def tag_img(text, style):
    f, fg, bg = TAG_STYLES[style]
    return rounded_box(text.split("\n"), f, fg, bg, pad=(30, 16) if style != "small" else (14, 6), radius=14 if style != "small" else 8, line_gap=4, shadow=style != "small")

def draw_tags(frame, tags, tl, gt):
    for tg in tags:
        t0 = tg.get("t0", 0.0); t1 = tg.get("t1", 99)
        tt = tl if tg.get("local", True) else gt
        if not (t0 <= tt < t1): continue
        im = tag_img(tg["text"], tg.get("style", "white")); a = np.asarray(im, np.float32)
        u = ease((tt - t0) / 0.18)
        sc = 0.86 + 0.14 * u if tg.get("pop", True) else 1.0
        if sc != 1.0:
            a = cv2.resize(a, (max(1, int(a.shape[1] * sc)), max(1, int(a.shape[0] * sc))), interpolation=cv2.INTER_LINEAR)
        x = int(tg.get("x", W / 2) - a.shape[1] / 2) if tg.get("align", "c") == "c" else int(tg["x"])
        y = int(tg.get("y", 360) - a.shape[0] / 2 + (1 - u) * 18)
        paste(frame, a, x, y, alpha=min(1.0, u * 1.4))

# ---------------------------------------------------------------- FX: sciatic lightning + glows
def bolt(p0, p1, rng, rough=0.22, depth=6):
    pts = [p0, p1]
    for d in range(depth):
        new = [pts[0]]
        for a, b in zip(pts, pts[1:]):
            mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
            L = math.hypot(b[0] - a[0], b[1] - a[1]); nx, ny = -(b[1] - a[1]) / (L + 1e-6), (b[0] - a[0]) / (L + 1e-6)
            off = rng.uniform(-1, 1) * L * rough
            new += [(mx + nx * off, my + ny * off), b]
        pts = new
    return pts

def nerve_layer(path_pts, tl, cfg, seed):
    """Additive RGB float layer: soft red 'inflamed nerve' band + flickering lightning along the path."""
    lay = np.zeros((H, W, 3), np.float32)
    start = cfg.get("start", 0.12); env = ease((tl - start) / 0.12) if tl >= start else 0.0
    if env <= 0: return lay, 0.0
    flick = 0.78 + 0.22 * math.sin(tl * 37) * math.sin(tl * 13 + 1)
    pts = np.array(path_pts, np.int32)
    band = np.zeros((H, W), np.float32)
    cv2.polylines(band, [pts], False, 1.0, cfg.get("band", 70), cv2.LINE_AA)
    band = cv2.GaussianBlur(band, (0, 0), 28)
    rng = random.Random(seed + int(tl * FPS / 2))   # re-branch every 2 frames
    core = np.zeros((H, W), np.float32); glow = np.zeros((H, W), np.float32)
    for a, b in zip(path_pts, path_pts[1:]):
        bp = np.array(bolt(a, b, rng), np.int32)
        cv2.polylines(core, [bp], False, 1.0, 3, cv2.LINE_AA); cv2.polylines(glow, [bp], False, 1.0, 10, cv2.LINE_AA)
        for _ in range(rng.randint(1, 2)):   # side branches
            k = rng.randint(2, len(bp) - 3); q = bp[k]
            ang = rng.uniform(-1.2, 1.2) + math.atan2(b[1] - a[1], b[0] - a[0])
            L = rng.uniform(50, 130); br = np.array(bolt((float(q[0]), float(q[1])), (q[0] + math.cos(ang) * L, q[1] + math.sin(ang) * L), rng, 0.3, 4), np.int32)
            cv2.polylines(core, [br], False, 0.7, 2, cv2.LINE_AA); cv2.polylines(glow, [br], False, 0.7, 6, cv2.LINE_AA)
    glow = cv2.GaussianBlur(glow, (0, 0), 9); halo = cv2.GaussianBlur(glow, (0, 0), 30)
    # hot spot at the root (lumbar)
    hs = np.zeros((H, W), np.float32); r = cfg.get("root_r", 120)
    cv2.circle(hs, (int(path_pts[0][0]), int(path_pts[0][1])), r, 1.0, -1, cv2.LINE_AA); hs = cv2.GaussianBlur(hs, (0, 0), r * 0.55)
    pulse = 0.75 + 0.25 * math.sin(tl * 2 * math.pi * 2.2)
    i = env * cfg.get("intensity", 1.0)
    lay += band[..., None] * np.array([150, 18, 0], np.float32) * 0.85 * i
    lay += hs[..., None] * np.array([255, 60, 10], np.float32) * pulse * i
    lay += halo[..., None] * np.array([255, 40, 0], np.float32) * 1.6 * flick * i
    lay += glow[..., None] * np.array([255, 120, 30], np.float32) * 1.4 * flick * i
    lay += core[..., None] * np.array([255, 240, 215], np.float32) * flick * i
    return lay, env

def apply_fx(frame, s, tl, gt):
    fx = s.get("fx", {})
    if "zoom" in fx:   # push-in (or out) around a centre point
        z0, z1 = fx["zoom"]; dur = s["n"] / FPS
        z = z0 + (z1 - z0) * min(1.0, tl / max(dur, 1e-3)); cx, cy = fx.get("zc", (W / 2, H / 2))
        M = np.float32([[z, 0, cx - z * cx], [0, z, cy - z * cy]])
        frame = cv2.warpAffine(frame, M, (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
    f = frame.astype(np.float32)
    if "nerve" in fx:
        c = fx["nerve"]; pts = lerp_kf(c["kf"], tl + s.get("ss", 0)) if "kf" in c else c["pts"]
        lay, env = nerve_layer(pts, tl, c, seed=s["i"] * 1000)
        if c.get("darken", 0.25) and env:   # dim + desaturate the plate so the nerve reads
            g = f.mean(axis=2, keepdims=True); f = (f * 0.55 + g * 0.45) * (1 - c.get("darken", 0.25) * env)
            f[..., 0] *= 1 + 0.10 * env
        f += lay
    for gl in fx.get("glows", []):
        c = lerp_kf(gl["kf"], tl + s.get("ss", 0)) if "kf" in gl else gl["c"]
        m = np.zeros((H, W), np.float32); r = gl.get("r", 140)
        cv2.circle(m, (int(c[0]), int(c[1])), r, 1.0, -1, cv2.LINE_AA); m = cv2.GaussianBlur(m, (0, 0), r * 0.6)
        pulse = 0.7 + 0.3 * math.sin(tl * 2 * math.pi * 2.0); u = ease((tl - gl.get("start", 0.1)) / 0.25)
        f += m[..., None] * np.array([255, 45, 5], np.float32) * pulse * u * gl.get("i", 1.0)
    if fx.get("vignette"):
        yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
        v = ((xx - W / 2) / (W * 0.75)) ** 2 + ((yy - H / 2) / (H * 0.7)) ** 2
        f *= (1 - np.clip(v, 0, 1) * fx["vignette"])[..., None]
    if "flash" in fx and tl < 0.1:
        f = f + (255 - f) * (1 - tl / 0.1) * fx["flash"]
    frame = np.clip(f, 0, 255).astype(np.uint8)
    if "outline" in fx:   # progressive blue stroke (e.g. toe-box outline)
        o = fx["outline"]; pts = np.array(o["pts"], np.float32); u = ease((tl - o.get("start", 0.2)) / o.get("dur", 0.7))
        if u > 0:
            seg = np.cumsum(np.r_[0, np.hypot(*np.diff(pts, axis=0).T)]); L = seg[-1] * u
            keep = [p for p, d in zip(pts, seg) if d <= L]
            if len(keep) >= 2:
                arr = np.array(keep, np.int32)
                cv2.polylines(frame, [arr], False, (255, 255, 255), 16, cv2.LINE_AA)
                cv2.polylines(frame, [arr], False, BLUE, 9, cv2.LINE_AA)
    return frame

# ---------------------------------------------------------------- cards (full-frame graphics)
@lru_cache(maxsize=64)
def load_rgba(path, maxw, maxh):
    im = Image.open(path).convert("RGBA"); im.thumbnail((maxw, maxh), Image.LANCZOS); return im

def feather(a, px=60):
    """fade an opaque photo's edges into the card background"""
    a = a.copy(); h, w = a.shape[:2]
    if a.shape[2] == 3: a = np.dstack([a, np.full((h, w), 255, np.float32)])
    yy, xx = np.mgrid[0:h, 0:w]; d = np.minimum.reduce([xx, yy, w - 1 - xx, h - 1 - yy]).astype(np.float32)
    a[..., 3] *= np.clip(d / px, 0, 1); return a

def text_stroked(text, fnt, fill, stroke=8, stroke_fill=(0, 0, 0), shadow=10):
    d0 = ImageDraw.Draw(Image.new("RGB", (1, 1))); b = d0.textbbox((0, 0), text, font=fnt, stroke_width=stroke)
    w, h = b[2] - b[0] + 40, b[3] - b[1] + 40
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    if shadow:
        sh = Image.new("RGBA", (w, h), (0, 0, 0, 0)); ImageDraw.Draw(sh).text((20 - b[0] + shadow * 0.6, 20 - b[1] + shadow), text, font=fnt, fill=(0, 0, 0, 160), stroke_width=stroke, stroke_fill=(0, 0, 0, 160))
        im = Image.alpha_composite(im, sh.filter(ImageFilter.GaussianBlur(4)))
    ImageDraw.Draw(im).text((20 - b[0], 20 - b[1]), text, font=fnt, fill=fill, stroke_width=stroke, stroke_fill=stroke_fill)
    return im

def card_frame(c, tl, dur):
    t = c["type"]
    if t in ("number", "pack", "criteria", "fit", "cta_bg"):
        bgc = BURG if t == "number" else PACK_BG
        f = np.zeros((H, W, 3), np.uint8); f[:] = bgc
        if t == "number":   # subtle radial light
            yy, xx = np.mgrid[0:H, 0:W].astype(np.float32); v = np.clip(1 - (((xx - W / 2) / W) ** 2 + ((yy - H * 0.55) / H) ** 2) * 1.6, 0, 1)
            f = np.clip(f.astype(np.float32) * (0.82 + 0.3 * v[..., None]), 0, 255).astype(np.uint8)
    if t == "number":
        title = text_stroked(f"NUMBER {c['n']}", font("AlfaSlabOne-400.ttf", 128), (255, 0, 0), 9)
        u = ease(tl / 0.16); a = np.asarray(title, np.float32)
        sc = 1.25 - 0.25 * u; a = cv2.resize(a, (int(a.shape[1] * sc), int(a.shape[0] * sc)))
        paste(f, a, int(W / 2 - a.shape[1] / 2), int(430 - a.shape[0] / 2), alpha=u)
        sub = tag_img(c["brand"], "white"); paste(f, np.asarray(sub, np.float32), int(W / 2 - sub.width / 2), 560, alpha=ease((tl - 0.12) / 0.15))
        imgs = c["imgs"]; n = len(imgs)
        for k, (p, lab) in enumerate(imgs):
            uu = ease((tl - 0.22 - 0.1 * k) / 0.22)
            if uu <= 0: continue
            maxw = 940 if n == 1 else 480
            im = load_rgba(str(p), maxw, 760 if n == 1 else 560); a = np.asarray(im, np.float32)
            sc = 0.8 + 0.2 * uu + 0.03 * min(1, tl / dur); a = cv2.resize(a, (int(a.shape[1] * sc), int(a.shape[0] * sc)))
            cx = W / 2 if n == 1 else (W / 4 + 10 if k == 0 else 3 * W / 4 - 10)
            cy = 1150 + (1 - uu) * 60
            paste(f, a, int(cx - a.shape[1] / 2), int(cy - a.shape[0] / 2), alpha=uu)
            if lab:
                li = tag_img(lab, "small"); paste(f, np.asarray(li, np.float32), int(cx - li.width / 2), int(cy + 290), alpha=uu)
        if n == 2 and tl > 0.5:
            vs = tag_img("VS", "dark"); paste(f, np.asarray(vs, np.float32), int(W / 2 - vs.width / 2), int(1150 - vs.height / 2))
        return f
    if t == "pack":
        im = load_rgba(str(c["img"]), 1000, 1000); a = feather(np.asarray(im, np.float32)) if c.get("feather") else np.asarray(im, np.float32)
        z = 1.0 + 0.05 * tl / dur; a = cv2.resize(a, (int(a.shape[1] * z), int(a.shape[0] * z)))
        paste(f, a, int(W / 2 - a.shape[1] / 2), int(1010 - a.shape[0] / 2))
        lab = tag_img(c["brand"], "dark"); paste(f, np.asarray(lab, np.float32), int(W / 2 - lab.width / 2), 330, alpha=ease(tl / 0.12))
        return f
    if t == "criteria":
        hd = tag_img("3 THINGS TO CHECK", "burg"); paste(f, np.asarray(hd, np.float32), int(W / 2 - hd.width / 2), 300, alpha=ease(tl / 0.15))
        for k, item in enumerate(["FEEL IN MOTION", "FIT", "EVERYDAY COMFORT"]):
            uu = ease((tl - c.get("at", [0.5, 0.9, 1.3])[k]) / 0.2)
            if uu <= 0: continue
            num = tag_img(str(k + 1), "dark"); it = tag_img(item, "white")
            y = 620 + k * 230 + int((1 - uu) * 30)
            paste(f, np.asarray(num, np.float32), 150, y, alpha=uu); paste(f, np.asarray(it, np.float32), 150 + num.width + 20, y, alpha=uu)
        return f
    if t == "fit":   # neutral forefoot-fit illustration (generic outlines, no brands)
        img = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
        def foot(cx, cy, s=1.0):
            pts = [(cx + x * s, cy + y * s) for x, y in [(-95, 330), (-120, 120), (-118, -60), (-100, -200), (-70, -290), (-20, -330), (40, -320), (95, -270), (120, -150), (115, 60), (90, 330)]]
            d.line(pts + [pts[0]], fill=(60, 60, 60), width=7, joint="curve")
            for k, (tx, ty, r) in enumerate([(-65, -300, 38), (-5, -330, 30), (45, -318, 27), (85, -285, 24), (112, -240, 21)]):
                d.ellipse((cx + tx * s - r, cy + ty * s - r, cx + tx * s + r, cy + ty * s + r), outline=(60, 60, 60), width=6)
        foot(300, 1080); foot(780, 1080)
        u = ease((tl - 0.3) / 0.6)
        d.rounded_rectangle((300 - 165, 1080 - 400, 300 + 165, 1080 + 380), 150, outline=BLUE + (255,), width=10)
        nar = [(780 - 120, 1080 + 380), (780 - 135, 1080 - 150), (780 - 60, 1080 - 380), (780 + 70, 1080 - 370), (780 + 110, 1080 - 160), (780 + 120, 1080 + 380)]
        d.line(nar, fill=(200, 40, 30, 255), width=10, joint="curve")
        a = np.asarray(img, np.float32); paste(f, a, 0, 0, alpha=u if u > 0 else 0.0)
        for txt, x, st in (("ROOM TO MOVE", 300, "blue"), ("CROWDED", 780, "dark")):
            ti = tag_img(txt, st); paste(f, np.asarray(ti, np.float32), int(x - ti.width / 2), 1530, alpha=ease((tl - 0.6) / 0.3))
        hd = tag_img("ROOM TO MOVE?", "white"); paste(f, np.asarray(hd, np.float32), int(W / 2 - hd.width / 2), 300)
        sm = tag_img("Fit illustration", "small"); paste(f, np.asarray(sm, np.float32), 40, 1780)
        return f
    raise ValueError(t)

# ---------------------------------------------------------------- audio
SR = 48000
def sfx_whoosh(d=0.38, seed=1):
    rng = np.random.default_rng(seed); n = int(d * SR); x = rng.standard_normal(n)
    t = np.linspace(0, 1, n); env = np.sin(np.pi * t) ** 2
    out = np.zeros(n); y = 0.0; a_lo, a_hi = 0.02, 0.35
    for i in range(n):   # swept one-pole lowpass
        a = a_lo + (a_hi - a_lo) * env[i]; y += a * (x[i] - y); out[i] = y
    return out * env * 0.5
def sfx_hit(d=0.6):
    t = np.arange(int(d * SR)) / SR
    return (np.sin(2 * np.pi * (55 + 40 * np.exp(-t * 18)) * t) * np.exp(-t * 7) * 0.9 + np.random.default_rng(3).standard_normal(len(t)) * np.exp(-t * 60) * 0.25)
def sfx_zap(d=0.5, seed=5):
    rng = np.random.default_rng(seed); n = int(d * SR); x = rng.standard_normal(n)
    x = np.diff(np.r_[0, x]); t = np.arange(n) / SR
    crackle = (rng.random(n) < 0.02).astype(float) * rng.standard_normal(n) * 3
    return (x * 0.25 + crackle) * np.exp(-t * 6) * 0.35
def pad_music(total):
    """Quiet restrained pad: slow chord bed (temp bed until licensed music is chosen)."""
    t = np.arange(int(total * SR)) / SR; out = np.zeros_like(t)
    chords = [[261.6, 329.6, 392.0, 493.9], [220.0, 261.6, 329.6, 392.0], [174.6, 220.0, 261.6, 329.6], [196.0, 246.9, 293.7, 392.0]]
    L = 4.0
    for k in range(int(total / L) + 1):
        c = chords[k % 4]; s0 = int(k * L * SR); s1 = min(len(t), int((k + 1) * L * SR + 1.0 * SR))
        if s0 >= len(t): break
        tt = t[s0:s1] - k * L; env = np.minimum(1, tt / 1.2) * np.minimum(1, np.maximum(0, (L + 1.0 - tt) / 1.2))
        for fq in c:
            out[s0:s1] += (np.sin(2 * np.pi * fq / 2 * tt) * 0.6 + np.sin(2 * np.pi * fq * tt) * 0.25) * env
    k = np.exp(-np.arange(400) / 80); k /= k.sum(); out = np.convolve(out, k, "same")
    return out / np.abs(out).max()

def mix_audio(tl, sfx_events, out_wav):
    import soundfile as sf
    vo, sr = sf.read(HERE / "vo.wav"); vo = vo if vo.ndim == 1 else vo.mean(1)
    n = int(TOTAL * SR); mix = np.zeros(n)
    vo = vo / (np.sqrt(np.mean(vo[vo != 0] ** 2)) + 1e-9) * 0.1   # ~-20 dBFS rms
    mix[:min(n, len(vo))] += vo[:n]
    m = pad_music(TOTAL) * 0.022
    lift = timing[30]["start"]; m[int(lift * SR):] *= 1.35
    fade = np.ones(n); fade[-int(1.5 * SR):] = np.linspace(1, 0, int(1.5 * SR)); mix += m[:n] * fade
    for kind, t in sfx_events:
        x = {"whoosh": sfx_whoosh, "hit": sfx_hit, "zap": sfx_zap}[kind]() * {"whoosh": 0.22, "hit": 0.35, "zap": 0.18}[kind]
        s0 = int(t * SR); e = min(n, s0 + len(x)); mix[s0:e] += x[:e - s0]
    peak = np.abs(mix).max(); mix = mix / peak * 0.89 if peak > 0.89 else mix
    sf.write(out_wav, mix.astype(np.float32), SR)

# ---------------------------------------------------------------- render
def render(only=None, out=None, preview=False):
    tl = build_timeline(edl.SHOTS)
    sel = [s for s in tl if only is None or only[0] <= s["row"] <= only[1]]
    with ThreadPoolExecutor(3) as ex: bases = dict(zip([s["i"] for s in sel], ex.map(base_clip, sel)))
    chunks = caption_chunks()
    f0, f1 = sel[0]["f0"], sel[-1]["f1"]
    out = out or P / "out" / ("preview.mp4" if only else "ComfortWear_Sciatica_V1.mp4")
    wav = P / "build" / "mix.wav"
    sfx = [(e[0], e[1]) for e in getattr(edl, "SFX", [])]
    for s in tl:
        for kind, dt in s.get("sfx", []): sfx.append((kind, s["t0"] + dt))
    mix_audio(tl, sfx, wav)
    enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                            "-ss", f"{f0 / FPS:.3f}", "-t", f"{(f1 - f0) / FPS:.3f}", "-i", str(wav),
                            "-c:v", "libx264", "-preset", "veryfast" if preview else "medium", "-crf", "20" if preview else "17", "-pix_fmt", "yuv420p",
                            "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", str(out)], stdin=subprocess.PIPE)
    for s in sel:
        frames = read_frames(bases[s["i"]], s["n"]) if bases[s["i"]] else (None for _ in range(s["n"]))
        for k, fr in enumerate(frames):
            tloc = k / FPS; gt = (s["f0"] + k) / FPS
            fr = card_frame(s["card"], tloc, s["n"] / FPS) if "card" in s else apply_fx(fr, s, tloc, gt)
            draw_tags(fr, s.get("tags", []), tloc, gt)
            if not s.get("nocap"):
                for c in chunks:
                    if c["s"] - 0.02 <= gt < c["e"]:
                        im = caption_img(c["text"]); cy = s.get("cap_y", 1290)
                        paste(fr, np.asarray(im, np.float32), int(W / 2 - im.width / 2), int(cy - im.height / 2)); break
            enc.stdin.write(np.ascontiguousarray(fr).tobytes())
        print(f"row {s['row']:02d} shot {s['i']:03d} {s['n']}f", flush=True)
    enc.stdin.close(); enc.wait(); print("wrote", out)

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--only"); ap.add_argument("--preview", action="store_true"); a = ap.parse_args()
    only = tuple(map(int, a.only.split("-"))) if a.only else None
    render(only, preview=a.preview)
