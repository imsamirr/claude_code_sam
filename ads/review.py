"""Preview generated ads and record approve/reject feedback.

    python ads/review.py sheet --week 2026-W41            # contact sheets of unreviewed ads
    python ads/review.py sheet --week 2026-W41 W41_03     # only these concepts
    python ads/review.py log W41_03_..._v1 approve "love the clean layout"
    python ads/review.py log W41_05_..._v1 reject  "too much text, shoe looks fake"
    python ads/review.py summary
    python ads/review.py cost --week 2026-W43             # image API spend from output/_usage.jsonl
    python ads/review.py csv --week 2026-W43              # concept list + image links, for the Drive sheet

All commands take --brand (default: comfortwear, or $ADS_BRAND). Sheets show
each 9:16 ad with dashed lines marking the 4:5 safe area; "GIF" marks ads that
also have an animated version. Verdicts live in ads/brands/<brand>/feedback.json.
generate.py reads the notes and adds them to every prompt, so later rounds
follow what was approved and avoid what wasn't.
"""

import argparse
import datetime as dt
import json
import os
import re
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ADS_DIR = Path(__file__).resolve().parent
STATIC = re.compile(r".+_v\d+")


def font(size):
    for name in ("DejaVuSans-Bold.ttf", "Arial Bold.ttf"):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def load_feedback(bdir):
    path = bdir / "feedback.json"
    return json.loads(path.read_text()) if path.exists() else []


def out_dirs(bdir, week):
    if week:
        return [bdir / "weeks" / week / "output"]
    return [bdir / "output"] + sorted(bdir.glob("weeks/*/output"))


def dashed(draw, y, x0, x1, fill):
    for x in range(x0, x1, 14):
        draw.line([(x, y), (min(x + 7, x1), y)], fill=fill, width=2)


def sheet(bdir, week, prefixes):
    reviewed = {f["image"] for f in load_feedback(bdir)}
    out = out_dirs(bdir, week)[0]
    imgs = sorted(p for p in out.glob("*_v*.png")
                  if STATIC.fullmatch(p.stem) and p.stem not in reviewed
                  and (not prefixes or any(p.stem.startswith(x) for x in prefixes)))
    if not imgs:
        sys.exit("No unreviewed images.")
    tw, th, label, cols, per_page = 360, 640, 40, 4, 8
    paths = []
    for page in range(0, len(imgs), per_page):
        batch = imgs[page:page + per_page]
        rows = (len(batch) + cols - 1) // cols
        canvas = Image.new("RGB", (tw * cols, (th + label) * rows), "white")
        draw = ImageDraw.Draw(canvas)
        for i, p in enumerate(batch):
            im = Image.open(p).convert("RGB")
            im = im.resize((tw - 8, int((tw - 8) * im.height / im.width)))
            x, y = (i % cols) * tw, (i // cols) * (th + label)
            name = p.stem + ("  GIF" if (p.parent / f"{p.stem}.gif").exists() else "")
            draw.text((x + 6, y + 6), name[:30], fill="black", font=font(15))
            draw.text((x + 6, y + 22), name[30:60], fill="black", font=font(15))
            canvas.paste(im, (x + 4, y + label))
            safe = int(im.width * 5 / 4)
            top = y + label + (im.height - safe) // 2
            for yy in (top, top + safe):
                dashed(draw, yy, x + 4, x + 4 + im.width, (230, 40, 40))
        path = out / f"_preview_{dt.date.today()}_{page // per_page + 1}.jpg"
        canvas.save(path, quality=88)
        paths.append(path)
    for p in paths:
        print(p.relative_to(ADS_DIR.parent))


def log(bdir, image, verdict, notes):
    if verdict not in ("approve", "reject"):
        sys.exit("verdict must be approve or reject")
    if not any((d / f"{image}.png").exists() for d in out_dirs(bdir, None)):
        sys.exit(f"{image}.png not found under {bdir.relative_to(ADS_DIR.parent)}")
    fb = [f for f in load_feedback(bdir) if f["image"] != image]
    fb.append({"image": image, "concept": image.rsplit("_v", 1)[0], "verdict": verdict,
               "notes": notes, "date": str(dt.date.today())})
    (bdir / "feedback.json").write_text(json.dumps(fb, indent=2, ensure_ascii=False))
    print(f"Logged {verdict} for {image}")


def cost(bdir, week):
    rows = [json.loads(line) for d in out_dirs(bdir, week) if (d / "_usage.jsonl").exists()
            for line in (d / "_usage.jsonl").read_text().splitlines()]
    by = {}
    for r in rows:
        k = (r["kind"], r["quality"])
        n, c = by.get(k, (0, 0.0))
        by[k] = (n + 1, c + r["cost_usd"])
    for (kind, q), (n, c) in sorted(by.items()):
        print(f"{kind:<8} {q:<7} {n:>4} calls  ${c:7.2f}")
    print(f"{'total':<16} {len(rows):>4} calls  ${sum(r['cost_usd'] for r in rows):7.2f}")


def concept_csv(bdir, week, repo_url):
    """CSV of a week's concepts with links to each rendered file, for the weekly Drive sheet."""
    import csv, io
    wdir = bdir / "weeks" / week
    concepts = json.loads((wdir / "concepts.json").read_text())["concepts"]
    verdicts = {f["concept"]: f for f in load_feedback(bdir)}
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(["ID", "Group", "Persona", "Language", "Colorway", "Headline", "Angle", "Based on",
                "GIF candidate", "9:16 image", "4:5 image", "GIF", "Verdict", "Notes"])
    for c in concepts:
        out = wdir / "output"
        stems = sorted(p.stem for p in out.glob(f"{c['id']}_v*.png") if STATIC.fullmatch(p.stem))
        link = lambda name: f"{repo_url}/{(out / name).relative_to(ADS_DIR.parent)}" if (out / name).exists() else ""
        stem = stems[-1] if stems else ""
        fb = verdicts.get(c["id"], {})
        w.writerow([c["id"], c.get("group", ""), c["persona"], c.get("lang", "en"), c.get("colorway", ""),
                    c["headline"], c["angle"], c["based_on"], "yes" if c.get("gif") else "",
                    link(f"{stem}.png"), link(f"{stem}_4x5.png"), link(f"{stem}.gif"),
                    fb.get("verdict", ""), fb.get("notes", "")])
    print(buf.getvalue(), end="")


def summary(bdir):
    for f in load_feedback(bdir):
        print(f"{f['verdict']:<8} {f['image']:<48} {f['notes']}")


if __name__ == "__main__":
    p = argparse.ArgumentParser(usage=__doc__)
    p.add_argument("cmd", choices=["sheet", "log", "summary", "cost", "csv"])
    p.add_argument("--repo-url", default=os.getenv("ADS_REPO_URL",
                   "https://github.com/imsamirr/claude_code_sam/blob/claude/clever-albattani-90x4ya"))
    p.add_argument("rest", nargs="*")
    p.add_argument("--brand", default=os.getenv("ADS_BRAND", "comfortwear"))
    p.add_argument("--week")
    a = p.parse_args()
    bdir = ADS_DIR / "brands" / a.brand
    if a.cmd == "sheet":
        sheet(bdir, a.week, a.rest)
    elif a.cmd == "log" and len(a.rest) >= 2:
        log(bdir, a.rest[0], a.rest[1], " ".join(a.rest[2:]))
    elif a.cmd == "csv":
        concept_csv(bdir, a.week, a.repo_url)
    elif a.cmd == "cost":
        cost(bdir, a.week)
    elif a.cmd == "summary":
        summary(bdir)
    else:
        sys.exit(__doc__)
