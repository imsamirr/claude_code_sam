"""Contact sheets of ad thumbnails from an Atria CSV, for eyeballing what competitors and winners look like.

    python ads/contact_sheet.py --brand dentalpulse competitor_ads.csv --by brand --per 6
    python ads/contact_sheet.py --brand dentalpulse current_winners.csv --per 20
    python ads/contact_sheet.py --brand dentalpulse inspiration_raw.csv --by query --per 3

Reads ads/brands/<brand>/research/data/<csv>, picks the longest-running (or highest-spend) rows per group,
skips duplicate headlines, and writes 20-tile JPG pages to research/sheets/ (prints the paths; Read them).
"""

import argparse
import csv
import io
import os
from pathlib import Path

import requests
from PIL import Image, ImageDraw

ADS_DIR = Path(__file__).resolve().parent


def pick(rows, by, per):
    def rank(r):  # best first: impression percentile (lower = more impressions), else days running / spend
        if r.get("impression_percentile") not in (None, ""):
            return float(r["impression_percentile"])
        return -float(r.get("days_running") or r.get("spend") or 0)
    groups = {}
    for r in rows:
        if r.get("image_url") or r.get("thumbnail_url"):
            groups.setdefault(r.get(by, "") if by else "", []).append(r)
    out = []
    for g in groups.values():
        seen = set()
        for r in sorted(g, key=rank):
            key = (r.get("title") or r.get("headline") or r.get("ad_name") or "")[:40]
            if key in seen:
                continue
            seen.add(key)
            out.append(r)
            if len(seen) >= per:
                break
    return out


def tile(r, by):
    url = r.get("image_url") or r.get("thumbnail_url")
    im = Image.open(io.BytesIO(requests.get(url, timeout=30).content)).convert("RGB")
    im.thumbnail((300, 380))
    t = Image.new("RGB", (300, 410), "white")
    t.paste(im, (0, 30))
    label = " ".join(str(x) for x in (r.get(by, "") if by else "", r.get("format", "")[:1],
                                      f"top {float(r['impression_percentile'])*100:.1f}%" if r.get("impression_percentile") not in (None, "") else "",
                                      f"{r['days_running']}d" if r.get("days_running") else "",
                                      f"${float(r['spend']):,.0f}" if r.get("spend") else "",
                                      f"ROAS {r['roas']}" if r.get("roas") else "") if x)
    ImageDraw.Draw(t).text((4, 4), label[:48], fill="black")
    return t


def main():
    p = argparse.ArgumentParser()
    p.add_argument("csv")
    p.add_argument("--brand", default=os.getenv("ADS_BRAND", "comfortwear"))
    p.add_argument("--by", default="", help="column to group by, e.g. brand or query")
    p.add_argument("--per", type=int, default=6, help="tiles per group")
    a = p.parse_args()
    bdir = ADS_DIR / "brands" / a.brand / "research"
    rows = list(csv.DictReader(open(bdir / "data" / a.csv)))
    tiles = []
    for r in pick(rows, a.by, a.per):
        try:
            tiles.append(tile(r, a.by))
        except Exception as e:  # expired CDN links are common; skip them
            print(f"  skip: {e}")
    out = bdir / "sheets"
    out.mkdir(exist_ok=True)
    for i in range(0, len(tiles), 20):
        page = Image.new("RGB", (1500, 1640), "white")
        for k, t in enumerate(tiles[i:i + 20]):
            page.paste(t, ((k % 5) * 300, (k // 5) * 410))
        path = out / f"{Path(a.csv).stem}_{i // 20 + 1}.jpg"
        page.save(path, quality=80)
        print(path.relative_to(ADS_DIR.parent))


if __name__ == "__main__":
    main()
