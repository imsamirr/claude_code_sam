"""
Meta (Facebook) Marketing API client for pulling creative-level ad performance data.

Fetches ad-level metrics including spend, impressions, clicks, CTR, CPC, CPM,
conversions, CPA, and ROAS for each individual creative/ad.

Setup:
    1. Create a Facebook App at developers.facebook.com
    2. Add the Marketing API product
    3. Generate a User Access Token with ads_read + read_insights permissions
    4. Get your Ad Account ID (act_XXXXXXXXX) from Meta Business Manager
    5. Add META_ACCESS_TOKEN and META_AD_ACCOUNT_ID to your .env file
"""

import requests
import time
from datetime import datetime, timedelta


class MetaAdsClient:
    BASE_URL = "https://graph.facebook.com/v21.0"

    # Fields to pull at ad level
    AD_INSIGHT_FIELDS = [
        "ad_id",
        "ad_name",
        "adset_id",
        "adset_name",
        "campaign_id",
        "campaign_name",
        "objective",
        "spend",
        "impressions",
        "clicks",
        "cpc",
        "cpm",
        "ctr",
        "actions",
        "action_values",
        "cost_per_action_type",
        "purchase_roas",
        "reach",
        "frequency",
    ]

    def __init__(self, access_token, ad_account_id):
        self.access_token = access_token
        # Ensure account ID has the act_ prefix
        if not ad_account_id.startswith("act_"):
            ad_account_id = f"act_{ad_account_id}"
        self.ad_account_id = ad_account_id

    def get_creative_performance(self, start_date, end_date, level="ad"):
        """
        Pull ad-level performance data for a date range.

        Args:
            start_date: 'YYYY-MM-DD'
            end_date: 'YYYY-MM-DD'
            level: 'ad', 'adset', or 'campaign'

        Returns:
            List of dicts with parsed creative performance metrics.
        """
        all_results = []
        url = f"{self.BASE_URL}/{self.ad_account_id}/insights"

        params = {
            "access_token": self.access_token,
            "fields": ",".join(self.AD_INSIGHT_FIELDS),
            "time_range": f'{{"since":"{start_date}","until":"{end_date}"}}',
            "level": level,
            "time_increment": 1,  # daily breakdown
            "limit": 500,
            "filtering": '[{"field":"spend","operator":"GREATER_THAN","value":"0"}]',
        }

        page = 1
        while True:
            response = requests.get(url, params=params, timeout=60)

            if response.status_code == 429:
                # Rate limited — wait and retry
                retry_after = int(response.headers.get("Retry-After", 60))
                print(f"  [Meta] Rate limited. Waiting {retry_after}s...")
                time.sleep(retry_after)
                continue

            response.raise_for_status()
            data = response.json()

            rows = data.get("data", [])
            for row in rows:
                parsed = self._parse_ad_row(row)
                all_results.append(parsed)

            print(f"  [Meta] Page {page}: {len(rows)} ads (total: {len(all_results)})")

            # Handle pagination
            paging = data.get("paging", {})
            next_url = paging.get("next")
            if next_url:
                url = next_url
                params = {}  # params are embedded in the next URL
                page += 1
                time.sleep(0.5)  # gentle rate limiting
            else:
                break

        return all_results

    def get_creative_performance_chunked(self, start_date, end_date, chunk_days=7):
        """
        Pull creative data in chunks to avoid timeouts on large date ranges.

        Args:
            start_date: 'YYYY-MM-DD'
            end_date: 'YYYY-MM-DD'
            chunk_days: Number of days per API call (default 7)

        Returns:
            List of all parsed ad rows across the full date range.
        """
        all_results = []
        current = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        total_days = (end - current).days + 1

        while current <= end:
            chunk_end = min(current + timedelta(days=chunk_days - 1), end)
            cs = current.strftime("%Y-%m-%d")
            ce = chunk_end.strftime("%Y-%m-%d")

            day_num = (current - datetime.strptime(start_date, "%Y-%m-%d")).days + 1
            print(f"[Meta] Fetching {cs} to {ce} (day {day_num}/{total_days})...")

            chunk_results = self.get_creative_performance(cs, ce)
            all_results.extend(chunk_results)

            current = chunk_end + timedelta(days=1)
            time.sleep(1)  # pause between chunks

        return all_results

    def _parse_ad_row(self, row):
        """Parse a single ad insight row into a clean dict."""
        # Extract purchase actions
        purchases = 0
        purchase_value = 0.0
        cost_per_purchase = 0.0

        actions = row.get("actions") or []
        for action in actions:
            if action.get("action_type") == "purchase":
                purchases = int(action.get("value", 0))
                break

        action_values = row.get("action_values") or []
        for av in action_values:
            if av.get("action_type") == "purchase":
                purchase_value = float(av.get("value", 0))
                break

        cost_per_action = row.get("cost_per_action_type") or []
        for cpa in cost_per_action:
            if cpa.get("action_type") == "purchase":
                cost_per_purchase = float(cpa.get("value", 0))
                break

        # Extract ROAS
        roas_list = row.get("purchase_roas") or []
        roas = float(roas_list[0].get("value", 0)) if roas_list else 0.0

        spend = float(row.get("spend", 0))
        impressions = int(row.get("impressions", 0))
        clicks = int(row.get("clicks", 0))

        return {
            "date": row.get("date_start", ""),
            "ad_id": row.get("ad_id", ""),
            "ad_name": row.get("ad_name", ""),
            "adset_id": row.get("adset_id", ""),
            "adset_name": row.get("adset_name", ""),
            "campaign_id": row.get("campaign_id", ""),
            "campaign_name": row.get("campaign_name", ""),
            "objective": row.get("objective", ""),
            "spend": round(spend, 2),
            "impressions": impressions,
            "clicks": clicks,
            "cpc": round(float(row.get("cpc", 0)), 2),
            "cpm": round(float(row.get("cpm", 0)), 2),
            "ctr": round(float(row.get("ctr", 0)), 2),
            "reach": int(row.get("reach", 0)),
            "frequency": round(float(row.get("frequency", 0)), 2),
            "purchases": purchases,
            "purchase_value": round(purchase_value, 2),
            "cpa": round(cost_per_purchase, 2),
            "roas": round(roas, 2),
        }

    def test_connection(self):
        """Verify API credentials work."""
        url = f"{self.BASE_URL}/{self.ad_account_id}"
        params = {
            "access_token": self.access_token,
            "fields": "name,account_id,account_status,currency,timezone_name",
        }
        response = requests.get(url, params=params, timeout=15)
        response.raise_for_status()
        data = response.json()
        print(f"  [Meta] Connected: {data.get('name')} ({data.get('account_id')})")
        print(f"  [Meta] Currency: {data.get('currency')}, TZ: {data.get('timezone_name')}")
        return data
