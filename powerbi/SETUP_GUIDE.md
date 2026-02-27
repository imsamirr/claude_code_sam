# Power BI Report Setup Guide — Performance Marketing Dashboard

## Quick Start

### Step 1: Import Data Sources

Open Power BI Desktop → **Get Data** → **Text/CSV** and import these files:

| File | Description |
|------|-------------|
| `data/powerbi/daily_kpis.csv` | Blended daily KPIs (revenue, spend, MER, AOV, etc.) |
| `data/powerbi/platform_daily.csv` | Per-platform daily metrics (spend, ROAS, CPA by platform) |
| `data/powerbi/dim_date.csv` | Date dimension table for time intelligence |
| `data/powerbi/creative_performance.csv` | Daily ad-level performance (Meta Ads — when connected) |
| `data/powerbi/creative_summary.csv` | Creative aggregate analysis (Meta Ads — when connected) |

### Step 2: Set Up Relationships

In **Model View**, create these relationships:

```
dim_date[date]  ──1:M──  daily_kpis[date]
dim_date[date]  ──1:M──  platform_daily[date]
dim_date[date]  ──1:M──  creative_performance[date]  (when available)
```

### Step 3: Create DAX Measures

Create a new Measures table (**Modeling** → **New Table** → `Measures = {BLANK()}`), then add these measures:

---

## DAX Measures

### Executive KPIs

```dax
// Revenue
Total Revenue = SUM(daily_kpis[gross_sales])
Net Revenue = SUM(daily_kpis[net_revenue])
Total Orders = SUM(daily_kpis[orders])
AOV = DIVIDE([Total Revenue], [Total Orders], 0)

// Spend & Efficiency
Total Ad Spend = SUM(daily_kpis[total_ad_spend])
MER = DIVIDE([Total Ad Spend], [Total Revenue], 0) * 100
Blended ROAS = DIVIDE([Total Revenue], [Total Ad Spend], 0)

// Profitability
Total COGS = SUM(daily_kpis[cogs])
Total Margin = SUM(daily_kpis[margin])
Gross Margin % = DIVIDE([Total Margin], [Net Revenue], 0) * 100

// Acquisition
Blended CAC = DIVIDE([Total Ad Spend], [Total Orders], 0)
New Customer CAC = DIVIDE([Total Ad Spend], SUM(daily_kpis[new_customer_orders]), 0)
```

### Conversion Funnel

```dax
Total Sessions = SUM(daily_kpis[sessions])
CVR = DIVIDE([Total Orders], [Total Sessions], 0) * 100
ATC Rate = AVERAGE(daily_kpis[atc_pct])

// Cost per Session
CPS = DIVIDE([Total Ad Spend], [Total Sessions], 0)
```

### Customer Metrics

```dax
New Customer Orders = SUM(daily_kpis[new_customer_orders])
New Customer Revenue = SUM(daily_kpis[new_customers_revenue])
Returning Customer Orders = SUM(daily_kpis[returning_customers_count])
Returning Customer Revenue = SUM(daily_kpis[returning_customers_revenue])
New Customer % = DIVIDE([New Customer Orders], [Total Orders], 0) * 100
```

### Platform Metrics

```dax
Platform Spend = SUM(platform_daily[spend])
Platform ROAS = DIVIDE(
    SUMX(platform_daily, platform_daily[spend] * platform_daily[roas]),
    [Platform Spend], 0
)
Platform CPA = AVERAGE(platform_daily[cpa])
Platform CPM = AVERAGE(platform_daily[cpm])
Platform CTR = AVERAGE(platform_daily[ctr])
Platform CPC = AVERAGE(platform_daily[cpc])

// Spend Share
Spend Share % = DIVIDE(
    [Platform Spend],
    CALCULATE([Platform Spend], ALL(platform_daily[platform])),
    0
) * 100
```

### Trending / Time Intelligence

