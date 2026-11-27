"""Magic Kingdom statics (D1-D4): being in the moment on a Disney trip. Own formats, not from the inspiration picks.
    python3 disney.py [D1 ...]  -> output/RET_A49_<id>_<funnel>_<slug>_{9x16,4x5}.png
Copy: copy_disney.json (StefanBrain). Scenes: renders/d* (disney_render.py). Real Cinderella Castle by Sam's choice.
"""
import json
import math
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageOps

from lib import *  # noqa: F401,F403
import lib
from layouts import S, COPY, rounded
import b2
from b2 import head, sub, scrim_top, scrim_bottom, SH, WARM

HERE = Path(__file__).resolve().parent
COPY.update({c["id"]: c for c in json.load(open(HERE / "copy_disney.json"))["concepts"]})
b2.PICK.update({"d1": "d1b_t1"})  # takes chosen after QA
PAPER = (250, 247, 240)


def hand(img, text, x, y, w, size=46, color=WHITE, lines=3, align="left", shadow=None):
    f, ls = fit(text, lambda q: shantell(q, bold=True), w, lines, size, int(size * 0.7))
    return draw_lines(img, ls, f, x, y, color, align, 1.1, shadow, w)


def arrow(img, p0, p1, color=WHITE, width=6, bend=0.25):
    """Hand-drawn style curved arrow from p0 to p1 (quadratic curve + open head)."""
    d = ImageDraw.Draw(img)
    (x0, y0), (x1, y1) = p0, p1
    mx, my = (x0 + x1) / 2, (y0 + y1) / 2
    cx, cy = mx - (y1 - y0) * bend, my + (x1 - x0) * bend
    pts = [((1 - t) ** 2 * x0 + 2 * (1 - t) * t * cx + t ** 2 * x1, (1 - t) ** 2 * y0 + 2 * (1 - t) * t * cy + t ** 2 * y1)
           for t in [i / 40 for i in range(41)]]
    d.line(pts, fill=color, width=width, joint="curve")
    ang = math.atan2(y1 - pts[-4][1], x1 - pts[-4][0])
    for s in (2.6, -2.6):
        d.line([(x1, y1), (x1 - 34 * math.cos(ang + s / 6), y1 - 34 * math.sin(ang + s / 6))], fill=color, width=width)


def print_card(photo, w, ph, cap_h, rot):
    """A snapshot print: white border, photo, caption strip; returned rotated with a soft shadow, plus its photo box."""
    pad = 18
    card = Image.new("RGBA", (w, pad + ph + cap_h), (255, 255, 255, 255))
    card.paste(ImageOps.fit(photo, (w - 2 * pad, ph), Image.LANCZOS, centering=(0.5, 0.45)), (pad, pad))
    sh = Image.new("RGBA", (card.width + 80, card.height + 80), (0, 0, 0, 0))
    ImageDraw.Draw(sh).rectangle((40, 50, 40 + card.width, 50 + card.height), fill=(0, 0, 0, 70))
    sh = sh.filter(ImageFilter.GaussianBlur(14))
    sh.alpha_composite(card, (40, 40))
    return sh.rotate(rot, Image.BICUBIC, expand=True)


# ---------------------------------------------------------------- D1 annotated fireworks
def d1(c):
    # the camera hangs at y~1780 of the render; lift the photo 280px so it sits inside the 4:5 band, and fill the
    # bottom (below the 4:5 crop) with a darkened mirror of the last rows
    SHIFT = 280
    ph = ImageOps.fit(b2.R("d1"), (W, H), Image.LANCZOS).convert("RGBA")
    img = canvas(WHITE)
    img.alpha_composite(ph, (0, -SHIFT))
    tail = ImageOps.flip(ph.crop((0, H - SHIFT, W, H))).filter(ImageFilter.GaussianBlur(12))
    img.alpha_composite(tail, (0, H - SHIFT))
    scrim_top(img, 700, 190)
    head(img, S(c, "headline"), 330, WARM, 88, 58, 2, shadow=SH)
    hand(img, S(c, "note_phones"), 560, 600, 470, 46, WHITE, 2, "right", SH)
    arrow(img, (900, 720), (960, 800), WHITE, 6, -0.3)
    YEL = (255, 226, 140)
    hand(img, S(c, "note_family"), 660, 1250, 390, 46, YEL, 2, "left", SH)
    arrow(img, (700, 1255), (640, 1180), YEL, 6, 0.3)
    scrim_bottom(img, 1380, 170)
    sub(img, S(c, "bottom_line"), 1450, WHITE, 36, 26, 3, x=480, w=560, align="left", shadow=SH, weight="SemiBold")
    return img


