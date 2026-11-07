"""Pull creative research data from the Atria Open API.

    export ATRIA_API_KEY=atria-sk_...
    python ads/atria_pull.py winners --brand <brand>   # account from brand.json → atria_account
    python ads/atria_pull.py winners     # statics with >= $5k lifetime spend (since 2024)
    python ads/atria_pull.py losers      # statics < $200 spend, paused at ad level (last 12 months)
    python ads/atria_pull.py seasonal --week 2026-W45  # top spenders in the same window last year
    python ads/atria_pull.py rising    # new ads (last 30 days) with >= $300 spend and ROAS >= 1.8
    python ads/atria_pull.py current   # any ad in the last 30 days with >= $300 spend and ROAS >= 1.8
    python ads/atria_pull.py inspo       # image ads, rising impressions, launched last 30 days
    python ads/atria_pull.py inspiration # CURATED inspiration (user rule Oct 28): active static ads launched 7-45 days ago,
                                         # impressions growing week over week, oral care + health & wellness queries
    python ads/atria_pull.py competitors # top-impression ads: competitor_brands + inspo_queries keywords
    python ads/atria_pull.py wellness    # health & wellness image ads (any category), 45 days, active, 10+ days running
    python ads/atria_pull.py rivals      # EVERY ad (image + video) from brand.json -> core_competitors (Hike, Stepprs), full copy
    python ads/atria_pull.py ultrasonic  # ultrasonic-cleaner brands + dental-appliance category (brand.json → ultrasonic_queries), images and video

Writes CSVs to ads/brands/<brand>/research/data/. Atria returns at most 50 ads per date window, so
spend is summed across monthly (winners) or weekly (losers) windows; ads
that never made a window's top 50 are missed, which only affects very
low spenders in the winners pull.
"""

import argparse
import csv
import json
import datetime as dt
import os
import sys
import time
from pathlib import Path

import requests
from dotenv import load_dotenv

