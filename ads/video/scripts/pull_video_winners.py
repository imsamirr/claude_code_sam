"""Lifetime spend of every VIDEO ad across the WearOrtho Atria ad accounts (monthly top-50 windows since 2023).

    python ads/video/scripts/pull_video_winners.py [--min-spend 20000]
Writes ads/video/research/data/wearortho_video_winners.json (detail incl. video URLs for ads >= min spend).
"""
import argparse, datetime as dt, json, os, sys, time
from pathlib import Path
import requests

BASE = "https://api.tryatria.com/open/v1"
OUT = Path(__file__).resolve().parents[1] / "research" / "data"
s = requests.Session(); s.headers["X-API-Key"] = os.environ["ATRIA_API_KEY"]

def get(path, params=None):
    for attempt in range(7):
        r = s.get(f"{BASE}/{path}", params=params, timeout=180)
        if r.status_code in (429, 500, 502, 503, 504):
            time.sleep(3 * 2 ** attempt); continue
        r.raise_for_status(); b = r.json()
        if b.get("code") != 0: raise RuntimeError(f"{path}: {b}")
        return b["data"]
    raise RuntimeError("retries")

def months(start, end):
    d = start
    while d <= end:
        nxt = (d.replace(day=28) + dt.timedelta(days=4)).replace(day=1)
        yield d, min(nxt - dt.timedelta(days=1), end); d = nxt

ap = argparse.ArgumentParser(); ap.add_argument("--min-spend", type=float, default=20000)
ap.add_argument("--since", default="2023-01-01"); a = ap.parse_args()
accts = [x for x in get("ad-accounts")["items"] if x["name"].startswith("WearOrtho")]
yday = dt.date.today() - dt.timedelta(days=1)
agg = {}
for acc in accts:
    for st, sp in months(dt.date.fromisoformat(a.since), yday):
        try: items = get(f"ad-accounts/{acc['id']}/ads", {"period": "custom", "date_start": str(st), "date_stop": str(sp), "sort_by": "spend", "limit": 50})["items"]
        except Exception as e: print("ERR", acc["name"], st, e, file=sys.stderr); continue
        nvid = 0
        for it in items:
            m = it["metrics"]; sp_ = m.get("spend") or 0
            r = agg.setdefault(it["platform_ad_id"], {"account": acc["name"], "account_id": acc["id"], "ad_name": it["ad_name"],
                 "format": it["asset_format"], "status": it["status"], "thumbnail_url": it["thumbnail_url"],
                 "spend": 0.0, "revenue": 0.0, "purchases": 0.0, "impressions": 0, "clicks": 0, "first": str(st), "last": str(st)})
            r["spend"] += sp_; r["revenue"] += (m.get("roas") or 0) * sp_; r["purchases"] += m.get("purchases") or 0
            r["impressions"] += m.get("impressions") or 0; r["clicks"] += m.get("clicks_all") or 0; r["last"] = str(st)
            nvid += it["asset_format"] == "VIDEO"
        print(acc["name"], st, len(items), "ads", nvid, "video", flush=True); time.sleep(0.6)
json.dump(agg, open(OUT / "wearortho_all_ads_lifetime.json", "w"), indent=1)
win = []
for pid, r in agg.items():
    if r["format"] != "VIDEO" or r["spend"] < a.min_spend: continue
    d = get(f"ad-accounts/{r['account_id']}/ads/{pid}", {"period": "last_7d"})
    c = d.get("creative") or {}
    win.append({**r, "platform_ad_id": pid, "roas": round(r["revenue"] / r["spend"], 2) if r["spend"] else None,
                "ctr_pct": round(100 * r["clicks"] / max(r["impressions"], 1), 2), "cpa": round(r["spend"] / r["purchases"], 2) if r["purchases"] else None,
                "headline": c.get("title"), "primary_text": c.get("body"), "videos": c.get("videos"), "creative": c})
    time.sleep(0.6)
win.sort(key=lambda r: -r["spend"])
json.dump(win, open(OUT / "wearortho_video_winners.json", "w"), indent=1)
print("WINNERS", len(win)); [print(f"{w['spend']:>10.0f} {w['roas']} {w['account']} {w['ad_name']}") for w in win]
