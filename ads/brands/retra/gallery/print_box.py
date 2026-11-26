"""Print the Retra box artwork (packaging/) onto the blank boxes in the Kie renders, keeping the render's lighting.

    python3 print_box.py   ->  renders/boxblank_<colour>_printed.png

Face corners (TL, TR, BR, BL in 2000x2000 render space) were read off a 50 px grid; see FACES.
"""
import json
from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageOps

HERE = Path(__file__).resolve().parent
S = 2000
FACES = json.load(open(HERE / "picks.json"))["box_faces"]


def print_on(render, art, quad, occluder=None, inset=3, blur=18):
    """Warp `art` onto `quad` of `render`; multiply by the face's own soft shading."""
    render = render if Path(render).exists() else Path(render).with_suffix(".jpg")  # PNGs stay local
    base = np.asarray(ImageOps.fit(Image.open(render).convert("RGB"), (S, S), Image.LANCZOS)).astype(np.float32)
    a = np.asarray(Image.open(art).convert("RGB")).astype(np.float32)
    h, w = a.shape[:2]
    src = np.float32([[0, 0], [w, 0], [w, h], [0, h]])
    dst = np.float32(quad)
    M = cv2.getPerspectiveTransform(src, dst)
    warped = cv2.warpPerspective(a, M, (S, S), flags=cv2.INTER_AREA)
    mask = np.zeros((S, S), np.uint8)
    c = dst.mean(0)
    shrunk = c + (dst - c) * (1 - inset / np.linalg.norm(dst - c, axis=1, keepdims=True))
    cv2.fillPoly(mask, [shrunk.astype(np.int32)], 255)
    if occluder is not None:
        mask[occluder] = 0
    mask = cv2.GaussianBlur(mask, (0, 0), 1.0).astype(np.float32)[..., None] / 255
    # shading of the blank face: heavy blur of its luminance, normalised to its bright level
    lum = base.mean(-1)
    inside = cv2.fillPoly(np.zeros((S, S), np.uint8), [dst.astype(np.int32)], 1).astype(bool)
    ref = np.percentile(lum[inside], 95)
    shade = cv2.GaussianBlur(lum, (0, 0), blur) / max(ref, 1)
    shade = np.clip(shade, 0.55, 1.03)[..., None]
    printed = warped * shade * 0.97 + base * 0.03
    out = base * (1 - mask) + printed * mask
    return Image.fromarray(np.clip(out, 0, 255).astype(np.uint8))


if __name__ == "__main__":
    for c in ["chalk", "obsidian", "sol"]:
        im = print_on(HERE / "renders" / f"boxblank_{c}_t1.png", HERE / "packaging" / f"retra_box_front_{c}.png",
                      FACES[c])
        im.save(HERE / "renders" / f"boxblank_{c}_printed.png")
        print(c)
