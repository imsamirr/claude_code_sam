"""Taxonomy, geography and service-mapping configuration.

Everything here is derived from public reference data:
  * NUCC Health Care Provider Taxonomy codes (used by the NPPES NPI registry)
  * US Census ACS 5-year geography identifiers
"""

from pathlib import Path

# --- Paths -----------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_RAW_DIR = PROJECT_ROOT / "raw"
DEFAULT_OUT_DIR = PROJECT_ROOT / "output"

# --- Source URLs -----------------------------------------------------------

NPPES_INDEX_URL = "https://download.cms.gov/nppes/NPI_Files.html"
NPPES_BASE_URL = "https://download.cms.gov/nppes/"

ACS_YEAR = 2023
ACS_INCOME_TABLE = "b19013"  # Median household income in the past 12 months
ACS_DAT_URL = (
    "https://www2.census.gov/programs-surveys/acs/summary_file/{year}/"
    "table-based-SF/data/5YRData/acsdt5y{year}-{table}.dat"
)
# 2020 ZCTA -> 2020 County national relationship file
ZCTA_COUNTY_REL_URL = (
    "https://www2.census.gov/geo/docs/maps-data/data/rel2020/zcta520/"
    "tab20_zcta520_county20_natl.txt"
)
COUNTY_NAMES_URL = (
    "https://www2.census.gov/geo/docs/reference/codes2020/national_county2020.txt"
)
# 2010 ZCTA -> county relationship file. Older vintage than the 2020 file above,
# but it carries per-part *population*, which assigns split ZIPs far better than
# land area does (a ZIP's population lives in one county even when its acreage
# does not).
ZCTA_COUNTY_POP_URL = (
    "https://www2.census.gov/geo/docs/maps-data/data/rel/zcta_county_rel_10.txt"
)

# Census summary-file GEO_ID prefixes
GEO_PREFIX_ZCTA = "860Z200US"
GEO_PREFIX_COUNTY = "0500000US"

# --- Dental taxonomy codes -------------------------------------------------
# NUCC "Dental Providers" grouping (12...) plus the dental facility code.

TAXONOMY = {
    "1223X0400X": "Dentist - Orthodontics and Dentofacial Orthopedics",
    "1223P0700X": "Dentist - Prosthodontics",
    "1223G0001X": "Dentist - General Practice",
    "122300000X": "Dentist (unspecified)",
    "1223P0221X": "Dentist - Pediatric Dentistry",
    "1223P0300X": "Dentist - Periodontics",
    "1223E0200X": "Dentist - Endodontics",
    "1223S0112X": "Dentist - Oral and Maxillofacial Surgery",
    "1223D0001X": "Dentist - Dental Public Health",
    "1223P0106X": "Dentist - Oral and Maxillofacial Pathology",
    "1223X0008X": "Dentist - Oral and Maxillofacial Radiology",
    "1223D0004X": "Dentist - Dentist Anesthesiologist",
    "1223X2210X": "Dentist - Orofacial Pain",
    "125K00000X": "Advanced Practice Dental Therapist",
    "125J00000X": "Dental Therapist",
    "126800000X": "Dental Assistant",
    "124Q00000X": "Dental Hygienist",
    "126900000X": "Dental Laboratory Technician",
    "261QD0000X": "Clinic/Center - Dental",
}

# The taxonomy that literally means "orthodontist".
ORTHODONTIST_CODE = "1223X0400X"

# Taxonomies that actually treat patients (excludes assistants/hygienists/labs).
TREATING_CODES = {
    "1223X0400X", "1223P0700X", "1223G0001X", "122300000X",
    "1223P0221X", "1223P0300X", "1223E0200X", "1223S0112X",
    "1223D0001X", "1223P0106X", "1223X0008X", "1223D0004X",
    "1223X2210X", "125K00000X", "125J00000X", "261QD0000X",
}

# --- Service capability mapping -------------------------------------------
# Which of the four requested services each taxonomy plausibly delivers.
#   "yes"   -> core scope of that specialty
#   "often" -> commonly offered, not the specialty's defining scope
# Note: dentures are prosthodontic / general-dentistry work, NOT orthodontic
# work. Orthodontists supply aligners, retainers and (frequently) nightguards.

SERVICE_MAP = {
    "invisalign": {
        "1223X0400X": "yes", "1223G0001X": "often", "122300000X": "often",
        "1223P0221X": "often", "261QD0000X": "often",
    },
    "retainers": {
        "1223X0400X": "yes", "1223G0001X": "often", "122300000X": "often",
        "1223P0221X": "often", "261QD0000X": "often",
    },
    "nightguards": {
        "1223X0400X": "often", "1223G0001X": "yes", "122300000X": "yes",
        "1223P0700X": "yes", "1223X2210X": "yes", "1223P0300X": "often",
        "1223P0221X": "often", "261QD0000X": "yes",
    },
    "dentures": {
        "1223P0700X": "yes", "1223G0001X": "yes", "122300000X": "yes",
        "1223S0112X": "often", "261QD0000X": "yes",
    },
}

SERVICES = ("invisalign", "retainers", "nightguards", "dentures")

# --- Geography -------------------------------------------------------------

US_STATES = {
    "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID",
    "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS",
    "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK",
    "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV",
    "WI", "WY", "DC",
}
US_TERRITORIES = {"PR", "VI", "GU", "AS", "MP"}
