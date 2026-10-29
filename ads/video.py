"""Build a narrated, illustrated video ad from a scenes.json (storybook / explainer format).

Pipeline (each step is cached, so reruns only redo what's missing or forced):
    images   Kie nano-banana-pro, one 4:5 illustration per scene, with the character sheet
             and/or the product photo as references
    anim     optional Kie image-to-video for scenes that define "anim" (replaces Ken Burns)
    voice    OpenAI TTS per scene (Kie's ElevenLabs endpoint was failing on 2026-10-29)
    music    optional Kie Suno instrumental bed, ducked under the voice
    render   Ken Burns per scene, chapter cards, word-timed captions (Whisper),
             4:5 master (1080x1350) + 9:16 (1080x1920, cream pads + headline)

Usage:
    python ads/video.py ads/brands/comfortwear/video/V01_50_year_history all
    python ads/video.py <dir> images --only s07 s08 --force
    python ads/video.py <dir> voice
    python ads/video.py <dir> render
"""

import argparse
import concurrent.futures as cf
import difflib
import json
import os
import subprocess
import sys
from pathlib import Path

import requests
from dotenv import load_dotenv
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, str(Path(__file__).resolve().parent))
import kie  # noqa: E402

load_dotenv(Path(__file__).resolve().parent.parent / ".env")
W, H = 1080, 1350            # 4:5 master
TALL = 1920                  # 9:16 height
FPS = 30
GAP = 0.25                   # silence after each scene's line
CREAM = (246, 239, 226)
FONTS = Path(__file__).resolve().parent / "fonts"


def sh(cmd):
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)


def duration(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0",
                          str(path)], capture_output=True, text=True, check=True).stdout
    return float(out.strip())


# ---------- images ----------

def scene_prompt(spec, scene):
    chars = spec["characters"]
    who = " ".join(chars[r] for r in scene.get("refs", []) if r != "shoe")
    shoe = chars["shoe"] if "shoe" in scene.get("refs", []) else ""
    refs = ""
    if any(r != "shoe" for r in scene.get("refs", [])):
        refs += "Draw the named characters exactly as they look in the attached character sheet (same faces, hair, clothes, proportions). "
    if shoe:
        refs += "Any Comfort Wear shoe in the scene must match the attached product photo. "
    return f"{scene['prompt']} {who} {shoe} {refs}{spec['style']}".strip()


def ref_urls(d, spec, scene, cache):
    urls = []
    refs = scene.get("refs", [])
    if any(r != "shoe" for r in refs):
        urls.append(cache.setdefault("characters", kie.upload(d / "refs/characters.jpg", "cw-video")))
    if "shoe" in refs:
        shoe = Path(__file__).resolve().parent / "brands" / spec.get("brand", "comfortwear") / spec["product_ref"]
        urls.append(cache.setdefault("shoe", kie.upload(shoe, "cw-video")))
    return urls


def make_image(d, spec, scene, cache, force):
    out = d / "img" / f"{scene['id']}.png"
    if out.exists() and not force:
        return out
    inp = {"prompt": scene_prompt(spec, scene), "aspect_ratio": "4:5", "resolution": "2K", "output_format": "png"}
    urls = ref_urls(d, spec, scene, cache)
    if urls:
        inp["image_input"] = urls
    for attempt in range(3):
        try:
            return kie.download(kie.run("nano-banana-pro", inp)[0], out)
        except Exception as e:  # transient Kie failures are common; retry
            print(f"  {scene['id']} attempt {attempt + 1}: {e}")
    raise RuntimeError(scene["id"])


def step_images(d, spec, ids, force):
    cache = {}
    ref_urls(d, spec, {"refs": ["grandma", "shoe"]}, cache)   # upload refs once, before threads
    todo = [s for s in spec["scenes"] if s.get("kind") != "card" and (not ids or s["id"] in ids)]
    with cf.ThreadPoolExecutor(8) as ex:
        for s, f in zip(todo, ex.map(lambda s: make_image(d, spec, s, cache, force), todo)):
            print("image", s["id"], f)


# ---------- animation (optional) ----------

