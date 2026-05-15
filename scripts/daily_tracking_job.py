"""Daily tracking refresh + Slack report.

Reads the 2026 ORDERS sheet, looks up every non-Delivered row with a
tracking number on yuntrack, writes status updates back to the sheet,
then posts a daily summary to Slack.

Expected env vars (provided by the GitHub Action):
    GOOGLE_SA_JSON    service-account JSON for sheet read/write
    SHEET_ID          target spreadsheet ID
    SHEET_TAB         worksheet/tab name
    SLACK_BOT_TOKEN   xoxb-... bot token
    SLACK_CHANNEL_ID  destination channel ID

Optional:
    LOOKUP_DELAY      seconds between yuntrack calls (default 0.4)
    DRY_RUN=1         skip sheet writes and print the Slack message
"""

from __future__ import annotations

import json
import os
import sys
import time
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import gspread
import requests
from google.oauth2.service_account import Credentials

sys.path.insert(0, str(Path(__file__).resolve().parent))
from yuntrack import lookup_one  # noqa: E402

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
# Statuses that still warrant a fresh lookup each day. Anything not in this
# set (Delivered, Canceled, Returned to sender, Unable to Deliver, Unfulfilled)
# is treated as terminal and skipped to keep manually-curated rows intact.
LOOKUP_STATUSES = {
    "",
    "In transit",
    "Stuck In Transit",
    "Out For Delivery",
    "Ready for Pick Up",
    "Fulfilled But Not Shipped",
}
NO_TRACKING_OPEN_SKIP = {"Delivered", "Canceled", "Unfulfilled"}
STUCK_THRESHOLD_DAYS = 10


def authorize() -> gspread.Client:
    sa_json = os.environ["GOOGLE_SA_JSON"]
    creds = Credentials.from_service_account_info(json.loads(sa_json), scopes=SCOPES)
    return gspread.authorize(creds)


def read_sheet():
    client = authorize()
    sh = client.open_by_key(os.environ["SHEET_ID"]).worksheet(os.environ["SHEET_TAB"])
    return sh, sh.get_all_values()


def collect_targets(values: list[list[str]]):
    """Split sheet rows into lookup targets and no-tracking-open lists."""
    lookup_targets: list[dict[str, Any]] = []
    no_tracking_open: list[dict[str, Any]] = []
    for i, row in enumerate(values[1:], start=2):
        padded = list(row) + [""] * (6 - len(row))
        date, order, tracking, status, days, _notes = [c.strip() for c in padded[:6]]
        if tracking and status in LOOKUP_STATUSES:
            lookup_targets.append({
                "row": i,
                "tracking": tracking,
                "old_status": status,
                "old_days": days,
                "order": order,
                "date": date,
            })
        elif not tracking and status not in NO_TRACKING_OPEN_SKIP:
            no_tracking_open.append({
                "row": i,
                "order": order,
                "date": date,
                "status": status,
            })
    return lookup_targets, no_tracking_open


def do_lookups(targets, delay: float):
    session = requests.Session()
    results = []
    for i, t in enumerate(targets):
        r = lookup_one(t["tracking"], session)
        results.append({
            **t,
            "new_status": r.shipping_update,
            "new_days": r.days_in_transit,
            "raw_status": r.raw_status,
            "error": r.error,
        })
        if (i + 1) % 100 == 0:
            print(f"  progress {i+1}/{len(targets)}", flush=True)
        if i < len(targets) - 1:
            time.sleep(delay)
    return results


def write_sheet_updates(sh, results, chunk_size: int = 1000) -> int:
    batch = []
    for r in results:
        if r.get("new_status") and (
            r["new_status"] != r["old_status"] or r["new_days"] != r["old_days"]
        ):
            batch.append({
                "range": f"D{r['row']}:E{r['row']}",
                "values": [[r["new_status"], r["new_days"]]],
            })
    for i in range(0, len(batch), chunk_size):
        sh.batch_update(batch[i:i + chunk_size], value_input_option="USER_ENTERED")
    return len(batch)


def parse_days(s: str) -> int:
    if not s:
        return 0
    try:
        return int(s.lower().replace("days", "").replace("day", "").strip().split()[0])
    except (ValueError, IndexError):
        return 0


def compute_metrics(results, no_tracking_open):
    newly_delivered = [
        r for r in results
        if r["old_status"] != "Delivered" and r["new_status"] == "Delivered"
    ]
    returned = [r for r in results if r["new_status"] == "Returned to sender"]
    fbns = [r for r in results if r["new_status"] == "Fulfilled But Not Shipped"]
    in_transit = [
        r for r in results
        if r["new_status"] in {"In transit", "Stuck In Transit"}
    ]
    stuck_10_plus = [
        r for r in in_transit if parse_days(r["new_days"]) > STUCK_THRESHOLD_DAYS
    ]
    avg_delivery_days = None
    if newly_delivered:
        dd = [parse_days(r["new_days"]) for r in newly_delivered]
        dd = [d for d in dd if d > 0]
        if dd:
            avg_delivery_days = sum(dd) / len(dd)
    return {
        "lookups": len(results),
        "in_transit_total": len(in_transit),
        "newly_delivered": newly_delivered,
        "avg_delivery_days": avg_delivery_days,
        "returned": returned,
        "fbns": fbns,
        "stuck_10_plus": stuck_10_plus,
        "no_tracking_open": no_tracking_open,
    }


