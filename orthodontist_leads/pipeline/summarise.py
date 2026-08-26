"""Per-state and per-metro rollups of the practice lists."""

from __future__ import annotations

import csv
import statistics
from collections import defaultdict
from pathlib import Path


def state_summary(csv_path: Path, out_path: Path) -> int:
    by_state: dict[str, list[dict]] = defaultdict(list)
    with open(csv_path, newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            by_state[row["state"]].append(row)

    rows = []
    for state, recs in sorted(by_state.items()):
        incomes = [int(r["median_household_income"]) for r in recs
                   if r["median_household_income"].strip().isdigit()]
        rows.append({
            "state": state,
            "practices": len(recs),
            "with_phone": sum(1 for r in recs if r["phone"].strip()),
            "with_email": sum(1 for r in recs if r["email"].strip()),
            "all_four_services": sum(1 for r in recs if r["services_covered"] == "4"),
            "counties_covered": len({r["county"] for r in recs if r["county"].strip()}),
            "median_area_income": int(statistics.median(incomes)) if incomes else "",
            "high_income_practices": sum(
                1 for r in recs if r["income_level"] in ("high", "very-high")),
        })

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    return len(rows)
