"""Pull creative research data from the Atria Open API.

    export ATRIA_API_KEY=atria-sk_...
    python ads/atria_pull.py winners --brand <brand>   # account from brand.json → atria_account
    python ads/atria_pull.py winners     # statics with >= $5k lifetime spend (since 2024)
    python ads/atria_pull.py losers      # statics < $200 spend, paused at ad level (last 12 months)
    python ads/atria_pull.py seasonal --week 2026-W45  # top spenders in the same window last year
    python ads/atria_pull.py rising    # new ads (last 30 days) with >= $300 spend and ROAS >= 1.8
    python ads/atria_pull.py current   # any ad in the last 30 days with >= $300 spend and ROAS >= 1.8
    python ads/atria_pull.py inspo       # image ads, rising impressions, launched last 30 days
    python ads/atria_pull.py competitors # competitor + adjacent brands' ads (brand.json → competitor_brands)
    python ads/atria_pull.py longform    # top PROSPECTING script families (last 90d) + copy + transcripts for long-form ads

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


def competitors(api, acc, args):
    """Image ads from named competitor and adjacent brands (brand.json → competitor_brands), longest-running first.

    Long-running ads are the ones those brands keep paying for, so they are the proven formats to borrow.
    """
    seen = {}
    for name in args.competitors:
        for fmt in ("image", "video"):
            try:
                items = api.get("ad-library/search", {"query": name, "display_format": fmt,
                                                      "order": "best_match", "page_size": 50})["items"]
            except Exception as e:  # one bad query shouldn't stop the pull
                print(f"  {name} {fmt}: {e}")
                continue
            key = name.lower().replace(" ", "")
            for it in items:
                if key in (it.get("brand_name") or "").lower().replace(" ", ""):
                    seen.setdefault(it["id"], {**it, "query": name, "fmt": fmt})
            time.sleep(0.8)
    rows = [{"brand": it["brand_name"], "format": it["fmt"], "days_running": it["days_running"],
             "status": it.get("status"), "title": it.get("title"), "body": (it.get("body") or "")[:700],
             "image_url": (it.get("images") or [{}])[0].get("url") or it.get("thumbnail_url"),
             "landing_url": it.get("link_url")} for it in seen.values()]
    rows.sort(key=lambda r: (r["brand"], -(r["days_running"] or 0)))
    write_csv("competitor_ads.csv", rows, list(rows[0]) if rows else ["brand"])


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


RTG_MARKERS = ("RTG", "RETARGET", "REMARKET", "WARM", "BOF")


def is_retargeting(*names):
    return any(m in (n or "").upper() for n in names for m in RTG_MARKERS)


def transcript(api, acc, video_id, pay):
    """Cached transcript (free); POST to transcribe on a cache miss only when pay=True (costs Atria credits)."""
    path = f"ad-accounts/{acc}/videos/{video_id}/transcript"
    try:
        d = api.get(path)
    except RuntimeError:
        d = None
    if (not d or d.get("status") != "success") and pay:
        r = api.s.post(f"{BASE}/{path}", timeout=300).json()
        d = r.get("data") if r.get("code") == 0 else None
    t = ((d or {}).get("transcript") or {}).get("text") if d and d.get("status") == "success" else None
    return " ".join(t.split()) if t else None


def body_key(text):
    """Script body without the hook (first ~60 words), used to merge hook variants of one script."""
    words = (text or "").lower().split()
    return " ".join(words[60:] if len(words) > 120 else words)


def longform(api, acc, args):
    """Top PROSPECTING ads (all formats) over the last --days, grouped into script families, with full
    copy + transcripts, as source material for long-form static ads.

    Retargeting is excluded (its ROAS reflects a warm audience, not the angle). A family = the same
    script/copy with different hooks or duplicate ad IDs. Families qualify on combined spend >= --lf-min-spend
    and ROAS >= the account's prospecting ROAS for the window x --lf-roas-factor, and are ranked by
    spend x (ROAS / prospecting ROAS), so they need both scale and efficiency.
    """
    import difflib
    end = dt.date.today() - dt.timedelta(days=1)
    start = end - dt.timedelta(days=args.days - 1)
    agg = aggregate(api, acc, start, end, "week")
    pro = {k: r for k, r in agg.items() if not is_retargeting(r["ad_name"])}
    base_roas = sum(r["revenue"] for r in pro.values()) / max(sum(r["spend"] for r in pro.values()), 1)
    cands = sorted(((k, r) for k, r in pro.items() if r["spend"] >= args.lf_ad_floor), key=lambda kv: -kv[1]["spend"])
    ads = []
    for ad_id, r in cands[:args.lf_max_ads]:
        d = api.get(f"ad-accounts/{acc}/ads/{ad_id}", {"period": "last_7d"})
        if is_retargeting(d.get("campaign_name"), d.get("adset_name")):
            continue
        c = d.get("creative") or {}
        vids = c.get("videos") or []
        pay = args.transcribe and r["spend"] >= args.lf_transcribe_floor
        tr = transcript(api, acc, vids[0]["video_id"], pay) if vids else None
        ads.append({**r, "platform_ad_id": ad_id, "campaign": d.get("campaign_name"), "adset": d.get("adset_name"),
                    "headline": c.get("title"), "primary_text": c.get("body") or "", "link_url": c.get("link_url"),
                    "video_id": vids[0]["video_id"] if vids else "", "transcript": tr or ""})
        time.sleep(0.5)
    fams = []
    for a in ads:  # videos merge only on transcript (shared primary text != same script); statics on copy
        if a["format"] == "VIDEO":
            key = "v:" + body_key(a["transcript"]) if a["transcript"] else ""
        else:
            key = "s:" + body_key((a["headline"] or "") + " " + a["primary_text"])
        if not key:
            fams.append({"key": f"untranscribed:{a['platform_ad_id']}", "ads": [a]})
            continue
        for f in fams:
            if key and difflib.SequenceMatcher(None, key[:1500], f["key"][:1500]).ratio() >= 0.6:
                f["ads"].append(a)
                break
        else:
            fams.append({"key": key, "ads": [a]})
    rows = []
    for i, f in enumerate(fams, 1):
        sp = sum(a["spend"] for a in f["ads"]); rev = sum(a["revenue"] for a in f["ads"])
        pu = sum(a["purchases"] for a in f["ads"]); roas = rev / sp if sp else 0
        lead = max(f["ads"], key=lambda a: a["spend"])
        rows.append({"family": i, "lead_ad": lead["ad_name"], "n_ads": len(f["ads"]), "format": lead["format"],
                     "spend": round(sp), "roas": round(roas, 2), "purchases": round(pu),
                     "cpa": round(sp / pu, 2) if pu else "", "score": round(sp * roas / base_roas),
                     "qualifies": sp >= args.lf_min_spend and roas >= base_roas * args.lf_roas_factor,
                     "has_transcript": bool(lead["transcript"]), "ads": f["ads"]})
    rows.sort(key=lambda r: (not r["qualifies"], -r["score"]))
    write_csv("longform_winners.csv", rows, ["family", "qualifies", "score", "spend", "roas", "cpa", "purchases",
              "n_ads", "format", "has_transcript", "lead_ad"])
    md = [f"# Prospecting winners for long-form copy ({start} to {end})\n",
          f"Prospecting ROAS baseline: {base_roas:.2f}. Qualify: family spend >= ${args.lf_min_spend:.0f} and ROAS >= "
          f"{base_roas * args.lf_roas_factor:.2f}. Ranked by spend x ROAS/baseline. Retargeting excluded.\n"]
    for r in [r for r in rows if r["qualifies"]]:
        lead = max(r["ads"], key=lambda a: a["spend"])
        md.append(f"\n## Family {r['family']}: {r['lead_ad']}\n\nSpend ${r['spend']:,} · ROAS {r['roas']} · CPA "
                  f"${r['cpa']} · {r['purchases']} purchases · score {r['score']:,} · {r['n_ads']} ad(s)\n")
        for a in sorted(r["ads"], key=lambda a: -a["spend"]):
            md.append(f"- {a['ad_name']} ({a['platform_ad_id']}): ${a['spend']:,.0f}, ROAS "
                      f"{a['revenue'] / a['spend']:.2f}, adset: {a['adset']}")
        md.append(f"\n**Headline:** {lead['headline']}  \n**Landing page:** {lead['link_url']}\n")
        md.append(f"**Primary text:**\n\n> " + lead["primary_text"].replace("\n", "\n> ") + "\n")
        hooks = {a["transcript"][:300] for a in r["ads"] if a["transcript"]}
        if lead["transcript"]:
            md.append(f"**Transcript (lead ad):**\n\n{lead['transcript']}\n")
        if len(hooks) > 1:
            md.append("**Hook variants (first 300 chars):**\n\n" + "\n".join(f"- {h}…" for h in hooks) + "\n")
        elif lead["format"] == "VIDEO" and not lead["transcript"]:
            md.append(f"_No cached transcript (video {lead['video_id']}). Re-run with --transcribe to pay for one._\n")
    path = DATA_DIR / "longform_winners.md"
    path.write_text("\n".join(md))
    print(f"Wrote {path}. {sum(r['qualifies'] for r in rows)} qualifying families of {len(rows)}.")


def main():
    load_dotenv()
    p = argparse.ArgumentParser()
    p.add_argument("what", choices=["winners", "losers", "inspo", "seasonal", "rising", "current", "competitors", "longform"])
    p.add_argument("--lf-min-spend", type=float, default=3000, help="longform: minimum combined family spend")
    p.add_argument("--lf-roas-factor", type=float, default=0.95, help="longform: family ROAS must be >= prospecting ROAS x this")
    p.add_argument("--lf-ad-floor", type=float, default=300, help="longform: ignore single ads under this spend")
    p.add_argument("--lf-max-ads", type=int, default=60, help="longform: max ads to fetch copy/transcripts for")
    p.add_argument("--lf-transcribe-floor", type=float, default=2000, help="longform: only pay to transcribe ads with at least this spend")
    p.add_argument("--transcribe", action="store_true", help="longform: pay Atria credits to transcribe uncached videos")
    p.add_argument("--days", type=int, default=30, help="rising: look-back window in days")
    p.add_argument("--min-spend-rising", type=float, default=300, help="rising: minimum spend in the window")
    p.add_argument("--min-roas", type=float, default=1.8, help="rising: minimum ROAS in the window")
    p.add_argument("--week", help="seasonal: target ISO week, e.g. 2026-W45 (default: next week)")
    p.add_argument("--pad-days", type=int, default=7, help="seasonal: widen last year's window by this many days each side")
    p.add_argument("--top", type=int, default=15, help="seasonal: how many top-spending ads to keep")
    p.add_argument("--min-spend", type=float, default=5000)
    p.add_argument("--max-spend", type=float, default=200)
    p.add_argument("--brand", default=os.getenv("ADS_BRAND", "comfortwear"))
    p.add_argument("--account", help="ad account name in Atria (default: brand.json → atria_account)")
    args = p.parse_args()
    global DATA_DIR
    bdir = Path(__file__).resolve().parent / "brands" / args.brand
    DATA_DIR = bdir / "research" / "data"
    brand = json.loads((bdir / "brand.json").read_text())
    args.account = args.account or brand.get("atria_account", ACCOUNT_NAME)
    args.queries = brand.get("inspo_queries", INSPO_QUERIES)
    args.competitors = brand.get("competitor_brands", [])
    # Without ATRIA_API_KEY the request relies on a network secret the proxy attaches.
    api = Atria(os.getenv("ATRIA_API_KEY"))
    acc = api.account_id(args.account)
    if not args.week:
        y, w, _ = (dt.date.today() + dt.timedelta(days=7)).isocalendar()
        args.week = f"{y}-W{w:02d}"
    if args.what == "longform" and args.days == 30:
        args.days = 90  # longform default window
    {"winners": winners, "losers": losers, "inspo": inspo, "seasonal": seasonal, "rising": rising, "current": rising,
     "competitors": competitors, "longform": longform}[args.what](api, acc, args)


if __name__ == "__main__":
    main()
