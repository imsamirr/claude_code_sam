"""
Google Sheets integration for writing comprehensive daily financial metrics.
"""

GSPREAD_AVAILABLE = False


# Column headers matching the user's requested layout
COLUMN_HEADERS = [
    "Date",
    # --- Revenue & P&L ---
    "Gross Sales (Order Revenue)",
    "Payment Gateway Fee",
    "Refunds",
    "Net Revenue",
    "COGS",
    "Margin",
    "Gross Margin %",
    "Orders",
    "New Customer Orders",
    "MER",
    "aMER",
    "AOV",
    # --- Conversion ---
    "Sessions",
    "Converted (CVR)",
    "CAC (all customers)",
    "nCAC (new customers)",
    "Added to Cart (ATC) %",
    "Reached Checkout (IC) %",
    "CLTV",
    # --- Traffic By Channel ---
    "Direct",
    "Unknown",
    "Social",
    "Search",
    "Email",
    # --- Users & Customers ---
    "Users",
    "Customers",
    "New Customer (%)",
    "Returning Customers (%)",
    "New Customers (#)",
    "New Customers ($)",
    "Returning Customers (#)",
    "Returning Customers ($)",
    "New Customer Growth (Since Yesterday)",
    # --- Platform Spend ---
    "Google Spend",
    "Facebook Spend",
    "TikTok Spend",
    "Snapchat Spend",
    "Pinterest Spend",
    "Outbrain Spend",
    "Taboola Spend",
    "Applovin Spend",
    # --- Platform ROAS ---
    "Google ROAS (Triple ROAS)",
    "Facebook ROAS (Triple ROAS)",
    "TikTok ROAS (Triple ROAS)",
    "Snapchat ROAS (Triple ROAS)",
    "Pinterest ROAS (Triple ROAS)",
    "Taboola ROAS (Triple ROAS)",
    "Applovin ROAS (Triple ROAS)",
    # --- Google Detailed ---
    "Google CPC",
    "Google Clicks",
    "Google CPM",
    "Google CTR",
    "Google CPA",
    # --- Facebook Detailed ---
    "Facebook CPC",
    "Facebook Clicks",
    "Facebook CPM",
    "Facebook CTR",
    "Facebook CPA",
    # --- TikTok Detailed ---
    "TikTok CPC",
    "TikTok Clicks",
    "TikTok CPM",
    "TikTok CTR",
    "TikTok CPA",
    # --- Snapchat Detailed ---
    "Snapchat CPC",
    "Snapchat Clicks",
    "Snapchat CPM",
    "Snapchat CTR",
    "Snapchat CPA",
    # --- Pinterest Detailed ---
    "Pinterest CPC",
    "Pinterest Clicks",
    "Pinterest CPM",
    "Pinterest CTR",
    "Pinterest CPA",
    # --- Taboola Detailed ---
    "Taboola CPC",
    "Taboola Clicks",
    "Taboola CPM",
    "Taboola CTR",
    "Taboola CPA",
    # --- Applovin Detailed ---
    "Applovin CPC",
    "Applovin Clicks",
    "Applovin CPM",
    "Applovin CTR",
    "Applovin CPA",
    # --- Weekly Trends ---
    "Weekly Google Spend Increase",
    "Weekly Facebook Spend Increase",
]

