"""Composite StefanBrain's copy onto the approved W48 scenes (brief section 6) -> 1080x1350 masters.

    python3 compose.py            # all ads, using copy.json and picks.json
    python3 compose.py 01 08      # just these

copy.json  : StefanBrain's final copy (chat_e2881d64bb4e43c687b42831eb31dff3, project "Retra Launch").
picks.json : which render each ad uses, plus its version number.
Headline/subhead are variables, so FR lines can be swapped in later (phase 2): pass LANG=fr.
"""
import json
import os
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont, ImageOps

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[4]
FONTS = HERE.parents[1] / "fonts"
CUT = REPO / "assets/retra/product/cutout"
OUTDIR = HERE / "output"
OUTDIR.mkdir(exist_ok=True)
W, H = 1080, 1350
CREAM = (243, 238, 228)
INK = (2, 43, 73)  # landing-page navy #022B49
CTA_A, CTA_B = (44, 77, 99), (142, 166, 180)  # landing-page CTA gradient #2C4D63 -> #8EA6B4
RED = (178, 34, 34)
WHITE = (255, 255, 255)

COPY = {a["id"]: a for a in json.load(open(HERE / "copy.json"))["ads"]}
PICKS = json.load(open(HERE / "picks.json"))
LANG = os.environ.get("LANG_AD", "en")


# ---------- type helpers ----------
def font(name, size, weight=None):
    f = ImageFont.truetype(str(FONTS / name), size)
    if weight:
        f.set_variation_by_name(weight)
    return f


# Landing-page type system (landing-pages/retra/index.html): display = Tinos (Times New Roman metrics),
# weight 400, letter-spacing -0.04em; body = Inter; hand/kicker = Shantell Sans italic.
def tinos(size, track=-0.04):
    f = ImageFont.truetype(str(FONTS / "Tinos-Regular.ttf"), size)
    f.track = track * size
    return f


def shantell(size, track=0.0, bold=False):
    f = ImageFont.truetype(str(FONTS / ("ShantellSans-BoldItalic.ttf" if bold else "ShantellSans-Italic.ttf")), size)
    f.track = track * size
    return f


def inter(size, weight="Bold"):
    return font("Inter.ttf", size, weight)


def measure(f, text):
    return f.getlength(text) + getattr(f, "track", 0) * max(0, len(text) - 1)


def draw_text(d, xy, text, f, fill):
    tr = getattr(f, "track", 0)
    if not tr:
        d.text(xy, text, font=f, fill=fill)
        return
    x, y = xy
    for i, ch in enumerate(text):
        # where this glyph sits in the normally kerned line, plus i steps of tracking
        gx = f.getlength(text[: i + 1]) - f.getlength(ch) + i * tr
        d.text((x + gx, y), ch, font=f, fill=fill)


def wrap(text, f, maxw):
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if measure(f, t) <= maxw or not cur:
            cur = t
        else:
            lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines


def balanced(text, f, maxw):
    """Like CSS text-wrap: balance - same line count, narrowest width that still fits."""
    lines = wrap(text, f, maxw)
    if len(lines) < 2:
        return lines
    lo, hi = maxw * 0.4, maxw
    while hi - lo > 2:
        mid = (lo + hi) / 2
        if len(wrap(text, f, mid)) == len(lines) and all(measure(f, l) <= mid for l in wrap(text, f, mid)):
            hi = mid
        else:
            lo = mid
    return wrap(text, f, hi)


def fit(text, make_font, maxw, max_lines, start, floor):
    size = start
    while size > floor:
        f = make_font(size)
        lines = wrap(text, f, maxw)
        if len(lines) <= max_lines and all(measure(f, l) <= maxw for l in lines):
            return f, balanced(text, f, maxw)
        size -= 2
    f = make_font(floor)
    return f, balanced(text, f, maxw)


TEXT_BOXES = []  # (ad, box) for the text-coverage check


def draw_lines(img, lines, f, x, y, fill, align="left", lead=1.05, shadow=None, width=None):
    d = ImageDraw.Draw(img)
    asc, desc = f.getmetrics()
    lh = int((asc + desc) * lead)
    y0 = y
    for line in lines:
        lw = measure(f, line)
        if align == "center":
            lx = x + (width - lw) / 2
        elif align == "right":
            lx = x + width - lw
        else:
            lx = x
        if shadow:
            sh = Image.new("RGBA", img.size, (0, 0, 0, 0))
            draw_text(ImageDraw.Draw(sh), (lx + 2, y + 3), line, f, shadow)
            sh = sh.filter(ImageFilter.GaussianBlur(4))
            img.alpha_composite(sh)
            d = ImageDraw.Draw(img)
        draw_text(d, (lx, y), line, f, fill)
        TEXT_BOXES.append((lx, y, lx + lw, y + lh))
        y += lh
    return y


