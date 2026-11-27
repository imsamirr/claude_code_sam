"""Pain-point batch (ids 68-77): under-covered angles, one specific pain each.
    python3 pain.py [ids...]  -> output/RET_A49_<id>_<funnel>_<slug>_{9x16,4x5}.png
Copy: copy_pain.json (StefanBrain). Scenes: renders/p68..p77 (pain_render.py); product photos: renders/p34_*.
"""
import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageOps

from lib import *  # noqa: F401,F403
import lib
from layouts import S, COPY, rounded
from scenes import tiktok_caption
import b2
from b2 import head, sub, photo, checklist, badge, scrim_top, scrim_bottom, card, SH, WARM

HERE = Path(__file__).resolve().parent
COPY.update({c["id"]: c for c in json.load(open(HERE / "copy_pain.json"))["concepts"]})
b2.PICK.update({"p68": "p68_t2", "p70": "p70_t2", "p77": "p77_t2"})  # takes chosen after QA
PICK = b2.PICK
IOS_BG = (242, 242, 247)
IOS_BLUE = (10, 122, 255)
IOS_RED = (255, 59, 48)


def full(k, cen=(0.5, 0.5)):
    return b2.full(k, cen)


def ios_alert(img, title, body, cy, w=640, buttons=("Close",), battery=False):
    """Mock iOS system alert (frosted rounded card, centred title/body, button row)."""
    ft, fb, fbtn = inter(36, "SemiBold"), inter(29, "Regular"), inter(34, "Regular")
    tl = wrap(title, ft, w - 80)
    bl = wrap(body, fb, w - 80)
    asc, desc = fb.getmetrics()
    h_body = len(bl) * (asc + desc) * 1.2
    h = 46 + (70 if battery else 0) + len(tl) * 46 + 12 + h_body + 34 + 96
    x0, y0 = (W - w) / 2, cy - h / 2
    sh = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle((x0, y0 + 14, x0 + w, y0 + h + 14), 36, fill=(0, 0, 0, 110))
    img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(26)))
    # frosted: blur what's behind the card
    box = tuple(int(v) for v in (x0, y0, x0 + w, y0 + h))
    behind = img.crop(box).filter(ImageFilter.GaussianBlur(30))
    m = Image.new("L", behind.size, 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0, behind.width - 1, behind.height - 1), 36, fill=255)
    img.paste(behind, box[:2], m)
    ov = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(ov).rounded_rectangle(box, 36, fill=IOS_BG + (228,))
    img.alpha_composite(ov)
    d = ImageDraw.Draw(img)
    y = y0 + 46
    if battery:  # red near-empty battery glyph
        bx, by = W / 2 - 50, y
        d.rounded_rectangle((bx, by, bx + 92, by + 44), 10, outline=(30, 30, 32), width=4)
        d.rounded_rectangle((bx + 96, by + 14, bx + 104, by + 30), 3, fill=(30, 30, 32))
        d.rounded_rectangle((bx + 8, by + 8, bx + 22, by + 36), 4, fill=IOS_RED)
        y += 70
    y = draw_lines(img, tl, ft, x0 + 40, y, (0, 0, 0), "center", 1.15, None, w - 80) + 12
    y = draw_lines(img, bl, fb, x0 + 40, y, (0, 0, 0), "center", 1.2, None, w - 80) + 34
    d = ImageDraw.Draw(img)
    d.line([(x0, y), (x0 + w, y)], fill=(198, 198, 204), width=2)
    n = len(buttons)
    for i, b in enumerate(buttons):
        cx = x0 + w * (i + 0.5) / n
        draw_text(d, (cx - measure(fbtn, b) / 2, y + 26), b, fbtn, IOS_BLUE)
        if i:
            d.line([(x0 + w * i / n, y), (x0 + w * i / n, y0 + h)], fill=(198, 198, 204), width=2)
    lib.TEXT_BOXES.append(box)
    return y0 + h


