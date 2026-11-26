"""Shared layout helpers for the W49 angles batch (type system from W48 / landing page).
Canvas is 1080x1920 (9:16); everything that matters sits in the centred 4:5 band SAFE = (0, 285, 1080, 1635),
which is also the 4:5 crop."""
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageOps, ImageFont

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[4]
FONTS = HERE.parents[1] / "fonts"
CUT = REPO / "assets/retra/product/cutout_clean"
GAL = HERE.parents[1] / "gallery"
OUT = HERE / "output"
OUT.mkdir(exist_ok=True)
W, H = 1080, 1920
TOP, BOT = 285, 1635          # 4:5 safe band
CREAM = (243, 238, 228)
INK = (2, 43, 73)
BODY = (65, 96, 119)
CTA_A, CTA_B = (44, 77, 99), (142, 166, 180)
RED = (178, 34, 34)
WHITE = (255, 255, 255)
COLOURS = ["chalk", "obsidian", "sol", "dune", "pine", "blossom"]
SWATCH = {"chalk": (236, 229, 214), "obsidian": (38, 38, 40), "sol": (226, 172, 46), "dune": (184, 108, 62),
          "pine": (96, 104, 66), "blossom": (206, 52, 92)}

def font(name, size, weight=None):
    f = ImageFont.truetype(str(FONTS / name), size)
    if weight:
        f.set_variation_by_name(weight)
    return f


# Landing-page type system (landing-pages/retra/index.html): display = Tinos (Times New Roman metrics),
# weight 400, letter-spacing -0.04em; body = Inter; hand/kicker = Shantell Sans italic.
def tinos(size, track=-0.04):
    f = ImageFont.truetype(str(FONTS / "Tinos-Regular.ttf"), size)
    f.track = track * size
    return f


def shantell(size, track=0.0, bold=False):
    f = ImageFont.truetype(str(FONTS / ("ShantellSans-BoldItalic.ttf" if bold else "ShantellSans-Italic.ttf")), size)
    f.track = track * size
    return f


def inter(size, weight="Bold"):
    return font("Inter.ttf", size, weight)


def measure(f, text):
    return f.getlength(text) + getattr(f, "track", 0) * max(0, len(text) - 1)


def draw_text(d, xy, text, f, fill):
    tr = getattr(f, "track", 0)
    if not tr:
        d.text(xy, text, font=f, fill=fill)
        return
    x, y = xy
    for i, ch in enumerate(text):
        # where this glyph sits in the normally kerned line, plus i steps of tracking
        gx = f.getlength(text[: i + 1]) - f.getlength(ch) + i * tr
        d.text((x + gx, y), ch, font=f, fill=fill)


def wrap(text, f, maxw):
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if measure(f, t) <= maxw or not cur:
            cur = t
        else:
            lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines


def balanced(text, f, maxw):
    """Like CSS text-wrap: balance - same line count, narrowest width that still fits."""
    lines = wrap(text, f, maxw)
    if len(lines) < 2:
        return lines
    lo, hi = maxw * 0.4, maxw
    while hi - lo > 2:
        mid = (lo + hi) / 2
        if len(wrap(text, f, mid)) == len(lines) and all(measure(f, l) <= mid for l in wrap(text, f, mid)):
            hi = mid
        else:
            lo = mid
    return wrap(text, f, hi)


def fit(text, make_font, maxw, max_lines, start, floor):
    size = start
    while size > floor:
        f = make_font(size)
        lines = wrap(text, f, maxw)
        if len(lines) <= max_lines and all(measure(f, l) <= maxw for l in lines):
            return f, balanced(text, f, maxw)
        size -= 2
    f = make_font(floor)
    return f, balanced(text, f, maxw)


TEXT_BOXES = []  # (ad, box) for the text-coverage check


def draw_lines(img, lines, f, x, y, fill, align="left", lead=1.05, shadow=None, width=None):
    d = ImageDraw.Draw(img)
    asc, desc = f.getmetrics()
    lh = int((asc + desc) * lead)
    y0 = y
    for line in lines:
        lw = measure(f, line)
        if align == "center":
            lx = x + (width - lw) / 2
        elif align == "right":
            lx = x + width - lw
        else:
            lx = x
        if shadow:
            sh = Image.new("RGBA", img.size, (0, 0, 0, 0))
            draw_text(ImageDraw.Draw(sh), (lx + 2, y + 3), line, f, shadow)
            sh = sh.filter(ImageFilter.GaussianBlur(4))
            img.alpha_composite(sh)
            d = ImageDraw.Draw(img)
        draw_text(d, (lx, y), line, f, fill)
        TEXT_BOXES.append((lx, y, lx + lw, y + lh))
        y += lh
    return y


