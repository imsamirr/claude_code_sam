"""
Main script — Fetches daily metrics from TripleWhale and writes them to Google Sheets.

Usage:
    # Pull yesterday's data (default)
    python src/main.py

    # Pull data for a specific date
    python src/main.py --date 2026-01-15

    # Pull data for a date range (backfill)
    python src/main.py --from 2026-01-01 --to 2026-02-25

    # Save to CSV instead of Google Sheets (for environments where Sheets API is blocked)
    python src/main.py --from 2026-01-01 --to 2026-02-25 --csv output.csv

    # Run in scheduled mode (runs daily at a set time)
    python src/main.py --schedule 08:00
"""

import os
import sys
import csv
import argparse
from datetime import datetime, timedelta
from dotenv import load_dotenv

# Add the project root to the path so imports work when running from any directory
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.triplewhale import TripleWhaleClient
from src.sheets import SheetsClient, COLUMN_HEADERS, build_row


def load_config():
    """Load configuration from .env file."""
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    env_path = os.path.join(project_root, ".env")
    load_dotenv(env_path)

    required_vars = [
        "TRIPLEWHALE_API_KEY",
        "SHOPIFY_STORE_URL",
    ]

    missing = [v for v in required_vars if not os.getenv(v)]
    if missing:
        print("ERROR: Missing required environment variables:")
        for var in missing:
            print(f"  - {var}")
        sys.exit(1)

    creds_path = os.getenv("GOOGLE_CREDENTIALS_PATH", "")
    if creds_path and not os.path.isabs(creds_path):
        creds_path = os.path.join(project_root, creds_path)

    return {
        "triplewhale_api_key": os.getenv("TRIPLEWHALE_API_KEY"),
        "shopify_store_url": os.getenv("SHOPIFY_STORE_URL"),
        "google_credentials_path": creds_path,
        "google_sheet_id": os.getenv("GOOGLE_SHEET_ID", ""),
        "google_sheet_tab": os.getenv("GOOGLE_SHEET_TAB_NAME", "Daily Metrics"),
    }


def fetch_date_range(config, start_date, end_date):
    """Fetch metrics for a range of dates and compute calculated fields."""
    tw_client = TripleWhaleClient(config["triplewhale_api_key"], config["shopify_store_url"])

    all_data = []
    current = start_date
    total_days = (end_date - start_date).days + 1

    while current <= end_date:
        date_str = current.strftime("%Y-%m-%d")
        day_num = (current - start_date).days + 1
        print(f"[{day_num}/{total_days}] Fetching {date_str}...")

        data = tw_client.get_daily_metrics(date_str)
        all_data.append(data)

        current += timedelta(days=1)

    # Post-process: calculate fields that depend on other days
    _calculate_growth_fields(all_data)

    return all_data


def _calculate_growth_fields(all_data):
    """Calculate day-over-day and week-over-week fields."""
    # Build lookup by date for weekly calculations
    date_lookup = {d["date"]: d for d in all_data}

    for i, data in enumerate(all_data):
        # New Customer Growth (since yesterday)
        if i > 0:
            prev = all_data[i - 1]
            prev_nc = prev.get("new_customers_count", 0) or 0
            curr_nc = data.get("new_customers_count", 0) or 0
            if prev_nc > 0:
                growth = round((curr_nc - prev_nc) / prev_nc * 100, 2)
                data["new_customer_growth"] = growth
            else:
                data["new_customer_growth"] = ""

        # Weekly spend increases (compare to 7 days ago)
        current_date = datetime.strptime(data["date"], "%Y-%m-%d")
        week_ago_str = (current_date - timedelta(days=7)).strftime("%Y-%m-%d")

        if week_ago_str in date_lookup:
            prev_week = date_lookup[week_ago_str]
            # Google
            prev_g = prev_week.get("google_spend", 0) or 0
            curr_g = data.get("google_spend", 0) or 0
            if prev_g > 0:
                data["weekly_google_spend_increase"] = round((curr_g - prev_g) / prev_g * 100, 2)
            else:
                data["weekly_google_spend_increase"] = ""
            # Facebook
            prev_f = prev_week.get("facebook_spend", 0) or 0
            curr_f = data.get("facebook_spend", 0) or 0
            if prev_f > 0:
                data["weekly_facebook_spend_increase"] = round((curr_f - prev_f) / prev_f * 100, 2)
            else:
                data["weekly_facebook_spend_increase"] = ""


