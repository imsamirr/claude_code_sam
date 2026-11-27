"""Holiday gifting / New Year / offer statics (G*, N*, O*): StefanBrain chose angle, template and copy per concept.
    python3 holiday.py [G1 ...]  -> output/RET_A49_<id>_<funnel>_<slug>_{9x16,4x5}.png   (Sam wants 4:5)
Copy: copy_holiday.json. Scenes: renders/h_<id> (holiday_render.py). Offers from the Shopify store 2026-11-27:
$99 (compare at $200), automatic Buy 2 Get 1 Free and Buy 3 Get 2 Free.
"""
import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageOps

from lib import *  # noqa: F401,F403
import lib
from layouts import S, COPY, tick
import b2
from b2 import head, sub, scrim_top, scrim_bottom, card, SH, WARM, checklist
from pain import ios_alert
from wedding import bubble, wordmark, IM_GREY, IM_BLUE

HERE = Path(__file__).resolve().parent
CON = {c["id"]: c for c in json.load(open(HERE / "copy_holiday.json"))["concepts"]}
COPY.update(CON)
PICK = {"h_O5": "h_O5_t2", "h_N3": "h_N3_t2"}  # chosen takes
COL = {}   # concept id -> camera colour key (set in holiday_render.py, mirrored here)
PRICE_OLD, PRICE_NEW = "$200", "$99"
RED_ = (196, 30, 45)


def R(cid):
    k = f"h_{cid}"
    return Image.open(HERE / "renders" / f"{PICK.get(k, k + '_t1')}.png").convert("RGB")


CROP_TOP = {"O5": 0.335}  # Kie left a flat band at the top of these renders: crop it and fill the 4:5 band


def full(cid, cen=(0.5, 0.5)):
    im = R(cid)
    if cid in CROP_TOP:
        im = im.crop((0, int(im.height * CROP_TOP[cid]), im.width, im.height))
        band = ImageOps.fit(im, (W, 1350), Image.LANCZOS, centering=(0.5, 0.6))
        out = ImageOps.fit(band, (W, H), Image.LANCZOS).filter(ImageFilter.GaussianBlur(30)).convert("RGBA")
        out.paste(band, (0, 285))
        return out
    return ImageOps.fit(im, (W, H), Image.LANCZOS, centering=cen).convert("RGBA")


def colour(cid):
    return json.load(open(HERE / "holiday_colours.json")).get(cid, "chalk")


# ---------------------------------------------------------------- T1 hero photo
CTA_TOP = {"G1"}  # camera sits low in these photos: CTA goes under the sub instead of over the lens


def t1(c):
    img = full(c)
    scrim_top(img, 900 if c in CTA_TOP else 840, 240 if c in CTA_TOP else 215)
    y = head(img, S(c, "headline"), 340, WARM, 92, 60, 2, shadow=SH)
    y = sub(img, S(c, "sub"), y + 14, WHITE, 38, 28, 2, shadow=SH, weight="Medium")
    if c in CTA_TOP:
        pill(img, S(c, "cta"), inter(38, "SemiBold"), W / 2, y + 70, "cta", WHITE, padx=56, pady=18)
        return img
    scrim_bottom(img, 1360, 150)
    pill(img, S(c, "cta"), inter(38, "SemiBold"), W / 2, 1545, "cta", WHITE, padx=56, pady=18)
    return img


# ---------------------------------------------------------------- T2 price card on white
def t2(c):
    img = canvas(WHITE)
    pill(img, S(c, "kicker").upper(), inter(30, "Medium"), W / 2, 350, PILL_DARK, WHITE, padx=30, pady=12)
    y = head(img, S(c, "headline"), 410, INK, 92, 60, 2)
    fo, fn = tinos(96), tinos(210, -0.05)
    d = ImageDraw.Draw(img)
    wo, wn = measure(fo, PRICE_OLD), measure(fn, PRICE_NEW)
    x = (W - wo - 50 - wn) / 2
    draw_text(d, (x, y + 96), PRICE_OLD, fo, NAVY50)
    d.line([(x - 6, y + 96 + 66), (x + wo + 6, y + 96 + 50)], fill=RED_, width=7)
    draw_text(d, (x + wo + 50, y), PRICE_NEW, fn, INK)
    lib.TEXT_BOXES.append((x, y, x + wo + 50 + wn, y + 240))
    y2 = checklist(img, [S(c, f"list_{i}") for i in (1, 2, 3)], 220, y + 280, 680, True, 34, INK)
    prod(img, f"p34_{colour(c)}" if colour(c) != "aegean" else "p34_chalk", 460, W / 2, min(y2 + 150, 1420))
    pill(img, S(c, "cta"), inter(36, "SemiBold"), W / 2, 1565, "cta", WHITE, padx=56, pady=18)
    return img


