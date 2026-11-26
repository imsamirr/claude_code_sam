"""KLIK-inspired statics (ids 60-67). python3 klik.py [ids...]
Copy: copy_klik.json (StefanBrain). Scenes: renders/k6x_t*.png (klik_render.py). Product photos: renders/p*.png.
"""
import json
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageOps

from lib import *  # noqa: F401,F403
import lib
from layouts import S, tick, COPY

HERE = Path(__file__).resolve().parent
if (HERE / "copy_klik.json").exists():
    COPY.update({c["id"]: c for c in json.load(open(HERE / "copy_klik.json"))["concepts"]})
PICK = {"k63": "k63_t2"}


def R(k):
    return Image.open(HERE / "renders" / f"{PICK.get(k, k + '_t1')}.png").convert("RGB")


def white_full(k, cen=(0.5, 0.5)):
    a = lib._level_white(np.asarray(R(k)).astype(np.float32))
    return ImageOps.fit(Image.fromarray(a.astype("uint8")), (W, H), Image.LANCZOS, centering=cen).convert("RGBA")


def band(k, white=True):
    """A 4:5 render filling the 4:5 band; above/below continue its edge colour (pure white for white sweeps)."""
    im = R(k)
    if white:
        im = Image.fromarray(lib._level_white(np.asarray(im).astype(np.float32)).astype("uint8"))
    im = ImageOps.fit(im, (W, BOT - TOP), Image.LANCZOS)
    a = np.asarray(im)
    top_c, bot_c = tuple(int(v) for v in np.median(a[:6].reshape(-1, 3), 0)), tuple(int(v) for v in np.median(a[-6:].reshape(-1, 3), 0))
    img = Image.new("RGBA", (W, H), WHITE + (255,))
    ImageDraw.Draw(img).rectangle((0, 0, W, TOP + 40), fill=top_c)
    ImageDraw.Draw(img).rectangle((0, BOT - 40, W, H), fill=bot_c)
    img.alpha_composite(im.convert("RGBA"), (0, TOP))
    return img


def hand(img, text, x, y, w, size=64, floor=40, lines=3, color=INK, align="left", bold=False):
    f, ls = fit(text, lambda s: shantell(s, bold=bold), w, lines, size, floor)
    return draw_lines(img, ls, f, x, y, color, align, 1.15, None, w)


def wordmark(img, y=1560, color=INK, size=60):
    draw_lines(img, ["Retra"], tinos(size, -0.02), 0, y, color, "center", 1, None, W)


def k60(c):
    """Diagonal stair-step built from the six verified product photos (Kie's group shot changed the buttons)."""
    img = canvas(WHITE)
    order = ["chalk", "sol", "blossom", "obsidian", "dune", "pine"]
    for i, col in enumerate(order):
        prod(img, f"p34_{col}", 360, 260 + i * 105, 470 + i * 205)
    hand(img, S(c, "hook"), 520, 360, 500, 70, 46, 3, INK, "right")
    y = 1360
    for i in (1, 2, 3):
        y = hand(img, S(c, f"line_{i}"), 70, y, 520, 40, 28, 1, INK)
    wordmark(img, 1545)
    return img


def k61(c):
    img = band("k61", white=False)
    hand(img, S(c, "line"), 70, 1400, 600, 50, 34, 3, (240, 236, 222))
    return img


