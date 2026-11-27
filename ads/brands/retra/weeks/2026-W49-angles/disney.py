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
b2.PICK.update({"d1": "d1_t1", "d3": "d3_t1", "d4": "d4_t1"})  # takes chosen after QA
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


# ---------------------------------------------------------------- D3 postcard to future you
def d3(c):
    img = canvas(WHITE)
    y = head(img, S(c, "headline"), 320, INK, 84, 56, 2)
    top = int(y + 20)
    # front: photo postcard
    fw, fh = 820, 520
    front = Image.new("RGBA", (fw, fh), (255, 255, 255, 255))
    front.paste(ImageOps.fit(b2.R("d3"), (fw - 36, fh - 36), Image.LANCZOS, centering=(0.5, 0.5)), (18, 18))
    # back: message side
    bw, bh = 920, 560
    back = Image.new("RGBA", (bw, bh), PAPER + (255,))
    d = ImageDraw.Draw(back)
    d.line([(bw * 0.56, 60), (bw * 0.56, bh - 50)], fill=(200, 190, 175), width=3)
    hand(back, S(c, "message"), 40, 46, int(bw * 0.56) - 60, 30, INK, 11)
    for k in range(3):
        d.line([(bw * 0.6, 300 + k * 70), (bw - 40, 300 + k * 70)], fill=(200, 190, 175), width=3)
    hand(back, S(c, "to_line"), int(bw * 0.6), 240, int(bw * 0.4) - 40, 34, INK, 2)
    hand(back, S(c, "signoff"), int(bw * 0.6), 470, int(bw * 0.4) - 40, 32, INK, 1)
    # stamp with the camera
    sx, sy, sw, shh = bw - 190, 40, 150, 180
    d.rectangle((sx, sy, sx + sw, sy + shh), fill=(255, 255, 255), outline=(190, 60, 60), width=4)
    lib.prod(back, "p34_sol", 120, sx + sw / 2, sy + shh / 2)
    for i, (card, cx, cy, rot) in enumerate([(front, W / 2 - 20, top + 290, -3), (back, W / 2 + 15, top + 800, 2)]):
        sh = Image.new("RGBA", (card.width + 80, card.height + 80), (0, 0, 0, 0))
        ImageDraw.Draw(sh).rectangle((40, 52, 40 + card.width, 52 + card.height), fill=(0, 0, 0, 80))
        sh = sh.filter(ImageFilter.GaussianBlur(16))
        sh.alpha_composite(card, (40, 40))
        sh = sh.rotate(rot, Image.BICUBIC, expand=True)
        img.alpha_composite(sh, (int(cx - sh.width / 2), int(cy - sh.height / 2)))
    lib.TEXT_BOXES.append((80, top + 520, 1000, top + 1080))
    return img


# ---------------------------------------------------------------- D4 hero photo + white band with colours
def d4(c):
    img = canvas(WHITE)
    ph = 1000
    img.alpha_composite(ImageOps.fit(b2.R("d4"), (W, ph), Image.LANCZOS, centering=(0.5, 0.4)).convert("RGBA"), (0, 0))
    y = head(img, S(c, "headline"), ph + 30, INK, 72, 50, 2)
    y = sub(img, S(c, "sub"), y + 8, BODY, 34, 26, 2)
    d = ImageDraw.Draw(img)
    names = [n.title() for n in COLOURS]
    gap = 160
    x0 = W / 2 - gap * 2.5
    yy = y + 30
    for i, n in enumerate(COLOURS):
        cx = x0 + i * gap
        d.ellipse((cx - 30, yy, cx + 30, yy + 60), fill=SWATCH[n], outline=(210, 214, 218), width=2)
        f = inter(24, "Medium")
        draw_text(d, (cx - measure(f, names[i]) / 2, yy + 70), names[i], f, BODY)
    lib.TEXT_BOXES.append((x0 - 40, yy, x0 + gap * 5 + 40, yy + 100))
    pill(img, S(c, "cta"), inter(36, "SemiBold"), W / 2, min(yy + 170, 1580), "cta", WHITE, padx=56, pady=18)
    return img


PLACE = {}  # per-render note / arrow positions, set after seeing the chosen take
BUILDERS = {"D1": d1, "D2": d2, "D3": d3, "D4": d4}
SLUG = {"D1": "disney-fireworks-annotated", "D2": "disney-snapshot-board", "D3": "disney-postcard-future-you",
        "D4": "disney-main-street-colours"}

if __name__ == "__main__":
    ids = sys.argv[1:] or list(BUILDERS)
    for i in ids:
        lib.TEXT_BOXES.clear()
        c = COPY[i]
        tag = "_ILLUSTRATIVE" if i == "D2" else ""
        try:
            print(save(BUILDERS[i](i), f"RET_A49_{i}_{c['funnel'].lower()}_{SLUG[i]}{tag}"))
        except Exception as e:  # noqa: BLE001
            import traceback
            traceback.print_exc()
            print("FAIL", i, repr(e))
