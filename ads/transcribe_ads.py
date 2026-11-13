"""Transcribe the WHOLE script of our video winners (user rule 2026-11-13) and append to research/data/video_transcripts.md.

    python ads/transcribe_ads.py top7_spenders.csv current_winners.csv new7_winners.csv --brand comfortwear

Gets each video's CDN url from the Atria ad detail (creative.videos[0].url), extracts mono audio with ffmpeg and
transcribes it with OpenAI (gpt-4o-transcribe, fallback whisper-1). Skips ads already in video_transcripts.md.
"""
import argparse, csv, os, subprocess, sys, tempfile, time
from pathlib import Path
import requests
from dotenv import load_dotenv

BASE = "https://api.tryatria.com/open/v1"
ROOT = Path(__file__).resolve().parent


def main():
    load_dotenv()
    p = argparse.ArgumentParser()
    p.add_argument("csvs", nargs="+")
    p.add_argument("--brand", default="comfortwear")
    a = p.parse_args()
    bdir = ROOT / "brands" / a.brand
    import json
    acc_name = json.loads((bdir / "brand.json").read_text()).get("atria_account")
    s = requests.Session(); s.headers["X-API-Key"] = os.environ["ATRIA_API_KEY"]
    acc = next(x["id"] for x in s.get(f"{BASE}/ad-accounts", timeout=60).json()["data"]["items"] if x["name"] == acc_name)
    out = bdir / "research" / "data" / "video_transcripts.md"
    done = out.read_text() if out.exists() else ""
    seen = set()
    for c in a.csvs:
        for r in csv.DictReader(open(bdir / "research" / "data" / c)):
            if r.get("format") != "VIDEO" or r["platform_ad_id"] in seen:
                continue
            seen.add(r["platform_ad_id"])
            if f"[{r['platform_ad_id']}]" in done or r["ad_name"] in done:
                print("have", r["ad_name"][:50]); continue
            for attempt in range(8):
                d = s.get(f"{BASE}/ad-accounts/{acc}/ads/{r['platform_ad_id']}", params={"period": "last_7d"}, timeout=90)
                if d.status_code == 429: time.sleep(5 * (attempt + 1)); continue
                break
            vids = (d.json()["data"].get("creative") or {}).get("videos") or []
            if not vids or not vids[0].get("url"): print("no video url", r["ad_name"]); continue
            with tempfile.TemporaryDirectory() as t:
                mp4, mp3 = f"{t}/v.mp4", f"{t}/a.mp3"
                open(mp4, "wb").write(requests.get(vids[0]["url"], timeout=300).content)
                subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", mp4, "-vn", "-ac", "1", "-ar", "16000", "-b:a", "48k", mp3], check=True)
                text = None
                for model in ("gpt-4o-transcribe", "whisper-1"):
                    tr = requests.post("https://api.openai.com/v1/audio/transcriptions", headers={"Authorization": "Bearer " + os.environ["OPENAI_API_KEY"]},
                                       files={"file": open(mp3, "rb")}, data={"model": model}, timeout=600)
                    if tr.ok: text = tr.json()["text"]; break
                if not text: print("transcription failed", r["ad_name"], tr.text[:150]); continue
            with open(out, "a") as f:
                f.write(f"\n## {r['ad_name']} [{r['platform_ad_id']}]\nSpend: ${float(r['spend']):,.0f} · ROAS {r['roas']} · transcribed {time.strftime('%Y-%m-%d')} (full script)\n\n{text}\n")
            print("transcribed", r["ad_name"][:50], len(text), "chars")


if __name__ == "__main__":
    main()
