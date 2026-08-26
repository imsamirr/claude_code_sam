"""Website discovery and contact-email extraction for dental practices.

NPPES carries no website or email field, so those columns have to be earned:

1. **Registered endpoints** - the NPPES endpoint file sometimes contains a
   practice URL or a Direct-messaging address, which gives a free, authoritative
   domain for a minority of records.
2. **Name-derived domain candidates** - a practice's domain is usually its name
   with the punctuation removed. Candidates are only accepted once the fetched
   page *proves* it belongs to the practice (its phone number, or its ZIP plus
   city, appears in the page text). Unverified guesses are discarded.
3. **Contact-page crawl** - for a verified site, the home page and the usual
   contact/about paths are scanned for ``mailto:`` links and email addresses.

The crawler identifies itself, honours ``robots.txt``, keeps concurrency low
and rate-limits per host.
"""

from __future__ import annotations

import re
import socket
import threading
import time
import urllib.robotparser
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from urllib.parse import urljoin, urlparse

import requests

USER_AGENT = (
    "Mozilla/5.0 (compatible; PracticeContactBot/1.0; "
    "+contact-research; respects robots.txt)"
)
REQUEST_TIMEOUT = (5, 8)
CONTACT_PATHS = ("/contact", "/contact-us", "/contact-us/", "/contact/",
                 "/contact.html", "/about", "/about-us", "/our-office")
# Anchors whose href or text look like a contact page.
CONTACT_LINK_RE = re.compile(
    r'<a\b[^>]*href=["\']([^"\'#]+)["\'][^>]*>(.{0,120}?)</a>', re.I | re.S)
CONTACT_HINT_RE = re.compile(
    r"contact|reach[\s-]?us|get[\s-]?in[\s-]?touch|our[\s-]?office|"
    r"appointment|about[\s-]?us|location", re.I)

EMAIL_RE = re.compile(
    r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}", re.I
)
# Addresses that are never a practice's real inbox.
EMAIL_BLOCKLIST = re.compile(
    r"(?:@(?:example|sentry|wix|squarespace|godaddy|godaddysites|w3\.org|"
    r"schema\.org|googlemail|sentry\.io|domain|email|yourdomain|test)\b"
    r"|\.(?:png|jpe?g|gif|svg|webp|css|js|woff2?)$"
    r"|^[0-9a-f]{16,}@)", re.I
)
GENERIC_TLD = (".com", ".net", ".org", ".dental", ".dentist", ".care")
# Practically every US dental practice is on .com; the rest are a long tail.
# Each extra candidate costs a DNS lookup, so only the two strongest stems get
# the alternative TLDs, and the whole candidate list is hard-capped.
PRIMARY_TLD = ".com"
SECONDARY_TLDS = (".net", ".dental")
MAX_CANDIDATES = 12

_STOPWORDS = {
    "the", "of", "and", "a", "an", "at", "for", "in", "llc", "pllc", "pc",
    "pa", "inc", "ltd", "lp", "llp", "corp", "corporation", "company", "co",
    "dds", "dmd", "md", "professional", "association", "limited", "liability",
    "partnership", "group", "practice", "office", "offices",
}


@dataclass
class SiteResult:
    npi: str
    website: str = ""
    emails: str = ""
    source: str = ""
    verified: str = ""


class Politeness:
    """Per-host robots.txt cache plus a minimum delay between requests."""

    def __init__(self, min_delay: float = 1.0):
        self.min_delay = min_delay
        self._last: dict[str, float] = {}
        self._robots: dict[str, urllib.robotparser.RobotFileParser | None] = {}
        self._lock = threading.Lock()

    def _robots_for(self, host_root: str):
        with self._lock:
            if host_root in self._robots:
                return self._robots[host_root]
        parser = urllib.robotparser.RobotFileParser()
        parser.set_url(host_root + "/robots.txt")
        try:
            resp = requests.get(host_root + "/robots.txt",
                                headers={"User-Agent": USER_AGENT},
                                timeout=REQUEST_TIMEOUT)
            parser.parse(resp.text.splitlines() if resp.status_code == 200 else [])
        except requests.RequestException:
            parser.parse([])  # unreachable robots.txt -> treat as permissive
        with self._lock:
            self._robots[host_root] = parser
        return parser

    def allowed(self, url: str) -> bool:
        parts = urlparse(url)
        root = f"{parts.scheme}://{parts.netloc}"
        # www and apex are the same site in practice, so let them share one
        # robots.txt fetch instead of paying for it twice per candidate domain.
        canonical = root.replace("://www.", "://")
        with self._lock:
            parser = self._robots.get(canonical)
        if parser is None:
            parser = self._robots_for(root)
            with self._lock:
                self._robots[canonical] = parser
        try:
            return parser.can_fetch(USER_AGENT, url)
        except Exception:
            return True

    def wait(self, url: str) -> None:
        host = urlparse(url).netloc
        with self._lock:
            last = self._last.get(host, 0.0)
            delay = self.min_delay - (time.time() - last)
        if delay > 0:
            time.sleep(delay)
        with self._lock:
            self._last[host] = time.time()