def scrim(img, top, bottom, color=(0, 0, 0), max_a=150, direction="down"):
    """Vertical gradient band: 'down' = strongest at top, 'up' = strongest at bottom."""
    band = np.linspace(1, 0, bottom - top) if direction == "down" else np.linspace(0, 1, bottom - top)
    a = (band ** 1.3 * max_a).astype("uint8")
    alpha = Image.fromarray(np.repeat(a[:, None], img.width, 1))
    layer = Image.new("RGBA", (img.width, bottom - top), color + (0,))
    layer.putalpha(alpha)
    img.alpha_composite(layer, (0, top))


def pill(img, text, f, cx, cy, bg, fg, padx=30, pady=16, radius=None):
    d = ImageDraw.Draw(img)
    tw = measure(f, text)
    asc, desc = f.getmetrics()
    h = asc + desc + 2 * pady
    w = tw + 2 * padx
    box = (cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2)
    if bg == "cta":  # landing-page CTA: slate-blue gradient pill
        grad = Image.new("RGBA", (int(w), int(h)))
        gd = ImageDraw.Draw(grad)
        for i in range(int(w)):
            t = i / max(1, w - 1)
            gd.line([(i, 0), (i, h)], fill=tuple(int(a + (b - a) * t) for a, b in zip(CTA_A, CTA_B)) + (255,))
        m = Image.new("L", grad.size, 0)
        ImageDraw.Draw(m).rounded_rectangle((0, 0, w - 1, h - 1), radius=h / 2, fill=255)
        img.paste(grad, (int(box[0]), int(box[1])), m)
    else:
        d.rounded_rectangle(box, radius=radius or h / 2, fill=bg)
    draw_text(d, (cx - tw / 2, cy - h / 2 + pady), text, f, fg)
    TEXT_BOXES.append(box)
    return box


def src_path(path):
    """Raw renders are committed as JPEG archives; the full PNGs stay local (gitignored)."""
    path = Path(path)
    return path if path.exists() else path.with_suffix(".jpg")


def scene(path):
    im = Image.open(src_path(path)).convert("RGB")
    return ImageOps.fit(im, (W, H), Image.LANCZOS, centering=(0.5, 0.5)).convert("RGBA")


def soft_blur_region(img, box, radius=7, feather=18):
    """Out-of-focus pass on one region (used to keep tiny background UI/sign text unreadable)."""
    blurred = img.filter(ImageFilter.GaussianBlur(radius))
    m = Image.new("L", img.size, 0)
    ImageDraw.Draw(m).rounded_rectangle(box, radius=feather, fill=255)
    m = m.filter(ImageFilter.GaussianBlur(feather))
    img.paste(blurred, (0, 0), m)


def grain(img, amount=4, seed=1):
    rng = np.random.default_rng(seed)
    a = np.asarray(img.convert("RGB")).astype(np.int16)
    a = np.clip(a + rng.normal(0, amount, a.shape[:2])[..., None], 0, 255).astype("uint8")
    return Image.fromarray(a).convert("RGBA")


def typeset(t):
    """Typesetting only (no wording change): curly apostrophes."""
    return t.replace("'", "\u2019")


def copy(ad):
    c = COPY[ad]
    hl = c["fr_headline"] if LANG == "fr" else c["headline"]
    extra = {e["slot"]: typeset(e["text"]) for e in c["extra_lines"]}
    return typeset(hl), typeset(c["subhead"]), extra


# ---------- TOF ----------
def tof_top(ad, img, dark_text, align="left", box_w=900, scrim_color=None, scrim_a=0, top_pad=70, x=70,
            hl_size=88, sub_size=36, max_lines=2, scrim_h=520):
    hl, sub, _ = copy(ad)
    if scrim_color is not None:
        scrim(img, 0, scrim_h, scrim_color, scrim_a, "down")
    fill = INK if dark_text else WHITE
    shadow = None if dark_text else (0, 0, 0, 170)
    f, lines = fit(hl, tinos, box_w, max_lines, hl_size, 56)
    y = draw_lines(img, lines, f, x, top_pad, fill, align, 1.04, shadow, box_w)
    fs, slines = fit(sub, lambda s: inter(s, "Bold"), box_w, max_lines, sub_size, 28)
    draw_lines(img, slines, fs, x, y + 10, fill, align, 1.15, shadow, box_w)


