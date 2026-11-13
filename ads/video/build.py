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
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
from datetime import date
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
    """Cut one clip to an exact-length 1080x1920 30fps intermediate (near-lossless) with an audio
    track of the same length (silence when muted), so every join downstream is frame-exact."""
    zin, zout = float(clip["in"]), float(clip["out"])
    speed = float(clip.get("speed", 1.0))
    zoom = float(clip.get("zoom", 1.0))
    fx, fy = float(clip.get("focus", 0.5)), float(clip.get("focus_y", 0.5))
    if clip.get("push"):
        print(f"  clip {i}: 'push' is ignored (per-frame rescaling jitters); use a static 'zoom'")
    dur = (zout - zin) / speed
    cover = max(W / meta["w"], H / meta["h"]) * zoom
    sw, sh = math.ceil(meta["w"] * cover / 2) * 2, math.ceil(meta["h"] * cover / 2) * 2
    # constant 30 fps first (sources are 25/29.97/VFR/60), then a single high-quality resize + crop
    vf = [f"setpts=(PTS-STARTPTS)/{speed}", f"fps={FPS}", f"scale={sw}:{sh}:flags=lanczos",
          f"crop={W}:{H}:{int((sw - W) * fx)}:{int((sh - H) * fy)}"]
    if clip.get("hflip"):
        vf.append("hflip")
    if clip.get("eq"):
        vf.append(f"eq={clip['eq']}")
    vf += ["setsar=1", "format=yuv420p", f"trim=duration={dur:.4f}", "setpts=PTS-STARTPTS"]
    out = tmp / f"clip_{i:02d}.mp4"
    gain = float(clip.get("gain", 1.0))
    cmd = ["ffmpeg", "-v", "error", "-y", "-ss", f"{zin:.3f}", "-t", f"{zout - zin + 0.1:.3f}", "-i", str(src_path)]
    pad = f"apad,atrim=duration={dur:.4f},asetpts=PTS-STARTPTS"
    if meta["audio"] and gain > 0:
        af = ([f"atempo={speed}"] if speed != 1.0 else []) + [
            f"volume={gain}", "aresample=48000", "aformat=sample_fmts=fltp:channel_layouts=stereo", pad]
        fc = f"[0:v]{','.join(vf)}[v];[0:a]{','.join(af)}[a]"
    else:
        cmd += ["-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo"]
        fc = f"[0:v]{','.join(vf)}[v];[1:a]aformat=sample_fmts=fltp:channel_layouts=stereo,{pad}[a]"
    cmd += ["-filter_complex", fc, "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-preset", "medium",
            "-crf", "10", "-r", str(FPS), "-c:a", "pcm_s16le", str(out.with_suffix(".mov"))]
    run(cmd)
    return out.with_suffix(".mov"), dur


def speech_segments(path, silence_db=-40, min_pause=0.12, n=None):
    """(start, end) of each spoken line in a voiceover take. Pauses >= min_pause are candidate
    line breaks; with n, the n-1 longest pauses are used (sentence ends are longer than commas)."""
    out = subprocess.run(["ffmpeg", "-v", "info", "-i", str(path), "-af",
                          f"silencedetect=noise={silence_db}dB:d={min_pause}", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    dur = probe_audio_duration(path)
    starts = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", out)]
    ends = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", out)]
    ends += [dur] * (len(starts) - len(ends))
    speech_start = ends[0] if starts and starts[0] < 0.02 else 0.0
    speech_end = starts[-1] if starts and ends[-1] >= dur - 0.02 else dur
    pauses = [(s, e) for s, e in zip(starts, ends) if s > speech_start + 0.05 and e < speech_end - 0.05]
    if n:
        pauses = sorted(sorted(pauses, key=lambda p: p[1] - p[0], reverse=True)[:max(0, n - 1)])
    segs, cur = [], speech_start
    for s, e in pauses:
        segs.append((cur, s))
        cur = e
    segs.append((cur, speech_end))
    return segs


def probe_audio_duration(path):
    return float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)]).strip())


def brand_dir(edit_path):
    for d in edit_path.parents:
        if (d / "brand.json").exists():
            return d
    return None


