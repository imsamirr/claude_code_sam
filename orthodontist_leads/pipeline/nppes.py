"""Download and filter the NPPES bulk data dissemination file.

NPPES (National Plan and Provider Enumeration System) is the CMS registry of
every NPI-holding healthcare provider in the United States. The monthly
dissemination file is public-domain US government data and is the
authoritative source for practice name, practice address, practice phone and
the organisation's authorized official.

The main data file is ~11.6 GB uncompressed, so it is streamed straight out of
the zip archive and filtered row by row; it is never fully extracted to disk.
"""

from __future__ import annotations

import csv
import io
import re
import sys
import zipfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterator

import requests

from .config import (
    NPPES_BASE_URL,
    NPPES_INDEX_URL,
    TAXONOMY,
    TREATING_CODES,
    US_STATES,
    US_TERRITORIES,
)

csv.field_size_limit(10_000_000)

# Column indices in npidata_pfile (330 columns, stable across releases).
COL = {
    "npi": 0,
    "entity_type": 1,
    "org_name": 4,
    "last_name": 5,
    "first_name": 6,
    "middle_name": 7,
    "name_prefix": 8,
    "credential": 10,
    "other_org_name": 11,
    "addr1": 28,
    "addr2": 29,
    "city": 30,
    "state": 31,
    "postal": 32,
    "country": 33,
    "phone": 34,
    "fax": 35,
    "deactivation_date": 39,
    "reactivation_date": 40,
    "ao_last": 42,
    "ao_first": 43,
    "ao_middle": 44,
    "ao_title": 45,
    "ao_phone": 46,
    "parent_org": 309,
    "ao_prefix": 311,
    "ao_credential": 313,
}
# Healthcare Provider Taxonomy Code_1..15 start at col 47, stride 4.
TAX_START, TAX_STRIDE, TAX_COUNT = 47, 4, 15
# Primary Taxonomy Switch_1..15 start at col 50, same stride.
SWITCH_START = 50

OUT_FIELDS = [
    "npi", "entity_type", "org_name", "dba_name", "provider_last",
    "provider_first", "provider_middle", "provider_prefix", "credential",
    "contact_last", "contact_first", "contact_title", "contact_phone",
    "parent_org", "addr1", "addr2", "city", "state", "zip5", "zip4",
    "phone", "fax", "primary_taxonomy", "taxonomies",
]


def find_monthly_file_url(session: requests.Session | None = None) -> str:
    """Scrape the CMS download index for the current monthly dissemination zip."""
    session = session or requests.Session()
    html = session.get(NPPES_INDEX_URL, timeout=60).text
    matches = re.findall(
        r"href='\./(NPPES_Data_Dissemination_[A-Z][a-z]+_\d{4}(?:_V\d+)?\.zip)'", html
    )
    if not matches:
        raise RuntimeError("Could not locate the NPPES monthly file on the CMS index page")
    return NPPES_BASE_URL + matches[0]


def download(url: str, dest: Path, session: requests.Session | None = None) -> Path:
    """Stream a large file to disk, skipping the work if it is already present."""
    session = session or requests.Session()
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists() and dest.stat().st_size > 0:
        return dest
    tmp = dest.with_suffix(dest.suffix + ".part")
    with session.get(url, stream=True, timeout=(30, 600)) as r:
        r.raise_for_status()
        total = int(r.headers.get("Content-Length") or 0)
        done = 0
        with open(tmp, "wb") as fh:
            for chunk in r.iter_content(chunk_size=1 << 20):
                fh.write(chunk)
                done += len(chunk)
                if total:
                    pct = 100 * done / total
                    print(f"\r  {dest.name}: {done/1e6:,.0f}/{total/1e6:,.0f} MB "
                          f"({pct:4.1f}%)", end="", file=sys.stderr)
        print(file=sys.stderr)
    tmp.rename(dest)
    return dest


def _member(zf: zipfile.ZipFile, prefix: str) -> str:
    for name in zf.namelist():
        if name.startswith(prefix) and name.endswith(".csv") and "fileheader" not in name:
            return name
    raise KeyError(f"No member starting with {prefix!r} in archive")


def _split_zip(postal: str) -> tuple[str, str]:
    digits = re.sub(r"\D", "", postal or "")
    if len(digits) >= 9:
        return digits[:5], digits[5:9]
    return digits[:5], ""


def _clean(value: str) -> str:
    return (value or "").strip().strip('"').strip()


@dataclass
class ExtractStats:
    rows_read: int = 0
    dental_rows: int = 0
    kept: int = 0
    dropped_inactive: int = 0
    dropped_non_us: int = 0
    dropped_no_address: int = 0
    by_taxonomy: dict = field(default_factory=dict)


