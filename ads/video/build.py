"""Render a short-form video ad from an edit file (edit.json) with ffmpeg.

An edit file lists source footage, the clips cut from it, on-screen captions and the
audio plan. This script downloads Drive sources, cuts and reframes every clip to 9:16,
burns in native-looking captions, mixes the audio and writes:

    <id>.mp4         1080x1920, 30 fps, H.264/AAC, loudness-normalized. The only deliverable: all text and
                     key content sit inside the centered 4:5 area (y 285-1635), so the same file runs in
                     Reels/TikTok/Stories and in 4:5 feed placements (--with-4x5 writes a crop if wanted)
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
SAFE_TOP, SAFE_BOT = (H - FEED_H) / 2 / H, (H + FEED_H) / 2 / H   # 4:5 area inside 9:16
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
    """Return a local path for 'drive:<id>', 'tiktok:<video id>' or a repo-relative/absolute path."""
    if spec.startswith("tiktok:"):
        vid = spec.split(":", 1)[1].strip()
        CACHE.mkdir(parents=True, exist_ok=True)
        out = CACHE / f"tiktok_{vid}.mp4"
        if not out.exists():
            print(f"  downloading TikTok {vid} ...", flush=True)
            run(["yt-dlp", "--impersonate", "chrome", "-q", "--no-warnings", "-f", "b[ext=mp4]/b",
                 "-o", str(out), f"https://www.tiktok.com/@x/video/{vid}"])
        return out
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
            or 0x2300 <= cp <= 0x23FF or 0x2190 <= cp <= 0x21FF or 0x2934 <= cp <= 0x2935
            or cp in (0x200D, 0xFE0F, 0x2764, 0x203C, 0x2049, 0x2122, 0x2139, 0x3030, 0x303D))


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
    return full.height, canvas.width


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
    dur = max(2, round((zout - zin) / speed * FPS)) / FPS   # whole frames: keeps the xfade chain exact
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
    # blur boxes (logos, other brands' markings): [{"box": [x0, y0, x1, y1], "t": [a, b], "strength": 28}]
    # box in fractions of the 1080x1920 output frame, t in seconds of this clip's output (optional)
    vchain = f"[0:v]{','.join(vf)}[vb0]"
    # shift_y: move the picture down (fraction of H, max 0.14) so faces near the top land inside the
    # 4:5 area; the band it opens at the top (outside 4:5) is filled with a blurred copy
    sy = min(0.14, float(clip.get("shift_y", 0)))
    if sy > 0:
        sh = int(sy * H) // 2 * 2
        vchain = (f"[0:v]{','.join(vf)}[vs0];[vs0]split[vsa][vsb];"
                  f"[vsa]scale={int(W * 1.3) // 2 * 2}:-2,crop={W}:{H},boxblur=30:3[vsbg];"
                  f"[vsb]crop={W}:{H - sh}:0:0[vsfg];[vsbg][vsfg]overlay=0:{sh}[vb0]")
    for bi, bl in enumerate(clip.get("blur", [])):
        x0, y0, x1, y1 = bl["box"]
        bx, by = int(x0 * W) // 2 * 2, int(y0 * H) // 2 * 2
        bw, bh = max(8, int((x1 - x0) * W) // 2 * 2), max(8, int((y1 - y0) * H) // 2 * 2)
        st = int(bl.get("strength", 28))
        st = min(st, bw // 2 - 1, bh // 2 - 1)
        en = f":enable='between(t,{bl['t'][0]},{bl['t'][1]})'" if bl.get("t") else ""
        vchain += (f";[vb{bi}]split[vs{bi}a][vs{bi}b];[vs{bi}b]crop={bw}:{bh}:{bx}:{by},boxblur={st}:3"
                   f"[vbb{bi}];[vs{bi}a][vbb{bi}]overlay={bx}:{by}{en}[vb{bi + 1}]")
    vchain += f";[vb{len(clip.get('blur', []))}]null[v]"
    if meta["audio"] and gain > 0:
        af = ([f"atempo={speed}"] if speed != 1.0 else []) + [
            f"volume={gain}", "aresample=48000", "aformat=sample_fmts=fltp:channel_layouts=stereo", pad]
        fc = f"{vchain};[0:a]{','.join(af)}[a]"
    else:
        cmd += ["-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo"]
        fc = f"{vchain};[1:a]aformat=sample_fmts=fltp:channel_layouts=stereo,{pad}[a]"
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


_CASCADES = None
_YUNET = None
YUNET_MODEL = Path(__file__).resolve().parent / "models" / "yunet.onnx"


def face_boxes(path, t):
    """Face boxes (y0, y1, x0, x1 as fractions of the frame) in the frame of `path` at t seconds.
    YuNet DNN detector (ads/video/models/yunet.onnx: robust to expressions, motion, profiles);
    falls back to OpenCV Haar cascades if the model or cv2.FaceDetectorYN is missing."""
    global _CASCADES, _YUNET
    try:
        import cv2
    except ImportError:
        return []
    cap = cv2.VideoCapture(str(path))
    cap.set(cv2.CAP_PROP_POS_MSEC, max(0.0, t) * 1000)
    ok, frame = cap.read()
    cap.release()
    if not ok:
        return []
    h, w = frame.shape[:2]
    if YUNET_MODEL.exists() and hasattr(cv2, "FaceDetectorYN"):
        sw, sh = 360, int(360 * h / w)
        if _YUNET is None or _YUNET[1] != (sw, sh):
            _YUNET = (cv2.FaceDetectorYN.create(str(YUNET_MODEL), "", (sw, sh), 0.6, 0.3, 5000), (sw, sh))
        _, faces = _YUNET[0].detect(cv2.resize(frame, (sw, sh)))
        return [] if faces is None else [(r[1] / sh, (r[1] + r[3]) / sh, r[0] / sw, (r[0] + r[2]) / sw)
                                         for r in faces]
    if _CASCADES is None:
        d = cv2.data.haarcascades
        _CASCADES = [cv2.CascadeClassifier(d + n) for n in
                     ("haarcascade_frontalface_default.xml", "haarcascade_profileface.xml",
                      "haarcascade_frontalface_alt2.xml")]
    small = cv2.resize(frame, (w // 3, h // 3))
    gray = cv2.equalizeHist(cv2.cvtColor(small, cv2.COLOR_BGR2GRAY))
    sw, sh = gray.shape[1], gray.shape[0]
    found = []
    for k, cc in enumerate(_CASCADES):
        for img, flip in ((gray, False), (cv2.flip(gray, 1), True)) if k == 1 else ((gray, False),):
            for (x, y, fw, fh) in cc.detectMultiScale(img, 1.1, 6, minSize=(int(sw * 0.09), int(sw * 0.09))):
                if flip:
                    x = sw - x - fw
                found.append((y / sh, (y + fh) / sh, x / sw, (x + fw) / sw))
    return found


def chunk_line(text, max_words=4):
    """Split a VO line into short subtitle chunks, breaking after punctuation when possible."""
    words, out, cur = text.split(), [], []
    for wd in words:
        cur.append(wd)
        if len(cur) >= max_words or (wd[-1] in ",.?!:;—" and len(cur) >= 2):
            out.append(" ".join(cur))
            cur = []
    if cur:
        if out and len(cur) == 1 and len(out[-1].split()) < max_words + 1:
            out[-1] += " " + cur[0]
        else:
            out.append(" ".join(cur))
    return out


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
    lang = edit.get("lang", "en")
    same = [c for c in cards if c.get("lang", "en") == lang]
    cards = same or [c for c in cards if c.get("lang", "en") == "en"]
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

def build(edit_path, sheet_every=1.5, feed=False):
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
            f = 0.0 if i == 0 else min(f, d / 2, durs[i - 1] / 2)
            fades.append(max(1, round(f * FPS)) / FPS if i else 0.0)
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

        # subtitles from the voiceover: one short chunk at a time, timed to the speech of each line
        caps_all = [dict(c) for c in edit.get("captions", [])]
        if vo and vo.get("lines"):
            lines = vo["lines"]
            if len(lines) != len(vo_segs):
                raise SystemExit(f"voiceover.lines has {len(lines)} entries, take has {len(vo_segs)} lines")
            lead = float(vo.get("lead", 0.12))
            sub = {"style": "box", "size": 58, "width": 0.86, "y": 0.70, "fade": 0.0, **vo.get("sub", {})}
            for i, (line, (a, b)) in enumerate(zip(lines, vo_segs)):
                if not line:
                    continue
                t0 = (lead + a) if continuous else (win[i][0] + lead)
                t1 = t0 + (b - a)
                chunks = chunk_line(line, int(sub.get("max_words", 4)))
                weights = [max(4, len(c)) for c in chunks]
                tt = t0
                for k, ch_text in enumerate(chunks):
                    d = (t1 - t0) * weights[k] / sum(weights)
                    end = tt + d if k < len(chunks) - 1 else min(t1 + 0.25, win[i][1])
                    caps_all.append({**sub, "text": ch_text, "start": tt, "end": end, "_scene": i,
                                     **(vo.get("sub_overrides", {}).get(str(i), {}))})
                    tt += d

        def scene_at(t):
            return next((i for i, (a, b) in enumerate(win) if a <= t < b), len(win) - 1)

        # captions: timed by clip index ("clip": i or "clips": [a, b]) or explicit start/end.
        # Each is placed at its requested y unless that covers a face (Haar detection on the frames
        # it spans), a clip's "keep_clear" bands, or another caption on screen at the same time;
        # then it moves to the nearest clear y in 0.17..0.76.
        placed_boxes = []

        def resolve(cap):
            if "clip" in cap or "clips" in cap:
                a, b = cap.get("clips", [cap.get("clip")] * 2)
                if max(a, b) >= n_content:
                    raise SystemExit(f"caption clip index {max(a, b)} out of range (0..{n_content - 1})")
                s0, e0 = win[a][0], win[b][1]
            else:
                s0, e0 = float(cap["start"]), min(float(cap["end"]), total)
            return max(0.0, s0 + float(cap.get("delay", 0))), min(e0, total)

        def find_y(cap, s, e, ch, cw):
            """Nearest y to the requested one that keeps the caption off faces (sampled every 0.25 s),
            keep_clear bands and other captions, inside the 4:5 area. None if no y is clear."""
            want = float(cap.get("y", 0.3))
            blocks = []
            if cap.get("avoid_faces", edit.get("avoid_faces", True)):
                nst = max(4, min(80, int((e - s) / 0.25)))
                for t in [s + (e - s) * (k + 0.5) / nst for k in range(nst)]:
                    i = scene_at(t)
                    for fb in face_boxes(parts[i], t - offs[i]):
                        fh = fb[1] - fb[0]
                        blocks.append((fb[0] - 0.12 * fh, fb[1] + 0.12 * fh, fb[2] - 0.05, fb[3] + 0.05))
            for i in {scene_at(s + 0.01), scene_at(max(s, e - 0.01))}:
                for y0, y1 in clips[i].get("keep_clear", []):
                    blocks.append((y0, y1, 0.0, 1.0))
            for (ps, pe, py0, py1) in placed_boxes:
                if ps < e and s < pe:
                    blocks.append((py0 - 0.006, py1 + 0.006, 0.0, 1.0))
            x0f, x1f, hf = (W - cw) / 2 / W, (W + cw) / 2 / W, ch / H
            lo, hi = SAFE_TOP + 0.02 + hf / 2, SAFE_BOT - 0.03 - hf / 2   # inside the 4:5 area, clear of UI
            cands = sorted({round(want + d * sg, 3) for d in [k * 0.01 for k in range(60)] for sg in (1, -1)},
                           key=lambda yc: abs(yc - want))
            for yc in cands:
                if lo <= yc <= hi and all(not (yc - hf / 2 < b1 and b0 < yc + hf / 2 and x0f < bx1 and bx0 < x1f)
                                          for b0, b1, bx0, bx1 in blocks):
                    return yc
            return None

        # a caption with no clear y across all its scenes is split per scene (it moves at the cuts)
        segments = []
        for j, cap in enumerate(caps_all):
            s, e = resolve(cap)
            png = tmp / f"cap_{j:02d}.png"
            ch, cw = render_caption(cap, png)
            yc = find_y(cap, s, e, ch, cw)
            if yc is not None:
                segments.append((cap, png, ch, s, e, yc))
                placed_boxes.append((s, e, yc - ch / H / 2, yc + ch / H / 2))
                continue
            cuts = sorted({s, e, *[a for a, _ in win if s < a < e]})
            print(f"   caption {j} '{cap['text'][:28]}': no single clear y, placed per scene")
            for s1, e1 in zip(cuts, cuts[1:]):
                y1 = find_y(cap, s1, e1, ch, cw)
                if y1 is None:
                    y1 = min(max(float(cap.get("y", 0.3)), SAFE_TOP + 0.02 + ch / H / 2), SAFE_BOT - 0.03 - ch / H / 2)
                    print(f"     WARNING {s1:.1f}-{e1:.1f}s: still overlaps a face; move or shorten it")
                segments.append((cap, png, ch, s1, e1, y1))
                placed_boxes.append((s1, e1, y1 - ch / H / 2, y1 + ch / H / 2))

        for j, (cap, png, ch, s, e, yc) in enumerate(segments):
            if abs(yc - float(cap.get("y", 0.3))) > 0.005:
                print(f"   caption '{cap['text'][:28]}' {s:.1f}-{e:.1f}s: y {float(cap.get('y', 0.3)):.2f} -> {yc:.2f}")
            y = int(H * yc - ch / 2)
            k = n + j
            inputs += ["-loop", "1", "-framerate", str(FPS), "-t", f"{total:.3f}", "-i", str(png)]
            fade = float(cap.get("fade", 0.12))
            fx = ["format=rgba"]
            if fade and s > 0.01:
                fx.append(f"fade=t=in:st={s:.3f}:d={fade}:alpha=1")
            if fade and e < total - 0.01:
                fx.append(f"fade=t=out:st={e - fade:.3f}:d={fade}:alpha=1")
            g.append(f"[{k}:v]{','.join(fx)}[cp{j}]")
            g.append(f"[{vl}][cp{j}]overlay=0:{y}:eof_action=pass:enable='between(t,{s:.3f},{e:.3f})'[vc{j}]")
            vl = f"vc{j}"

        next_in = n + len(segments)
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
        if not feed:
            (out_dir / f"{vid}_4x5.mp4").unlink(missing_ok=True)
        if feed:
            f45 = out_dir / f"{vid}_4x5.mp4"
            run(["ffmpeg", "-v", "error", "-y", "-i", str(final), "-vf", f"crop={W}:{FEED_H}:0:{(H - FEED_H) // 2}",
                 "-c:v", "libx264", "-preset", "slow", "-crf", "17", "-pix_fmt", "yuv420p", "-g", str(FPS * 2),
                 "-movflags", "+faststart", "-c:a", "copy", str(f45)])
            outs.append(f45)
        outs.append(sheet(final, out_dir / f"{vid}_sheet.jpg", every=sheet_every))
        print(f"{vid}: {total:.2f}s, {n_content} clips" + (f" + end card '{card['name']}'" if card else "")
              + f", {len(caps_all)} captions")
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
    ap.add_argument("--with-4x5", action="store_true", help="also write a 4:5 crop (off by default)")
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
        build(a.edit, a.sheet_every, feed=a.with_4x5)
    else:
        ap.print_help()


if __name__ == "__main__":
    main()
