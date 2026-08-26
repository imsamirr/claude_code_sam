"""US Census ACS median-household-income lookups by ZIP code and county.

Uses the ACS 5-year *table-based summary files* published on www2.census.gov.
Unlike the api.census.gov JSON API these need no API key, and a single file
covers every geography in the country.

Table B19013_001 = "Median household income in the past 12 months
(in inflation-adjusted dollars)".
"""

from __future__ import annotations

import csv
import re
from pathlib import Path

import requests

from .config import (
    ACS_DAT_URL,
    ACS_INCOME_TABLE,
    ACS_YEAR,
    COUNTY_NAMES_URL,
    GEO_PREFIX_COUNTY,
    GEO_PREFIX_ZCTA,
    ZCTA_COUNTY_POP_URL,
    ZCTA_COUNTY_REL_URL,
)

# ACS "jam values": negative sentinels meaning suppressed / not applicable.
JAM_VALUES = {
    "-666666666", "-999999999", "-888888888", "-222222222",
    "-333333333", "-555555555", "-.", "", "null",
}


def _fetch(url: str, dest: Path, session: requests.Session | None = None) -> Path:
    session = session or requests.Session()
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists() and dest.stat().st_size > 0:
        return dest
    with session.get(url, stream=True, timeout=(30, 600)) as r:
        r.raise_for_status()
        with open(dest, "wb") as fh:
            for chunk in r.iter_content(chunk_size=1 << 20):
                fh.write(chunk)
    return dest


def _parse_income(value: str) -> int | None:
    value = (value or "").strip()
    if value in JAM_VALUES:
        return None
    try:
        num = int(float(value))
    except ValueError:
        return None
    return num if num > 0 else None


def load_income(raw_dir: Path, session: requests.Session | None = None
                ) -> tuple[dict[str, int], dict[str, int]]:
    """Return ``(income_by_zcta, income_by_county_fips)`` median household income."""
    url = ACS_DAT_URL.format(year=ACS_YEAR, table=ACS_INCOME_TABLE)
    path = _fetch(url, raw_dir / f"acsdt5y{ACS_YEAR}-{ACS_INCOME_TABLE}.dat", session)

    by_zcta: dict[str, int] = {}
    by_county: dict[str, int] = {}
    with open(path, encoding="utf-8", errors="replace") as fh:
        reader = csv.reader(fh, delimiter="|")
        next(reader, None)  # header
        for row in reader:
            if len(row) < 2:
                continue
            geo_id, estimate = row[0].strip(), row[1]
            if geo_id.startswith(GEO_PREFIX_ZCTA):
                income = _parse_income(estimate)
                if income is not None:
                    by_zcta[geo_id[len(GEO_PREFIX_ZCTA):]] = income
            elif geo_id.startswith(GEO_PREFIX_COUNTY):
                income = _parse_income(estimate)
                if income is not None:
                    by_county[geo_id[len(GEO_PREFIX_COUNTY):]] = income
    return by_zcta, by_county


def load_zcta_to_county_by_area(raw_dir: Path, session: requests.Session | None = None
                               ) -> dict[str, tuple[str, str]]:
    """Map ZIP (ZCTA5) -> ``(county_fips, county_name)`` by dominant land area.

    Uses the 2020-vintage relationship file, so it covers current ZCTAs, but a
    ZIP whose acreage sprawls into an empty neighbouring county is mis-assigned.
    Used as the fallback and as the source of county *names*.
    """
    path = _fetch(ZCTA_COUNTY_REL_URL, raw_dir / "zcta_county_rel.txt", session)
    best: dict[str, tuple[float, str, str]] = {}
    with open(path, encoding="utf-8-sig", errors="replace") as fh:
        reader = csv.DictReader(fh, delimiter="|")
        for row in reader:
            zcta = (row.get("GEOID_ZCTA5_20") or "").strip()
            fips = (row.get("GEOID_COUNTY_20") or "").strip()
            if not zcta or not fips:
                continue
            try:
                area = float((row.get("AREALAND_PART") or "0").strip() or 0)
            except ValueError:
                area = 0.0
            name = (row.get("NAMELSAD_COUNTY_20") or "").strip()
            if zcta not in best or area > best[zcta][0]:
                best[zcta] = (area, fips, name)
    return {z: (fips, name) for z, (_, fips, name) in best.items()}


