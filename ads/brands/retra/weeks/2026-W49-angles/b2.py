"""Batch 2 (ids 20-59): Sam's remaining picked formats with the agreed angles.
    python3 b2.py [ids...]  -> output/RET_A49_<id>_<funnel>_<slug>_{9x16,4x5}.png
Copy: copy_b2.json (StefanBrain). Scenes: renders/s*.png (batch2.py), product photos: renders/p*.png (products.py).
"""
import json
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps

from lib import *  # noqa: F401,F403
import lib
from layouts import S, text_block, tick, rounded, raw, SAMPLES, COPY
from scenes import tiktok_caption

HERE = Path(__file__).resolve().parent
COPY.update({c["id"]: c for c in json.load(open(HERE / "copy_b2.json"))["concepts"]})
PICK = {"s34": "s34b_t1", "s30a": "s30a_t2", "s32": "s32_t2", "s36": "s36_t3", "s42a": "s42a_t2", "s56a": "s56a_t2"}
WARM = (247, 240, 226)


def R(k):
    return Image.open(HERE / "renders" / f"{PICK.get(k, k + '_t1')}.png").convert("RGB")


def full(k, cen=(0.5, 0.5), trim_bottom=0.0):
    im = R(k)
    if trim_bottom:
        im = im.crop((0, 0, im.width, int(im.height * (1 - trim_bottom))))
    return ImageOps.fit(im, (W, H), Image.LANCZOS, centering=cen).convert("RGBA")


def whiten(k, width, fade=0.0):
    """A whole white-sweep scene levelled to pure white (no isolation), optional fade of the outer edges."""
    a = lib._level_white(np.asarray(R(k)).astype(np.float32))
    if fade:
        import cv2
        h, w = a.shape[:2]
        m = np.zeros((h, w), np.float32)
        m[int(h * fade):int(h * (1 - fade)), int(w * fade):int(w * (1 - fade))] = 1
        m = cv2.GaussianBlur(m, (0, 0), w * fade / 2.5)[..., None]
        a = a * m + 255 * (1 - m)
    im = Image.fromarray(a.astype("uint8"))
    return im.resize((width, int(im.height * width / im.width)), Image.LANCZOS)


def head(img, text, y, color=INK, size=96, floor=60, lines=3, x=70, w=940, align="center", shadow=None):
    return text_block(img, text, lambda s: tinos(s, -0.04), x, y, w, lines, size, floor, color, align, 1.1, shadow)


def sub(img, text, y, color=BODY, size=38, floor=26, lines=2, x=90, w=900, align="center", shadow=None, weight="Regular"):
    return text_block(img, text, lambda s: inter(s, weight), x, y, w, lines, size, floor, color, align, 1.25, shadow)


def photo(img, k, box, cen=(0.5, 0.5), radius=24, filt=None, src=None):
    x0, y0, x1, y1 = [int(v) for v in box]
    im = src if src is not None else R(k)
    im = ImageOps.fit(im, (x1 - x0, y1 - y0), Image.LANCZOS, centering=cen)
    if filt:
        from compose_gallery import retra_filter
        im = retra_filter(im, filt)
    img.alpha_composite(rounded(im, radius) if radius else im.convert("RGBA"), (x0, y0))