# Map from TW data dict keys to column order (must match COLUMN_HEADERS)
ROW_KEYS = [
    "date",
    "gross_sales", "payment_gateway_fee", "refunds", "net_revenue",
    "cogs", "margin", "gross_margin_pct", "orders", "new_customer_orders",
    "mer", "amer", "aov",
    "sessions", "cvr", "cac", "ncac", "atc_pct", "ic_pct", "cltv",
    "traffic_direct", "traffic_unknown", "traffic_social", "traffic_search", "traffic_email",
    "users", "customers", "new_customer_pct", "returning_customer_pct",
    "new_customers_count", "new_customers_revenue",
    "returning_customers_count", "returning_customers_revenue",
    "new_customer_growth",
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


def build_row(data):
    """Convert a metrics dict into a row list matching COLUMN_HEADERS order."""
    return [data.get(k, "") for k in ROW_KEYS]


class SheetsClient:
    SCOPES = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive",
    ]

    def __init__(self, credentials_path, sheet_id, tab_name="Daily Metrics"):
        try:
            import gspread
            from google.oauth2.service_account import Credentials
        except Exception:
            raise ImportError(
                "gspread/google-auth not available. "
                "Install: pip install gspread google-auth cffi cryptography"
            )
        creds = Credentials.from_service_account_file(credentials_path, scopes=self.SCOPES)
        self.client = gspread.authorize(creds)
        self.sheet_id = sheet_id
        self.tab_name = tab_name

    def _get_worksheet(self):
        """Open the spreadsheet and get (or create) the target worksheet."""
        spreadsheet = self.client.open_by_key(self.sheet_id)

        try:
            worksheet = spreadsheet.worksheet(self.tab_name)
        except Exception:
            worksheet = spreadsheet.add_worksheet(
                title=self.tab_name, rows=1000, cols=len(COLUMN_HEADERS) + 5
            )

        return worksheet

    def ensure_headers(self, worksheet):
        """Make sure the header row exists."""
        first_row = worksheet.row_values(1)
        if not first_row or first_row[0] != COLUMN_HEADERS[0]:
            worksheet.update("A1", [COLUMN_HEADERS])
            last_col = chr(64 + len(COLUMN_HEADERS)) if len(COLUMN_HEADERS) <= 26 else None
            # For 90+ columns we need multi-letter column reference
            col_count = len(COLUMN_HEADERS)
            col_letter = _col_letter(col_count)
            worksheet.format(f"A1:{col_letter}1", {
                "textFormat": {"bold": True},
                "backgroundColor": {"red": 0.9, "green": 0.9, "blue": 0.95},
            })
            print("[Sheets] Header row created.")

    def write_daily_row(self, data):
        """Write one row of metrics. Updates existing row if date exists."""
        worksheet = self._get_worksheet()
        self.ensure_headers(worksheet)

        date = data.get("date")
        if not date:
            print("[Sheets] Error: No date found in data.")
            return

        row = build_row(data)

        # Check if row for this date already exists
        existing_dates = worksheet.col_values(1)
        row_index = None
        for i, val in enumerate(existing_dates):
            if val == date:
                row_index = i + 1
                break

        col_letter = _col_letter(len(COLUMN_HEADERS))
        if row_index:
            cell_range = f"A{row_index}:{col_letter}{row_index}"
            worksheet.update(cell_range, [row])
            print(f"  [Sheets] Updated row for {date} (row {row_index}).")
        else:
            worksheet.append_row(row, value_input_option="USER_ENTERED")
            print(f"  [Sheets] Added row for {date}.")

    def write_batch(self, rows_data):
        """Write multiple rows at once (more efficient for backfill)."""
        worksheet = self._get_worksheet()
        self.ensure_headers(worksheet)

        # Get existing dates to find where to start
        existing_dates = worksheet.col_values(1)
        existing_set = set(existing_dates)

        rows_to_append = []
        for data in rows_data:
            date = data.get("date", "")
            if date in existing_set:
                # Update in place
                for i, val in enumerate(existing_dates):
                    if val == date:
                        row_index = i + 1
                        col_letter = _col_letter(len(COLUMN_HEADERS))
                        worksheet.update(
                            f"A{row_index}:{col_letter}{row_index}",
                            [build_row(data)]
                        )
                        print(f"  [Sheets] Updated row for {date}.")
                        break
            else:
                rows_to_append.append(build_row(data))

        if rows_to_append:
            # Batch append all new rows
            next_row = len(existing_dates) + 1
            col_letter = _col_letter(len(COLUMN_HEADERS))
            cell_range = f"A{next_row}:{col_letter}{next_row + len(rows_to_append) - 1}"
            worksheet.update(cell_range, rows_to_append, value_input_option="USER_ENTERED")
            print(f"  [Sheets] Appended {len(rows_to_append)} rows.")


def _col_letter(n):
    """Convert 1-based column number to Excel-style letter (1=A, 27=AA, etc.)."""
    result = ""
    while n > 0:
        n, remainder = divmod(n - 1, 26)
        result = chr(65 + remainder) + result
    return result
