"""Build today's Slack report from a CSV snapshot + a lookup-results queue file.

Used for one-off / local invocations where the daily job's gspread path is not
available. Inputs:
    --csv       CSV export of the sheet (pre-lookup state, with old statuses)
    --queue     queue JSON produced by lookup_tracking.py (row, shipping_update, days_in_transit)
    --raw       raw-status JSON: [{row, raw_status}] — optional, lets us classify
                Fulfilled But Not Shipped accurately. If absent we fall back to
                the queue's shipping_update field.
    --out-file  write the message body to this file instead of stdout

Reuses the metrics + message builder from daily_tracking_job.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from daily_tracking_job import (  # noqa: E402
    LOOKUP_STATUSES,
    NO_TRACKING_OPEN_SKIP,
    build_message,
    compute_metrics,
)


def read_csv(path: str):
    rows = []
    with open(path, newline="") as f:
        reader = csv.reader(f)
        next(reader)  # header
        for i, row in enumerate(reader, start=2):
            padded = list(row) + [""] * (6 - len(row))
            date, order, tracking, status, days, _ = [c.strip() for c in padded[:6]]
            rows.append({
                "row": i, "date": date, "order": order,
                "tracking": tracking, "status": status, "days": days,
            })
    return rows


def collect_targets(rows):
    targets = []
    no_tracking_open = []
    for r in rows:
        if r["tracking"] and r["status"] in LOOKUP_STATUSES:
            targets.append({
                "row": r["row"], "tracking": r["tracking"],
                "old_status": r["status"], "old_days": r["days"],
                "order": r["order"], "date": r["date"],
            })
        elif not r["tracking"] and r["order"] and r["status"] not in NO_TRACKING_OPEN_SKIP:
            no_tracking_open.append({
                "row": r["row"], "order": r["order"],
                "date": r["date"], "status": r["status"],
            })
    return targets, no_tracking_open


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", required=True)
    ap.add_argument("--queue", required=True)
    ap.add_argument("--raw", default=None,
                    help="JSON [{row, raw_status}, ...] for FBNS classification")
    ap.add_argument("--out-file", default=None)
    args = ap.parse_args()

    rows = read_csv(args.csv)
    targets, no_tracking_open = collect_targets(rows)
    print(f"csv rows: {len(rows)}, lookup targets: {len(targets)}, "
          f"no-tracking open: {len(no_tracking_open)}", file=sys.stderr)

    queue = json.loads(Path(args.queue).read_text())
    queue_by_row = {q["row"]: q for q in queue}

    raw_by_row = {}
    if args.raw:
        for entry in json.loads(Path(args.raw).read_text()):
            raw_by_row[entry["row"]] = entry.get("raw_status", "")

    results = []
    for t in targets:
        q = queue_by_row.get(t["row"])
        new_status = q["shipping_update"] if q else ""
        new_days = q["days_in_transit"] if q else ""
        raw = raw_by_row.get(t["row"], "")
        # Override FBNS if raw status says so (queue may have mapped to In transit)
        if raw and raw.lower().startswith("shipment information received"):
            new_status = "Fulfilled But Not Shipped"
        results.append({
            **t, "new_status": new_status, "new_days": new_days,
            "raw_status": raw, "error": None,
        })

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    metrics = compute_metrics(results, no_tracking_open)
    message = build_message(metrics, today)

    print(json.dumps({
        "lookups": metrics["lookups"],
        "in_transit_total": metrics["in_transit_total"],
        "newly_delivered": len(metrics["newly_delivered"]),
        "avg_delivery_days": metrics["avg_delivery_days"],
        "returned": len(metrics["returned"]),
        "fbns": len(metrics["fbns"]),
        "stuck_10_plus": len(metrics["stuck_10_plus"]),
        "no_tracking_open": len(metrics["no_tracking_open"]),
    }, indent=2), file=sys.stderr)

    if args.out_file:
        Path(args.out_file).write_text(message)
        print(f"wrote {args.out_file}", file=sys.stderr)
    else:
        print(message)


if __name__ == "__main__":
    main()
