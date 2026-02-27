"""
Power BI Python Data Source Script.

Use this in Power BI Desktop: Get Data → Python Script
Paste this script to pull data directly from TripleWhale and Meta Ads
into Power BI without needing CSV files.

Note: Requires pandas, requests, python-dotenv installed in your Python environment.
"""

import os
import pandas as pd
import requests
from datetime import datetime, timedelta
from collections import defaultdict

# ============================================================
# CONFIGURATION — Update these values
# ============================================================
TRIPLEWHALE_API_KEY = "b5b10dc3-a96a-4bef-a77a-355714f76132"
SHOP_DOMAIN = "ortho-wears.myshopify.com"
META_ACCESS_TOKEN = ""  # Fill when Meta App is ready
META_AD_ACCOUNT_ID = ""  # Fill when Meta App is ready

# Date range — adjust as needed
START_DATE = (datetime.now() - timedelta(days=60)).strftime("%Y-%m-%d")
END_DATE = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")

# ============================================================
# TRIPLEWHALE DATA FETCH
# ============================================================
PLATFORMS = ["google", "facebook", "tiktok", "snapchat", "pinterest", "taboola", "applovin"]

TW_HEADERS = {
    "x-api-key": TRIPLEWHALE_API_KEY,
    "Content-Type": "application/json",
}

def fetch_tw_day(date_str):
    """Fetch one day from TripleWhale summary-page."""
    payload = {
        "period": {"start": date_str, "end": date_str},
        "todayHour": 23,
        "shopDomain": SHOP_DOMAIN,
    }
    try:
        r = requests.post(
            "https://api.triplewhale.com/api/v2/summary-page/get-data",
            headers=TW_HEADERS, json=payload, timeout=120
        )
        r.raise_for_status()
        data = r.json()
        metrics = {m["metricId"]: m.get("values", {}).get("current", 0) for m in data.get("metrics", [])}
        f = lambda v: round(float(v or 0), 2)

        gross = f(metrics.get("totalSales", 0))
        refunds = f(metrics.get("totalRefunds", 0))
        gateway = f(metrics.get("totalPaymentGatewayCosts", 0))
        net = round(gross - refunds - gateway, 2)
        cogs = f(metrics.get("totalProductCosts", 0))
        margin = round(net - cogs, 2)
        attr_roas = f(metrics.get("blendedAttributedRoas", 0))

        row = {
            "date": date_str,
            "gross_sales": gross, "net_revenue": net, "refunds": refunds,
            "cogs": cogs, "margin": margin,
            "gross_margin_pct": round(margin / net * 100, 2) if net > 0 else 0,
            "orders": f(metrics.get("totalOrders", 0)),
            "aov": f(metrics.get("shopifyAov", 0)),
            "mer": f(metrics.get("mer", 0)),
            "amer": round(1 / attr_roas * 100, 2) if attr_roas > 0 else 0,
            "cac": f(metrics.get("totalCpa", 0)),
            "ncac": f(metrics.get("newCustomersCpa", 0)),
            "sessions": f(metrics.get("pixelVisitors", 0)),
            "cvr": f(metrics.get("pixelConversionRate", 0)),
            "atc_pct": f(metrics.get("pixelPercentAtc", 0)),
            "users": f(metrics.get("pixelUniqueVisitors", 0)),
            "new_customer_orders": f(metrics.get("newCustomersOrders", 0)),
            "new_customer_pct": f(metrics.get("newCustomersPercent", 0)),
            "new_customers_revenue": f(metrics.get("newCustomerSales", 0)),
            "returning_customers_count": f(metrics.get("returningCustomerOrders", 0)),
            "returning_customers_revenue": f(metrics.get("rcRevenue", 0)),
            "cltv": f(metrics.get("uniqueCustomerLifetimeValue", 0)),
        }

        # Platform metrics
        platform_map = {
            "google": {"spend": "ga_adCost", "roas": "ga_ROAS", "cpc": "googleCpc", "clicks": "totalGoogleAdsClicks", "cpm": "totalGoogleAdsCpm", "ctr": "totalGoogleAdsCtr", "cpa": "googleAllCpa"},
            "facebook": {"spend": "fb_ads_spend", "roas": "fb_ads_purchase_roas", "cpc": "averageFacebookCpc", "clicks": "facebookClicks", "cpm": "averageFacebookCpm", "ctr": "facebookCtr", "cpa": "facebookCpa"},
            "tiktok": {"spend": "tiktok_spend", "roas": "tiktok_complete_payment_roas", "cpc": "averageTiktokCpc", "clicks": "tiktok_clicks", "cpm": "averageTiktokCpm", "ctr": "tiktokCtr", "cpa": "tiktokCpa"},
            "snapchat": {"spend": "totalSnapchatSpend", "roas": "totalSnapchatRoas", "cpm": "snapchatCpm", "cpa": "snapchatCpa"},
            "pinterest": {"spend": "pinterestSpend", "roas": "pinterestRoas", "cpc": "pinterestCpc", "clicks": "pinterestClicks", "cpm": "pinterestCpm", "ctr": "pinterestCtr"},
            "taboola": {"spend": "taboolaSpend", "roas": "taboolaRoas", "cpc": "taboolaCPC", "clicks": "taboolaClicks", "cpm": "taboolaVCPM", "ctr": "taboolaVCTR", "cpa": "taboolaCPA"},
            "applovin": {"spend": "applovinSpend", "roas": "applovinRoas", "cpc": "applovinActualCPC", "clicks": "applovinClicks", "cpm": "applovinVCPM", "ctr": "applovinVCTR", "cpa": "applovinCPA"},
        }

        for plat, fields in platform_map.items():
            for key, metric_id in fields.items():
                row[f"{plat}_{key}"] = f(metrics.get(metric_id, 0))

        total_spend = sum(row.get(f"{p}_spend", 0) for p in PLATFORMS)
        row["total_ad_spend"] = round(total_spend, 2)
        row["blended_roas"] = round(gross / total_spend, 2) if total_spend > 0 else 0

        return row
    except Exception as e:
        print(f"Error fetching {date_str}: {e}")
        return None


# Fetch all days
import time
all_rows = []
current = datetime.strptime(START_DATE, "%Y-%m-%d")
end = datetime.strptime(END_DATE, "%Y-%m-%d")

while current <= end:
    ds = current.strftime("%Y-%m-%d")
    row = fetch_tw_day(ds)
    if row:
        all_rows.append(row)
    current += timedelta(days=1)
    time.sleep(0.3)

# Build DataFrames for Power BI
daily_kpis = pd.DataFrame(all_rows)

# Build platform_daily (unpivoted)
platform_rows = []
for row in all_rows:
    for plat in PLATFORMS:
        spend = row.get(f"{plat}_spend", 0)
        if spend > 0:
            platform_rows.append({
                "date": row["date"],
                "platform": plat.title(),
                "spend": spend,
                "roas": row.get(f"{plat}_roas", 0),
                "cpc": row.get(f"{plat}_cpc", 0),
                "clicks": row.get(f"{plat}_clicks", 0),
                "cpm": row.get(f"{plat}_cpm", 0),
                "ctr": row.get(f"{plat}_ctr", 0),
                "cpa": row.get(f"{plat}_cpa", 0),
            })

platform_daily = pd.DataFrame(platform_rows)

# Power BI will detect these DataFrames automatically:
# - daily_kpis
# - platform_daily