def pick_end_card(edit, edit_path):
    """Resolve edit['end_card'] ('auto', a card name, or a path) from brand.json video.end_cards.
    'auto' picks the first card whose from/until window (inclusive) contains the edit's 'created'
    date (default: today); cards without a window are the fallback."""
    want = edit.get("end_card")
    if not want:
        return None
    bdir = brand_dir(edit_path)
    cards = json.loads((bdir / "brand.json").read_text()).get("video", {}).get("end_cards", []) if bdir else []
    if want != "auto":
        hit = next((c for c in cards if c["name"] == want), None)
        return (hit or {"name": want, "file": want})
    day = str(edit.get("created") or date.today().isoformat())
    for c in cards:
        if (c.get("from") or c.get("until")) and c.get("from", "0000") <= day <= c.get("until", "9999"):
            return c
    return next((c for c in cards if not c.get("from") and not c.get("until")), None)


def windows(durs, fades):
    """Clip start offsets in the crossfaded timeline and each clip's 'on screen' window
    (switching at the middle of each crossfade)."""
    offs, length = [], 0.0
    for i, d in enumerate(durs):
        off = 0.0 if i == 0 else length - fades[i]
        offs.append(off)
        length = off + d
    win = []
    for i in range(len(durs)):
        a = 0.0 if i == 0 else offs[i] + fades[i] / 2
        b = length if i == len(durs) - 1 else offs[i + 1] + fades[i + 1] / 2
        win.append((a, b))
    return offs, win, length


# ---------------------------------------------------------------- build