def checklist(img, items, x, y, w, ok=True, size=34, color=INK, dot=None, gap=20):
    d = ImageDraw.Draw(img)
    dot = dot or ((29, 111, 95) if ok else NAVY50)
    for t in items:
        if not t:
            continue
        s = int(size * 1.25)
        d.ellipse((x, y + 2, x + s, y + 2 + s), fill=dot)
        tick(d, x + s * .22, y + 2 + s * .25, s * .56, WHITE, ok, max(3, s // 9))
        f, ls = fit(t, lambda q: inter(q, "Medium"), w - s - 18, 2, size, int(size * .75))
        y = draw_lines(img, ls, f, x + s + 18, y, color, "left", 1.18, None, w - s - 18) + gap
        d = ImageDraw.Draw(img)
    return y


def badge(img, text, cx, cy, r, bg=INK, fg=WHITE, size=44):
    d = ImageDraw.Draw(img)
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=bg)
    f, ls = fit(text, lambda q: tinos(q, -0.03), r * 1.5, 2, size, 24)
    asc, desc = f.getmetrics()
    th = len(ls) * (asc + desc) * 1.0
    draw_lines(img, ls, f, cx - r, cy - th / 2 - 4, fg, "center", 1.0, None, 2 * r)


def scrim_top(img, y1=760, a=150):
    scrim(img, 0, y1, (0, 0, 0), a, "down")


def scrim_bottom(img, y0=1250, a=170):
    scrim(img, y0, H, (0, 0, 0), a, "up")


def card(img, box, fill=(244, 246, 248), radius=28):
    ImageDraw.Draw(img).rounded_rectangle(box, radius, fill=fill)


def phone_icon(d, cx, cy, h, color=INK, width=6):
    w = h * 0.52
    d.rounded_rectangle((cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2), h * 0.09, outline=color, width=width)
    d.ellipse((cx - h * .04, cy + h * .38, cx + h * .04, cy + h * .46), fill=color)


SH = (0, 0, 0, 150)  # text shadow on photos


# ---------------------------------------------------------------- scenes with a headline
def b20(c):
    img = full("s20", (0.5, 0.62))
    y = head(img, S(c, "headline"), 360, INK, 110, 72)
    sub(img, S(c, "sub"), y + 12, INK)
    return img


def b21(c):
    img = canvas(WHITE)
    y = head(img, S(c, "headline"), 340, INK, 92, 60)
    emo = S(c, "emoji", "📵")
    try:
        ef = ImageFont.truetype("/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf", 109)
        e = Image.new("RGBA", (160, 160), (0, 0, 0, 0))
        ImageDraw.Draw(e).text((10, 10), emo, font=ef, embedded_color=True)
        e = e.crop(e.getbbox()).resize((520, 520), Image.LANCZOS)
        img.alpha_composite(e, (int(W / 2 - 260), int(y + 60)))
    except OSError:
        pass
    prod(img, "p34_sol", 330, W - 230, 1390)
    ImageDraw.Draw(img).rectangle((0, 1505, W, H), fill=INK)
    sub(img, S(c, "bar"), 1540, WHITE, 38, 28, 1, weight="SemiBold")
    return img


def b23(c):
    img = full("s23", (0.5, 0.55))
    scrim_top(img, 820, 170)
    head(img, S(c, "headline"), 360, WARM, 84, 56, 4, shadow=SH)
    return img


def b25(c):
    img = full("s25", (0.5, 0.6))
    sub(img, S(c, "kicker").upper(), 360, KICKER, 40, 28, 1, weight="SemiBold")
    head(img, S(c, "headline"), 420, INK, 150, 96, 2)
    pill(img, S(c, "pill"), inter(38, "SemiBold"), W / 2, 1540, "cta", WHITE, padx=60, pady=22)
    return img


def b26(c):
    img = full("s26", (0.5, 0.5))
    head(img, S(c, "headline"), 340, WHITE, 90, 60, 2, shadow=SH)
    fl = inter(32, "SemiBold")
    pos = [(200, 640, 400, 760), (880, 640, 690, 760), (200, 1220, 420, 1040), (880, 1220, 670, 1040)]
    d = ImageDraw.Draw(img)
    for i, (lx, ly, ax, ay) in enumerate(pos, 1):
        d.line([(lx, ly), (ax, ay)], fill=WHITE, width=3)
        d.ellipse((ax - 8, ay - 8, ax + 8, ay + 8), fill=WHITE)
        pill(img, S(c, f"label_{i}"), fl, lx, ly, WHITE, INK, padx=22, pady=12)
        d = ImageDraw.Draw(img)
    return img


def b29(c):
    img = full("s29", (0.5, 0.62))
    y = head(img, S(c, "headline"), 360, WARM, 100, 66, 2)
    sub(img, S(c, "sub"), y + 14, (205, 196, 182))
    return img


def b41(c):
    img = full("s41", (0.5, 0.45))
    d = ImageDraw.Draw(img)
    card(img, (70, 330, 1010, 640), (255, 255, 255))
    d.ellipse((100, 362, 172, 434), fill=INK)
    draw_text(d, (136 - measure(tinos(40), "R") / 2, 372), "R", tinos(40), (232, 205, 140))
    draw_text(d, (192, 372), S(c, "comment_name", "retra"), inter(34, "Bold"), (15, 20, 25))
    f, ls = fit(S(c, "comment_text"), lambda q: inter(q, "Regular"), 800, 4, 36, 28)
    draw_lines(img, ls, f, 192, 424, (15, 20, 25), "left", 1.25, None, 800)
    ImageDraw.Draw(img).rectangle((0, 1290, W, H), fill=WHITE)
    for cx, n in [(220, "p34_chalk"), (540, "p34_sol"), (860, "p34_blossom")]:
        prod(img, n, 280, cx, 1450)
    return img


def b43(c):
    img = full("s43", (0.5, 0.55))
    head(img, S(c, "headline"), 340, INK, 84, 56, 3)
    return img


def b46(c):
    img = full("s46", (0.5, 0.5))
    scrim_top(img, 700, 130)
    head(img, S(c, "headline"), 350, WARM, 92, 60, 2, shadow=SH)
    fl = inter(26, "SemiBold")
    for i, cx in enumerate([190, 540, 890], 1):
        pill(img, S(c, f"tag_{i}"), fl, cx, 1550, WHITE, INK, padx=18, pady=10)
    return img


def b47(c):
    img = full("s47", (0.5, 0.5))
    y = tiktok_caption(img, S(c, "title"), 330, 44, 960)
    for i in (1, 2, 3, 4):
        y = tiktok_caption(img, S(c, f"week_{i}"), y + 18, 34, 960)
    return img


def b48(c):
    img = full("s48", (0.5, 0.5))
    tiktok_caption(img, S(c, "caption_1"), 340, 44, 960)
    tiktok_caption(img, S(c, "caption_2"), 1400, 40, 960)
    return img


def b49(c):
    img = full("s49", (0.5, 0.5))
    scrim_top(img, 820, 210)
    head(img, S(c, "headline"), 350, WARM, 96, 62, 3, shadow=SH)
    pill(img, S(c, "badge"), inter(34, "SemiBold"), W / 2, 1560, INK, WHITE, padx=30, pady=14)
    return img


def b53(c):
    img = full("s53", (0.5, 0.6))
    scrim_top(img, 760, 120)
    head(img, S(c, "headline"), 360, WARM, 96, 62, 2, shadow=SH)
    fl = inter(32, "SemiBold")
    xs = [230, 540, 850]
    for i, cx in enumerate(xs, 1):
        pill(img, S(c, f"pill_{i}"), fl, cx, 620, (255, 255, 255), INK, padx=20, pady=12)
    badge(img, S(c, "sticker"), 880, 1480, 120, (226, 172, 46), INK, 52)
    return img


def b57(c):
    img = full("s57", (0.5, 0.55))
    tiktok_caption(img, S(c, "caption"), 340, 44, 960)
    return img


def b58(c):
    img = full("s58", (0.5, 0.5))
    hl = S(c, "headline").upper()
    f, ls = fit(hl, lambda q: inter(q, "Black"), 960, 3, 120, 70)
    y = draw_lines(img, ls, f, 60, 360, WHITE, "center", 0.98, SH, 960)
    sub(img, S(c, "sub"), y + 16, WHITE, 40, 28, 2, shadow=SH, weight="SemiBold")
    return img


def b59(c):
    img = full("s59", (0.5, 0.5), trim_bottom=0.07)
    scrim_top(img, 860, 220)
    y = head(img, S(c, "headline"), 350, WHITE, 92, 60, 3, shadow=SH)
    sub(img, S(c, "sub"), y + 14, (235, 228, 240), shadow=SH)
    return img


# ---------------------------------------------------------------- white layouts with product photos
def letter(c, title_k, body_k, close_k, product_name, side=False):
    from layouts import side_column
    img = canvas(WHITE)
    y = head(img, S(c, title_k), 350, INK, 92, 60, 2, x=80, w=920, align="left")
    ImageDraw.Draw(img).line([(80, y + 14), (240, y + 14)], fill=SAND, width=5)
    y += 50
    top = int(y)
    TW = 560 if side else 920
    body = S(c, body_k)
    size = 46
    while size > 26:
        f = tinos(size, -0.02)
        need = len(wrap(body, f, TW)) * sum(f.getmetrics()) * 1.3
        if y + need < (1500 if side else 1320):
            break
        size -= 1
    f = tinos(size, -0.02)
    y = draw_lines(img, wrap(body, f, TW), f, 80, y, (30, 50, 66), "left", 1.3, None, TW)
    if close_k:
        draw_lines(img, [S(c, close_k)], shantell(46 if side else 48), 80, y + 24, INK, "left", 1.0, None, TW)
    if side:
        side_column(img, top - 10, product_name.replace("p34_", ""))
    else:
        prod(img, product_name, 340, W - 230, 1500)
    return img


def b22(c):
    return letter(c, "title", "body", "closing", "p34_chalk")


def b44(c):
    return letter(c, "title", "body", None, "p34_obsidian")


def b50(c):
    return letter(c, "title", "body", "signoff", "p34_sol", side=True)


def b24(c):
    img = canvas(WHITE)
    y = head(img, S(c, "headline"), 330, INK, 92, 60, 2)
    y = sub(img, S(c, "sub"), y + 8, BODY, 36, 26, 2)
    multiply(img, whiten("s24", 900, fade=0.05), W / 2, y + 450)
    labels = [S(c, k) for k in ("box_camera", "box_cable", "box_strap", "box_card", "box_giftbox")]
    fl = inter(28, "SemiBold")
    row = [labels[:3], labels[3:]]
    yy = 1400
    for r in row:
        ws = [measure(fl, t) + 44 for t in r]
        x = (W - sum(ws) - 16 * (len(r) - 1)) / 2
        for t, w_ in zip(r, ws):
            pill(img, t, fl, x + w_ / 2, yy, (238, 241, 244), INK, padx=22, pady=10)
            x += w_ + 16
        yy += 66
    pill(img, S(c, "price_line"), inter(34, "SemiBold"), W / 2, 1560, "cta", WHITE, padx=50, pady=18)
    return img


def b27(c):
    img = canvas(WHITE)
    y = head(img, S(c, "headline"), 340, INK, 90, 60, 2)
    prod(img, "p34_chalk", 780, W / 2, y + 400)
    d = ImageDraw.Draw(img)
    cy = 1390
    for i, cx in enumerate([150, 410, 670, 930]):
        r = 46
        if i == 0:  # vintage: sun-faded circle
            d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(214, 182, 130))
        elif i == 1:  # black & white: half-filled circle
            d.ellipse((cx - r, cy - r, cx + r, cy + r), outline=INK, width=5)
            d.pieslice((cx - r, cy - r, cx + r, cy + r), 90, 270, fill=INK)
        elif i == 2:  # natural: sun
            d.ellipse((cx - 22, cy - 22, cx + 22, cy + 22), fill=(226, 172, 46))
            for k in range(8):
                import math
                a = k * math.pi / 4
                d.line([(cx + 30 * math.cos(a), cy + 30 * math.sin(a)), (cx + 44 * math.cos(a), cy + 44 * math.sin(a))],
                       fill=(226, 172, 46), width=5)
        else:  # film: strip
            d.rectangle((cx - 50, cy - 34, cx + 50, cy + 34), outline=INK, width=5)
            for k in range(4):
                d.rectangle((cx - 40 + k * 22, cy - 28, cx - 32 + k * 22, cy - 20), fill=INK)
                d.rectangle((cx - 40 + k * 22, cy + 20, cx - 32 + k * 22, cy + 28), fill=INK)
        f, ls = fit(S(c, f"icon_{i + 1}"), lambda q: inter(q, "SemiBold"), 230, 2, 30, 22)
        draw_lines(img, ls, f, cx - 115, cy + 66, INK, "center", 1.15, None, 230)
        d = ImageDraw.Draw(img)
    return img