# ---------------------------------------------------------------- T3 bundle math on white
def t3(c):
    img = canvas(WHITE)
    y = head(img, S(c, "headline"), 330, INK, 88, 58, 2)
    y = sub(img, S(c, "sub"), y + 10, BODY, 36, 26, 2)
    paid, free = (2, 1) if S(c, "bundle").upper().startswith("B2") else (3, 2)
    cols = ["blossom", "sol", "pine", "chalk", "dune", "obsidian"]
    n = paid + free
    cw = 300 if n == 3 else 172
    gap_sym = 70 if n == 3 else 56
    total = n * cw + (n - 1) * (20 if n == 3 else 10) + gap_sym
    x = (W - total) / 2 + cw / 2
    cy = y + 270
    fsym = tinos(110, -0.02)
    for i in range(n):
        if i == paid:  # the "+" between paid and free
            d = ImageDraw.Draw(img)
            draw_text(d, (x - cw / 2 - (4 if n == 3 else 14), cy - 70), "+", fsym if n == 3 else tinos(84), INK)
            x += gap_sym
        place(img, cam(cols[i % 6], cw, 0), x, cy, shadow=0.35, blur=14, drop=(4, 12))
        if i >= paid:
            pill(img, "FREE", inter(28 if n == 3 else 24, "Bold"), x, cy + cw * 0.45, RED_, WHITE, padx=20 if n == 3 else 14, pady=8)
        x += cw + (20 if n == 3 else 10)
    d = ImageDraw.Draw(img)
    lab = f"Pay for {paid}. Get {n}."
    draw_lines(img, [lab], tinos(76, -0.03), 80, cy + 230, INK, "center", 1, None, 920)
    draw_lines(img, [f"{PRICE_NEW} each (was {PRICE_OLD})"], inter(34, "Medium"), 80, cy + 330, BODY, "center", 1, None, 920)
    pill(img, S(c, "cta"), inter(36, "SemiBold"), W / 2, 1560, "cta", WHITE, padx=56, pady=18)
    return img


# ---------------------------------------------------------------- T4 gift tag on a gift-wrapped photo
def t4(c):
    img = full(c, (0.5, 0.55))
    scrim_top(img, 700, 170)
    head(img, S(c, "headline"), 340, WARM, 88, 58, 2, shadow=SH)
    # kraft gift tag with string, rotated
    tw_, th_ = 520, 300
    tag = Image.new("RGBA", (tw_, th_), (0, 0, 0, 0))
    td = ImageDraw.Draw(tag)
    td.polygon([(60, 0), (tw_, 0), (tw_, th_), (60, th_), (0, th_ / 2)], fill=(222, 196, 156))
    td.ellipse((34, th_ / 2 - 14, 62, th_ / 2 + 14), fill=(250, 245, 235))
    f1 = shantell(40, bold=True)
    to = S(c, "tag_to")
    to = to if to.lower().startswith("to") else "To: " + to
    f1, l1 = fit(to, lambda q: shantell(q, bold=True), tw_ - 120, 1, 40, 26)
    draw_lines(tag, l1, f1, 90, 30, (60, 40, 25), "left", 1, None, tw_ - 120)
    f2, ls = fit(S(c, "tag_message"), lambda q: shantell(q, bold=True), tw_ - 120, 4, 36, 24)
    draw_lines(tag, ls, f2, 90, 96, (60, 40, 25), "left", 1.12, None, tw_ - 120)
    tag = tag.rotate(-6, Image.BICUBIC, expand=True)
    place(img, tag, W - 360, 1180, shadow=0.45, blur=14, drop=(6, 14))
    lib.TEXT_BOXES.append((W - 600, 1020, W - 60, 1340))
    scrim_bottom(img, 1400, 160)
    sub(img, S(c, "sub"), 1500, WHITE, 38, 28, 2, shadow=SH, weight="SemiBold")
    return img


