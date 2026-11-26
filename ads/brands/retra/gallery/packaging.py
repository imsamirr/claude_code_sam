"""Retra retail box artwork (front panel, one per colour) in the style of Sam's packaging reference.

    python3 packaging.py   ->  packaging/retra_box_front_<colour>.png (2400x1500, 1.6:1)

Words: gallery_copy.json["packaging"] (StefanBrain). Type: landing-page system (Tinos / Inter, navy #022B49,
gold wordmark). Icons are simple line drawings made here. No eco/green claims (not substantiated).
"""
import json
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

HERE = Path(__file__).resolve().parent
FONTS = HERE.parent / "fonts"
OUT = HERE / "packaging"
OUT.mkdir(exist_ok=True)
REPO = HERE.parents[3]
CUT = REPO / "assets/retra/product/cutout"
W, H = 2400, 1500
NAVY = (2, 43, 73)
BODY = (65, 96, 119)
GOLD = (176, 141, 72)
PILL = (220, 230, 238)
PAPER = (252, 251, 249)
COPY = json.load(open(HERE / "gallery_copy.json"))["packaging"]


def tinos(size, track=-0.03):
    f = ImageFont.truetype(str(FONTS / "Tinos-Regular.ttf"), size)
    f.track = track * size
    return f


def inter(size, weight="Medium", track=0.0):
    f = ImageFont.truetype(str(FONTS / "Inter.ttf"), size)
    f.set_variation_by_name(weight)
    f.track = track * size
    return f


def measure(f, t):
    return f.getlength(t) + f.track * max(0, len(t) - 1)


def text(d, xy, t, f, fill=NAVY, anchor="l"):
    x, y = xy
    w = measure(f, t)
    x -= {"l": 0, "c": w / 2, "r": w}[anchor]
    for i, ch in enumerate(t):
        gx = f.getlength(t[: i + 1]) - f.getlength(ch) + i * f.track
        d.text((x + gx, y), ch, font=f, fill=fill)
    return w


# ---- line icons, drawn in a 120x120 box at (x, y) ----
LW = 7


def ic_noscreen(d, x, y):
    d.rounded_rectangle((x + 10, y + 22, x + 110, y + 98), radius=10, outline=NAVY, width=LW)
    d.line([(x + 6, y + 112), (x + 114, y + 8)], fill=NAVY, width=LW)


def ic_filters(d, x, y):
    for cx, cy in [(42, 42), (78, 42), (42, 78), (78, 78)]:
        d.ellipse((x + cx - 30, y + cy - 30, x + cx + 30, y + cy + 30), outline=NAVY, width=LW - 2)


def ic_nofilm(d, x, y):
    d.rectangle((x + 14, y + 26, x + 106, y + 94), outline=NAVY, width=LW)
    for k in range(4):
        d.rectangle((x + 24 + k * 22, y + 32, x + 32 + k * 22, y + 40), fill=NAVY)
        d.rectangle((x + 24 + k * 22, y + 80, x + 32 + k * 22, y + 88), fill=NAVY)
    d.line([(x + 6, y + 112), (x + 114, y + 8)], fill=NAVY, width=LW)


def ic_card(d, x, y):
    d.polygon([(x + 30, y + 10), (x + 76, y + 10), (x + 92, y + 26), (x + 92, y + 110), (x + 30, y + 110)],
              outline=NAVY, width=LW)
    for k in range(4):
        d.line([(x + 42 + k * 12, y + 22), (x + 42 + k * 12, y + 40)], fill=NAVY, width=5)


def ic_usbc(d, x, y):
    d.rounded_rectangle((x + 36, y + 8, x + 84, y + 60), radius=10, outline=NAVY, width=LW)
    d.rounded_rectangle((x + 48, y + 60, x + 72, y + 80), radius=8, outline=NAVY, width=LW - 2)
    d.line([(x + 60, y + 80), (x + 60, y + 116)], fill=NAVY, width=LW)
    d.rounded_rectangle((x + 46, y + 22, x + 74, y + 34), radius=6, fill=NAVY)