def save_to_csv(all_data, csv_path):
    """Save all data to a CSV file."""
    with open(csv_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(COLUMN_HEADERS)
        for data in all_data:
            writer.writerow(build_row(data))
    print(f"\nSaved {len(all_data)} rows to {csv_path}")


def save_to_sheets(config, all_data):
    """Write all data to Google Sheets."""
    if not config["google_credentials_path"] or not config["google_sheet_id"]:
        print("ERROR: Google Sheets credentials not configured. Use --csv to save locally.")
        return

    sheets_client = SheetsClient(
        config["google_credentials_path"],
        config["google_sheet_id"],
        config["google_sheet_tab"],
    )
    sheets_client.write_batch(all_data)
    print(f"\nWrote {len(all_data)} rows to Google Sheets.")


def fetch_and_write_single(config, date_str, csv_path=None):
    """Fetch metrics for a single date."""
    print(f"\n{'='*50}")
    print(f"Processing date: {date_str}")
    print(f"{'='*50}")

    tw_client = TripleWhaleClient(config["triplewhale_api_key"], config["shopify_store_url"])
    data = tw_client.get_daily_metrics(date_str)

    print(f"  Gross Sales: ${data['gross_sales']}")
    print(f"  Orders: {data['orders']}")
    print(f"  Ad Spend: ${data['google_spend'] + data['facebook_spend'] + data['tiktok_spend'] + data['applovin_spend']}")
    print(f"  MER: {data['mer']}%")

    if csv_path:
        save_to_csv([data], csv_path)
    else:
        save_to_sheets(config, [data])

    print(f"Done for {date_str}!")


def run_scheduled(config, time_str):
    """Run the fetch job on a daily schedule."""
    import schedule
    import time

    def job():
        yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
        try:
            fetch_and_write_single(config, yesterday)
        except Exception as e:
            print(f"[ERROR] Job failed: {e}")

    schedule.every().day.at(time_str).do(job)
    print(f"Scheduler started. Will run daily at {time_str}.")
    print("Press Ctrl+C to stop.\n")

    while True:
        schedule.run_pending()
        time.sleep(60)


def main():
    parser = argparse.ArgumentParser(
        description="Pull daily financial metrics from TripleWhale into Google Sheets"
    )
    parser.add_argument("--date", help="Fetch data for a specific date (YYYY-MM-DD).")
    parser.add_argument("--from", dest="from_date", help="Start date for backfill (YYYY-MM-DD).")
    parser.add_argument("--to", dest="to_date", help="End date for backfill (YYYY-MM-DD).")
    parser.add_argument("--csv", help="Save to CSV file instead of Google Sheets.")
    parser.add_argument("--schedule", help="Run daily at this time (HH:MM, 24h).")

    args = parser.parse_args()
    config = load_config()

    if args.schedule:
        run_scheduled(config, args.schedule)
    elif args.from_date:
        start = datetime.strptime(args.from_date, "%Y-%m-%d")
        end_str = args.to_date or (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
        end = datetime.strptime(end_str, "%Y-%m-%d")

        print(f"Backfill: {args.from_date} to {end_str} ({(end - start).days + 1} days)")
        all_data = fetch_date_range(config, start, end)

        if args.csv:
            save_to_csv(all_data, args.csv)
        else:
            save_to_sheets(config, all_data)

        print(f"\nBackfill complete!")
    else:
        date_str = args.date or (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
        fetch_and_write_single(config, date_str, args.csv)


if __name__ == "__main__":
    main()