def b28(c):
    img = canvas(WHITE)
    y = head(img, S(c, "headline"), 330, INK, 88, 58, 2, x=70, w=940, align="left")
    fb = inter(34, "Medium")
    y += 40
    for i in range(1, 6):
        t = S(c, f"bubble_{i}")
        tw = measure(fb, t)
        left = i % 2 == 1
        x0 = 70 if left else W - 70 - tw - 60
        box = (x0, y, x0 + tw + 60, y + 86)
        ImageDraw.Draw(img).rounded_rectangle(box, 40, fill=(232, 238, 243) if left else INK)
        draw_text(ImageDraw.Draw(img), (x0 + 30, y + 22), t, fb, INK if left else WHITE)
        lib.TEXT_BOXES.append(box)
        y += 112
    prod(img, "p34_pine", 380, W - 250, max(y + 140, 1460))
    return img


def b30(c):
    img = canvas(WHITE)
    y = head(img, S(c, "headline"), 320, INK, 88, 58, 2)
    top = int(y + 24)
    for i, (k, lab, pre, ok) in enumerate([("s30a", "left_label", "left_", False), ("s30b", "right_label", "right_", True)]):
        x0 = 60 + i * 500
        photo(img, k, (x0, top, x0 + 460, top + 560), (0.5, 0.4), 22)
        pill(img, S(c, lab), inter(30, "Bold"), x0 + 230, top + 520, INK if ok else NAVY50, WHITE, padx=20, pady=10)
        checklist(img, [S(c, f"{pre}{j}") for j in (1, 2, 3, 4)], x0, top + 600, 460, ok, 28, INK, gap=14)
    return img


