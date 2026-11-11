"""Story images for long-form statics, generated with Kie.ai (google/nano-banana).

The style copies the long-form winners saved in Atria: an unedited phone snapshot of ONE moment
or object from the story (the bench, the bin, the café chair). No studio look, no ad layout, and
usually no product. Specs live in ads/brands/<brand>/output/longform/images/specs.json:

    {"LF01_A": {"prompt": "...", "size": "4:5", "overlay": null}, ...}

An optional "overlay" draws exact text on top with PIL (for example iMessage bubbles), so text
the story depends on is never left to the image model.

    export KIE_AI=...                     # Kie.ai API key
    python ads/longform_images.py --brand comfortwear            # every spec without an image
    python ads/longform_images.py --brand comfortwear LF03_B     # one image (re-renders it)
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path

import requests
from PIL import Image, ImageDraw, ImageFont

API = "https://api.kie.ai/api/v1/jobs"
STYLE = ("Unedited amateur smartphone photo, the kind a family member snaps and posts to Facebook: "
         "imperfect framing, slightly crooked, ordinary or harsh on-camera lighting, a little digital noise and softness, "
         "real everyday clutter, nothing staged. NOT cinematic, NOT professional, NOT an ad. "
         "No logos, no brand names, no watermarks, no recognizable landmarks or characters. ")


def kie(key, prompt, size):
    h = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
    r = requests.post(f"{API}/createTask", headers=h, timeout=60, json={
        "model": "google/nano-banana",
        "input": {"prompt": STYLE + prompt, "output_format": "png", "image_size": size}}).json()
    if r.get("code") != 200:
        raise RuntimeError(r)
    tid = r["data"]["taskId"]
    for _ in range(60):
        time.sleep(5)
        d = requests.get(f"{API}/recordInfo", headers=h, params={"taskId": tid}, timeout=60).json()["data"]
        if d["state"] == "success":
            return requests.get(json.loads(d["resultJson"])["resultUrls"][0], timeout=120).content
        if d["state"] == "fail":
            raise RuntimeError(d.get("failMsg"))
    raise RuntimeError(f"timed out: {tid}")


def font(size, bold=False):
    for f in (["DejaVuSans-Bold.ttf"] if bold else ["DejaVuSans.ttf"]):
        for d in ("/usr/share/fonts/truetype/dejavu/", ""):
            try:
                return ImageFont.truetype(d + f, size)
            except OSError:
                pass
    return ImageFont.load_default()


def imessage(img, ov):
    """Draw iMessage bubbles: ov = {"bubbles": [{"text": "...", "me": false}, ...], "time": "7:42 PM"}."""
    img = img.convert("RGB")
    W, H = img.size
    d = ImageDraw.Draw(img)
    f = font(int(W * 0.042))
    pad, gap, maxw = int(W * 0.03), int(W * 0.02), int(W * 0.62)
    lines_all = []
    for b in ov["bubbles"]:
        words, lines, cur = b["text"].split(), [], ""
        for w in words:
            t = (cur + " " + w).strip()
            if d.textlength(t, font=f) > maxw - 2 * pad and cur:
                lines.append(cur); cur = w
            else:
                cur = t
        lines.append(cur)
        lines_all.append((b, lines))
    lh = int(f.size * 1.25)
    total = sum(len(l) * lh + 2 * pad + gap for _, l in lines_all) + (lh if ov.get("time") else 0)
    y = H - total - int(H * 0.05)
    if ov.get("time"):
        tf = font(int(W * 0.03))
        d.text(((W - d.textlength(ov["time"], font=tf)) / 2, y), ov["time"], font=tf, fill=(235, 235, 235))
        y += lh
    for b, lines in lines_all:
        bw = max(d.textlength(l, font=f) for l in lines) + 2 * pad
        bh = len(lines) * lh + 2 * pad
        x = W - bw - int(W * 0.04) if b.get("me") else int(W * 0.04)
        fill, color = ((10, 132, 255), "white") if b.get("me") else ((233, 233, 235), "black")
        d.rounded_rectangle([x, y, x + bw, y + bh], radius=int(lh * 0.8), fill=fill)
        for i, l in enumerate(lines):
            d.text((x + pad, y + pad + i * lh), l, font=f, fill=color)
        y += bh + gap
    return img


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--brand", default="comfortwear")
    p.add_argument("ids", nargs="*")
    a = p.parse_args()
    out = Path(__file__).resolve().parent / "brands" / a.brand / "output" / "longform" / "images"
    specs = json.loads((out / "specs.json").read_text())
    key = os.getenv("KIE_AI") or sys.exit("KIE_AI not set")
    for sid, s in specs.items():
        if a.ids and sid not in a.ids:
            continue
        raw, final = out / f"{sid}_raw.png", out / f"{sid}.png"
        if final.exists() and not a.ids:
            continue
        print(f"{sid}: generating…", flush=True)
        raw.write_bytes(kie(key, s["prompt"], s.get("size", "4:5")))
        img = Image.open(raw)
        if s.get("overlay", {}) and s["overlay"].get("type") == "imessage":
            img = imessage(img, s["overlay"])
        img.convert("RGB").save(final)
        print(f"  saved {final}")


if __name__ == "__main__":
    main()