def name_stems(name: str) -> list[str]:
    """Ordered, most-likely-first domain stems for one practice name."""
    words = [w for w in re.split(r"[^A-Za-z0-9]+", (name or "").lower()) if w]
    words = [w for w in words if w not in _STOPWORDS and not w.isdigit()]
    if not words:
        return []
    stems = ["".join(words)]
    if len(words) > 2:
        stems.append("".join(words[:2]))
        stems.append(words[0] + words[-1])
    if len(words) > 1:
        stems.append("".join(words[:-1]))
    stems.append(words[0])
    out: list[str] = []
    for stem in stems:
        if 3 <= len(stem) <= 40 and stem not in out:
            out.append(stem)
    return out


# Suffixes dental practices overwhelmingly use in their domain names.
PRACTICE_SUFFIXES = ("orthodontics", "ortho", "dental", "dentistry", "braces",
                     "smiles", "familydental", "dds", "dentalcare")
_HAS_SUFFIX_RE = re.compile("|".join(PRACTICE_SUFFIXES), re.I)


def pattern_stems(surnames: list[str] | None, city: str) -> list[str]:
    """Stems built from the ``<surname>orthodontics`` / ``dr<surname>`` habit."""
    out: list[str] = []
    seen = set()

    def add(stem: str) -> None:
        stem = re.sub(r"[^a-z0-9]", "", (stem or "").lower())
        if 5 <= len(stem) <= 34 and stem not in seen:
            seen.add(stem)
            out.append(stem)

    for surname in (surnames or [])[:3]:
        base = re.sub(r"[^A-Za-z]", "", surname).lower()
        if len(base) < 3:
            continue
        for suffix in ("orthodontics", "ortho", "dental", "dentistry", "braces", "smiles"):
            add(base + suffix)
        add("dr" + base)
        add("dr" + base + "ortho")
    city_slug = re.sub(r"[^A-Za-z]", "", city or "").lower()
    if 3 <= len(city_slug) <= 22:
        for suffix in ("orthodontics", "ortho", "braces", "dental", "dentistry"):
            add(city_slug + suffix)
    return out


def domain_candidates(*names: str, limit: int = 10) -> list[str]:
    """Build plausible domains from a practice's name(s).

    Ordered TLD-major so that the ``.com`` of every name variant is tried
    before falling back to ``.net``/``.dental``/etc.
    """
    stems: list[str] = []
    for name in names:
        for stem in name_stems(name):
            if stem not in stems:
                stems.append(stem)
    return build_candidates(stems, limit)


def build_candidates(stems: list[str], limit: int = MAX_CANDIDATES) -> list[str]:
    """Turn ordered stems into an ordered, hard-capped candidate domain list."""
    out: list[str] = []
    for stem in stems:
        cand = stem + PRIMARY_TLD
        if cand not in out:
            out.append(cand)
    for stem in stems[:2]:
        for tld in SECONDARY_TLDS:
            cand = stem + tld
            if cand not in out:
                out.append(cand)
    return out[:limit]


_DNS_CACHE: dict[str, bool] = {}
_DNS_LOCK = threading.Lock()


def resolves(domain: str) -> bool:
    """Cheap DNS pre-check so we never open a socket to a domain that is not registered."""
    with _DNS_LOCK:
        if domain in _DNS_CACHE:
            return _DNS_CACHE[domain]
    try:
        socket.getaddrinfo(domain, 443, proto=socket.IPPROTO_TCP)
        ok = True
    except OSError:
        ok = False
    with _DNS_LOCK:
        _DNS_CACHE[domain] = ok
    return ok


def _digits(value: str) -> str:
    return re.sub(r"\D", "", value or "")