def ic_battery(d, x, y):
    d.rounded_rectangle((x + 8, y + 32, x + 100, y + 88), radius=10, outline=NAVY, width=LW)
    d.rectangle((x + 100, y + 48, x + 112, y + 72), fill=NAVY)
    d.polygon([(x + 60, y + 38), (x + 38, y + 64), (x + 56, y + 64), (x + 48, y + 84), (x + 72, y + 56),
               (x + 54, y + 56)], fill=NAVY)


ICONS = [ic_noscreen, ic_filters, ic_nofilm, ic_card, ic_usbc, ic_battery]


def front(colour, camera=True):
    rng = np.random.default_rng(5)
    base = np.array(PAPER, float)[None, None, :] + rng.normal(0, 1.2, (H, W, 1))
    img = Image.fromarray(np.clip(base, 0, 255).astype("uint8")).convert("RGBA")
    d = ImageDraw.Draw(img)
    # pill, top-left
    pf = inter(40, "SemiBold", 0.04)
    pt = COPY["pill"].upper()
    pw = measure(pf, pt)
    d.rounded_rectangle((90, 80, 90 + pw + 80, 160), radius=40, fill=PILL)
    text(d, (130, 98), pt, pf)
    # wordmark + descriptor
    text(d, (W / 2, 70), "Retra", tinos(150, -0.02), GOLD, "c")
    text(d, (W / 2, 250), COPY["descriptor"].upper(), inter(58, "SemiBold", 0.12), NAVY, "c")
    # camera photo
    if not camera:  # lid version: branding only, larger wordmark in the middle
        d = ImageDraw.Draw(img)
        text(d, (W / 2, 520), "Retra", tinos(330, -0.02), GOLD, "c")
        return _icons_and_tagline(img).convert("RGB")
    import compose_gallery  # straight-on front cut-outs (Chalk via its green-screen mask)
    cam = compose_gallery.front_cut(colour)
    cw = 1100
    cam = cam.resize((cw, int(cam.height * cw / cam.width)), Image.LANCZOS)
    cx, top = W / 2, 430
    sh = Image.new("RGBA", (cam.width + 200, cam.height + 200), (0, 0, 0, 0))
    sh.paste(Image.new("RGBA", cam.size, (40, 30, 20, 90)), (100, 130), cam.getchannel("A"))
    img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(30)), (int(cx - cam.width / 2 - 100), top - 100))
    img.alpha_composite(cam, (int(cx - cam.width / 2), top))
    return _icons_and_tagline(img).convert("RGB")


def _icons_and_tagline(img):
    # icons: three each side
    lf = inter(40, "Medium")
    d = ImageDraw.Draw(img)
    for i, (fn, label) in enumerate(zip(ICONS, COPY["icon_labels"])):
        side, row = divmod(i, 3)
        x = 150 if side == 0 else W - 150 - 120
        y = 420 + row * 300
        fn(d, x, y)
        words = label.split()
        k2 = (len(words) + 1) // 2
        lines = [label] if measure(lf, label) < 300 else [" ".join(words[:k2]), " ".join(words[k2:])]
        for k, ln in enumerate([l for l in lines if l]):
            text(d, (x + 60, y + 135 + k * 48), ln, lf, BODY, "c")
    # tagline
    text(d, (W / 2, H - 200), COPY["tagline"].upper(), tinos(78, 0.02), NAVY, "c")
    d.line([(W / 2 - 60, H - 90), (W / 2 + 60, H - 90)], fill=GOLD, width=4)
    return img


if __name__ == "__main__":
    for c in ["chalk", "obsidian", "sol"]:
        front(c).save(OUT / f"retra_box_front_{c}.png")
        print(c)
    front("chalk", camera=False).save(OUT / "retra_box_lid.png")
    print("lid")