def k62(c):
    img = band("k62")
    fade = Image.new("L", (W, H), 0)
    fd = ImageDraw.Draw(fade)
    for x in range(W):
        fd.line([(x, 0), (x, H)], fill=int(255 * min(1, max(0, (520 - x) / 200))))
    img.paste(Image.new("RGBA", (W, H), WHITE + (255,)), (0, 0), fade)
    draw_lines(img, ["Retra"], tinos(60, -0.02), 0, 330, INK, "center", 1, None, W)
    d = ImageDraw.Draw(img)
    x, y = 130, 500
    for i in range(4):
        cy = y + i * 235
        if i == 0:  # no screen
            d.rounded_rectangle((x - 46, cy - 32, x + 46, cy + 32), 8, outline=INK, width=5)
            d.line([(x - 54, cy + 44), (x + 54, cy - 44)], fill=INK, width=5)
        elif i == 1:  # four filters
            for dx, dy in [(-18, -18), (18, -18), (-18, 18), (18, 18)]:
                d.ellipse((x + dx - 20, cy + dy - 20, x + dx + 20, cy + dy + 20), outline=INK, width=4)
        elif i == 2:  # battery
            d.rounded_rectangle((x - 46, cy - 24, x + 38, cy + 24), 8, outline=INK, width=5)
            d.rectangle((x + 38, cy - 10, x + 48, cy + 10), fill=INK)
            d.rectangle((x - 36, cy - 14, x + 26, cy + 14), fill=INK)
        else:  # memory card
            d.polygon([(x - 26, cy - 40), (x + 14, cy - 40), (x + 30, cy - 24), (x + 30, cy + 40), (x - 26, cy + 40)], outline=INK, width=5)
            for k in range(4):
                d.line([(x - 14 + k * 10, cy - 30), (x - 14 + k * 10, cy - 14)], fill=INK, width=3)
        f, ls = fit(S(c, f"icon_{i + 1}"), lambda s: inter(s, "Medium"), 260, 2, 30, 22)
        draw_lines(img, ls, f, x - 110, cy + 60, INK, "center", 1.15, None, 260)
        d = ImageDraw.Draw(img)
    hand(img, S(c, "line"), 60, 1520, 960, 46, 30, 1, INK, "center")
    return img


def k63(c):
    img = white_full("k63", (0.5, 0.5))
    draw_lines(img, ["Retra"], tinos(78, -0.02), 70, 380, INK, "left", 1, None, 400)
    y = 520
    for k in ("big_1", "big_2"):
        f, ls = fit(S(c, k), lambda s: shantell(s, bold=True), 470, 1, 150, 70)
        y = draw_lines(img, ls, f, 70, y, INK, "left", 1.0, None, 470)
    return img


def k64(c):
    img = band("k64")
    nl, nr = S(c, "num_left", "27"), S(c, "num_right", "500")
    fb = tinos(240, -0.05)
    d = ImageDraw.Draw(img)
    wl, wr = measure(fb, nl), measure(fb, nr)
    x = (W - (wl + 120 + wr)) / 2
    y = 330
    draw_text(d, (x, y), nl, fb, NAVY50)
    ax = x + wl + 22
    d.line([(ax, y + 150), (ax + 70, y + 150)], fill=INK, width=8)
    d.polygon([(ax + 70, y + 130), (ax + 96, y + 150), (ax + 70, y + 170)], fill=INK)
    draw_text(d, (x + wl + 120, y), nr, fb, INK)
    lib.TEXT_BOXES.append((x, y, x + wl + 120 + wr, y + 260))
    fl = inter(32, "Regular")
    draw_lines(img, [S(c, "label_left")], fl, x, y + 280, NAVY50, "left", 1, None, wl + 60)
    draw_lines(img, [S(c, "label_right")], fl, x + wl + 120, y + 280, INK, "left", 1, None, wr + 60)
    specs = "  ·  ".join(S(c, f"spec_{i}") for i in (1, 2, 3, 4) if S(c, f"spec_{i}"))
    f, ls = fit(specs, lambda s: inter(s, "Regular"), 960, 2, 28, 20)
    draw_lines(img, ls, f, 60, y + 350, BODY, "center", 1.3, None, 960)
    draw_lines(img, ["Retra"], tinos(60, -0.02), 0, 1530, INK, "right", 1, None, W - 70)
    return img


