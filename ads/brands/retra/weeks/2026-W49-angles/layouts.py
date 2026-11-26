"""Product-only layouts for the W49 angles batch (no scene renders needed).
    python3 layouts.py [ids...]      -> output/RET_A49_<id>_<funnel>_<slug>_{9x16,4x5}.png
Copy comes from copy.json (StefanBrain); every on-image word is a copy slot.
"""
import json
import math
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageOps

from lib import *  # noqa: F401,F403
import lib

HERE = Path(__file__).resolve().parent
GAL = HERE.parents[1] / "gallery"
COPY = {c["id"]: c for c in json.load(open(HERE / "copy.json"))["concepts"]} if (HERE / "copy.json").exists() else {}
MUTED = (110, 122, 132)


def S(cid, name, default=""):
    c = COPY.get(cid, {})
    v = {s["name"]: s["text"] for s in c.get("slots", [])}.get(name, default)
    return typeset(v)


def text_block(img, text, mk, x, y, w, max_lines, start, floor, color, align="left", lead=1.1, shadow=None):
    f, lines = fit(text, mk, w, max_lines, start, floor)
    return draw_lines(img, lines, f, x, y, color, align, lead, shadow, w)


def raw(path):
    p = Path(path)
    return Image.open(p if p.exists() else p.with_suffix(".jpg")).convert("RGB")


def disposable(height):
    """Generic, unbranded disposable camera + film canister (green-screen cut-out)."""
    im = Image.open(HERE / "renders/disposable_cut.png").convert("RGBA")
    return im.resize((int(im.width * height / im.height), height), Image.LANCZOS)


def rounded(im, r):
    m = Image.new("L", im.size, 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0, im.width - 1, im.height - 1), r, fill=255)
    out = im.convert("RGBA")
    out.putalpha(m)
    return out


def paper(color=CREAM, seed=3, amt=2.2):
    rng = np.random.default_rng(seed)
    a = np.array(color, float)[None, None, :] + rng.normal(0, amt, (H, W, 1))
    return Image.fromarray(np.clip(a, 0, 255).astype("uint8")).convert("RGBA")


def tick(d, x, y, s, color, ok=True, width=6):
    if ok:
        d.line([(x, y + s * .55), (x + s * .38, y + s * .9), (x + s, y + s * .1)], fill=color, width=width, joint="curve")
    else:
        d.line([(x + s * .1, y + s * .1), (x + s * .9, y + s * .9)], fill=color, width=width)
        d.line([(x + s * .9, y + s * .1), (x + s * .1, y + s * .9)], fill=color, width=width)


# ---------------------------------------------------------------- 02 nostalgic dreamer: film-print collage
SAMPLES = {  # raw (unfiltered) gallery renders, ILLUSTRATIVE
    "ferry": GAL / "renders/sample_ferry_t1.png", "harbour": GAL / "renders/scene_split_t1.png",
    "bike": GAL / "renders/sample_bike_t2.png", "party": GAL / "renders/sample_party_t2.png",
    "portrait": GAL / "renders/portrait_t1.png", "sand": GAL / "renders/sample_sand_t1.png",
}


def film_print(key, look, size, crop=None):
    from compose_gallery import retra_filter
    im = raw(SAMPLES[key])
    if key == "party":
        im = im.crop((66, 66, im.width - 66, im.height - 66))
    im = ImageOps.fit(im, (size[0], size[1]), Image.LANCZOS)
    im = retra_filter(im, look)
    b = int(size[0] * 0.05)
    card = Image.new("RGBA", (size[0] + 2 * b, size[1] + int(b * 2.6)), (250, 247, 240, 255))
    card.paste(im, (b, b))
    return card


