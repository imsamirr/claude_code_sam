"""Print the Retra box artwork on the gift-box lids (under the navy ribbon) in renders/gift_<colour>_t1.png.

    python3 print_gift.py  ->  renders/gift_<colour>_printed.png
Lid corners (TL, TR, BR, BL) from picks.json["gift_lids"]. Ribbon = navy pixels, kept on top; the lid's old
gold wordmark is painted over; ribbon shadows stay as shading.
"""
import json
from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageOps

HERE = Path(__file__).resolve().parent
S = 2000
LIDS = json.load(open(HERE / "picks.json"))["gift_lids"]
PAPER = (252, 251, 249)

for c, quad in LIDS.items():
    src = HERE / "renders" / f"gift_{c}_t1.png"
    src = src if src.exists() else src.with_suffix(".jpg")  # PNGs stay local
    base = np.asarray(ImageOps.fit(Image.open(src).convert("RGB"), (S, S),
                                   Image.LANCZOS)).astype(np.float32)
    dst = np.float32(quad)
    lid_w = (np.linalg.norm(dst[1] - dst[0]) + np.linalg.norm(dst[2] - dst[3])) / 2
    lid_h = (np.linalg.norm(dst[3] - dst[0]) + np.linalg.norm(dst[2] - dst[1])) / 2
    art = Image.open(HERE / "packaging" / "retra_box_lid.png").convert("RGB")  # branding-only lid
    th = int(art.width * lid_h / lid_w)  # pad the 1.6:1 panel to the lid's proportions
    padded = Image.new("RGB", (art.width, max(th, art.height)), PAPER)
    padded.paste(art, (0, (padded.height - art.height) // 2))
    a = np.asarray(padded).astype(np.float32)
    h, w = a.shape[:2]
    M = cv2.getPerspectiveTransform(np.float32([[0, 0], [w, 0], [w, h], [0, h]]), dst)
    warped = cv2.warpPerspective(a, M, (S, S), flags=cv2.INTER_AREA)
    hsv = cv2.cvtColor(base.astype(np.uint8), cv2.COLOR_RGB2HSV)
    r, g, b = base[..., 0], base[..., 1], base[..., 2]
    ribbon = ((b - r > 22) & (hsv[..., 1] > 50)) | (hsv[..., 2] < 135)  # navy satin, incl. its dark folds
    ribbon = cv2.morphologyEx(ribbon.astype(np.uint8), cv2.MORPH_CLOSE, np.ones((9, 9), np.uint8))
    ribbon = cv2.dilate(ribbon, np.ones((3, 3), np.uint8), iterations=2).astype(bool)
    gold = (r - b > 18) & (hsv[..., 2] > 90)
    gold = cv2.dilate(gold.astype(np.uint8), np.ones((5, 5), np.uint8), iterations=3).astype(bool)
    inside = cv2.fillPoly(np.zeros((S, S), np.uint8), [dst.astype(np.int32)], 1).astype(bool)
    mask = np.zeros((S, S), np.uint8)
    cen = dst.mean(0)
    shr = cen + (dst - cen) * (1 - 3 / np.linalg.norm(dst - cen, axis=1, keepdims=True))
    cv2.fillPoly(mask, [shr.astype(np.int32)], 255)
    mask[ribbon] = 0
    mask = cv2.GaussianBlur(mask, (0, 0), 0.8).astype(np.float32)[..., None] / 255
    lum = base.mean(-1)
    ref = np.percentile(lum[inside & ~ribbon & ~gold], 95)
    lum2 = lum.copy()
    lum2[gold | ribbon] = ref  # ignore the old wordmark and the ribbon itself when estimating shading
    lum2 = cv2.inpaint(np.clip(lum2, 0, 255).astype(np.uint8), (gold & inside).astype(np.uint8) * 255, 5,
                       cv2.INPAINT_TELEA).astype(np.float32)
    shade = np.clip(cv2.GaussianBlur(lum2, (0, 0), 3) / ref, 0.5, 1.03)[..., None]
    out = base * (1 - mask) + (warped * shade) * mask
    Image.fromarray(np.clip(out, 0, 255).astype(np.uint8)).save(HERE / "renders" / f"gift_{c}_printed.png")
    print(c)