def b31(c):
    img = canvas(WHITE)
    y = head(img, S(c, "headline"), 350, INK, 96, 62, 2)
    sub(img, S(c, "sub"), y + 10)
    multiply(img, whiten("s31", 900, fade=0.16), W / 2, 1150)
    return img


def b32(c):
    img = full("s32", (0.5, 0.5))
    d = ImageDraw.Draw(img)
    f1 = shantell(84, bold=True)
    y = draw_lines(img, balanced(S(c, "line_1"), f1, 900), f1, 90, 360, NAVY50, "center", 1.1, None, 900)
    y = draw_lines(img, balanced(S(c, "line_2"), f1, 900), f1, 90, y + 6, INK, "center", 1.1, None, 900)
    # marker sketches: phone (left) vs our camera taped up (right)
    d = ImageDraw.Draw(img)
    phone_icon(d, 300, y + 260, 300, (60, 60, 64), 8)
    d.line([(190, y + 120), (410, y + 400)], fill=(178, 34, 34), width=10)
    prod(img, "p34_sol", 400, 760, y + 260)
    fl = shantell(46)
    draw_lines(img, [S(c, "left_label")], fl, 150, y + 450, (60, 60, 64), "center", 1, None, 300)
    draw_lines(img, [S(c, "right_label")], fl, 610, y + 450, INK, "center", 1, None, 300)
    return img


