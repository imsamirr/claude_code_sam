"""Shared FX helpers for engine2."""
import math, random
import numpy as np, cv2
W, H = 1080, 1920

def ease(x): x = min(max(x, 0.0), 1.0); return 1 - (1 - x) ** 3

def text_mask(band, mode="auto"):
    """mask of burned-in caption glyphs (white/yellow/cyan fill + dark stroke) inside a band image (RGB uint8)."""
    r, g, b = [band[..., i].astype(int) for i in range(3)]
    mx, mn = band.max(axis=2).astype(int), band.min(axis=2).astype(int)
    white = (mn > 205) & (mx - mn < 40)
    yellow = (r > 200) & (g > 170) & (b < 110)
    cyan = (g > 170) & (b > 170) & (r < 140)
    m = (white | yellow | cyan).astype(np.uint8)
    # keep only text-like blobs (small, many) - drop big flat white areas
    n, lab, st, _ = cv2.connectedComponentsWithStats(m, 8)
    keep = np.zeros(n, bool)
    for i in range(1, n):
        x, y, w, h, a = st[i]
        if 4 < h < 90 and w < 260 and a < 6000: keep[i] = True
    m = keep[lab].astype(np.uint8)
    return cv2.dilate(m, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (13, 13)))

def inpaint_band(frame, y0, y1, x0=0, x1=W):
    band = frame[y0:y1, x0:x1]
    m = text_mask(band)
    if m.sum() == 0: return frame
    small = cv2.resize(band, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    ms = cv2.resize(m, (small.shape[1], small.shape[0]), interpolation=cv2.INTER_NEAREST)
    fixed = cv2.inpaint(small, ms, 6, cv2.INPAINT_TELEA)
    fixed = cv2.resize(fixed, (band.shape[1], band.shape[0]), interpolation=cv2.INTER_LINEAR)
    mm = cv2.GaussianBlur(m.astype(np.float32), (0, 0), 3)[..., None]
    frame[y0:y1, x0:x1] = (fixed * mm + band * (1 - mm)).astype(np.uint8)
    return frame

def blit(canvas, rgba, cx, cy, scale=1.0, alpha=1.0, rot=0.0):
    """Sub-pixel accurate composite of RGBA (float32 HxWx4) centred at (cx, cy) with scale/rotation."""
    h, w = rgba.shape[:2]
    M = cv2.getRotationMatrix2D((w / 2, h / 2), rot, scale)
    M[0, 2] += cx - w / 2; M[1, 2] += cy - h / 2
    x0 = int(max(0, math.floor(cx - w * scale / 2 - 4))); x1 = int(min(W, math.ceil(cx + w * scale / 2 + 4)))
    y0 = int(max(0, math.floor(cy - h * scale / 2 - 4))); y1 = int(min(H, math.ceil(cy + h * scale / 2 + 4)))
    if x1 <= x0 or y1 <= y0: return
    M2 = M.copy(); M2[0, 2] -= x0; M2[1, 2] -= y0
    warped = cv2.warpAffine(rgba, M2, (x1 - x0, y1 - y0), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=(0, 0, 0, 0))
    a = warped[..., 3:4] / 255.0 * alpha
    reg = canvas[y0:y1, x0:x1].astype(np.float32)
    canvas[y0:y1, x0:x1] = np.clip(warped[..., :3] * a + reg * (1 - a), 0, 255).astype(np.uint8)

def sparks(tl, c, seed, n=46, start=0.0, dur=0.9, R=260):
    """additive spark burst layer (float HxWx3) around point c: hot core + streaking particles."""
    lay = np.zeros((H, W, 3), np.float32); u = tl - start
    if u < 0: return lay
    rng = random.Random(seed); m = np.zeros((H, W), np.float32); core = np.zeros((H, W), np.float32)
    for i in range(n):
        ang = rng.uniform(0, 2 * math.pi); sp = rng.uniform(0.4, 1.0); life = rng.uniform(0.35, dur)
        if u > life: continue
        k = u / life; d0 = R * sp * ease(k); d1 = max(0, d0 - 40 * sp)
        p0 = (c[0] + math.cos(ang) * d1, c[1] + math.sin(ang) * d1); p1 = (c[0] + math.cos(ang) * d0, c[1] + math.sin(ang) * d0)
        cv2.line(m, tuple(map(int, p0)), tuple(map(int, p1)), 1.0 - k, 2, cv2.LINE_AA)
    cv2.circle(core, (int(c[0]), int(c[1])), 60, 1.0, -1, cv2.LINE_AA); core = cv2.GaussianBlur(core, (0, 0), 40)
    pulse = 0.75 + 0.25 * math.sin(tl * 2 * math.pi * 2.4)
    glow = cv2.GaussianBlur(m, (0, 0), 5)
    lay += core[..., None] * np.array([255, 70, 15], np.float32) * pulse * 1.3
    lay += glow[..., None] * np.array([255, 150, 50], np.float32) * 1.6 + m[..., None] * np.array([255, 235, 200], np.float32)
    return lay

def light_leak(f, tl, dur=0.35, side=0):
    if tl >= dur: return f
    u = 1 - tl / dur; yy, xx = np.mgrid[0:H:4, 0:W:4].astype(np.float32)
    g = np.exp(-(((xx - (0 if side == 0 else W)) / (W * 0.7)) ** 2 + ((yy - H * 0.4) / (H * 0.6)) ** 2))
    g = cv2.resize(g, (W, H))[..., None] * u
    col = np.array([255, 150, 70], np.float32)
    return 255 - (255 - f) * (1 - g * col / 255 * 0.95)

def zoom_blur(f, tl, dur=0.18, amt=0.16):
    if tl >= dur: return f
    u = 1 - tl / dur; acc = f.copy(); n = 5
    for k in range(1, n):
        z = 1 + amt * u * k / n
        M = np.float32([[z, 0, W / 2 - z * W / 2], [0, z, H / 2 - z * H / 2]])
        acc += cv2.warpAffine(f, M, (W, H), borderMode=cv2.BORDER_REFLECT)
    return acc / n

def red_x(f, tl, start=0.12):
    u = ease((tl - start) / 0.12)
    if u <= 0: return f
    over = f.copy(); L = int(250 * u); c = (W // 2, int(H * 0.5))
    for s in (1, -1):
        cv2.line(over, (c[0] - L, c[1] - L * s), (c[0] + L, c[1] + L * s), (235, 18, 18), 58, cv2.LINE_AA)
    return over
