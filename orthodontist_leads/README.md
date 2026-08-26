# US Orthodontic & Dental Practice Lead Pipeline

Builds a nationwide list of US dental and orthodontic practices — practice
name, contact person, phone, full address, and the median household income of
the surrounding ZIP code and county — from public, no-API-key data sources.

## What it produces

| File | Rows | Contents |
| --- | --- | --- |
| `output/orthodontic_practices_usa.csv` | ~20,800 | Every practice location in the US with at least one licensed orthodontist |
| `output/orthodontic_practices_all_four_services.csv` | ~9,000 | The subset that also has a general dentist or prosthodontist on site, so the location plausibly covers **aligners + retainers + nightguards + dentures** |
| `output/all_dental_practices_usa.csv` | ~271,000 | Every US dental practice location (all specialties) |
| `output/orthodontic_practices_by_state.csv` | 55 | Per-state rollup: practice counts, field coverage, counties reached, median area income |

### Columns

`practice_name`, `dba_name`, `contact_person`, `contact_title`, `phone`,
`email`, `website`, `email_source`, `address_line1`, `address_line2`, `city`,
`state`, `zip_code`, `full_address`, `county`, `median_household_income`,
`median_household_income_zip`, `median_household_income_county`,
`income_level`, `is_orthodontic_practice`, `specialties`,
`service_invisalign`, `service_retainers`, `service_nightguards`,
`service_dentures`, `services_covered`, `providers_at_location`,
`provider_count`, `npi`, `npi_type`, `fax`, `address_shared_by_practices`,
`data_source`.

The four `service_*` columns are `yes` (core scope of a specialty present at
the location), `often` (commonly offered but not the defining scope), or blank.
They are inferred from the licensed specialties registered at the address, not
scraped from marketing pages — see *Accuracy notes*.

## Data sources