def page_proves_practice(text: str, phone: str, zip5: str, city: str) -> str:
    """Return the evidence kind if ``text`` demonstrably belongs to the practice."""
    flat = re.sub(r"\D", "", text)
    phone_digits = _digits(phone)[-10:]
    if len(phone_digits) == 10 and phone_digits in flat:
        return "phone-match"
    low = text.lower()
    if zip5 and zip5 in text and city and city.lower() in low:
        return "city-zip-match"
    return ""


def extract_emails(text: str, domain: str = "") -> list[str]:
    found: list[str] = []
    for raw in EMAIL_RE.findall(text or ""):
        addr = raw.strip(".,;:'\"()<>").lower()
        if EMAIL_BLOCKLIST.search(addr) or len(addr) > 100:
            continue
        if addr not in found:
            found.append(addr)
    if domain:
        host = domain.replace("www.", "")
        found.sort(key=lambda a: (0 if a.endswith("@" + host) else 1, len(a)))
    return found[:5]


# Health-information-exchange domains: these Direct addresses are machine
# routing endpoints, not an inbox a human at the practice reads.
HIE_DOMAIN_RE = re.compile(
    r"(?:^|\.)(?:direct|cerner(?:direct)?|epic(?:hosted)?|surescripts|updox|"
    r"maxmd|medallies|nextgen|athenahealth|iqhealth|veradigm|allscripts|"
    r"netsmart|ntst|inteligent|hiedirect|secureexchange|datamotion|"
    r"medicity|kno2|globalmed|zixcorp)\b", re.I)

URLISH_RE = re.compile(r"^(?:https?://)?(?:www\.)?[A-Za-z0-9\-]+(?:\.[A-Za-z0-9\-]+)+"
                       r"(?:[:/?].*)?$")


def classify_endpoint(value: str) -> tuple[str, str]:
    """Classify one NPPES endpoint string as ``("email"|"website"|"", value)``.

    The endpoint column is free text and holds a mix of Direct addresses, real
    practice mailboxes, practice websites and junk ("Aurora", "WAUTOMA").
    """
    value = (value or "").strip()
    if not value or len(value) > 200:
        return "", ""
    if EMAIL_RE.fullmatch(value):
        domain = value.rsplit("@", 1)[-1].lower()
        if HIE_DOMAIN_RE.search(domain) or EMAIL_BLOCKLIST.search(value.lower()):
            return "", ""
        return "email", value.lower()
    if "@" in value:
        return "", ""
    if URLISH_RE.match(value):
        host = urlparse(value if value.startswith("http") else "https://" + value).netloc
        host = host.split(":")[0].lower()
        if not host or HIE_DOMAIN_RE.search(host):
            return "", ""
        # Machine API endpoints are not the practice's marketing site.
        if re.search(r"/(?:fhir|api|wcf|gateway|nhinservice|interconnect)", value, re.I):
            return "", ""
        return "website", value if value.startswith("http") else "https://" + value
    return "", ""


def endpoint_contacts(endpoints: list[dict]) -> dict[str, str]:
    """Collapse an NPI's endpoint rows into ``{"email": ..., "website": ...}``."""
    emails: list[str] = []
    websites: list[str] = []
    for ep in endpoints or []:
        kind, value = classify_endpoint(ep.get("endpoint", ""))
        if kind == "email" and value not in emails:
            emails.append(value)
        elif kind == "website" and value not in websites:
            websites.append(value)
    return {"email": "; ".join(emails[:3]), "website": websites[0] if websites else ""}


