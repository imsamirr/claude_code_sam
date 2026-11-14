"""TikTok 'Classic' caption renderer matched to the reference (measured at 1080x1920):
stacked per-line white rounded boxes, black bold TikTok Sans, line pitch 58 px, single-line box 105 px,
centred at y=1275, max box width ~510 px."""
from functools import lru_cache
from PIL import Image, ImageDraw, ImageFont
FONT = ImageFont.truetype("/home/user/claude_code_sam/ads/video/fonts/TikTokSans-700.ttf", 46)
TRACK = -1.9
PITCH, BOXH, PADX, RAD, MAXW = 58, 105, 27, 24, 456

_D = ImageDraw.Draw(Image.new("RGB", (1, 1)))
def tlen(s, fnt=FONT): return sum(_D.textlength(c, font=fnt) for c in s) + TRACK * max(0, len(s) - 1)
def tdraw(d, xy, s, fnt=FONT, fill=(0, 0, 0)):
    x, y = xy
    for c in s: d.text((x, y), c, font=fnt, fill=fill); x += _D.textlength(c, font=fnt) + TRACK

def wrap(text, fnt=FONT, maxw=MAXW):
    lines, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if cur and tlen(t, fnt) > maxw: lines.append(cur); cur = w
        else: cur = t
    return lines + ([cur] if cur else [])

@lru_cache(maxsize=1024)
def caption(text, upper=False):
    text = text.upper() if upper else text
    lines = wrap(text); d0 = ImageDraw.Draw(Image.new("RGB", (1, 1)))
    widths = [tlen(l) for l in lines]
    W = int(max(widths) + 2 * PADX) + 4; H = BOXH + PITCH * (len(lines) - 1) + 4
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    for i, (l, w) in enumerate(zip(lines, widths)):
        bw = w + 2 * PADX; x0 = (W - bw) / 2; y0 = 2 + i * PITCH
        d.rounded_rectangle((x0, y0, x0 + bw, y0 + BOXH), RAD, fill=(255, 255, 255, 255))
    asc, desc = FONT.getmetrics()
    for i, (l, w) in enumerate(zip(lines, widths)):
        y = 2 + i * PITCH + (BOXH - (asc + desc)) / 2 + 2
        tdraw(d, ((W - w) / 2, y), l)
    return im