def scrim(img, top, bottom, color=(0, 0, 0), max_a=150, direction="down"):
    """Vertical gradient band: 'down' = strongest at top, 'up' = strongest at bottom."""
    band = np.linspace(1, 0, bottom - top) if direction == "down" else np.linspace(0, 1, bottom - top)
    a = (band ** 1.3 * max_a).astype("uint8")
    alpha = Image.fromarray(np.repeat(a[:, None], img.width, 1))
    layer = Image.new("RGBA", (img.width, bottom - top), color + (0,))
    layer.putalpha(alpha)
    img.alpha_composite(layer, (0, top))


def pill(img, text, f, cx, cy, bg, fg, padx=30, pady=16, radius=None):
    d = ImageDraw.Draw(img)
    tw = measure(f, text)
    asc, desc = f.getmetrics()
    h = asc + desc + 2 * pady
    w = tw + 2 * padx
    box = (cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2)
    if bg == "cta":  # landing-page CTA: slate-blue gradient pill
        grad = Image.new("RGBA", (int(w), int(h)))
        gd = ImageDraw.Draw(grad)
        for i in range(int(w)):
            t = i / max(1, w - 1)
            gd.line([(i, 0), (i, h)], fill=tuple(int(a + (b - a) * t) for a, b in zip(CTA_A, CTA_B)) + (255,))
        m = Image.new("L", grad.size, 0)
        ImageDraw.Draw(m).rounded_rectangle((0, 0, w - 1, h - 1), radius=h / 2, fill=255)
        img.paste(grad, (int(box[0]), int(box[1])), m)
    else:
        d.rounded_rectangle(box, radius=radius or h / 2, fill=bg)
    draw_text(d, (cx - tw / 2, cy - h / 2 + pady), text, f, fg)
    TEXT_BOXES.append(box)
    return box


def src_path(path):
    """Raw renders are committed as JPEG archives; the full PNGs stay local (gitignored)."""
    path = Path(path)
    return path if path.exists() else path.with_suffix(".jpg")


def scene(path):
    im = Image.open(src_path(path)).convert("RGB")
    return ImageOps.fit(im, (W, H), Image.LANCZOS, centering=(0.5, 0.5)).convert("RGBA")


def soft_blur_region(img, box, radius=7, feather=18):
    """Out-of-focus pass on one region (used to keep tiny background UI/sign text unreadable)."""
    blurred = img.filter(ImageFilter.GaussianBlur(radius))
    m = Image.new("L", img.size, 0)
    ImageDraw.Draw(m).rounded_rectangle(box, radius=feather, fill=255)
    m = m.filter(ImageFilter.GaussianBlur(feather))
    img.paste(blurred, (0, 0), m)


def grain(img, amount=4, seed=1):
    rng = np.random.default_rng(seed)
    a = np.asarray(img.convert("RGB")).astype(np.int16)
    a = np.clip(a + rng.normal(0, amount, a.shape[:2])[..., None], 0, 255).astype("uint8")
    return Image.fromarray(a).convert("RGBA")


def typeset(t):
    """Typesetting only (no wording change): curly apostrophes."""
    return t.replace("'", "\u2019")




def cam(colour, width, angle=0):
    """Clean 3/4 cut-out of one colour, scaled to `width` px."""
    im = Image.open(CUT / f"retra_{colour}_34.png").convert("RGBA")
    im = im.resize((width, int(im.height * width / im.width)), Image.LANCZOS)
    return im.rotate(angle, Image.BICUBIC, expand=True) if angle else im


def front(colour, width):
    """Straight-on 4K front cut-out (chalk / obsidian / sol only)."""
    im = Image.open(GAL / "cutouts" / f"front_{colour}.png").convert("RGBA")
    return im.resize((width, int(im.height * width / im.width)), Image.LANCZOS)


def place(img, obj, cx, cy, shadow=0.35, blur=26, drop=(0, 26)):
    """Paste obj centred at (cx, cy) with a soft contact shadow."""
    x, y = int(cx - obj.width / 2), int(cy - obj.height / 2)
    if shadow:
        sh = Image.new("RGBA", img.size, (0, 0, 0, 0))
        a = obj.getchannel("A").point(lambda v: int(v * shadow))
        sh.paste(Image.new("RGBA", obj.size, (20, 15, 10, 255)), (x + drop[0], y + drop[1]), a)
        img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(blur)))
    img.alpha_composite(obj, (x, y))
    return (x, y, x + obj.width, y + obj.height)


def canvas(color=CREAM):
    return Image.new("RGBA", (W, H), color + (255,))


def save(img, stem):
    """Write the 9:16 master and its centred 4:5 crop."""
    rgb = img.convert("RGB")
    rgb.save(OUT / f"{stem}_9x16.png")
    rgb.crop((0, TOP, W, BOT)).save(OUT / f"{stem}_4x5.png")
    return OUT / f"{stem}_4x5.png"
