"""Top video ads per competitor brand from the Atria library: running >= 30 days, ranked by impressions, variants collapsed.
    python ads/video/scripts/pull_competitor_videos.py [--per 10]
Writes research/data/competitor_videos.json and downloads videos to research/media/competitors/<brand>/"""
import argparse, json, os, re, time
from pathlib import Path
import requests
BRANDS = {"Hike Footwear": "m275270825974823", "Viasox": "m805189916549928", "Hollow Socks": "m111034490269087",
          "Everstride": "m373478645850236", "KittySpout": "m102825741868911", "BioRoot Labs": "m711948225325316",
          "OneCompress": "m865468883845266", "Orthora Footwear": "m825781737288711", "Stepprs": "m216540858213050",
          "The Xstance": "m107225168201875"}
R = Path(__file__).resolve().parents[1] / "research"
s = requests.Session(); s.headers["X-API-Key"] = os.environ["ATRIA_API_KEY"]
def get(path, params):
    for a in range(7):
        r = s.get("https://api.tryatria.com/open/v1/" + path, params=params, timeout=180)
        if r.status_code in (429, 500, 502, 503, 504) or (r.ok and r.json().get("code") == 42901): time.sleep(3 * 2 ** a); continue
        return r.json()
ap = argparse.ArgumentParser(); ap.add_argument("--per", type=int, default=10); a = ap.parse_args()
out = []
for name, bid in BRANDS.items():
    j = get("ad-library/search", {"brand_id": bid, "media_format": "video", "min_days_running": 30, "order": "most_impressions",
                                  "collapse_variants": "true", "page_size": 20})
    items = (j.get("data") or {}).get("items", [])
    slug = re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_"); d = R / "media" / "competitors" / slug; d.mkdir(parents=True, exist_ok=True)
    kept = 0
    for it in items:
        v = (it.get("videos") or [{}])[0]
        if not v.get("url") or kept >= a.per: continue
        kept += 1; key = f"{slug}_{kept:02d}"
        f = d / f"{key}.mp4"
        if not f.exists():
            try: f.write_bytes(s.get(v["url"], timeout=300).content)
            except Exception as e: print("dl fail", key, e); continue
        rk = (it.get("impression_rank") or {}).get("latest_rank") or {}
        out.append({"key": key, "brand": name, "ad_id": it["id"], "status": it["status"], "days_running": it["days_running"],
                    "start_date": it["start_date"], "duration": v.get("duration"), "w": v.get("width"), "h": v.get("height"),
                    "impression_rank": rk.get("rank"), "rank_pool": rk.get("total"), "percentile": rk.get("percentile"),
                    "trend": it.get("impression_trend"), "dupes": it.get("creative_duplicates"), "themes": it.get("themes"),
                    "title": it.get("title"), "body": it.get("body"), "link_url": it.get("link_url"), "file": str(f)})
    print(name, len(items), "found,", kept, "kept", flush=True); time.sleep(1.5)
json.dump(out, open(R / "data" / "competitor_videos.json", "w"), indent=1)
