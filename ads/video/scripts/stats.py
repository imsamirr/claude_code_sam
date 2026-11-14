"""Aggregate structural stats (duration, shots, shot length, first cut, VO wpm) for WearOrtho winners vs each competitor brand -> research/data/structure_stats.md"""
import json, re, statistics as st
from pathlib import Path
R = Path(__file__).resolve().parents[1] / "research"
def load(root):
    out = []
    for c in sorted((R / "media" / root).glob("*/cuts.json")):
        j = json.load(open(c)); t = c.parent / "transcript.json"
        tj = json.load(open(t)) if t.exists() else {}
        hook = [s["len"] for s in j["shots"] if s["start"] < 3]
        body = [s["len"] for s in j["shots"] if 3 <= s["start"] < j["duration"] - 10]
        out.append({"key": c.parent.name.split("_")[0] if root.startswith("wear") else c.parent.name, "dur": j["duration"], "shots": j["n_shots"],
                    "avg": j["avg_shot"], "med": j["median_shot"], "first": j["first_cut"], "c3": j["cuts_first_3s"], "c10": j["cuts_first_10s"],
                    "body_med": st.median(body) if body else None, "wpm": tj.get("wpm"), "lang": tj.get("language")})
    return out
def summ(rows):
    f = lambda k: [r[k] for r in rows if r[k] is not None]
    m = lambda k: round(st.median(f(k)), 2) if f(k) else "-"
    return f"| {len(rows)} | {m('dur')} | {m('shots')} | {m('med')} | {m('body_med')} | {m('first')} | {m('c3')} | {m('c10')} | {m('wpm')} |"
wo = load("wearortho_analysis"); comp = load("competitor_analysis")
groups = {"WearOrtho >$20k winners": wo}
for r in comp: groups.setdefault(re.sub(r"_\d+$", "", r["key"]), []).append(r)
lines = ["# Structure stats (medians)", "", "| group | n | duration s | shots | median shot s | body median shot s | first cut s | cuts in 0–3 s | cuts in 0–10 s | VO wpm |", "|---|---|---|---|---|---|---|---|---|---|"]
lines += [f"| {g} " + summ(rs) for g, rs in groups.items()]
lines += ["", "## WearOrtho per video", "", "| key | dur | shots | avg | med | first cut | cuts 0–3 | cuts 0–10 | wpm | lang |", "|---|---|---|---|---|---|---|---|---|---|"]
lines += [f"| {r['key']} | {r['dur']} | {r['shots']} | {r['avg']} | {r['med']} | {r['first']} | {r['c3']} | {r['c10']} | {r['wpm']} | {r['lang']} |" for r in wo]
(R / "data" / "structure_stats.md").write_text("\n".join(lines)); print("\n".join(lines[:16]))
