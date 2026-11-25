"""Hand-back for W48: contact sheet of all 10 masters + CSV (brief section 9) + cost summary.

    python3 finalize.py
"""
import csv
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[4]
FONTS = HERE.parents[1] / "fonts"
COPY = {a["id"]: a for a in json.load(open(HERE / "copy.json"))["ads"]}
PICKS = json.load(open(HERE / "picks.json"))
REPORT = json.load(open(HERE / "work/compose_report.json"))
QA = json.load(open(HERE / "qa.json"))
USD_PER_RENDER = 18 * 0.005  # Nano Banana Pro 2K = 18 Kie credits; $0.005 per credit

usage = [json.loads(l) for l in open(HERE / "renders/_usage.jsonl")]
renders_per_ad = {}
for u in usage:
    renders_per_ad[u["ad"]] = renders_per_ad.get(u["ad"], 0) + 1


def contact_sheet():
    tw, th, pad, lab = 432, 540, 24, 44
    cols, rows = 5, 2
    sheet = Image.new("RGB", (cols * tw + (cols + 1) * pad, rows * (th + lab) + (rows + 1) * pad + 70), (252, 251, 249))
    d = ImageDraw.Draw(sheet)
    title = ImageFont.truetype(str(FONTS / "Tinos-Regular.ttf"), 40)
    small = ImageFont.truetype(str(FONTS / "Inter.ttf"), 18)
    small.set_variation_by_name("SemiBold")
    d.text((pad, 22), "Retra W48 statics: 7 TOF + 3 BOF (1080x1350 masters)", font=title, fill=(2, 43, 73))
    for i, ad in enumerate(sorted(PICKS)):
        r, c = divmod(i, cols)
        x = pad + c * (tw + pad)
        y = 70 + pad + r * (th + lab + pad)
        im = Image.open(HERE / "output" / REPORT[ad]["file"]).convert("RGB").resize((tw, th), Image.LANCZOS)
        sheet.paste(im, (x, y))
        p = PICKS[ad]
        tag = f"{ad} · {p['funnel'].upper()} · {p['angle']} · v{p['v']}" + (" · ILLUSTRATIVE" if p.get("illustrative") else "")
        d.text((x, y + th + 10), tag, font=small, fill=(65, 96, 119))
    out = HERE / "output" / "RET_W48_contact_sheet.jpg"
    sheet.save(out, quality=90)
    return out


def write_csv():
    out = HERE / "output" / "RET_W48_ads.csv"
    total = 0.0
    with open(out, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["ID", "funnel", "angle", "persona", "headline", "subhead", "primary text", "FR headline",
                    "file path", "render cost (USD)", "notes"])
        for ad in sorted(PICKS):
            c, p = COPY[ad], PICKS[ad]
            n = renders_per_ad.get(ad, 0)
            cost = round(n * USD_PER_RENDER, 2)
            total += cost
            path = f"ads/brands/retra/weeks/2026-W48/output/{REPORT[ad]['file']}"
            w.writerow([ad, p["funnel"].upper(), p["angle"], c["persona"], c["headline"], c["subhead"],
                        c["primary_text"], c["fr_headline"], path, f"{cost:.2f}", QA[ad]])
    return out, total


if __name__ == "__main__":
    print(contact_sheet())
    out, total = write_csv()
    print(out, f"render total ${total:.2f}", renders_per_ad)
