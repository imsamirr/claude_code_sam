"""Spanish (US) version of the Comfort Wear Black Friday end card.

Takes the final frame of the English card, removes its English elements (ribbon, offer ticket,
SALE tapes, badges) with OpenCV inpainting, redraws them in Spanish, and animates the build like
the original: title + shoes, then ribbon, ticket, tapes and badges pop in, then hold.

    python ads/video/make_end_card_es.py
    -> ads/brands/comfortwear/video/end_cards/black_friday_2026_es.mp4 (+ _es_still.png)
"""

import math
import subprocess
import tempfile
from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = Path(__file__).resolve().parents[2]
FONTS = ROOT / "ads" / "video" / "fonts"
CARDS = ROOT / "ads" / "brands" / "comfortwear" / "video" / "end_cards"
SRC = CARDS / "black_friday_2026.mp4"
OUT = CARDS / "black_friday_2026_es.mp4"
W, H, FPS, DUR = 1080, 1920, 30, 7.0
RED, DARK_RED = (226, 6, 19), (186, 10, 30)


def font(weight, size):
    return ImageFont.truetype(str(FONTS / f"Inter-{weight}.otf"), size)


def condensed_text(text, weight, size, fill, squeeze=0.82, stroke=0):
    """Text rendered then squeezed horizontally (a condensed, poster look)."""
    f = font(weight, size)
    l, t, r, b = f.getbbox(text, stroke_width=stroke)
    im = Image.new("RGBA", (r - l + 8, b - t + 8), (0, 0, 0, 0))
    ImageDraw.Draw(im).text((4 - l, 4 - t), text, font=f, fill=fill, stroke_width=stroke,
                            stroke_fill=(0, 0, 0))
    return im.resize((int(im.width * squeeze), im.height), Image.LANCZOS)


def base_frame():
    tmp = Path(tempfile.mkdtemp()) / "f.png"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", "6.0", "-i", str(SRC), "-frames:v", "1", str(tmp)], check=True)
    img = cv2.imread(str(tmp))
    mask = np.zeros(img.shape[:2], np.uint8)
    # English elements (measured on the 1080x1920 frame)
    cv2.fillPoly(mask, [np.array([[0, 30], [1080, 150], [1080, 230], [0, 110]])], 255)       # top SALE tape
    cv2.fillPoly(mask, [np.array([[312, 425], [742, 408], [742, 490], [312, 505]])], 255)     # 'sale is here' ribbon
    cv2.fillPoly(mask, [np.array([[195, 650], [850, 650], [850, 1015], [195, 1015]])], 255)   # 60% OFF ticket
    cv2.fillPoly(mask, [np.array([[0, 1490], [1080, 1250], [1080, 1365], [0, 1625]])], 255)   # lower SALE tape
    cv2.circle(mask, (168, 1758), 150, 255, -1)                                                # 30-day seal
    cv2.rectangle(mask, (770, 1600), (1065, 1900), 255, -1)                                     # free shipping
    clean = cv2.inpaint(img, mask, 9, cv2.INPAINT_TELEA)
    # the lower tape crossed the shoes; inpainting smears there, so a new tape covers it anyway
    return Image.fromarray(cv2.cvtColor(clean, cv2.COLOR_BGR2RGB)).convert("RGBA")