def b33(c):
    img = canvas(WHITE)
    y = head(img, S(c, "headline"), 340, INK, 88, 58, 2)
    art = R("s33")
    w_, h_ = art.size
    art = art.crop((int(w_ * .2), int(h_ * .2), int(w_ * .78), int(h_ * .84)))  # the drawing sheet
    art = ImageOps.autocontrast(ImageOps.grayscale(art), cutoff=2).convert("RGB")
    a = np.asarray(art).astype(np.float32)
    a = np.where(a > 150, 255, a * 0.6)
    art = Image.fromarray(a.astype("uint8")).resize((880, int(880 * art.height / art.width)), Image.LANCZOS)
    multiply(img, art, W / 2, y + 60 + art.height / 2)
    yy = y + 90 + art.height
    for i in range(3):
        t = S(c, f"month_{i + 1}")
        day, rest = (t.split(":", 1) + [""])[:2]
        x0 = 60 + i * 330
        draw_lines(img, [day.strip()], tinos(46), x0, yy, INK, "center", 1, None, 300)
        f, ls = fit(rest.strip(), lambda q: inter(q, "Regular"), 290, 4, 30, 22)
        draw_lines(img, ls, f, x0 + 5, yy + 64, BODY, "center", 1.2, None, 290)
    prod(img, "p34_dune", 250, W / 2, 1545)
    return img


