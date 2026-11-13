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
    # faces outside the 4:5 area (would be cut in feed placements), content scenes only
    import sys as _s
    _s.path.insert(0, str(Path(__file__).resolve().parent))
    from build import face_boxes, SAFE_TOP, SAFE_BOT
    warn = []
    for i, sc in enumerate(tl["scenes"]):
        if sc["src"] == "_end_card":
            continue
        for f in (0.25, 0.5, 0.75):
            t = sc["start"] + (sc["end"] - sc["start"]) * f
            for y0, y1, x0, x1 in face_boxes(v, t):
                if y0 < SAFE_TOP - 0.005 or y1 > SAFE_BOT + 0.005:
                    warn.append(f"scene {i} ({sc['src']}) t={t:.1f}s face y {y0:.2f}-{y1:.2f}")
    print("faces outside 4:5: " + ("none" if not warn else "\n  " + "\n  ".join(sorted(set(warn)))))
    # strip: mid-scene frames of the 9:16 with the 4:5 area outlined in green
    tmp = v.with_name("_qa")
    tmp.mkdir(exist_ok=True)
    times = [(s["start"] + s["end"]) / 2 for s in tl["scenes"]]
    files = []
    for i, t in enumerate(times):
        f = tmp / f"v{i:02d}.png"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{t:.2f}", "-i", str(v), "-frames:v", "1", "-vf",
                        "drawbox=x=0:y=285:w=1080:h=1350:color=lime@0.85:t=6,scale=240:-2", str(f)])
        if f.exists():
            files.append(f)
    out = Path(a.out) if a.out else v.with_name(v.stem + "_qa.png")
    inputs = sum((["-i", str(f)] for f in files), [])
    subprocess.run(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex",
                    "".join(f"[{i}:v]" for i in range(len(files))) + f"hstack=inputs={len(files)}", str(out)])
    for f in files:
        f.unlink(missing_ok=True)
    tmp.rmdir()
    print(f"strip ({len(files)} scenes, 4:5 area outlined): {out}")


if __name__ == "__main__":
    main()
