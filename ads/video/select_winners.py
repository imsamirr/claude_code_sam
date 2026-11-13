"""Pick the winners a weekly video batch iterates on, from the brand's Atria ad accounts.

Rules (brand.json -> video.weekly.winners, defaults = Comfort Wear user rules, Nov 2026):
  top:  spend >= $1,000 over the last 7 days and ROAS >= 1.6
  new:  launched in the last 7 days (no spend in the 60 days before), spend >= $200, ROAS >= 1.6
Statics count too (their angle becomes a video concept).

    python ads/video/select_winners.py --brand comfortwear [--out <dir>]
    -> <out>/winners.json + winners.md (copy, headline, landing page, video URL, transcript)
Needs ATRIA_API_KEY. Every connected account named in brand.json -> video.weekly.atria_accounts.
"""

import argparse
import datetime as dt
import json
import os
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from atria_pull import Atria  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]


def page(api, acc, start, stop, pages=6):
    """All ads with spend in the window, best effort (50 per page, by spend)."""
    out = []
    for k in range(pages):
        try:
            items = api.get(f"ad-accounts/{acc}/ads", {"period": "custom", "date_start": str(start),
                                                      "date_stop": str(stop), "sort_by": "spend",
                                                      "limit": 50, "offset": 50 * k})["items"]
        except RuntimeError:
            break
        out += items
        if len(items) < 50 or (items and (items[-1]["metrics"].get("spend") or 0) < 50):
            break
        time.sleep(0.6)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--brand", default="comfortwear")
    ap.add_argument("--out")
    a = ap.parse_args()
    bdir = ROOT / "ads" / "brands" / a.brand
    brand = json.loads((bdir / "brand.json").read_text())
    rules = {"top_min_spend": 1000, "top_min_roas": 1.6, "new_min_spend": 200, "new_min_roas": 1.6,
             "days": 7, **brand.get("video", {}).get("weekly", {}).get("winners", {})}
    accounts = brand.get("video", {}).get("weekly", {}).get("atria_accounts") or [brand.get("atria_account")]
    api = Atria(os.environ.get("ATRIA_API_KEY"))
    end = dt.date.today() - dt.timedelta(days=1)
    start = end - dt.timedelta(days=rules["days"] - 1)
    winners = []
    for name in accounts:
        try:
            acc = api.account_id(name)
        except SystemExit:
            print(f"account {name!r} not found, skipped")
            continue
        recent = page(api, acc, start, end)
        before = {it["platform_ad_id"] for it in page(api, acc, start - dt.timedelta(days=60),
                                                      start - dt.timedelta(days=1), pages=10)}
        for it in recent:
            m = it["metrics"]
            spend, roas = m.get("spend") or 0, m.get("roas") or 0
            is_new = it["platform_ad_id"] not in before
            tier = ("top" if spend >= rules["top_min_spend"] and roas >= rules["top_min_roas"] else
                    "new" if is_new and spend >= rules["new_min_spend"] and roas >= rules["new_min_roas"] else None)
            if not tier:
                continue
            d = api.get(f"ad-accounts/{acc}/ads/{it['platform_ad_id']}", {"period": "last_7d"})
            c = d.get("creative") or {}
            vids = c.get("videos") or []
            tr = ""
            if vids and vids[0].get("video_id"):
                try:
                    t = api.get(f"ad-accounts/{acc}/videos/{vids[0]['video_id']}/transcript")
                    tr = (t.get("transcript") or {}).get("text") or ""
                except Exception:  # noqa: BLE001 - transcript is optional
                    tr = ""
            winners.append({"tier": tier, "account": name, "platform_ad_id": it["platform_ad_id"],
                            "ad_name": it["ad_name"], "format": it["asset_format"], "status": it["status"],
                            "spend_7d": round(spend, 2), "roas_7d": round(roas, 2),
                            "purchases_7d": m.get("purchases"), "headline": c.get("title"),
                            "primary_text": c.get("body"), "link": c.get("link_url"),
                            "video_url": vids[0]["url"] if vids else None,
                            "image_url": (c.get("images") or [{}])[0].get("url"), "transcript": tr.strip()})
            time.sleep(0.6)
    winners.sort(key=lambda w: (w["tier"] != "top", -w["spend_7d"] * w["roas_7d"]))
    out = Path(a.out) if a.out else bdir / "video" / "winners"
    out.mkdir(parents=True, exist_ok=True)
    (out / "winners.json").write_text(json.dumps({"window": [str(start), str(end)], "rules": rules,
                                                  "winners": winners}, indent=2, ensure_ascii=False))
    lines = [f"# Winners {start} to {end}", "",
             f"top: >= ${rules['top_min_spend']:.0f} & ROAS >= {rules['top_min_roas']} | "
             f"new (launched in window): >= ${rules['new_min_spend']:.0f} & ROAS >= {rules['new_min_roas']}", ""]
    for w in winners:
        lines += [f"## [{w['tier']}] {w['ad_name']}", f"{w['account']} · {w['format']} · ${w['spend_7d']:,.0f} · "
                  f"ROAS {w['roas_7d']} · {w['purchases_7d']} purchases · {w['link']}",
                  f"**Headline:** {w['headline']}", "", (w["primary_text"] or "")[:600], ""]
        if w["transcript"]:
            lines += [f"> {w['transcript'][:900]}", ""]
    (out / "winners.md").write_text("\n".join(lines))
    print(f"{len(winners)} winners ({sum(w['tier'] == 'top' for w in winners)} top, "
          f"{sum(w['tier'] == 'new' for w in winners)} new) -> {out}/winners.json")
    for w in winners:
        print(f"  [{w['tier']}] ${w['spend_7d']:>8,.0f}  ROAS {w['roas_7d']:<4}  {w['ad_name'][:90]}")


if __name__ == "__main__":
    main()
