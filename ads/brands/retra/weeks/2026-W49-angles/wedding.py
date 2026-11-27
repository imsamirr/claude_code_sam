"""Wedding-memories statics W1-W5, formats from Sam's references (RTR text bubbles, The Knot quiz card / dark flash
headline / iOS reminder, Olive & Piper bridal product hero).
    python3 wedding.py [W1 ...]  -> output/RET_A49_<id>_..._{9x16,4x5}.png   (Sam wants the 4:5 files)
Copy: copy_wedding.json (StefanBrain). Scenes: renders/w1-w4 (wedding_render.py).
"""
import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from lib import *  # noqa: F401,F403
import lib
from layouts import S, COPY
import b2
from b2 import head, sub, scrim_top, scrim_bottom, SH, WARM
from pain import ios_alert

HERE = Path(__file__).resolve().parent
COPY.update({c["id"]: c for c in json.load(open(HERE / "copy_wedding.json"))["concepts"]})
b2.PICK.update({})  # takes chosen after QA
IM_GREY = (233, 233, 235)
IM_BLUE = (88, 96, 230)
PINK = (255, 92, 168)


def tinos_i(size, track=-0.02):
    f = ImageFont.truetype(str(lib.FONTS / "Tinos-Italic.ttf"), size)
    f.track = track * size
    return f


def wordmark(img, y, color=WHITE, size=64):
    f = tinos(size, -0.03)
    draw_text(ImageDraw.Draw(img), (W / 2 - measure(f, "Retra") / 2, y), "Retra", f, color)
    lib.TEXT_BOXES.append((W / 2 - 120, y, W / 2 + 120, y + size))


def bubble(img, text, y, right, fill, fg, maxw=720, size=38):
    f, ls = fit(text, lambda q: inter(q, "Medium"), maxw, 3, size, 28)
    asc, desc = f.getmetrics()
    lh = (asc + desc) * 1.15
    tw = max(measure(f, ln) for ln in ls)
    bw, bh = tw + 64, len(ls) * lh + 36
    x0 = W - 70 - bw if right else 70
    ImageDraw.Draw(img).rounded_rectangle((x0, y, x0 + bw, y + bh), 40, fill=fill)
    draw_lines(img, ls, f, x0 + 32, y + 16, fg, "left", 1.15, None, tw + 4)
    lib.TEXT_BOXES.append((x0, y, x0 + bw, y + bh))
    return y + bh


# ---------------------------------------------------------------- W1 flash photo + text-message bubbles (RTR)
def w1(c):
    img = b2.full("w1", (0.5, 0.45))
    scrim_bottom(img, 940, 150)
    y = bubble(img, S(c, "bubble_1"), 1010, False, IM_GREY, (20, 20, 22)) + 20
    y = bubble(img, S(c, "bubble_2"), y, True, IM_BLUE, WHITE) + 14
    y = bubble(img, S(c, "bubble_3"), y, True, IM_BLUE, WHITE) + 14
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((W - 70 - 130, y, W - 70, y + 66), 33, fill=IM_BLUE)
    for k in range(3):
        cx = W - 70 - 100 + k * 35
        d.ellipse((cx - 8, y + 25, cx + 8, y + 41), fill=(230, 232, 255))
    wordmark(img, 1560, WHITE, 52)
    return img


# ---------------------------------------------------------------- W2 dance-floor photo + white quiz-style card (Knot)
def w2(c):
    img = b2.full("w2", (0.5, 0.45))
    x0, y0, x1 = 70, 1300, 760
    f, ls = fit(S(c, "card_headline"), lambda q: inter(q, "Bold"), x1 - x0 - 80, 2, 64, 44)
    asc, desc = f.getmetrics()
    hh = len(ls) * (asc + desc) * 1.05
    y1 = y0 + 50 + hh + 30 + 50 + 40
    sh = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle((x0, y0 + 10, x1, y1 + 10), 36, fill=(0, 0, 0, 90))
    img.alpha_composite(sh.filter(lib.ImageFilter.GaussianBlur(18)))
    ImageDraw.Draw(img).rounded_rectangle((x0, y0, x1, y1), 36, fill=(255, 255, 255))
    y = draw_lines(img, ls, f, x0 + 40, y0 + 46, (15, 15, 15), "left", 1.05, None, x1 - x0 - 80)
    draw_lines(img, [S(c, "card_cta") + " →"], inter(38, "SemiBold"), x0 + 40, y + 26, (15, 15, 15), "left", 1, None,
               x1 - x0 - 80)
    lib.TEXT_BOXES.append((x0, y0, x1, y1))
    # small party stickers like the reference
    d = ImageDraw.Draw(img)
    for (cx, cy, r, col) in [(150, 560, 26, (255, 120, 170)), (130, 1080, 20, (255, 196, 60)), (930, 1500, 22, (120, 200, 255))]:
        d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=col)
    f_ = tinos(56, -0.03)
    draw_text(ImageDraw.Draw(img), (W - 70 - measure(f_, "Retra"), 330), "Retra", f_, WHITE)
    return img