def step_anim(d, spec, ids, force):
    todo = [s for s in spec["scenes"] if s.get("anim") and (not ids or s["id"] in ids)]

    def one(s):
        out = d / "anim" / f"{s['id']}.mp4"
        if out.exists() and not force:
            return out
        url = kie.upload(d / "img" / f"{s['id']}.png", "cw-video")
        model = spec.get("anim_model", "kling/v3-turbo-image-to-video")
        secs = max(3, min(15, round(duration(d / "vo" / f"{s['id']}.wav") + GAP + 0.5)))
        prompt = s["anim"] + " Keep the hand-drawn colored-pencil storybook style, gentle subtle motion, no camera cuts, no text."
        return kie.download(kie.run(model, {"prompt": prompt, "image_urls": [url], "duration": str(secs),
                                            "resolution": "1080p"})[0], out)

    with cf.ThreadPoolExecutor(6) as ex:
        for s, f in zip(todo, ex.map(one, todo)):
            print("anim", s["id"], f)


# ---------- voice ----------

def trim_silence(src, out):
    """Cut the dead air TTS leaves before and after a line, keeping a 60 ms tail."""
    trim = "silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.03"
    sh(["ffmpeg", "-y", "-i", str(src), "-af", f"{trim},areverse,{trim},apad=pad_dur=0.06,areverse",
        "-ar", "48000", "-ac", "1", str(out)])


def step_voice(d, spec, ids, force):
    v = spec["voice"]
    key = os.environ["OPENAI_API_KEY"]

    def one(s):
        out = d / "vo" / f"{s['id']}.mp3"
        if out.exists() and not force:
            if not out.with_suffix(".wav").exists():
                trim_silence(out, out.with_suffix(".wav"))
            return out
        out.parent.mkdir(parents=True, exist_ok=True)
        r = requests.post("https://api.openai.com/v1/audio/speech", timeout=300,
                          headers={"Authorization": f"Bearer {key}"},
                          json={"model": v["model"], "voice": v["voice"], "input": s["vo"],
                                "instructions": v["instructions"], "speed": v.get("speed", 1.0),
                                "response_format": "mp3"})
        r.raise_for_status()
        out.write_bytes(r.content)
        trim_silence(out, out.with_suffix(".wav"))
        return out

    todo = [s for s in spec["scenes"] if not ids or s["id"] in ids]
    with cf.ThreadPoolExecutor(8) as ex:
        list(ex.map(one, todo))
    words = d / "vo" / "words.json"
    timing = json.loads(words.read_text()) if words.exists() else {}
    for s in todo:
        if s["id"] in timing and not force:
            continue
        with open(d / "vo" / f"{s['id']}.wav", "rb") as f:
            r = requests.post("https://api.openai.com/v1/audio/transcriptions", timeout=300,
                              headers={"Authorization": f"Bearer {key}"}, files={"file": f},
                              data={"model": "whisper-1", "response_format": "verbose_json",
                                    "timestamp_granularities[]": "word", "prompt": s["vo"]})
        r.raise_for_status()
        timing[s["id"]] = [(w["word"], w["start"], w["end"]) for w in r.json().get("words", [])]
    words.write_text(json.dumps(timing))
    print("voice", sum(duration(d / "vo" / f"{s['id']}.wav") + GAP for s in spec["scenes"]), "s total")


# ---------- music (optional) ----------

def step_music(d, spec, force):
    out = d / "music.mp3"
    m = spec.get("music")
    if not m or (out.exists() and not force):
        return
    task = kie.create("ai-music-api/generate", {
        "custom_mode": True, "instrumental": True, "model": m.get("model", "V6"), "title": spec["id"][:80],
        "style": m["style"], "prompt": m["prompt"]})
    import time
    for _ in range(120):
        data = requests.get(f"{kie.API}/jobs/recordInfo", headers=kie._headers(), timeout=60,
                            params={"taskId": task}).json().get("data") or {}
        if data.get("state") == "fail":
            raise RuntimeError(data)
        blob = json.dumps(data)
        if data.get("state") == "success":
            res = json.loads(data.get("resultJson") or "{}")
            urls = res.get("resultUrls") or [t.get("audio_url") for t in (data.get("response") or {}).get("data", [])]
            urls = [u for u in urls if u] or [w.strip('"') for w in blob.split() if ".mp3" in w]
            kie.download(urls[0], out)
            print("music", out)
            return
        time.sleep(10)


# ---------- render ----------

def font(name, size):
    return ImageFont.truetype(str(FONTS / name), size)


