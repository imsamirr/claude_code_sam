#!/usr/bin/env python3
"""Build a US dental / orthodontic practice lead list.

Sources (all public, no API key required):
  * NPPES monthly data dissemination file (CMS) - practices, contacts, phones,
    addresses, provider specialties.
  * ACS 5-year table-based summary files (US Census Bureau) - median household
    income by ZIP code and by county.
  * The practices' own public websites - contact email addresses (optional).

Usage:
    python run_pipeline.py --help
    python run_pipeline.py                      # full build, no web crawling
    python run_pipeline.py --enrich-emails 500  # crawl the top 500 practices
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))

from pipeline import build, census, nppes
from pipeline.config import DEFAULT_OUT_DIR, DEFAULT_RAW_DIR, ORTHODONTIST_CODE


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--raw-dir", type=Path, default=DEFAULT_RAW_DIR,
                   help="where source downloads are cached")
    p.add_argument("--out-dir", type=Path, default=DEFAULT_OUT_DIR,
                   help="where the CSV outputs are written")
    p.add_argument("--nppes-zip", type=Path, default=None,
                   help="use an already-downloaded NPPES zip instead of fetching one")
    p.add_argument("--filtered-csv", type=Path, default=None,
                   help="reuse a previously extracted dental subset CSV")
    p.add_argument("--enrich-emails", type=int, default=0, metavar="N",
                   help="crawl N practice websites for contact emails (0 = skip)")
    p.add_argument("--enrich-workers", type=int, default=8)
    p.add_argument("--enrich-delay", type=float, default=1.0,
                   help="minimum seconds between requests to the same host")
    p.add_argument("--no-territories", action="store_true",
                   help="restrict to the 50 states + DC")
    p.add_argument("--xlsx", action="store_true",
                   help="also write .xlsx copies of the smaller lists")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    args.raw_dir.mkdir(parents=True, exist_ok=True)
    args.out_dir.mkdir(parents=True, exist_ok=True)
    session = requests.Session()
    t0 = time.time()

    # 1. NPPES ---------------------------------------------------------------
    filtered = args.filtered_csv or (args.raw_dir / "dental_nppes.csv")
    zip_path = args.nppes_zip
    if not filtered.exists():
        if zip_path is None:
            url = nppes.find_monthly_file_url(session)
            print(f"[1/4] Downloading NPPES monthly file: {url}")
            zip_path = nppes.download(url, args.raw_dir / Path(url).name, session)
        print(f"[1/4] Filtering dental providers out of {zip_path.name} ...")
        stats = nppes.extract(zip_path, filtered, include_territories=not args.no_territories)
        print(f"      {stats.kept:,} active US dental NPIs from {stats.rows_read:,} rows")
    else:
        print(f"[1/4] Reusing filtered dental subset: {filtered}")
        if zip_path is None:
            guess = sorted(args.raw_dir.glob("*.zip"))
            zip_path = guess[0] if guess else None

    rows = build.load_rows(filtered)
    print(f"      loaded {len(rows):,} dental NPI records")

    # 2. Roll up into practices ---------------------------------------------
    print("[2/4] Rolling records up into practices ...")
    practices = build.build_practices(rows)
    print(f"      {len(practices):,} practice records")

    # 3. Census income -------------------------------------------------------
    print("[3/4] Attaching Census median household income ...")
    lookup = census.IncomeLookup(args.raw_dir, session)
    build.attach_income(practices, lookup)

    # 3b. Emails / websites already registered with NPPES ---------------------
    if zip_path and zip_path.exists():
        from pipeline import enrich as _enrich
        anchors = {p["npi"] for p in practices}
        print("[3/4] Reading registered NPPES endpoints for emails and websites ...")
        endpoints = nppes.load_endpoints(zip_path, anchors)
        hits = 0
        by_npi = {p["npi"]: p for p in practices}
        for npi, eps in endpoints.items():
            rec = by_npi.get(npi)
            if not rec:
                continue
            contacts = _enrich.endpoint_contacts(eps)
            if contacts["email"] or contacts["website"]:
                rec["email"] = contacts["email"]
                rec["website"] = contacts["website"]
                rec["email_source"] = "nppes-registered-endpoint"
                hits += 1
        print(f"      {hits:,} practices matched a registered endpoint")

    ortho = [p for p in practices if p["is_orthodontic_practice"] == "yes"]
    # Orthodontic practices that also cover dentures - i.e. an orthodontist plus
    # a general dentist or prosthodontist at the same location. This is the
    # tightest match for "does aligners, retainers, nightguards AND dentures".
    ortho_four = [p for p in ortho if p["services_covered"] == 4]

    # 4. Optional email enrichment ------------------------------------------
    if args.enrich_emails:
        from pipeline import enrich
        targets = sorted(
            [p for p in ortho if not p["email"]],
            key=lambda r: (-(int(r["median_household_income"] or 0)),
                           -int(r["provider_count"] or 0)),
        )[: args.enrich_emails]
        print(f"[4/4] Crawling {len(targets)} practice websites for contact emails ...")
        results = enrich.enrich_many(targets, workers=args.enrich_workers,
                                     min_delay=args.enrich_delay)
        by_npi = {p["npi"]: p for p in practices}
        for npi, res in results.items():
            rec = by_npi.get(npi)
            if rec and res.website and not rec["email"]:
                rec["website"] = res.website
                rec["email"] = res.emails
                rec["email_source"] = f"{res.source} ({res.verified})" if res.verified else res.source
        found = sum(1 for r in results.values() if r.emails)
        print(f"      {found} practices with a public email address")
    else:
        print("[4/4] Email enrichment skipped (--enrich-emails 0)")

    # Write ------------------------------------------------------------------
    outputs = {
        "orthodontic_practices_usa.csv": ortho,
        "orthodontic_practices_all_four_services.csv": ortho_four,
        "all_dental_practices_usa.csv": practices,
    }
    summary = {}
    for name, data in outputs.items():
        path = args.out_dir / name
        build.write_csv(data, path)
        summary[name] = len(data)
        print(f"      wrote {len(data):>7,} rows -> {path}")
        if args.xlsx and len(data) <= 500_000:
            from pipeline.export import csv_to_xlsx
            xlsx = path.with_suffix(".xlsx")
            csv_to_xlsx(path, xlsx, sheet_name=path.stem[:31])
            print(f"      wrote {len(data):>7,} rows -> {xlsx}")

    summary["elapsed_seconds"] = round(time.time() - t0, 1)
    (args.out_dir / "summary.json").write_text(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
