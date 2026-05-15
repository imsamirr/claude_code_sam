"""Look up a Yuntrack tracking number and return a normalized status + days-in-transit.

This module is designed to run inside a Claude Code session where the
environment's network allowlist includes yuntrack.com. The default endpoint is
the public JSON API used by the parcel-tracking web app.

The exact response schema may evolve; the parser falls back to a generic
"latest event description" reading. Run __main__ for a quick smoke test:
    python scripts/yuntrack.py YT2604300702459959 [YT...]
"""

from __future__ import annotations

import dataclasses
import hashlib
import hmac
import json
import re
import sys
import time
from datetime import datetime, timezone
from typing import Optional

import requests

API_URL = "https://services.yuntrack.com/Track/Query"
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)
# HMAC-SHA256 secret extracted from yuntrack.com's app bundle (utils.getSign).
# Public-facing key embedded in their SPA; required for unauthenticated lookups.
SIGN_KEY = b"f3c42837e3b46431ddf5d7db7d67017d"

# Map sheet vocabulary -> phrases that appear in yuntrack event descriptions / status text.
# Order matters: first match wins, so put the most specific buckets first.
STATUS_PATTERNS: list[tuple[str, list[str]]] = [
    ("Delivered", ["delivered", "signed", "pickup completed", "received by recipient"]),
    ("Out For Delivery", ["out for delivery", "with courier for delivery"]),
    ("Ready for Pick Up", ["ready for pickup", "available for pickup", "awaiting collection", "held at"]),
    ("Returned to sender", ["return to sender", "returned to sender", "returning", "abandoned"]),
    ("Unable to Deliver", ["unable to deliver", "delivery failed", "delivery attempt failed", "address incorrect", "rejected by"]),
    ("Fulfilled But Not Shipped", ["shipment information received"]),
    ("In transit", ["in transit", "arrived at", "departed from", "processed", "accepted", "handed over", "in custom", "cleared customs"]),
]


@dataclasses.dataclass
class TrackingResult:
    tracking_number: str
    shipping_update: str       # normalized to sheet vocabulary
    days_in_transit: str       # e.g. "12 Days"
    raw_status: str = ""       # original status text from yuntrack
    last_event_date: Optional[str] = None
    last_event_description: Optional[str] = None
    first_event_date: Optional[str] = None
    error: Optional[str] = None

    def to_update(self, row: int) -> dict:
        return {
            "row": row,
            "shipping_update": self.shipping_update,
            "days_in_transit": self.days_in_transit,
        }


def _normalize_status(text: str) -> str:
    t = text.lower()
    for canonical, patterns in STATUS_PATTERNS:
        for p in patterns:
            if p in t:
                return canonical
    return "In transit"


def _parse_date(s: str) -> Optional[datetime]:
    if not s:
        return None
    # Yuntrack uses ISO-ish strings like "2026-05-10 14:23:00" or with 'T'.
    for fmt in ("%Y-%m-%dT%H:%M:%S", "%Y-%m-%d %H:%M:%S", "%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%d"):
        try:
            return datetime.strptime(s[:19], fmt).replace(tzinfo=timezone.utc)
        except ValueError:
            continue
    return None


def _days_between(start: Optional[datetime], end: Optional[datetime]) -> Optional[int]:
    if not start or not end:
        return None
    delta = end - start
    return max(delta.days, 0)


def _extract_events(payload: dict) -> list[dict]:
    """Best-effort: peel back the layers of yuntrack's response to find an event list."""
    candidates = []

    def walk(obj):
        if isinstance(obj, list):
            if obj and isinstance(obj[0], dict) and any(
                k.lower() in {"trackdate", "processdate", "processcontent", "description", "date"}
                for k in obj[0].keys()
            ):
                candidates.append(obj)
            for x in obj:
                walk(x)
        elif isinstance(obj, dict):
            for v in obj.values():
                walk(v)

    walk(payload)
    candidates.sort(key=len, reverse=True)
    return candidates[0] if candidates else []


def _event_field(ev: dict, *names: str) -> str:
    for n in names:
        for k, v in ev.items():
            if k.lower() == n.lower() and v:
                return str(v)
    return ""


def _sign_body(number_list: list[str]) -> dict:
    """Build the signed request body that yuntrack's public API requires."""
    ts = int(time.time() * 1000)
    nl_json = json.dumps(number_list, separators=(",", ":"))
    msg = f"Timestamp={ts}&NumberList={nl_json}"
    sig = hmac.new(SIGN_KEY, msg.encode(), hashlib.sha256).hexdigest()
    return {
        "NumberList": number_list,
        "Year": 0,
        "Timestamp": ts,
        "Signature": sig,
    }


