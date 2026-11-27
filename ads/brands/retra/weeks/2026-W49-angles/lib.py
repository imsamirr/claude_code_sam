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
CTA_MID = (75, 107, 128)          # site --cta: #2C4D63 0% / #4B6B80 45% / #8EA6B4 100%
NAVY50 = (128, 149, 164)           # site --navy-50 (#022B49 at 50%) on white
KICKER = (163, 150, 128)           # site --kicker #A39680
SAND = (217, 199, 174)             # site --sand #D9C7AE
PILL_DARK = (14, 28, 39)           # site .pill #0e1c27
RED = (178, 34, 34)
WHITE = (255, 255, 255)
COLOURS = ["chalk", "obsidian", "sol", "dune", "pine", "blossom"]
SWATCH = {"chalk": (236, 229, 214), "obsidian": (38, 38, 40), "sol": (226, 172, 46), "dune": (184, 108, 62),
          "pine": (96, 104, 66), "blossom": (206, 52, 92), "aegean": (170, 197, 209)}
# Store display names (Shopify, renamed 2026-11-27; Blue/"aegean" is the 7th colour). Keys stay the old asset names.
STORE_NAME = {"chalk": "White", "obsidian": "Midnight", "sol": "Yellow", "dune": "Brown", "pine": "Green Forest",
              "aegean": "Blue", "blossom": "Red"}
STORE_ORDER = ["chalk", "dune", "pine", "aegean", "sol", "blossom", "obsidian"]  # store variant order

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
            a_, b_, u = (CTA_A, CTA_MID, t / 0.45) if t < 0.45 else (CTA_MID, CTA_B, (t - 0.45) / 0.55)
            gd.line([(i, 0), (i, h)], fill=tuple(int(a + (b - a) * u) for a, b in zip(a_, b_)) + (255,))
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


# ---------------------------------------------------------------- real product photos (Kie, white sweep)
PROD_PICKS = {"p34_chalk": "p34_chalk_t2", "p34_obsidian": "p34_obsidian_t2", "p34_dune": "p34_dune_t2"}  # default <name>_t1


def _level_white(a):
    """Lift the paper sweep to pure white (per-channel gain from the border median), keep shadows."""
    h, w = a.shape[:2]
    e = max(8, h // 40)
    border = np.concatenate([a[:e].reshape(-1, 3), a[-e:].reshape(-1, 3), a[:, :e].reshape(-1, 3), a[:, -e:].reshape(-1, 3)])
    bg = np.percentile(border, 60, axis=0)
    a = np.clip(a * (255.0 / np.maximum(bg, 1)), 0, 255)
    # near-white paper falloff -> pure white (values 228..244 stretched to 228..255); real shadows are darker
    return np.where(a > 228, np.minimum(255, 228 + (a - 228) * 1.7), a)


def product(name, width, pad=0.05, shadow=0.12, share=0.25):
    """A white-sweep product render, levelled to pure white, isolated to the camera(s) + contact shadow
    (stray props and backdrop edges fade to white), cropped and scaled to `width`."""
    import cv2
    stem = PROD_PICKS.get(name, f"{name}_t1")
    im = Image.open(HERE / "renders" / f"{stem}.png").convert("RGB")
    a = _level_white(np.asarray(im).astype(np.float32))
    h, w = a.shape[:2]
    dark = (a.min(-1) < (215 if share < 0.1 else 150)).astype(np.uint8)
    dark = cv2.morphologyEx(dark, cv2.MORPH_CLOSE, np.ones((max(5, w // 150),) * 2, np.uint8))
    n, lab, st, _ = cv2.connectedComponentsWithStats(dark)
    inner = [i for i in range(1, n) if st[i, 0] > 2 and st[i, 1] > 2 and st[i, 0] + st[i, 2] < w - 2
             and st[i, 1] + st[i, 3] < h - 2]  # ignore backdrop edges touching the frame
    inner = inner or list(range(1, n))  # subject fills the frame: keep everything
    top = max(st[i, cv2.CC_STAT_AREA] for i in inner)
    keep = [i for i in inner if st[i, cv2.CC_STAT_AREA] > top * share]  # the camera(s); drops props
    xs0 = min(st[i, 0] for i in keep); ys0 = min(st[i, 1] for i in keep)
    xs1 = max(st[i, 0] + st[i, 2] for i in keep); ys1 = max(st[i, 1] + st[i, 3] for i in keep)
    bw, bh = xs1 - xs0, ys1 - ys0
    sig = bw * 0.045
    # mask: body + a little side/top room + the contact shadow below, feathered; crop leaves room for the fade
    mx0, mx1 = xs0 - bw * pad * 0.6, xs1 + bw * pad * 0.6
    my0, my1 = ys0 - bh * pad * 0.6, ys1 + bh * shadow
    m = np.zeros((h, w), np.float32)
    m[int(max(0, my0)):int(min(h, my1)), int(max(0, mx0)):int(min(w, mx1))] = 1
    m = cv2.GaussianBlur(m, (0, 0), sig)
    X0, X1 = max(0, int(mx0 - 3 * sig)), min(w, int(mx1 + 3 * sig))
    Y0, Y1 = max(0, int(my0 - 3 * sig)), min(h, int(my1 + 3 * sig))
    a = a * m[..., None] + 255 * (1 - m[..., None])
    out = Image.fromarray(a[Y0:Y1, X0:X1].astype("uint8"))
    return out.resize((width, int(out.height * width / out.width)), Image.LANCZOS)


def multiply(img, photo, cx, cy):
    """Multiply-blend an RGB photo (white = transparent) centred at (cx, cy); returns the placed box."""
    from PIL import ImageChops
    x, y = int(cx - photo.width / 2), int(cy - photo.height / 2)
    box = (x, y, x + photo.width, y + photo.height)
    base = img.crop(box).convert("RGB")
    img.paste(ImageChops.multiply(base, photo).convert("RGBA"), (x, y))
    return box


def prod(img, name, width, cx, cy, **kw):
    return multiply(img, product(name, width, **kw), cx, cy)