# ---------------------------------------------------------------- W3 dark first-dance flash photo + headline + link (Knot)
def w3(c):
    img = b2.full("w3", (0.5, 0.6))
    scrim_top(img, 820, 235)
    f, ls = fit(S(c, "headline"), lambda q: inter(q, "Bold"), 900, 2, 76, 52)
    y = draw_lines(img, ls, f, 90, 340, WHITE, "center", 1.08, None, 900)
    fl = inter(38, "SemiBold")
    t = S(c, "link_cta")
    tw = measure(fl, t)
    glow = Image.new("RGBA", img.size, (0, 0, 0, 0))  # soft dark halo so the link reads over the string lights
    ImageDraw.Draw(glow).rounded_rectangle((W / 2 - tw / 2 - 40, y + 6, W / 2 + tw / 2 + 40, y + 96), 45, fill=(0, 0, 0, 170))
    img.alpha_composite(glow.filter(lib.ImageFilter.GaussianBlur(22)))
    d = ImageDraw.Draw(img)
    draw_text(d, (W / 2 - tw / 2, y + 22), t, fl, PINK)
    d.line([(W / 2 - tw / 2, y + 22 + 48), (W / 2 + tw / 2, y + 22 + 48)], fill=PINK, width=3)
    lib.TEXT_BOXES.append((W / 2 - tw / 2, y + 22, W / 2 + tw / 2, y + 74))
    scrim_bottom(img, 1400, 120)
    wordmark(img, 1530, WHITE, 64)
    return img


# ---------------------------------------------------------------- W4 iOS reminder over a couple photo (Knot)
def w4(c):
    img = b2.full("w4", (0.5, 0.5))
    ios_alert(img, S(c, "alert_title"), S(c, "alert_body"), 1270, w=700,
              buttons=(S(c, "button_left"), S(c, "button_right")))
    scrim_bottom(img, 1380, 130)
    wordmark(img, 1530, WHITE, 64)
    return img


# ---------------------------------------------------------------- W5 bridal product hero on white (Olive & Piper)
def w5(c):
    img = canvas(WHITE)
    k = S(c, "kicker").upper()
    fk = inter(30, "Medium")
    fk.track = 0.12 * 30 if hasattr(fk, "track") else 0
    draw_lines(img, [k], fk, 80, 330, (60, 60, 60), "center", 1, None, 920)
    hl, it = S(c, "headline"), S(c, "headline_italic_word")
    fr, fi = tinos(84, -0.02), tinos_i(84, -0.02)
    words = hl.split()
    lines, cur = [], []
    for w_ in words:  # wrap by measured width with mixed fonts
        test = cur + [w_]
        wd = sum(measure(fi if x.strip(".,!") == it else fr, x + " ") for x in test)
        if wd > 900 and cur:
            lines.append(cur)
            cur = [w_]
        else:
            cur = test
    lines.append(cur)
    d = ImageDraw.Draw(img)
    y = 390
    for ln in lines:
        wd = sum(measure(fi if x.strip(".,!") == it else fr, x + " ") for x in ln) - measure(fr, " ")
        x = W / 2 - wd / 2
        for x_ in ln:
            f = fi if x_.strip(".,!") == it else fr
            draw_text(d, (x, y), x_, f, (25, 25, 25))
            x += measure(f, x_ + " ")
        y += 96
    lib.TEXT_BOXES.append((90, 390, 990, y))
    box = prod(img, "p34_chalk", 860, 640, y + 400)
    # callout: thin line from the label to the leatherette panel
    fy = y + 520
    fc = inter(28, "Regular")
    ct = S(c, "callout")
    ls = wrap(ct, fc, 190)
    draw_lines(img, ls, fc, 60, fy + 14, (60, 60, 60), "left", 1.2, None, 190)
    d = ImageDraw.Draw(img)
    d.line([(60, fy), (330, fy)], fill=(120, 120, 120), width=2)
    lib.TEXT_BOXES.append((60, fy, 250, fy + 130))
    pl = S(c, "product_line").upper()
    fp = inter(30, "Medium")
    draw_lines(img, [pl], fp, 80, 1470, (60, 60, 60), "center", 1, None, 920)
    wordmark(img, 1515, INK, 76)
    return img


# ---------------------------------------------------------------- W6-W9 through the Retra lens + iOS alert (W4 style)
LOOK = None
LOOKS = {"vintage": "Vintage", "bw": "Black & White", "film": "Film"}