BASE = "https://api.tryatria.com/open/v1"
ACCOUNT_NAME = "WearOrtho"
DATA_DIR = Path(__file__).resolve().parent / "brands" / "comfortwear" / "research" / "data"
INSPO_QUERIES = [  # default; brand.json → inspo_queries overrides
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
    DATA_DIR.mkdir(parents=True, exist_ok=True)
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
    for q in args.queries:
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

def _num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def inspiration(api, acc, args):
    """Curated inspiration ads (user rule Oct 28). An ad qualifies only if ALL of these hold:
      - static image, currently active (status == active)
      - launched within the last --launched-within days (default 45)
      - ran at least --min-days days (default 7): start_date at least 7 days ago, so ads launched in the last 7 days are excluded
      - impressions growing week over week: Atria impression_trend == rising AND (reach grew over 7d OR impression rank improved over 7d)
    Queries come from brand.json -> inspiration_queries (oral care + health & wellness). Writes inspiration_curated.csv
    (sorted by impression percentile, best first) and prints how many ads each filter removed."""
    today = dt.date.today()
    since = (today - dt.timedelta(days=args.launched_within)).isoformat()
    newest = today - dt.timedelta(days=args.min_days)
    seen, stats = {}, {"fetched": 0, "not_image/active": 0, "too_new(<%dd)" % args.min_days: 0, "too_old": 0,
                       "not_growing": 0, "non_english": 0}
    for q in args.inspiration_queries:
        cursor = None
        for _ in range(args.pages):
            params = {"query": q, "display_format": "image", "impression_trend": "rising", "launched_after": since,
                      "status": "active", "order": "most_impressions", "page_size": 50}
            if cursor:
                params["cursor"] = cursor
            try:
                data = api.get("ad-library/search", params)
            except Exception as e:  # keep going: one bad query must not kill the pull
                print(f"  {q}: {e}")
                break
            for it in data.get("items", []):
                stats["fetched"] += 1
                if it.get("status") != "active" or it.get("media_format", "image") != "image":
                    stats["not_image/active"] += 1
                    continue
                start = (it.get("start_date") or "")[:10]
                if not start:
                    stats["too_old"] += 1
                    continue
                started = dt.date.fromisoformat(start)
                if started > newest or (it.get("days_running") or 0) < args.min_days:
                    stats["too_new(<%dd)" % args.min_days] += 1
                    continue
                if started < today - dt.timedelta(days=args.launched_within):
                    stats["too_old"] += 1
                    continue
                if it.get("language") not in (None, "en"):
                    stats["non_english"] += 1
                    continue
                rank = it.get("impression_rank") or {}
                reach = it.get("reach") or {}
                grew = (it.get("impression_trend") == "rising"
                        and ((_num(reach.get("delta_7d")) or 0) > 0 or (_num(rank.get("rank_delta_7d")) or 0) < 0
                             or (_num(rank.get("percentile_change_7d")) or 0) < 0))
                if not grew:
                    stats["not_growing"] += 1
                    continue
                seen.setdefault(it["id"], {**it, "query": q})
            cursor = data.get("cursor")
            if not cursor or len(data.get("items", [])) < 50:
                break
            time.sleep(0.8)
        time.sleep(0.8)
    rows = []
    for it in seen.values():
        rank = it.get("impression_rank") or {}
        latest = rank.get("latest_rank") or {}
        reach = it.get("reach") or {}
        rows.append({"brand": it["brand_name"], "query": it["query"], "start_date": (it.get("start_date") or "")[:10],
                     "days_running": it["days_running"], "impression_percentile": latest.get("percentile"),
                     "rank_delta_7d": rank.get("rank_delta_7d"), "percentile_change_7d": rank.get("percentile_change_7d"),
                     "reach_pct_change_7d": reach.get("pct_change_7d"), "reach_latest": reach.get("latest"),
                     "title": it.get("title"), "body": (it.get("body") or "")[:600], "cta": it.get("cta_text"),
                     "image_url": (it.get("images") or [{}])[0].get("url"), "landing_url": it.get("link_url")})
    rows.sort(key=lambda r: r["impression_percentile"] if r["impression_percentile"] is not None else 9)
    print("Filter log:", stats, "-> kept", len(rows))
    write_csv("inspiration_curated.csv", rows, list(rows[0]) if rows else ["brand"])


def wellness(api, acc, args):
    """Objective health & wellness inspiration (user rules 2026-10-28). Data only, no hand-picking:
    image ads, active, launched in the last `wellness.launched_days` days (45), running at least
    `wellness.min_days_running` days (10), impressions RISING, found with health & wellness category
    keywords only (brand.json -> wellness.queries; never our own angle words like nurse/travel/Disney).
    Keeps only DIRECT-RESPONSE ads (title/body has an offer, CTA, guarantee, number or problem hook:
    wellness.dr_signals), drops off-niche ads (wellness.exclude), max `wellness.per_brand` per brand, and
    ranks by impression growth: growth = -rank_delta_7d (places climbed in 7 days), then impression share.
    Writes inspiration_wellness_<days>d.csv with a `growth_rank` column; formats are taken from the top
    of this list in order, skipping only formats already in research/format_ledger.json.
    """
    import re
    cfg = args.wellness
    days, min_days, per_brand = cfg.get("launched_days", 45), cfg.get("min_days_running", 10), cfg.get("per_brand", 2)
    exclude = [w.lower() for w in cfg.get("exclude", [])]
    dr = re.compile(cfg.get("dr_signals", r"%|\$|off\b|free|guarantee|money.back|risk.free|buy \d|get \d|shop|order|try|today|tonight|sale|deal|save|ends|limited|relief|pain|\?"), re.I)
    since = (dt.date.today() - dt.timedelta(days=days)).isoformat()
    seen = {}
    for q in cfg.get("queries", []):
        for order in ("most_impressions", "best_match"):
            try:
                items = api.get("ad-library/search", {"query": q, "display_format": "image", "launched_after": since,
                                                      "status": "active", "impression_trend": "rising",
                                                      "order": order, "page_size": 50})["items"]
            except Exception as e:
                print(f"  {q} {order}: {e}")
                continue
            for it in items:
                seen.setdefault(it["id"], {**it, "query": q})
            time.sleep(0.6)
    rows, drop = [], {"days": 0, "off_niche": 0, "not_dr": 0}
    for it in seen.values():
        if (it.get("days_running") or 0) < min_days:
            drop["days"] += 1
            continue
        text = f"{it.get('brand_name', '')} {it.get('title') or ''} {it.get('body') or ''}".lower()
        if any(w in text for w in exclude):
            drop["off_niche"] += 1
            continue
        if not dr.search(f"{it.get('title') or ''} {it.get('body') or ''}"):
            drop["not_dr"] += 1
            continue
        rank = it.get("impression_rank") or {}
        latest = rank.get("latest_rank") or {}
        delta = rank.get("rank_delta_7d")
        rows.append({"brand": it["brand_name"], "query": it["query"], "days_running": it["days_running"],
                     "growth_7d": -delta if delta is not None else None, "rank_delta_7d": delta,
                     "impression_percentile": latest.get("percentile"),
                     "title": " ".join((it.get("title") or "").split()),
                     "body": " ".join((it.get("body") or "").split())[:400],
                     "image_url": (it.get("images") or [{}])[0].get("url"), "landing_url": it.get("link_url")})
    rows.sort(key=lambda r: (-(r["growth_7d"] if r["growth_7d"] is not None else -1e9),
                             r["impression_percentile"] if r["impression_percentile"] is not None else 9))
    kept, per = [], {}
    for r in rows:
        if per.get(r["brand"], 0) < per_brand:
            per[r["brand"]] = per.get(r["brand"], 0) + 1
            r["growth_rank"] = len(kept) + 1
            kept.append(r)
    print(f"{len(seen)} rising ads found; dropped {drop}; {len(kept)} kept (max {per_brand} per brand), ranked by 7-day impression growth")
    write_csv(f"inspiration_wellness_{days}d.csv", kept, list(kept[0]) if kept else ["brand"])


def ultrasonic(api, acc, args):
    """Ads from other ultrasonic cleaner brands (Zima, Sonic Dental, Ploise, oPro, Novapod, iSonic...) and
    the dental-appliance category (denture/retainer/night guard/aligner cleaners). Queries come from
    brand.json -> ultrasonic_queries; no brand filter, so any advertiser running them shows up. Images and
    video, top by impressions, plus most_recent for what is new. Writes ultrasonic_ads.csv.
    """
    seen = {}
    for query in args.ultra_queries:
        for fmt in ("image", "video"):
            for order in ("most_impressions", "best_match"):
                try:
                    items = api.get("ad-library/search", {"query": query, "display_format": fmt,
                                                          "order": order, "page_size": 50})["items"]
                except Exception as e:
                    print(f"  {query} {fmt} {order}: {e}")
                    continue
                for it in items:
                    seen.setdefault(it["id"], {**it, "query": query, "fmt": fmt})
                time.sleep(0.6)
    rows = []
    for it in seen.values():
        latest = (it.get("impression_rank") or {}).get("latest_rank") or {}
        rows.append({"brand": it["brand_name"], "query": it["query"], "format": it["fmt"],
                     "impression_percentile": latest.get("percentile"), "impression_rank": latest.get("rank"),
                     "days_running": it["days_running"], "status": it.get("status"), "title": it.get("title"),
                     "body": (it.get("body") or "")[:900],
                     "image_url": (it.get("images") or [{}])[0].get("url") or it.get("thumbnail_url"),
                     "landing_url": it.get("link_url")})
    rows.sort(key=lambda r: (r["impression_percentile"] if r["impression_percentile"] is not None else 9))
    write_csv("ultrasonic_ads.csv", rows, list(rows[0]) if rows else ["brand"])


def competitors(api, acc, args):
    """Top-impression ads from competitor and adjacent brands (brand.json → competitor_brands), plus the
    top-impression image ads for each category keyword (inspo_queries). Atria ranks by impressions, so these
    are the statics getting the most delivery right now, not just the longest-running.
    """
    seen = {}

    def add(items, query, fmt, brand_filter):
        key = brand_filter.lower().replace(" ", "") if brand_filter else ""
        for it in items:
            if key and key not in (it.get("brand_name") or "").lower().replace(" ", ""):
                continue
            seen.setdefault(it["id"], {**it, "query": query, "fmt": fmt})

    searches = [(name, fmt, name) for name in args.competitors for fmt in ("image", "video")]
    searches += [(q, "image", "") for q in args.queries]
    for query, fmt, brand_filter in searches:
        try:
            items = api.get("ad-library/search", {"query": query, "display_format": fmt,
                                                  "order": "most_impressions", "page_size": 50})["items"]
        except Exception as e:  # one bad query shouldn't stop the pull
            print(f"  {query} {fmt}: {e}")
            continue
        add(items, query, fmt, brand_filter)
        time.sleep(0.8)
    rows = []
    for it in seen.values():
        latest = (it.get("impression_rank") or {}).get("latest_rank") or {}
        rows.append({"brand": it["brand_name"], "query": it["query"], "format": it["fmt"],
                     "impression_percentile": latest.get("percentile"), "impression_rank": latest.get("rank"),
                     "days_running": it["days_running"], "status": it.get("status"), "title": it.get("title"),
                     "body": (it.get("body") or "")[:700],
                     "image_url": (it.get("images") or [{}])[0].get("url") or it.get("thumbnail_url"),
                     "landing_url": it.get("link_url")})
    rows.sort(key=lambda r: (r["impression_percentile"] if r["impression_percentile"] is not None else 9))
    write_csv("competitor_ads.csv", rows, list(rows[0]) if rows else ["brand"])


def rivals(api, acc, args):
    """Deep study of the core competitors (brand.json -> core_competitors; Comfort Wear: Hike Footwear, Stepprs).
    Pulls their ads in every order Atria offers (most impressions, best match), images AND videos, active and
    inactive, keeps only that brand's ads, and saves the FULL title/body so the copy can be studied line by line.
    Writes research/data/core_competitors_<date>.csv sorted by brand, then status (active first), then days running
    (longest first: the ads they keep paying for are the ones that work)."""
    seen = {}
    for name in args.core_competitors:
        key = name.lower().replace(" ", "").replace("-", "")
        for fmt in ("image", "video"):
            for order in ("most_impressions", "best_match"):
                try:
                    items = api.get("ad-library/search", {"query": name, "display_format": fmt, "order": order,
                                                          "page_size": 50})["items"]
                except Exception as e:
                    print(f"  {name} {fmt} {order}: {e}")
                    continue
                for it in items:
                    if key in (it.get("brand_name") or "").lower().replace(" ", "").replace("-", ""):
                        seen.setdefault(it["id"], {**it, "competitor": name, "fmt": fmt})
                time.sleep(0.6)
    rows = []
    for it in seen.values():
        rank = it.get("impression_rank") or {}
        latest = rank.get("latest_rank") or {}
        rows.append({"competitor": it["competitor"], "brand": it.get("brand_name"), "format": it["fmt"],
                     "status": it.get("status"), "days_running": it.get("days_running"),
                     "start_date": it.get("start_date"), "impression_percentile": latest.get("percentile"),
                     "rank_delta_7d": rank.get("rank_delta_7d"), "atria_id": it["id"],
                     "title": " ".join((it.get("title") or "").split()),
                     "body": " ".join((it.get("body") or "").split()),
                     "image_url": (it.get("images") or [{}])[0].get("url") or it.get("thumbnail_url"),
                     "landing_url": it.get("link_url")})
    rows.sort(key=lambda r: (r["competitor"], r["status"] != "active", -(r["days_running"] or 0)))
    counts = {n: sum(r["competitor"] == n for r in rows) for n in args.core_competitors}
    print(f"{len(rows)} ads: {counts}")
    write_csv(f"{args.out_prefix}_{dt.date.today()}.csv", rows, list(rows[0]) if rows else ["competitor"])


def seasonal(api, acc, args):
    """Top-spending ads (all formats) in the same calendar window last year as the target week.

    The weekly batch turns these into statics: a video that won in early November last year
    becomes static versions for early November this year.
    """
    year, week = (int(x) for x in args.week.split("-W"))
    monday = dt.date.fromisocalendar(year, week, 1)
    start = monday - dt.timedelta(days=364 + args.pad_days)  # same weekday, one year earlier
    end = monday - dt.timedelta(days=364 - 6 - args.pad_days)
    agg = aggregate(api, acc, start, end, "week")
    top = sorted(agg.items(), key=lambda kv: -kv[1]["spend"])[:args.top]
    rows = []
    for ad_id, r in top:
        detail = api.get(f"ad-accounts/{acc}/ads/{ad_id}", {"period": "last_7d"})
        c = detail.get("creative") or {}
        # transcript field name isn't documented; keep whichever one the API returns
        transcript = detail.get("transcript") or c.get("transcript") or (c.get("video") or {}).get("transcript")
        rows.append({**r, "platform_ad_id": ad_id, "roas": round(r["revenue"] / r["spend"], 2) if r["spend"] else 0,
                     "headline": c.get("title"), "primary_text": (c.get("body") or "")[:800],
                     "transcript": (transcript or "")[:4000]})
        time.sleep(0.7)
    print(f"Window {start} to {end} (target week {args.week})")
    write_csv(f"seasonal_{args.week}.csv", rows, ["platform_ad_id", "ad_name", "format", "status", "spend",
              "roas", "purchases", "headline", "primary_text", "transcript", "thumbnail_url"])


def rising(api, acc, args):
    """Recently launched ads (any format) that already hit the iteration bar: spend >= --min-spend
    and ROAS >= --min-roas over the last --days. "Recently launched" = no spend in the 60 days before
    that window (Atria exposes no launch date). Each one gets static iterations in the next batch.
    """
    end = dt.date.today() - dt.timedelta(days=1)
    start = end - dt.timedelta(days=args.days - 1)
    recent = aggregate(api, acc, start, end, "week")
    before = None if args.what == "current" else aggregate(
        api, acc, start - dt.timedelta(days=60), start - dt.timedelta(days=1), "week")
    rows = []
    for ad_id, r in recent.items():
        roas = r["revenue"] / r["spend"] if r["spend"] else 0
        if (before is not None and ad_id in before) or r["spend"] < args.min_spend_rising or roas < args.min_roas:
            continue
        detail = api.get(f"ad-accounts/{acc}/ads/{ad_id}", {"period": "last_7d"})
        c = detail.get("creative") or {}
        name = r["ad_name"]
        rows.append({**r, "platform_ad_id": ad_id, "roas": round(roas, 2),
                     "audience": "retargeting" if name.upper().startswith("RTG") else "prospecting",
                     "headline": c.get("title"), "primary_text": (c.get("body") or "")[:800]})
        time.sleep(0.7)
    rows.sort(key=lambda r: -r["roas"] * r["spend"])
    print(f"Window {start} to {end}: {len(rows)} {'' if before is None else 'new '}ads with spend >= ${args.min_spend_rising:.0f} and ROAS >= {args.min_roas}")
    write_csv("current_winners.csv" if before is None else "rising_winners.csv", rows, ["platform_ad_id", "ad_name", "format", "audience", "status", "spend",
              "roas", "purchases", "headline", "primary_text", "thumbnail_url"])


def main():
    load_dotenv()
    p = argparse.ArgumentParser()
    p.add_argument("what", choices=["winners", "losers", "inspo", "inspiration", "seasonal", "rising", "current", "competitors", "ultrasonic", "wellness", "rivals"])
    p.add_argument("--days", type=int, default=30, help="rising: look-back window in days")
    p.add_argument("--min-spend-rising", type=float, default=300, help="rising: minimum spend in the window")
    p.add_argument("--min-roas", type=float, default=1.8, help="rising: minimum ROAS in the window")
    p.add_argument("--week", help="seasonal: target ISO week, e.g. 2026-W45 (default: next week)")
    p.add_argument("--pad-days", type=int, default=7, help="seasonal: widen last year's window by this many days each side")
    p.add_argument("--top", type=int, default=15, help="seasonal: how many top-spending ads to keep")
    p.add_argument("--min-spend", type=float, default=5000)
    p.add_argument("--max-spend", type=float, default=200)
    p.add_argument("--launched-within", type=int, default=45, help="inspiration: ads launched in the last N days")
    p.add_argument("--min-days", type=int, default=7, help="inspiration: must have run at least N days (excludes ads launched in the last N days)")
    p.add_argument("--pages", type=int, default=2, help="inspiration: result pages (50 ads each) per query")
    p.add_argument("--brand", default=os.getenv("ADS_BRAND", "comfortwear"))
    p.add_argument("--account", help="ad account name in Atria (default: brand.json → atria_account)")
    p.add_argument("--wide", action="store_true", help="rivals: also pull brand.json -> angle_rivals (angle-gap study)")
    args = p.parse_args()
    global DATA_DIR
    bdir = Path(__file__).resolve().parent / "brands" / args.brand
    DATA_DIR = bdir / "research" / "data"
    brand = json.loads((bdir / "brand.json").read_text())
    args.account = args.account or brand.get("atria_account", ACCOUNT_NAME)
    args.queries = brand.get("inspo_queries", INSPO_QUERIES)
    args.inspiration_queries = brand.get("inspiration_queries", args.queries)
    args.competitors = brand.get("competitor_brands", [])
    args.core_competitors = brand.get("core_competitors", []) + (brand.get("angle_rivals", []) if args.wide else [])
    args.out_prefix = "angle_rivals" if args.wide else "core_competitors"
    args.ultra_queries = brand.get("ultrasonic_queries", [])
    args.wellness = brand.get("wellness", {})
    # Without ATRIA_API_KEY the request relies on a network secret the proxy attaches.
    api = Atria(os.getenv("ATRIA_API_KEY"))
    acc = api.account_id(args.account)
    if not args.week:
        y, w, _ = (dt.date.today() + dt.timedelta(days=7)).isocalendar()
        args.week = f"{y}-W{w:02d}"
    {"winners": winners, "losers": losers, "inspo": inspo, "inspiration": inspiration, "seasonal": seasonal, "rising": rising, "current": rising, "competitors": competitors, "ultrasonic": ultrasonic, "wellness": wellness, "rivals": rivals}[args.what](api, acc, args)


if __name__ == "__main__":
    main()
