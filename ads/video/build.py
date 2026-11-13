"""Render a short-form video ad from an edit file (edit.json) with ffmpeg.

An edit file lists source footage, the clips cut from it, on-screen captions and the
audio plan. This script downloads Drive sources, cuts and reframes every clip to 9:16,
burns in native-looking captions, mixes the audio and writes:

    <id>.mp4         1080x1920, 30 fps, H.264/AAC, loudness-normalized (Reels/TikTok/Stories)
    <id>_4x5.mp4     1080x1350 center crop (Meta feed); captions stay inside it by design
    <id>_sheet.jpg   contact sheet, one frame every `--sheet-every` seconds, for QA

Usage:
    python ads/video/build.py ads/brands/comfortwear/video/<folder>/<id>/edit.json
    python ads/video/build.py <edit.json> --sheet-every 1      # denser QA sheet
    python ads/video/build.py <edit.json> --no-4x5             # skip the feed crop
    python ads/video/build.py --probe drive:<fileId>           # download + print duration/size
    python ads/video/build.py --sheet drive:<fileId> --every 2 # contact sheet of a raw source

Edit file schema (see the skill `video-ads` for the full guide):
{
  "id": "V47_01_disney_plus_size_pov",
  "sources": {"a": "drive:<fileId>", "b": "path/relative/to/repo.mp4"},
  "clips": [
    {"src": "a", "in": 3.2, "out": 5.0,          # seconds in the source
     "focus": 0.5,                               # horizontal crop center 0..1 for landscape/odd sizes
     "focus_y": 0.5,                             # vertical crop center 0..1
     "zoom": 1.0,                                # extra punch-in (1.15 = 15% tighter)
     "push": 0.0,                                # slow zoom over the clip (0.06 = +6% by the end)
     "speed": 1.0,                               # 0.5..2.0
     "gain": 1.0,                                # source audio level for this clip (0 = mute)
     "hflip": false}
  ],
  "captions": [
    {"start": 0.0, "end": 3.0, "text": "POV: ...", "style": "box", "y": 0.30, "size": 54, "width": 0.84}
  ],
  "music": {"file": "path.mp3", "gain": 0.25},  # optional; licensed tracks only
  "loudness": -14
}
Caption styles: box (white rounded box, black text: TikTok classic), outline (white text,
black stroke), dark (black box, white text), brand (brand-colored pill, white text).
`y` is the caption's vertical center as a fraction of the 1920px frame. Keep captions between
y 0.18 and 0.72: that is inside the 4:5 feed crop and clear of the TikTok/Reels UI.
"""

import argparse
import json
import math
import shutil
import subprocess
import sys
import tempfile
import unicodedata
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[2]
VIDEO_DIR = Path(__file__).resolve().parent
CACHE = ROOT / "ads" / ".cache" / "footage"
FONTS = VIDEO_DIR / "fonts"
EMOJI_FONT = Path("/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf")
W, H, FPS = 1080, 1920, 30
FEED_H = 1350
DRIVE_URL = "https://drive.usercontent.google.com/download?id={id}&export=download&confirm=t"
BRAND_PURPLE = "#7A2FE0"


def run(cmd, quiet=True):
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        sys.stderr.write(" ".join(map(str, cmd)) + "\n" + res.stderr[-3000:])
        raise SystemExit(f"command failed: {cmd[0]}")
    return res.stdout


# ---------------------------------------------------------------- sources

def resolve_source(spec):
    """Return a local path for 'drive:<id>' or a repo-relative/absolute path."""
    if spec.startswith("drive:"):
        fid = spec.split(":", 1)[1]
        CACHE.mkdir(parents=True, exist_ok=True)
        hits = list(CACHE.glob(f"{fid}.*"))
        if hits:
            return hits[0]
        tmp = CACHE / f"{fid}.part"
        print(f"  downloading {fid} ...", flush=True)
        run(["curl", "-sS", "-L", "--fail", "--retry", "3", "-o", str(tmp), DRIVE_URL.format(id=fid)])
        kind = run(["file", "-b", "--mime-type", str(tmp)]).strip()
        if not kind.startswith(("video/", "image/", "audio/")):
            tmp.unlink(missing_ok=True)
            raise SystemExit(f"Drive file {fid} did not download as media ({kind}); is it shared by link?")
        ext = {"video/quicktime": ".mov", "video/mp4": ".mp4", "image/jpeg": ".jpg",
               "image/png": ".png", "audio/mpeg": ".mp3"}.get(kind, "." + kind.split("/")[-1])
        out = CACHE / f"{fid}{ext}"
        tmp.rename(out)
        return out
    p = Path(spec)
    return p if p.is_absolute() else ROOT / p