def lens(c, k, colour, cen=(0.5, 0.45)):
    """Narrowed vision: the scene sharp inside a rounded frame window, blurred and darkened outside, frame marks,
    iOS alert over the lower edge, the camera + wordmark in the dark margin."""
    base = b2.full(k, cen)
    if LOOK:  # Sam: versions in Retra's looks (landing-page curves)
        from compose_gallery import retra_filter
        base = retra_filter(base, LOOK).convert("RGBA")
    out = base.filter(lib.ImageFilter.GaussianBlur(22))
    out = Image.blend(out.convert("RGB"), Image.new("RGB", out.size, (0, 0, 0)), 0.7).convert("RGBA")
    x0, y0, x1, y1 = 140, 380, 940, 1200
    m = Image.new("L", base.size, 0)
    ImageDraw.Draw(m).rounded_rectangle((x0, y0, x1, y1), 34, fill=255)
    out.paste(base, (0, 0), m.filter(lib.ImageFilter.GaussianBlur(3)))
    img = out
    d = ImageDraw.Draw(img)
    L, i_ = 60, 26
    for (x, y, sx, sy) in [(x0 + i_, y0 + i_, 1, 1), (x1 - i_, y0 + i_, -1, 1), (x0 + i_, y1 - i_, 1, -1), (x1 - i_, y1 - i_, -1, -1)]:
        d.line([(x, y), (x + sx * L, y)], fill=(255, 255, 255), width=5)
        d.line([(x, y), (x, y + sy * L)], fill=(255, 255, 255), width=5)
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2  # small centre focus brackets
    for sx in (-1, 1):
        for sy in (-1, 1):
            d.line([(cx + sx * 40, cy + sy * 40), (cx + sx * 40, cy + sy * 22)], fill=(255, 255, 255, 200), width=3)
            d.line([(cx + sx * 40, cy + sy * 40), (cx + sx * 22, cy + sy * 40)], fill=(255, 255, 255, 200), width=3)
    ios_alert(img, S(c, "alert_title"), S(c, "alert_body"), y1 + 40, w=720,
              buttons=(S(c, "button_left"), S(c, "button_right")))
    if LOOK:  # filter name pill in the frame's top-left corner
        pill(img, LOOK, inter(28, "SemiBold"), x0 + 40 + measure(inter(28, "SemiBold"), LOOK) / 2 + 22, y0 + 104,
             (20, 18, 16), (255, 236, 200), padx=22, pady=10)
    place(img, cam(colour, 320, -6), 260, 1498, shadow=0.5, blur=16, drop=(4, 14))
    f = tinos(64, -0.03)
    draw_text(ImageDraw.Draw(img), (W - 90 - measure(f, "Retra"), 1505), "Retra", f, WHITE)
    lib.TEXT_BOXES.append((W - 300, 1505, W - 90, 1575))
    return img


def w6(c):
    return lens(c, "w6", "blossom")


def w7(c):
    return lens(c, "w7", "pine")


def w8(c):
    return lens(c, "w8", "chalk", (0.5, 0.4))


def w9(c):
    return lens(c, "w9", "sol")


BUILDERS = {"W1": w1, "W2": w2, "W3": w3, "W4": w4, "W5": w5, "W6": w6, "W7": w7, "W8": w8, "W9": w9}
SLUG = {"W1": "wedding-text-bubbles", "W2": "wedding-card-cta", "W3": "wedding-first-dance-headline",
        "W4": "wedding-ios-reminder", "W5": "wedding-bridal-product-hero",
        "W6": "wedding-lens-sparkler-exit", "W7": "wedding-lens-bridal-party", "W8": "wedding-lens-confetti-aisle",
        "W9": "wedding-lens-guest-toast"}

if __name__ == "__main__":
    sys.path.insert(0, str(HERE.parents[1] / "gallery"))
    args = sys.argv[1:] or list(BUILDERS)  # "W6:film" builds one look; "W6:all" builds the three looks
    jobs = []
    for a_ in args:
        i, _, lk = a_.partition(":")
        jobs += [(i, k_) for k_ in (LOOKS if lk == "all" else [lk])] if lk else [(i, None)]
    for i, lk in jobs:
        lib.TEXT_BOXES.clear()
        c = COPY[i]
        LOOK = LOOKS.get(lk)
        try:
            print(save(BUILDERS[i](i), f"RET_A49_{i}_{c['funnel'].lower()}_{SLUG[i]}" + (f"_{lk}" if lk else "")))
        except Exception as e:  # noqa: BLE001
            import traceback
            traceback.print_exc()
            print("FAIL", i, repr(e))
