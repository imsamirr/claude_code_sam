"""
TripleWhale API client for fetching comprehensive daily metrics.

Pulls all revenue, ad spend, attribution, pixel, and per-platform metrics
from the TripleWhale summary-page endpoint.
"""

import requests
from datetime import datetime, timedelta


class TripleWhaleClient:
    BASE_URL = "https://api.triplewhale.com/api/v2"

    def __init__(self, api_key, shop_domain):
        self.api_key = api_key
        # Strip protocol prefix — the API expects just the domain
        self.shop_domain = shop_domain.replace("https://", "").replace("http://", "").rstrip("/")
        self.headers = {
            "x-api-key": api_key,
            "Content-Type": "application/json",
        }

    def _make_request(self, method, endpoint, json_data=None, params=None):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.request(
            method, url, headers=self.headers, json=json_data, params=params, timeout=60
        )
        response.raise_for_status()
        return response.json()

    def get_daily_metrics(self, date=None):
        """
        Fetch ALL daily metrics from TripleWhale for a given date.
        Returns a flat dict with every metric the sheet needs.
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
            return self._parse_all_metrics(data, date)
        except requests.exceptions.HTTPError as e:
            print(f"  [TripleWhale] Error fetching metrics for {date}: {e}")
            return self._empty_metrics(date)

    def _parse_all_metrics(self, data, date):
        """Parse ALL metrics from TW response into a flat dict."""
        metrics = data.get("metrics", [])

        # Build lookup: metricId -> current value
        lk = {}
        for m in metrics:
            mid = m.get("metricId", "")
            current = m.get("values", {}).get("current", 0)
            lk[mid] = current

        f = self._safe_float

        # --- Revenue & P&L ---
        gross_sales = f(lk.get("totalSales", 0))
        payment_gateway_fee = f(lk.get("totalPaymentGatewayCosts", 0))
        refunds = f(lk.get("totalRefunds", 0))
        net_revenue = round(gross_sales - refunds - payment_gateway_fee, 2)
        cogs = f(lk.get("totalProductCosts", 0))
        margin = round(net_revenue - cogs, 2)
        gross_margin_pct = round((margin / net_revenue * 100), 2) if net_revenue > 0 else 0

        # --- Ad Spend ---
        total_ad_spend = f(lk.get("blendedAds", 0))
        google_spend = f(lk.get("ga_adCost", 0))
        fb_spend = f(lk.get("fb_ads_spend", 0))
        tiktok_spend = f(lk.get("tiktok_spend", 0))
        snapchat_spend = f(lk.get("totalSnapchatSpend", 0))
        pinterest_spend = f(lk.get("pinterestSpend", 0))
        outbrain_spend = f(lk.get("outbrainSpend", 0))
        taboola_spend = f(lk.get("taboolaSpend", 0))
        applovin_spend = f(lk.get("applovinSpend", 0))

        # --- Pixel / Sessions ---
        sessions = f(lk.get("pixelVisitors", 0))
        atc_sessions = f(lk.get("pixelUniqueSessionsAtc", 0))
        checkout_sessions = f(lk.get("pixelUniqueSessionsCheckout", 0))
        ic_pct = round((checkout_sessions / sessions * 100), 2) if sessions > 0 else 0

        # --- aMER calculation ---
        # aMER = ad spend / attributed conversion value × 100
        attributed_roas = f(lk.get("blendedAttributedRoas", 0))
        amer = round((1 / attributed_roas * 100), 2) if attributed_roas > 0 else 0

        # --- Snapchat calculated fields ---
        snap_swipes = f(lk.get("snapchat_swipes", 0))
        snap_impr = f(lk.get("snapchatImpressions", 0))
        snap_cpc = round(snapchat_spend / snap_swipes, 2) if snap_swipes > 0 else 0
        snap_ctr = round(snap_swipes / snap_impr * 100, 2) if snap_impr > 0 else 0

        # --- Pinterest CPA (not directly available) ---
        pinterest_purchases = f(lk.get("pinterestPurchases", 0))
        pinterest_cpa = round(pinterest_spend / pinterest_purchases, 2) if pinterest_purchases > 0 else 0

        # --- New customer orders for growth tracking ---
        new_customers_count = f(lk.get("newCustomersOrders", 0))

        return {
            "date": date,
            # Revenue & P&L
            "gross_sales": gross_sales,
            "payment_gateway_fee": payment_gateway_fee,
            "refunds": refunds,
            "net_revenue": net_revenue,
            "cogs": cogs,
            "margin": margin,
            "gross_margin_pct": gross_margin_pct,
            "orders": f(lk.get("totalOrders", 0)),
            "new_customer_orders": new_customers_count,
            "mer": f(lk.get("mer", 0)),
            "amer": amer,
            "aov": f(lk.get("shopifyAov", 0)),
            # Pixel / Conversion
            "sessions": sessions,
            "cvr": f(lk.get("pixelConversionRate", 0)),
            "cac": f(lk.get("totalCpa", 0)),
            "ncac": f(lk.get("newCustomersCpa", 0)),
            "atc_pct": f(lk.get("pixelPercentAtc", 0)),
            "ic_pct": ic_pct,
            "cltv": f(lk.get("uniqueCustomerLifetimeValue", 0)),
            # Traffic by channel (not available from summary-page endpoint)
            "traffic_direct": "",
            "traffic_unknown": "",
            "traffic_social": "",
            "traffic_search": "",
            "traffic_email": "",
            # Users / Customers
            "users": f(lk.get("pixelUniqueVisitors", 0)),
            "customers": f(lk.get("getUniqueCustomerCount", 0)),
            "new_customer_pct": f(lk.get("newCustomersPercent", 0)),
            "returning_customer_pct": f(lk.get("oldCustomersPercent", 0)),
            "new_customers_count": new_customers_count,
            "new_customers_revenue": f(lk.get("newCustomerSales", 0)),
            "returning_customers_count": f(lk.get("returningCustomerOrders", 0)),
            "returning_customers_revenue": f(lk.get("rcRevenue", 0)),
            "new_customer_growth": "",  # calculated during backfill
            # Platform Spend
            "google_spend": google_spend,
            "facebook_spend": fb_spend,
            "tiktok_spend": tiktok_spend,
            "snapchat_spend": snapchat_spend,
            "pinterest_spend": pinterest_spend,
            "outbrain_spend": outbrain_spend,
            "taboola_spend": taboola_spend,
            "applovin_spend": applovin_spend,
            # Platform ROAS
            "google_roas": f(lk.get("ga_ROAS", 0)),
            "facebook_roas": f(lk.get("fb_ads_purchase_roas", 0)),
            "tiktok_roas": f(lk.get("tiktok_complete_payment_roas", 0)),
            "snapchat_roas": f(lk.get("totalSnapchatRoas", 0)),
            "pinterest_roas": f(lk.get("pinterestRoas", 0)),
            "taboola_roas": f(lk.get("taboolaRoas", 0)),
            "applovin_roas": f(lk.get("applovinRoas", 0)),
            # Google detailed
            "google_cpc": f(lk.get("googleCpc", 0)),
            "google_clicks": f(lk.get("totalGoogleAdsClicks", 0)),
            "google_cpm": f(lk.get("totalGoogleAdsCpm", 0)),
            "google_ctr": f(lk.get("totalGoogleAdsCtr", 0)),
            "google_cpa": f(lk.get("googleAllCpa", 0)),
            # Facebook detailed
            "facebook_cpc": f(lk.get("averageFacebookCpc", 0)),
            "facebook_clicks": f(lk.get("facebookClicks", 0)),
            "facebook_cpm": f(lk.get("averageFacebookCpm", 0)),
            "facebook_ctr": f(lk.get("facebookCtr", 0)),
            "facebook_cpa": f(lk.get("facebookCpa", 0)),
            # TikTok detailed
            "tiktok_cpc": f(lk.get("averageTiktokCpc", 0)),
            "tiktok_clicks": f(lk.get("tiktok_clicks", 0)),
            "tiktok_cpm": f(lk.get("averageTiktokCpm", 0)),
            "tiktok_ctr": f(lk.get("tiktokCtr", 0)),
            "tiktok_cpa": f(lk.get("tiktokCpa", 0)),
            # Snapchat detailed
            "snapchat_cpc": snap_cpc,
            "snapchat_clicks": snap_swipes,
            "snapchat_cpm": f(lk.get("snapchatCpm", 0)),
            "snapchat_ctr": snap_ctr,
            "snapchat_cpa": f(lk.get("snapchatCpa", 0)),
            # Pinterest detailed
            "pinterest_cpc": f(lk.get("pinterestCpc", 0)),
            "pinterest_clicks": f(lk.get("pinterestClicks", 0)),
            "pinterest_cpm": f(lk.get("pinterestCpm", 0)),
            "pinterest_ctr": f(lk.get("pinterestCtr", 0)),
            "pinterest_cpa": pinterest_cpa,
            # Taboola detailed
            "taboola_cpc": f(lk.get("taboolaCPC", 0)),
            "taboola_clicks": f(lk.get("taboolaClicks", 0)),
            "taboola_cpm": f(lk.get("taboolaVCPM", 0)),
            "taboola_ctr": f(lk.get("taboolaVCTR", 0)),
            "taboola_cpa": f(lk.get("taboolaCPA", 0)),
            # Applovin detailed
            "applovin_cpc": f(lk.get("applovinActualCPC", 0)),
            "applovin_clicks": f(lk.get("applovinClicks", 0)),
            "applovin_cpm": f(lk.get("applovinVCPM", 0)),
            "applovin_ctr": f(lk.get("applovinVCTR", 0)),
            "applovin_cpa": f(lk.get("applovinCPA", 0)),
            # Weekly spend increases (calculated during backfill)
            "weekly_google_spend_increase": "",
            "weekly_facebook_spend_increase": "",
        }

    def _empty_metrics(self, date):
        """Return empty metrics dict when API fails."""
        keys = [
            "gross_sales", "payment_gateway_fee", "refunds", "net_revenue",
            "cogs", "margin", "gross_margin_pct", "orders", "new_customer_orders",
            "mer", "amer", "aov", "sessions", "cvr", "cac", "ncac", "atc_pct",
            "ic_pct", "cltv", "traffic_direct", "traffic_unknown", "traffic_social",
            "traffic_search", "traffic_email", "users", "customers",
            "new_customer_pct", "returning_customer_pct", "new_customers_count",
            "new_customers_revenue", "returning_customers_count",
            "returning_customers_revenue", "new_customer_growth",
            "google_spend", "facebook_spend", "tiktok_spend", "snapchat_spend",
            "pinterest_spend", "outbrain_spend", "taboola_spend", "applovin_spend",
            "google_roas", "facebook_roas", "tiktok_roas", "snapchat_roas",
            "pinterest_roas", "taboola_roas", "applovin_roas",
            "google_cpc", "google_clicks", "google_cpm", "google_ctr", "google_cpa",
            "facebook_cpc", "facebook_clicks", "facebook_cpm", "facebook_ctr", "facebook_cpa",
            "tiktok_cpc", "tiktok_clicks", "tiktok_cpm", "tiktok_ctr", "tiktok_cpa",
            "snapchat_cpc", "snapchat_clicks", "snapchat_cpm", "snapchat_ctr", "snapchat_cpa",
            "pinterest_cpc", "pinterest_clicks", "pinterest_cpm", "pinterest_ctr", "pinterest_cpa",
            "taboola_cpc", "taboola_clicks", "taboola_cpm", "taboola_ctr", "taboola_cpa",
            "applovin_cpc", "applovin_clicks", "applovin_cpm", "applovin_ctr", "applovin_cpa",
            "weekly_google_spend_increase", "weekly_facebook_spend_increase",
        ]
        result = {"date": date}
        for k in keys:
            result[k] = 0
        return result

    @staticmethod
    def _safe_float(value):
        try:
            return round(float(value), 2)
        except (TypeError, ValueError):
            return 0.0
