"""Batch rules check (user rule: scenes NEVER repeat): no source clip is used by two different ads,
inside this batch or against any earlier batch of the brand. (One ad may cut two moments of the
same clip, e.g. a shoe box then on-foot.)

Usage:
    python ads/video/check_batch.py ads/brands/<brand>/video/<week>/            # this week + all history
    python ads/video/check_batch.py <week dir> --no-history                       # this week only
    python ads/video/check_batch.py --used ads/brands/<brand>/video               # list every used clip
Exit code 1 when a clip is reused.
"""

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path


def uses_in(dirs):
    uses = defaultdict(list)
    for d in dirs:
        for f in sorted(Path(d).glob("*/edit.json")):
            e = json.loads(f.read_text())
            for i, c in enumerate(e["clips"]):
                uses[e["sources"][c["src"]]].append((e["id"], i, f.parent.parent.name))
    return uses


ap = argparse.ArgumentParser()
ap.add_argument("week", nargs="?")
ap.add_argument("--no-history", action="store_true")
ap.add_argument("--used", help="brand video dir: print every clip used so far")
a = ap.parse_args()
if a.used:
    root = Path(a.used)
    u = uses_in([p for p in root.iterdir() if p.is_dir() and any(p.glob("*/edit.json"))])
    for k, v in sorted(u.items()):
        print(f"{k}\t{', '.join(sorted({x[0] for x in v}))}")
    print(f"{len(u)} clips used", file=sys.stderr)
    sys.exit(0)
week = Path(a.week)
weeks = [week] if a.no_history else [p for p in week.parent.iterdir() if p.is_dir() and any(p.glob("*/edit.json"))]
uses = uses_in(weeks)
bad = {}
for k, v in uses.items():
    ads = {x[0] for x in v}
    if len(ads) > 1 and any(x[2] == week.name for x in v):
        bad[k] = sorted(ads)
here = sum(1 for v in uses.values() for x in v if x[2] == week.name)
print(f"{week.name}: {here} scenes; checked against {len(weeks) - 1} earlier batch folder(s)")
for k, v in bad.items():
    print(f"REUSED {k}: {', '.join(v)}")
sys.exit(1 if bad else 0)