# ---------------------------------------------------------------- T5 iOS alert over a lifestyle photo
def t5(c):
    img = full(c)
    ios_alert(img, S(c, "alert_title"), S(c, "alert_body"), 1320, w=720,
              buttons=(S(c, "button_left"), S(c, "button_right")))
    scrim_bottom(img, 1400, 130)
    wordmark(img, 1530, WHITE, 64)
    return img


# ---------------------------------------------------------------- T6 notes-app list
def t6(c):
    img = canvas(WHITE)
    d = ImageDraw.Draw(img)
    # notes-app chrome
    draw_text(d, (70, 320), "‹ Notes", inter(36, "Medium"), (232, 168, 30))
    lib.TEXT_BOXES.append((70, 320, 260, 360))
    y = 400
    f = inter(76, "Bold")
    y = draw_lines(img, wrap(S(c, "title"), f, 920), f, 70, y, (20, 20, 22), "left", 1.05, None, 920) + 40
    fi = inter(46, "Medium")
    for i in range(1, 6):
        t = S(c, f"item_{i}")
        if not t:
            continue
        kind = "x" if t[:2].lower() == "x " else "v" if t[:2].lower() == "v " else ""
        txt = t[2:] if kind else t
        s_ = 54
        d = ImageDraw.Draw(img)
        if kind == "v":
            d.ellipse((70, y + 2, 70 + s_, y + 2 + s_), fill=(232, 168, 30))
            tick(d, 70 + s_ * .22, y + 2 + s_ * .25, s_ * .56, WHITE, True, 6)
        else:
            d.ellipse((70, y + 2, 70 + s_, y + 2 + s_), outline=(190, 190, 196), width=4)
        col = (150, 150, 156) if kind == "x" else (20, 20, 22)
        f_, ls = fit(txt, lambda q: inter(q, "Medium"), 820, 2, 46, 34)
        yy = draw_lines(img, ls, f_, 150, y + 2, col, "left", 1.15, None, 820)
        if kind == "x":
            for j, ln in enumerate(ls):
                lw = measure(f_, ln)
                ly = y + 2 + j * sum(f_.getmetrics()) * 1.15 + f_.size * 0.6
                ImageDraw.Draw(img).line([(146, ly), (154 + lw, ly)], fill=(150, 150, 156), width=4)
        y = yy + 34
    prod(img, f"p34_{colour(c)}" if colour(c) != "aegean" else "p34_chalk", 420, W - 260, min(y + 190, 1440))
    sub(img, S(c, "sub"), min(y + 110, 1360), BODY, 38, 26, 4, x=70, w=520, align="left")
    return img


# ---------------------------------------------------------------- T7 text bubbles over a flash photo
def t7(c):
    img = full(c, (0.5, 0.45))
    scrim_bottom(img, 1040, 160)
    y = bubble(img, S(c, "bubble_1"), 1120, False, IM_GREY, (20, 20, 22)) + 20
    y = bubble(img, S(c, "bubble_2"), y, True, IM_BLUE, WHITE) + 14
    y = bubble(img, S(c, "bubble_3"), y, True, IM_BLUE, WHITE) + 14
    wordmark(img, 1560, WHITE, 52)
    return img


# ---------------------------------------------------------------- T8 plain-text letter
def t8(c):
    img = canvas(WHITE)
    y = head(img, S(c, "title"), 350, INK, 92, 60, 2, x=80, w=920, align="left")
    ImageDraw.Draw(img).line([(80, y + 14), (240, y + 14)], fill=SAND, width=5)
    y += 50
    body = S(c, "body")
    size = 46
    while size > 28:
        f = tinos(size, -0.02)
        if y + len(wrap(body, f, 920)) * sum(f.getmetrics()) * 1.3 < 1300:
            break
        size -= 1
    f = tinos(size, -0.02)
    y = draw_lines(img, wrap(body, f, 920), f, 80, y, (30, 50, 66), "left", 1.3, None, 920)
    draw_lines(img, [S(c, "signoff")], shantell(48), 80, y + 24, INK, "left", 1.0, None, 600)
    place(img, cam(colour(c) if colour(c) != "aegean" else "chalk", 380, -6), W / 2, min(y + 300, 1470), shadow=0.4,
          blur=18, drop=(6, 18))
    return img