```dax
Revenue 7d Avg =
AVERAGEX(
    DATESINPERIOD(dim_date[date], MAX(dim_date[date]), -7, DAY),
    CALCULATE(SUM(daily_kpis[gross_sales]))
)

Spend 7d Avg =
AVERAGEX(
    DATESINPERIOD(dim_date[date], MAX(dim_date[date]), -7, DAY),
    CALCULATE(SUM(daily_kpis[total_ad_spend]))
)

Revenue WoW Change =
VAR CurrentWeek = [Total Revenue]
VAR PriorWeek = CALCULATE([Total Revenue], DATEADD(dim_date[date], -7, DAY))
RETURN DIVIDE(CurrentWeek - PriorWeek, PriorWeek, 0) * 100

MER 7d Avg = DIVIDE([Spend 7d Avg], [Revenue 7d Avg], 0) * 100
```

### Creative Analysis (when Meta Ads connected)

```dax
// Creative Win Rate — % of creatives that reached $1K spend
Total Creatives = COUNTROWS(creative_summary)
Creatives Over 1K = CALCULATE(COUNTROWS(creative_summary), creative_summary[hit_1k_spend] = "Yes")
Creative Win Rate = DIVIDE([Creatives Over 1K], [Total Creatives], 0) * 100

// Creative Graduation Rates
Creatives Over 5K = CALCULATE(COUNTROWS(creative_summary), creative_summary[hit_5k_spend] = "Yes")
Creatives Over 10K = CALCULATE(COUNTROWS(creative_summary), creative_summary[hit_10k_spend] = "Yes")
Graduation Rate 5K = DIVIDE([Creatives Over 5K], [Total Creatives], 0) * 100
Graduation Rate 10K = DIVIDE([Creatives Over 10K], [Total Creatives], 0) * 100

// Top Creative ROAS
Avg Creative ROAS = AVERAGE(creative_summary[roas])
Avg Creative CPA = AVERAGE(creative_summary[cpa])
```

---

## Report Pages

### Page 1: Executive Dashboard
- **KPI Cards**: Revenue, Spend, MER, ROAS, Orders, AOV
- **Line Chart**: Revenue vs Spend (daily, with 7d moving average)
- **Gauge**: MER target (aim for <50%)
- **Card**: Gross Margin %

### Page 2: Platform Performance
- **Stacked Bar**: Spend by Platform (daily)
- **Table**: Platform | Spend | ROAS | CPA | CTR | CPC | Spend Share %
- **Donut Chart**: Spend distribution by platform
- **Line Chart**: Platform ROAS trends over time

### Page 3: Conversion Funnel
- **Funnel**: Sessions → ATC → Checkout → Orders
- **Line Chart**: CVR trend (daily)
- **KPI Cards**: Sessions, CVR, ATC%, CAC, nCAC
- **Bar Chart**: New vs Returning customer revenue

### Page 4: Creative Analysis (Meta Ads)
- **KPI Cards**: Total Creatives, Win Rate ($1K), Graduation Rate ($5K)
- **Bar Chart**: Spend tier distribution (Under $100 / $100-$500 / $500-$1K / $1K-$5K / $5K+)
- **Table**: Top 20 creatives by spend (Ad Name, Spend, ROAS, CPA, Days Active)
- **Scatter Plot**: Spend vs ROAS (bubble size = purchases)
- **Line Chart**: Creative daily spend trend for top performers

### Page 5: Creative Deep Dive
- **Slicer**: Campaign Name, Spend Tier, Date Range
- **Matrix**: Campaign → AdSet → Ad with Spend, ROAS, CPA
- **Waterfall**: Creative spend accumulation over time
- **Table**: Creatives that hit $1K spend — how many days did it take?

---

## Refreshing Data

To update the report with fresh data, re-run the export script:

```bash
# Platform data only (TripleWhale)
python src/powerbi_export.py --from 2025-12-30 --to 2026-02-27

# With Meta Ads creative data
python src/powerbi_export.py --from 2025-12-30 --to 2026-02-27 --meta
```

Then in Power BI: **Home** → **Refresh**.

---

## Connecting Meta Ads

Once you have your Meta App set up:

1. Add to `.env`:
   ```
   META_ACCESS_TOKEN=your_token_here
   META_AD_ACCOUNT_ID=act_XXXXXXXXX
   ```

2. Re-run export with `--meta` flag:
   ```bash
   python src/powerbi_export.py --from 2025-12-30 --to 2026-02-27 --meta
   ```

3. Import `creative_performance.csv` and `creative_summary.csv` into Power BI
4. Add the Creative Analysis DAX measures
5. Build Pages 4 & 5
