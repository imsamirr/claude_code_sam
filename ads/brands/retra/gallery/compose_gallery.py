"""Compose the Retra product-gallery squares (2000x2000) in the landing-page gallery style.

    python3 compose_gallery.py

Words: gallery_copy.json (StefanBrain, project "Retra Launch").  Scenes: picks.json -> renders/.
Type: Tinos headlines at -0.04em and Inter labels, in landing-page navy #022B49 (as in
landing-pages/retra/gallery-src/gallery.html).
"""
import json
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps
from scipy import ndimage

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
FONTS = HERE.parent / "fonts"
CUT = REPO / "assets/retra/product/cutout"
OUT = HERE / "output"
OUT.mkdir(exist_ok=True)
S = 2000
CREAM = (243, 238, 228)
NAVY = (2, 43, 73)
MUTE = (2, 43, 73, 128)
COPY = json.load(open(HERE / "gallery_copy.json"))
PICKS = json.load(open(HERE / "picks.json"))
COLOURS = ["chalk", "obsidian", "sol"]


def tinos(size, track=-0.04):
    f = ImageFont.truetype(str(FONTS / "Tinos-Regular.ttf"), size)
    f.track = track * size
    return f


def inter(size, weight="Medium"):
    f = ImageFont.truetype(str(FONTS / "Inter.ttf"), size)
    f.set_variation_by_name(weight)
    f.track = 0
    return f


def measure(f, t):
    return f.getlength(t) + f.track * max(0, len(t) - 1)


def text(d, xy, t, f, fill=NAVY, anchor="l"):
    x, y = xy
    w = measure(f, t)
    if anchor == "c":
        x -= w / 2
    elif anchor == "r":
        x -= w
    for i, ch in enumerate(t):
        gx = f.getlength(t[: i + 1]) - f.getlength(ch) + i * f.track
        d.text((x + gx, y), ch, font=f, fill=fill)
    return w


def typeset(t):
    return t.replace("'", "’")


def src(name):
    p = HERE / "renders" / name
    return p if p.exists() else p.with_suffix(".jpg")


def cutout(im, thresh=34):
    """Cut a product off a flat light background (corner colour), dropping its soft floor shadow."""
    im = im.convert("RGB")
    a = np.asarray(im).astype(float)
    corners = np.concatenate([a[:30, :30].reshape(-1, 3), a[:30, -30:].reshape(-1, 3),
                              a[-30:, :30].reshape(-1, 3), a[-30:, -30:].reshape(-1, 3)])
    bg = np.median(corners, axis=0)
    lum = a.sum(-1)
    chd = np.abs(a / np.maximum(lum[..., None], 1) - bg / bg.sum()).sum(-1)
    d = np.sqrt(((a - bg) ** 2).sum(-1))
    tan = (chd < 0.09) & ((a[..., 0] - a[..., 2]) > 30)  # background hue incl. its darker floor shadow
    m = ~((d <= thresh) | ((chd < 0.04) & (lum > bg.sum() * 0.62)) | tan)
    m = ndimage.binary_opening(m, iterations=2)
    m = ndimage.binary_closing(m, iterations=4)
    # light panels (Chalk) sit close to the cream background: also take everything enclosed by the black body
    dark = ndimage.binary_closing(lum < 0.30 * 765, iterations=3)
    m = ndimage.binary_fill_holes(m | ndimage.binary_fill_holes(dark))
    lab, n = ndimage.label(m)
    m = lab == (1 + np.argmax(ndimage.sum(m, lab, range(1, n + 1))))
    mask = Image.fromarray((m * 255).astype("uint8")).filter(ImageFilter.GaussianBlur(1.2))
    o = im.copy()
    o.putalpha(mask)
    return o.crop(mask.getbbox())


def front_cut(c):
    """Front view cut-out; Chalk uses its green-screen mask (cutout_chalk_front.py)."""
    pre = HERE / "renders" / f"front_{c}_cutout.png"
    return Image.open(pre).convert("RGBA") if pre.exists() else cutout(Image.open(src(PICKS[f"front_{c}"])))


