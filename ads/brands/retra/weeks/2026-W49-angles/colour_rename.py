"""Store renamed the colours (Shopify, checked 2026-11-27) and added a 7th:
Chalk->White, Obsidian->Midnight, Sol->Yellow, Dune->Brown, Pine->Green Forest, Blossom->Red, new: Blue (alt 'Aegean').
Fact swap only (names + colour count) across the copy files and the concepts CSV. python3 colour_rename.py"""
import csv
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
SUBS = [
    ("Chalk, Obsidian, Sol, Dune, Pine, and Blossom", "White, Midnight, Yellow, Brown, Green Forest, Blue, and Red"),
    ("Chalk, Obsidian, Sol, Dune, Pine, or Blossom", "White, Midnight, Yellow, Brown, Green Forest, Blue, or Red"),
    ("including Blossom, Sol, and Dune", "including Red, Yellow, and Brown"),
    ("All 6 colours", "All 7 colours"),
    ("stock on all six is", "stock on all seven is"),
]
SIX = re.compile(r"\b([Ss])ix (curated |classic |timeless |gorgeous )?(colou?r(?:s|ways))\b")
OLD = re.compile(r"\b(Chalk|Obsidian|Dune|Blossom)\b|\bSol\b(?! )|\bPine\b")


def fix(t):
    for a, b in SUBS:
        t = t.replace(a, b)
    t = SIX.sub(lambda m: ("S" if m.group(1) == "S" else "s") + "even " + (m.group(2) or "") + m.group(3), t)
    return t


def walk(o):
    if isinstance(o, dict):
        return {k: (v if k in ("format", "id", "angle") else walk(v)) for k, v in o.items()}
    if isinstance(o, list):
        return [walk(v) for v in o]
    return fix(o) if isinstance(o, str) else o


if __name__ == "__main__":
    for f in ["copy.json", "copy_b2.json", "copy_klik.json", "copy_pain.json", "copy_disney.json"]:
        p = HERE / f
        d = json.load(open(p))
        json.dump(walk(d), open(p, "w"), indent=1, ensure_ascii=False)
    p = HERE / "output/RET_A49_concepts.csv"
    rows = list(csv.DictReader(open(p)))
    fields = list(rows[0].keys())
    for r in rows:
        for k in ("on_image_text", "meta_headline", "primary_text"):
            r[k] = fix(r[k])
    with open(p, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)
    left = [(r["id"], m.group(0)) for r in rows for k in ("on_image_text", "meta_headline", "primary_text")
            for m in OLD.finditer(r[k])]
    print("old names left:", left)
