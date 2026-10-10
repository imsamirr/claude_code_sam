"""Preview generated ads and record approve/reject feedback.

    python ads/review.py sheet                 # contact sheet of images not yet reviewed
    python ads/review.py sheet C01 C04         # only these concepts
    python ads/review.py log C01_v2 approve "love the clean layout"
    python ads/review.py log C05_v1 reject  "too much text, shoe looks fake"
    python ads/review.py summary               # verdicts so far

Verdicts live in ads/feedback.json. generate.py reads the notes and adds them
to every prompt, so later rounds follow what was approved and avoid what wasn't.
"""

import datetime as dt
import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ADS_DIR = Path(__file__).resolve().parent
OUT_DIR = ADS_DIR / "output"
FEEDBACK = ADS_DIR / "feedback.json"


def load_feedback():
    return json.loads(FEEDBACK.read_text()) if FEEDBACK.exists() else []


def font(size):
    for name in ("DejaVuSans-Bold.ttf", "Arial Bold.ttf"):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def sheet(prefixes):
    reviewed = {f["image"] for f in load_feedback()}
    imgs = sorted(p for p in OUT_DIR.glob("C*_v*.png")
                  if p.stem not in reviewed and (not prefixes or any(p.stem.startswith(x) for x in prefixes)))
    if not imgs:
        sys.exit("No unreviewed images.")
    tile, label, cols = 512, 44, 3
    paths = []
    for page in range(0, len(imgs), 9):
        batch = imgs[page:page + 9]
        rows = (len(batch) + cols - 1) // cols
        canvas = Image.new("RGB", (tile * cols, (tile + label) * rows), "white")
        draw = ImageDraw.Draw(canvas)
        for i, p in enumerate(batch):
            im = Image.open(p).convert("RGB")
            im.thumbnail((tile - 8, tile - 8))
            x, y = (i % cols) * tile, (i // cols) * (tile + label)
            draw.text((x + 8, y + 8), p.stem, fill="black", font=font(26))
            canvas.paste(im, (x + 4, y + label))
        path = OUT_DIR / f"_preview_{dt.date.today()}_{page // 9 + 1}.jpg"
        canvas.save(path, quality=88)
        paths.append(path)
    for p in paths:
        print(p.relative_to(ADS_DIR.parent))


def log(image, verdict, notes):
    if verdict not in ("approve", "reject"):
        sys.exit("verdict must be approve or reject")
    if not (OUT_DIR / f"{image}.png").exists():
        sys.exit(f"ads/output/{image}.png not found")
    fb = [f for f in load_feedback() if f["image"] != image]
    fb.append({"image": image, "concept": image.rsplit("_v", 1)[0], "verdict": verdict,
               "notes": notes, "date": str(dt.date.today())})
    FEEDBACK.write_text(json.dumps(fb, indent=2))
    print(f"Logged {verdict} for {image}")


def summary():
    for f in load_feedback():
        print(f"{f['verdict']:<8} {f['image']:<40} {f['notes']}")


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    cmd, rest = args[0], args[1:]
    if cmd == "sheet":
        sheet(rest)
    elif cmd == "log" and len(rest) >= 2:
        log(rest[0], rest[1], " ".join(rest[2:]))
    elif cmd == "summary":
        summary()
    else:
        sys.exit(__doc__)