def k65(c):
    img = canvas(WHITE)
    rw = 760
    rec = Image.new("RGBA", (rw, 1000), (252, 252, 250, 255))
    d = ImageDraw.Draw(rec)
    fm = inter(30, "Medium")
    ft = inter(32, "Bold")

    def rule(y, ch="="):
        x = 40
        while x < rw - 40:
            d.text((x, y), ch, font=fm, fill=(60, 60, 60))
            x += fm.getlength(ch)

    y = 40
    rule(y); y += 36
    t = S(c, "title", "Photography hobby").upper()
    d.text(((rw - ft.getlength(t)) / 2, y), t, font=ft, fill=(30, 30, 30)); y += 50
    rule(y); y += 52
    for i in range(1, 7):
        it = S(c, f"item_{i}")
        if not it:
            continue
        name, price = ([p.strip() for p in it.split("|")] + [""])[:2]
        d.text((40, y), name, font=fm, fill=(30, 30, 30))
        d.text((rw - 40 - fm.getlength(price), y), price, font=fm, fill=(30, 30, 30))
        y += 46
    y += 10; rule(y, "-"); y += 46
    tl = S(c, "total_line", "TOTAL | $99")
    name, price = ([p.strip() for p in tl.split("|")] + [""])[:2]
    d.text((40, y), name.upper(), font=ft, fill=(20, 20, 20))
    d.text((rw - 40 - ft.getlength(price), y), price, font=ft, fill=(20, 20, 20)); y += 60
    rule(y); y += 52
    for k in ("fun_1", "fun_2"):
        d.text((40, y), S(c, k).upper(), font=fm, fill=(30, 30, 30)); y += 46
    y += 10; rule(y); y += 50
    th = S(c, "thanks").upper()
    f2, ls = fit(th, lambda s: inter(s, "Medium"), rw - 80, 2, 28, 20)
    for ln in ls:
        d.text(((rw - f2.getlength(ln)) / 2, y), ln, font=f2, fill=(30, 30, 30)); y += 40
    y += 16; rule(y)
    rec = rec.crop((0, 0, rw, y + 60))
    # torn bottom edge
    m = Image.new("L", rec.size, 255)
    md = ImageDraw.Draw(m)
    rng = np.random.default_rng(4)
    pts = [(0, rec.height)] + [(x, rec.height - 14 + int(rng.integers(0, 12))) for x in range(0, rw + 20, 20)] + [(rw, rec.height)]
    md.polygon(pts + [(rw, rec.height + 2), (0, rec.height + 2)], fill=0)
    rec.putalpha(m)
    place(img, rec, W / 2, 300 + rec.height / 2 + 30, shadow=0.25, blur=22, drop=(0, 14))
    prod(img, "p34_pine", 420, W / 2, 330 + rec.height + 170)
    return img


def k66(c):
    img = white_full("k66", (0.5, 0.6)) if False else ImageOps.fit(R("k66"), (W, H), Image.LANCZOS, centering=(0.5, 0.6)).convert("RGBA")
    pill(img, S(c, "kicker").upper(), inter(30, "Medium"), W / 2, 360, PILL_DARK, WHITE, padx=30, pady=12)
    f, ls = fit(S(c, "big"), lambda s: tinos(s, -0.05), 980, 1, 230, 120)
    y = draw_lines(img, ls, f, 50, 400, INK, "center", 1.0, None, 980)
    f2, ls2 = fit(S(c, "sub"), lambda s: inter(s, "Medium"), 900, 2, 40, 28)
    draw_lines(img, ls2, f2, 90, y + 4, INK, "center", 1.2, None, 900)
    pill(img, S(c, "pill"), inter(36, "SemiBold"), W / 2, 1550, "cta", WHITE, padx=56, pady=20)
    return img


def k67(c):
    img = band("k67")
    y = hand(img, S(c, "line_1"), 70, 340, 900, 76, 50, 1, INK)
    y = hand(img, S(c, "line_2"), 70, y, 900, 76, 50, 1, INK)
    f, ls = fit(S(c, "sub"), lambda s: inter(s, "Regular"), 620, 3, 36, 26)
    draw_lines(img, ls, f, 72, y + 18, BODY, "left", 1.25, None, 620)
    return img


BUILDERS = {k[1:]: v for k, v in globals().items() if k.startswith("k") and k[1:].isdigit()}

if __name__ == "__main__":
    sys.path.insert(0, str(HERE.parents[1] / "gallery"))
    for i in sys.argv[1:] or sorted(BUILDERS):
        lib.TEXT_BOXES.clear()
        c = COPY.get(i, {"funnel": "TOF", "angle": "klik"})
        slug = "klik-" + "".join(ch if ch.isalnum() else "-" for ch in c["angle"].lower()).strip("-")[:24].strip("-")
        try:
            print(save(BUILDERS[i](i), f"RET_A49_{i}_{c['funnel'].lower()}_{slug}"))
        except Exception as e:  # noqa: BLE001
            print("FAIL", i, repr(e))