def card_image(d, s, out):
    """Hand-lettered chapter card: a paper card with a pencil border and soft shadow on cream paper."""
    from PIL import ImageFilter
    import random
    rnd = random.Random(7)
    bg = Image.new("RGB", (W, H), CREAM)
    dr = ImageDraw.Draw(bg)
    for _ in range(140):  # faint diagonal pencil hatching, like the paper in the art
        x, y = rnd.randrange(-200, W), rnd.randrange(0, H)
        dr.line((x, y, x + 90, y - 60), fill=(236, 228, 214), width=1)
    box = (int(W * 0.14), int(H * 0.36), int(W * 0.86), int(H * 0.61))
    shadow = Image.new("L", (W, H), 0)
    ImageDraw.Draw(shadow).rounded_rectangle([box[0] + 10, box[1] + 14, box[2] + 10, box[3] + 14], 28, fill=90)
    bg.paste((200, 188, 170), (0, 0, W, H), shadow.filter(ImageFilter.GaussianBlur(14)))
    dr.rounded_rectangle(box, 28, fill=(250, 245, 236), outline=(92, 82, 72), width=3)
    ink = (60, 52, 46)
    for text, f, y in ((s["title"], font("patrick-hand-latin-400-normal.ttf", 96), H * 0.44),
                       (s["subtitle"], font("patrick-hand-latin-400-normal.ttf", 64), H * 0.53)):
        size = f.size
        while dr.textlength(text, font=f) > W * 0.62 and size > 30:
            size -= 2
            f = font("patrick-hand-latin-400-normal.ttf", size)
        dr.text((W / 2, y), text, font=f, fill=ink, anchor="mm")
    bg.save(out)


MOVES = {  # (zoom start, zoom end, x drift, y drift) as fractions of the spare margin
    "in": (1.0, 1.10, 0, 0), "out": (1.10, 1.0, 0, 0), "left": (1.08, 1.08, 1, 0),
    "right": (1.08, 1.08, -1, 0), "up": (1.08, 1.08, 0, 1), "down": (1.08, 1.08, 0, -1), "none": (1, 1, 0, 0)}


def ken_burns(img, secs, move, out):
    z0, z1, dx, dy = MOVES.get(move, MOVES["in"])
    n = max(1, round(secs * FPS))
    zexpr = f"{z0}+({z1}-{z0})*on/{n}"
    # x/y: centered, plus a drift across the spare margin left by the zoom
    xexpr = f"(iw-iw/zoom)/2+{dx}*(iw-iw/zoom)/2*(2*on/{n}-1)"
    yexpr = f"(ih-ih/zoom)/2+{dy}*(ih-ih/zoom)/2*(2*on/{n}-1)"
    sh(["ffmpeg", "-y", "-loop", "1", "-i", str(img), "-frames:v", str(n), "-vf",
        f"scale={W * 2}:{H * 2}:flags=lanczos,zoompan=z='{zexpr}':x='{xexpr}':y='{yexpr}':d=1:s={W}x{H}:fps={FPS},"
        "format=yuv420p", "-c:v", "libx264", "-preset", "medium", "-crf", "18", str(out)])


def fit_clip(src, secs, out):
    """Scale/crop an animated clip to the 4:5 master and hold its last frame if it runs short."""
    sh(["ffmpeg", "-y", "-i", str(src), "-an", "-vf",
        f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS},"
        f"tpad=stop_mode=clone:stop_duration={secs},format=yuv420p",
        "-t", f"{secs:.3f}", "-c:v", "libx264", "-preset", "medium", "-crf", "18", str(out)])


NUMERALS = [  # spoken form (as the script is written for TTS) -> caption form
    ("fifty nine ninety five", "$59.95"), ("from ninety", "from $90"),
    ("a hundred and seventy dollars", "$170"), ("hundred and seventy dollar", "$170"),
    ("three hundred dollars", "$300"), ("three hundred dollar", "$300"), ("four hundred dollars", "$400"),
    ("three hundred", "$300"), ("two million", "2 million"), ("fifty year", "50-year"), ("fifty years", "50 years"),
    ("thirty minute", "30-minute"), ("twelve hour", "12-hour"), ("hour twelve", "hour 12"), ("hour one", "hour 1"),
    ("hour four", "hour 4"), ("eight", "8"), ("ten", "10"), ("twelve hours", "12 hours"),
    ("nineteen seventies", "1970s"), ("eighties", "'80s"), ("nineties", "'90s"), ("two thousand two", "2002"),
    ("twenty tens", "2010s")]


def _norm(w):
    return w.lower().strip(".,?!:;\"'")