def ios_banner(img, title, body, y0, w=960):
    """Mock iOS notification banner: frosted card, battery glyph, bold title + body, left aligned."""
    ft, fb = inter(36, "SemiBold"), inter(31, "Regular")
    bl = wrap(body, fb, w - 190)
    asc, desc = fb.getmetrics()
    h = 40 + 46 + len(bl) * (asc + desc) * 1.2 + 34
    x0 = (W - w) / 2
    box = tuple(int(v) for v in (x0, y0, x0 + w, y0 + h))
    sh = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle((box[0], box[1] + 12, box[2], box[3] + 12), 40, fill=(0, 0, 0, 100))
    img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(22)))
    behind = img.crop(box).filter(ImageFilter.GaussianBlur(30))
    m = Image.new("L", behind.size, 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0, behind.width - 1, behind.height - 1), 40, fill=255)
    img.paste(behind, box[:2], m)
    ov = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(ov).rounded_rectangle(box, 40, fill=IOS_BG + (232,))
    img.alpha_composite(ov)
    d = ImageDraw.Draw(img)
    bx, by = x0 + 36, y0 + h / 2 - 24
    d.rounded_rectangle((bx, by, bx + 92, by + 48), 11, outline=(30, 30, 32), width=4)
    d.rounded_rectangle((bx + 96, by + 15, bx + 104, by + 33), 3, fill=(30, 30, 32))
    d.rounded_rectangle((bx + 9, by + 9, bx + 24, by + 39), 4, fill=IOS_RED)
    draw_text(d, (x0 + 150, y0 + 36), title, ft, (0, 0, 0))
    draw_lines(img, bl, fb, x0 + 150, y0 + 36 + 52, (40, 40, 44), "left", 1.2, None, w - 190)
    lib.TEXT_BOXES.append(box)
    return y0 + h


# ---------------------------------------------------------------- 68 theme park: low-battery alert
def p68(c):
    img = full("p68", (0.5, 0.55))
    scrim_top(img, 720, 190)
    y = head(img, S(c, "headline"), 340, WARM, 92, 60, 2, shadow=SH)
    ios_banner(img, S(c, "alert_title"), S(c, "alert_body"), y + 20)
    scrim_bottom(img, 1330, 190)
    sub(img, S(c, "bottom_line"), 1500, WHITE, 42, 30, 2, shadow=SH, weight="SemiBold")
    return img


