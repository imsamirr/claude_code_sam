#!/usr/bin/env python3
"""Crawl practice websites for contact emails, resumably.

Reads a generated list, works through every practice that does not already
have an email, and appends one JSON object per practice to
``work/crawl_results.jsonl``. The run can be interrupted and restarted at any
time - practices already present in the results file are skipped. Fold the
results back into the CSV/XLSX outputs with ``merge_crawl.py``.

Usage:
    python crawl_websites.py                       # the orthodontic list
    python crawl_websites.py --limit 2000          # just the first 2,000
    python crawl_websites.py --source output/all_dental_practices_usa.csv
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from pipeline import enrich

BASE = Path(__file__).resolve().parent
csv.field_size_limit(10_000_000)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--source", type=Path,
                   default=BASE / "output" / "orthodontic_practices_usa.csv")
    p.add_argument("--results", type=Path, default=BASE / "work" / "crawl_results.jsonl")
    p.add_argument("--workers", type=int, default=64,
                   help="concurrent practices; each host is still rate-limited")
    p.add_argument("--delay", type=float, default=0.5,
                   help="minimum seconds between requests to the same host")
    p.add_argument("--max-probes", type=int, default=5,
                   help="candidate domains actually fetched per practice")
    p.add_argument("--limit", type=int, default=0, help="stop after N practices")
    return p.parse_args()


def add_surnames(row: dict) -> dict:
    """Recover provider surnames from the rendered provider list."""
    names = [p.split(" (")[0] for p in row.get("providers_at_location", "").split("; ") if p]
    if not names and row.get("contact_person"):
        names = [row["contact_person"]]
    surnames = []
    for name in names[:3]:
        bare = name.split(",")[0].strip()
        if bare:
            surnames.append(bare.split()[-1])
    row["_surnames"] = surnames
    return row


def main() -> int:
    args = parse_args()
    args.results.parent.mkdir(parents=True, exist_ok=True)

    with open(args.source, newline="", encoding="utf-8") as fh:
        rows = [add_surnames(r) for r in csv.DictReader(fh)]

    done: set[str] = set()
    if args.results.exists():
        with open(args.results, encoding="utf-8") as fh:
            for line in fh:
                try:
                    done.add(json.loads(line)["npi"])
                except (ValueError, KeyError):
                    continue

    todo = [r for r in rows if r["npi"] not in done and not r.get("email", "").strip()]
    if args.limit:
        todo = todo[: args.limit]
    print(f"{len(rows):,} practices, {len(done):,} already crawled, {len(todo):,} to go",
          flush=True)
    if not todo:
        return 0

    polite = enrich.Politeness(min_delay=args.delay)
    lock = threading.Lock()
    counter = {"n": 0, "sites": 0, "emails": 0}
    t0 = time.time()

    def work(rec: dict) -> enrich.SiteResult:
        try:
            return enrich.SiteEnricher(polite, max_probes=args.max_probes).enrich(rec)
        except Exception:
            return enrich.SiteResult(rec["npi"])

    with open(args.results, "a", encoding="utf-8") as out:
        with ThreadPoolExecutor(max_workers=args.workers) as pool:
            futures = {pool.submit(work, r): r for r in todo}
            for fut in as_completed(futures):
                rec = futures[fut]
                try:
                    res = fut.result()
                except Exception:
                    res = enrich.SiteResult(rec["npi"])
                with lock:
                    out.write(json.dumps({
                        "npi": rec["npi"], "website": res.website,
                        "emails": res.emails, "source": res.source,
                        "verified": res.verified,
                    }) + "\n")
                    counter["n"] += 1
                    counter["sites"] += bool(res.website)
                    counter["emails"] += bool(res.emails)
                    if counter["n"] % 250 == 0:
                        out.flush()
                        rate = counter["n"] / max(time.time() - t0, 1)
                        eta = (len(todo) - counter["n"]) / max(rate, 0.01) / 60
                        print(f"  {counter['n']:,}/{len(todo):,} | sites {counter['sites']:,}"
                              f" | emails {counter['emails']:,} | {rate:.1f}/s"
                              f" | ETA {eta:.0f}m", flush=True)
    print(json.dumps(counter), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
