"""
Google Sheets integration for writing daily financial metrics.
"""

import gspread
from google.oauth2.service_account import Credentials


# Column headers in the order they appear in the sheet
# Shopify metrics match Shopify Analytics definitions exactly
COLUMN_HEADERS = [
    "Date",
    # --- Shopify Revenue Metrics (matches Shopify Analytics) ---
    "Gross Sales",
    "Discounts",
    "Returns",
    "Net Sales",
    "Shipping",
    "Tax",
    "Total Sales",
    "Total Orders",
    "Avg Order Value",
    "Items Sold",
    "New Customer Orders",
    "Returning Customer Orders",
    # --- TripleWhale Ad & Attribution Metrics ---
    "Total Ad Spend",
    "Facebook Spend",
    "Google Spend",
    "TikTok Spend",
    "Other Spend",
    "Blended ROAS",
    "Blended CPA",
    "NC CPA",
    "TW New Customers",
    "TW Returning Customers",
    "MER",
    # --- Calculated P&L Metrics ---
    "Net Profit (Sales - Ads)",
    "Ad Spend % of Sales",
]


class SheetsClient:
    SCOPES = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive",
    ]

    def __init__(self, credentials_path, sheet_id, tab_name="Daily Metrics"):
        creds = Credentials.from_service_account_file(credentials_path, scopes=self.SCOPES)
        self.client = gspread.authorize(creds)
        self.sheet_id = sheet_id
        self.tab_name = tab_name

    def _get_worksheet(self):
        """Open the spreadsheet and get (or create) the target worksheet."""
        spreadsheet = self.client.open_by_key(self.sheet_id)

        try:
            worksheet = spreadsheet.worksheet(self.tab_name)
        except gspread.exceptions.WorksheetNotFound:
            worksheet = spreadsheet.add_worksheet(title=self.tab_name, rows=1000, cols=30)

        return worksheet

    def ensure_headers(self, worksheet):
        """Make sure the header row exists. If the sheet is empty, write headers."""
        first_row = worksheet.row_values(1)
        if not first_row or first_row[0] != COLUMN_HEADERS[0]:
            worksheet.update("A1", [COLUMN_HEADERS])
            # Bold the header row
            worksheet.format("A1:Z1", {
                "textFormat": {"bold": True},
                "backgroundColor": {"red": 0.9, "green": 0.9, "blue": 0.95},
            })
            print("[Sheets] Header row created.")

    def write_daily_row(self, shopify_data, tw_data):
        """
        Write one row of combined daily metrics to the sheet.
        If a row for this date already exists, it will be updated instead.
        """
        worksheet = self._get_worksheet()
        self.ensure_headers(worksheet)

        date = shopify_data.get("date") or tw_data.get("date")
        if not date:
            print("[Sheets] Error: No date found in data.")
            return

        # Calculate derived P&L fields
        total_sales = shopify_data.get("shopify_total_sales", 0)
        total_ad_spend = tw_data.get("tw_total_ad_spend", 0)
        net_profit = round(total_sales - total_ad_spend, 2)
        ad_spend_pct = round((total_ad_spend / total_sales * 100), 2) if total_sales > 0 else 0

        # Build the row in the same order as COLUMN_HEADERS
        row = [
            date,
            # Shopify (matches Shopify Analytics definitions)
            shopify_data.get("shopify_gross_sales", 0),
            shopify_data.get("shopify_discounts", 0),
            shopify_data.get("shopify_returns", 0),
            shopify_data.get("shopify_net_sales", 0),
            shopify_data.get("shopify_shipping", 0),
            shopify_data.get("shopify_tax", 0),
            shopify_data.get("shopify_total_sales", 0),
            shopify_data.get("shopify_total_orders", 0),
            shopify_data.get("shopify_avg_order_value", 0),
            shopify_data.get("shopify_items_sold", 0),
            shopify_data.get("shopify_new_customer_orders", 0),
            shopify_data.get("shopify_returning_customer_orders", 0),
            # TripleWhale
            tw_data.get("tw_total_ad_spend", 0),
            tw_data.get("tw_facebook_spend", 0),
            tw_data.get("tw_google_spend", 0),
            tw_data.get("tw_tiktok_spend", 0),
            tw_data.get("tw_other_spend", 0),
            tw_data.get("tw_blended_roas", 0),
            tw_data.get("tw_blended_cpa", 0),
            tw_data.get("tw_nc_cpa", 0),
            tw_data.get("tw_new_customers", 0),
            tw_data.get("tw_returning_customers", 0),
            tw_data.get("tw_mer", 0),
            # Calculated
            net_profit,
            ad_spend_pct,
        ]

        # Check if a row for this date already exists (update instead of duplicate)
        existing_dates = worksheet.col_values(1)
        row_index = None
        for i, val in enumerate(existing_dates):
            if val == date:
                row_index = i + 1  # gspread is 1-indexed
                break

        if row_index:
            # Update existing row
            cell_range = f"A{row_index}:Z{row_index}"
            worksheet.update(cell_range, [row])
            print(f"[Sheets] Updated existing row for {date} (row {row_index}).")
        else:
            # Append new row
            worksheet.append_row(row, value_input_option="USER_ENTERED")
            print(f"[Sheets] Added new row for {date}.")

    def write_multiple_days(self, daily_data_list):
        """
        Write multiple days of data at once.
        daily_data_list: list of tuples (shopify_data, tw_data)
        """
        for shopify_data, tw_data in daily_data_list:
            self.write_daily_row(shopify_data, tw_data)
