"""Apply queued tracking updates to the Google Sheet.

Reads every JSON file in tracking-updates/queue/, batch-updates the sheet,
then moves processed files to tracking-updates/applied/.

Each queue file is a JSON array of update objects:
  [
    {"row": 1610, "shipping_update": "Returned to sender", "days_in_transit": "52 Days"},
    {"row": 2109, "shipping_update": "In transit", "days_in_transit": "60 Days", "notes": "..."}
  ]

Required env: GOOGLE_SA_JSON (service account JSON string), SHEET_ID, SHEET_TAB.
"""

import json
import os
import shutil
import sys
from pathlib import Path

import gspread
from google.oauth2.service_account import Credentials

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
QUEUE_DIR = Path("tracking-updates/queue")
APPLIED_DIR = Path("tracking-updates/applied")


def authorize():
    sa_json = os.environ.get("GOOGLE_SA_JSON")
    if not sa_json:
        sys.exit("GOOGLE_SA_JSON env var is missing")
    info = json.loads(sa_json)
    creds = Credentials.from_service_account_info(info, scopes=SCOPES)
    return gspread.authorize(creds)


def build_batch(updates):
    batch = []
    for u in updates:
        row = u["row"]
        status = u.get("shipping_update", "")
        days = u.get("days_in_transit", "")
        if "notes" in u:
            batch.append({"range": f"D{row}:F{row}", "values": [[status, days, u["notes"]]]})
        else:
            batch.append({"range": f"D{row}:E{row}", "values": [[status, days]]})
    return batch


def main():
    if not QUEUE_DIR.exists():
        print(f"No queue dir at {QUEUE_DIR}; nothing to do.")
        return

    queue_files = sorted(QUEUE_DIR.glob("*.json"))
    if not queue_files:
        print("Queue is empty; nothing to do.")
        return

    client = authorize()
    sheet_id = os.environ["SHEET_ID"]
    tab_name = os.environ["SHEET_TAB"]
    worksheet = client.open_by_key(sheet_id).worksheet(tab_name)

    APPLIED_DIR.mkdir(parents=True, exist_ok=True)

    total = 0
    for f in queue_files:
        updates = json.loads(f.read_text())
        if not updates:
            print(f"{f.name}: empty, skipping move-only")
            shutil.move(str(f), str(APPLIED_DIR / f.name))
            continue

        batch = build_batch(updates)
        worksheet.batch_update(batch, value_input_option="USER_ENTERED")
        print(f"{f.name}: applied {len(updates)} row updates")
        total += len(updates)

        shutil.move(str(f), str(APPLIED_DIR / f.name))

    print(f"Done. {total} row updates applied across {len(queue_files)} file(s).")


if __name__ == "__main__":
    main()
