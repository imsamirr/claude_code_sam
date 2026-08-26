#!/usr/bin/env python3
"""Harvest candidate dental-practice domains from the Common Crawl host index.

Guessing a practice's domain from its name has poor recall. This inverts the
problem: Common Crawl publishes a host-level index of every hostname it has
seen, so the dental-looking ones can be enumerated directly, fetched once, and
matched back to NPPES by the phone number printed on the page. A phone match is
exact, so precision comes from the match rather than from the keyword filter -
which means the filter can afford to be generous.

Hosts are stored reversed ("com.example.www"), so they are flipped back here.
"""

from __future__ import annotations

import argparse
import gzip
import re
import sys
from pathlib import Path

import requests

PATHS_URL = ("https://data.commoncrawl.org/projects/hyperlinkgraph/"
             "cc-main-2024-jul-aug-sep/host/"
             "cc-main-2024-jul-aug-sep-host-vertices.paths.gz")
DATA_ROOT = "https://data.commoncrawl.org/"

# Generous - a false positive only costs one fetch, and the phone match filters.
INCLUDE_RE = re.compile(
    r"orthodont|dental|dentist|braces|invisalign|smiles|dds|dmd|"
    r"toothdoc|familydent|kidsdent|pediatricdent", re.I)
# "ortho" also prefixes orthopedics, orthodoxy, orthotics and orthography.
EXCLUDE_RE = re.compile(
    r"orthope|orthopae|orthodox|orthotic|orthograph|orthomol|orthodontist-?directory|"
    r"orthorexi|orthogon", re.I)
# Country-code TLDs a US practice would not normally sit on.
ALLOWED_TLD = re.compile(
    r"\.(?:com|net|org|us|dental|dentist|care|health|clinic|co)$", re.I)


def unreverse(host: str) -> str:
    return ".".join(reversed(host.split(".")))


def apex(host: str) -> str:
    parts = host.split(".")
    return ".".join(parts[-2:]) if len(parts) > 2 and parts[0] == "www" else host


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", type=Path,
                    default=Path(__file__).resolve().parent / "work" / "cc_dental_domains.txt")
    ap.add_argument("--parts", type=int, default=16, help="how many index parts to scan")
    ap.add_argument("--state", type=Path,
                    default=Path(__file__).resolve().parent / "work" / "cc_harvest_state.txt",
                    help="records which index parts are already done, for resuming")
    args = ap.parse_args()
    args.out.parent.mkdir(parents=True, exist_ok=True)

    session = requests.Session()
    session.headers["User-Agent"] = "practice-contact-research/1.0"
    paths = gzip.decompress(session.get(PATHS_URL, timeout=120).content).decode().split()

    # Resume from whatever a previous run already wrote.
    found: set[str] = set()
    if args.out.exists():
        found = {d.strip() for d in args.out.read_text().split() if d.strip()}
        print(f"  resuming with {len(found):,} domains already harvested", flush=True)
    done_parts = set()
    if args.state.exists():
        done_parts = {int(x) for x in args.state.read_text().split() if x.strip().isdigit()}

    def checkpoint(part: int) -> None:
        args.out.write_text("\n".join(sorted(found)) + "\n")
        done_parts.add(part)
        args.state.write_text("\n".join(str(x) for x in sorted(done_parts)) + "\n")

    scanned = 0
    for i, path in enumerate(paths[: args.parts]):
        if i in done_parts:
            continue
        # A 160 MB stream can drop mid-read; retry the part rather than losing
        # the whole run to one broken connection.
        for attempt in range(1, 4):
            before = len(found)
            try:
                with session.get(DATA_ROOT + path, stream=True, timeout=(30, 900)) as r:
                    r.raise_for_status()
                    with gzip.open(r.raw, "rt", errors="replace") as fh:
                        for line in fh:
                            scanned += 1
                            tab = line.rfind("\t")
                            if tab < 0:
                                continue
                            rev = line[tab + 1:].strip()
                            if not INCLUDE_RE.search(rev) or EXCLUDE_RE.search(rev):
                                continue
                            host = unreverse(rev)
                            if not ALLOWED_TLD.search(host):
                                continue
                            found.add(apex(host))
                break
            except Exception as exc:
                print(f"  part {i+1}: attempt {attempt} failed ({type(exc).__name__}); "
                      f"kept {len(found) - before:,} before the break", flush=True)
                if attempt == 3:
                    print(f"  part {i+1}: giving up, moving on", flush=True)
        checkpoint(i)
        print(f"  part {i+1}/{args.parts}: scanned {scanned:,} hosts, "
              f"kept {len(found):,} dental domains", flush=True)

    print(f"wrote {len(found):,} candidate domains -> {args.out}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
