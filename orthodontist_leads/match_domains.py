#!/usr/bin/env python3
"""Fetch harvested dental domains and match them to practices by phone number.

The inverse of guessing a domain from a practice's name: take a list of real
dental domains (see ``harvest_domains.py``), fetch each one once, read the
phone numbers and email addresses off the page, and look the phones up in an
index built from the practice list. A phone number identifies a location
exactly, so a hit is proof the site belongs to that practice.

A chain site legitimately carries many locations' phone numbers and will match
each of them. A directory or aggregator would match hundreds, so any domain
matching more than ``--max-matches`` practices is discarded rather than
allowed to smear one generic address across the file.

Results are appended to ``work/domain_matches.jsonl`` and the run is
resumable: domains already recorded are skipped.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import threading
import time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from pipeline import enrich

BASE = Path(__file__).resolve().parent
csv.field_size_limit(10_000_000)

# North American numbers as they appear in page text, in any common format.
PHONE_RE = re.compile(r"(?:\+?1[\s.\-]?)?\(?([2-9]\d{2})\)?[\s.\-]?(\d{3})[\s.\-]?(\d{4})")


def parse_args() -> argparse.Namespace:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--domains", type=Path, default=BASE / "work" / "cc_dental_domains.txt")
    ap.add_argument("--practices", type=Path,
                    default=BASE / "output" / "all_dental_practices_usa.csv")
    ap.add_argument("--results", type=Path, default=BASE / "work" / "domain_matches.jsonl")
    ap.add_argument("--workers", type=int, default=64)
    ap.add_argument("--delay", type=float, default=0.5)
    ap.add_argument("--max-matches", type=int, default=60,
                    help="discard a domain matching more practices than this")
    ap.add_argument("--limit", type=int, default=0)
    return ap.parse_args()


def load_phone_index(path: Path) -> dict[str, list[str]]:
    """Map a 10-digit phone number to the NPIs of practices that registered it."""
    index: dict[str, list[str]] = defaultdict(list)
    with open(path, newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            digits = re.sub(r"\D", "", row.get("phone", ""))[-10:]
            if len(digits) == 10:
                index[digits].append(row["npi"])
    return index


def phones_on_page(text: str) -> set[str]:
    return {"".join(m) for m in PHONE_RE.findall(text or "")}


def main() -> int:
    args = parse_args()
    args.results.parent.mkdir(parents=True, exist_ok=True)

    domains = [d.strip() for d in args.domains.read_text().split() if d.strip()]
    print(f"loading phone index from {args.practices.name} ...", flush=True)
    index = load_phone_index(args.practices)
    print(f"  {len(index):,} distinct practice phone numbers", flush=True)

    done: set[str] = set()
    if args.results.exists():
        with open(args.results, encoding="utf-8") as fh:
            for line in fh:
                try:
                    done.add(json.loads(line)["domain"])
                except (ValueError, KeyError):
                    continue
    todo = [d for d in domains if d not in done]
    if args.limit:
        todo = todo[: args.limit]
    print(f"{len(domains):,} domains, {len(done):,} already fetched, {len(todo):,} to go",
          flush=True)
    if not todo:
        return 0

    polite = enrich.Politeness(min_delay=args.delay)
    lock = threading.Lock()
    counter = {"n": 0, "reachable": 0, "matched": 0, "practices": 0, "emails": 0}
    t0 = time.time()

    def work(domain: str) -> dict:
        site = enrich.SiteEnricher(polite, max_pages=3)
        url = html = ""
        for host in (domain, "www." + domain):
            if not enrich.resolves(host):
                continue
            html = site._get("https://" + host)
            if html:
                url = "https://" + host
                break
        if not html:
            return {"domain": domain, "url": "", "npis": [], "emails": ""}

        text = html
        contact_urls = site._contact_urls(url, html)[:2]
        for c in contact_urls:
            extra = site._get(c)
            if extra:
                text += "\n" + extra

        found = phones_on_page(text)
        npis: list[str] = []
        for digits in found:
            npis.extend(index.get(digits, ()))
        emails = enrich.extract_emails(text, domain)
        return {"domain": domain, "url": url, "npis": sorted(set(npis)),
                "emails": "; ".join(emails)}

    with open(args.results, "a", encoding="utf-8") as out:
        with ThreadPoolExecutor(max_workers=args.workers) as pool:
            futures = {pool.submit(work, d): d for d in todo}
            for fut in as_completed(futures):
                domain = futures[fut]
                try:
                    rec = fut.result()
                except Exception:
                    rec = {"domain": domain, "url": "", "npis": [], "emails": ""}
                if len(rec["npis"]) > args.max_matches:
                    rec["npis"] = []
                    rec["dropped"] = "too-many-matches"
                with lock:
                    out.write(json.dumps(rec) + "\n")
                    counter["n"] += 1
                    counter["reachable"] += bool(rec["url"])
                    counter["matched"] += bool(rec["npis"])
                    counter["practices"] += len(rec["npis"])
                    counter["emails"] += bool(rec["emails"] and rec["npis"])
                    if counter["n"] % 250 == 0:
                        out.flush()
                        rate = counter["n"] / max(time.time() - t0, 1)
                        eta = (len(todo) - counter["n"]) / max(rate, 0.01) / 60
                        print(f"  {counter['n']:,}/{len(todo):,} | live {counter['reachable']:,}"
                              f" | matched {counter['matched']:,} domains"
                              f" -> {counter['practices']:,} practices"
                              f" | {rate:.1f}/s | ETA {eta:.0f}m", flush=True)
    print(json.dumps(counter), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
