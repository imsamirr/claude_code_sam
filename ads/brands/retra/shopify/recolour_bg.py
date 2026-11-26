"""Shift each product image's backdrop to #F2EEE3 (the cream of the front/back gallery image), keeping shadows.

    python3 recolour_bg.py            # all files in media.json -> recoloured/
    python3 recolour_bg.py a.jpg      # just these

Backdrop = pixels whose chromaticity is close to the image's border colour and that are connected to the image
edge; they keep their relative brightness (shadows), only the hue/level moves to the target. Foreground
(camera, hands, text, props) is left alone.
"""
import json
import sys
from pathlib import Path

import cv2
import numpy as np
from PIL import Image

HERE = Path(__file__).resolve().parent
TARGET = np.array([0xF2, 0xEE, 0xE3], np.float32)
GALLERY = HERE.parent / "gallery" / "output"


def source(fn):
    """Gallery images: use the latest local version (packaging update); others: the Shopify original."""
    p = GALLERY / fn
    return p if p.exists() else HERE / "original" / fn


def recolour(path, loose=0.10):
    a = np.asarray(Image.open(path).convert("RGB")).astype(np.float32)
    h, w = a.shape[:2]
    e = max(8, h // 60)
    border = np.concatenate([a[:e].reshape(-1, 3), a[-e:].reshape(-1, 3), a[:, :e].reshape(-1, 3),
                             a[:, -e:].reshape(-1, 3)])
    bg = np.median(border, 0)
    # explain each pixel as a shaded backdrop: p ~ s * bg; residual = what shading can't explain
    s = (a @ bg) / float(bg @ bg)
    resid = np.linalg.norm(a - s[..., None] * bg, axis=-1) / np.maximum(np.linalg.norm(a, axis=-1), 1)
    # hard object outlines block the backdrop region; soft shadows have no hard edges so they are included
    grey = cv2.GaussianBlur(a.mean(-1).astype(np.uint8), (0, 0), 2)
    edges = cv2.Canny(grey, 18, 45)
    edges = cv2.dilate(edges, np.ones((5, 5), np.uint8)).astype(bool)
    cand = (resid < loose) & (s > 0.3) & (s < 1.25) & ~edges
    n, lab = cv2.connectedComponents(cand.astype(np.uint8), connectivity=4)
    edge_labels = set(np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))) - {0}
    region = np.isin(lab, list(edge_labels)).astype(np.uint8)
    region = cv2.morphologyEx(region, cv2.MORPH_CLOSE, np.ones((7, 7), np.uint8))
    # grow back over the thin edge band, but only onto backdrop-coloured pixels
    grow = cv2.dilate(region, np.ones((9, 9), np.uint8)).astype(bool) & (resid < loose) & (s > 0.3)
    region = region.astype(bool) | grow
    wgt = cv2.GaussianBlur(region.astype(np.float32), (0, 0), 1.2)[..., None]
    new = TARGET[None, None, :] * np.clip(s, 0, 1.25)[..., None]
    out = a * (1 - wgt) + new * wgt
    return Image.fromarray(np.clip(out, 0, 255).astype(np.uint8)), bg


def recolour_chroma(path, t1=0.022, t2=0.05):
    """Conservative backdrop mask by chromaticity only (for skin on a skin-coloured backdrop)."""
    a = np.asarray(Image.open(path).convert("RGB")).astype(np.float32)
    h, w = a.shape[:2]
    e = max(8, h // 60)
    border = np.concatenate([a[:e].reshape(-1, 3), a[-e:].reshape(-1, 3), a[:, :e].reshape(-1, 3),
                             a[:, -e:].reshape(-1, 3)])
    bg = np.median(border, 0)
    lum = a.sum(-1)
    chd = np.abs(a / np.maximum(lum[..., None], 1) - bg / bg.sum()).sum(-1)
    ratio = lum / bg.sum()
    tol = t1 + 0.09 * np.clip(1 - ratio, 0, 0.6)
    core = (chd < tol) & (ratio > 0.35) & (ratio < 1.2)
    n, lab = cv2.connectedComponents(core.astype(np.uint8), connectivity=4)
    edge_labels = set(np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))) - {0}
    region = np.isin(lab, list(edge_labels))
    region = cv2.morphologyEx(region.astype(np.uint8), cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8)).astype(bool)
    soft = np.clip((tol + (t2 - t1) - chd) / (t2 - t1), 0, 1)
    near = cv2.dilate(region.astype(np.uint8), np.ones((7, 7), np.uint8)).astype(bool)
    wgt = np.where(region, 1.0, np.where(near, soft, 0.0)).astype(np.float32)
    wgt = cv2.GaussianBlur(wgt, (0, 0), 1.0)[..., None]
    out = a * (1 - wgt) + TARGET[None, None, :] * np.clip(ratio, 0, 1.25)[..., None] * wgt
    return Image.fromarray(np.clip(out, 0, 255).astype(np.uint8)), bg


CHROMA_ONLY = {"retra-g6-hand.jpg"}  # hand skin is almost the backdrop colour: region growing leaks into it


if __name__ == "__main__":
    files = sys.argv[1:] or [fn for _, fn in json.load(open(HERE / "media.json"))]
    (HERE / "recoloured").mkdir(exist_ok=True)
    for fn in files:
        im, bg = (recolour_chroma if fn in CHROMA_ONLY else recolour)(source(fn))
        im.save(HERE / "recoloured" / fn, quality=93)
        print(fn, "from", "#%02X%02X%02X" % tuple(bg.astype(int)))
