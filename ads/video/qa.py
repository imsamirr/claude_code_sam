"""Automated QA for a rendered ad: frame count, timestamp gaps, freezes, loudness/peak, and a
strip of one frame from the middle of every scene (9:16 and 4:5) to Read.

Usage:
    python ads/video/qa.py ads/brands/<brand>/video/<week>/<id>/<id>.mp4 [--out strip.png]
Needs <id>_timeline.json (written by build.py next to the video).
"""

import argparse
import json
import re
import subprocess
from pathlib import Path


def sh(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    return r.stdout + r.stderr


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video")
    ap.add_argument("--out")
    a = ap.parse_args()
    v = Path(a.video)
    tl = json.loads(v.with_name(v.stem + "_timeline.json").read_text())
    total = tl["total"]
    frames = int(sh(["ffprobe", "-v", "error", "-count_frames", "-select_streams", "v:0", "-show_entries",
                     "stream=nb_read_frames", "-of", "csv=p=0", str(v)]).strip())
    pts = [float(x) for x in sh(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                                 "packet=pts_time", "-of", "csv=p=0", str(v)]).split()]
    pts.sort()
    gaps = [(p, q) for p, q in zip(pts, pts[1:]) if not 0.032 <= q - p <= 0.0345]
    fr = sh(["ffmpeg", "-v", "info", "-i", str(v), "-vf", "freezedetect=n=0.002:d=0.3", "-map", "0:v", "-f", "null", "-"])
    freezes = [float(x) for x in re.findall(r"freeze_start: ([\d.]+)", fr)]
    card = tl["scenes"][-1]["start"] if tl["scenes"][-1]["src"] == "_end_card" else total
    freezes_content = [f for f in freezes if f < card - 0.2]
    loud = sh(["ffmpeg", "-v", "info", "-i", str(v), "-af", "ebur128=peak=true", "-f", "null", "-"])
    lufs = re.findall(r"I:\s+(-?[\d.]+) LUFS", loud)[-1]
    peak = re.findall(r"Peak:\s+(-?[\d.]+) dBFS", loud)[-1]
    ok = abs(frames - round(total * 30)) <= 1 and not gaps and not freezes_content and float(peak) <= -1.0
    print(f"{v.name}: {total:.2f}s  frames {frames} (expect {round(total * 30)})  gaps {len(gaps)}  "
          f"freezes in content {len(freezes_content)}  loudness {lufs} LUFS  peak {peak} dBFS  -> {'PASS' if ok else 'CHECK'}")
    # strip: mid-scene frames from the 9:16, then the same times from the 4:5
    tmp = v.with_name("_qa")
    tmp.mkdir(exist_ok=True)
    times = [(s["start"] + s["end"]) / 2 for s in tl["scenes"]]
    files = []
    for kind, src in (("v", v), ("f", v.with_name(v.stem + "_4x5.mp4"))):
        if not src.exists():
            continue
        for i, t in enumerate(times):
            f = tmp / f"{kind}{i:02d}.png"
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{t:.2f}", "-i", str(src), "-frames:v", "1",
                            "-vf", "scale=240:-2,pad=240:428:0:(oh-ih)/2", str(f)])
            files.append(f)
    n = len(times)
    out = Path(a.out) if a.out else v.with_name(v.stem + "_qa.png")
    inputs = sum((["-i", str(f)] for f in files), [])
    rows = len(files) // n
    fc = "".join(f"[{i}:v]" for i in range(len(files)))
    fc += f"xstack=inputs={len(files)}:layout=" + "|".join(
        f"{(i % n) * 240}_{(i // n) * 428}" for i in range(len(files)))
    subprocess.run(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", fc, str(out)])
    for f in files:
        f.unlink()
    tmp.rmdir()
    print(f"strip ({rows} rows x {n} scenes): {out}")


if __name__ == "__main__":
    main()