class SiteEnricher:
    def __init__(self, politeness: Politeness | None = None, max_pages: int = 4,
                 max_probes: int = 8):
        self.polite = politeness or Politeness()
        self.max_pages = max_pages
        self.max_probes = max_probes
        self.session = requests.Session()
        self.session.headers["User-Agent"] = USER_AGENT

    def _get(self, url: str) -> str:
        if not self.polite.allowed(url):
            return ""
        self.polite.wait(url)
        try:
            resp = self.session.get(url, timeout=REQUEST_TIMEOUT, allow_redirects=True)
        except requests.RequestException:
            return ""
        ctype = resp.headers.get("Content-Type", "")
        if resp.status_code != 200 or "html" not in ctype.lower():
            return ""
        if len(resp.content) > 3_000_000:
            return ""
        return resp.text

    def probe(self, domain: str, phone: str, zip5: str, city: str) -> tuple[str, str, str]:
        """Try a domain; return ``(final_url, html, evidence)`` or empty strings."""
        # https only, apex first: requests follows the redirect to www on its
        # own, so probing both host forms is wasted round-trips.
        hosts = [domain] if resolves(domain) else (
            ["www." + domain] if resolves("www." + domain) else [])
        for host in hosts:
            url = "https://" + host
            html = self._get(url)
            if not html:
                continue
            evidence = page_proves_practice(html, phone, zip5, city)
            if evidence:
                return url, html, evidence
            return "", "", ""  # site exists but isn't this practice
        return "", "", ""

    def _contact_urls(self, base_url: str, home_html: str) -> list[str]:
        """Contact-ish URLs linked from the home page, then the usual guesses."""
        base_host = urlparse(base_url).netloc.replace("www.", "")
        found: list[str] = []
        for href, text in CONTACT_LINK_RE.findall(home_html or ""):
            if href.lower().startswith(("mailto:", "tel:", "javascript:")):
                continue
            if not (CONTACT_HINT_RE.search(href) or CONTACT_HINT_RE.search(text)):
                continue
            url = urljoin(base_url, href.strip())
            if urlparse(url).netloc.replace("www.", "") != base_host:
                continue
            if url not in found:
                found.append(url)
        for path in CONTACT_PATHS:
            url = urljoin(base_url, path)
            if url not in found:
                found.append(url)
        return found

    def harvest(self, base_url: str, home_html: str, domain: str) -> list[str]:
        texts = [home_html]
        emails = extract_emails(home_html, domain)
        pages = 1
        for url in self._contact_urls(base_url, home_html):
            if pages >= self.max_pages or emails:
                break
            html = self._get(url)
            if html:
                texts.append(html)
                pages += 1
                emails = extract_emails("\n".join(texts), domain)
        return emails

    def enrich(self, record: dict) -> SiteResult:
        """Resolve a website + emails for one practice record."""
        npi = record.get("npi", "")
        phone = record.get("phone", "") or record.get("contact_phone", "")
        zip5 = record.get("zip5", "")
        city = record.get("city", "")

        # 1. Website already known from a registered NPPES endpoint.
        known = (record.get("endpoint_url") or "").strip()
        if known:
            url = known if known.startswith("http") else "https://" + known
            html = self._get(url)
            if html:
                domain = urlparse(url).netloc
                emails = self.harvest(url, html, domain)
                return SiteResult(npi, url, "; ".join(emails), "nppes-endpoint", "registered")

        # 2. Guess from the practice name, accept only on proof.
        names = [record.get("practice_name", ""), record.get("dba_name", ""),
                 record.get("org_name", "")]
        stems: list[str] = []
        for name in names:
            for stem in name_stems(name):
                if stem not in stems:
                    stems.append(stem)
        # A name with no dental word in it rarely maps to a bare domain, so also
        # try it with the usual practice suffixes appended.
        for stem in list(stems):
            if not _HAS_SUFFIX_RE.search(stem):
                for suffix in ("orthodontics", "ortho", "dental", "dentistry"):
                    if stem + suffix not in stems:
                        stems.append(stem + suffix)
        for stem in pattern_stems(record.get("_surnames"), city):
            if stem not in stems:
                stems.append(stem)
        stems = stems[:MAX_CANDIDATES]

        candidates = build_candidates(stems)

        probes = 0
        for domain in candidates:
            if probes >= self.max_probes:
                break
            if not (resolves(domain) or resolves("www." + domain)):
                continue
            probes += 1
            url, html, evidence = self.probe(domain, phone, zip5, city)
            if url:
                emails = self.harvest(url, html, domain)
                return SiteResult(npi, url, "; ".join(emails), "name-derived", evidence)
        return SiteResult(npi)


def enrich_many(records: list[dict], workers: int = 8, min_delay: float = 1.0,
                progress_every: int = 100) -> dict[str, SiteResult]:
    """Enrich a batch of practice records concurrently."""
    polite = Politeness(min_delay=min_delay)
    results: dict[str, SiteResult] = {}
    done = 0

    def work(rec: dict) -> SiteResult:
        return SiteEnricher(polite).enrich(rec)

    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(work, r): r for r in records}
        for fut in as_completed(futures):
            rec = futures[fut]
            try:
                res = fut.result()
            except Exception:
                res = SiteResult(rec.get("npi", ""))
            results[res.npi or rec.get("npi", "")] = res
            done += 1
            if progress_every and done % progress_every == 0:
                hits = sum(1 for r in results.values() if r.website)
                print(f"  enriched {done}/{len(records)} - {hits} sites found", flush=True)
    return results