def a02(cid):
    img = paper((44, 33, 26), seed=2, amt=3)
    # warm smoky glow
    glow = Image.new("L", (W, H), 0)
    ImageDraw.Draw(glow).ellipse((-200, 500, 1280, 1700), fill=120)
    img.alpha_composite(Image.merge("RGBA", (*Image.new("RGB", (W, H), (150, 96, 60)).split(),
                                             glow.filter(ImageFilter.GaussianBlur(160)))))
    prints = [("ferry", "Vintage", (360, 450), -8, 230, 720), ("harbour", "Film", (380, 380), 6, 560, 650),
              ("portrait", "Natural", (330, 410), -3, 860, 780), ("bike", "Black & White", (340, 340), 9, 330, 1060),
              ("party", "Film", (360, 360), -6, 760, 1080)]
    for key, look, size, ang, cx, cy in prints:
        p = film_print(key, look, size).rotate(ang, Image.BICUBIC, expand=True)
        place(img, p, cx, cy, shadow=0.55, blur=18, drop=(8, 14))
    # title band
    d = ImageDraw.Draw(img)
    band_y = 360
    d.rectangle((0, band_y, W, band_y + 96), fill=(243, 234, 214))
    bt = S(cid, "band_title", "FILM AESTHETIC").upper()
    f = shantell(44, track=0.09)
    draw_lines(img, [bt], f, 0, band_y + 18, (44, 33, 26), "center", 1.0, None, W)
    y = text_block(img, S(cid, "headline", "Headline here"), tinos, 70, 1290, 650, 3, 62, 46, (247, 240, 226), "left")
    text_block(img, S(cid, "sub", "Sub line here"), lambda s: inter(s, "Regular"), 72, y + 8, 620, 2, 30, 24,
               (222, 205, 184), "left", 1.25)
    place(img, cam("dune", 320, -4), 880, 1440, shadow=0.6, blur=20)
    return grain(img, 3)


# ---------------------------------------------------------------- 04 grandparents: minimal hero + handwriting
def a04(cid):
    img = canvas(WHITE)
    lines = [S(cid, f"line_{i}", f"Handwritten line {i}") for i in (1, 2, 3)]
    y = 400
    for ln in lines:
        f, ls = fit(ln, lambda s: shantell(s), 900, 1, 78, 50)
        y = draw_lines(img, ls, f, 90, y, INK, "left", 1.12, None, 900) + 6
    place(img, cam("blossom", 760, -3), W / 2 + 40, 1090, shadow=0.42, blur=30, drop=(0, 34))
    text_block(img, S(cid, "footer", "Footer line"), lambda s: inter(s, "Regular"), 90, 1460, 900, 1, 36, 26, BODY,
               "center")
    return img


# ---------------------------------------------------------------- 07 social detox: colour-block question
def a07(cid):
    img = canvas(INK)
    y = text_block(img, S(cid, "headline", "A big question here?"), lambda s: tinos(s, -0.04), 70, 370, 940, 3, 112,
                   72, (247, 240, 226), "center", 1.1)
    text_block(img, S(cid, "sub", "Sub line here"), lambda s: inter(s, "Regular"), 90, y + 18, 900, 2, 38, 28,
               (190, 205, 216), "center", 1.25)
    place(img, cam("sol", 840, -4), W / 2, 1270, shadow=0.7, blur=34, drop=(0, 40))
    return img