def ad01(ad, src):
    img = scene(src)
    soft_blur_region(img, (470, 880, 780, 1270), radius=6)  # phone sits behind the camera; keep its UI soft
    tof_top(ad, img, dark_text=True, scrim_color=(245, 242, 236), scrim_a=120)
    return img


def ad02(ad, src):
    img = scene(src)
    hl, sub, _ = copy(ad)
    scrim(img, 860, H, (0, 0, 0), 200, "up")
    box_w = 940
    fs, slines = fit(sub, lambda s: inter(s, "SemiBold"), box_w, 2, 36, 28)
    f, lines = fit(hl, tinos, box_w, 2, 88, 56)
    asc, desc = f.getmetrics()
    sasc, sdesc = fs.getmetrics()
    total = len(lines) * int((asc + desc) * 1.04) + 10 + len(slines) * int((sasc + sdesc) * 1.15)
    y = H - 70 - total
    y = draw_lines(img, lines, f, 70, y, WHITE, "left", 1.04, (0, 0, 0, 160), box_w)
    draw_lines(img, slines, fs, 70, y + 10, WHITE, "left", 1.15, (0, 0, 0, 160), box_w)
    return img


def ad03(ad, src):
    img = scene(src)
    for box in PICKS[ad].get("blur", []):
        soft_blur_region(img, tuple(box), radius=6)
    tof_top(ad, img, dark_text=False, scrim_color=(20, 30, 45), scrim_a=200, scrim_h=600)
    return img


def ad04(ad, src):
    img = scene(src)
    tof_top(ad, img, dark_text=False, box_w=760, scrim_color=(25, 20, 15), scrim_a=200, scrim_h=600)
    return img


def ad05(ad, src):
    img = scene(src)
    _, _, extra = copy(ad)
    tof_top(ad, img, dark_text=False, align="center", box_w=940, x=70, scrim_color=(0, 0, 0), scrim_a=150, scrim_h=560)
    # handwritten line on the blank place card
    x0, y0, x1, y1 = PICKS[ad]["card"]
    cw, ch = x1 - x0, y1 - y0
    layer = Image.new("RGBA", (cw * 3, ch * 3), (0, 0, 0, 0))
    f, lines = fit(extra["place_card"], shantell, cw * 3 - 60, 3, 110, 40)
    draw_lines(layer, lines, f, 30, 0, (40, 38, 52, 235), "center", 0.95, None, cw * 3 - 60)
    TEXT_BOXES.pop()  # scene text on the card; counted once below
    for _ in lines[1:]:
        TEXT_BOXES.pop()
    bb = layer.getbbox()
    layer = layer.crop(bb)
    layer.thumbnail((int(cw * 0.86), int(ch * 0.78)), Image.LANCZOS)
    layer = layer.filter(ImageFilter.GaussianBlur(0.5))
    img.alpha_composite(layer, (int(x0 + (cw - layer.width) / 2), int(y0 + (ch - layer.height) / 2)))
    TEXT_BOXES.append((x0, y0, x1, y1))
    return img


def ad06(ad, src):
    img = scene(src)
    tof_top(ad, img, dark_text=False, scrim_color=(0, 0, 0), scrim_a=110)
    return img


def ad07(ad, src):
    img = scene(src)
    tof_top(ad, img, dark_text=True, box_w=470, scrim_color=(240, 232, 220), scrim_a=90, max_lines=3, hl_size=80, sub_size=32, x=56)
    return img


# ---------- BOF ----------
def cta(img, text, cy):
    return pill(img, text, inter(34, "SemiBold"), W / 2, cy, "cta", WHITE, padx=56, pady=20)


def bof_head(ad, img, top=64, size=78, sub_size=34, color=INK, hl_lines=2, floor=52):
    hl, sub, _ = copy(ad)
    f, lines = fit(hl, tinos, 960, hl_lines, size, floor)
    y = draw_lines(img, lines, f, 60, top, color, "center", 1.06, None, 960)
    fs, slines = fit(sub, lambda s: inter(s, "Medium"), 940, 2, sub_size, 26)
    return draw_lines(img, slines, fs, 70, y + 8, (65, 96, 119), "center", 1.25, None, 940)  # body #416077


