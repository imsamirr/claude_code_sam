"""Smooth the outline of cutout/retra_<c>_34.png -> cutout_clean/retra_<c>_34.png (no re-render).
Removes thin spikes along the side and bottom (floor-shadow leftovers) with a morphological opening, then feathers."""
from pathlib import Path
import cv2, numpy as np
from PIL import Image
HERE = Path(__file__).resolve().parent
(HERE / "cutout_clean").mkdir(exist_ok=True)
for c in ["chalk", "obsidian", "blossom", "sol", "pine", "dune"]:
    im = Image.open(HERE / f"cutout/retra_{c}_34.png").convert("RGBA")
    a = np.asarray(im)
    m = (a[..., 3] > 127).astype(np.uint8)
    k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (31, 31))
    m = cv2.morphologyEx(m, cv2.MORPH_OPEN, k)
    n, lab, st, _ = cv2.connectedComponentsWithStats(m)
    m = (lab == 1 + np.argmax(st[1:, cv2.CC_STAT_AREA])).astype(np.uint8)
    m = cv2.erode(m, np.ones((3, 3), np.uint8), iterations=1)
    # smooth the contour itself (removes stair-steps) by re-drawing a simplified polygon
    cs, _ = cv2.findContours(m, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cnt = max(cs, key=cv2.contourArea)
    cnt = cv2.approxPolyDP(cnt, 1.5, True)
    mm = np.zeros_like(m); cv2.fillPoly(mm, [cnt], 1)
    alpha = cv2.GaussianBlur(mm.astype(np.float32), (0, 0), 1.1)
    out = a.copy(); out[..., 3] = (np.clip(alpha, 0, 1) * 255).astype(np.uint8)
    o = Image.fromarray(out); o = o.crop(o.getbbox()); o.save(HERE / f"cutout_clean/retra_{c}_34.png")
    print(c, o.size)
