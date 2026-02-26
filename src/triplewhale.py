"""
TripleWhale API client for fetching ad spend, ROAS, and attribution metrics.
"""

import requests
from datetime import datetime, timedelta


class TripleWhaleClient:
    BASE_URL = "https://api.triplewhale.com/api/v2"

    def __init__(self, api_key):
        self.api_key = api_key
        self.headers = {
            "x-api-key": api_key,
            "Content-Type": "application/json",
        }

    def _make_request(self, method, endpoint, json_data=None, params=None):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.request(
            method, url, headers=self.headers, json=json_data, params=params, timeout=30
        )
        response.raise_for_status()
        return response.json()

    def get_daily_metrics(self, date=None):
        """
        Fetch daily P&L metrics from TripleWhale for a given date.
        If no date is provided, fetches yesterday's data.

        Requires API key with "Summary Page: Read" scope.
        """
        if date is None:
            date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")

        payload = {
            "start": date,
            "end": date,
        }

        try:
            data = self._make_request("POST", "summary-page/get-data", json_data=payload)
            return self._parse_summary(data, date)
        except requests.exceptions.HTTPError as e:
            print(f"[TripleWhale] Error fetching metrics for {date}: {e}")
            return self._empty_metrics(date)

    def _parse_summary(self, data, date):
        """Parse the TripleWhale summary response into a flat dict."""
        # The response structure may vary; adapt field names to your TW dashboard
        summary = data.get("data", data)

        # Handle both list and dict responses
        if isinstance(summary, list) and len(summary) > 0:
            summary = summary[0]
        elif isinstance(summary, list):
            return self._empty_metrics(date)

        return {
            "date": date,
            "tw_total_ad_spend": self._safe_float(summary.get("totalAdSpend", summary.get("adSpend", 0))),
            "tw_facebook_spend": self._safe_float(summary.get("facebookSpend", summary.get("fbSpend", 0))),
            "tw_google_spend": self._safe_float(summary.get("googleSpend", summary.get("gSpend", 0))),
            "tw_tiktok_spend": self._safe_float(summary.get("tiktokSpend", summary.get("ttSpend", 0))),
            "tw_other_spend": self._safe_float(summary.get("otherSpend", 0)),
            "tw_blended_roas": self._safe_float(summary.get("blendedRoas", summary.get("roas", 0))),
            "tw_blended_cpa": self._safe_float(summary.get("blendedCpa", summary.get("cpa", 0))),
            "tw_blended_cac": self._safe_float(summary.get("blendedCac", summary.get("cac", 0))),
            "tw_new_customers": self._safe_float(summary.get("newCustomers", 0)),
            "tw_returning_customers": self._safe_float(summary.get("returningCustomers", 0)),
            "tw_pixel_revenue": self._safe_float(summary.get("pixelRevenue", 0)),
            "tw_pixel_roas": self._safe_float(summary.get("pixelRoas", 0)),
        }

    def _empty_metrics(self, date):
        """Return an empty metrics dict when no data is available."""
        return {
            "date": date,
            "tw_total_ad_spend": 0,
            "tw_facebook_spend": 0,
            "tw_google_spend": 0,
            "tw_tiktok_spend": 0,
            "tw_other_spend": 0,
            "tw_blended_roas": 0,
            "tw_blended_cpa": 0,
            "tw_blended_cac": 0,
            "tw_new_customers": 0,
            "tw_returning_customers": 0,
            "tw_pixel_revenue": 0,
            "tw_pixel_roas": 0,
        }

    @staticmethod
    def _safe_float(value):
        try:
            return round(float(value), 2)
        except (TypeError, ValueError):
            return 0.0