def filter_looks(im):
    """Same four looks as the landing page (landing-pages/retra/tools/filters2.py)."""
    from PIL import ImageEnhance

    w, h = im.size

    def curves(img, r, g, b):
        return Image.merge("RGB", [c.point(f) for c, f in zip(img.split(), (r, g, b))])

    def grn(img, a):
        n = Image.effect_noise((w, h), a).convert("RGB").point(lambda v: (v - 128) * 0.08 + 128)
        return ImageChops.add(img, n, 1, -128)

    return {
        "Vintage": curves(ImageEnhance.Color(im).enhance(0.78), lambda x: int(26 + x * .88),
                          lambda x: int(20 + x * .84), lambda x: int(14 + x * .72)),
        "Black & White": grn(ImageEnhance.Contrast(ImageOps.grayscale(im)).enhance(1.18).convert("RGB"), 30),
        "Natural": ImageEnhance.Contrast(im).enhance(1.02),
        "Film": grn(curves(ImageEnhance.Contrast(ImageEnhance.Color(im).enhance(.9)).enhance(.92),
                           lambda x: int(18 + x * .86), lambda x: int(14 + x * .84), lambda x: int(36 + x * .84)), 36),
    }


def ad08(ad, src):
    _, _, extra = copy(ad)
    img = grain(Image.new("RGB", (W, H), CREAM), 3, 8)
    y = bof_head(ad, img, top=50, size=76)
    base = Image.open(src_path(src)).convert("RGB")
    # square crop from the upper part of the scene: the render's bottom edge holds an invented camera, keep it out
    bw, bh = base.size
    side = min(bw, int(bh * 0.84))
    top = int(bh * 0.03)
    sq = base.crop(((bw - side) // 2, top, (bw - side) // 2 + side, top + side)).resize((900, 900), Image.LANCZOS)
    looks = filter_looks(sq)
    labels = [s_.strip() for s_ in extra.get("filter_labels", "Vintage, Black & White, Natural, Film").split(",")]
    tile, gap, border, lab = 392, 64, 12, 44
    gx = (W - (2 * tile + gap)) / 2
    gy = y + 18 + lab  # top-row labels sit above the tiles
    lf = tinos(32, -0.03)
    d = ImageDraw.Draw(img)
    for i, name in enumerate(["Vintage", "Black & White", "Natural", "Film"]):
        r, c = divmod(i, 2)
        x = int(gx + c * (tile + gap))
        yy = int(gy + r * (tile + gap))
        t = looks[name].resize((tile - 2 * border, tile - 2 * border), Image.LANCZOS)
        card = Image.new("RGB", (tile, tile), WHITE)
        card.paste(t, (border, border))
        sh = Image.new("RGBA", (tile + 40, tile + 40), (0, 0, 0, 0))
        ImageDraw.Draw(sh).rectangle((20, 26, tile + 20, tile + 26), fill=(0, 0, 0, 60))
        img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(10)), (x - 20, yy - 20))
        img.paste(card, (x, yy))
        label = labels[i] if i < len(labels) else name
        lw = measure(lf, label)
        ly = yy - lab + 2 if r == 0 else yy + tile + 6
        draw_text(d, (x + (tile - lw) / 2, ly), label, lf, INK)
        TEXT_BOXES.append((x + (tile - lw) / 2, ly, x + (tile + lw) / 2, ly + 40))
    # product cutout over the centre of the grid
    cam = Image.open(CUT / f"retra_{PICKS[ad].get('colour', 'pine')}_34.png").convert("RGBA")
    cw = 380
    cam = cam.resize((cw, int(cam.height * cw / cam.width)), Image.LANCZOS)
    cx = int(W / 2 - cw / 2)
    cy = int(gy + tile + gap / 2 - cam.height / 2)
    shadow = Image.new("RGBA", (cam.width + 80, cam.height + 80), (0, 0, 0, 0))
    shadow.paste(Image.new("RGBA", cam.size, (0, 0, 0, 120)), (40, 52), cam.getchannel("A"))
    img.alpha_composite(shadow.filter(ImageFilter.GaussianBlur(16)), (cx - 40, cy - 40))
    img.alpha_composite(cam, (cx, cy))
    yb = int(gy + 2 * tile + gap + lab + 16)
    pf = tinos(50, -0.03)
    price = extra.get("price_offer_line", "")
    pw = measure(pf, price)
    draw_text(ImageDraw.Draw(img), ((W - pw) / 2, yb), price, pf, INK)
    TEXT_BOXES.append(((W - pw) / 2, yb, (W + pw) / 2, yb + 60))
    cta(img, extra.get("cta", ""), H - 66)
    return img


