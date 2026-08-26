"""Fold website-crawl results back into the published CSV/XLSX outputs.

Reads ``work/crawl_results.jsonl`` (written incrementally by a crawl run) and
fills the empty ``website`` / ``email`` columns in the generated lists. Safe to
run repeatedly and against a partial crawl - existing values are never
overwritten, so each run only adds what the crawl has found so far.
"""
from __future__ import annotations

import csv
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from pipeline.enrich import EMAIL_BLOCKLIST
from pipeline.export import csv_to_xlsx
from pipeline.summarise import state_summary


def clean_emails(value: str) -> str:
    """Re-apply the placeholder blocklist to emails recorded by a crawl.

    The raw crawl log is left untouched; filtering here means results captured
    before a blocklist change still get cleaned on the next merge.
    """
    kept = [e.strip() for e in (value or "").split(";") if e.strip()
            and not EMAIL_BLOCKLIST.search(e.strip().lower())]
    return "; ".join(dict.fromkeys(kept))

BASE = Path(__file__).resolve().parent
OUT = BASE / 'output'
JSONL = BASE / 'work' / 'crawl_results.jsonl'

crawled = {}
if JSONL.exists():
    for line in open(JSONL):
        try:
            d = json.loads(line)
        except Exception:
            continue
        if d.get('website'):
            crawled[d['npi']] = d
print(f"{len(crawled):,} verified practice websites from the crawl")

targets = ['orthodontic_practices_usa.csv',
           'orthodontic_practices_all_four_services.csv',
           'all_dental_practices_usa.csv']
for name in targets:
    path = OUT / name
    if not path.exists():
        continue
    rows = list(csv.DictReader(open(path, newline='', encoding='utf-8')))
    fields = list(rows[0].keys())
    added_site = added_mail = 0
    for r in rows:
        if r['email'].strip():
            cleaned = clean_emails(r['email'])
            if cleaned != r['email']:
                r['email'] = cleaned
                if not cleaned:
                    r['email_source'] = ''

        hit = crawled.get(r['npi'])
        if not hit:
            continue
        if not r['website'].strip():
            r['website'] = hit['website']
            added_site += 1
        emails = clean_emails(hit.get('emails', ''))
        if not r['email'].strip() and emails:
            r['email'] = emails
            r['email_source'] = f"website-crawl ({hit.get('verified','')})"
            added_mail += 1
    with open(path, 'w', newline='', encoding='utf-8') as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader(); w.writerows(rows)
    total_mail = sum(1 for r in rows if r['email'].strip())
    total_site = sum(1 for r in rows if r['website'].strip())
    print(f"  {name}: +{added_site:,} websites, +{added_mail:,} emails  "
          f"(now {total_site:,} websites / {total_mail:,} emails of {len(rows):,})")
    if len(rows) <= 100_000:
        csv_to_xlsx(path, path.with_suffix('.xlsx'), sheet_name=path.stem[:31])

state_summary(OUT / 'orthodontic_practices_usa.csv',
              OUT / 'orthodontic_practices_by_state.csv')
os.system(f"gzip -9 -f -k {OUT / 'all_dental_practices_usa.csv'}")
print("merged, xlsx + state rollup + gzip refreshed")
