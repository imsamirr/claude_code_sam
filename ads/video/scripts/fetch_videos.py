"""Download each unique winning video (dedupe by video_id); re-query detail in the ad's active window when URL missing."""
import json, os, sys, time, datetime as dt
from pathlib import Path
import requests
D = Path(__file__).resolve().parents[1] / "research" / "data"
MEDIA = Path(__file__).resolve().parents[1] / "research" / "media" / "wearortho"
MEDIA.mkdir(parents=True, exist_ok=True)
s = requests.Session(); s.headers["X-API-Key"] = os.environ["ATRIA_API_KEY"]
def get(path, params):
    for a in range(7):
        r = s.get("https://api.tryatria.com/open/v1/" + path, params=params, timeout=180)
        if r.status_code in (429, 500, 502, 503, 504): time.sleep(3 * 2 ** a); continue
        b = r.json()
        if b.get("code") == 42901: time.sleep(3 * 2 ** a); continue
        return b
w = json.load(open(D / "wearortho_video_winners.json"))
groups = {}
for r in w:
    for i, v in enumerate(r.get("videos") or [{}]):
        vid = v.get("video_id") or r["platform_ad_id"]
        g = groups.setdefault(vid, {"video_id": vid, "rows": [], "url": None, "duration": v.get("duration")})
        g["rows"].append(r)
        if v.get("url"): g["url"] = v["url"]
        break
for vid, g in groups.items():
    if g["url"]: continue
    for r in g["rows"]:
        st = dt.date.fromisoformat(r["last"]); sp = min(st + dt.timedelta(days=27), dt.date.today() - dt.timedelta(days=1))
        b = get(f"ad-accounts/{r['account_id']}/ads/{r['platform_ad_id']}", {"period": "custom", "date_start": str(st), "date_stop": str(sp)})
        vs = ((b.get("data") or {}).get("creative") or {}).get("videos") or []
        if vs and vs[0].get("url"): g["url"] = vs[0]["url"]; g["duration"] = vs[0].get("duration"); break
        print("no url", vid, r["ad_name"][:50], b.get("code"), file=sys.stderr); time.sleep(1)
idx = []
for n, (vid, g) in enumerate(sorted(groups.items(), key=lambda x: -sum(r["spend"] for r in x[1]["rows"])), 1):
    spend = sum(r["spend"] for r in g["rows"]); rev = sum(r["revenue"] for r in g["rows"])
    f = MEDIA / f"W{n:02d}_{vid}.mp4"
    if g["url"] and not f.exists():
        with s.get(g["url"], stream=True, timeout=300) as resp:
            resp.raise_for_status(); f.write_bytes(resp.content)
    r0 = g["rows"][0]
    idx.append({"rank": n, "key": f"W{n:02d}", "video_id": vid, "file": str(f) if f.exists() else None, "spend_cad": round(spend),
                "roas": round(rev / spend, 2) if spend else None, "n_ads": len(g["rows"]), "ad_names": [r["ad_name"] for r in g["rows"]],
                "account_id": r0["account_id"], "duration": g["duration"], "headline": r0.get("headline"), "primary_text": r0.get("primary_text"),
                "link_url": (r0.get("creative") or {}).get("link_url"), "first_month": min(r["first"] for r in g["rows"]), "last_month": max(r["last"] for r in g["rows"]),
                "impressions": sum(r["impressions"] for r in g["rows"]), "ctr_pct": round(100 * sum(r["clicks"] for r in g["rows"]) / max(1, sum(r["impressions"] for r in g["rows"])), 2)})
    print(n, vid, idx[-1]["file"] is not None, flush=True)
json.dump(idx, open(D / "wearortho_video_index.json", "w"), indent=1)
