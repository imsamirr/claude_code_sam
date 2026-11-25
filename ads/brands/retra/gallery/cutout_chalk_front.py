"""Cut out front_chalk_t2 (off-white panel on cream: too close for a colour key).

Mask = not-green in Kie's green-screen copy (renders/front_chalk_green.png), clipped below the black bottom
band; pixels come from the original render so no green spill. -> renders/front_chalk_cutout.png
"""
import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage

g_im = np.asarray(Image.open("renders/front_chalk_green.png").convert("RGB")).astype(int)
src = Image.open("renders/front_chalk_t2.png").convert("RGB")
r, g, b = g_im[..., 0], g_im[..., 1], g_im[..., 2]
green = (g > r + 40) & (g > b + 30)
m = ~green
lum = g_im.sum(-1)
# bottom band: lowest row where dark pixels cover a long run inside the camera's columns
cols = np.where((~green).sum(0) > 0)[0]
dark = lum < 200
rows = np.where(dark.sum(1) > 0.5 * (cols.max() - cols.min()))[0]
bottom = rows.max()
m[bottom + 3:] = False
m = ndimage.binary_opening(m, iterations=2)
lab, n = ndimage.label(m)
m = lab == (1 + np.argmax(ndimage.sum(m, lab, range(1, n + 1))))
m = ndimage.binary_fill_holes(m)
mask = Image.fromarray((m * 255).astype("uint8")).filter(ImageFilter.GaussianBlur(1.2))
o = src.copy()
o.putalpha(mask)
o = o.crop(mask.getbbox())
o.save("renders/front_chalk_cutout.png")
print(o.size, "bottom row", bottom)