def iter_dental_records(zip_path: Path, stats: ExtractStats,
                        include_territories: bool = True) -> Iterator[dict]:
    """Yield one dict per active US dental NPI found in the bulk file."""
    allowed_states = set(US_STATES) | (set(US_TERRITORIES) if include_territories else set())
    with zipfile.ZipFile(zip_path) as zf:
        member = _member(zf, "npidata_pfile")
        with zf.open(member) as raw:
            text = io.TextIOWrapper(raw, encoding="utf-8", errors="replace", newline="")
            reader = csv.reader(text)
            next(reader, None)  # header
            for row in reader:
                stats.rows_read += 1
                if len(row) < 330:
                    continue

                codes, primary = [], ""
                for i in range(TAX_COUNT):
                    code = _clean(row[TAX_START + i * TAX_STRIDE])
                    if not code:
                        continue
                    codes.append(code)
                    if _clean(row[SWITCH_START + i * TAX_STRIDE]).upper() == "Y":
                        primary = code
                dental = [c for c in codes if c in TAXONOMY]
                if not dental or not any(c in TREATING_CODES for c in dental):
                    continue
                stats.dental_rows += 1

                if _clean(row[COL["deactivation_date"]]) and not _clean(row[COL["reactivation_date"]]):
                    stats.dropped_inactive += 1
                    continue

                state = _clean(row[COL["state"]]).upper()
                country = _clean(row[COL["country"]]).upper() or "US"
                if country != "US" or state not in allowed_states:
                    stats.dropped_non_us += 1
                    continue

                addr1 = _clean(row[COL["addr1"]])
                zip5, zip4 = _split_zip(_clean(row[COL["postal"]]))
                if not addr1 or len(zip5) != 5:
                    stats.dropped_no_address += 1
                    continue

                if primary not in dental:
                    primary = dental[0]
                for c in dental:
                    stats.by_taxonomy[c] = stats.by_taxonomy.get(c, 0) + 1
                stats.kept += 1

                yield {
                    "npi": _clean(row[COL["npi"]]),
                    "entity_type": _clean(row[COL["entity_type"]]),
                    "org_name": _clean(row[COL["org_name"]]),
                    "dba_name": _clean(row[COL["other_org_name"]]),
                    "provider_last": _clean(row[COL["last_name"]]),
                    "provider_first": _clean(row[COL["first_name"]]),
                    "provider_middle": _clean(row[COL["middle_name"]]),
                    "provider_prefix": _clean(row[COL["name_prefix"]]),
                    "credential": _clean(row[COL["credential"]]),
                    "contact_last": _clean(row[COL["ao_last"]]),
                    "contact_first": _clean(row[COL["ao_first"]]),
                    "contact_title": _clean(row[COL["ao_title"]]),
                    "contact_phone": _clean(row[COL["ao_phone"]]),
                    "parent_org": _clean(row[COL["parent_org"]]),
                    "addr1": addr1,
                    "addr2": _clean(row[COL["addr2"]]),
                    "city": _clean(row[COL["city"]]),
                    "state": state,
                    "zip5": zip5,
                    "zip4": zip4,
                    "phone": _clean(row[COL["phone"]]),
                    "fax": _clean(row[COL["fax"]]),
                    "primary_taxonomy": primary,
                    "taxonomies": "|".join(dental),
                }


def extract(zip_path: Path, out_csv: Path, include_territories: bool = True) -> ExtractStats:
    """Stream the bulk file and write the filtered dental subset to ``out_csv``."""
    stats = ExtractStats()
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    with open(out_csv, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=OUT_FIELDS)
        writer.writeheader()
        for rec in iter_dental_records(zip_path, stats, include_territories):
            writer.writerow(rec)
            if stats.kept % 25_000 == 0:
                print(f"\r  scanned {stats.rows_read:,} NPIs, kept {stats.kept:,} dental",
                      end="", file=sys.stderr)
    print(f"\r  scanned {stats.rows_read:,} NPIs, kept {stats.kept:,} dental",
          file=sys.stderr)
    return stats


def load_other_names(zip_path: Path, npis: set[str]) -> dict[str, list[str]]:
    """Map NPI -> additional / doing-business-as organisation names."""
    out: dict[str, list[str]] = {}
    with zipfile.ZipFile(zip_path) as zf:
        with zf.open(_member(zf, "othername_pfile")) as raw:
            reader = csv.reader(io.TextIOWrapper(raw, encoding="utf-8", errors="replace", newline=""))
            next(reader, None)
            for row in reader:
                if len(row) < 2:
                    continue
                npi = _clean(row[0])
                if npi in npis:
                    name = _clean(row[1])
                    if name:
                        out.setdefault(npi, []).append(name)
    return out


def load_endpoints(zip_path: Path, npis: set[str]) -> dict[str, list[dict]]:
    """Map NPI -> registered health-information endpoints (URLs / Direct addresses)."""
    out: dict[str, list[dict]] = {}
    with zipfile.ZipFile(zip_path) as zf:
        with zf.open(_member(zf, "endpoint_pfile")) as raw:
            reader = csv.reader(io.TextIOWrapper(raw, encoding="utf-8", errors="replace", newline=""))
            next(reader, None)
            for row in reader:
                if len(row) < 6:
                    continue
                npi = _clean(row[0])
                if npi in npis:
                    out.setdefault(npi, []).append({
                        "type": _clean(row[2]),
                        "endpoint": _clean(row[3]),
                        "description": _clean(row[5]),
                    })
    return out


def load_secondary_locations(zip_path: Path, npis: set[str]) -> dict[str, list[dict]]:
    """Map NPI -> secondary practice locations (satellite offices)."""
    out: dict[str, list[dict]] = {}
    with zipfile.ZipFile(zip_path) as zf:
        with zf.open(_member(zf, "pl_pfile")) as raw:
            reader = csv.reader(io.TextIOWrapper(raw, encoding="utf-8", errors="replace", newline=""))
            next(reader, None)
            for row in reader:
                if len(row) < 8:
                    continue
                npi = _clean(row[0])
                if npi not in npis:
                    continue
                state = _clean(row[4]).upper()
                zip5, zip4 = _split_zip(_clean(row[5]))
                if state not in US_STATES | US_TERRITORIES or len(zip5) != 5:
                    continue
                out.setdefault(npi, []).append({
                    "addr1": _clean(row[1]), "addr2": _clean(row[2]),
                    "city": _clean(row[3]), "state": state,
                    "zip5": zip5, "zip4": zip4, "phone": _clean(row[7]),
                })
    return out
