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
EMO = "/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf"
@lru_cache(maxsize=64)
def emoji(ch, px):
    """colour emoji (Noto, bitmap 109px) scaled to px; RGBA PIL image"""
    f = ImageFont.truetype(EMO, 109); im = Image.new("RGBA", (160, 160), (0, 0, 0, 0))
    ImageDraw.Draw(im).text((10, 10), ch, font=f, embedded_color=True); im = im.crop(im.getbbox())
    return im.resize((max(1, round(im.width * px / im.height)), px), Image.LANCZOS)
def split_emoji(l):
    """'TEXT ❌' -> ('TEXT', '❌'); emoji = trailing token with no ascii letters/digits"""
    p = l.rsplit(" ", 1)
    if len(p) == 2 and not any(c.isascii() and c.isalnum() for c in p[1]) and any(ord(c) > 0x2000 for c in p[1]): return p[0], p[1]
    return l, None
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
    rl = [red] if isinstance(red, str) else list(red); bl = list(black); k = 1.0
    while max([tl(l, F(int(100 * k)), -1.8) for l in rl] + [tl(l, F(int(78 * k)), -1.8) for l in bl]) > 990: k -= 0.02   # feedback: hook text bigger; card stays inside the frame
    fr, fb = F(int(100 * k)), F(int(78 * k)); tr = -1.8
    lines = [(l, fr, (232, 20, 30)) for l in rl] + [(l, fb, (0, 0, 0)) for l in bl]
    em = [split_emoji(l) for l, _, _ in lines]; lines = [(t, f, c) for (t, _), (_, f, c) in zip(em, lines)]
    ews = [(f.size * 1.05 + 20 if e else 0) for (_, e), (_, f, _) in zip(em, lines)]
    ws = [tl(l, f, tr) + ew for (l, f, _), ew in zip(lines, ews)]; W = int(max(ws)) + 44
    hs = [f.getmetrics()[0] + f.getmetrics()[1] - 8 for _, f, _ in lines]; H = sum(hs) + 26
    im = Image.new("RGBA", (W + 8, H + 8), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle((4, 4, W + 4, H + 4), 20, fill=(255, 255, 255, 255)); y = 14
    for (l, f, col), w, h, (_, e), ew in zip(lines, ws, hs, em, ews):
        x0 = 4 + (W - w) / 2; td(d, x0, y - 2, l, f, col, tr)
        if e: g = emoji(e, int(f.size * 1.0)); im.alpha_composite(g, (int(x0 + w - ew + 20), int(y + (h - g.height) / 2)))
        y += h
    return np.asarray(im, np.float32)

@lru_cache(maxsize=64)
def section(lines):
    em = [split_emoji(l) for l in lines]; lines = [t for t, _ in em]; sz = 81
    while max(tl(l, F(sz), -1.4) + (sz * 1.2 if e else 0) for l, (_, e) in zip(lines, em)) > 1000: sz -= 1     # stays inside the frame
    f = F(sz); tr = -1.4; ep = int(sz * 0.98)
    ws = [tl(l, f, tr) + (ep + 18 if e else 0) for l, (_, e) in zip(lines, em)]; W = int(max(ws)) + 50; lh = int(sz * 1.06); H = lh * len(lines) + 36
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); sh = Image.new("RGBA", (W, H), (0, 0, 0, 0)); ds = ImageDraw.Draw(sh)
    for i, (l, w) in enumerate(zip(lines, ws)): td(ds, (W - w) / 2 + 5, 14 + i * lh + 6, l, f, (0, 0, 0, 200), tr, 6, (0, 0, 0, 200))
    im = Image.alpha_composite(im, sh.filter(ImageFilter.GaussianBlur(4))); d = ImageDraw.Draw(im)
    for i, (l, w) in enumerate(zip(lines, ws)):
        td(d, (W - w) / 2, 14 + i * lh, l, f, (255, 255, 255), tr, 5, (0, 0, 0))
        if em[i][1]: g = emoji(em[i][1], ep); im.alpha_composite(g, (int((W + w) / 2 - g.width), 14 + i * lh + 6))
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