# ---------------------------------------------------------------- T9 calendar page
def t9(c):
    img = canvas(WHITE)
    cx, top = W / 2, 330
    cw_, ch_ = 520, 470
    x0 = cx - cw_ / 2
    sh = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle((x0, top + 12, x0 + cw_, top + ch_ + 12), 40, fill=(0, 0, 0, 60))
    img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(18)))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((x0, top, x0 + cw_, top + ch_), 40, fill=(255, 255, 255), outline=(225, 228, 232), width=2)
    d.rounded_rectangle((x0, top, x0 + cw_, top + 130), 40, fill=RED_)
    d.rectangle((x0, top + 90, x0 + cw_, top + 130), fill=RED_)
    lab = S(c, "date_label").upper().split()
    mon, day = (lab[0], lab[1]) if len(lab) > 1 else (lab[0], "")
    fm = inter(64, "Bold")
    draw_text(d, (cx - measure(fm, mon) / 2, top + 28), mon, fm, WHITE)
    fd = inter(250, "Bold")
    draw_text(d, (cx - measure(fd, day) / 2, top + 150), day, fd, (20, 20, 22))
    lib.TEXT_BOXES.append((x0, top, x0 + cw_, top + ch_))
    y = head(img, S(c, "headline"), top + ch_ + 50, INK, 84, 56, 2)
    y = sub(img, S(c, "sub"), y + 10, BODY, 36, 26, 2)
    place(img, cam(colour(c) if colour(c) != "aegean" else "chalk", 300, -6), cx, min(y + 150, 1420), shadow=0.4,
          blur=18, drop=(6, 18))
    pill(img, S(c, "cta"), inter(36, "SemiBold"), W / 2, 1565, "cta", WHITE, padx=56, pady=18)
    return img


# ---------------------------------------------------------------- T10 check / cross comparison
def t10(c):
    img = canvas(WHITE)
    y = head(img, S(c, "headline"), 330, INK, 88, 58, 2)
    top = int(y + 40)
    for i, (t, pre, ok, fill) in enumerate([("left_title", "left_", False, (243, 245, 247)),
                                            ("right_title", "right_", True, (233, 241, 246))]):
        x0 = 50 + i * 500
        card(img, (x0, top, x0 + 480, top + 900), fill)
        if ok:
            place(img, cam(colour(c) if colour(c) != "aegean" else "chalk", 330, -4), x0 + 240, top + 190, shadow=0.35,
                  blur=14, drop=(4, 12))
        else:
            b2.phone_icon(ImageDraw.Draw(img), x0 + 240, top + 190, 230, NAVY50, 8)
        draw_lines(img, [S(c, t)], tinos(52), x0 + 20, top + 350, INK, "center", 1, None, 440)
        checklist(img, [S(c, f"{pre}{j}") for j in (1, 2, 3)], x0 + 30, top + 450, 430, ok, 32, INK, gap=26)
    return img


T = {"T1": t1, "T2": t2, "T3": t3, "T4": t4, "T5": t5, "T6": t6, "T7": t7, "T8": t8, "T9": t9, "T10": t10}

if __name__ == "__main__":
    ids = sys.argv[1:] or list(CON)
    for i in ids:
        lib.TEXT_BOXES.clear()
        c = CON[i]
        slug = "".join(ch if ch.isalnum() else "-" for ch in c["angle"].lower()).strip("-")[:30].strip("-")
        try:
            print(save(T[c["template"].split()[0].upper()](i), f"RET_A49_{i}_{c['funnel'].lower()}_{slug}"))
        except Exception as e:  # noqa: BLE001
            import traceback
            traceback.print_exc()
            print("FAIL", i, repr(e))