def build(edit_path, sheet_every=1.5, feed=True):
    edit_path = Path(edit_path).resolve()
    edit = json.loads(edit_path.read_text())
    out_dir = edit_path.parent
    vid = edit["id"]
    tmp = Path(tempfile.mkdtemp(prefix="vid_"))
    try:
        clips = [dict(c) for c in edit["clips"]]
        sources = dict(edit["sources"])
        n_content = len(clips)
        card = pick_end_card(edit, edit_path)
        if card:
            sources["_end_card"] = card["file"]
        srcs = {k: resolve_source(v) for k, v in sources.items()}
        metas = {k: probe(p) for k, p in srcs.items()}
        if card:
            secs = float(edit.get("end_card_seconds") or card.get("seconds") or metas["_end_card"]["dur"])
            clips.append({"src": "_end_card", "in": 0, "out": min(secs, metas["_end_card"]["dur"] - 0.05),
                          "gain": card.get("gain", 1.0),
                          "transition": edit.get("end_card_transition", "fade"),
                          "transition_duration": edit.get("end_card_transition_duration", 0.35)})

        # voiceover: split the take at its pauses (one line per content scene) and size each scene
        # so its line fits: window = lead + line + tail (at least the clip's "min" seconds)
        vo = edit.get("voiceover")
        vo_path, vo_segs = None, []
        if vo:
            vo_path = edit_path.parent / vo["file"]
            vo_path = vo_path if vo_path.exists() else resolve_source(vo["file"])
            vo_segs = vo.get("segments") or speech_segments(
                vo_path, vo.get("silence_db", -40), vo.get("min_pause", 0.12), n=n_content)
            if len(vo_segs) != n_content:
                raise SystemExit(f"voiceover has {len(vo_segs)} lines but there are {n_content} scenes: "
                                 f"{[(round(a, 2), round(b, 2)) for a, b in vo_segs]}")
            tempo = float(vo.get("tempo", 1.0))   # pitch-preserving speed-up of the whole take
            vo_segs = [(a / tempo, b / tempo) for a, b in vo_segs]
            lead, tail = float(vo.get("lead", 0.12)), float(vo.get("tail", 0.3))
            nominal = [0.0] + [float(c.get("transition_duration", edit.get("transition_duration", 0.25)))
                               if c.get("transition", edit.get("transition", "fade")) != "cut" else 1.0 / FPS
                               for c in clips[1:]] + [0.0]
            continuous = vo.get("mode", "continuous") == "continuous"
            if continuous:
                # the take plays unbroken from `lead`; each cut lands in the breath between two lines
                cuts = [0.0] + [lead + (vo_segs[i][1] + vo_segs[i + 1][0]) / 2 for i in range(n_content - 1)] \
                    + [lead + vo_segs[-1][1] + tail]
                wins = [cuts[i + 1] - cuts[i] for i in range(n_content)]
            else:
                wins = [max(float(clips[i].get("min", 1.6)), lead + (b - a) + tail) for i, (a, b) in enumerate(vo_segs)]
            for i in range(n_content):
                d = wins[i] + nominal[i] / 2 + nominal[i + 1] / 2
                clips[i]["out"] = round(float(clips[i]["in"]) + d * float(clips[i].get("speed", 1.0)), 3)
        parts, durs, fades = [], [], []
        for i, clip in enumerate(clips):
            meta = metas[clip["src"]]
            if float(clip["out"]) > meta["dur"] + 0.05:
                raise SystemExit(f"clip {i}: out {clip['out']} > source '{clip['src']}' duration {meta['dur']:.2f}")
            p, d = cut_clip(i, clip, srcs[clip["src"]], meta, tmp)
            parts.append(p)
            durs.append(d)
            t = clip.get("transition", edit.get("transition", "fade"))
            f = 1.0 / FPS if t == "cut" else float(clip.get("transition_duration", edit.get("transition_duration", 0.25)))
            fades.append(0.0 if i == 0 else min(f, d / 2, durs[i - 1] / 2))
            clip["_t"] = "fade" if t == "cut" else t
        offs, win, total = windows(durs, fades)

        inputs = []
        for p in parts:
            inputs += ["-i", str(p)]
        n = len(parts)
        g = [f"[{i}:v]settb=AVTB,setpts=PTS-STARTPTS[v{i}];[{i}:a]asetpts=PTS-STARTPTS[a{i}]" for i in range(n)]
        vl, al = "v0", "a0"
        for i in range(1, n):
            g.append(f"[{vl}][v{i}]xfade=transition={clips[i]['_t']}:duration={fades[i]:.4f}:offset={offs[i]:.4f}[vx{i}]")
            g.append(f"[{al}][a{i}]acrossfade=d={fades[i]:.4f}:c1=tri:c2=tri[ax{i}]")
            vl, al = f"vx{i}", f"ax{i}"

        # captions: timed by clip index ("clip": i or "clips": [a, b]) or explicit start/end;
        # each fades in/out over CAP_FADE except a caption that is on screen at t=0 (the hook)
        CAP_FADE = 0.12
        for j, cap in enumerate(edit.get("captions", [])):
            if "clip" in cap or "clips" in cap:
                a, b = cap.get("clips", [cap.get("clip")] * 2)
                if max(a, b) >= n_content:
                    raise SystemExit(f"caption {j}: clip index {max(a, b)} out of range (0..{n_content - 1})")
                s, e = win[a][0], win[b][1]
            else:
                s, e = float(cap["start"]), min(float(cap["end"]), total)
            s, e = s + float(cap.get("delay", 0)), min(e, total)
            png = tmp / f"cap_{j:02d}.png"
            ch = render_caption(cap, png)
            y = int(H * cap.get("y", 0.3) - ch / 2)
            k = n + j
            inputs += ["-loop", "1", "-framerate", str(FPS), "-t", f"{total:.3f}", "-i", str(png)]
            fx = ["format=rgba"]
            if s > 0.01:
                fx.append(f"fade=t=in:st={s:.3f}:d={CAP_FADE}:alpha=1")
            if e < total - 0.01:
                fx.append(f"fade=t=out:st={e - CAP_FADE:.3f}:d={CAP_FADE}:alpha=1")
            g.append(f"[{k}:v]{','.join(fx)}[cp{j}]")
            g.append(f"[{vl}][cp{j}]overlay=0:{y}:eof_action=pass:enable='between(t,{s:.3f},{e:.3f})'[vc{j}]")
            vl = f"vc{j}"

        next_in = n + len(edit.get("captions", []))
        A = "aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo"

        # voiceover: continuous mode plays the whole take once (natural flow); "lines" mode places
        # each line at its scene start. Then the end card's own line.
        voices = []
        if vo_path:
            inputs += ["-i", str(vo_path)]
            vin, gain = next_in, float(vo.get("gain", 1.0))
            next_in += 1
            lead = float(vo.get("lead", 0.12))
            if continuous:
                end = vo_segs[-1][1] + 0.15
                g.append(f"[{vin}:a]{A},volume={gain},atempo={tempo},atrim=0:{end:.3f},asetpts=PTS-STARTPTS,"
                         f"afade=t=out:st={end - 0.1:.3f}:d=0.1,adelay={int(lead * 1000)}:all=1[vp0]")
                voices.append("[vp0]")
            else:
                g.append(f"[{vin}:a]{A},volume={gain},atempo={tempo},asplit={len(vo_segs)}" + "".join(f"[vs{i}]" for i in range(len(vo_segs))))
                for i, (a, b) in enumerate(vo_segs):
                    at = int((win[i][0] + lead) * 1000)
                    g.append(f"[vs{i}]atrim={max(0, a - 0.04):.3f}:{b + 0.08:.3f},asetpts=PTS-STARTPTS,"
                             f"afade=t=in:d=0.02,afade=t=out:st={b - a + 0.06:.3f}:d=0.06,adelay={at}:all=1[vp{i}]")
                    voices.append(f"[vp{i}]")
            if card and card.get("vo"):
                inputs += ["-i", str(resolve_source(card["vo"]))]
                at = int((win[-1][0] + float(card.get("vo_delay", 0.35))) * 1000)
                g.append(f"[{next_in}:a]{A},volume={gain},adelay={at}:all=1[vpcard]")
                voices.append("[vpcard]")
                next_in += 1
            g.append(f"{''.join(voices)}amix=inputs={len(voices)}:normalize=0:duration=longest,"
                     f"apad=whole_dur={total:.3f},atrim=0:{total:.3f}[voall]")

        # music bed: low (gain ~0.15 = about -16 dB) and ducked a further ~6 dB under the voice
        music = edit.get("music")
        beds = []
        if music and music.get("file"):
            mp = edit_path.parent / music["file"]
            mp = mp if mp.exists() else resolve_source(music["file"])
            inputs += ["-stream_loop", "-1", "-i", str(mp)]
            g.append(f"[{next_in}:a]{A},atrim={float(music.get('start', 0)):.3f}:{float(music.get('start', 0)) + total:.3f},"
                     f"asetpts=PTS-STARTPTS,volume={music.get('gain', 0.15)},afade=t=in:d=0.3,"
                     f"afade=t=out:st={max(0, total - 0.8):.3f}:d=0.8[mus]")
            next_in += 1
            if vo_path and music.get("duck", True):
                g.append("[voall]asplit=2[voa][vosc]")
                g.append("[mus][vosc]sidechaincompress=threshold=0.02:ratio=4:attack=30:release=350:makeup=1[musd]")
                beds, vo_label = ["[musd]"], "[voa]"
            else:
                beds, vo_label = ["[mus]"], "[voall]" if vo_path else ""
        else:
            vo_label = "[voall]" if vo_path else ""
        mix = [f"[{al}]"] + ([vo_label] if vo_label else []) + beds
        if len(mix) > 1:
            g.append(f"{''.join(mix)}amix=inputs={len(mix)}:normalize=0:duration=first[amixed]")
            al = "amixed"
        loud = edit.get("loudness", -14)
        g.append(f"[{al}]loudnorm=I={loud}:TP=-1.5:LRA=11,aresample=48000[aout]")
        g.append(f"[{vl}]format=yuv420p[vout]")
        final = out_dir / f"{vid}.mp4"
        run(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", ";".join(g),
             "-map", "[vout]", "-map", "[aout]", "-r", str(FPS), "-c:v", "libx264", "-preset", "slow",
             "-crf", "17", "-profile:v", "high", "-pix_fmt", "yuv420p", "-g", str(FPS * 2),
             "-movflags", "+faststart", "-c:a", "aac", "-b:a", "192k", "-t", f"{total:.3f}", str(final)])
        outs = [final]
        if feed:
            f45 = out_dir / f"{vid}_4x5.mp4"
            run(["ffmpeg", "-v", "error", "-y", "-i", str(final), "-vf", f"crop={W}:{FEED_H}:0:{(H - FEED_H) // 2}",
                 "-c:v", "libx264", "-preset", "slow", "-crf", "17", "-pix_fmt", "yuv420p", "-g", str(FPS * 2),
                 "-movflags", "+faststart", "-c:a", "copy", str(f45)])
            outs.append(f45)
        outs.append(sheet(final, out_dir / f"{vid}_sheet.jpg", every=sheet_every))
        print(f"{vid}: {total:.2f}s, {n_content} clips" + (f" + end card '{card['name']}'" if card else "")
              + f", {len(edit.get('captions', []))} captions")
        for i, (a, b) in enumerate(win):
            print(f"   clip {i}: {a:6.2f} - {b:6.2f}  {clips[i]['src']}")
        (out_dir / f"{vid}_timeline.json").write_text(json.dumps(
            {"total": round(total, 3), "scenes": [{"src": clips[i]["src"], "start": round(a, 3), "end": round(b, 3)}
                                                  for i, (a, b) in enumerate(win)]}, indent=1))
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