def caption_words(text, words):
    """Script words (with their casing and punctuation) on Whisper's timings, numbers as numerals.

    Whisper drops punctuation and capitalizes oddly ("HOKAS"), so when its word count matches the
    script's, the script's own words are used; otherwise Whisper's words are kept as they are.
    """
    script = text.replace("-", " ").split()
    if words:
        # align script words to Whisper's; script words Whisper missed get times from their neighbours
        sm = difflib.SequenceMatcher(None, [_norm(w) for w in script], [_norm(w[0]) for w in words], autojunk=False)
        times = [None] * len(script)
        for a, b, n in sm.get_matching_blocks():
            for k in range(n):
                times[a + k] = words[b + k][1:]
        for k, tm in enumerate(times):
            if tm is None:
                prev = next((times[j] for j in range(k - 1, -1, -1) if times[j]), (0.0, 0.0))
                nxt = next((times[j] for j in range(k + 1, len(times)) if times[j]), (prev[1], prev[1]))
                times[k] = (prev[1], nxt[0])
        words = [(sw, s, e) for sw, (s, e) in zip(script, times)]
    out, i = [], 0
    while i < len(words):
        for spoken, written in NUMERALS:
            n = len(spoken.split())
            if " ".join(_norm(w[0]) for w in words[i:i + n]) == spoken:
                last = words[i + n - 1][0]
                tail = last[len(last.rstrip(".,?!:;")):]
                first = words[i][0]
                out.append(((written[0].upper() + written[1:] if first[:1].isupper() else written) + tail,
                            words[i][1], words[i + n - 1][2]))
                i += n
                break
        else:
            out.append(words[i])
            i += 1
    return out


def caption_chunks(words, offset, max_words=5, max_chars=26):
    chunks, cur = [], []
    for w, s, e in words:
        cur.append((w.strip(), s, e))
        text = " ".join(x[0] for x in cur)
        end = w.strip()[-1:]
        if len(cur) >= max_words or len(text) >= max_chars or end in ".?!:" or (end == "," and len(cur) >= 3):
            chunks.append((text, cur[0][1] + offset, cur[-1][2] + offset))
            cur = []
    if cur:
        chunks.append((" ".join(x[0] for x in cur), cur[0][1] + offset, cur[-1][2] + offset))
    # each caption stays up until the next one starts
    return [(t, s, chunks[i + 1][1] if i + 1 < len(chunks) else e + 0.3) for i, (t, s, e) in enumerate(chunks)]


