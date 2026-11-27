"""COM376 text system (measured on the winner at 1080x1920): Verdana-style bold (DejaVu Sans Bold).
caption(): black text, per-line white rounded boxes, centred ~y 1300.
hook_box(): one white rounded card, line 1 RED caps, rest black caps, mid-frame.
section(): white caps, black outline + shadow, top third.
doctor_label(): 'Dr. Moore, DPM' white/outlined + blue 'PODIATRIST PHYSICIAN' bar."""
from functools import lru_cache
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
def F(s): return ImageFont.truetype(B, s)
_D = ImageDraw.Draw(Image.new("RGB", (1, 1)))
def tl(s, f, tr): return sum(_D.textlength(c, font=f) for c in s) + tr * max(0, len(s) - 1)
def td(d, x, y, s, f, fill, tr, stroke=0, sf=None):
    for c in s:
        d.text((x, y), c, font=f, fill=fill, stroke_width=stroke, stroke_fill=sf); x += _D.textlength(c, font=f) + tr

CAP = dict(size=83, track=-3.2, padx=22, pady=8, rad=16, maxw=900)   # measured on COM376 (720p) and scaled x1.5 to 1080
def wrap(text, f, tr, maxw):
    lines, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if cur and tl(t, f, tr) > maxw: lines.append(cur); cur = w
        else: cur = t
    lines += [cur] if cur else []
    if len(lines) == 2:   # balance, avoid orphans (COM376 breaks e.g. 'that soft foam / feeling' only when needed)
        ws = text.split(); best = None
        for k in range(1, len(ws)):
            a, b = " ".join(ws[:k]), " ".join(ws[k:]); m = max(tl(a, f, tr), tl(b, f, tr))
            if m <= maxw and (best is None or m < best[0] - 1): best = (m, [a, b])
        if best and len(text.split()) > 3: lines = best[1]
    return lines

@lru_cache(maxsize=2048)
def caption(text):
    c = CAP; f = F(c["size"]); lines = wrap(text, f, c["track"], c["maxw"])
    asc, desc = f.getmetrics(); lh = asc + desc - 6; pitch = lh + 2 * c["pady"] - 4
    ws = [tl(l, f, c["track"]) for l in lines]; W = int(max(ws) + 2 * c["padx"]) + 6; H = pitch * (len(lines) - 1) + lh + 2 * c["pady"] + 6
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    for i, (l, w) in enumerate(zip(lines, ws)):
        x0 = (W - w) / 2 - c["padx"]; y0 = 3 + i * pitch
        d.rounded_rectangle((x0, y0, x0 + w + 2 * c["padx"], y0 + lh + 2 * c["pady"]), c["rad"], fill=(255, 255, 255, 255))
    for i, (l, w) in enumerate(zip(lines, ws)):
        td(d, (W - w) / 2, 3 + i * pitch + c["pady"] - 3, l, f, (0, 0, 0), c["track"])
    return np.asarray(im, np.float32)

@lru_cache(maxsize=64)
def hook_box(red, black):
    fr, fb = F(80), F(60); tr = -1.8
    rl = [red] if isinstance(red, str) else list(red); bl = list(black)
    lines = [(l, fr, (232, 20, 30)) for l in rl] + [(l, fb, (0, 0, 0)) for l in bl]
    ws = [tl(l, f, tr) for l, f, _ in lines]; W = int(max(ws)) + 44
    hs = [f.getmetrics()[0] + f.getmetrics()[1] - 8 for _, f, _ in lines]; H = sum(hs) + 26
    im = Image.new("RGBA", (W + 8, H + 8), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle((4, 4, W + 4, H + 4), 16, fill=(255, 255, 255, 255)); y = 14
    for (l, f, col), w, h in zip(lines, ws, hs):
        td(d, 4 + (W - w) / 2, y - 2, l, f, col, tr); y += h
    return np.asarray(im, np.float32)

@lru_cache(maxsize=64)
def section(lines):
    f = F(81); tr = -1.4; ws = [tl(l, f, tr) for l in lines]; W = int(max(ws)) + 50; lh = 86; H = lh * len(lines) + 36
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); sh = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ds = ImageDraw.Draw(sh)
    for i, (l, w) in enumerate(zip(lines, ws)): td(ds, (W - w) / 2 + 5, 14 + i * lh + 6, l, f, (0, 0, 0, 200), tr, 6, (0, 0, 0, 200))
    im = Image.alpha_composite(im, sh.filter(ImageFilter.GaussianBlur(4))); d = ImageDraw.Draw(im)
    for i, (l, w) in enumerate(zip(lines, ws)): td(d, (W - w) / 2, 14 + i * lh, l, f, (255, 255, 255), tr, 5, (0, 0, 0))
    return np.asarray(im, np.float32)

@lru_cache(maxsize=4)
def doctor_label(name="Dr. Moore, DPM", title="PODIATRIST PHYSICIAN"):
    fn, ft = F(72), F(40)
    wn, wt = tl(name, fn, -2), tl(title, ft, -0.5); W = int(max(wn, wt + 30)) + 30; H = 175
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    td(ImageDraw.Draw(sh), 18, 10, name, fn, (0, 0, 0, 220), -2, 4, (0, 0, 0, 220)); im = Image.alpha_composite(im, sh.filter(ImageFilter.GaussianBlur(3)))
    d = ImageDraw.Draw(im); td(d, 12, 4, name, fn, (255, 255, 255), -2, 3, (60, 60, 60))
    d.rectangle((12, 100, 12 + wt + 30, 160), fill=(20, 98, 200, 255)); td(d, 27, 108, title, ft, (255, 255, 255), -0.5)
    return np.asarray(im, np.float32)
