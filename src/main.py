"""
Main script — Fetches daily metrics from TripleWhale + Shopify and writes them to Google Sheets.

Usage:
    # Pull yesterday's data (default)
    python src/main.py

    # Pull data for a specific date
    python src/main.py --date 2025-01-15

    # Pull data for a date range (backfill)
    python src/main.py --from 2025-01-01 --to 2025-01-31

    # Run in scheduled mode (runs daily at a set time)
    python src/main.py --schedule 08:00
"""

import os
import sys
import argparse
from datetime import datetime, timedelta
from dotenv import load_dotenv

# Add the project root to the path so imports work when running from any directory
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.triplewhale import TripleWhaleClient
from src.shopify_client import ShopifyClient
from src.sheets import SheetsClient


def load_config():
    """Load configuration from .env file."""
    # Look for .env in the project root
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    env_path = os.path.join(project_root, ".env")
    load_dotenv(env_path)

    required_vars = [
        "TRIPLEWHALE_API_KEY",
        "SHOPIFY_STORE_URL",
        "SHOPIFY_ACCESS_TOKEN",
        "GOOGLE_CREDENTIALS_PATH",
        "GOOGLE_SHEET_ID",
    ]

    missing = [v for v in required_vars if not os.getenv(v)]
    if missing:
        print("ERROR: Missing required environment variables:")
        for var in missing:
            print(f"  - {var}")
        print("\nPlease copy .env.example to .env and fill in your values.")
        print("See SETUP_GUIDE.md for step-by-step instructions.")
        sys.exit(1)

    # Resolve credentials path relative to project root
    creds_path = os.getenv("GOOGLE_CREDENTIALS_PATH")
    if not os.path.isabs(creds_path):
        creds_path = os.path.join(project_root, creds_path)

    return {
        "triplewhale_api_key": os.getenv("TRIPLEWHALE_API_KEY"),
        "shopify_store_url": os.getenv("SHOPIFY_STORE_URL"),
        "shopify_access_token": os.getenv("SHOPIFY_ACCESS_TOKEN"),
        "google_credentials_path": creds_path,
        "google_sheet_id": os.getenv("GOOGLE_SHEET_ID"),
        "google_sheet_tab": os.getenv("GOOGLE_SHEET_TAB_NAME", "Daily Metrics"),
    }


def fetch_and_write(config, date_str):
    """Fetch metrics for a single date and write to Google Sheets."""
    print(f"\n{'='*50}")
    print(f"Processing date: {date_str}")
    print(f"{'='*50}")

    # 1. Fetch from TripleWhale
    print("[1/3] Fetching TripleWhale metrics...")
    tw_client = TripleWhaleClient(config["triplewhale_api_key"], config["shopify_store_url"])
    tw_data = tw_client.get_daily_metrics(date_str)
    print(f"  Ad Spend: ${tw_data['tw_total_ad_spend']}")
    print(f"  Blended ROAS: {tw_data['tw_blended_roas']}")
    print(f"  Blended CPA: ${tw_data['tw_blended_cpa']}")

    # 2. Fetch from Shopify
    print("[2/3] Fetching Shopify metrics...")
    shopify_client = ShopifyClient(config["shopify_store_url"], config["shopify_access_token"])
    shopify_data = shopify_client.get_daily_metrics(date_str)
    print(f"  Gross Sales: ${shopify_data['shopify_gross_sales']}")
    print(f"  Total Sales: ${shopify_data['shopify_total_sales']}")
    print(f"  Total Orders: {shopify_data['shopify_total_orders']}")

    # 3. Write to Google Sheets
    print("[3/3] Writing to Google Sheets...")
    sheets_client = SheetsClient(
        config["google_credentials_path"],
        config["google_sheet_id"],
        config["google_sheet_tab"],
    )
    sheets_client.write_daily_row(shopify_data, tw_data)

    print(f"Done for {date_str}!")


def run_scheduled(config, time_str):
    """Run the fetch job on a daily schedule."""
    import schedule
    import time

    def job():
        yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
        try:
            fetch_and_write(config, yesterday)
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
        description="Pull daily financial metrics from TripleWhale & Shopify into Google Sheets"
    )
    parser.add_argument(
        "--date",
        help="Fetch data for a specific date (YYYY-MM-DD). Default: yesterday.",
    )
    parser.add_argument(
        "--from", dest="from_date",
        help="Start date for a backfill range (YYYY-MM-DD).",
    )
    parser.add_argument(
        "--to", dest="to_date",
        help="End date for a backfill range (YYYY-MM-DD). Default: yesterday.",
    )
    parser.add_argument(
        "--schedule",
        help="Run on a daily schedule at the given time (HH:MM, 24h format). Example: 08:00",
    )

    args = parser.parse_args()
    config = load_config()

    if args.schedule:
        run_scheduled(config, args.schedule)
    elif args.from_date:
        # Backfill mode: process a range of dates
        start = datetime.strptime(args.from_date, "%Y-%m-%d")
        end_str = args.to_date or (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
        end = datetime.strptime(end_str, "%Y-%m-%d")

        current = start
        while current <= end:
            date_str = current.strftime("%Y-%m-%d")
            try:
                fetch_and_write(config, date_str)
            except Exception as e:
                print(f"[ERROR] Failed for {date_str}: {e}")
            current += timedelta(days=1)

        print(f"\nBackfill complete: {args.from_date} to {end_str}")
    else:
        # Single date mode
        date_str = args.date or (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
        fetch_and_write(config, date_str)


if __name__ == "__main__":
    main()