def fit_w(im, w):
    return im.resize((w, int(im.height * w / im.width)), Image.LANCZOS)


def place(canvas, obj, cx, bottom, shadow=True):
    x, y = int(cx - obj.width / 2), int(bottom - obj.height)
    if shadow:
        sh = Image.new("RGBA", (obj.width + 160, 120), (0, 0, 0, 0))
        ImageDraw.Draw(sh).ellipse((80, 40, obj.width + 80, 80), fill=(60, 45, 30, 90))
        canvas.alpha_composite(sh.filter(ImageFilter.GaussianBlur(22)), (x - 80, int(bottom - 62)))
    canvas.alpha_composite(obj, (x, y))


def arrow(d, pts, head=True, w=6):
    """Hand-drawn style arrow along a quadratic curve p0 -> p2 with control p1."""
    (x0, y0), (x1, y1), (x2, y2) = pts
    path = [((1 - t) ** 2 * x0 + 2 * (1 - t) * t * x1 + t ** 2 * x2,
             (1 - t) ** 2 * y0 + 2 * (1 - t) * t * y1 + t ** 2 * y2) for t in np.linspace(0, 1, 40)]
    d.line(path, fill=NAVY, width=w, joint="curve")
    if head:
        (ax, ay), (bx, by) = path[-4], path[-1]
        ang = np.arctan2(by - ay, bx - ax)
        for s in (2.6, -2.6):
            d.line([(bx, by), (bx + 34 * np.cos(ang + s), by + 34 * np.sin(ang + s))], fill=NAVY, width=w)


def canvas():
    rng = np.random.default_rng(3)
    a = np.array(CREAM, float)[None, None, :] + rng.normal(0, 1.6, (S, S, 1))
    return Image.fromarray(np.clip(a, 0, 255).astype("uint8")).convert("RGBA")


def hand(c):
    im = ImageOps.fit(Image.open(src(PICKS[f"hand_{c}"])).convert("RGB"), (S, S), Image.LANCZOS)
    return im


def howto(c):
    img = canvas()
    d = ImageDraw.Draw(img)
    text(d, (S / 2, 120), typeset(COPY["howto_title"]), tinos(150), anchor="c")
    pad, gap, top = 170, 80, 400
    cw = (S - 2 * pad - gap) / 2
    ch = (S - top - 150 - gap) / 2
    back = Image.open(HERE / "base/back_cutout.png").convert("RGBA")
    back = back.filter(ImageFilter.GaussianBlur(0))
    imgs = [Image.open(CUT / f"retra_{c}_34.png").convert("RGBA"),
            back,
            front_cut(c),
            cutout(Image.open(src(PICKS[f"bottom_{c}"])))]
    lab = inter(58, "SemiBold")
    for i, (step, ob) in enumerate(zip(COPY["howto_steps"], imgs)):
        r, col = divmod(i, 2)
        x0 = pad + col * (cw + gap)
        y0 = top + r * (ch + gap)
        card = Image.new("RGBA", (int(cw), int(ch)), (0, 0, 0, 0))
        ImageDraw.Draw(card).rounded_rectangle((0, 0, cw - 1, ch - 1), radius=52, fill=(255, 255, 255, 255))
        img.alpha_composite(card, (int(x0), int(y0)))
        d = ImageDraw.Draw(img)
        cx, cy, rad = x0 + 90, y0 + 92, 46
        d.ellipse((cx - rad, cy - rad, cx + rad, cy + rad), fill=NAVY)
        text(d, (cx, cy - 32), str(i + 1), inter(50, "SemiBold"), (255, 255, 255), "c")
        ls = 58
        while measure(inter(ls, "SemiBold"), typeset(step)) > cw - 168 - 44:
            ls -= 2
        text(d, (x0 + 168, y0 + 58 + (58 - ls) * 0.6), typeset(step), inter(ls, "SemiBold"))
        ob = fit_w(ob, int(cw * 0.84))
        if ob.height > ch * 0.68:
            ob = ob.resize((int(ob.width * ch * 0.68 / ob.height), int(ch * 0.68)), Image.LANCZOS)
        place(img, ob, x0 + cw / 2, y0 + ch - 60)
    return img.convert("RGB")


