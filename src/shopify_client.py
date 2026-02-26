"""
Shopify Admin API client for fetching revenue, orders, and financial metrics.

Metrics match Shopify Analytics definitions:
  - Gross Sales = sum of (line item price × quantity) before discounts
  - Discounts = total discount amounts applied
  - Returns = value of refunded line items
  - Net Sales = Gross Sales - Discounts - Returns
  - Total Sales = Net Sales + Shipping + Tax
"""

import requests
from datetime import datetime, timedelta, timezone


class ShopifyClient:
    API_VERSION = "2024-01"

    def __init__(self, store_url, access_token):
        # Normalize store URL
        self.store_url = store_url.rstrip("/")
        if not self.store_url.startswith("https://"):
            self.store_url = f"https://{self.store_url}"

        self.access_token = access_token
        self.headers = {
            "X-Shopify-Access-Token": access_token,
            "Content-Type": "application/json",
        }
        self._timezone_offset = None

    def _get(self, endpoint, params=None):
        url = f"{self.store_url}/admin/api/{self.API_VERSION}/{endpoint}.json"
        response = requests.get(url, headers=self.headers, params=params, timeout=30)
        response.raise_for_status()
        return response.json()

    def _get_raw(self, url, params=None):
        """GET request with a full URL (for cursor-based pagination)."""
        response = requests.get(url, headers=self.headers, params=params, timeout=30)
        response.raise_for_status()
        return response

    def _get_timezone_offset(self):
        """Fetch the store's timezone offset from the Shopify API."""
        if self._timezone_offset is not None:
            return self._timezone_offset

        data = self._get("shop")
        iana_tz = data.get("shop", {}).get("iana_timezone", "America/New_York")

        # Map common US timezones to UTC offsets
        tz_offsets = {
            "America/New_York": "-05:00",
            "America/Chicago": "-06:00",
            "America/Denver": "-07:00",
            "America/Los_Angeles": "-08:00",
            "America/Anchorage": "-09:00",
            "Pacific/Honolulu": "-10:00",
            "America/Phoenix": "-07:00",
            "America/Toronto": "-05:00",
            "America/Vancouver": "-08:00",
            "Europe/London": "+00:00",
            "UTC": "+00:00",
        }
        self._timezone_offset = tz_offsets.get(iana_tz, "-05:00")
        return self._timezone_offset

    def get_daily_metrics(self, date=None):
        """
        Fetch daily financial metrics from Shopify for a given date.
        Uses the store's timezone to match Shopify Analytics.

        Returns are fetched separately to match Shopify Analytics, which counts
        refunds by the date they were processed (not the original order date).
        """
        if date is None:
            date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")

        tz_offset = self._get_timezone_offset()
        start = f"{date}T00:00:00{tz_offset}"
        end = f"{date}T23:59:59{tz_offset}"

        orders = self._fetch_all_orders(start, end)
        refund_total = self._fetch_daily_refunds(date, tz_offset)
        return self._calculate_metrics(orders, date, refund_total)

    def _fetch_all_orders(self, created_at_min, created_at_max):
        """Fetch all orders for a date range using cursor-based pagination."""
        all_orders = []
        url = f"{self.store_url}/admin/api/{self.API_VERSION}/orders.json"
        params = {
            "created_at_min": created_at_min,
            "created_at_max": created_at_max,
            "status": "any",
            "limit": 250,
        }

        while url:
            response = self._get_raw(url, params=params)
            data = response.json()
            orders = data.get("orders", [])
            all_orders.extend(orders)

            # Use Link header for cursor-based pagination
            url = None
            params = None  # params are included in the next URL
            link_header = response.headers.get("Link", "")
            for part in link_header.split(","):
                if 'rel="next"' in part:
                    url = part.split("<")[1].split(">")[0].strip()
                    break

        return all_orders

    def _fetch_daily_refunds(self, date, tz_offset):
        """
        Fetch the total refund amount for a specific date.

        Shopify Analytics counts refunds by the date they were processed,
        not the original order date. We search orders updated within a wide
        window and filter refunds by their created_at date.
        """
        target_date = datetime.strptime(date, "%Y-%m-%d").date()
        # Search orders updated within ±30 days to catch all refunds
        search_start = (target_date - timedelta(days=30)).strftime("%Y-%m-%d")
        search_end = (target_date + timedelta(days=1)).strftime("%Y-%m-%d")

        all_orders = []
        url = f"{self.store_url}/admin/api/{self.API_VERSION}/orders.json"
        params = {
            "updated_at_min": f"{search_start}T00:00:00{tz_offset}",
            "updated_at_max": f"{search_end}T23:59:59{tz_offset}",
            "status": "any",
            "limit": 250,
            "fields": "id,refunds",
        }

        while url:
            response = self._get_raw(url, params=params)
            data = response.json()
            orders = data.get("orders", [])
            all_orders.extend(orders)

            url = None
            params = None
            link_header = response.headers.get("Link", "")
            for part in link_header.split(","):
                if 'rel="next"' in part:
                    url = part.split("<")[1].split(">")[0].strip()
                    break

        # Sum refund transaction amounts for refunds processed on the target date
        # Parse timezone offset for comparison
        tz_hours = int(tz_offset.split(":")[0])
        tz_mins = int(tz_offset.split(":")[1]) if tz_hours >= 0 else -int(tz_offset.split(":")[1])
        tz_info = timezone(timedelta(hours=tz_hours, minutes=tz_mins))

        total_refunds = 0.0
        for order in all_orders:
            for refund in order.get("refunds", []):
                created_str = refund.get("created_at", "")
                if not created_str:
                    continue
                created_dt = datetime.fromisoformat(created_str.replace("Z", "+00:00"))
                created_local = created_dt.astimezone(tz_info)
                if created_local.date() == target_date:
                    for txn in refund.get("transactions", []):
                        total_refunds += self._safe_float(txn.get("amount", 0))

        return round(total_refunds, 2)

    def _calculate_metrics(self, orders, date, refund_total=0.0):
        """
        Calculate metrics matching Shopify Analytics definitions:
          Gross Sales = sum(line_item.price * line_item.quantity)
          Discounts = sum(order.total_discounts)
          Returns = refund transaction amounts processed on this date
          Net Sales = Gross Sales - Discounts - Returns
          Total Sales = Net Sales + Shipping + Tax
        """
        total_orders = len(orders)
        gross_sales = 0.0
        total_discounts = 0.0
        total_shipping = 0.0
        total_tax = 0.0
        new_customer_orders = 0
        returning_customer_orders = 0
        total_items_sold = 0

        for order in orders:
            # Gross sales = sum of original line item prices × quantity
            for item in order.get("line_items", []):
                price = self._safe_float(item.get("price", 0))
                qty = int(item.get("quantity", 0))
                gross_sales += price * qty
                total_items_sold += qty

            total_discounts += self._safe_float(order.get("total_discounts", 0))

            # Shipping
            shipping_set = order.get("total_shipping_price_set", {})
            shop_money = shipping_set.get("shop_money", {})
            total_shipping += self._safe_float(shop_money.get("amount", 0))

            # Tax
            total_tax += self._safe_float(order.get("total_tax", 0))

            # Customer type
            customer = order.get("customer", {})
            if customer:
                order_count = customer.get("orders_count", 1)
                if order_count <= 1:
                    new_customer_orders += 1
                else:
                    returning_customer_orders += 1

        net_sales = gross_sales - total_discounts - refund_total
        total_sales = net_sales + total_shipping + total_tax
        avg_order_value = total_sales / total_orders if total_orders > 0 else 0

        return {
            "date": date,
            "shopify_gross_sales": round(gross_sales, 2),
            "shopify_discounts": round(total_discounts, 2),
            "shopify_returns": round(refund_total, 2),
            "shopify_net_sales": round(net_sales, 2),
            "shopify_shipping": round(total_shipping, 2),
            "shopify_tax": round(total_tax, 2),
            "shopify_total_sales": round(total_sales, 2),
            "shopify_total_orders": total_orders,
            "shopify_avg_order_value": round(avg_order_value, 2),
            "shopify_items_sold": total_items_sold,
            "shopify_new_customer_orders": new_customer_orders,
            "shopify_returning_customer_orders": returning_customer_orders,
        }

    @staticmethod
    def _safe_float(value):
        try:
            return float(value)
        except (TypeError, ValueError):
            return 0.0
