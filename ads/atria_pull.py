"""Pull creative research data from the Atria Open API.

    export ATRIA_API_KEY=atria-sk_...
    python ads/atria_pull.py winners     # statics with >= $5k lifetime spend (since 2024)
    python ads/atria_pull.py losers      # statics < $200 spend, paused at ad level (last 12 months)
    python ads/atria_pull.py inspo       # image ads, rising impressions, launched last 30 days

Writes CSVs to ads/data/. Atria returns at most 50 ads per date window, so
spend is summed across monthly (winners) or weekly (losers) windows; ads
that never made a window's top 50 are missed, which only affects very
low spenders in the winners pull.
"""

import argparse
import csv
import datetime as dt
import os
import sys
import time
from pathlib import Path

import requests
from dotenv import load_dotenv

BASE = "https://api.tryatria.com/open/v1"
ACCOUNT_NAME = "WearOrtho"
DATA_DIR = Path(__file__).resolve().parent / "data"
INSPO_QUERIES = [
    "orthopedic shoes", "plantar fasciitis", "nurse shoes", "foot pain", "wide toe box",
    "comfort shoes", "walking shoes", "bunions", "neuropathy", "standing all day",
    "heel pain", "arch support", "swollen feet",
]


class Atria:
    def __init__(self, key):
        self.s = requests.Session()
        if key:
            self.s.headers["X-API-Key"] = key

    def get(self, path, params=None):
        for attempt in range(6):
            r = self.s.get(f"{BASE}/{path}", params=params, timeout=180)
            if r.status_code in (429, 502, 503, 504):
                time.sleep(3 * 2 ** attempt)
                continue
            r.raise_for_status()
            body = r.json()
            if body.get("code") != 0:
                raise RuntimeError(f"{path}: {body.get('code')} {body.get('message')}")
            return body["data"]
        raise RuntimeError(f"{path}: gave up after retries")

    def account_id(self, name):
        for a in self.get("ad-accounts")["items"]:
            if a["name"] == name:
                return a["id"]
        sys.exit(f"Ad account {name!r} not found in this Atria workspace.")

    def top_ads(self, acc, start, stop):
        return self.get(f"ad-accounts/{acc}/ads", {
            "period": "custom", "date_start": str(start), "date_stop": str(stop),
            "sort_by": "spend", "limit": 50,
        })["items"]


def windows(start, end, step):
    d = start
    while d <= end:
        if step == "month":
            nxt = (d.replace(day=28) + dt.timedelta(days=4)).replace(day=1)
        else:
            nxt = d + dt.timedelta(days=7)
        yield d, min(nxt - dt.timedelta(days=1), end)
        d = nxt


def aggregate(api, acc, start, end, step):
    agg = {}
    for a, b in windows(start, end, step):
        for it in api.top_ads(acc, a, b):
            row = agg.setdefault(it["platform_ad_id"], {
                "ad_name": it["ad_name"], "format": it["asset_format"], "status": it["status"],
                "thumbnail_url": it["thumbnail_url"], "spend": 0.0, "revenue": 0.0,
                "purchases": 0.0, "impressions": 0, "clicks": 0,
            })
            m = it["metrics"]
            spend = m.get("spend") or 0
            row["spend"] += spend
            row["revenue"] += (m.get("roas") or 0) * spend
            row["purchases"] += m.get("purchases") or 0
            row["impressions"] += m.get("impressions") or 0
            row["clicks"] += m.get("clicks_all") or 0
        time.sleep(0.7)
    return agg


def write_csv(name, rows, fields):
    DATA_DIR.mkdir(exist_ok=True)
    path = DATA_DIR / name
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    print(f"Wrote {len(rows)} rows to {path}")


def winners(api, acc, args):
    yesterday = dt.date.today() - dt.timedelta(days=1)
    agg = aggregate(api, acc, dt.date(2024, 1, 1), yesterday, "month")
    rows = []
    for ad_id, r in agg.items():
        if r["format"] == "VIDEO" or r["spend"] < args.min_spend:
            continue
        detail = api.get(f"ad-accounts/{acc}/ads/{ad_id}", {"period": "last_7d"})
        c = detail.get("creative") or {}
        imgs = c.get("images") or []
        rows.append({**r, "platform_ad_id": ad_id, "roas": round(r["revenue"] / r["spend"], 2),
                     "headline": c.get("title"), "primary_text": c.get("body"),
                     "image_url": imgs[0]["url"] if imgs else r["thumbnail_url"]})
        time.sleep(0.7)
    rows.sort(key=lambda r: -r["spend"])
    write_csv("winning_statics_raw.csv", rows, ["platform_ad_id", "ad_name", "status", "spend", "roas",
              "purchases", "headline", "primary_text", "image_url"])


def losers(api, acc, args):
    yesterday = dt.date.today() - dt.timedelta(days=1)
    agg = aggregate(api, acc, yesterday - dt.timedelta(days=365), yesterday, "week")
    rows = [{**r, "platform_ad_id": k, "ctr_pct": round(100 * r["clicks"] / max(r["impressions"], 1), 2)}
            for k, r in agg.items()
            if r["format"] == "IMAGE" and 0 < r["spend"] < args.max_spend and r["status"] == "PAUSED"]
    rows.sort(key=lambda r: r["spend"])
    write_csv("losing_statics_raw.csv", rows, ["platform_ad_id", "ad_name", "spend", "purchases",
              "ctr_pct", "thumbnail_url"])


def inspo(api, acc, args):
    since = (dt.date.today() - dt.timedelta(days=30)).isoformat()
    seen = {}
    for q in INSPO_QUERIES:
        items = api.get("ad-library/search", {
            "query": q, "display_format": "image", "impression_trend": "rising",
            "launched_after": since, "status": "active", "order": "best_match", "page_size": 50,
        })["items"]
        for it in items:
            seen.setdefault(it["id"], {**it, "query": q})
        time.sleep(0.8)
    rows = []
    for it in seen.values():
        rank = it.get("impression_rank") or {}
        latest = rank.get("latest_rank") or {}
        rows.append({"brand": it["brand_name"], "query": it["query"], "days_running": it["days_running"],
                     "impression_percentile": latest.get("percentile"),
                     "rank_delta_7d": rank.get("rank_delta_7d"), "title": it.get("title"),
                     "body": (it.get("body") or "")[:500],
                     "image_url": (it.get("images") or [{}])[0].get("url"), "landing_url": it.get("link_url")})
    rows.sort(key=lambda r: r["impression_percentile"] if r["impression_percentile"] is not None else 9)
    write_csv("inspiration_raw.csv", rows, list(rows[0]) if rows else ["brand"])


def main():
    load_dotenv()
    p = argparse.ArgumentParser()
    p.add_argument("what", choices=["winners", "losers", "inspo"])
    p.add_argument("--min-spend", type=float, default=5000)
    p.add_argument("--max-spend", type=float, default=200)
    args = p.parse_args()
    # Without ATRIA_API_KEY the request relies on a network secret the proxy attaches.
    api = Atria(os.getenv("ATRIA_API_KEY"))
    acc = api.account_id(ACCOUNT_NAME)
    {"winners": winners, "losers": losers, "inspo": inspo}[args.what](api, acc, args)


if __name__ == "__main__":
    main()