| Source | Used for | Licence |
| --- | --- | --- |
| [NPPES monthly data dissemination file](https://download.cms.gov/nppes/NPI_Files.html) (CMS) | Practice names, DBA names, authorized-official contact, phone, fax, full address, licensed specialty | US Government public domain |
| [ACS 5-year table-based summary files](https://www2.census.gov/programs-surveys/acs/summary_file/) (Census, table B19013) | Median household income by ZIP (ZCTA) and county | US Government public domain |
| [Census ZCTA↔county relationship files](https://www2.census.gov/geo/docs/maps-data/data/rel/) | ZIP → county assignment | US Government public domain |
| Practices' own public websites | Contact email addresses (optional step) | Crawled politely; see below |

Nothing here scrapes Google Maps, Yelp, or a directory whose terms forbid it.

## Usage

```bash
pip install -r requirements.txt

# Full build. Downloads ~1.2 GB on first run, then caches in raw/.
python run_pipeline.py

# Also write .xlsx copies of the smaller lists
python run_pipeline.py --xlsx

# Additionally crawl 2,000 practice websites for contact emails
python run_pipeline.py --enrich-emails 2000

# Or crawl separately - resumable, and safe to interrupt at any point
python crawl_websites.py            # appends to work/crawl_results.jsonl
python merge_crawl.py               # folds results into the CSV/XLSX outputs

# Restrict to the 50 states + DC (drops PR/GU/VI/MP)
python run_pipeline.py --no-territories
```

Run `python run_pipeline.py --help` for the full option list. Re-runs reuse
anything already in `--raw-dir`, so only the first build pays the download and
the ~3-minute scan of the 11.6 GB NPPES file.

## How practices are identified

NPPES enumerates *providers*, not practices, so records are rolled up by
normalised street address + ZIP:

* Each **organisation NPI** at an address becomes one practice row, with its
  registered authorized official as `contact_person`.
* Individual dentists at an address with **no** organisation NPI become solo
  practice rows.
* `providers_at_location` lists the individual dentists at that address with
  their specialties; `address_shared_by_practices` flags office buildings
  holding several registered organisations.

## Email addresses

NPPES has no email or website field, so these columns are filled from two
places and are **partial by design**:

1. **Registered NPPES endpoints** — a minority of practices register a public
   website or mailbox. Health-information-exchange Direct addresses
   (`…@direct.example.org`, Cerner/Epic routing endpoints) are discarded, since
   they are machine endpoints rather than an inbox anyone reads.
2. **The practice's own website** (`--enrich-emails N`) — candidate domains are
   generated from the practice name and from the patterns dental practices
   actually use (`smithorthodontics.com`, `drsmith.com`, `<city>braces.com`),
   DNS-filtered, then fetched. **A candidate is only accepted once the fetched
   page proves it belongs to the practice** — its registered phone number, or
   its ZIP plus city, has to appear in the page text. Unproven guesses are
   discarded rather than written to the file. The crawler identifies itself,
   honours `robots.txt`, rate-limits per host, and stops as soon as it finds an
   address.

Most dental practices publish a contact *form* rather than an email address, so
expect email coverage in the low tens of percent even after a full crawl. Phone
and postal address are complete; treat email as a bonus column.

## Field confidence

Not every column is equally trustworthy. Measured on the 20,824-row
orthodontic list:

**Registry facts — verified against CMS, 100% filled**

`practice_name`, `phone`, `address_line1`, `city`, `state`, `zip_code`,
`specialties`, `npi`. Spot-checked against the live NPI registry API: name,
street, ZIP and phone matched 6/6 on random rows. `npi` is the join key
commercial enrichment vendors match on.

**Solid, with a caveat**

| Column | Fill | Caveat |
| --- | --- | --- |
| `county`, `median_household_income*` | 99.5% | ACS 5-year median for the ZIP (county fallback). Describes the neighbourhood, not the practice's patients. CT county income is sparse - ACS moved CT to planning regions in 2022. |
| `contact_person` | 100% | Two different things. 14,039 are an organisation's registered authorized official - a real named person, but whoever signed the NPI paperwork, sometimes a corporate officer rather than the owner-dentist. 6,785 are solo practitioners, where it is the dentist. `npi_type` distinguishes them. |
| `providers_at_location` | 82.5% | Dentists at that street address. 33.4% of rows share an address with more than one registered practice (office buildings), flagged by `address_shared_by_practices`; those rows may list a neighbouring suite's dentists. |

**Inference, not observation — do not treat as fact**

The four `service_*` columns are derived from licensed specialties. No public
registry states which procedures an office actually performs. `service_
invisalign` and `service_retainers` read `yes` on every row, which only
restates "an orthodontist practises here" and carries no filtering signal -
**filter on `specialties` instead**.

**Sparse by nature**

`email` and `website` are partial and always will be; see *Email addresses*
above. Every address was read off a page that proved it belongs to the
practice, or was registered with CMS by the practice itself - check
`email_source`. Nothing is synthesised from an `info@<domain>` pattern.
`fax` is 52% because only half of practices register one.

## Accuracy notes

* **Specialty is licensure, not a service menu.** NPPES records the specialty a
  provider is enumerated under. A location with an orthodontist certainly does
  aligners and retainers; whether that specific office takes Invisalign cases
  or fabricates dentures in-house is not something any public registry states.
  The `service_*` columns are a well-grounded inference, not a confirmed
  service list — confirm before a high-value outreach push.
* **Dentures are not orthodontic work.** They are prosthodontic and general
  dentistry. `orthodontic_practices_all_four_services.csv` exists because of
  this: it keeps only orthodontic locations that also have a general dentist or
  prosthodontist on site.
* **Income is areal, not practice-level.** `median_household_income` is the ACS
  5-year median for the practice's ZIP code (falling back to its county), which
  describes the neighbourhood, not the practice's patients.
* **Connecticut county income is sparse.** ACS moved CT from counties to
  planning regions in 2022; CT rows carry a county name from the older vintage
  and may have a blank `median_household_income_county`. The ZIP-level figure
  is present and is what `median_household_income` uses.
* **NPPES lags reality.** Providers are supposed to keep their record current
  but some do not, so a small share of addresses and phones are stale. Counts
  are NPI enumerations, so a provider practising at two locations appears at
  both — which is usually what a location-based outreach list wants.

## Compliance

The output is business contact information for commercial entities. Contacting
these practices is subject to CAN-SPAM (commercial email), the TCPA and state
law (calls and texts, including the national and state Do-Not-Call registries),
and any applicable state anti-solicitation rules. Screening phone numbers
against DNC lists and honouring opt-outs is the sender's responsibility; this
pipeline does neither.
