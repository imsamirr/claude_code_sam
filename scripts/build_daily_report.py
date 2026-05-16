"""Build today's Slack report from a CSV snapshot.

Two modes, picked by which inputs you pass:

* **--queue (post-lookup)**: classic one-off / dry-run path. You give it
  the pre-lookup sheet CSV plus a queue JSON produced by lookup_tracking.py,
  and it derives "newly delivered today" from the old-status → new-status
  diff. Useful when iterating on the report from outside the GitHub Action.

* **--from-sheet (post-only)**: derive the report from the sheet's
  *current* state alone, no queue file needed. Counts a row as newly
  delivered if status == "Delivered" and Last Update == today — which is
  exactly the rows the daily workflow just flipped to Delivered, since
  already-Delivered rows are skipped by LOOKUP_STATUSES and their
  Last Update column stays frozen at the original delivery date. This is
  the path the daily Slack-post trigger uses: workflow refreshes the
  sheet at 13:00 UTC, trigger reads the updated sheet at 14:00 UTC and
  posts. No yuntrack calls needed in this mode.

Inputs:
    --csv       CSV export of the sheet (always required)
    --queue     queue JSON from lookup_tracking.py — picks --queue mode
    --raw       raw-status JSON for FBNS classification (optional, --queue mode only)
    --from-sheet  use sheet's current state for metrics — picks post-only mode
    --out-file  write the message body to this file instead of stdout
    --csv-out   also write the action-lists CSV here

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
    build_lists_csv,
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
            date, order, tracking, status, days, last_update = [c.strip() for c in padded[:6]]
            rows.append({
                "row": i, "date": date, "order": order,
                "tracking": tracking, "status": status, "days": days,
                "last_update": last_update,
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


def build_results_from_sheet(rows, today):
    """Synthesize a results list from the sheet's current state.

    For each row in a lookup-eligible status (or already Delivered), emit
    a result whose new_status / new_days come straight from the sheet.

    "Newly delivered today" detection: if status == "Delivered" and the
    Last Update column equals today's date, the row was just flipped to
    Delivered by today's workflow run (terminal rows are skipped by
    LOOKUP_STATUSES, so their Last Update never gets re-stamped). For
    those rows we set old_status = "" so the existing compute_metrics
    diff picks them up.
    """
    results = []
    for r in rows:
        status = r["status"]
        is_newly_delivered = (status == "Delivered" and r["last_update"] == today)
        # Only emit a result for rows that were lookup-eligible (so the
        # in_transit total and stuck buckets are consistent with the daily
        # job's view) or for newly-delivered rows (so the metric counts).
        if not (status in LOOKUP_STATUSES or is_newly_delivered):
            continue
        results.append({
            "row": r["row"], "tracking": r["tracking"],
            "order": r["order"], "date": r["date"],
            "old_status": "" if is_newly_delivered else status,
            "old_days": "",
            "new_status": status, "new_days": r["days"],
            "raw_status": "",
            "error": None,
        })
    return results


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", required=True)
    ap.add_argument("--queue", default=None,
                    help="Queue JSON from lookup_tracking.py (selects --queue mode)")
    ap.add_argument("--raw", default=None,
                    help="JSON [{row, raw_status}, ...] for FBNS classification (--queue mode only)")
    ap.add_argument("--from-sheet", action="store_true",
                    help="Build the report from the sheet's current state, no queue file")
    ap.add_argument("--out-file", default=None)
    ap.add_argument("--csv-out", default=None, help="Also write the action-lists CSV here")
    args = ap.parse_args()

    if not args.queue and not args.from_sheet:
        ap.error("pass either --queue <queue.json> or --from-sheet")
    if args.queue and args.from_sheet:
        ap.error("--queue and --from-sheet are mutually exclusive")

    rows = read_csv(args.csv)
    targets, no_tracking_open = collect_targets(rows)
    print(f"csv rows: {len(rows)}, lookup targets: {len(targets)}, "
          f"no-tracking open: {len(no_tracking_open)}", file=sys.stderr)

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    if args.from_sheet:
        results = build_results_from_sheet(rows, today)
        print(f"from-sheet results: {len(results)}", file=sys.stderr)
    else:
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
            if raw and raw.lower().startswith("shipment information received"):
                new_status = "Fulfilled But Not Shipped"
            results.append({
                **t, "new_status": new_status, "new_days": new_days,
                "raw_status": raw, "error": None,
            })
    metrics = compute_metrics(results, no_tracking_open)
    message = build_message(metrics, today)

    print(json.dumps({
        "lookups": metrics["lookups"],
        "in_transit_total": metrics["in_transit_total"],
        "newly_delivered": len(metrics["newly_delivered"]),
        "avg_delivery_days": metrics["avg_delivery_days"],
        "returned": len(metrics["returned"]),
        "fbns": len(metrics["fbns"]),
        "stuck_in_customs": len(metrics["stuck_in_customs"]),
        "stuck_10_plus": len(metrics["stuck_10_plus"]),
        "no_tracking_open": len(metrics["no_tracking_open"]),
    }, indent=2), file=sys.stderr)

    if args.out_file:
        Path(args.out_file).write_text(message)
        print(f"wrote {args.out_file}", file=sys.stderr)
    else:
        print(message)

    if args.csv_out:
        Path(args.csv_out).write_text(build_lists_csv(metrics))
        print(f"wrote {args.csv_out}", file=sys.stderr)


if __name__ == "__main__":
    main()
