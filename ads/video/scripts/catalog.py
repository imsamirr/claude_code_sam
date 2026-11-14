"""Catalogue video assets: metadata + contact sheets (2 frames per clip at 25%/70%, labelled #id name dur WxH).
    python catalog.py <root> [<root>...] --out <dir>   -> <dir>/catalog.json, <dir>/<group>_NN.jpg"""
import argparse, io, json, re, subprocess
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
F = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 13)
ap = argparse.ArgumentParser(); ap.add_argument("roots", nargs="+"); ap.add_argument("--out", required=True); a = ap.parse_args()
out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
files = [p for r in a.roots for p in sorted(Path(r).rglob("*")) if p.suffix.lower() in (".mp4", ".mov", ".m4v", ".gif")
         and not (p.name.endswith(".px.mp4") is False and p.with_suffix(".px.mp4").exists())]
def probe(p):
    j = json.loads(subprocess.run(["ffprobe", "-v", "quiet", "-print_format", "json", "-show_streams", "-show_format", str(p)], capture_output=True, text=True).stdout or "{}")
    v = next((s for s in j.get("streams", []) if s.get("codec_type") == "video"), None)
    if not v: return None
    w, h = int(v["width"]), int(v["height"])
    rot = 0
    for sd in v.get("side_data_list", []) or []:
        if "rotation" in sd: rot = abs(int(sd["rotation"]))
    if rot in (90, 270): w, h = h, w
    return {"dur": float(j["format"].get("duration", 0) or 0), "w": w, "h": h, "audio": any(s.get("codec_type") == "audio" for s in j["streams"])}
def frame(p, t, H=200):
    b = subprocess.run(["ffmpeg", "-v", "quiet", "-ss", f"{t:.2f}", "-i", str(p), "-frames:v", "1", "-vf", f"scale=-2:{H}", "-f", "image2pipe", "-vcodec", "png", "-"], capture_output=True).stdout
    return Image.open(io.BytesIO(b)).convert("RGB") if b else Image.new("RGB", (112, H), "gray")
def tile(i, p):
    m = probe(p)
    if not m: return None
    ims = [frame(p, m["dur"] * f) for f in (0.25, 0.7)]
    T = Image.new("RGB", (232, 232), "white")
    x = 0
    for im in ims:
        im.thumbnail((116, 200)); T.paste(im, (x + (116 - im.width) // 2, 0)); x += 116
    d = ImageDraw.Draw(T); name = re.sub(r"\.px$", "", p.stem)
    d.text((2, 201), f"#{i} {m['dur']:.0f}s {m['w']}x{m['h']}{'' if m['audio'] else ' mute'}", fill="black", font=F)
    d.text((2, 216), name[:34], fill="black", font=F)
    return {"id": i, "path": str(p), "name": name, **m}, T
with ThreadPoolExecutor(4) as ex:
    res = list(ex.map(lambda ip: tile(*ip), enumerate(files, 1)))
res = [r for r in res if r]
json.dump([r[0] for r in res], open(out / "catalog.json", "w"), indent=0)
groups = {}
for meta, T in res:
    g = re.sub(r"[^A-Za-z0-9]+", "_", str(Path(meta["path"]).parent.relative_to(Path(meta["path"]).parents[len(Path(meta["path"]).parts) - 3]) if False else Path(meta["path"]).parent.name))[:30]
    groups.setdefault(g, []).append(T)
for g, ts in groups.items():
    for k in range(0, len(ts), 30):
        ch = ts[k:k + 30]; S = Image.new("RGB", (5 * 232, ((len(ch) + 4) // 5) * 232), "white")
        for j, T in enumerate(ch): S.paste(T, ((j % 5) * 232, (j // 5) * 232))
        S.save(out / f"{g}_{k // 30 + 1:02d}.jpg", quality=80)
print(len(res), "clips;", {g: len(t) for g, t in groups.items()})
