"""
Shopify Admin API client for fetching revenue, orders, and financial metrics.
"""

import requests
from datetime import datetime, timedelta


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

    def _get(self, endpoint, params=None):
        url = f"{self.store_url}/admin/api/{self.API_VERSION}/{endpoint}.json"
        response = requests.get(url, headers=self.headers, params=params, timeout=30)
        response.raise_for_status()
        return response.json()

    def get_daily_metrics(self, date=None):
        """
        Fetch daily financial metrics from Shopify for a given date.
        If no date is provided, fetches yesterday's data.

        Returns a dict with keys like:
            gross_revenue, net_revenue, total_orders, avg_order_value,
            refund_amount, total_shipping, total_tax, total_discounts, etc.
        """
        if date is None:
            date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")

        start = f"{date}T00:00:00-00:00"
        end = f"{date}T23:59:59-00:00"

        orders = self._fetch_all_orders(start, end)
        return self._calculate_metrics(orders, date)

    def _fetch_all_orders(self, created_at_min, created_at_max):
        """Fetch all orders for a date range, handling pagination."""
        all_orders = []
        params = {
            "created_at_min": created_at_min,
            "created_at_max": created_at_max,
            "status": "any",
            "limit": 250,
            "fields": (
                "id,total_price,subtotal_price,total_discounts,"
                "total_shipping_price_set,total_tax,financial_status,"
                "refunds,line_items,customer"
            ),
        }

        while True:
            data = self._get("orders", params=params)
            orders = data.get("orders", [])
            all_orders.extend(orders)

            if len(orders) < 250:
                break

            # Use the last order ID for pagination
            params["since_id"] = orders[-1]["id"]

        return all_orders

    def _calculate_metrics(self, orders, date):
        """Calculate P&L metrics from raw Shopify orders."""
        total_orders = len(orders)
        gross_revenue = 0.0
        subtotal = 0.0
        total_discounts = 0.0
        total_shipping = 0.0
        total_tax = 0.0
        refund_amount = 0.0
        total_cogs = 0.0
        new_customer_orders = 0
        returning_customer_orders = 0
        total_items_sold = 0

        for order in orders:
            price = self._safe_float(order.get("total_price", 0))
            gross_revenue += price
            subtotal += self._safe_float(order.get("subtotal_price", 0))
            total_discounts += self._safe_float(order.get("total_discounts", 0))

            # Shipping
            shipping_set = order.get("total_shipping_price_set", {})
            shop_money = shipping_set.get("shop_money", {})
            total_shipping += self._safe_float(shop_money.get("amount", 0))

            # Tax
            total_tax += self._safe_float(order.get("total_tax", 0))

            # Refunds
            for refund in order.get("refunds", []):
                for txn in refund.get("transactions", []):
                    refund_amount += self._safe_float(txn.get("amount", 0))

            # Line items for COGS and item count
            for item in order.get("line_items", []):
                qty = item.get("quantity", 0)
                total_items_sold += qty
                # Shopify doesn't have native COGS — this uses cost per item if set
                cost = self._safe_float(item.get("price", 0))
                # Note: For actual COGS you may need to use inventory cost
                # from product variants or a separate COGS data source

            # Customer type
            customer = order.get("customer", {})
            if customer:
                order_count = customer.get("orders_count", 1)
                if order_count <= 1:
                    new_customer_orders += 1
                else:
                    returning_customer_orders += 1

        net_revenue = gross_revenue - refund_amount - total_discounts
        avg_order_value = gross_revenue / total_orders if total_orders > 0 else 0

        return {
            "date": date,
            "shopify_gross_revenue": round(gross_revenue, 2),
            "shopify_net_revenue": round(net_revenue, 2),
            "shopify_subtotal": round(subtotal, 2),
            "shopify_total_orders": total_orders,
            "shopify_avg_order_value": round(avg_order_value, 2),
            "shopify_total_discounts": round(total_discounts, 2),
            "shopify_total_shipping": round(total_shipping, 2),
            "shopify_total_tax": round(total_tax, 2),
            "shopify_refund_amount": round(refund_amount, 2),
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