def usbc(c):
    img = ImageOps.fit(Image.open(src(PICKS[f"usbc_{c}"])).convert("RGB"), (S, S), Image.LANCZOS).convert("RGBA")
    d = ImageDraw.Draw(img)
    f = tinos(150)
    words = typeset(COPY["usbc_headline"]).split()
    # two balanced lines in the clear top-right area, like the source layout
    best = min(range(1, len(words)), key=lambda k: abs(measure(f, " ".join(words[:k])) - measure(f, " ".join(words[k:]))))
    lines = [" ".join(words[:best]), " ".join(words[best:])] if len(words) > 1 else words
    y = PICKS.get("usbc_text_y", 230)
    for ln in lines:
        text(d, (PICKS.get("usbc_text_x", 1000), y), ln, f)
        y += 165
    return img.convert("RGB")


def frontback(c):
    img = canvas()
    d = ImageDraw.Draw(img)
    hs = 230
    while measure(tinos(hs), typeset(COPY["frontback_headline"])) > S - 300:
        hs -= 4
    text(d, (150, 200), typeset(COPY["frontback_headline"]), tinos(hs))
    if COPY.get("frontback_second_line"):
        text(d, (158, 200 + hs * 1.12), typeset(COPY["frontback_second_line"]), tinos(int(hs * 0.52)), MUTE)
    front = fit_w(front_cut(c), 820)
    back = fit_w(Image.open(HERE / "base/back_cutout.png").convert("RGBA"), 820)
    base = 1640
    place(img, front, 545, base)
    place(img, back, 1455, base)
    d = ImageDraw.Draw(img)
    lf = inter(64, "Medium")
    text(d, (1600, base - back.height - 230), typeset(COPY["back_label"]), lf)
    arrow(d, [(1580, base - back.height - 160), (1500, base - back.height - 120), (1520, base - back.height - 30)])
    fw = measure(lf, typeset(COPY["front_label"]))
    text(d, (520 - fw, base + 170), typeset(COPY["front_label"]), lf)
    arrow(d, [(545, base + 205), (625, base + 150), (600, base + 50)])
    return img.convert("RGB")


def sparkle(d, cx, cy, r, col=(201, 162, 77), w=5):
    for k in range(4):
        ang = k * np.pi / 4
        d.line([(cx - r * np.cos(ang), cy - r * np.sin(ang)), (cx + r * np.cos(ang), cy + r * np.sin(ang))], fill=col, width=w)


def filters(c):
    img = canvas()
    d = ImageDraw.Draw(img)
    text(d, (170, 110), typeset(COPY["filters_title"]), tinos(140))
    tw, th, gx, gy = 830, 619, 70, 160
    x0s = [(S - 2 * tw - gx) / 2, (S + gx) / 2]
    y0s = [350, 350 + th + gy]
    rule = (2, 43, 73, 60)
    d.line([(S / 2, 330), (S / 2, y0s[1] + th + 110)], fill=rule, width=3)
    d.line([(240, y0s[0] + th + 98), (S - 240, y0s[0] + th + 98)], fill=rule, width=3)
    lf = inter(60, "Medium")
    files = {"Natural": "f-natural", "Vintage": "f-vintage", "Black & White": "f-bw", "Film": "f-film"}
    for i, name in enumerate(COPY["filter_labels"]):
        r, col = divmod(i, 2)
        ph = ImageOps.fit(Image.open(HERE / "base" / f"{files[name]}_2x.jpg").convert("RGB"), (tw, th), Image.LANCZOS)
        img.paste(ph, (int(x0s[col]), int(y0s[r])))
        ly = y0s[r] + th + 22
        if col == 0:
            text(d, (x0s[col], ly), name, lf)
        else:
            text(d, (x0s[col] + tw, ly), name, lf, anchor="r")
    # centre card with the front view
    cw, ch = 800, 520
    card = Image.new("RGBA", (cw + 120, ch + 120), (0, 0, 0, 0))
    ImageDraw.Draw(card).rounded_rectangle((60, 76, cw + 60, ch + 76), radius=70, fill=(0, 0, 0, 70))
    card = card.filter(ImageFilter.GaussianBlur(24))
    cx, cy = S / 2, y0s[0] + th + gy / 2 + 10
    img.alpha_composite(card, (int(cx - cw / 2 - 60), int(cy - ch / 2 - 60)))
    face = Image.new("RGBA", (cw, ch), (0, 0, 0, 0))
    ImageDraw.Draw(face).rounded_rectangle((0, 0, cw - 1, ch - 1), radius=70, fill=CREAM + (255,))
    img.alpha_composite(face, (int(cx - cw / 2), int(cy - ch / 2)))
    cam = fit_w(front_cut(c), 600)
    place(img, cam, cx, cy + cam.height / 2 + 10)
    return img.convert("RGB")


