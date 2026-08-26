"""Roll the filtered NPPES rows up into practice-level lead records."""

from __future__ import annotations

import csv
import re
from collections import defaultdict
from pathlib import Path

from .config import ORTHODONTIST_CODE, SERVICE_MAP, SERVICES, TAXONOMY

csv.field_size_limit(10_000_000)

_SUFFIX = {
    "street": "ST", "st": "ST", "avenue": "AVE", "ave": "AVE", "road": "RD",
    "rd": "RD", "drive": "DR", "dr": "DR", "boulevard": "BLVD", "blvd": "BLVD",
    "lane": "LN", "ln": "LN", "court": "CT", "ct": "CT", "place": "PL",
    "pl": "PL", "parkway": "PKWY", "pkwy": "PKWY", "highway": "HWY",
    "hwy": "HWY", "suite": "STE", "ste": "STE", "north": "N", "south": "S",
    "east": "E", "west": "W", "northeast": "NE", "northwest": "NW",
    "southeast": "SE", "southwest": "SW",
}

OUTPUT_COLUMNS = [
    "practice_name", "dba_name", "contact_person", "contact_title",
    "phone", "email", "website", "email_source",
    "address_line1", "address_line2", "city", "state", "zip_code",
    "full_address", "county", "median_household_income",
    "median_household_income_zip", "median_household_income_county",
    "income_level", "is_orthodontic_practice", "specialties",
    "service_invisalign", "service_retainers", "service_nightguards",
    "service_dentures", "services_covered", "providers_at_location",
    "provider_count", "npi", "npi_type", "fax",
    "address_shared_by_practices", "data_source",
]


def norm_street(value: str) -> str:
    value = (value or "").upper()
    value = re.sub(r"[^A-Z0-9 ]+", " ", value)
    words = [_SUFFIX.get(w.lower(), w) for w in value.split()]
    return " ".join(words).strip()


def address_key(rec: dict) -> tuple[str, str]:
    return norm_street(rec.get("addr1", "")), (rec.get("zip5") or "").strip()


def format_phone(value: str) -> str:
    digits = re.sub(r"\D", "", value or "")
    if len(digits) == 11 and digits.startswith("1"):
        digits = digits[1:]
    if len(digits) == 10:
        return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    return (value or "").strip()


ORG_KEEP_UPPER = {"DDS", "DMD", "MD", "PC", "PA", "PLLC", "LLC", "LLP", "LP",
                  "INC", "MS", "PHD", "DO", "II", "III", "IV", "USA", "NW",
                  "NE", "SW", "SE", "N", "S", "E", "W", "&"}
# Person names must not upper-case ordinary words that happen to be initialisms
# elsewhere ("Do", "Ms", "Pa" are common surnames and middle names).
PERSON_KEEP_UPPER = {"II", "III", "IV", "V"}


def titlecase(value: str, keep_upper: set[str] | None = None) -> str:
    """Convert the registry's ALL-CAPS text into readable title case."""
    value = (value or "").strip()
    if not value:
        return ""
    keep_upper = ORG_KEEP_UPPER if keep_upper is None else keep_upper
    out = []
    for word in value.split():
        bare = word.strip(".,").upper()
        if bare in keep_upper:
            out.append(word.upper())
        elif re.search(r"\d", word):
            out.append(word.upper())
        else:
            out.append(word.capitalize() if word.isupper() else word)
    return " ".join(out)


def person_name(first: str, middle: str, last: str, prefix: str = "",
                credential: str = "") -> str:
    parts = [titlecase(prefix, PERSON_KEEP_UPPER), titlecase(first, PERSON_KEEP_UPPER),
             titlecase(middle, PERSON_KEEP_UPPER), titlecase(last, PERSON_KEEP_UPPER)]
    name = " ".join(p for p in parts if p)
    cred = (credential or "").strip().strip(",.")
    if cred:
        name = f"{name}, {cred.upper()}"
    return name.strip()


def service_values(codes: set[str]) -> dict[str, str]:
    """Best service capability across the taxonomy codes present at a practice."""
    out = {}
    for service in SERVICES:
        mapping = SERVICE_MAP[service]
        best = ""
        for code in codes:
            val = mapping.get(code, "")
            if val == "yes":
                best = "yes"
                break
            if val == "often":
                best = "often"
        out[service] = best
    return out


# NPPES writes these literal strings instead of leaving a field empty. They are
# stripped at extraction time too, but scrubbing here as well keeps a cached
# extract from an older run from leaking them into the published columns.
PLACEHOLDERS = {"", "-", "--", "---", "N/A", "NA", "NONE", "NOT APPLICABLE",
                "<UNAVAIL>", "UNAVAIL", "UNAVAILABLE", "NULL", "."}


def scrub(row: dict) -> dict:
    return {k: ("" if (v or "").strip().upper() in PLACEHOLDERS else v)
            for k, v in row.items()}


def load_rows(path: Path) -> list[dict]:
    with open(path, newline="", encoding="utf-8") as fh:
        return [scrub(r) for r in csv.DictReader(fh)]