def ad09(ad, src):
    _, _, extra = copy(ad)
    img = scene(src)
    y = bof_head(ad, img, top=80, size=88, hl_lines=1, floor=60)
    pill(img, extra.get("pill", "").upper(), shantell(26, 0.09), W / 2, y + 46, INK, WHITE, padx=28, pady=12)
    cta(img, extra.get("cta", ""), H - 90)
    return img


def stamp_tag(img, text, cx, y):
    f = inter(24, "ExtraBold")
    tw = measure(f, text.upper())
    pad = 14
    w, h = int(tw + 2 * pad), 44
    layer = Image.new("RGBA", (w + 20, h + 20), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    d.rounded_rectangle((10, 10, 10 + w, 10 + h), radius=6, outline=RED + (235,), width=3)
    d.text((10 + pad, 10 + (h - 30) / 2), text.upper(), font=f, fill=RED + (235,))
    # rubber-stamp texture: knock out a little ink at random
    rng = np.random.default_rng(int(cx))
    a = np.asarray(layer.getchannel("A")).astype(float)
    a *= (rng.random(a.shape) > 0.12)
    layer.putalpha(Image.fromarray(a.astype("uint8")).filter(ImageFilter.GaussianBlur(0.6)))
    layer = layer.rotate(rng.uniform(-6, 6), resample=Image.BICUBIC, expand=True)
    img.alpha_composite(layer, (int(cx - layer.width / 2), int(y)))
    TEXT_BOXES.append((cx - w / 2, y, cx + w / 2, y + h))


def ad10(ad, src):
    _, _, extra = copy(ad)
    img = scene(src)
    y = bof_head(ad, img, top=90, size=80)
    pos = json.load(open(HERE / "renders/10_positions.json"))
    sx = W / pos["canvas"][0]
    sy = H / pos["canvas"][1]
    s = max(sx, sy)
    ox = (pos["canvas"][0] * s - W) / 2
    oy = (pos["canvas"][1] * s - H) / 2
    tag = extra.get("tag_under_each_camera", "")
    for c in pos["order"]:
        x0, y0, x1, y1 = pos["boxes"][c]
        cx = (x0 + x1) / 2 * s - ox
        stamp_tag(img, tag, cx, y1 * s - oy + 22)
    pf = tinos(56, -0.03)
    price = extra.get("price_line", "")
    pw = measure(pf, price)
    py = 1005
    draw_text(ImageDraw.Draw(img), ((W - pw) / 2, py), price, pf, INK)
    TEXT_BOXES.append(((W - pw) / 2, py, (W + pw) / 2, py + 56))
    cta(img, extra.get("cta", ""), H - 110)
    return img


BUILDERS = {"01": ad01, "02": ad02, "03": ad03, "04": ad04, "05": ad05, "06": ad06, "07": ad07,
            "08": ad08, "09": ad09, "10": ad10}


def coverage(boxes):
    m = np.zeros((H, W), bool)
    for x0, y0, x1, y1 in boxes:
        m[max(0, int(y0)):min(H, int(y1)), max(0, int(x0)):min(W, int(x1))] = True
    return m.mean()


def main():
    ads = sys.argv[1:] or list(BUILDERS)
    report = {}
    for ad in ads:
        p = PICKS[ad]
        TEXT_BOXES.clear()
        img = BUILDERS[ad](ad, HERE / "renders" / p["render"])
        img = img.convert("RGB")
        assert img.size == (W, H)
        suffix = "_ILLUSTRATIVE" if p.get("illustrative") else ""
        lang = "" if LANG == "en" else f"_{LANG}"
        name = f"RET_W48_{ad}_{p['funnel']}_{p['angle']}_v{p['v']}{lang}{suffix}.png"
        img.save(OUTDIR / name, optimize=True)
        report[ad] = {"file": name, "text_coverage": round(coverage(TEXT_BOXES), 3)}
        print(ad, name, "text coverage", report[ad]["text_coverage"], flush=True)
    json.dump(report, open(HERE / "work" / f"compose_report{('_' + LANG) if LANG != 'en' else ''}.json", "w"),
              indent=1)


if __name__ == "__main__":
    main()
