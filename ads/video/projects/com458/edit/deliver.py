"""Finish a rendered COM458 cut: loudnorm to -15 LUFS, 540p review copy, SRT, per-shot asset/licence sheet.
    python edit/deliver.py H1 [H2 H3]       (expects out/COM458_<h>.mp4 from engine4.py)"""
import csv, subprocess, sys
from pathlib import Path
import engine4 as E, edl4

OUT = E.P / "out"
SRC = {}
for row in csv.reader(open(E.P / "tiktok" / "sources.tsv"), delimiter="\t"):
    if len(row) >= 6: SRC[f"{row[1]}_{row[2]}"] = (row[1], row[5])

def ts(t):
    h, r = divmod(t, 3600); m, s = divmod(r, 60)
    return f"{int(h):02d}:{int(m):02d}:{s:06.3f}".replace(".", ",")

def origin(src):
    if src.startswith("tiktok/"):
        stem = Path(src).stem; c, u = SRC.get(stem, ("?", "?"))
        return "TikTok UGC", "@" + c, u, "NEEDS CREATOR LICENCE before launch"
    if src.startswith("gen/"): return "AI generated (Kie Kling avatar / Atria Kling 4.0)", "", "", "owned"
    if src == edl4.R376: return "ComfortWear COM376 (own ad)", "", "", "owned"
    return "ComfortWear Drive library", "", "", "owned"

def run(h):
    raw = OUT / f"COM458_{h}.mp4"; fin = OUT / f"COM458_{h}_final.mp4"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(raw), "-c:v", "copy", "-af", "loudnorm=I=-15:TP=-1.5:LRA=11", "-ar", "48000",
                    "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", str(fin)], check=True)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(fin), "-vf", "scale=540:960", "-c:v", "libx264", "-crf", "24", "-preset", "veryfast",
                    "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart", str(OUT / f"COM458_{h}_preview540.mp4")], check=True)
    audio, words, off, total = E.timeline_audio(h)
    secs = [h] + [f"P{i}" for i in range(1, 8)]
    with open(OUT / f"COM458_{h}.srt", "w") as f:
        for i, c in enumerate(E.caption_chunks(words, secs), 1): f.write(f"{i}\n{ts(c['s'])} --> {ts(c['e'])}\n{c['text']}\n\n")
    shots = E.build([dict(x) for x in edl4.HOOKS[h] + edl4.BODY], words, total)
    with open(OUT / f"COM458_{h}_asset_sources.csv", "w", newline="") as f:
        w = csv.writer(f); w.writerow(["#", "start_s", "dur_s", "section", "vo_cue", "source_type", "file", "in_s", "creator", "url", "rights"])
        for s in shots:
            typ, cr, url, rights = origin(s["src"])
            w.writerow([s["i"] + 1, f"{s['t0']:.2f}", f"{s['n'] / E.FPS:.2f}", s["sec"], s.get("w"), typ, s["src"], s.get("ss", 0), cr, url, rights])
    print(h, "->", fin.name, f"{total:.1f}s", len(shots), "shots")

if __name__ == "__main__":
    for h in sys.argv[1:] or ["H1", "H2", "H3"]: run(h)
