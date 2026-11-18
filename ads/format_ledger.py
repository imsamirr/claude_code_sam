"""Format ledger: every static format a brand has used, so each run brings NEW formats (user rule 2026-10-28).

    python ads/format_ledger.py --brand comfortwear list
    python ads/format_ledger.py --brand comfortwear check --week 2026-W45-tue   # before rendering
    python ads/format_ledger.py --brand comfortwear add --week 2026-W45-tue     # after the batch ships

Each concept names its visual format in "format_name" (short slug, e.g. "four_stage_ladder") and the ad it was
discovered from in "format_source" (brand, category, days running). `check` fails when a concept reuses a
format already in research/format_ledger.json or when two concepts in the batch share one. Formats listed in
brand.json -> wellness.proven_layouts (our own $10k+ winning layouts) may repeat; name them "proven:<slug>".
"""

import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

ADS_DIR = Path(__file__).resolve().parent


def slug(s):
    return re.sub(r"[^a-z0-9]+", "_", (s or "").lower()).strip("_")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("cmd", choices=["list", "check", "add"])
    p.add_argument("--brand", default="comfortwear")
    p.add_argument("--week")
    a = p.parse_args()
    bdir = ADS_DIR / "brands" / a.brand
    path = bdir / "research" / "format_ledger.json"
    ledger = json.loads(path.read_text()) if path.exists() else []
    used = {slug(e["format_name"]): e for e in ledger}
    proven = {slug(x) for x in json.loads((bdir / "brand.json").read_text()).get("wellness", {}).get("proven_layouts", [])}
    if a.cmd == "list":
        for e in ledger:
            print(f"{e['format_name']:40} {e['folder']:28} {e.get('format_source', '')}")
        print(f"{len(ledger)} formats used")
        return
    data = json.loads((bdir / "weeks" / a.week / "concepts.json").read_text())
    concepts = data["concepts"] if isinstance(data, dict) else data
    problems, batch = [], {}
    for c in concepts:
        name = c.get("format_name")
        if not name:
            problems.append(f"{c['id']}: no format_name")
            continue
        s = slug(name)
        if s.startswith("proven_"):
            if s[len("proven_"):] not in proven:
                problems.append(f"{c['id']}: {name} is not in wellness.proven_layouts")
            continue
        if s in used and used[s]["folder"] != a.week:
            problems.append(f"{c['id']}: {name} already used in {used[s]['folder']}")
        if s in batch:
            problems.append(f"{c['id']}: {name} also used by {batch[s]} in this batch")
        batch[s] = c["id"]
    if a.cmd == "check":
        print("\n".join(problems) or f"OK: {len(batch)} new formats, {len(concepts) - len(batch)} proven layouts")
        sys.exit(1 if problems else 0)
    added = 0
    for s, cid in batch.items():
        if s not in used:
            c = next(x for x in concepts if x["id"] == cid)
            ledger.append({"format_name": c["format_name"], "folder": a.week, "first_id": cid,
                           "format_source": c.get("format_source", ""), "date": dt.date.today().isoformat()})
            added += 1
    path.write_text(json.dumps(ledger, ensure_ascii=False, indent=1) + "\n")
    print(f"added {added} formats to {path}")


if __name__ == "__main__":
    main()