def fmt_rows(rows, max_items=20, fields=("order", "date", "tracking")) -> str:
    if not rows:
        return "_none_"
    lines = []
    for r in rows[:max_items]:
        parts = [str(r.get(f, "")) for f in fields if r.get(f)]
        lines.append("• " + " | ".join(parts))
    if len(rows) > max_items:
        lines.append(f"_… and {len(rows) - max_items} more_")
    return "\n".join(lines)


def build_message(metrics, today: str) -> str:
    m = metrics
    avg = (
        f"{m['avg_delivery_days']:.1f} days"
        if m["avg_delivery_days"] is not None
        else "n/a (no new deliveries today)"
    )

    parts = [f"*Daily Tracking Update — {today}*", ""]
    parts.append(f"*In Transit:* {m['in_transit_total']} orders")
    parts.append(
        f"*Newly Delivered:* {len(m['newly_delivered'])} orders   "
        f"·   *Avg Delivery Time:* {avg}"
    )
    parts.append("")

    if m["stuck_10_plus"]:
        parts.append(
            f":rotating_light: *In Transit > {STUCK_THRESHOLD_DAYS} days* "
            f"({len(m['stuck_10_plus'])} orders)"
        )
        parts.append(fmt_rows(
            m["stuck_10_plus"],
            max_items=25,
            fields=("order", "date", "new_days", "tracking"),
        ))
        parts.append("")

    parts.append(f"*Returned to sender* ({len(m['returned'])} orders)")
    parts.append(fmt_rows(m["returned"]))
    parts.append("")

    parts.append(
        f"*Fulfilled But Not Shipped* "
        f"({len(m['fbns'])} orders — tracking event still \"Shipment information received\")"
    )
    parts.append(fmt_rows(m["fbns"]))
    parts.append("")

    parts.append(
        f"*No Tracking Numbers* "
        f"({len(m['no_tracking_open'])} open orders without a tracking number)"
    )
    parts.append(fmt_rows(m["no_tracking_open"], fields=("order", "date", "status")))

    return "\n".join(parts)


def post_slack(message: str) -> None:
    token = os.environ.get("SLACK_BOT_TOKEN")
    channel = os.environ.get("SLACK_CHANNEL_ID")
    if not token or not channel:
        print("SLACK_BOT_TOKEN / SLACK_CHANNEL_ID not set; printing message only:\n")
        print(message)
        return
    # Slack caps a single text block at ~40k chars. The report can grow long
    # if there are many stuck orders, so chunk by paragraph just in case.
    chunks = []
    cur = ""
    for line in message.split("\n"):
        if len(cur) + len(line) + 1 > 3500:
            chunks.append(cur.rstrip())
            cur = ""
        cur += line + "\n"
    if cur.strip():
        chunks.append(cur.rstrip())

    parent_ts = None
    for i, chunk in enumerate(chunks):
        body = {"channel": channel, "text": chunk, "mrkdwn": True}
        if parent_ts:
            body["thread_ts"] = parent_ts
        r = requests.post(
            "https://slack.com/api/chat.postMessage",
            headers={
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json; charset=utf-8",
            },
            json=body,
            timeout=20,
        )
        data = r.json()
        if not data.get("ok"):
            raise RuntimeError(f"Slack post failed (chunk {i}): {data}")
        if i == 0:
            parent_ts = data["ts"]
    print(f"Posted to Slack channel {channel}: {len(chunks)} message(s)")


def main():
    dry_run = os.environ.get("DRY_RUN") == "1"
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    print(f"Daily tracking job — {today} (dry_run={dry_run})")

    sh, values = read_sheet()
    print(f"sheet rows: {len(values)}")

    targets, no_tracking_open = collect_targets(values)
    print(f"lookup targets: {len(targets)} | no-tracking open: {len(no_tracking_open)}")
    print("by old_status:", dict(Counter(t["old_status"] for t in targets)))

    delay = float(os.environ.get("LOOKUP_DELAY", "0.4"))
    results = do_lookups(targets, delay)
    print(f"lookups complete: {sum(1 for r in results if not r['error'])} ok, "
          f"{sum(1 for r in results if r['error'])} errors")

    if not dry_run:
        n_updates = write_sheet_updates(sh, results)
        print(f"applied {n_updates} sheet updates")
    else:
        print("DRY_RUN=1, skipping sheet writes")

    metrics = compute_metrics(results, no_tracking_open)
    message = build_message(metrics, today)
    post_slack(message)


if __name__ == "__main__":
    main()
