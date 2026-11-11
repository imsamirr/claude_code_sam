"""Story images for long-form statics, generated with Kie.ai (nano-banana-pro), finished as 4:5 iPhone-style JPEGs.

The style copies the long-form winners saved in Atria: an unedited phone snapshot of ONE moment
or object from the story (the bench, the bin, the café chair). No studio look, no ad layout, and
usually no product. Specs live in ads/brands/<brand>/output/longform/images/specs.json:

    {"LF01_A": {"prompt": "...", "size": "3:4", "overlay": null}, ...}

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
STYLE = ("A real, unremarkable snapshot straight from a regular person's phone camera roll. The image is the photo only, edge to edge, "
         "with no captions, timestamps, camera labels, borders or interface of any kind. Native iPhone camera look: "
         "everything in focus front to back (small phone sensor, NO shallow depth of field, NO bokeh), flat HDR processing with slightly "
         "lifted shadows, a bit over-sharpened, mild JPEG compression, some noise in dark areas, white balance slightly off from the room "
         "lighting, handheld and a little crooked, subject not perfectly centered, ordinary cluttered real-life surroundings. Not a "
         "professional photo, not cinematic, no color grading, no dramatic lighting, no film look, no studio, not an ad, no text overlays, "
         "no app interface, no borders. No logos, brand names, watermarks, recognizable landmarks or characters. ")
MODEL = "nano-banana-pro"      # most photo-real on Kie.ai in a side-by-side test (2026-11-11)
FEED = (1080, 1350)            # 4:5 feed size; renders are 3:4 and centre-cropped to this


def kie(key, prompt, size):
    h = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
    r = requests.post(f"{API}/createTask", headers=h, timeout=60, json={
        "model": MODEL,
        "input": {"prompt": STYLE + prompt, "aspect_ratio": size, "resolution": "1K"}}).json()
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


def phone_finish(img):
    """Centre-crop a 3:4 render to 4:5 and resize to 1080x1350, like a feed upload."""
    img = img.convert("RGB")
    w, h = img.size
    th = int(w * FEED[1] / FEED[0])
    if th < h:
        top = (h - th) // 2
        img = img.crop((0, top, w, top + th))
    return img.resize(FEED, Image.LANCZOS)


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
        raw, final = out / f"{sid}_raw.png", out / f"{sid}.jpg"
        if final.exists() and not a.ids:
            continue
        print(f"{sid}: generating…", flush=True)
        raw.write_bytes(kie(key, s["prompt"], s.get("size", "3:4")))
        img = phone_finish(Image.open(raw))
        if s.get("overlay", {}) and s["overlay"].get("type") == "imessage":
            img = imessage(img, s["overlay"])
        final = final.with_suffix(".jpg")
        img.convert("RGB").save(final, quality=84)  # re-compressed like a phone photo uploaded to Facebook
        print(f"  saved {final}")


if __name__ == "__main__":
    main()
