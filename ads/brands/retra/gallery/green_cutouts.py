"""Clean camera cut-outs via Kie green-screen copies (fixes ragged edges, tan patches and render smudges).

    python3 green_cutouts.py [names...]   -> renders/green_<name>.png  and  cutouts/<name>.png
names: 34_<colour> (product 3/4 shot), front_<colour> (gallery front render), bottom_<colour> (recoloured bottom view)
"""
import json
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
sys.path.insert(0, str(REPO / "ads"))
import kie  # noqa: E402

PICKS = json.load(open(HERE / "picks.json"))
(HERE / "cutouts").mkdir(exist_ok=True)
FIX = {
    "bottom": " Also make the leatherette panel's edges clean and continuous (no speckles or ragged bits at its left end).",
}


def source(name):
    kind, c = name.split("_", 1)
    if kind == "34":
        return REPO / f"assets/retra/product/retra_{c}_34.jpg"
    p = HERE / "renders" / PICKS[f"{kind}_{c}"]
    return p if p.exists() else p.with_suffix(".jpg")


def green(name):
    out = HERE / "renders" / f"green_{name}.png"
    if not out.exists():
        u = kie.upload(source(name), "retra-gallery")
        prompt = ("Edit this product photo: replace the entire background (including the floor and any shadow on it) with"
                  " a flat, even chroma-key green (#00B140). Keep the camera exactly as it is: same position, size,"
                  " angle, colours, textures, buttons, ports, lenses and gold 'Retra' wordmark. Do not add anything."
                  + FIX.get(name, FIX["bottom"] if name.startswith("bottom") else ""))
        res = "4K" if name.startswith("front") else "2K"
        tid = kie.create("nano-banana-pro", {"prompt": prompt, "image_input": [u], "aspect_ratio": "auto",
                                             "resolution": res, "output_format": "png"})
        r = kie.wait(tid)
        kie.download(r[0], out)
        with open(HERE / "renders" / "_usage.jsonl", "a") as f:
            f.write(json.dumps({"job": f"green_{name}", "try": 1, "task_id": tid, "model": "nano-banana-pro",
                                "resolution": "2K", "prompt": prompt}) + "\n")
    return out


def key(name):
    gimg = Image.open(green(name)).convert("RGB")
    a = np.asarray(gimg).astype(np.float32)
    clean = np.asarray(Image.open(source(name)).convert("RGB").resize(gimg.size, Image.LANCZOS)).astype(np.float32)
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    gness = g - np.maximum(r, b)
    alpha = np.clip(1 - (gness - 20) / 60, 0, 1)  # soft edge: 20..80 of green excess
    solid = alpha > 0.5
    lab, n = ndimage.label(solid)
    keep = lab == (1 + np.argmax(ndimage.sum(solid, lab, range(1, n + 1))))
    keep = ndimage.binary_fill_holes(keep)
    near = ndimage.binary_dilation(keep, iterations=3)
    alpha = np.where(keep, np.maximum(alpha, ndimage.binary_erosion(keep, iterations=2)), np.where(near, alpha, 0))
    if name.startswith("front"):  # Kie sometimes keeps a cream shelf under the camera: cut below the bottom band
        dark = (clean.sum(-1) < 200) & keep
        cols = np.where(keep.any(0))[0]
        rows = np.where(dark.sum(1) > 0.5 * (cols.max() - cols.min()))[0]
        cut = rows.max() + 1
        keep[cut:] = False
        alpha[cut:] = 0
        # clip to the convex hull of the camera's dark frame (body edges, bands, lugs): drops any shelf
        import cv2
        dk = ((clean.sum(-1) < 200) & keep).astype(np.uint8)
        dk = cv2.morphologyEx(dk, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
        pts = cv2.findNonZero(dk)
        hull = np.zeros_like(dk)
        cv2.fillConvexPoly(hull, cv2.convexHull(pts), 1)
        hull = cv2.dilate(hull, np.ones((5, 5), np.uint8)).astype(bool)
        alpha[~hull] = 0
        keep &= hull
    # the green copy only supplies the outline; visible pixels come from the clean (un-tinted) render, except the
    # bottom views, whose only source is an older recolour with ragged panel edges: there the green copy's cleaned
    # pixels are used, with despill and teal removal
    hard = ndimage.binary_erosion(alpha > 0.5, iterations=1)
    hard = ndimage.binary_opening(hard, iterations=4)  # drop specks of floor shadow
    lab, n = ndimage.label(hard)
    hard = lab == (1 + np.argmax(ndimage.sum(hard, lab, range(1, n + 1))))
    alpha = ndimage.binary_fill_holes(hard) * 1.0
    if name.startswith("bottom"):
        a[..., 1] = np.minimum(g, np.maximum(r, b) + 4)
        g2 = a[..., 1]
        teal = (g2 - r > 12) & (b - r > 6) & (np.abs(g2 - b) < 30)
        grey = a[..., :3].mean(-1)
        for ch in range(3):
            a[..., ch] = np.where(teal, grey, a[..., ch])
        lum = a[..., :3].mean(-1)
        dk = np.clip((110 - lum) / 40, 0, 1)[..., None]  # blacks/greys -> neutral (slightly warm, like the fronts)
        neutral = np.stack([lum * 1.03, lum * 0.99, lum * 0.98], -1)
        a[..., :3] = a[..., :3] * (1 - dk) + neutral * dk
        out = Image.fromarray(np.clip(a, 0, 255).astype("uint8"))
    else:
        out = Image.fromarray(np.clip(clean, 0, 255).astype("uint8"))
    m = Image.fromarray((alpha * 255).astype("uint8")).filter(ImageFilter.GaussianBlur(1.0))
    out.putalpha(m)
    out = out.crop(m.getbbox())
    out.save(HERE / "cutouts" / f"{name}.png")
    return name, out.size


if __name__ == "__main__":
    names = sys.argv[1:] or [f"{k}_{c}" for k in ("34", "front", "bottom") for c in ("chalk", "obsidian", "sol")]
    with ThreadPoolExecutor(9) as ex:
        for r in ex.map(key, names):
            print(r, flush=True)
