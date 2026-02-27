"""
Power BI data export pipeline.

Pulls data from TripleWhale (platform-level KPIs) and Meta Ads (creative-level),
structures it into analytics-ready CSV files for Power BI import.

Usage:
    # Export TripleWhale platform data only
    python src/powerbi_export.py --from 2026-01-01 --to 2026-02-26

    # Export with Meta Ads creative data
    python src/powerbi_export.py --from 2026-01-01 --to 2026-02-26 --meta

    # Custom output directory
    python src/powerbi_export.py --from 2026-01-01 --to 2026-02-26 --output data/powerbi

Output files (for Power BI import):
    data/powerbi/daily_kpis.csv           - Blended daily KPIs
    data/powerbi/platform_daily.csv       - Per-platform daily metrics
    data/powerbi/creative_performance.csv - Ad-level creative data (Meta Ads)
    data/powerbi/creative_summary.csv     - Creative aggregate analysis
    data/powerbi/dim_date.csv             - Date dimension table
"""

import os
import sys
import csv
import argparse
from datetime import datetime, timedelta
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv
from src.triplewhale import TripleWhaleClient


PLATFORMS = [
    "google", "facebook", "tiktok", "snapchat",
    "pinterest", "taboola", "applovin",
]


def load_config():
    """Load configuration from .env file."""
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    load_dotenv(os.path.join(project_root, ".env"))

    return {
        "triplewhale_api_key": os.getenv("TRIPLEWHALE_API_KEY"),
        "shopify_store_url": os.getenv("SHOPIFY_STORE_URL"),
        "meta_access_token": os.getenv("META_ACCESS_TOKEN", ""),
        "meta_ad_account_id": os.getenv("META_AD_ACCOUNT_ID", ""),
    }


def fetch_triplewhale_data(config, start_date, end_date):
    """Fetch TripleWhale data for a date range with retry logic."""
    import time as _time
    tw = TripleWhaleClient(config["triplewhale_api_key"], config["shopify_store_url"])

    all_data = []
    current = start_date
    total_days = (end_date - start_date).days + 1

    while current <= end_date:
        date_str = current.strftime("%Y-%m-%d")
        day_num = (current - start_date).days + 1
        print(f"[{day_num}/{total_days}] Fetching {date_str}...")

        data = None
        for attempt in range(4):
            try:
                data = tw.get_daily_metrics(date_str)
                break
            except Exception as e:
                wait = 2 ** (attempt + 1)
                print(f"  Retry {attempt+1}/3 after {wait}s ({e.__class__.__name__})")
                _time.sleep(wait)

        if data is None:
            print(f"  [!] Failed after retries, using empty metrics for {date_str}")
            data = tw._empty_metrics(date_str)

        all_data.append(data)
        current += timedelta(days=1)
        _time.sleep(0.3)  # gentle rate limiting

    return all_data


def build_daily_kpis(all_data):
    """Build the blended daily KPIs fact table."""
    rows = []
    for d in all_data:
        total_spend = sum(d.get(f"{p}_spend", 0) or 0 for p in PLATFORMS)
        gross = d.get("gross_sales", 0) or 0
        blended_roas = round(gross / total_spend, 2) if total_spend > 0 else 0

        rows.append({
            "date": d["date"],
            "gross_sales": d.get("gross_sales", 0),
            "net_revenue": d.get("net_revenue", 0),
            "refunds": d.get("refunds", 0),
            "cogs": d.get("cogs", 0),
            "margin": d.get("margin", 0),
            "gross_margin_pct": d.get("gross_margin_pct", 0),
            "orders": d.get("orders", 0),
            "aov": d.get("aov", 0),
            "total_ad_spend": round(total_spend, 2),
            "mer": d.get("mer", 0),
            "amer": d.get("amer", 0),
            "blended_roas": blended_roas,
            "cac": d.get("cac", 0),
            "ncac": d.get("ncac", 0),
            "sessions": d.get("sessions", 0),
            "cvr": d.get("cvr", 0),
            "atc_pct": d.get("atc_pct", 0),
            "ic_pct": d.get("ic_pct", 0),
            "users": d.get("users", 0),
            "customers": d.get("customers", 0),
            "new_customer_orders": d.get("new_customer_orders", 0),
            "new_customer_pct": d.get("new_customer_pct", 0),
            "new_customers_revenue": d.get("new_customers_revenue", 0),
            "returning_customers_count": d.get("returning_customers_count", 0),
            "returning_customers_revenue": d.get("returning_customers_revenue", 0),
            "cltv": d.get("cltv", 0),
        })
    return rows