# ---------------------------------------------------------------- 08 wireless detox: annotated product diagram
def a08(cid):
    img = canvas(WHITE)
    hl = S(cid, "headline", "Headline with keywords")
    kws = [k.strip().strip('"').lower() for k in S(cid, "keywords_to_colour", "").replace(";", ",").split(",") if k.strip()]
    f, lines = fit(hl, tinos, 960, 3, 92, 60)
    asc, desc = f.getmetrics()
    lh = int((asc + desc) * 1.04)
    y = 360
    d = ImageDraw.Draw(img)
    for line in lines:  # colour keyword runs
        lw = measure(f, line)
        x = (W - lw) / 2
        low = line.lower()
        spans = []
        for k in kws:
            i = low.find(k)
            if i >= 0:
                spans.append((i, i + len(k)))
        cur = 0
        segs = []
        for a_, b_ in sorted(spans):
            if a_ > cur:
                segs.append((line[cur:a_], NAVY50))
            segs.append((line[a_:b_], INK))
            cur = b_
        segs.append((line[cur:], NAVY50))
        for t, col in segs:
            if not t:
                continue
            draw_text(d, (x, y), t, f, col)
            x += measure(f, t) + f.track
        lib.TEXT_BOXES.append(((W - lw) / 2, y, (W + lw) / 2, y + lh))
        y += lh
    obj = front("obsidian", 820)
    box = place(img, obj, W / 2, 1120, shadow=0.4, blur=30, drop=(0, 32))
    bx0, by0, bx1, by1 = box
    bw, bh = bx1 - bx0, by1 - by0
    pts = [(0.17, 0.16), (0.80, 0.14), (0.84, 0.58), (0.33, 0.62)]  # wordmark band, viewfinder/flash, button, lens
    labels = [(140, by0 - 70, "l"), (W - 140, by0 - 70, "r"), (W - 120, by1 + 70, "r"), (120, by1 + 70, "l")]
    fl = inter(36, "SemiBold")
    d = ImageDraw.Draw(img)
    for i, ((px, py), (lx, ly, side)) in enumerate(zip(pts, labels), 1):
        t = S(cid, f"callout_{i}", f"Callout {i}")
        ax, ay = bx0 + px * bw, by0 + py * bh
        tw = measure(fl, t)
        tx = lx if side == "l" else lx - tw
        anchor = (lx if side == "l" else lx, ly + 22)
        d.line([(ax, ay), (anchor[0] + (tw / 2 if side == "l" else -tw / 2), ly + (44 if ly < ay else 0))],
               fill=INK, width=3)
        d.ellipse((ax - 9, ay - 9, ax + 9, ay + 9), fill=WHITE, outline=INK, width=3)
        pill(img, t, fl, tx + tw / 2, ly + 22, (238, 241, 244), INK, padx=22, pady=12)
        d = ImageDraw.Draw(img)
    return img


# ---------------------------------------------------------------- 09 cost vs disposables: comparison table
def a09(cid):
    img = canvas(WHITE)
    y = text_block(img, S(cid, "headline", "Headline here"), tinos, 70, 340, 940, 2, 84, 58, INK, "center")
    top = y + 30
    colx = [70, 470, 780]  # label col, left col centre band start, right col
    # header images
    place(img, disposable(280), 530, top + 150, shadow=0.35, blur=16, drop=(0, 14))
    place(img, cam("chalk", 300, -3), 850, top + 150, shadow=0.35, blur=18, drop=(0, 16))
    fh = inter(34, "Bold")
    hy = top + 310
    for txt, cx in [(S(cid, "col_left", "Disposable"), 530), (S(cid, "col_right", "Retra"), 850)]:
        f_, l_ = fit(txt, lambda s: inter(s, "Bold"), 290, 2, 34, 24)
        draw_lines(img, l_, f_, cx - 145, hy, INK, "center", 1.08, None, 290)
    d = ImageDraw.Draw(img)
    ry = hy + 100
    rows = []
    for i in range(1, 6):
        r = S(cid, f"row_{i}", "")
        if r:
            parts = [p.strip() for p in r.split("|")]
            rows.append(parts + [""] * (3 - len(parts)))
    rh = 128
    # highlight Retra column
    d.rounded_rectangle((700, hy - 20, 1000, ry + rh * len(rows) + 10), 26, fill=(239, 243, 246))
    fl = inter(32, "SemiBold")
    fv = inter(32, "Medium")
    for i, (lab, lv, rv) in enumerate(rows):
        yy = ry + i * rh
        if i:
            d.line([(70, yy - 8), (1010, yy - 8)], fill=(222, 226, 230), width=2)
        f1, l1 = fit(lab, lambda s: inter(s, "SemiBold"), 300, 2, 32, 24)
        draw_lines(img, l1, f1, 70, yy + 12, INK, "left", 1.15, None, 300)
        f2, l2 = fit(lv, lambda s: inter(s, "Regular"), 250, 2, 32, 24)
        draw_lines(img, l2, f2, 405, yy + 12, (130, 120, 110), "center", 1.15, None, 250)
        f3, l3 = fit(rv, lambda s: inter(s, "SemiBold"), 260, 2, 32, 24)
        draw_lines(img, l3, f3, 720, yy + 12, INK, "center", 1.15, None, 260)
        d = ImageDraw.Draw(img)
    return img


