"""Lifestyle-scene layouts for the W49 angles batch (4K Kie renders in renders/, picks below).
    python3 scenes.py [ids...]  -> output/RET_A49_<id>_..._{9x16,4x5}.png
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageOps

from lib import *  # noqa: F401,F403
import lib
from layouts import S, text_block, tick, rounded

HERE = Path(__file__).resolve().parent
R = HERE / "renders"
PICKS = {"01": "01_t1", "03": "03_t1", "05a": "05a_t2", "05b": "05b_t1", "06": "06_t1", "12": "12_t1", "13": "13_t2"}


def src(k):
    return Image.open(R / f"{PICKS[k]}.png").convert("RGB")


def full(k, centering=(0.5, 0.5)):
    return ImageOps.fit(src(k), (W, H), Image.LANCZOS, centering=centering).convert("RGBA")


def tiktok_caption(img, text, y, size=44, maxw=900, align="center"):
    """TikTok-style caption: each line on its own white rounded block."""
    f, lines = fit(text, lambda s: inter(s, "SemiBold"), maxw - 40, 4, size, 32)
    asc, desc = f.getmetrics()
    lh = asc + desc + 18
    d = ImageDraw.Draw(img)
    for i, ln in enumerate(lines):
        tw = measure(f, ln)
        x = (W - tw) / 2 if align == "center" else 70
        box = (x - 20, y + i * lh - 6, x + tw + 20, y + i * lh + lh - 10)
        d.rounded_rectangle(box, 14, fill=(255, 255, 255))
        lib.TEXT_BOXES.append(box)
    for i, ln in enumerate(lines):
        tw = measure(f, ln)
        x = (W - tw) / 2 if align == "center" else 70
        draw_text(d, (x, y + i * lh + 2), ln, f, (18, 18, 18))
    return y + len(lines) * lh


# ---------------------------------------------------------------- 01 wedding: X-style post from Retra's account
def s01(cid):
    img = canvas(WHITE)
    d = ImageDraw.Draw(img)
    x0, y0 = 60, 330
    d.ellipse((x0, y0, x0 + 96, y0 + 96), fill=INK)  # avatar: Retra wordmark monogram
    fa = tinos(52, -0.02)
    draw_text(d, (x0 + 48 - measure(fa, "R") / 2, y0 + 14), "R", fa, (232, 205, 140))
    fn, fh = inter(36, "Bold"), inter(34, "Regular")
    name = S(cid, "display_name", "Retra")
    draw_text(d, (x0 + 120, y0 + 6), name, fn, (15, 20, 25))
    draw_text(d, (x0 + 120, y0 + 52), f'{S(cid, "handle", "@retra")} · {S(cid, "date", "Nov 28")}', fh, (83, 100, 113))
    lib.TEXT_BOXES.append((x0, y0, x0 + 700, y0 + 96))
    f, lines = fit(S(cid, "post_text", "Post"), lambda s: inter(s, "Regular"), 960, 6, 40, 30)
    y = draw_lines(img, wrap(S(cid, "post_text", "Post"), f, 960), f, x0, y0 + 130, (15, 20, 25), "left", 1.28, None, 960)
    ph = 1600 - (y + 26)
    photo = ImageOps.fit(src("01"), (960, int(ph)), Image.LANCZOS, centering=(0.45, 0.5))
    img.alpha_composite(rounded(photo, 32), (x0, int(y + 26)))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((x0, y + 26, x0 + 960, y + 26 + ph), 32, outline=(207, 217, 222), width=2)
    return img


# ---------------------------------------------------------------- 03 sensory: dark close-up + callouts
def s03(cid):
    img = full("03", (0.5, 0.42))
    scrim(img, 0, 700, (0, 0, 0), 120, "down")
    text_block(img, S(cid, "headline", "Headline"), lambda s: tinos(s, -0.04), 80, 340, 920, 2, 88, 60,
               (245, 240, 232), "center", 1.1)
    # camera sits ~y 700-1200 in this crop; labels in two rows underneath with leader lines up to it
    fl = inter(32, "SemiBold")
    d = ImageDraw.Draw(img)
    slots = [(285, 1330, 300), (795, 1330, 780), (285, 1450, 420), (795, 1450, 660)]
    for i, (cx, cy, ax) in enumerate(slots, 1):
        t = S(cid, f"callout_{i}", "")
        d.line([(cx, cy - 26), (ax, 1185)], fill=(235, 228, 216), width=2)
        d.ellipse((ax - 7, 1185 - 7, ax + 7, 1185 + 7), fill=(235, 228, 216))
        pill(img, t, fl, cx, cy, (20, 20, 22), (240, 234, 224), padx=22, pady=12)
        d = ImageDraw.Draw(img)
    return img


# ---------------------------------------------------------------- 05 solo travel: split phone vs Retra
def s05(cid):
    img = canvas(WHITE)
    y = text_block(img, S(cid, "headline", "Headline"), tinos, 70, 320, 940, 2, 76, 56, INK, "center")
    top = int(y + 24)
    half = (1635 - top - 12) // 2
    PW = 430  # stats panel width; photo fills the rest, cropped to its subject
    rows = [("05a", (0.56, 0.55), "left_label", "left_", False), ("05b", (0.41, 0.45), "right_label", "right_", True)]
    for r_, (k, cen, lab, pre, ok) in enumerate(rows):
        yy = top + r_ * (half + 12)
        ph = ImageOps.fit(src(k), (W - PW, half), Image.LANCZOS, centering=cen).convert("RGBA")
        img.alpha_composite(ph, (PW, yy))
        ImageDraw.Draw(img).rectangle((0, yy, PW - 1, yy + half - 1), fill=(14, 16, 20) if not ok else INK)
        draw_lines(img, [S(cid, lab, "")], tinos(58, -0.03), 44, yy + 40, WHITE, "left", 1.0, None, PW - 70)
        d = ImageDraw.Draw(img)
        ty = yy + 140
        for i in (1, 2, 3):
            t = S(cid, f"{pre}{i}", "")
            col = (95, 200, 160) if ok else (240, 110, 100)
            d.ellipse((44, ty + 2, 84, ty + 42), fill=col)
            tick(d, 53, ty + 11, 22, WHITE, ok, 5)
            f, ls = fit(t, lambda s: inter(s, "SemiBold"), PW - 130, 2, 32, 24)
            ty = draw_lines(img, ls, f, 100, ty + 2, WHITE, "left", 1.15, None, PW - 130) + 22
            d = ImageDraw.Draw(img)
    return img


# ---------------------------------------------------------------- 06 theme park: POV caption
def s06(cid):
    img = full("06", (0.5, 0.5))
    tiktok_caption(img, S(cid, "pov_caption", "POV"), 330, 46, 940)
    scrim(img, 1380, 1700, (0, 0, 0), 150, "up")
    text_block(img, S(cid, "sub", "Sub"), lambda s: inter(s, "SemiBold"), 90, 1530, 900, 1, 40, 30, WHITE, "center",
               1.1, (0, 0, 0, 160))
    return img


# ---------------------------------------------------------------- 12 honeymoon: caption bubble
def s12(cid):
    img = full("12", (0.5, 0.5))
    tiktok_caption(img, S(cid, "caption", "Caption"), 330, 46, 940)
    return img


# ---------------------------------------------------------------- 13 parents' gift: bow + headline
def s13(cid):
    img = canvas(WHITE)
    y = text_block(img, S(cid, "headline", "Headline"), lambda s: tinos(s, -0.04), 80, 330, 920, 3, 84, 58, INK,
                   "center", 1.1)
    y = text_block(img, S(cid, "sub", "Sub"), lambda s: inter(s, "Regular"), 90, y + 12, 900, 2, 36, 28, BODY, "center", 1.25)
    ph_top = int(y + 36)
    photo = src("13")
    photo = photo.crop((0, 1270, photo.width, photo.height))  # below the flat band Kie left at the top
    photo = ImageOps.fit(photo, (W, H - ph_top), Image.LANCZOS, centering=(0.5, 0.75))
    img.alpha_composite(photo.convert("RGBA"), (0, ph_top))
    return img


BUILDERS = {"01": s01, "03": s03, "05": s05, "06": s06, "12": s12, "13": s13}
NAMES = {"01": "tof_wedding-post", "03": "tof_sensory-calm", "05": "tof_solo-travel-split", "06": "tof_theme-park-pov",
         "12": "tof_honeymoon-pov", "13": "tof_screen-free-gift"}

if __name__ == "__main__":
    for i in sys.argv[1:] or list(BUILDERS):
        lib.TEXT_BOXES.clear()
        print(save(BUILDERS[i](i), f"RET_A49_{i}_{NAMES[i]}"))