# ---------------------------------------------------------------- D2 snapshot board
def d2(c):
    img = canvas(WHITE)
    y = head(img, S(c, "headline"), 320, INK, 84, 56, 2)
    y = sub(img, S(c, "sub"), y + 10, BODY, 34, 26, 2)
    top = y + 20
    spots = [(290, top + 230, -4), (790, top + 245, 3), (300, top + 715, 3), (780, top + 725, -3)]
    for i, (k, (cx, cy, rot)) in enumerate(zip(["d2a", "d2b", "d2c", "d2d"], spots), 1):
        card = print_card(b2.R(k), 420, 360, 84, rot)
        img.alpha_composite(card, (int(cx - card.width / 2), int(cy - card.height / 2)))
        cap = S(c, f"caption_{i}")
        tmp = Image.new("RGBA", (400, 76), (0, 0, 0, 0))
        hand(tmp, cap, 0, 14, 396, 34, INK, 1, "center")
        tmp = tmp.rotate(rot, Image.BICUBIC, expand=True)
        # caption sits on the print's bottom strip: offset from centre along the rotated vertical axis
        r = math.radians(rot)
        off = (18 + 360 + 42) - (18 + 360 + 84) / 2  # card centre -> caption strip centre
        img.alpha_composite(tmp, (int(cx + off * math.sin(r) - tmp.width / 2), int(cy + off * math.cos(r) - tmp.height / 2)))
        lib.TEXT_BOXES.append((cx - 210, cy, cx + 210, cy + 300))
    return img


def photo_print(photo, w, h, border=26, rot=0.0):
    """A plain lab print (4x6 style, even white border - not an instant-film shape) with a soft drop shadow."""
    card = Image.new("RGBA", (w, h), (252, 251, 248, 255))
    card.paste(ImageOps.fit(photo, (w - 2 * border, h - 2 * border), Image.LANCZOS), (border, border))
    sh = Image.new("RGBA", (w + 90, h + 90), (0, 0, 0, 0))
    ImageDraw.Draw(sh).rectangle((45, 58, 45 + w, 58 + h), fill=(0, 0, 0, 75))
    sh = sh.filter(ImageFilter.GaussianBlur(16))
    sh.alpha_composite(card, (45, 45))
    return sh.rotate(rot, Image.BICUBIC, expand=True)


def faded(im):
    """Age a print: lift blacks, warm cast, lower saturation."""
    from PIL import ImageEnhance
    im = ImageEnhance.Color(im.convert("RGB")).enhance(0.8)
    a = Image.new("RGB", im.size, (236, 214, 180))
    return Image.blend(im, a, 0.12)


# ---------------------------------------------------------------- D3 your parents' Disney photos vs yours
def d3(c):
    img = canvas(WHITE)
    y = head(img, S(c, "headline"), 320, INK, 80, 54, 2)
    top = int(y + 34)
    ph = 760
    # left: album page with two faded prints and photo corners
    lx0, lx1 = 40, 520
    ImageDraw.Draw(img).rounded_rectangle((lx0, top, lx1, top + ph), 14, fill=(238, 229, 211))
    for k, (cx, cy, w_, h_, rot) in [("d3v1", (280, top + 200, 400, 310, 3)), ("d3v2", (270, top + 530, 270, 350, -4))]:
        pr = photo_print(faded(b2.R(k)), w_, h_, 16, rot)
        img.alpha_composite(pr, (int(cx - pr.width / 2), int(cy - pr.height / 2)))
    pill(img, S(c, "left_label"), inter(30, "Bold"), (lx0 + lx1) / 2, top + ph + 44, NAVY50, WHITE, padx=22, pady=10)
    # right: a generic phone camera roll of near-identical shots
    rx0, rx1 = 570, 1040
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((rx0, top, rx1, top + ph), 56, fill=(18, 18, 20))
    sx0, sy0, sx1, sy1 = rx0 + 18, top + 18, rx1 - 18, top + ph - 18
    d.rounded_rectangle((sx0, sy0, sx1, sy1), 42, fill=(255, 255, 255))
    src = b2.R("d3p")
    cols, gap = 4, 4
    cw = (sx1 - sx0 - 2 * 12 - (cols - 1) * gap) // cols
    from PIL import ImageEnhance
    yy, i = sy0 + 70, 0
    while yy + cw <= sy1 - 40:
        for col in range(cols):
            dx, dy, z = (i * 37) % 9 / 100, (i * 53) % 7 / 100, 1 + (i % 5) * 0.03
            w0 = int(src.width / z)
            x0 = int((src.width - w0) * (0.3 + dx))
            y0 = int((src.height - w0) * (0.3 + dy))
            t = src.crop((x0, y0, x0 + w0, y0 + w0)).resize((cw, cw), Image.LANCZOS)
            t = ImageEnhance.Brightness(t).enhance(0.92 + (i % 4) * 0.04)
            img.paste(t, (sx0 + 12 + col * (cw + gap), yy))
            i += 1
        yy += cw + gap
    d = ImageDraw.Draw(img)
    d.rounded_rectangle(((rx0 + rx1) / 2 - 70, top + 30, (rx0 + rx1) / 2 + 70, top + 58), 14, fill=(18, 18, 20))
    pill(img, S(c, "right_label"), inter(30, "Bold"), (rx0 + rx1) / 2, top + ph + 44, INK, WHITE, padx=22, pady=10)
    yb = top + ph + 100
    prod(img, "p34_chalk", 300, 230, min(yb + 120, 1500))
    sub(img, S(c, "product_line"), min(yb + 60, 1440), INK, 36, 26, 3, x=420, w=600, align="left", weight="SemiBold")
    return img


