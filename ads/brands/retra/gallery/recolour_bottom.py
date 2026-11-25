"""Recolour the landing page's Aegean bottom-view render (base/bottom.jpg) to Chalk/Obsidian/Sol.

Deterministic pixel recolour of the leatherette panel only (ports, buttons, body untouched), because Kie
ignored the bottom angle when asked to recolour it. Output: renders/bottom_<colour>_recolour.png
"""
import numpy as np
from PIL import Image
from scipy import ndimage

im = Image.open("base/bottom.jpg").convert("RGB")
a = np.asarray(im).astype(float) / 255
r, g, b = a[..., 0], a[..., 1], a[..., 2]
mx, mn = a.max(-1), a.min(-1)
sat = (mx - mn) / np.maximum(mx, 1e-6)
lum = 0.299 * r + 0.587 * g + 0.114 * b
core = (b > r + 0.04) & (sat > 0.12)
core = ndimage.binary_opening(core, iterations=2)
lab, n = ndimage.label(core)
core = lab == (1 + np.argmax(ndimage.sum(core, lab, range(1, n + 1))))
near = ndimage.binary_dilation(core, iterations=45)
loose = ((b > r - 0.005) & (sat > 0.04) & (mx > 0.25)) | ((np.abs(r - b) < 0.07) & (lum > 0.30))
panel = ndimage.binary_closing(core | (loose & near), iterations=4)
holes = ndimage.binary_fill_holes(panel) & ~panel  # pill button etc. sit in holes of the panel: never repaint them
holes = ndimage.binary_dilation(holes, iterations=3)
panel &= (lum > 0.18) | core
lab, n = ndimage.label(panel)
panel = lab == (1 + np.argmax(ndimage.sum(panel, lab, range(1, n + 1))))
panel |= ndimage.binary_dilation(panel, iterations=14) & (lum > 0.25) & (r - b < 0.08)  # pale end-edge sliver (not tan bg, not dark body)
L = lum[core]
lo, hi = np.percentile(L, 2), np.percentile(L, 98)
t = np.clip((lum - lo) / (hi - lo), 0, 1)
TARGETS = {"chalk": ((150, 146, 138), (236, 232, 222)), "obsidian": ((20, 20, 22), (68, 68, 70)),
           "sol": ((168, 112, 20), (240, 184, 58))}
panel &= ~holes
soft = ndimage.gaussian_filter(panel.astype(float), 0.8)[..., None]
for c, (dark, light) in TARGETS.items():
    dark, light = np.array(dark) / 255, np.array(light) / 255
    out = a * (1 - soft) + (dark + (light - dark) * t[..., None]) * soft
    Image.fromarray((np.clip(out, 0, 1) * 255).astype("uint8")).save(f"renders/bottom_{c}_recolour.png")
print("ok")
