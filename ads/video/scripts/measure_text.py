"""Measure on-screen text in a full-res frame: grabs frame at time T, finds rows dominated by text-colored pixels in a y-band.
    python ads/video/scripts/measure_text.py <video> <t_seconds> [--y0 0 --y1 1920] [--color white|black|yellow|red|any]
Prints frame size, detected text line bands (y start-end, height px = ~cap+descender height), and saves a crop png next to /tmp path printed."""
import argparse, io, subprocess
import numpy as np
from PIL import Image
ap = argparse.ArgumentParser(); ap.add_argument("video"); ap.add_argument("t", type=float)
ap.add_argument("--y0", type=int, default=0); ap.add_argument("--y1", type=int, default=99999); ap.add_argument("--color", default="white")
ap.add_argument("--save", default="/tmp/claude-0/measure_crop.png"); a = ap.parse_args()
b = subprocess.run(["ffmpeg", "-v", "quiet", "-ss", str(a.t), "-i", a.video, "-frames:v", "1", "-f", "image2pipe", "-vcodec", "png", "-"], capture_output=True).stdout
im = Image.open(io.BytesIO(b)).convert("RGB"); W, H = im.size
im = im.resize((1080, round(H * 1080 / W))) if W != 1080 else im; W, H = im.size
y1 = min(a.y1, H); px = np.asarray(im).astype(int)[a.y0:y1]
r, g, bl = px[..., 0], px[..., 1], px[..., 2]
m = {"white": (r > 225) & (g > 225) & (bl > 225), "black": (r < 35) & (g < 35) & (bl < 35),
     "yellow": (r > 200) & (g > 180) & (bl < 90), "red": (r > 180) & (g < 80) & (bl < 80)}.get(a.color)
rows = m.mean(axis=1) if m is not None else None
print(f"frame normalized to {W}x{H} (orig scaled); band y={a.y0}-{y1}")
if rows is not None:
    on = rows > 0.02; bands = []; s = None
    for i, v in enumerate(on):
        if v and s is None: s = i
        if not v and s is not None:
            if i - s >= 6: bands.append((s + a.y0, i + a.y0))
            s = None
    if s is not None: bands.append((s + a.y0, len(on) + a.y0))
    for s, e in bands:
        cols = np.where(m[s - a.y0:e - a.y0].any(axis=0))[0]
        print(f"  text band y={s}-{e} height={e - s}px  x={cols.min()}-{cols.max()} width={cols.max() - cols.min()}px  ({100 * s / H:.0f}%-{100 * e / H:.0f}% from top)")
im.crop((0, a.y0, W, y1)).save(a.save); print("crop saved:", a.save)