# ---------------------------------------------------------------- 69 wedding: 2x2 "nobody tells you" cards
def p69(c):
    img = canvas(WHITE)
    y = head(img, S(c, "headline"), 320, INK, 84, 56, 2)
    top = y + 28
    for i in range(4):
        x0 = 60 + (i % 2) * 490
        y0 = top + (i // 2) * 380
        card(img, (x0, y0, x0 + 470, y0 + 360), (246, 242, 235))
        draw_lines(img, [str(i + 1)], tinos(60), x0 + 30, y0 + 18, KICKER, "left", 1, None, 100)
        f, ls = fit(S(c, f"card_{i + 1}"), lambda q: inter(q, "Medium"), 410, 5, 36, 26)
        draw_lines(img, ls, f, x0 + 30, y0 + 100, INK, "left", 1.2, None, 410)
    yb = top + 2 * 380
    prod(img, "p34_chalk", 360, 250, min(yb + 150, 1480))
    sub(img, S(c, "product_line"), min(yb + 90, 1420), INK, 42, 30, 3, x=460, w=560, align="left", weight="SemiBold")
    return img


# ---------------------------------------------------------------- 70 grandparents: future question over candid
def p70(c):
    img = canvas(WHITE)
    y = head(img, S(c, "headline"), 320, INK, 80, 54, 4)
    y = sub(img, S(c, "sub"), y + 14, BODY, 36, 28, 2)
    top = int(y + 34)
    im = b2.R("p70")
    im = im.crop((0, int(im.height * 0.30), im.width, im.height))  # below the plain wall band Kie left at the top
    im = ImageOps.fit(im, (W, H - top), Image.LANCZOS, centering=(0.5, 0.35))
    img.alpha_composite(im.convert("RGBA"), (0, top))
    return img


# ---------------------------------------------------------------- 71 social detox: struck-through chain
def p71(c):
    img = canvas(WHITE)
    y = head(img, S(c, "headline"), 320, INK, 84, 56, 2, x=80, w=920, align="left")
    y += 40
    d = ImageDraw.Draw(img)
    f = inter(46, "Medium")
    for i in range(1, 6):
        t = S(c, f"strike_{i}")
        draw_text(d, (80, y), f"{i}.", f, (178, 190, 199))
        draw_text(d, (150, y), t, f, NAVY50)
        lw = measure(f, t)
        d.line([(142, y + 30), (150 + lw + 10, y + 26)], fill=RED, width=5)
        lib.TEXT_BOXES.append((80, y, 160 + lw, y + 60))
        y += 84
    y += 20
    s = 64
    d.ellipse((80, y + 8, 80 + s, y + 8 + s), fill=(29, 111, 95))
    tick(d, 80 + s * .22, y + 8 + s * .25, s * .56, WHITE, True, 7)
    yy = draw_lines(img, wrap(S(c, "payoff"), tinos(76, -0.03), 820), tinos(76, -0.03), 170, y, INK, "left", 1.05, None, 820)
    prod(img, "p34_sol", 420, W - 300, max(yy + 230, 1400))
    sub(img, S(c, "product_line"), max(yy + 120, 1290), BODY, 34, 26, 4, x=80, w=420, align="left")
    return img


# ---------------------------------------------------------------- 72 solo travel: same trip, different target
def p72(c):
    img = canvas(WHITE)
    y = head(img, S(c, "headline"), 320, INK, 92, 60, 2)
    top = int(y + 30)
    ph = 760
    photo(img, "p72a", (40, top, 530, top + ph), (0.5, 0.35), 22)
    photo(img, "p72b", (550, top, 1040, top + ph), (0.5, 0.4), 22)
    pill(img, S(c, "left_label"), inter(30, "Bold"), 285, top + ph - 60, (255, 255, 255), RED, padx=22, pady=10)
    pill(img, S(c, "right_label"), inter(30, "Bold"), 795, top + ph - 60, INK, WHITE, padx=22, pady=10)
    sub(img, S(c, "sub"), top + ph + 40, BODY, 38, 28, 3)
    return img


# ---------------------------------------------------------------- 73 sensory: five things it never does
def p73(c):
    img = canvas(WHITE)
    y = head(img, S(c, "headline"), 320, INK, 86, 58, 2, x=70, w=940, align="left")
    y += 40
    for i in range(1, 6):
        t = S(c, f"bubble_{i}")
        f, ls = fit(t, lambda q: inter(q, "Medium"), 820, 2, 44, 30)
        asc, desc = f.getmetrics()
        bh = len(ls) * (asc + desc) * 1.15 + 44
        tw = max(measure(f, ln) for ln in ls)
        left = i % 2 == 1
        x0 = 70 if left else W - 70 - tw - 64
        box = (x0, y, x0 + tw + 64, y + bh)
        ImageDraw.Draw(img).rounded_rectangle(box, 40, fill=(236, 240, 244) if left else INK)
        draw_lines(img, ls, f, x0 + 32, y + 20, INK if left else WHITE, "left", 1.15, None, tw + 4)
        y += bh + 28
    yb = max(y + 30, 1250)
    prod(img, "p34_dune", 380, W - 250, min(yb + 170, 1470))
    sub(img, S(c, "product_line"), min(yb + 80, 1390), BODY, 36, 26, 4, x=70, w=520, align="left")
    return img


# ---------------------------------------------------------------- 74 wireless: stacked permission dialogs
def p74(c):
    img = canvas(WHITE)
    y = head(img, S(c, "headline"), 320, INK, 88, 58, 2)
    y += 30
    btns = [("Not Now", "Allow"), ("Cancel", "Pair"), ("Later", "Update"), ("Cancel", "Sign In")]
    fb, ft = inter(30, "Regular"), inter(34, "SemiBold")
    for i in range(4):
        x0 = 150 + i * 18
        w = 780 - i * 36
        box = (x0, y, x0 + w, y + 138)
        sh = Image.new("RGBA", img.size, (0, 0, 0, 0))
        ImageDraw.Draw(sh).rounded_rectangle((box[0], box[1] + 8, box[2], box[3] + 8), 30, fill=(0, 0, 0, 45))
        img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(14)))
        d = ImageDraw.Draw(img)
        d.rounded_rectangle(box, 30, fill=IOS_BG)
        t = S(c, f"dialog_{i + 1}")
        f, ls = fit(t, lambda q: inter(q, "SemiBold"), w - 60, 1, 34, 24)
        draw_lines(img, ls, f, x0 + 30, y + 18, (0, 0, 0), "center", 1, None, w - 60)
        d = ImageDraw.Draw(img)
        d.line([(x0, y + 78), (x0 + w, y + 78)], fill=(205, 205, 210), width=2)
        d.line([(x0 + w / 2, y + 78), (x0 + w / 2, y + 138)], fill=(205, 205, 210), width=2)
        for j, b in enumerate(btns[i]):
            cx = x0 + w * (j * 2 + 1) / 4
            draw_text(d, (cx - measure(fb, b) / 2, y + 90), b, fb, IOS_BLUE)
        # red strike across the whole dialog
        d.line([(x0 - 20, y + 110), (x0 + w + 20, y + 34)], fill=RED + (255,), width=7)
        lib.TEXT_BOXES.append(box)
        y += 156
    y = head(img, S(c, "payoff"), y + 20, INK, 66, 48, 2)
    prod(img, "p34_obsidian", 300, 240, min(y + 150, 1490))
    sub(img, S(c, "product_line"), min(y + 70, 1430), BODY, 34, 26, 4, x=460, w=560, align="left")
    return img


