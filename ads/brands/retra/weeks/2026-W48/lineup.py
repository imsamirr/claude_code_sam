"""Build the product-lineup bases for ads 09 and 10 from the real product cutouts (pixel-exact cameras).

    python3 lineup.py   ->  renders/09_base.png, renders/10_base.png, renders/10_positions.json
"""
import json
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[4]
CUT = REPO / "assets/retra/product/cutout"
OUT = HERE / "renders"
W, H = 1856, 2304
CREAM = (243, 238, 228)
ORDER = ["chalk", "obsidian", "blossom", "sol", "pine"]


def background(seed=7):
    rng = np.random.default_rng(seed)
    y, x = np.mgrid[0:H, 0:W]
    # soft seamless-paper falloff: lighter top, slightly warmer/darker toward the bottom and corners
    v = 1 - 0.05 * (y / H) - 0.04 * (((x - W / 2) / (W / 2)) ** 2)
    base = np.array(CREAM, float)[None, None, :] * v[..., None]
    base += rng.normal(0, 2.2, (H, W, 1))  # mild grain
    return Image.fromarray(np.clip(base, 0, 255).astype("uint8"))


def shadow_for(cam, blur=28, opacity=0.38, squash=0.10):
    """Contact + soft ground shadow from the camera's alpha footprint."""
    a = cam.getchannel("A")
    w, h = cam.size
    sh = a.resize((w, max(1, int(h * squash))))
    canvas = Image.new("L", (w + 4 * blur, int(h * squash) + 4 * blur), 0)
    canvas.paste(sh, (2 * blur, 2 * blur))
    canvas = canvas.filter(ImageFilter.GaussianBlur(blur)).point(lambda p: int(p * opacity))
    return canvas


def place(bg, cam, x, y):
    """Paste camera with its bottom-centre at (x, y) and a ground shadow beneath."""
    w, h = cam.size
    sh = shadow_for(cam)
    dark = Image.new("RGB", sh.size, (120, 100, 80))
    bg.paste(dark, (int(x - sh.width / 2), int(y - sh.height / 2 - 6)), sh)
    bg.paste(cam, (int(x - w / 2), int(y - h)), cam)
    return (int(x - w / 2), int(y - h), int(x + w / 2), int(y))


def load(colour, width):
    im = Image.open(CUT / f"retra_{colour}_34.png").convert("RGBA")
    return im.resize((width, int(im.height * width / im.width)), Image.LANCZOS)


def lineup_09():
    bg = background(9)
    # slightly diagonal row, back-left to front-right, small perspective growth; drawn back to front
    n = len(ORDER)
    for i, c in enumerate(ORDER):
        t = i / (n - 1)
        width = int(470 + 70 * t)
        x = 290 + t * (W - 600)
        y = 1330 + t * 420
        place(bg, load(c, width), x, y)
    bg.save(OUT / "09_base.png")


def lineup_10():
    bg = background(10)
    n = len(ORDER)
    margin, gap = 40, 14
    width = int((W - 2 * margin - gap * (n - 1)) / n)
    boxes = {}
    y = 1500
    for i, c in enumerate(ORDER):
        x = margin + width / 2 + i * (width + gap)
        boxes[c] = place(bg, load(c, width), x, y)
    bg.save(OUT / "10_base.png")
    json.dump({"canvas": [W, H], "boxes": boxes, "order": ORDER}, open(OUT / "10_positions.json", "w"), indent=1)


if __name__ == "__main__":
    lineup_09()
    lineup_10()
    print("ok")
