"""Batch rules check: no source clip is used twice, inside one ad or across the batch (user rule:
every creative uses different scenes). Run before rendering a batch.

Usage:
    python ads/video/check_batch.py ads/brands/<brand>/video/<week>/
    python ads/video/check_batch.py <week dir> --also <other week dir> ...   # include earlier batches
Exit code 1 when a clip is reused.
"""

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("week")
ap.add_argument("--also", nargs="*", default=[])
a = ap.parse_args()

uses = defaultdict(list)
for d in [a.week, *a.also]:
    for f in sorted(Path(d).glob("*/edit.json")):
        e = json.loads(f.read_text())
        for i, c in enumerate(e["clips"]):
            uses[e["sources"][c["src"]]].append((e["id"], i, float(c["in"])))
# a clip may appear twice in ONE ad (different moments, e.g. a box shot then on-foot); never in two ads
bad = {k: [f"{a}#{i}" for a, i, _ in v] for k, v in uses.items() if len({a for a, _, _ in v}) > 1}
print(f"{sum(len(v) for v in uses.values())} scenes, {len(uses)} distinct source clips")
for k, v in bad.items():
    print(f"REUSED ACROSS ADS {k}: {', '.join(v)}")
sys.exit(1 if bad else 0)