def gift(c):
    img = ImageOps.fit(Image.open(src(PICKS[f"gift_{c}"])).convert("RGB"), (S, S), Image.LANCZOS).convert("RGBA")
    d = ImageDraw.Draw(img)
    text(d, (150, 120), typeset(COPY["gift_headline"]), tinos(210))
    text(d, (160, 360), typeset(COPY["gift_second_line"]), tinos(110), MUTE)
    lx, ly = PICKS.get("gift_label", {}).get(c, (1470, 560))
    lf = inter(62, "Medium")
    text(d, (lx, ly), typeset(COPY["gift_arrow_label"]), lf)
    ax, ay = PICKS.get("gift_arrow_to", {}).get(c, (1500, 800))
    arrow(d, [(lx + 120, ly + 90), (lx + 70, ly + 150), (ax, ay)])
    for (x, y, r) in [(1780, 160, 36), (1560, 330, 26), (1860, 430, 30), (110, 560, 30), (140, 1660, 34),
                      (1900, 1780, 40), (1120, 1700, 28)]:
        sparkle(d, x, y, r)
    return img.convert("RGB")


def box(c):
    img = ImageOps.fit(Image.open(src(PICKS[f"box_{c}"])).convert("RGB"), (S, S), Image.LANCZOS).convert("RGBA")
    d = ImageDraw.Draw(img)
    bf = inter(60, "Bold")
    badge = typeset(COPY["box_badge"]).upper()
    bw = measure(bf, badge)
    bx, by = PICKS["box_badge_xy"][c]
    d.rounded_rectangle((bx, by, bx + bw + 100, by + 130), radius=65, fill=NAVY)
    text(d, (bx + 50, by + 30), badge, bf, (255, 255, 255))
    lf = inter(62, "Medium")
    for key in ["camera", "cable", "strap", "card"]:
        spec = PICKS["box_labels"][c][key]
        (tx, ty), anchor, ctrl, tip = spec["text"], spec.get("anchor", "l"), spec["ctrl"], spec["tip"]
        w = text(d, (tx, ty), typeset(COPY[f"box_label_{key}"]), lf, anchor=anchor)
        arrow(d, [tuple(spec["start"]), tuple(ctrl), tuple(tip)])
    return img.convert("RGB")


BUILD = {"hand": hand, "howto": howto, "usbc": usbc, "frontback": frontback, "filters": filters, "gift": gift,
         "box": box}
RENDERED_BACK = {"howto", "usbc", "frontback"}  # show back/bottom/port views that come from renders, not photos
SUFFIX = {"filters": "_ILLUSTRATIVE"}  # filter samples are renders, not photos taken with a Retra


def main():
    which = sys.argv[1:] or list(BUILD)
    for k in which:
        for c in COLOURS:
            im = BUILD[k](c)
            assert im.size == (S, S)
            suffix = "_RENDERED-BACK" if k in RENDERED_BACK else SUFFIX.get(k, "")
            name = f"RET_gallery_{k}_{c}{suffix}.jpg"
            im.save(OUT / name, quality=92)
            print(name)


if __name__ == "__main__":
    main()
