# Setup Guide — Daily Financial Metrics Automation

This guide walks you through every step to connect TripleWhale, Shopify, and
Google Sheets so your financial metrics get pulled automatically every day.

**Time needed:** About 30–45 minutes (one-time setup).

---

## Table of Contents

1. [Install Python](#step-1-install-python)
2. [Download this project](#step-2-download-this-project)
3. [Install dependencies](#step-3-install-dependencies)
4. [Set up Google Sheets API](#step-4-set-up-google-sheets-api)
5. [Set up Shopify API access](#step-5-set-up-shopify-api-access)
6. [Set up TripleWhale API access](#step-6-set-up-triplewhale-api-access)
7. [Configure the .env file](#step-7-configure-the-env-file)
8. [Run your first test](#step-8-run-your-first-test)
9. [Set up daily automation](#step-9-set-up-daily-automation)
10. [Troubleshooting](#troubleshooting)

---

## Step 1: Install Python

You need Python 3.9 or later.

### On Mac:
1. Open **Terminal** (search for "Terminal" in Spotlight)
2. Type: `python3 --version`
3. If it shows 3.9 or higher, you're good! Skip to Step 2.
4. If not, go to https://www.python.org/downloads/ and download the latest version
5. Run the installer and follow the prompts

### On Windows:
1. Go to https://www.python.org/downloads/
2. Click "Download Python 3.x.x"
3. **IMPORTANT:** Check the box that says "Add Python to PATH" during installation
4. Run the installer

---

## Step 2: Download This Project

If you haven't already, download or clone this project to your computer:

```bash
git clone <your-repo-url>
cd claude_code_sam
```

---

## Step 3: Install Dependencies

Open Terminal (Mac) or Command Prompt (Windows), navigate to the project folder,
and run:

```bash
# Create a virtual environment (keeps things clean)
python3 -m venv venv

# Activate it:
# On Mac/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install the required packages:
pip install -r requirements.txt
```

You should see packages being downloaded. When it's done, you're ready for the
API setup.

---

## Step 4: Set Up Google Sheets API

This is the most involved step, but just follow along:

### 4a. Create a Google Cloud Project

1. Go to https://console.cloud.google.com/
2. Sign in with your Google account
3. Click the project dropdown at the top → **"New Project"**
4. Name it something like "Financial Metrics Automation"
5. Click **Create**
6. Make sure your new project is selected in the dropdown

### 4b. Enable the Google Sheets API

1. In the Google Cloud Console, go to **APIs & Services** → **Library**
   (or search for "APIs & Services" in the search bar)
2. Search for **"Google Sheets API"**
3. Click on it → Click **Enable**
4. Go back to the Library and also search for and enable **"Google Drive API"**

### 4c. Create a Service Account

1. Go to **APIs & Services** → **Credentials**
2. Click **"+ CREATE CREDENTIALS"** → **"Service Account"**
3. Name: "sheets-automation" (or anything you like)
4. Click **Create and Continue**
5. For the role, select **"Editor"** → click **Continue**
6. Click **Done**

### 4d. Download the JSON Key

1. On the Credentials page, click on the service account you just created
2. Go to the **"Keys"** tab
3. Click **"Add Key"** → **"Create New Key"**
4. Choose **JSON** → Click **Create**
5. A file will download — this is your credentials file!
6. **Rename it** to `google_credentials.json`
7. **Move it** into the `config/` folder in this project

### 4e. Share Your Google Sheet

1. Open your Google Sheet where you want the data
2. Copy the **Sheet ID** from the URL. It's the long string between `/d/` and `/edit`:
   ```
   https://docs.google.com/spreadsheets/d/THIS_IS_YOUR_SHEET_ID/edit
   ```
3. Click the **Share** button in your Google Sheet
4. In the credentials JSON file you downloaded, find the `"client_email"` field
   (it looks like: `sheets-automation@your-project.iam.gserviceaccount.com`)
5. **Share your sheet with that email address** and give it **Editor** access
6. Click Send (uncheck "Notify people" if asked)

---

## Step 5: Set Up Shopify API Access

### 5a. Create a Custom App in Shopify

1. Log in to your **Shopify Admin** panel
2. Go to **Settings** (bottom left) → **Apps and sales channels**
3. Click **"Develop apps"** (you may need to click "Allow custom app development" first)
4. Click **"Create an app"**
5. Name it: "Financial Metrics Sync" (or anything you like)
6. Click **Create app**

### 5b. Set API Permissions

1. Click **"Configure Admin API scopes"**
2. Search for and check these permissions:
   - `read_orders`
   - `read_products`
   - `read_inventory`
   - `read_customers`
   - `read_analytics`
3. Click **Save**

### 5c. Install and Get Your Token

1. Click the **"API credentials"** tab
2. Click **"Install app"** → Confirm
3. You'll see your **Admin API access token** — copy it immediately!
   (You can only see it once — if you lose it, you'll need to create a new app)
4. Your store URL is: `your-store-name.myshopify.com`

---

## Step 6: Set Up TripleWhale API Access

1. Log in to your **TripleWhale** dashboard
2. Go to **Settings** → **API** (or **Integrations** → **API**)
3. Click **"Generate API Key"** or **"Create New Key"**
4. Name it: "Google Sheets Sync"
5. Copy the API key

> **Note:** If you don't see an API section, you may need to contact TripleWhale
> support to enable API access on your plan. Enterprise and Growth plans typically
> include API access.

---

## Step 7: Configure the .env File

1. In the project folder, find the file `.env.example`
2. **Copy it** and rename the copy to `.env`
   ```bash
   cp .env.example .env
   ```
3. Open `.env` in any text editor (Notepad, TextEdit, VS Code, etc.)
4. Fill in your values:

```
TRIPLEWHALE_API_KEY=paste_your_triplewhale_key_here
SHOPIFY_STORE_URL=your-store-name.myshopify.com
SHOPIFY_ACCESS_TOKEN=paste_your_shopify_token_here
GOOGLE_CREDENTIALS_PATH=config/google_credentials.json
GOOGLE_SHEET_ID=paste_your_sheet_id_here
GOOGLE_SHEET_TAB_NAME=Daily Metrics
```

**Important:** No quotes around the values, no spaces around the `=` sign.

---

## Step 8: Run Your First Test

Now let's make sure everything works!

```bash
# Make sure your virtual environment is active:
# Mac/Linux:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# Pull yesterday's data:
python src/main.py
```

You should see output like:
```
==================================================
Processing date: 2025-01-15
==================================================
[1/3] Fetching TripleWhale metrics...
  Ad Spend: $1234.56
  Blended ROAS: 3.2
[2/3] Fetching Shopify metrics...
  Gross Revenue: $5678.90
  Total Orders: 42
[3/3] Writing to Google Sheets...
[Sheets] Added new row for 2025-01-15.
Done for 2025-01-15!
```

Check your Google Sheet — you should see a new row with all the data!

### Other useful commands:

```bash
# Pull data for a specific date:
python src/main.py --date 2025-01-10

# Backfill a range of dates:
python src/main.py --from 2025-01-01 --to 2025-01-31
```

---

## Step 9: Set Up Daily Automation

### Option A: Built-in Scheduler (simplest)

Run this command and leave it running:

```bash
python src/main.py --schedule 08:00
```

This will pull yesterday's data every day at 8:00 AM. But your computer needs
to stay on, and you need to keep this terminal open.

### Option B: Cron Job (Mac/Linux — recommended)

This runs automatically in the background even if you close the terminal:

```bash
# Run the setup helper:
bash schedule_daily.sh
```

Or set it up manually:
1. Open your terminal
2. Type: `crontab -e`
3. Add this line (change the path to match your project location):
   ```
   0 8 * * * cd /path/to/claude_code_sam && /path/to/claude_code_sam/venv/bin/python src/main.py >> logs/daily_run.log 2>&1
   ```
4. Save and exit

### Option C: Task Scheduler (Windows)

1. Open **Task Scheduler** (search for it in the Start menu)
2. Click **"Create Basic Task"**
3. Name: "Daily Metrics Sync"
4. Trigger: **Daily**, set your preferred time (e.g., 8:00 AM)
5. Action: **Start a Program**
6. Program: `C:\path\to\claude_code_sam\venv\Scripts\python.exe`
7. Arguments: `src\main.py`
8. Start in: `C:\path\to\claude_code_sam`
9. Click Finish

---

## Troubleshooting

### "Missing required environment variables"
→ Make sure you copied `.env.example` to `.env` and filled in all values.

### "Google Sheets: Permission denied"
→ Make sure you shared your Google Sheet with the service account email
  (found in `google_credentials.json` under `client_email`).

### "Shopify: 401 Unauthorized"
→ Your access token may be wrong or expired. Create a new custom app in Shopify.

### "TripleWhale: 401 or 403 error"
→ Check that your API key is correct and that your plan includes API access.

### "No data returned for a date"
→ The date might be too recent (today's data isn't available yet) or too old.
  TripleWhale and Shopify may have different data retention limits.

### "ModuleNotFoundError: No module named 'gspread'"
→ Make sure you activated the virtual environment:
  `source venv/bin/activate` (Mac/Linux) or `venv\Scripts\activate` (Windows)

---

## What Gets Written to Your Sheet

Each row contains one day of data with these columns:

| Column | Source | Description |
|--------|--------|-------------|
| Date | — | The date (YYYY-MM-DD) |
| Gross Revenue | Shopify | Total revenue before deductions |
| Net Revenue | Shopify | Revenue after refunds and discounts |
| Subtotal | Shopify | Revenue before shipping and tax |
| Total Orders | Shopify | Number of orders |
| Avg Order Value | Shopify | Average order value |
| Total Discounts | Shopify | Total discount amount |
| Total Shipping | Shopify | Shipping charges collected |
| Total Tax | Shopify | Tax collected |
| Refund Amount | Shopify | Total refunds issued |
| Items Sold | Shopify | Total items sold |
| New Customer Orders | Shopify | Orders from first-time buyers |
| Returning Customer Orders | Shopify | Orders from repeat buyers |
| Total Ad Spend | TripleWhale | Combined ad spend across all platforms |
| Facebook Spend | TripleWhale | Facebook/Meta ad spend |
| Google Spend | TripleWhale | Google Ads spend |
| TikTok Spend | TripleWhale | TikTok ad spend |
| Other Spend | TripleWhale | Other platform ad spend |
| Blended ROAS | TripleWhale | Return on ad spend (all platforms) |
| Blended CPA | TripleWhale | Cost per acquisition |
| Blended CAC | TripleWhale | Customer acquisition cost |
| TW New Customers | TripleWhale | New customers (TW attribution) |
| TW Returning Customers | TripleWhale | Returning customers (TW attribution) |
| Pixel Revenue | TripleWhale | Revenue attributed via TW pixel |
| Pixel ROAS | TripleWhale | ROAS based on TW pixel data |
| Net Profit (Rev - Ads) | Calculated | Net Revenue minus Total Ad Spend |
| Ad Spend % of Revenue | Calculated | Ad spend as % of net revenue |