def probe(path):
    info = json.loads(run(["ffprobe", "-v", "error", "-print_format", "json", "-show_streams",
                           "-show_format", str(path)]))
    v = next((s for s in info["streams"] if s["codec_type"] == "video"), None)
    a = any(s["codec_type"] == "audio" for s in info["streams"])
    w, h = int(v["width"]), int(v["height"])
    rot = 0
    for sd in v.get("side_data_list", []) or []:
        if "rotation" in sd:
            rot = int(sd["rotation"])
    rot = int(v.get("tags", {}).get("rotate", rot))
    if abs(rot) % 180 == 90:
        w, h = h, w
    return {"w": w, "h": h, "dur": float(info["format"].get("duration", 0)), "audio": a}


def sheet(path, out, every=2.0, cols=6, width=240):
    """Contact sheet with timestamps: the way to *watch* footage before cutting it."""
    meta = probe(path)
    n = max(1, math.ceil(meta["dur"] / every))
    rows = math.ceil(n / cols)
    font = (FONTS / "Inter-Bold.otf").as_posix()
    run(["ffmpeg", "-v", "error", "-y", "-i", str(path), "-vf",
         f"fps=1/{every},scale={width}:-2,drawtext=fontfile={font}:text='%{{pts\\:hms}}':x=4:y=4:"
         f"fontsize=15:fontcolor=yellow:box=1:boxcolor=black@0.7,tile={cols}x{rows}",
         "-frames:v", "1", "-q:v", "3", str(out)])
    return out


# ---------------------------------------------------------------- captions

def is_emoji(ch):
    cp = ord(ch)
    return (0x1F000 <= cp <= 0x1FAFF or 0x2600 <= cp <= 0x27BF or 0x2B00 <= cp <= 0x2BFF
            or cp in (0x200D, 0xFE0F, 0x2764))


def runs(text):
    """Split into (is_emoji, string) runs; ZWJ/VS16 stay with their emoji."""
    out = []
    for ch in text:
        e = is_emoji(ch)
        if out and out[-1][0] == e:
            out[-1][1] += ch
        else:
            out.append([e, ch])
    return out


class Typesetter:
    def __init__(self, size, weight="Bold"):
        self.size = size
        self.font = ImageFont.truetype(str(FONTS / f"Inter-{weight}.otf"), size)
        self.emoji = ImageFont.truetype(str(EMOJI_FONT), 109) if EMOJI_FONT.exists() else None

    def emoji_img(self, s):
        if not self.emoji:
            return None
        im = Image.new("RGBA", (160 * len(s), 160), (0, 0, 0, 0))
        ImageDraw.Draw(im).text((0, 0), s, font=self.emoji, embedded_color=True)
        bbox = im.getbbox()
        if not bbox:
            return None
        im = im.crop(bbox)
        k = self.size * 1.05 / im.height
        return im.resize((max(1, int(im.width * k)), max(1, int(im.height * k))), Image.LANCZOS)

    def width(self, line):
        w = 0
        for e, s in runs(line):
            if e:
                im = self.emoji_img(s)
                w += im.width + 4 if im else 0
            else:
                w += self.font.getlength(s)
        return int(w)

    def _greedy(self, words, max_w):
        lines, cur = [], ""
        for word in words:
            trial = (cur + " " + word).strip()
            if cur and self.width(trial) > max_w:
                lines.append(cur)
                cur = word
            else:
                cur = trial
        lines.append(cur)
        return lines

    def wrap(self, text, max_w):
        """Greedy wrap, then balance: shrink the width while the line count holds, so lines come
        out even (no orphan word on the last line). Emoji-only tokens stick to the word before."""
        lines = []
        for para in text.split("\n"):
            words = []
            for w in para.split(" "):
                if words and w and all(is_emoji(c) for c in w):
                    words[-1] += " " + w
                elif w:
                    words.append(w)
            best = self._greedy(words, max_w)
            if len(best) > 1:
                w = max_w
                while w > max_w * 0.5:
                    trial = self._greedy(words, w - 10)
                    if len(trial) != len(best):
                        break
                    best, w = trial, w - 10
            lines += best
        return lines

    def draw_line(self, canvas, x, y, line, fill, stroke=0, stroke_fill=None):
        d = ImageDraw.Draw(canvas)
        asc, desc = self.font.getmetrics()
        for e, s in runs(line):
            if e:
                im = self.emoji_img(s)
                if im:
                    canvas.alpha_composite(im, (int(x) + 2, int(y + (asc + desc - im.height) / 2)))
                    x += im.width + 4
            else:
                d.text((x, y), s, font=self.font, fill=fill, stroke_width=stroke, stroke_fill=stroke_fill)
                x += self.font.getlength(s)


