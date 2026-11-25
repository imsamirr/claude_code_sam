import sys, random
from PIL import Image, ImageEnhance, ImageOps, ImageFilter, ImageChops
src, outdir = sys.argv[1], sys.argv[2]
im = Image.open(src).convert('RGB')
w, h = im.size
def grain(img, amt):
    n = Image.effect_noise((w, h), amt).convert('RGB')
    return ImageChops.add(ImageChops.subtract(img, Image.new('RGB',(w,h),(8,8,8))), n.point(lambda v: v*0.06))
def vignette(img, strength=0.35):
    m = Image.radial_gradient('L').resize((w, h)); m = m.point(lambda v: 255 - int(v*strength))
    return Image.composite(img, Image.new('RGB',(w,h),(0,0,0)), m)
def curves(img, r, g, b):
    return Image.merge('RGB', [c.point(f) for c, f in zip(img.split(), (r, g, b))])
# Natural: as shot, light clean-up
nat = ImageEnhance.Contrast(im).enhance(1.03)
# Vintage: warm, faded blacks, lower saturation, soft vignette
v = ImageEnhance.Color(im).enhance(0.75)
v = curves(v, lambda x: int(34 + x*0.86), lambda x: int(24 + x*0.8), lambda x: int(12 + x*0.6))
v = vignette(v.filter(ImageFilter.GaussianBlur(0.6)), 0.4)
# B&W: contrasty mono with grain
bw = ImageOps.grayscale(im); bw = ImageEnhance.Contrast(bw).enhance(1.25).convert('RGB'); bw = grain(bw, 40)
# Film: cool-green shadows, warm highlights, grain
f = ImageEnhance.Contrast(ImageEnhance.Color(im).enhance(1.3)).enhance(1.12)
f = curves(f, lambda x: min(255, int(16 + x*1.0)), lambda x: int(6 + x*0.93), lambda x: int(x*0.74))
f = grain(vignette(f, 0.25), 50)
for name, img in [('natural', nat), ('vintage', v), ('bw', bw), ('film', f)]:
    img.save(f'{outdir}/filter-{name}.jpg', quality=84)
print('ok')
