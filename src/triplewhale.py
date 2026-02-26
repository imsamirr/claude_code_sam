"""
TripleWhale API client for fetching ad spend, ROAS, and attribution metrics.
"""

import requests
from datetime import datetime, timedelta


class TripleWhaleClient:
    BASE_URL = "https://api.triplewhale.com/api/v2"

    def __init__(self, api_key, shop_domain):
        self.api_key = api_key
        self.shop_domain = shop_domain
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
            "period": {
                "start": date,
                "end": date,
            },
            "todayHour": 23,
            "shopDomain": self.shop_domain,
        }

        try:
            data = self._make_request("POST", "summary-page/get-data", json_data=payload)
            return self._parse_summary(data, date)
        except requests.exceptions.HTTPError as e:
            print(f"[TripleWhale] Error fetching metrics for {date}: {e}")
            return self._empty_metrics(date)

    def _parse_summary(self, data, date):
        """Parse the TripleWhale summary response into a flat dict.

        The API returns a list of metric objects, each with:
          - metricId: unique identifier
          - values.current: the aggregated value for the period
        """
        metrics = data.get("metrics", [])

        # Build a lookup by metricId
        lookup = {}
        for m in metrics:
            mid = m.get("metricId", "")
            current = m.get("values", {}).get("current", 0)
            lookup[mid] = current

        total_ad_spend = self._safe_float(lookup.get("blendedAds", 0))
        fb_spend = self._safe_float(lookup.get("fb_ads_spend", 0))
        google_spend = self._safe_float(lookup.get("ga_adCost", 0))
        tiktok_spend = self._safe_float(lookup.get("tiktok_spend", 0))
        other_spend = round(total_ad_spend - fb_spend - google_spend - tiktok_spend, 2)

        return {
            "date": date,
            "tw_total_ad_spend": total_ad_spend,
            "tw_facebook_spend": fb_spend,
            "tw_google_spend": google_spend,
            "tw_tiktok_spend": tiktok_spend,
            "tw_other_spend": max(other_spend, 0),
            "tw_blended_roas": self._safe_float(lookup.get("totalRoas", 0)),
            "tw_blended_cpa": self._safe_float(lookup.get("totalCpa", 0)),
            "tw_nc_cpa": self._safe_float(lookup.get("newCustomersCpa", 0)),
            "tw_new_customers": self._safe_float(lookup.get("newCustomersOrders", 0)),
            "tw_returning_customers": self._safe_float(lookup.get("returningCustomerOrders", 0)),
            "tw_mer": self._safe_float(lookup.get("mer", 0)),
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
            "tw_nc_cpa": 0,
            "tw_new_customers": 0,
            "tw_returning_customers": 0,
            "tw_mer": 0,
        }

    @staticmethod
    def _safe_float(value):
        try:
            return round(float(value), 2)
        except (TypeError, ValueError):
            return 0.0