# ---------------------------------------------------------------- 10 one click, four filters: filter grid
def a10(cid):
    from compose_gallery import retra_filter
    img = canvas(WHITE)
    y = text_block(img, S(cid, "headline", "Headline here"), tinos, 70, 330, 940, 2, 84, 58, INK, "center")
    T, gap = 400, 20
    base = ImageOps.fit(raw(SAMPLES["harbour"]), (T, T), Image.LANCZOS, centering=(0.5, 0.45))
    looks = [S(cid, f"filter_{i}", d) for i, d in enumerate(["Vintage", "Black & White", "Natural", "Film"], 1)]
    keys = ["Vintage", "Black & White", "Natural", "Film"]
    gx, gy = (W - 2 * T - gap) / 2, y + 30
    fl = inter(28, "SemiBold")
    for i, (lk, key) in enumerate(zip(looks, keys)):
        tile = rounded(retra_filter(base, key), 18)
        x = gx + (i % 2) * (T + gap)
        yy = gy + (i // 2) * (T + gap)
        img.alpha_composite(tile, (int(x), int(yy)))
        pill(img, lk, fl, x + 18 + measure(fl, lk) / 2 + 20, yy + T - 40, (250, 247, 240), INK, padx=20, pady=10)
    bottom = gy + 2 * T + gap
    text_block(img, S(cid, "sub", "Sub line here"), lambda s: inter(s, "Regular"), int(gx), bottom + 34, 520, 3, 34, 24,
               BODY, "left", 1.25)
    place(img, cam("sol", 300, -4), W - gx - 150, bottom + 125, shadow=0.45, blur=20, drop=(0, 16))
    return img


# ---------------------------------------------------------------- 11 gifting: 2x3 colour chooser
TILE_BG = {"chalk": (238, 233, 222), "obsidian": (216, 214, 212), "sol": (246, 228, 182), "dune": (236, 212, 192),
           "pine": (219, 224, 204), "blossom": (245, 213, 222)}


def a11(cid):
    img = canvas(WHITE)
    y = text_block(img, S(cid, "headline", "Headline here"), tinos, 70, 320, 940, 2, 80, 56, INK, "center")
    tw_, th_, gap = 300, 360, 20
    x0 = (W - 3 * tw_ - 2 * gap) / 2
    y0 = y + 30
    fl = inter(28, "SemiBold")
    for i, c in enumerate(COLOURS):
        x = x0 + (i % 3) * (tw_ + gap)
        yy = y0 + (i // 3) * (th_ + gap)
        t = Image.new("RGBA", (tw_, th_), TILE_BG[c] + (255,))
        t = rounded(t, 24)
        img.alpha_composite(t, (int(x), int(yy)))
        place(img, cam(c, 260, -3), x + tw_ / 2, yy + 150, shadow=0.35, blur=12, drop=(0, 10))
        lab = S(cid, f"tile_{c}", c.title())
        f, ls = fit(lab, lambda s: inter(s, "SemiBold"), tw_ - 30, 2, 28, 20)
        draw_lines(img, ls, f, x + 15, yy + 262, INK, "center", 1.12, None, tw_ - 30)
    bottom = y0 + 2 * th_ + gap
    pill(img, S(cid, "pill", "Pill text"), inter(34, "SemiBold"), W / 2, bottom + 70, "cta", WHITE, padx=50, pady=18)
    return img


# ---------------------------------------------------------------- 14 offer: colour lineup lit on black
def a14(cid):
    img = canvas((8, 8, 10))
    spot = Image.new("L", (W, H), 0)
    ImageDraw.Draw(spot).ellipse((-150, 700, 1230, 1650), fill=255)
    spot = spot.filter(ImageFilter.GaussianBlur(170)).point(lambda v: int(v * 0.42))
    img.alpha_composite(Image.merge("RGBA", (*Image.new("RGB", (W, H), (70, 62, 54)).split(), spot)))
    y = text_block(img, S(cid, "headline", "Pay for 2. Get 3."), lambda s: tinos(s, -0.04), 70, 360, 940, 2, 118, 80,
                   (247, 240, 226), "center", 1.1)
    text_block(img, S(cid, "sub", "Sub line here"), lambda s: inter(s, "Regular"), 90, y + 14, 900, 2, 38, 28,
               (200, 192, 180), "center", 1.25)
    rows = [(["chalk", "sol", "blossom"], 980), (["obsidian", "dune", "pine"], 1300)]
    for r_, (cols, cy) in enumerate(rows):
        for j, c in enumerate(cols):
            cx = 200 + j * 340
            o = cam(c, 330)
            if r_ == 0:
                place(img, o, cx, cy, shadow=0.8, blur=14, drop=(0, 18))
                continue
            # floor reflection
            ref = ImageOps.flip(o)
            fade = np.linspace(0.32, 0, ref.height)[:, None] * (np.asarray(ref.getchannel("A")) / 255)
            ref.putalpha(Image.fromarray((fade * 255).astype("uint8")))
            img.alpha_composite(ref, (int(cx - o.width / 2), int(cy + o.height / 2 - 6)))
            place(img, o, cx, cy, shadow=0.0)
    return img


# ---------------------------------------------------------------- 15 low stock: "we're sorry" letter
def a15(cid):
    img = canvas(WHITE)
    d = ImageDraw.Draw(img)
    y = text_block(img, S(cid, "title", "We're sorry."), lambda s: tinos(s, -0.04), 80, 360, 920, 2, 104, 70, INK)
    d.line([(80, y + 14), (240, y + 14)], fill=SAND, width=5)
    y += 50
    body = S(cid, "body", "Body copy here.")
    paras = [p.strip() for p in body.split("\n") if p.strip()]
    fb = lambda s: tinos(s, -0.02)
    size = 48
    while size > 28:  # one size for every paragraph so the block fits above the product
        f = fb(size)
        need = sum(len(wrap(p, f, 920)) for p in paras) * (sum(f.getmetrics()) * 1.32) + 26 * len(paras)
        if y + need < 1330:
            break
        size -= 1
    f = fb(size)
    for p in paras:
        y = draw_lines(img, wrap(p, f, 920), f, 80, y, (30, 50, 66), "left", 1.32, None, 920) + 26
    so = S(cid, "signoff", "The Retra team")
    fs = shantell(52)
    draw_lines(img, [so], fs, 80, y + 10, INK, "left", 1.0, None, 900)
    place(img, cam("blossom", 340, -6), W - 240, 1500, shadow=0.45, blur=22, drop=(0, 20))
    return img


# ---------------------------------------------------------------- 16 price card
def a16(cid):
    img = canvas((226, 172, 46))
    card = rounded(Image.new("RGBA", (940, 1240), (255, 255, 255, 255)), 40)
    place(img, card, W / 2, 960, shadow=0.35, blur=30, drop=(0, 20))
    pill(img, S(cid, "label", "EXCLUSIVE DEAL").upper(), inter(30, "Medium"), W / 2, 420, PILL_DARK, WHITE, padx=32, pady=12)
    y = text_block(img, S(cid, "headline", "Headline here"), tinos, 120, 470, 840, 2, 84, 58, INK, "center")
    po, pn = S(cid, "price_old", "$165"), S(cid, "price_new", "$99")
    fo, fn = tinos(80), tinos(170, -0.05)
    d = ImageDraw.Draw(img)
    wo, wn = measure(fo, po), measure(fn, pn)
    tot = wo + 40 + wn
    x = (W - tot) / 2
    py = y + 10
    draw_text(d, (x, py + 70), po, fo, NAVY50)
    d.line([(x - 6, py + 70 + 52), (x + wo + 6, py + 70 + 40)], fill=NAVY50, width=6)
    draw_text(d, (x + wo + 40, py), pn, fn, INK)
    lib.TEXT_BOXES.append((x, py, x + tot, py + 200))
    y = py + 230
    fl = inter(36, "SemiBold")
    for i in (1, 2, 3):
        t = S(cid, f"tick_{i}", "")
        if not t:
            continue
        d.ellipse((150, y + 2, 196, y + 48), fill=(29, 111, 95))
        tick(d, 160, y + 12, 26, WHITE, True, 5)
        draw_lines(img, [t], fl, 220, y + 2, INK, "left", 1.0, None, 720)
        d = ImageDraw.Draw(img)
        y += 72
    place(img, front("chalk", 520), W / 2, y + 150, shadow=0.35, blur=22, drop=(0, 18))
    pill(img, S(cid, "pill", "Shop now"), inter(36, "SemiBold"), W / 2, 1520, "cta", WHITE, padx=56, pady=20)
    return img


# ---------------------------------------------------------------- 17 camping: Venn diagram
def a17(cid):
    img = canvas(WHITE)
    y = text_block(img, S(cid, "headline", "Headline"), tinos, 70, 340, 940, 2, 88, 60, INK, "center")
    cy, r = y + 430, 320
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)
    d.ellipse((375 - r, cy - r, 375 + r, cy + r), fill=(2, 43, 73, 34), outline=INK + (255,), width=4)
    d.ellipse((705 - r, cy - r, 705 + r, cy + r), fill=(226, 172, 46, 70), outline=(176, 128, 20, 255), width=4)
    img.alpha_composite(lay)
    fl = inter(32, "Bold")
    draw_lines(img, [S(cid, "left_circle", "Phones")], fl, 130, cy - 150, INK, "center", 1, None, 230)
    draw_lines(img, [S(cid, "right_circle", "Disposables")], fl, 720, cy - 150, INK, "center", 1, None, 230)
    # small icons in each outer lobe
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((190, cy - 70, 270, cy + 80), 16, outline=INK, width=5)
    d.ellipse((222, cy + 54, 238, cy + 70), fill=INK)
    place(img, disposable(165), 875, cy + 5, shadow=0.3, blur=10, drop=(0, 8))
    place(img, cam("pine", 270, -3), 540, cy - 10, shadow=0.4, blur=14, drop=(0, 12))
    draw_lines(img, [S(cid, "overlap_center", "Retra")], inter(32, "Bold"), 390, cy + 110, INK, "center", 1, None, 300)
    text_block(img, S(cid, "sub", "Sub"), lambda s: inter(s, "Regular"), 90, cy + r + 40, 900, 2, 36, 26, BODY,
               "center", 1.25)
    return img


# ---------------------------------------------------------------- 18 nights out: "5 things" listicle
def a18(cid):
    from compose_gallery import retra_filter
    img = canvas(WHITE)
    y = text_block(img, S(cid, "headline", "Headline"), tinos, 70, 340, 940, 2, 80, 56, INK, "left")
    y += 26
    d = ImageDraw.Draw(img)
    for i in range(1, 6):
        t = S(cid, f"item_{i}", "")
        if not t:
            continue
        d.ellipse((70, y + 4, 116, y + 50), fill=(29, 111, 95))
        tick(d, 80, y + 14, 26, WHITE, True, 5)
        f, ls = fit(t, lambda s: inter(s, "Regular"), 820, 2, 38, 28)
        y = draw_lines(img, ls, f, 140, y + 2, INK, "left", 1.18, None, 820) + 24
        d = ImageDraw.Draw(img)
    party = raw(SAMPLES["party"]).crop((66, 66, 1982, 1982))
    pr = retra_filter(ImageOps.fit(party, (420, 420), Image.LANCZOS), "Film")
    card = Image.new("RGBA", (450, 500), (250, 247, 240, 255))
    card.paste(pr, (15, 15))
    place(img, card.rotate(-5, Image.BICUBIC, expand=True), 300, max(y + 250, 1330), shadow=0.4, blur=16, drop=(6, 12))
    place(img, cam("obsidian", 440, 4), 760, max(y + 300, 1380), shadow=0.5, blur=22, drop=(0, 20))
    return img


# ---------------------------------------------------------------- 19 road trip: Day 1 / 7 / 21 timeline
def a19(cid):
    from compose_gallery import retra_filter
    img = canvas(WHITE)
    y = text_block(img, S(cid, "headline", "Headline"), tinos, 70, 330, 940, 2, 84, 58, INK, "left")
    y += 40
    pics = [("ferry", "Natural"), ("bike", "Vintage"), ("harbour", "Film")]
    d = ImageDraw.Draw(img)
    x_line = 110
    step = 270
    d.line([(x_line, y + 30), (x_line, y + 30 + 2 * step)], fill=INK, width=4)
    for i in range(3):
        t = S(cid, f"timeline_{i + 1}", "Day")
        yy = y + i * step
        d.ellipse((x_line - 20, yy + 10, x_line + 20, yy + 50), fill=(226, 172, 46), outline=INK, width=4)
        if ":" in t:
            day, rest = t.split(":", 1)
        else:
            day, rest = t, ""
        draw_lines(img, [day.strip()], tinos(58), x_line + 50, yy - 4, INK, "left", 1, None, 480)
        f, ls = fit(rest.strip(), lambda s: inter(s, "Regular"), 470, 3, 34, 26)
        draw_lines(img, ls, f, x_line + 52, yy + 66, BODY, "left", 1.2, None, 470)
        k, look = pics[i]
        p = retra_filter(ImageOps.fit(raw(SAMPLES[k]), (300, 220), Image.LANCZOS), look)
        card = Image.new("RGBA", (320, 240), (250, 247, 240, 255))
        card.paste(p, (10, 10))
        place(img, card.rotate((-3, 4, -2)[i], Image.BICUBIC, expand=True), 840, yy + 100, shadow=0.35, blur=12,
              drop=(4, 8))
        d = ImageDraw.Draw(img)
    yb = y + 2 * step + 190
    text_block(img, S(cid, "sub", "Sub"), lambda s: inter(s, "Regular"), 90, yb + 80, 520, 2, 34, 26, INK, "left", 1.25)
    place(img, cam("dune", 300, -4), 840, yb + 175, shadow=0.45, blur=18, drop=(0, 16))
    return img


BUILDERS = {"02": a02, "04": a04, "07": a07, "08": a08, "09": a09, "10": a10, "11": a11, "14": a14, "15": a15,
            "16": a16, "17": a17, "18": a18, "19": a19}
NAMES = {"02": "tof_nostalgic-dreamer", "04": "tof_grandparents", "07": "tof_social-detox", "08": "tof_wireless-detox",
         "09": "mof_cost-vs-disposable", "10": "mof_one-click-filters", "11": "mof_gift-chooser",
         "14": "bof_pay2-get3", "15": "bof_sorry-low-stock", "16": "bof_price-card", "17": "tof_camping-venn", "18": "tof_nights-out-list",
         "19": "tof_road-trip-timeline"}

if __name__ == "__main__":
    sys.path.insert(0, str(GAL))
    ids = sys.argv[1:] or list(BUILDERS)
    for i in ids:
        lib.TEXT_BOXES.clear()
        im = BUILDERS[i](i)
        tag = "_ILLUSTRATIVE" if i in ("02", "10", "18", "19") else ""
        print(save(im, f"RET_A49_{i}_{NAMES[i]}{tag}"))
