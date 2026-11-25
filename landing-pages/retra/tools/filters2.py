# Klik-like filter looks: Natural (as shot), Vintage (warm fade), B&W (neutral mono), Film (cool cross-process)
import sys
from PIL import Image, ImageEnhance, ImageOps, ImageChops
src, out = sys.argv[1], sys.argv[2]
im = Image.open(src).convert('RGB'); w, h = im.size
def curves(img, r, g, b): return Image.merge('RGB', [c.point(f) for c, f in zip(img.split(), (r, g, b))])
def grain(img, a):
    n = Image.effect_noise((w, h), a).convert('RGB').point(lambda v: (v - 128) * 0.08 + 128)
    return ImageChops.add(img, n, 1, -128)
looks = {
 'natural': ImageEnhance.Contrast(im).enhance(1.02),
 'vintage': curves(ImageEnhance.Color(im).enhance(0.78), lambda x: int(26 + x * .88), lambda x: int(20 + x * .84), lambda x: int(14 + x * .72)),
 'bw': grain(ImageEnhance.Contrast(ImageOps.grayscale(im)).enhance(1.18).convert('RGB'), 30),
 'film': grain(curves(ImageEnhance.Contrast(ImageEnhance.Color(im).enhance(.9)).enhance(.92), lambda x: int(18 + x * .86), lambda x: int(14 + x * .84), lambda x: int(36 + x * .84)), 36),
}
for k, v in looks.items():
    v.thumbnail((1400, 1400)); v.save(f'{out}-{k}.jpg', quality=84, optimize=True, progressive=True)
