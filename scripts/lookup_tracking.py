"""Look up a batch of tracking numbers and write a queue file for the GitHub Action.

Input: a JSON file with [{"row": 1610, "tracking": "YT..."}, ...]
Output: tracking-updates/queue/<timestamp>.json with the resolved statuses

Usage:
    python scripts/lookup_tracking.py input.json [--limit N] [--delay 1.0]
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path

from yuntrack import lookup_one
import requests

QUEUE_DIR = Path("tracking-updates/queue")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input", help="JSON file with [{row, tracking}, ...]")
    ap.add_argument("--limit", type=int, default=None, help="Cap the number of lookups (useful for trials)")
    ap.add_argument("--delay", type=float, default=1.0, help="Seconds between requests")
    ap.add_argument("--out", type=str, default=None, help="Override output filename")
    args = ap.parse_args()

    items = json.loads(Path(args.input).read_text())
    if args.limit:
        items = items[: args.limit]

    session = requests.Session()
    updates = []
    errors = []

    for i, item in enumerate(items):
        row = item["row"]
        tracking = item.get("tracking", "").strip()
        if not tracking:
            errors.append({"row": row, "error": "empty tracking number"})
            continue

        result = lookup_one(tracking, session)
        print(f"[{i+1}/{len(items)}] row={row} {tracking} -> {result.shipping_update!r} {result.days_in_transit!r} err={result.error}")

        if result.error:
            errors.append({"row": row, "tracking": tracking, "error": result.error})
            continue

        if result.shipping_update:
            updates.append(result.to_update(row))

        if i < len(items) - 1:
            import time
            time.sleep(args.delay)

    QUEUE_DIR.mkdir(parents=True, exist_ok=True)
    stamp = dt.datetime.utcnow().strftime("%Y-%m-%dT%H-%M-%S")
    out_name = args.out or f"{stamp}.json"
    out_path = QUEUE_DIR / out_name
    out_path.write_text(json.dumps(updates, indent=2))

    print(f"\nWrote {len(updates)} updates to {out_path}")
    if errors:
        err_path = QUEUE_DIR.parent / f"errors-{stamp}.json"
        err_path.write_text(json.dumps(errors, indent=2))
        print(f"Wrote {len(errors)} errors to {err_path}")


if __name__ == "__main__":
    main()