# ---------------------------------------------------------------- D4 printed film-look photo + camera beside it
def d4(c):
    img = canvas(WHITE)
    y = head(img, S(c, "headline"), 320, INK, 76, 52, 2)
    y = sub(img, S(c, "sub"), y + 8, BODY, 34, 26, 2)
    top = int(y + 20)
    pr = photo_print(b2.R("d4p"), 780, 520, 26, 3.5)
    img.alpha_composite(pr, (int(W / 2 - 40 - pr.width / 2), top))
    pb = top + pr.height
    prod(img, "p34_chalk", 340, 810, pb - 60)
    d = ImageDraw.Draw(img)
    gap = 140
    x0 = W / 2 - gap * 3
    yy = pb + 100
    f = inter(22, "Medium")
    for i, n in enumerate(lib.STORE_ORDER):
        cx = x0 + i * gap
        d.ellipse((cx - 30, yy, cx + 30, yy + 60), fill=SWATCH[n], outline=(210, 214, 218), width=2)
        nm = lib.STORE_NAME[n]
        draw_text(d, (cx - measure(f, nm) / 2, yy + 70), nm, f, BODY)
    lib.TEXT_BOXES.append((x0 - 60, yy, x0 + gap * 6 + 60, yy + 100))
    pill(img, S(c, "cta"), inter(36, "SemiBold"), W / 2, min(yy + 175, 1575), "cta", WHITE, padx=56, pady=18)
    return img


# ---------------------------------------------------------------- D1V / D1F fireworks split: regular | filtered
def split(c, filt):
    from compose_gallery import retra_filter
    base = ImageOps.fit(b2.R("d5"), (W, H), Image.LANCZOS).convert("RGB")
    right = retra_filter(base, filt)
    img = base.convert("RGBA")
    img.paste(right.crop((W // 2, 0, W, H)), (W // 2, 0))
    scrim_top(img, 640, 170)
    scrim_bottom(img, 1360, 200)
    d = ImageDraw.Draw(img)
    d.line([(W / 2, 560), (W / 2, 1450)], fill=WHITE, width=6)  # divider stops short of the headline and sub
    head(img, S(c, "headline"), 330, WARM, 86, 58, 2, shadow=SH)
    d = ImageDraw.Draw(img)
    cy = 1010
    d.ellipse((W / 2 - 46, cy - 46, W / 2 + 46, cy + 46), fill=WHITE)
    for sgn in (-1, 1):  # slider arrows
        x = W / 2 + sgn * 14
        d.polygon([(x, cy - 16), (x, cy + 16), (x + sgn * 18, cy)], fill=INK)
    fl = inter(32, "Bold")
    pill(img, S(c, "left_label"), fl, W / 4, 600, (0, 0, 0, 0) if False else (20, 22, 26), WHITE, padx=24, pady=12)
    pill(img, S(c, "right_label"), fl, 3 * W / 4, 600, SAND, INK, padx=24, pady=12)
    sub(img, S(c, "sub"), 1500, WHITE, 40, 28, 2, shadow=SH, weight="SemiBold")
    return img


def d1v(c):
    return split(c, "Vintage")


def d1f(c):
    return split(c, "Film")


PLACE = {}  # per-render note / arrow positions, set after seeing the chosen take
BUILDERS = {"D1": d1, "D2": d2, "D3": d3, "D4": d4, "D1V": d1v, "D1F": d1f}
SLUG = {"D1": "disney-fireworks-annotated", "D2": "disney-snapshot-board", "D3": "disney-parents-album-vs-camera-roll",
        "D4": "disney-main-street-colours",
        "D1V": "disney-fireworks-split-vintage", "D1F": "disney-fireworks-split-film"}

if __name__ == "__main__":
    sys.path.insert(0, str(HERE.parents[1] / "gallery"))
    ids = sys.argv[1:] or list(BUILDERS)
    for i in ids:
        lib.TEXT_BOXES.clear()
        c = COPY[i]
        tag = "_ILLUSTRATIVE" if i in ("D2", "D1V", "D1F") else ""
        try:
            print(save(BUILDERS[i](i), f"RET_A49_{i}_{c['funnel'].lower()}_{SLUG[i]}{tag}"))
        except Exception as e:  # noqa: BLE001
            import traceback
            traceback.print_exc()
            print("FAIL", i, repr(e))
