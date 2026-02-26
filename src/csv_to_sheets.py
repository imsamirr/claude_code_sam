"""
Push a CSV file to Google Sheets.

Usage:
    python src/csv_to_sheets.py data/2026_metrics.csv
"""

import csv
import sys
import os
from dotenv import load_dotenv

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def main():
    if len(sys.argv) < 2:
        print("Usage: python src/csv_to_sheets.py <csv_file>")
        sys.exit(1)

    csv_path = sys.argv[1]
    if not os.path.exists(csv_path):
        print(f"File not found: {csv_path}")
        sys.exit(1)

    # Load config
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    load_dotenv(os.path.join(project_root, ".env"))

    creds_path = os.getenv("GOOGLE_CREDENTIALS_PATH", "")
    if not os.path.isabs(creds_path):
        creds_path = os.path.join(project_root, creds_path)

    sheet_id = os.getenv("GOOGLE_SHEET_ID")
    tab_name = os.getenv("GOOGLE_SHEET_TAB_NAME", "Daily Metrics")

    if not sheet_id:
        print("ERROR: GOOGLE_SHEET_ID not set in .env")
        sys.exit(1)

    # Read CSV
    with open(csv_path) as f:
        reader = csv.reader(f)
        headers = next(reader)
        rows = list(reader)

    print(f"Read {len(rows)} rows from {csv_path}")

    # Write to Google Sheets
    import gspread
    from google.oauth2.service_account import Credentials

    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive",
    ]
    creds = Credentials.from_service_account_file(creds_path, scopes=scopes)
    client = gspread.authorize(creds)
    spreadsheet = client.open_by_key(sheet_id)

    try:
        worksheet = spreadsheet.worksheet(tab_name)
    except Exception:
        worksheet = spreadsheet.add_worksheet(title=tab_name, rows=1000, cols=len(headers) + 5)

    # Write headers
    worksheet.update("A1", [headers])

    # Convert column count to letter
    def col_letter(n):
        result = ""
        while n > 0:
            n, r = divmod(n - 1, 26)
            result = chr(65 + r) + result
        return result

    last_col = col_letter(len(headers))

    # Format header row
    worksheet.format(f"A1:{last_col}1", {
        "textFormat": {"bold": True},
        "backgroundColor": {"red": 0.9, "green": 0.9, "blue": 0.95},
    })

    # Write all data rows at once
    if rows:
        cell_range = f"A2:{last_col}{len(rows) + 1}"
        worksheet.update(cell_range, rows, value_input_option="USER_ENTERED")

    print(f"Wrote {len(rows)} rows to Google Sheets tab '{tab_name}'")
    print("Done!")


if __name__ == "__main__":
    main()