def load_county_names(raw_dir: Path, session: requests.Session | None = None
                      ) -> dict[str, str]:
    """Map county FIPS -> full county name, from the 2020 relationship file."""
    path = _fetch(ZCTA_COUNTY_REL_URL, raw_dir / "zcta_county_rel.txt", session)
    out: dict[str, str] = {}
    with open(path, encoding="utf-8-sig", errors="replace") as fh:
        reader = csv.DictReader(fh, delimiter="|")
        for row in reader:
            fips = (row.get("GEOID_COUNTY_20") or "").strip()
            name = (row.get("NAMELSAD_COUNTY_20") or "").strip()
            if fips and name:
                out.setdefault(fips, name)
    return out


def load_zcta_to_county_by_population(raw_dir: Path, session: requests.Session | None = None
                                      ) -> dict[str, str]:
    """Map ZIP (ZCTA5) -> county FIPS holding most of that ZIP's population."""
    path = _fetch(ZCTA_COUNTY_POP_URL, raw_dir / "zcta_county_rel_pop.txt", session)
    best: dict[str, tuple[int, str]] = {}
    with open(path, encoding="utf-8-sig", errors="replace") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            zcta = (row.get("ZCTA5") or "").strip()
            fips = (row.get("GEOID") or "").strip().zfill(5)
            if not zcta or len(fips) != 5:
                continue
            try:
                pop = int(float((row.get("POPPT") or "0").strip() or 0))
            except ValueError:
                pop = 0
            if zcta not in best or pop > best[zcta][0]:
                best[zcta] = (pop, fips)
    return {z: fips for z, (_, fips) in best.items()}


def load_county_states(raw_dir: Path, session: requests.Session | None = None
                       ) -> dict[str, str]:
    """Map county FIPS -> USPS state abbreviation."""
    path = _fetch(COUNTY_NAMES_URL, raw_dir / "national_county.txt", session)
    out: dict[str, str] = {}
    with open(path, encoding="utf-8-sig", errors="replace") as fh:
        reader = csv.DictReader(fh, delimiter="|")
        for row in reader:
            statefp = (row.get("STATEFP") or "").strip()
            countyfp = (row.get("COUNTYFP") or "").strip()
            if statefp and countyfp:
                out[statefp + countyfp] = (row.get("STATE") or "").strip()
    return out


class IncomeLookup:
    """Bundles the ZIP/county income tables behind one ``lookup(zip5)`` call.

    County assignment prefers the population-weighted crosswalk and falls back
    to the area-weighted one when the population vintage has no usable answer
    (a newer ZIP, or a county FIPS that has since been retired - Connecticut
    replaced its counties with planning regions in 2022, for example).
    """

    def __init__(self, raw_dir: Path, session: requests.Session | None = None):
        self.income_by_zip, self.income_by_county = load_income(raw_dir, session)
        self.zip_to_county_area = load_zcta_to_county_by_area(raw_dir, session)
        self.zip_to_county_pop = load_zcta_to_county_by_population(raw_dir, session)
        self.county_names = load_county_names(raw_dir, session)
        self.county_state = load_county_states(raw_dir, session)

    def _county_for(self, zip5: str) -> tuple[str, str]:
        pop_fips = self.zip_to_county_pop.get(zip5, "")
        area_fips, area_name = self.zip_to_county_area.get(zip5, ("", ""))
        candidates = []
        if pop_fips:
            candidates.append((pop_fips, self.county_names.get(pop_fips, "")))
        if area_fips and area_fips != pop_fips:
            candidates.append((area_fips, area_name))
        # Prefer a FIPS that still carries an ACS income figure, then any that
        # resolves to a name, then whatever the population crosswalk said.
        for fips, name in candidates:
            if fips in self.income_by_county and name:
                return fips, name
        for fips, name in candidates:
            if name:
                return fips, name
        return (candidates[0] if candidates else ("", ""))

    def lookup(self, zip5: str) -> dict[str, object]:
        zip5 = re.sub(r"\D", "", zip5 or "")[:5].zfill(5) if zip5 else ""
        fips, county_name = self._county_for(zip5)
        zip_income = self.income_by_zip.get(zip5)
        county_income = self.income_by_county.get(fips) if fips else None
        return {
            "county": county_name,
            "county_fips": fips,
            "county_state": self.county_state.get(fips, ""),
            "median_household_income_zip": zip_income,
            "median_household_income_county": county_income,
            # Prefer the ZIP-level figure; fall back to the county.
            "median_household_income": zip_income if zip_income is not None else county_income,
            "income_level": _income_level(
                zip_income if zip_income is not None else county_income
            ),
        }


def _income_level(income: int | None) -> str:
    """Coarse band, handy for prioritising outreach lists."""
    if income is None:
        return ""
    if income < 50_000:
        return "low"
    if income < 75_000:
        return "moderate"
    if income < 100_000:
        return "above-average"
    if income < 150_000:
        return "high"
    return "very-high"