# ---------------------------------------------------------------- 75 parents: Christmas-morning POV sticker
def p75(c):
    img = full("p75", (0.5, 0.5))
    tiktok_caption(img, S(c, "caption"), 340, 44, 960)
    scrim_bottom(img, 1360, 180)
    sub(img, S(c, "sub"), 1520, WHITE, 42, 30, 2, shadow=SH, weight="SemiBold")
    return img


# ---------------------------------------------------------------- 76 honeymoon: headline + two caption bubbles
def p76(c):
    img = full("p76", (0.5, 0.5))
    scrim_top(img, 700, 170)
    head(img, S(c, "headline"), 340, WARM, 88, 58, 2, shadow=SH)
    tiktok_caption(img, S(c, "bubble_1"), 640, 40, 900)
    tiktok_caption(img, S(c, "bubble_2"), 1460, 40, 900)
    return img


# ---------------------------------------------------------------- 77 one-click photographer: pills + sale sticker
def p77(c):
    img = full("p77", (0.5, 0.5))
    scrim_top(img, 820, 190)
    y = head(img, S(c, "headline"), 340, WARM, 92, 60, 2, shadow=SH)
    fl = inter(32, "SemiBold")
    for i in range(4):
        cx = 300 + (i % 2) * 480
        cy = y + 60 + (i // 2) * 84
        pill(img, S(c, f"pill_{i + 1}"), fl, cx, cy, (255, 255, 255), INK, padx=24, pady=12)
    d = ImageDraw.Draw(img)
    cx, cy, r = 870, 1390, 130
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=SAND)
    d.ellipse((cx - r + 10, cy - r + 10, cx + r - 10, cy + r - 10), outline=INK, width=3)
    fs_, ls_ = fit(S(c, "sticker_top"), lambda q: tinos(q, -0.03), 2 * r - 70, 1, 60, 34)
    draw_lines(img, ls_, fs_, cx - r, cy - 62, INK, "center", 1, None, 2 * r)
    draw_lines(img, [S(c, "sticker_bottom")], inter(30, "Bold"), cx - r, cy + 14, INK, "center", 1, None, 2 * r)
    lib.TEXT_BOXES.append((cx - r, cy - r, cx + r, cy + r))
    pill(img, S(c, "cta"), inter(38, "SemiBold"), W / 2, 1560, "cta", WHITE, padx=60, pady=20)
    return img


from layouts import tick  # noqa: E402

SLUG = {"68": "theme-park-low-battery", "69": "wedding-nobody-tells-you", "70": "grandparents-trapped-photos",
        "71": "detox-struck-list", "72": "solo-travel-pickpocket-split", "73": "sensory-never-list",
        "74": "wireless-popups", "75": "kid-wants-phone-pov", "76": "honeymoon-through-a-screen",
        "77": "one-click-no-presets-sale"}
BUILDERS = {k: v for k, v in globals().items() if k.startswith("p") and k[1:].isdigit()}

if __name__ == "__main__":
    sys.path.insert(0, str(HERE.parents[1] / "gallery"))
    ids = sys.argv[1:] or sorted(k[1:] for k in BUILDERS)
    for i in ids:
        lib.TEXT_BOXES.clear()
        c = COPY[i]
        fun = c["funnel"].lower()
        try:
            print(save(BUILDERS["p" + i](i), f"RET_A49_{i}_{fun}_{SLUG[i]}"))
        except Exception as e:  # noqa: BLE001
            import traceback
            traceback.print_exc()
            print("FAIL", i, repr(e))