def lookup_one(tracking_number: str, session: Optional[requests.Session] = None) -> TrackingResult:
    s = session or requests.Session()
    try:
        r = s.post(
            API_URL,
            json=_sign_body([tracking_number]),
            headers={
                "Content-Type": "application/json;charset=UTF-8",
                "Accept": "application/json, text/plain, */*",
                "Authorization": "Nebula token:",
                "User-Agent": USER_AGENT,
                "Referer": "https://www.yuntrack.com/parcelTracking",
                "Origin": "https://www.yuntrack.com",
            },
            timeout=20,
        )
        r.raise_for_status()
        payload = r.json()
    except Exception as e:
        return TrackingResult(
            tracking_number=tracking_number,
            shipping_update="",
            days_in_transit="",
            error=f"HTTP/JSON error: {e}",
        )

    # Pull the numeric Status from ResultList[0] — authoritative for "Delivered".
    # Text events like "Delivered to local carrier" can otherwise produce false positives.
    status_code: Optional[int] = None
    result_list = payload.get("ResultList") if isinstance(payload, dict) else None
    if isinstance(result_list, list) and result_list and isinstance(result_list[0], dict):
        raw_code = result_list[0].get("Status")
        try:
            status_code = int(raw_code) if raw_code is not None else None
        except (TypeError, ValueError):
            status_code = None

    events = _extract_events(payload)
    if not events:
        if isinstance(result_list, list) and not result_list:
            return TrackingResult(
                tracking_number=tracking_number,
                shipping_update="",
                days_in_transit="",
                error="No tracking record found (ResultList empty)",
            )
        return TrackingResult(
            tracking_number=tracking_number,
            shipping_update="",
            days_in_transit="",
            error="No events found in response (schema may have changed)",
        )

    # Normalize to (date, description) tuples and sort newest-first.
    parsed = []
    for ev in events:
        date_str = _event_field(ev, "TrackDate", "ProcessDate", "CreatedOn", "Date", "EventTime")
        desc = _event_field(ev, "ProcessContent", "Description", "TrackContent", "Event", "StatusDescription")
        dt = _parse_date(date_str)
        parsed.append((dt, desc, date_str))

    parsed = [(d, desc, raw) for d, desc, raw in parsed if d or desc]
    if not parsed:
        return TrackingResult(
            tracking_number=tracking_number,
            shipping_update="",
            days_in_transit="",
            error="Events present but no parseable dates/descriptions",
        )

    parsed.sort(key=lambda x: x[0] or datetime.min.replace(tzinfo=timezone.utc), reverse=True)
    latest_dt, latest_desc, latest_raw = parsed[0]
    first_dt = next((d for d, _, _ in reversed(parsed) if d), None)

    raw_status = latest_desc or ""
    text_normalized = _normalize_status(raw_status)

    # Status code 50 = Delivered (final). Trust the numeric code over event text,
    # since intermediate events like "Delivered to local carrier" would otherwise
    # be misclassified as Delivered.
    if status_code == 50:
        normalized = "Delivered"
    elif text_normalized == "Delivered" and status_code is not None and status_code != 50:
        normalized = "In transit"
    else:
        normalized = text_normalized

    # Compute days-in-transit.
    if normalized == "Delivered" and first_dt and latest_dt:
        days = _days_between(first_dt, latest_dt)
    elif first_dt:
        days = _days_between(first_dt, datetime.now(timezone.utc))
    else:
        days = None

    return TrackingResult(
        tracking_number=tracking_number,
        shipping_update=normalized,
        days_in_transit=f"{days} Days" if days is not None else "",
        raw_status=raw_status,
        last_event_date=latest_raw or None,
        last_event_description=latest_desc or None,
        first_event_date=parsed[-1][2] if parsed else None,
    )


def lookup_many(tracking_numbers: list[str], delay: float = 1.0) -> list[TrackingResult]:
    """Sequential lookups with a small inter-request delay to be polite to yuntrack."""
    session = requests.Session()
    results = []
    for i, n in enumerate(tracking_numbers):
        results.append(lookup_one(n, session))
        if i < len(tracking_numbers) - 1:
            time.sleep(delay)
    return results


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/yuntrack.py <tracking_number> [more...]")
        sys.exit(1)
    for r in lookup_many(sys.argv[1:]):
        print(r)
