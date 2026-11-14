"""Per-video structural analysis: cuts (scene detection), shot lengths, hook frames, per-shot contact sheet, audio extract.

    python ads/video/scripts/analyze_video.py <video.mp4> [...] --out <dir>
Writes <out>/<stem>/: cuts.json, hook_sheet.jpg (0-3.5s every 0.25s), shots_sheet_N.jpg (one frame per shot, labelled), audio.mp3
"""
import argparse, json, re, subprocess, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
def run(cmd): return subprocess.run(cmd, capture_output=True, text=True)
def probe(f):
    j = json.loads(run(["ffprobe", "-v", "quiet", "-print_format", "json", "-show_streams", "-show_format", str(f)]).stdout)
    v = next(s for s in j["streams"] if s["codec_type"] == "video")
    return float(j["format"]["duration"]), int(v["width"]), int(v["height"]), any(s["codec_type"] == "audio" for s in j["streams"])
def cuts(f, thr):
    err = run(["ffmpeg", "-hide_banner", "-i", str(f), "-vf", f"scale=270:-2,select='gt(scene,{thr})',showinfo", "-an", "-f", "null", "-"]).stderr
    return [round(float(m), 2) for m in re.findall(r"pts_time:([\d.]+)", err)]
def frame(f, t, w=270):
    import io
    for tt in (t, max(0, t - 0.3), max(0, t - 1.0)):
        b = subprocess.run(["ffmpeg", "-v", "quiet", "-ss", f"{tt:.3f}", "-i", str(f), "-frames:v", "1", "-vf", f"scale={w}:-2", "-f", "image2pipe", "-vcodec", "png", "-"], capture_output=True).stdout
        if b: return Image.open(io.BytesIO(b)).convert("RGB")
    return Image.new("RGB", (w, w * 16 // 9), "gray")
def sheet(imgs, labels, cols, path):
    w, h = imgs[0].size; lab = 26
    S = Image.new("RGB", (cols * w, ((len(imgs) + cols - 1) // cols) * (h + lab)), "white"); d = ImageDraw.Draw(S)
    fnt = ImageFont.truetype(FONT, 18)
    for i, (im, l) in enumerate(zip(imgs, labels)):
        x, y = (i % cols) * w, (i // cols) * (h + lab)
        S.paste(im, (x, y + lab)); d.text((x + 4, y + 3), l, fill="black", font=fnt)
    S.save(path, quality=82)
ap = argparse.ArgumentParser(); ap.add_argument("videos", nargs="+"); ap.add_argument("--out", required=True); ap.add_argument("--thr", type=float, default=0.25)
a = ap.parse_args()
for f in map(Path, a.videos):
    o = Path(a.out) / f.stem; o.mkdir(parents=True, exist_ok=True)
    dur, W, H, has_a = probe(f)
    c = [t for t in cuts(f, a.thr) if 0.15 < t < dur - 0.1]
    bounds = [0.0] + c + [dur]
    shots = [{"i": i + 1, "start": round(bounds[i], 2), "end": round(bounds[i + 1], 2), "len": round(bounds[i + 1] - bounds[i], 2)} for i in range(len(bounds) - 1)]
    lens = sorted(s["len"] for s in shots)
    stats = {"file": f.name, "duration": round(dur, 2), "w": W, "h": H, "n_shots": len(shots), "avg_shot": round(dur / len(shots), 2),
             "median_shot": lens[len(lens) // 2], "cuts_first_3s": sum(1 for t in c if t <= 3), "cuts_first_10s": sum(1 for t in c if t <= 10),
             "first_cut": c[0] if c else None, "shots": shots}
    json.dump(stats, open(o / "cuts.json", "w"), indent=1)
    ts = [x * 0.25 for x in range(15)]
    sheet([frame(f, t, 216) for t in ts], [f"{t:.2f}s" for t in ts], 5, o / "hook_sheet.jpg")
    per = 24
    for k in range(0, len(shots), per):
        chunk = shots[k:k + per]
        sheet([frame(f, s["start"] + min(0.35, s["len"] / 2), 180) for s in chunk],
              [f"#{s['i']} {s['start']:.1f}s ({s['len']:.1f})" for s in chunk], 6, o / f"shots_sheet_{k // per + 1}.jpg")
    if has_a and not (o / "audio.mp3").exists():
        run(["ffmpeg", "-v", "quiet", "-i", str(f), "-vn", "-ac", "1", "-ar", "16000", "-b:a", "48k", str(o / "audio.mp3")])
    print(f.name, stats["duration"], "s", stats["n_shots"], "shots avg", stats["avg_shot"], "first cut", stats["first_cut"], flush=True)