def b34(c):
    img = canvas(WHITE)
    y = head(img, S(c, "headline"), 350, INK, 96, 62, 2)
    sub(img, S(c, "sub"), y + 10)
    photo(img, "s34", (90, 740, 990, 1580), (0.5, 0.9), 28)
    return img


def b35(c):
    from compose_gallery import retra_filter
    img = canvas(INK)
    head(img, S(c, "headline"), 360, WARM, 104, 66, 3, x=70, w=940, align="left")
    pr = retra_filter(ImageOps.fit(raw(SAMPLES["ferry"]), (620, 620), Image.LANCZOS), "Vintage")
    cardi = Image.new("RGBA", (660, 720), (250, 247, 240, 255))
    cardi.paste(pr, (20, 20))
    draw_lines(cardi, ["Vintage"], shantell(40), 20, 650, INK, "left", 1, None, 400)
    place(img, cardi.rotate(-4, Image.BICUBIC, expand=True), 600, 1170, shadow=0.6, blur=24, drop=(8, 16))
    return img


def b36(c):
    img = canvas(WHITE)
    y = head(img, S(c, "headline"), 340, INK, 96, 62, 2)
    multiply(img, whiten("s36", 900, fade=0.08), W / 2, y + 470)
    d = ImageDraw.Draw(img)
    cx, cy = W / 2, y + 470
    d.line([(cx - 330, cy - 300), (cx + 330, cy + 300)], fill=(178, 34, 34), width=22)
    d.line([(cx + 330, cy - 300), (cx - 330, cy + 300)], fill=(178, 34, 34), width=22)
    sub(img, S(c, "sub"), 1520)
    return img


def b37(c):
    img = canvas(WHITE)
    y = head(img, S(c, "headline"), 340, INK, 100, 64, 2)
    box = multiply(img, product("s37", 900, share=0.05, shadow=0.04), W / 2, y + 520)
    # printed tray label (bottom-right of the pack): text + barcode
    x0, y0 = box[2] - 360, box[3] - 240
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((x0, y0, x0 + 300, y0 + 170), 10, fill=WHITE, outline=(200, 205, 210), width=2)
    draw_lines(img, [S(c, "label")], inter(28, "Bold"), x0 + 18, y0 + 16, INK, "left", 1, None, 270)
    rng = np.random.default_rng(3)
    xx = x0 + 18
    while xx < x0 + 280:
        bw = int(rng.integers(2, 6))
        d.rectangle((xx, y0 + 70, xx + bw, y0 + 150), fill=(20, 20, 20))
        xx += bw + int(rng.integers(2, 5))
    badge(img, S(c, "sticker"), box[0] + 150, box[1] + 140, 120, (226, 172, 46), INK, 46)
    return img


def b38(c):
    img = canvas(WHITE)
    y = head(img, S(c, "headline"), 360, INK, 130, 84, 2, x=80, w=920, align="left")
    sub(img, S(c, "sub"), y + 20, BODY, 44, 30, 3, x=80, w=860, align="left")
    prod(img, "p34_blossom", 700, 520, 1250)
    badge(img, S(c, "badge"), 880, 1020, 130, INK, WHITE, 64)
    return img


def b39(c):
    img = canvas(WHITE)
    y = head(img, S(c, "headline"), 340, INK, 90, 60, 2)
    prod(img, "p34_chalk", 560, 760, y + 420)
    checklist(img, [S(c, f"list_{i}") for i in range(1, 6)], 60, y + 120, 470, True, 32, INK, gap=34)
    return img