def render_caption(cap, out_png):
    style = cap.get("style", "box")
    size = int(cap.get("size", 52))
    max_w = int(W * cap.get("width", 0.84))
    ts = Typesetter(size, cap.get("weight", "Bold" if style != "box" else "SemiBold"))
    pad_x, pad_y = int(size * 0.42), int(size * 0.20)
    lines = ts.wrap(cap["text"], max_w - 2 * pad_x)
    asc, desc = ts.font.getmetrics()
    line_h = int((asc + desc) * 1.02)
    canvas = Image.new("RGBA", (W, line_h * len(lines) + 2 * pad_y + 40), (0, 0, 0, 0))
    d = ImageDraw.Draw(canvas)
    align = cap.get("align", "center")
    colors = {"box": ("white", "black"), "dark": ("black", "white"),
              "brand": (cap.get("color", BRAND_PURPLE), "white")}
    for i, line in enumerate(lines):
        lw = ts.width(line)
        x = (W - lw) / 2 if align == "center" else int(W * (1 - cap.get("width", 0.84)) / 2) + pad_x
        y = pad_y + i * line_h + 10
        if style in colors:
            bg, fg = colors[style]
            r = int(size * 0.32)
            d.rounded_rectangle([x - pad_x, y - pad_y + 2, x + lw + pad_x, y + line_h + pad_y - 4],
                                radius=r, fill=bg)
            ts.draw_line(canvas, x, y, line, fg)
        else:  # outline
            ts.draw_line(canvas, x, y, line, "white", stroke=max(3, size // 12), stroke_fill="black")
    # merge the per-line boxes into one shape the way TikTok does (fill gaps between lines)
    canvas = canvas.crop(canvas.getbbox() or (0, 0, W, 10))
    full = Image.new("RGBA", (W, canvas.height), (0, 0, 0, 0))
    full.alpha_composite(canvas, ((W - canvas.width) // 2 if align == "center" else 0, 0))
    full.save(out_png)
    return full.height


# ---------------------------------------------------------------- clips

def cut_clip(i, clip, src_path, meta, tmp):
    zin, zout = float(clip["in"]), float(clip["out"])
    speed = float(clip.get("speed", 1.0))
    zoom = float(clip.get("zoom", 1.0))
    push = float(clip.get("push", 0.0))
    fx, fy = float(clip.get("focus", 0.5)), float(clip.get("focus_y", 0.5))
    dur = (zout - zin) / speed
    # scale to cover 1080x1920 (times zoom, plus room for the push), then crop at the focus point
    cover = max(W / meta["w"], H / meta["h"]) * zoom
    sw, sh = math.ceil(meta["w"] * cover / 2) * 2, math.ceil(meta["h"] * cover / 2) * 2
    vf = [f"setpts=(PTS-STARTPTS)/{speed}", f"scale={sw}:{sh}:flags=lanczos"]
    if push:
        # grow the frame a little every frame (eval=frame), then take a fixed 1080x1920 window
        k = f"(1+{push}*t/{dur:.3f})"
        vf.append(f"scale=w='trunc({sw}*{k}/2)*2':h='trunc({sh}*{k}/2)*2':eval=frame:flags=bicubic")
        vf.append(f"crop={W}:{H}:x='(in_w-{W})*{fx}':y='(in_h-{H})*{fy}'")
    else:
        vf.append(f"crop={W}:{H}:{int((sw - W) * fx)}:{int((sh - H) * fy)}")
    if clip.get("hflip"):
        vf.append("hflip")
    if clip.get("eq"):
        vf.append(f"eq={clip['eq']}")
    vf += [f"fps={FPS}", "setsar=1", "format=yuv420p"]
    out = tmp / f"clip_{i:02d}.mp4"
    gain = float(clip.get("gain", 1.0))
    cmd = ["ffmpeg", "-v", "error", "-y", "-ss", f"{zin:.3f}", "-t", f"{zout - zin:.3f}", "-i", str(src_path)]
    if meta["audio"] and gain > 0:
        af = [f"atempo={speed}"] if speed != 1.0 else []
        af += [f"volume={gain}", "aresample=48000", "aformat=channel_layouts=stereo"]
        cmd += ["-filter_complex", f"[0:v]{','.join(vf)}[v];[0:a]{','.join(af)}[a]",
                "-map", "[v]", "-map", "[a]"]
    else:
        cmd += ["-f", "lavfi", "-t", f"{dur:.3f}", "-i", "anullsrc=r=48000:cl=stereo",
                "-filter_complex", f"[0:v]{','.join(vf)}[v]", "-map", "[v]", "-map", "1:a"]
    cmd += ["-t", f"{dur:.3f}", "-c:v", "libx264", "-preset", "medium", "-crf", "17",
            "-c:a", "aac", "-b:a", "192k", "-ar", "48000", str(out)]
    run(cmd)
    return out, dur


# ---------------------------------------------------------------- build

def build(edit_path, sheet_every=1.5, feed=True):
    edit_path = Path(edit_path).resolve()
    edit = json.loads(edit_path.read_text())
    out_dir = edit_path.parent
    vid = edit["id"]
    tmp = Path(tempfile.mkdtemp(prefix="vid_"))
    try:
        srcs = {k: resolve_source(v) for k, v in edit["sources"].items()}
        metas = {k: probe(p) for k, p in srcs.items()}
        parts, total = [], 0.0
        for i, clip in enumerate(edit["clips"]):
            meta = metas[clip["src"]]
            if float(clip["out"]) > meta["dur"] + 0.05:
                raise SystemExit(f"clip {i}: out {clip['out']} > source '{clip['src']}' duration {meta['dur']:.2f}")
            p, d = cut_clip(i, clip, srcs[clip["src"]], meta, tmp)
            parts.append(p)
            total += d
        lst = tmp / "list.txt"
        lst.write_text("".join(f"file '{p}'\n" for p in parts))
        base = tmp / "base.mp4"
        run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy", str(base)])

        # captions -> PNG overlays
        inputs, chains, label = ["-i", str(base)], [], "0:v"
        for j, cap in enumerate(edit.get("captions", [])):
            png = tmp / f"cap_{j:02d}.png"
            ch = render_caption(cap, png)
            y = int(H * cap.get("y", 0.3) - ch / 2)
            inputs += ["-i", str(png)]
            end = min(float(cap["end"]), total)
            chains.append(f"[{label}][{j + 1}:v]overlay=0:{y}:enable='between(t,{cap['start']},{end})'[c{j}]")
            label = f"c{j}"
        n_in = len(edit.get("captions", [])) + 1

        # audio: clip audio (+ optional music bed), then loudness normalization
        music = edit.get("music")
        a_chain = "[0:a]anull[a0]"
        if music and music.get("file"):
            mpath = resolve_source(music["file"])
            inputs += ["-stream_loop", "-1", "-i", str(mpath)]
            a_chain = (f"[{n_in}:a]volume={music.get('gain', 0.25)},atrim=0:{total:.3f},"
                       f"afade=t=out:st={max(0, total - 0.6):.3f}:d=0.6[m];[0:a][m]amix=inputs=2:normalize=0[a0]")
        loud = edit.get("loudness", -14)
        a_chain += f";[a0]loudnorm=I={loud}:TP=-1.5:LRA=11,aresample=48000[aout]"
        fc = ";".join(chains + [a_chain]) if chains else f"[0:v]null[vout];{a_chain}"
        vout = f"[{label}]" if chains else "[vout]"
        final = out_dir / f"{vid}.mp4"
        run(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", fc, "-map", vout, "-map", "[aout]",
             "-c:v", "libx264", "-preset", "slow", "-crf", "18", "-profile:v", "high", "-pix_fmt", "yuv420p",
             "-movflags", "+faststart", "-c:a", "aac", "-b:a", "192k", "-t", f"{total:.3f}", str(final)])
        outs = [final]
        if feed:
            f45 = out_dir / f"{vid}_4x5.mp4"
            run(["ffmpeg", "-v", "error", "-y", "-i", str(final), "-vf", f"crop={W}:{FEED_H}:0:{(H - FEED_H) // 2}",
                 "-c:v", "libx264", "-preset", "slow", "-crf", "18", "-pix_fmt", "yuv420p",
                 "-movflags", "+faststart", "-c:a", "copy", str(f45)])
            outs.append(f45)
        outs.append(sheet(final, out_dir / f"{vid}_sheet.jpg", every=sheet_every))
        print(f"{vid}: {total:.1f}s, {len(edit['clips'])} clips, {len(edit.get('captions', []))} captions")
        for o in outs:
            print("  ", o)
        return outs
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("edit", nargs="?", help="path to edit.json")
    ap.add_argument("--sheet-every", type=float, default=1.5)
    ap.add_argument("--no-4x5", action="store_true")
    ap.add_argument("--probe", help="drive:<id> or path: download and print size/duration")
    ap.add_argument("--sheet", help="drive:<id> or path: contact sheet of a raw source")
    ap.add_argument("--every", type=float, default=2.0, help="seconds between frames for --sheet")
    ap.add_argument("--out", help="output path for --sheet")
    a = ap.parse_args()
    if a.probe:
        p = resolve_source(a.probe)
        print(p, probe(p))
    elif a.sheet:
        p = resolve_source(a.sheet)
        out = Path(a.out) if a.out else p.with_name(p.stem + "_sheet.jpg")
        print(sheet(p, out, every=a.every), probe(p))
    elif a.edit:
        build(a.edit, a.sheet_every, feed=not a.no_4x5)
    else:
        ap.print_help()


if __name__ == "__main__":
    main()