def build_platform_daily(all_data):
    """Build per-platform daily metrics (unpivoted for Power BI)."""
    rows = []
    for d in all_data:
        for platform in PLATFORMS:
            spend = d.get(f"{platform}_spend", 0) or 0
            # Skip platforms with zero spend for the day
            if spend == 0:
                continue

            rows.append({
                "date": d["date"],
                "platform": platform.title(),
                "spend": round(spend, 2),
                "roas": d.get(f"{platform}_roas", 0) or 0,
                "cpc": d.get(f"{platform}_cpc", 0) or 0,
                "clicks": d.get(f"{platform}_clicks", 0) or 0,
                "cpm": d.get(f"{platform}_cpm", 0) or 0,
                "ctr": d.get(f"{platform}_ctr", 0) or 0,
                "cpa": d.get(f"{platform}_cpa", 0) or 0,
            })
    return rows


def build_creative_summary(creative_data):
    """
    Aggregate creative data by ad to build the creative analysis:
    - Total spend per creative
    - Which creatives hit $1K spend threshold
    - Win rate analysis
    """
    # Aggregate by ad_id
    ad_agg = defaultdict(lambda: {
        "ad_name": "",
        "adset_name": "",
        "campaign_name": "",
        "objective": "",
        "total_spend": 0,
        "total_impressions": 0,
        "total_clicks": 0,
        "total_purchases": 0,
        "total_purchase_value": 0,
        "total_reach": 0,
        "first_date": "9999-12-31",
        "last_date": "0000-01-01",
        "days_active": set(),
    })

    for row in creative_data:
        ad_id = row["ad_id"]
        agg = ad_agg[ad_id]
        agg["ad_name"] = row["ad_name"]
        agg["adset_name"] = row["adset_name"]
        agg["campaign_name"] = row["campaign_name"]
        agg["objective"] = row["objective"]
        agg["total_spend"] += row["spend"]
        agg["total_impressions"] += row["impressions"]
        agg["total_clicks"] += row["clicks"]
        agg["total_purchases"] += row["purchases"]
        agg["total_purchase_value"] += row["purchase_value"]
        agg["total_reach"] += row["reach"]
        agg["days_active"].add(row["date"])
        if row["date"] < agg["first_date"]:
            agg["first_date"] = row["date"]
        if row["date"] > agg["last_date"]:
            agg["last_date"] = row["date"]

    # Build summary rows
    rows = []
    for ad_id, agg in ad_agg.items():
        spend = round(agg["total_spend"], 2)
        impr = agg["total_impressions"]
        clicks = agg["total_clicks"]
        purchases = agg["total_purchases"]
        revenue = round(agg["total_purchase_value"], 2)
        days = len(agg["days_active"])

        rows.append({
            "ad_id": ad_id,
            "ad_name": agg["ad_name"],
            "adset_name": agg["adset_name"],
            "campaign_name": agg["campaign_name"],
            "objective": agg["objective"],
            "total_spend": spend,
            "total_impressions": impr,
            "total_clicks": clicks,
            "total_purchases": purchases,
            "total_revenue": revenue,
            "total_reach": agg["total_reach"],
            "avg_cpc": round(spend / clicks, 2) if clicks > 0 else 0,
            "avg_cpm": round(spend / impr * 1000, 2) if impr > 0 else 0,
            "avg_ctr": round(clicks / impr * 100, 2) if impr > 0 else 0,
            "cpa": round(spend / purchases, 2) if purchases > 0 else 0,
            "roas": round(revenue / spend, 2) if spend > 0 else 0,
            "days_active": days,
            "first_active": agg["first_date"],
            "last_active": agg["last_date"],
            "avg_daily_spend": round(spend / days, 2) if days > 0 else 0,
            "hit_1k_spend": "Yes" if spend >= 1000 else "No",
            "hit_500_spend": "Yes" if spend >= 500 else "No",
            "hit_5k_spend": "Yes" if spend >= 5000 else "No",
            "hit_10k_spend": "Yes" if spend >= 10000 else "No",
            "spend_tier": _spend_tier(spend),
        })

    # Sort by total spend descending
    rows.sort(key=lambda x: x["total_spend"], reverse=True)
    return rows


def _spend_tier(spend):
    """Classify creative into spend tiers for Power BI slicing."""
    if spend >= 10000:
        return "$10K+"
    elif spend >= 5000:
        return "$5K-$10K"
    elif spend >= 1000:
        return "$1K-$5K"
    elif spend >= 500:
        return "$500-$1K"
    elif spend >= 100:
        return "$100-$500"
    else:
        return "Under $100"


def build_dim_date(start_date, end_date):
    """Build a date dimension table for Power BI."""
    rows = []
    current = start_date
    while current <= end_date:
        rows.append({
            "date": current.strftime("%Y-%m-%d"),
            "day_of_week": current.strftime("%A"),
            "day_of_week_num": current.isoweekday(),
            "week_num": current.isocalendar()[1],
            "month": current.strftime("%B"),
            "month_num": current.month,
            "quarter": f"Q{(current.month - 1) // 3 + 1}",
            "year": current.year,
            "year_month": current.strftime("%Y-%m"),
            "year_week": f"{current.isocalendar()[0]}-W{current.isocalendar()[1]:02d}",
            "is_weekend": 1 if current.isoweekday() >= 6 else 0,
        })
        current += timedelta(days=1)
    return rows