def build_practices(rows: list[dict]) -> list[dict]:
    """Emit one record per organisation NPI, plus solo practitioners."""
    by_address: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for rec in rows:
        by_address[address_key(rec)].append(rec)

    practices: list[dict] = []
    for key, group in by_address.items():
        orgs = [r for r in group if r.get("entity_type") == "2"]
        people = [r for r in group if r.get("entity_type") == "1"]

        people_codes: set[str] = set()
        for p in people:
            people_codes.update(c for c in (p.get("taxonomies") or "").split("|") if c)

        provider_names = []
        for p in sorted(people, key=lambda r: (r.get("provider_last", ""), r.get("provider_first", ""))):
            codes = [c for c in (p.get("taxonomies") or "").split("|") if c]
            spec = TAXONOMY.get(p.get("primary_taxonomy") or (codes[0] if codes else ""), "")
            spec = spec.replace("Dentist - ", "")
            nm = person_name(p.get("provider_first", ""), p.get("provider_middle", ""),
                             p.get("provider_last", ""), p.get("provider_prefix", ""),
                             p.get("credential", ""))
            provider_names.append(f"{nm} ({spec})" if spec else nm)

        shared = len(orgs) if orgs else 0

        if orgs:
            for org in orgs:
                org_codes = set(c for c in (org.get("taxonomies") or "").split("|") if c)
                practices.append(_practice_record(
                    anchor=org, codes=org_codes | people_codes,
                    provider_names=provider_names, people=people,
                    shared=shared, key=key, solo=False))
        else:
            # No registered organisation at this address: treat each dentist as
            # their own solo practice.
            for p in people:
                codes = set(c for c in (p.get("taxonomies") or "").split("|") if c)
                practices.append(_practice_record(
                    anchor=p, codes=codes, provider_names=provider_names,
                    people=people, shared=0, key=key, solo=True))
    return practices


def _practice_record(anchor: dict, codes: set[str], provider_names: list[str],
                     people: list[dict], shared: int, key, solo: bool) -> dict:
    if solo:
        name = titlecase(anchor.get("dba_name", "")) or person_name(
            anchor.get("provider_first", ""), "", anchor.get("provider_last", ""),
            "Dr.", anchor.get("credential", ""))
        contact = person_name(anchor.get("provider_first", ""),
                              anchor.get("provider_middle", ""),
                              anchor.get("provider_last", ""), "",
                              anchor.get("credential", ""))
        contact_title = "Dentist / Owner"
    else:
        name = titlecase(anchor.get("org_name", ""))
        contact = person_name(anchor.get("contact_first", ""), "",
                              anchor.get("contact_last", ""))
        contact_title = titlecase(anchor.get("contact_title", ""))
        if not contact and provider_names:
            contact = provider_names[0].split(" (")[0]
            contact_title = contact_title or "Dentist"

    services = service_values(codes)
    specialties = sorted({TAXONOMY.get(c, c).replace("Dentist - ", "")
                          for c in codes if c in TAXONOMY})
    addr2 = titlecase(anchor.get("addr2", ""))
    city = titlecase(anchor.get("city", ""))
    state = (anchor.get("state") or "").upper()
    zip5 = anchor.get("zip5", "")
    zip4 = anchor.get("zip4", "")
    zip_code = f"{zip5}-{zip4}" if zip4 and zip4 != "0000" else zip5
    line1 = titlecase(anchor.get("addr1", ""))
    full = ", ".join(p for p in [line1, addr2, city, f"{state} {zip_code}".strip()] if p)

    phone = format_phone(anchor.get("phone") or anchor.get("contact_phone") or "")
    if not phone:
        for p in people:
            phone = format_phone(p.get("phone", ""))
            if phone:
                break

    return {
        "practice_name": name,
        "dba_name": titlecase(anchor.get("dba_name", "")),
        "contact_person": contact,
        "contact_title": contact_title,
        "phone": phone,
        "email": "",
        "website": "",
        "email_source": "",
        "address_line1": line1,
        "address_line2": addr2,
        "city": city,
        "state": state,
        "zip_code": zip_code,
        "full_address": full,
        "county": "",
        "median_household_income": "",
        "median_household_income_zip": "",
        "median_household_income_county": "",
        "income_level": "",
        "is_orthodontic_practice": "yes" if ORTHODONTIST_CODE in codes else "no",
        "specialties": "; ".join(specialties),
        "service_invisalign": services["invisalign"],
        "service_retainers": services["retainers"],
        "service_nightguards": services["nightguards"],
        "service_dentures": services["dentures"],
        "services_covered": sum(1 for v in services.values() if v),
        "providers_at_location": "; ".join(provider_names[:12]),
        "provider_count": len(people),
        "npi": anchor.get("npi", ""),
        "npi_type": "Organization" if not solo else "Individual",
        "fax": format_phone(anchor.get("fax", "")),
        "address_shared_by_practices": shared,
        "data_source": "NPPES (CMS) monthly dissemination file",
        # internal, dropped before writing
        "_zip5": zip5,
        "_codes": codes,
        "_surnames": [n for n in (
            [titlecase(p.get("provider_last", ""), PERSON_KEEP_UPPER) for p in people]
            + [titlecase(anchor.get("provider_last", ""), PERSON_KEEP_UPPER)]
        ) if n],
    }


def attach_income(practices: list[dict], lookup) -> None:
    cache: dict[str, dict] = {}
    for rec in practices:
        zip5 = rec.get("_zip5", "")
        if zip5 not in cache:
            cache[zip5] = lookup.lookup(zip5)
        info = cache[zip5]
        rec["county"] = info["county"]
        rec["median_household_income"] = info["median_household_income"] or ""
        rec["median_household_income_zip"] = info["median_household_income_zip"] or ""
        rec["median_household_income_county"] = info["median_household_income_county"] or ""
        rec["income_level"] = info["income_level"]


def write_csv(practices: list[dict], path: Path) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=OUTPUT_COLUMNS, extrasaction="ignore")
        writer.writeheader()
        for rec in sorted(practices, key=lambda r: (r["state"], r["city"], r["practice_name"])):
            writer.writerow(rec)
    return len(practices)