def b40(c):
    img = canvas(WHITE)
    y = head(img, S(c, "headline"), 330, INK, 84, 56, 2)
    top = y + 30
    for i in range(4):
        x0 = 60 + (i % 2) * 490
        y0 = top + (i // 2) * 360
        card(img, (x0, y0, x0 + 470, y0 + 340), (243, 245, 247))
        draw_lines(img, [str(i + 1)], tinos(64), x0 + 30, y0 + 20, NAVY50, "left", 1, None, 100)
        f, ls = fit(S(c, f"card_{i + 1}"), lambda q: inter(q, "Medium"), 410, 5, 34, 24)
        draw_lines(img, ls, f, x0 + 30, y0 + 110, INK, "left", 1.22, None, 410)
    prod(img, "p34_obsidian", 300, W / 2, top + 2 * 360 + 120)
    return img


def b42(c):
    img = canvas(WHITE)
    y = head(img, S(c, "headline"), 330, INK, 88, 58, 2)
    top = int(y + 30)
    photo(img, "s42a", (60, top, 520, top + 700), (0.5, 0.4), 22)
    photo(img, "s42b", (560, top, 1020, top + 700), (0.5, 0.4), 22, filt="Film")
    pill(img, S(c, "left_label"), inter(30, "Bold"), 290, top + 750, NAVY50, WHITE, padx=22, pady=10)
    pill(img, S(c, "right_label"), inter(30, "Bold"), 790, top + 750, INK, WHITE, padx=22, pady=10)
    prod(img, "p34_chalk", 260, W / 2, min(top + 880, 1530))
    return img


def b45(c):
    img = canvas(WHITE)
    y = head(img, S(c, "headline"), 330, INK, 88, 58, 2)
    top = int(y + 30)
    for i, (t, pre, ok, fill) in enumerate([("left_title", "left_", False, (243, 245, 247)),
                                            ("right_title", "right_", True, (233, 241, 246))]):
        x0 = 50 + i * 500
        card(img, (x0, top, x0 + 480, top + 1000), fill)
        d = ImageDraw.Draw(img)
        if ok:
            prod(img, "p34_dune", 360, x0 + 240, top + 200)
        else:
            phone_icon(d, x0 + 240, top + 200, 250, NAVY50, 8)
        draw_lines(img, [S(c, t)], tinos(48), x0 + 20, top + 360, INK, "center", 1, None, 440)
        checklist(img, [S(c, f"{pre}{j}") for j in (1, 2, 3, 4)], x0 + 30, top + 450, 430, ok, 30, INK, gap=22)
    return img


def b51(c):
    img = canvas(WHITE)
    y = head(img, S(c, "headline"), 320, INK, 84, 56, 2)
    top = int(y + 24)
    h_ = (1630 - top - 16) // 2
    photo(img, "s51a", (40, top, 1040, top + h_), (0.5, 0.5), 22)
    photo(img, "s51b", (40, top + h_ + 16, 1040, top + 2 * h_ + 16), (0.5, 0.5), 22)
    pill(img, S(c, "before_label"), inter(30, "Bold"), 180, top + 50, NAVY50, WHITE, padx=22, pady=10)
    pill(img, S(c, "after_label"), inter(30, "Bold"), 200, top + h_ + 66, INK, WHITE, padx=22, pady=10)
    return img


def b52(c):
    img = canvas(WHITE)
    pill(img, S(c, "kicker").upper(), inter(30, "Medium"), W / 2, 360, PILL_DARK, WHITE, padx=30, pady=12)
    y = head(img, S(c, "headline"), 420, INK, 96, 62, 2)
    po, pn = S(c, "price_old"), S(c, "price_new")
    fo, fn = tinos(90), tinos(200, -0.05)
    d = ImageDraw.Draw(img)
    wo, wn = measure(fo, po), measure(fn, pn)
    x = (W - wo - 50 - wn) / 2
    draw_text(d, (x, y + 90), po, fo, NAVY50)
    d.line([(x - 6, y + 90 + 62), (x + wo + 6, y + 90 + 46)], fill=NAVY50, width=7)
    draw_text(d, (x + wo + 50, y), pn, fn, INK)
    lib.TEXT_BOXES.append((x, y, x + wo + 50 + wn, y + 230))
    y2 = checklist(img, [S(c, f"list_{i}") for i in (1, 2, 3)], 250, y + 270, 640, True, 34, INK)
    prod(img, "pfront_chalk", 520, W / 2, y2 + 190, pad=0.0)
    return img


def b54(c):
    img = canvas(WHITE)
    y = head(img, S(c, "headline"), 330, INK, 90, 60, 2)
    prod(img, "p34_obsidian", 620, W / 2, y + 250)
    top = y + 500
    draw_lines(img, ["Ours"], tinos(52), 60, top, INK, "left", 1, None, 460)
    draw_lines(img, ["Your phone"], tinos(52), 560, top, NAVY50, "left", 1, None, 460)
    checklist(img, [S(c, f"ours_{i}") for i in (1, 2, 3, 4)], 60, top + 90, 460, True, 30, INK, gap=22)
    checklist(img, [S(c, f"theirs_{i}") for i in (1, 2, 3, 4)], 560, top + 90, 460, False, 30, (90, 105, 118), gap=22)
    return img


def b55(c):
    img = canvas(WHITE)
    y = 360
    d = ImageDraw.Draw(img)
    for i in (1, 2, 3):
        t = S(c, f"struck_{i}")
        f, ls = fit(t, lambda q: tinos(q, -0.03), 900, 1, 64, 40)
        lw = measure(f, ls[0])
        x = (W - lw) / 2
        draw_lines(img, ls, f, 90, y, NAVY50, "center", 1, None, 900)
        d = ImageDraw.Draw(img)
        d.line([(x - 8, y + f.size * 0.62), (x + lw + 8, y + f.size * 0.62)], fill=NAVY50, width=5)
        y += int(f.size * 1.35)
    y = head(img, S(c, "headline"), y + 40, INK, 92, 60, 3)
    prod(img, "p34_blossom", 620, W / 2, max(y + 260, 1330))
    return img


def b56(c):
    from compose_gallery import retra_filter
    img = canvas(WHITE)
    y = head(img, S(c, "headline"), 330, INK, 88, 58, 2)
    top = int(y + 40)
    for i, (k, lab, hearted) in enumerate([("s56a", "left_label", False), (None, "right_label", True)]):
        x0 = 50 + i * 500
        card(img, (x0, top, x0 + 480, top + 760), (255, 255, 255))
        ImageDraw.Draw(img).rounded_rectangle((x0, top, x0 + 480, top + 760), 24, outline=(220, 225, 230), width=2)
        d = ImageDraw.Draw(img)
        d.ellipse((x0 + 20, top + 20, x0 + 64, top + 64), fill=(220, 225, 230) if not hearted else INK)
        draw_lines(img, [S(c, lab)], inter(28, "Bold"), x0 + 78, top + 28, INK, "left", 1, None, 380)
        if k:
            photo(img, k, (x0, top + 84, x0 + 480, top + 564), (0.5, 0.4), 0)
        else:
            src = raw(SAMPLES["portrait"])
            photo(img, None, (x0, top + 84, x0 + 480, top + 564), (0.5, 0.35), 0, filt="Film", src=src)
        d = ImageDraw.Draw(img)
        hx, hy = x0 + 40, top + 610
        col = (178, 34, 34) if hearted else NAVY50
        import math
        pts = [(hx + 1.3 * 16 * math.sin(t) ** 3, hy - 1.3 * (13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t)
               - math.cos(4 * t))) for t in [i_ * 2 * math.pi / 80 for i_ in range(80)]]
        if hearted:
            d.polygon(pts, fill=col)
        else:
            d.line(pts + [pts[0]], fill=col, width=4, joint="curve")
    prod(img, "p34_chalk", 280, W / 2, min(top + 880, 1540))
    return img


BUILDERS = {k: v for k, v in globals().items() if k.startswith("b") and k[1:].isdigit()}
SLUG = {}

if __name__ == "__main__":
    sys.path.insert(0, str(HERE.parents[1] / "gallery"))
    ids = sys.argv[1:] or sorted(k[1:] for k in BUILDERS)
    for i in ids:
        lib.TEXT_BOXES.clear()
        c = COPY[i]
        fun = c["funnel"].lower()
        slug = "".join(ch if ch.isalnum() else "-" for ch in c["angle"].lower()).strip("-")[:28].strip("-")
        tag = "_ILLUSTRATIVE" if i in ("35", "42", "56") else ""
        try:
            print(save(BUILDERS["b" + i](i), f"RET_A49_{i}_{fun}_{slug}{tag}"))
        except Exception as e:  # noqa: BLE001
            print("FAIL", i, repr(e))