def tape(text, angle, length=1500, thick=78):
    band = Image.new("RGBA", (length, thick), RED + (255,))
    d = ImageDraw.Draw(band)
    word = condensed_text(text, "Black", 50, (0, 0, 0), squeeze=0.9)
    x = 10
    while x < length:
        band.alpha_composite(word, (x, (thick - word.height) // 2))
        x += word.width + 34
    return band.rotate(angle, expand=True, resample=Image.BICUBIC)


def ribbon(text):
    t = condensed_text(text, "ExtraBold", 74, (255, 255, 255), squeeze=0.95)
    im = Image.new("RGBA", (max(t.width + 90, 470), t.height + 40), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    w, h = im.size
    d.polygon([(10, 6), (w - 4, 0), (w - 16, h - 4), (0, h)], fill=RED + (255,))
    im.alpha_composite(t, ((im.width - t.width) // 2, 18))
    return im.rotate(3, expand=True, resample=Image.BICUBIC)


def ticket():
    w, h = 700, 380
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, w, h], 26, fill=DARK_RED + (255,))
    for y in range(30, h - 20, 46):               # ticket notches
        d.ellipse([-14, y, 14, y + 28], fill=(0, 0, 0, 0))
        d.ellipse([w - 14, y, w + 14, y + 28], fill=(0, 0, 0, 0))
    l1 = condensed_text("60% DE", "Black", 150, (255, 255, 255), squeeze=0.86)
    l2 = condensed_text("DESCUENTO", "Black", 104, (255, 255, 255), squeeze=0.86)
    l3 = condensed_text("+ 2 REGALOS GRATIS", "ExtraBold", 66, (255, 255, 255), squeeze=0.86)
    y = 22
    for line in (l1, l2, l3):
        im.alpha_composite(line, ((w - line.width) // 2, y))
        y += line.height + 2
    return im.rotate(6, expand=True, resample=Image.BICUBIC)


def seal():
    s = 300
    im = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    pts = []
    for k in range(64):                           # scalloped gold edge
        r = s / 2 - (0 if k % 2 else 10)
        a = 2 * math.pi * k / 64
        pts.append((s / 2 + r * math.cos(a), s / 2 + r * math.sin(a)))
    d.polygon(pts, fill=(212, 170, 60, 255))
    d.ellipse([22, 22, s - 22, s - 22], fill=(245, 214, 110, 255))
    d.ellipse([38, 38, s - 38, s - 38], fill=(20, 98, 48, 255))
    for txt, size, y in (("30 DÍAS", 62, 70), ("GARANTÍA DE", 30, 150), ("DEVOLUCIÓN", 30, 186)):
        t = condensed_text(txt, "Black", size, (255, 236, 160), squeeze=0.86)
        im.alpha_composite(t, ((s - t.width) // 2, y))
    star = condensed_text("★ ★ ★", "Black", 26, (255, 236, 160), squeeze=1.0)
    im.alpha_composite(star, ((s - star.width) // 2, 228))
    return im.rotate(-8, expand=True, resample=Image.BICUBIC)


def shipping():
    BW = 300
    im = Image.new("RGBA", (BW, 270), (0, 0, 0, 0))
    t1 = condensed_text("ENVÍO", "Black", 96, (0, 0, 0), squeeze=0.78)
    t2 = condensed_text("GRATIS", "Black", 92, (255, 255, 255), squeeze=0.74)
    t3 = condensed_text("EN TODOS LOS PEDIDOS", "ExtraBold", 30, (255, 255, 255), squeeze=0.74)
    d = ImageDraw.Draw(im)
    im.alpha_composite(t1, ((BW - t1.width) // 2, 0))
    d.rectangle([0, t1.height + 2, BW, t1.height + t2.height + 6], fill=(0, 0, 0, 255))
    im.alpha_composite(t2, ((BW - t2.width) // 2, t1.height + 4))
    y3 = t1.height + t2.height + 16
    d.rectangle([(BW - t3.width) // 2 - 10, y3 - 4, (BW + t3.width) // 2 + 10, y3 + t3.height + 4], fill=(0, 0, 0, 255))
    im.alpha_composite(t3, ((BW - t3.width) // 2, y3))
    return im.rotate(6, expand=True, resample=Image.BICUBIC)


def shadow(layer, blur=14, offset=(0, 10), alpha=150):
    sh = Image.new("RGBA", layer.size, (0, 0, 0, 0))
    sh.putalpha(layer.getchannel("A").point(lambda a: min(a, alpha)))
    sh = sh.filter(ImageFilter.GaussianBlur(blur))
    out = Image.new("RGBA", (layer.width + 2 * blur + abs(offset[0]), layer.height + 2 * blur + abs(offset[1])), (0, 0, 0, 0))
    out.alpha_composite(sh, (blur + offset[0], blur + offset[1]))
    out.alpha_composite(layer, (blur, blur))
    return out, blur


def main():
    base = base_frame()
    # elements: (layer, center x, center y, appear time, pop) in draw order
    top = tape("OFERTA", -6.3, length=1400, thick=90)
    low = tape("OFERTA", 12.8, length=1500, thick=110)
    rib = ribbon("¡ya llegó!")
    tk, _ = shadow(ticket())
    sl, _ = shadow(seal(), blur=8, offset=(0, 6))
    sp = shipping()
    els = [(top, 540, 132, 0.15, False), (rib, 527, 457, 0.35, True), (tk, 525, 835, 0.0, "pulse"),
           (low, 540, 1438, 0.0, "static"), (sl, 175, 1755, 1.15, True), (sp, 905, 1752, 1.3, True)]
    tmp = Path(tempfile.mkdtemp())
    n = int(DUR * FPS)
    for i in range(n):
        t = i / FPS
        fr = base.copy()
        for layer, cx, cy, t0, pop in els:
            if t < t0:
                continue
            k = min(1.0, (t - t0) / 0.22)
            if pop == "static":
                lay = layer
            elif pop == "pulse":   # always on (it hides cleanup underneath); grows +10% at 0.6s
                kk = min(1.0, max(0.0, (t - 0.6) / 0.35))
                sc = 1 + 0.10 * math.sin(math.pi * kk)
                lay = layer.resize((int(layer.width * sc), int(layer.height * sc)), Image.BICUBIC)
            elif pop:   # overshoot scale-in
                s = 1.0 + 0.18 * math.sin(math.pi * k) if k < 1 else 1.0
                s *= 0.6 + 0.4 * k
                lay = layer.resize((max(1, int(layer.width * s)), max(1, int(layer.height * s))), Image.BICUBIC)
            else:     # tapes slide in from the left
                lay = layer
                cx = cx - int((1 - k) ** 2 * 1300)
            fr.alpha_composite(lay, (int(cx - lay.width / 2), int(cy - lay.height / 2)))
        if t > 1.8:   # gentle push-in for the rest of the card
            z = 1 + 0.03 * (t - 1.8) / (DUR - 1.8)
            fr = fr.resize((int(W * z), int(H * z)), Image.BICUBIC).crop(
                (int((W * z - W) / 2), int((H * z - H) / 2), int((W * z - W) / 2) + W, int((H * z - H) / 2) + H))
        fr.convert("RGB").save(tmp / f"{i:04d}.png")
        if i == n - 1:
            fr.convert("RGB").save(CARDS / "black_friday_2026_es_still.png")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-framerate", str(FPS), "-i", str(tmp / "%04d.png"),
                    "-f", "lavfi", "-t", str(DUR), "-i", "anullsrc=r=48000:cl=stereo",
                    "-c:v", "libx264", "-crf", "16", "-pix_fmt", "yuv420p", "-c:a", "aac", "-shortest",
                    "-movflags", "+faststart", str(OUT)], check=True)
    print(OUT)


if __name__ == "__main__":
    main()