def overlay_png(text, path, size=52, width=W):
    f = font("poppins-latin-700-normal.ttf", size)
    img = Image.new("RGBA", (width, size * 3), (0, 0, 0, 0))
    dr = ImageDraw.Draw(img)
    dr.text((width / 2, size * 1.5), text, font=f, fill="white", anchor="mm", stroke_width=max(4, size // 9),
            stroke_fill="black")
    img.save(path)


def step_render(d, spec):
    tmp = d / "build"
    tmp.mkdir(exist_ok=True)
    timing = json.loads((d / "vo/words.json").read_text())
    clips, captions, t = [], [], 0.0
    for s in spec["scenes"]:
        secs = duration(d / "vo" / f"{s['id']}.wav") + GAP
        clip = tmp / f"{s['id']}.mp4"
        src = d / "anim" / f"{s['id']}.mp4"
        src = src if src.exists() else d / "img" / f"{s['id']}.png"
        fresh = clip.exists() and abs(duration(clip) - secs) < 0.05 and (
            s.get("kind") == "card" or clip.stat().st_mtime > src.stat().st_mtime)
        if fresh:
            pass  # unchanged since the last render
        elif s.get("kind") == "card":
            card_image(d, s, tmp / f"{s['id']}.png")
            ken_burns(tmp / f"{s['id']}.png", secs, "none", clip)
        elif (d / "anim" / f"{s['id']}.mp4").exists():
            fit_clip(d / "anim" / f"{s['id']}.mp4", secs, clip)
        else:
            ken_burns(d / "img" / f"{s['id']}.png", secs, s.get("move", "in"), clip)
        clips.append(clip)
        if s.get("kind") != "card":
            captions += caption_chunks(caption_words(s["vo"], timing.get(s["id"], [])), t)
        if s.get("overlay"):
            captions.append(("@" + s["overlay"], t + 0.2, t + secs))
        t += secs
        print("clip", s["id"], f"{secs:.2f}s")

    (tmp / "list.txt").write_text("".join(f"file '{c.name}'\n" for c in clips))
    (tmp / "vo_list.txt").write_text("".join(
        f"file '{(d / 'vo' / (s['id'] + '.wav')).resolve()}'\nfile '{(tmp / 'gap.wav').resolve()}'\n"
        for s in spec["scenes"]))
    sh(["ffmpeg", "-y", "-f", "lavfi", "-i", "anullsrc=r=24000:cl=mono", "-t", str(GAP), str(tmp / "gap.wav")])
    sh(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(tmp / "list.txt"), "-c", "copy", str(tmp / "picture.mp4")])
    sh(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(tmp / "vo_list.txt"), "-ar", "48000", "-ac", "2",
        str(tmp / "voice.wav")])

    audio = tmp / "voice.wav"
    if (d / "music.mp3").exists():
        mixed = tmp / "mix.wav"
        vol = spec.get("music", {}).get("volume", 0.12)
        sh(["ffmpeg", "-y", "-i", str(audio), "-stream_loop", "-1", "-i", str(d / "music.mp3"), "-filter_complex",
            f"[1:a]volume={vol},afade=t=out:st={t - 2.5}:d=2.5[m];[0:a][m]amix=inputs=2:duration=first:normalize=0,"
            "loudnorm=I=-16:TP=-1.5:LRA=11[a]", "-map", "[a]", "-t", f"{t:.3f}", str(mixed)])
        audio = mixed

    # caption PNGs, overlaid with enable windows
    cap_dir = tmp / "caps"
    cap_dir.mkdir(exist_ok=True)
    for name, (pw, ph, pad_top) in {"4x5": (W, H, 0), "9x16": (W, TALL, (TALL - H) // 2)}.items():
        inputs, chain, last = ["-i", str(tmp / "picture.mp4")], [], "0:v"
        if pad_top:
            head = cap_dir / "headline.png"
            hl = Image.new("RGBA", (W, pad_top), (0, 0, 0, 0))
            dr = ImageDraw.Draw(hl)
            hf = font("poppins-latin-800-normal.ttf", 54)
            lines = spec.get("headline_lines", [spec["title"]])
            for i, line in enumerate(lines):
                dr.text((W / 2, pad_top * 0.62 + (i - (len(lines) - 1) / 2) * 66), line, font=hf, fill=(122, 47, 224),
                        anchor="mm")
            hl.save(head)
            chain.append(f"[0:v]pad={W}:{TALL}:0:{pad_top}:color=0x{''.join(f'{c:02x}' for c in CREAM)}[p0]")
            inputs += ["-i", str(head)]
            chain.append("[p0][1:v]overlay=0:0[p1]")
            last = "p1"
        for i, (text, a, b) in enumerate(captions):
            big = text.startswith("@")
            png = cap_dir / f"{name}_{i}.png"
            overlay_png(text.lstrip("@"), png, size=64 if big else 50)
            inputs += ["-i", str(png)]
            y = pad_top + (H * 0.16 if big else H * 0.70)
            idx = len(inputs) // 2 - 1
            chain.append(f"[{last}][{idx}:v]overlay=0:{int(y)}:enable='between(t,{a:.3f},{b:.3f})'[c{i}]")
            last = f"c{i}"
        script = tmp / f"filter_{name}.txt"
        script.write_text(";\n".join(chain))
        out = d / f"{spec['id']}_{name}.mp4"
        sh(["ffmpeg", "-y", *inputs, "-i", str(audio), "-filter_complex_script", str(script), "-map", f"[{last}]",
            "-map", f"{len(inputs) // 2}:a", "-c:v", "libx264", "-preset", "slow", "-crf", "23", "-pix_fmt",
            "yuv420p", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", "-shortest", str(out)])
        print("wrote", out, f"{duration(out):.1f}s")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dir")
    ap.add_argument("step", choices=["images", "anim", "voice", "music", "render", "all"])
    ap.add_argument("--only", nargs="*")
    ap.add_argument("--force", action="store_true")
    a = ap.parse_args()
    d = Path(a.dir).resolve()
    spec = json.loads((d / "scenes.json").read_text())
    if a.step in ("images", "all"):
        step_images(d, spec, a.only, a.force)
    if a.step in ("voice", "all"):
        step_voice(d, spec, a.only, a.force)
    if a.step in ("anim", "all"):
        step_anim(d, spec, a.only, a.force)
    if a.step in ("music", "all"):
        step_music(d, spec, a.force)
    if a.step in ("render", "all"):
        step_render(d, spec)


if __name__ == "__main__":
    main()
