"""Cut each Retra product shot out of its flat beige background -> cutout/retra_<colour>_34.png.

The floor shadow is removed by colour (beige/warm) and, per column, by cutting everything below the camera's
neutral dark bottom band.  python3 assets/retra/product/make_cutouts.py
"""
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage

HERE = Path(__file__).resolve().parent
(HERE / "cutout").mkdir(exist_ok=True)
for c in ["chalk", "obsidian", "blossom", "sol", "pine", "dune"]:
    im = Image.open(HERE / f"retra_{c}_34.jpg").convert("RGB")
    a = np.asarray(im).astype(float)
    bg = np.median(np.concatenate([a[:50].reshape(-1, 3), a[:, :50].reshape(-1, 3)]), axis=0)
    lum = a.sum(-1)
    chd = np.abs(a / np.maximum(lum[..., None], 1) - bg / bg.sum()).sum(-1)
    d = np.sqrt(((a - bg) ** 2).sum(-1))
    m = ~((d <= 38) | ((chd < 0.045) & (lum > 170)))
    m = ndimage.binary_opening(m, iterations=2)
    m = ndimage.binary_closing(m, iterations=4)
    m = ndimage.binary_fill_holes(m)
    lab, n = ndimage.label(m)
    m = lab == (1 + np.argmax(ndimage.sum(m, lab, range(1, n + 1))))
    # per column: keep nothing below the lowest neutral-dark pixel (the black bottom band)
    neutral_dark = (lum < 260) & (np.abs(a[..., 0] - a[..., 2]) < 16)
    h = m.shape[0]
    start = int(h * 0.5)
    for x in range(m.shape[1]):
        col = np.where(neutral_dark[start:, x] & m[start:, x])[0]
        if len(col):
            m[start + col.max() + 2:, x] = False
    m = ndimage.binary_opening(m, iterations=3)
    lab, n = ndimage.label(m)
    m = lab == (1 + np.argmax(ndimage.sum(m, lab, range(1, n + 1))))
    m = ndimage.binary_fill_holes(m)
    mask = Image.fromarray((m * 255).astype("uint8")).filter(ImageFilter.GaussianBlur(1.2))
    out = im.copy()
    out.putalpha(mask)
    out = out.crop(mask.getbbox())
    out.save(HERE / "cutout" / f"retra_{c}_34.png")
    print(c, out.size)