def write_csv(rows, filepath, fieldnames=None):
    """Write list of dicts to CSV."""
    if not rows:
        print(f"  Skipped {filepath} (no data)")
        return

    if fieldnames is None:
        fieldnames = list(rows[0].keys())

    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"  Wrote {len(rows)} rows to {filepath}")


def main():
    parser = argparse.ArgumentParser(description="Export data for Power BI")
    parser.add_argument("--from", dest="from_date", required=True, help="Start date (YYYY-MM-DD)")
    parser.add_argument("--to", dest="to_date", required=True, help="End date (YYYY-MM-DD)")
    parser.add_argument("--meta", action="store_true", help="Include Meta Ads creative data")
    parser.add_argument("--output", default="data/powerbi", help="Output directory")
    args = parser.parse_args()

    config = load_config()
    start = datetime.strptime(args.from_date, "%Y-%m-%d")
    end = datetime.strptime(args.to_date, "%Y-%m-%d")
    out_dir = args.output

    print(f"\n{'='*60}")
    print(f"Power BI Data Export: {args.from_date} to {args.to_date}")
    print(f"Output: {out_dir}/")
    print(f"{'='*60}\n")

    # --- TripleWhale data ---
    print("[1/4] Fetching TripleWhale platform data...")
    tw_data = fetch_triplewhale_data(config, start, end)

    print("\n[2/4] Building Power BI tables...")
    daily_kpis = build_daily_kpis(tw_data)
    platform_daily = build_platform_daily(tw_data)
    dim_date = build_dim_date(start, end)

    write_csv(daily_kpis, os.path.join(out_dir, "daily_kpis.csv"))
    write_csv(platform_daily, os.path.join(out_dir, "platform_daily.csv"))
    write_csv(dim_date, os.path.join(out_dir, "dim_date.csv"))

    # --- Meta Ads creative data ---
    if args.meta:
        if not config["meta_access_token"] or not config["meta_ad_account_id"]:
            print("\n[!] Meta Ads credentials not found in .env. Skipping creative data.")
            print("    Add META_ACCESS_TOKEN and META_AD_ACCOUNT_ID to .env")
        else:
            print("\n[3/4] Fetching Meta Ads creative data...")
            from src.meta_ads import MetaAdsClient
            meta = MetaAdsClient(config["meta_access_token"], config["meta_ad_account_id"])

            # Test connection first
            try:
                meta.test_connection()
            except Exception as e:
                print(f"  [!] Meta connection failed: {e}")
                print("      Check your META_ACCESS_TOKEN and META_AD_ACCOUNT_ID")
                return

            creative_data = meta.get_creative_performance_chunked(
                args.from_date, args.to_date
            )

            print("\n[4/4] Building creative analysis...")
            creative_summary = build_creative_summary(creative_data)

            write_csv(creative_data, os.path.join(out_dir, "creative_performance.csv"))
            write_csv(creative_summary, os.path.join(out_dir, "creative_summary.csv"))

            # Print creative analysis summary
            total_creatives = len(creative_summary)
            hit_1k = sum(1 for c in creative_summary if c["hit_1k_spend"] == "Yes")
            hit_5k = sum(1 for c in creative_summary if c["hit_5k_spend"] == "Yes")
            hit_10k = sum(1 for c in creative_summary if c["hit_10k_spend"] == "Yes")

            print(f"\n{'='*60}")
            print("Creative Analysis Summary")
            print(f"{'='*60}")
            print(f"  Total unique creatives: {total_creatives}")
            print(f"  Hit $1K spend:  {hit_1k} ({round(hit_1k/total_creatives*100,1) if total_creatives else 0}%)")
            print(f"  Hit $5K spend:  {hit_5k} ({round(hit_5k/total_creatives*100,1) if total_creatives else 0}%)")
            print(f"  Hit $10K spend: {hit_10k} ({round(hit_10k/total_creatives*100,1) if total_creatives else 0}%)")
    else:
        print("\n[Meta Ads] Skipped (use --meta flag to include creative data)")

    print(f"\nExport complete! Import these CSVs into Power BI:")
    print(f"  {out_dir}/daily_kpis.csv")
    print(f"  {out_dir}/platform_daily.csv")
    print(f"  {out_dir}/dim_date.csv")
    if args.meta:
        print(f"  {out_dir}/creative_performance.csv")
        print(f"  {out_dir}/creative_summary.csv")


if __name__ == "__main__":
    main()
