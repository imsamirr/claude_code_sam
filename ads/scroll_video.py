"""Scrolling long-form video ads: a looping background, a long story scrolling up from the bottom in big
bold outlined text, and a voice-over that reads it (synced section by section), with a soft music bed.

Format studied from Atria long-runners (a vet's "40 senior cats", FluffCo's hotel pillow, a physical
therapist on sciatica): 720x1280, 4-5 minutes, centered white/yellow text with a heavy black outline, the
hook on screen at second 0 in the lower half, short paragraphs.

    python ads/scroll_video.py --brand comfortwear --spec <variations.json> [IDs]   # full pipeline
    python ads/scroll_video.py --brand comfortwear --spec x.json LV01 --only render  # reuse assets

Spec (list): {"id","script","voice","background" (Veo prompt) or "background_image" (still photo prompt, slow zoom),
"caption","headline", optional "audio" ("voice" default, or "music" = no voice-over, fixed reading pace),
"text_color", "music_prompt"}. Without --music, one Suno bed per spec file is made next to it (<stem>_music.mp3).
Assets land in ads/brands/<brand>/output/scroll_videos/<ID>/ and the final video in .../<ID>.mp4.
Kie.ai (KIE_AI): veo3_fast for 3 background clips per video, Suno V4_5 for the music bed,
Voice: ElevenLabs direct (env ElevenLabKey / ELEVENLABS_API_KEY, eleven_multilingual_v2) first when the key is set,
then ElevenLabs via Kie, then OpenAI gpt-4o-mini-tts (OPENAI_API_KEY). Optional spec "el_voice_id" picks the voice.
"""

import argparse
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

import requests
from PIL import Image, ImageDraw, ImageFont

ADS = Path(__file__).resolve().parent
FONT = ADS / "assets" / "fonts" / "Montserrat.ttf"
KIE = "https://api.kie.ai/api/v1"
W, H, FPS = 1080, 1920, 60   # full-HD vertical; 60fps so the text can move exactly 1px per frame
START_Y = 0.60      # the hook's top sits here at t=0 (fraction of H), like the examples
READ_Y = 0.30       # a paragraph's top sits here when the voice starts reading it
MUSIC_DB = -24      # music bed under the voice
MUSIC_ONLY_DB = -6  # music bed when there is no voice ("audio": "music")
MUSIC_WPS = 2.5     # reading pace (words per second) for music-only videos
EASE_S = 6.0        # music-only: the text rises at a third of its speed for the first 6 seconds
PX_PER_FRAME = 1    # music-only: steady scroll of exactly 1px per frame (60px/s): no stutter from fractional motion
EASE_EVERY = 3      # during the ease-in the text moves 1px every 3 frames (20px/s)
DEFAULT_MUSIC = ("soft, slow, emotional solo piano with a light ambient pad, intimate and reflective, "
                 "no drums, no vocals, understated, steady from start to end")
TTS = "kie"         # "kie" (ElevenLabs via Kie, falls back to OpenAI) or "openai"
CLIP_ANGLES = ["", ""]  # two takes of the SAME prompt = two moments of one place, crossfaded and looped


def kie_headers():
    return {"Authorization": f"Bearer {os.environ['KIE_AI']}", "Content-Type": "application/json"}


def get(url, dest):
    dest.write_bytes(requests.get(url, timeout=300).content)
    return dest


# ---------- background (Veo via Kie) ----------
def veo_clip(prompt, dest):
    style = (" Raw handheld footage filmed by a regular person, full frame, vertical 9:16, natural light, realistic, slight "
             "handheld sway. The camera itself is never visible: no phone on screen, no screen-within-a-screen, no UI. People "
             "are seen from behind or busy, nobody talks to the camera. No text, no captions, no logos, no brand names, no "
             "recognizable landmarks or characters.")
    r = requests.post(f"{KIE}/veo/generate", headers=kie_headers(), timeout=60, json={
        "prompt": prompt + style, "model": "veo3_fast", "aspectRatio": "9:16", "enableTranslation": False}).json()
    if r.get("code") != 200:
        raise RuntimeError(f"veo: {r}")
    tid = r["data"]["taskId"]
    for _ in range(120):
        time.sleep(10)
        d = requests.get(f"{KIE}/veo/record-info", headers=kie_headers(), params={"taskId": tid}, timeout=60).json()["data"]
        if d.get("successFlag") == 1:
            return get(d["response"]["resultUrls"][0], dest)
        if d.get("successFlag") in (2, 3):
            raise RuntimeError(f"veo failed: {d.get('errorMessage')}")
    raise RuntimeError("veo timeout")


# ---------- still-image background (Kie nano-banana-pro) with a slow zoom ----------
IMG_STYLE = ("A real, unedited vertical photo straight from a regular person's phone camera roll, edge to edge: no borders, "
             "captions, text, logos, brand names or interface. Native phone-camera look, everything sharp front to back, a bit "
             "of noise in the shadows, slightly crooked framing. The story's key object is large, sharp and clearly visible in the "
             "UPPER HALF of the frame; the lower half is darker and simpler (a counter, a floor, a tabletop in shadow) because big "
             "white text scrolls over it. Low-key, moody, realistic light; gross details stay realistic, never cartoonish. ")


def still_image(prompt, dest):
    r = requests.post(f"{KIE}/jobs/createTask", headers=kie_headers(), timeout=60, json={
        "model": "nano-banana-pro", "input": {"prompt": IMG_STYLE + prompt, "aspect_ratio": "9:16", "resolution": "2K"}}).json()
    if r.get("code") != 200:
        raise RuntimeError(f"image: {r}")
    tid = r["data"]["taskId"]
    for _ in range(80):
        time.sleep(5)
        d = requests.get(f"{KIE}/jobs/recordInfo", headers=kie_headers(), params={"taskId": tid}, timeout=60).json()["data"]
        if d["state"] == "success":
            return get(json.loads(d["resultJson"])["resultUrls"][0], dest)
        if d["state"] == "fail":
            raise RuntimeError(d.get("failMsg"))
    raise RuntimeError("image timeout")


def still_loop(img, total, dest):
    """A slow, gentle zoom (1.00 -> 1.12 and back) over the whole video, rendered at 2x then scaled down to avoid jitter."""
    frames = int(total * FPS) + FPS
    z = "1.06-0.06*cos(2*PI*on/{p})".format(p=max(int(70 * FPS), 1))
    vf = (f"scale={W * 2}:{H * 2}:force_original_aspect_ratio=increase,crop={W * 2}:{H * 2},"
          f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={frames}:s={W * 2}x{H * 2}:fps={FPS},"
          f"scale={W}:{H}")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(img), "-vf", vf, "-frames:v", str(frames),
                    "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p", str(dest)], check=True)
    return dest


# ---------- music (Suno via Kie) ----------
def suno(prompt, dest):
    r = requests.post(f"{KIE}/generate", headers=kie_headers(), timeout=60, json={
        "prompt": prompt, "customMode": False, "instrumental": True, "model": "V4_5",
        "callBackUrl": "https://example.com/noop"}).json()
    tid = r["data"]["taskId"]
    for _ in range(90):
        time.sleep(10)
        d = requests.get(f"{KIE}/generate/record-info", headers=kie_headers(), params={"taskId": tid}, timeout=60).json()["data"]
        if d.get("status") == "SUCCESS":
            x = d["response"]["sunoData"][0]
            return get(x.get("audioUrl") or x.get("sourceAudioUrl"), dest)
        if d.get("status") and "FAIL" in d["status"]:
            raise RuntimeError(f"suno failed: {d}")
    raise RuntimeError("suno timeout")


# ---------- voice ----------
KIE_VOICES = {"female": "Rachel", "male": "Brian"}
OPENAI_VOICES = {"female": "sage", "male": "ash"}


def tts_kie(text, gender, dest, wait=240, voice=None):
    r = requests.post(f"{KIE}/jobs/createTask", headers=kie_headers(), timeout=60, json={
        "model": "elevenlabs/text-to-speech-turbo-2-5",
        "input": {"text": text, "voice": voice or KIE_VOICES[gender], "stability": 0.45, "similarity_boost": 0.75}}).json()
    if r.get("code") != 200:
        raise RuntimeError(r)
    tid = r["data"]["taskId"]
    t0 = time.time()
    while time.time() - t0 < wait:
        time.sleep(6)
        d = requests.get(f"{KIE}/jobs/recordInfo", headers=kie_headers(), params={"taskId": tid}, timeout=60).json()["data"]
        if d["state"] == "success":
            return get(json.loads(d["resultJson"])["resultUrls"][0], dest)
        if d["state"] == "fail":
            raise RuntimeError(d.get("failMsg"))
    raise RuntimeError("kie tts timeout")


EL_VOICES = {"female": "21m00Tcm4TlvDq8EpW7j", "male": "nPczCjzI2devNBz1zQrb"}  # ElevenLabs "Rachel" / "Brian"


EL_MODEL = "eleven_turbo_v2_5"   # 0.5 credit per character (multilingual_v2 costs 1 per character)
EL_RATE = {"eleven_turbo_v2_5": 0.5, "eleven_flash_v2_5": 0.5, "eleven_multilingual_v2": 1.0}
VOICE_BUDGET = 5000              # max ElevenLabs credits per day (one routine run); user rule 2026-11-12


def el_credits(text):
    return int(len(text) * EL_RATE.get(EL_MODEL, 1.0)) + 1


def budget_claim(out_root, credits):
    """Reserve ElevenLabs credits in a per-day ledger shared by parallel processes. False if it would exceed the budget."""
    import fcntl, datetime
    ledger = out_root / "elevenlabs_credit_ledger.json"
    ledger.touch(exist_ok=True)
    with open(ledger, "r+") as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        data = json.loads(f.read() or "{}")
        day = datetime.date.today().isoformat()
        used = data.get(day, 0)
        if used + credits > VOICE_BUDGET:
            return False, used
        data[day] = used + credits
        f.seek(0); f.truncate(); f.write(json.dumps(data, indent=1))
        return True, used + credits


def eleven_key():
    return os.getenv("ElevenLabKey") or os.getenv("ELEVENLABS_API_KEY")


def tts_eleven(text, gender, dest, voice_id=None):
    """ElevenLabs direct API (key in env ElevenLabKey or ELEVENLABS_API_KEY)."""
    vid = voice_id or EL_VOICES[gender]
    for attempt in range(5):
        r = requests.post(f"https://api.elevenlabs.io/v1/text-to-speech/{vid}?output_format=mp3_44100_128", timeout=300,
                          headers={"xi-api-key": eleven_key(), "Content-Type": "application/json"},
                          json={"text": text, "model_id": EL_MODEL,
                                "voice_settings": {"stability": 0.45, "similarity_boost": 0.75, "style": 0.15}})
        if r.status_code not in (429, 500, 502, 503):
            break
        time.sleep(min(60, 5 * 2 ** attempt))
    r.raise_for_status()
    dest.write_bytes(r.content)
    return dest


def tts_openai(text, gender, notes, dest):
    for attempt in range(8):
        r = _openai_tts_once(text, gender, notes)
        if r.status_code not in (429, 500, 502, 503):
            break
        time.sleep(min(90, 5 * 2 ** attempt))
    r.raise_for_status()
    dest.write_bytes(r.content)
    return dest


def _openai_tts_once(text, gender, notes):
    return requests.post("https://api.openai.com/v1/audio/speech", timeout=300,
                      headers={"Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}"},
                      json={"model": "gpt-4o-mini-tts", "voice": OPENAI_VOICES[gender], "input": text,
                            "response_format": "mp3",
                            "instructions": (f"Voice: {notes}. Read like a real woman telling her own story to a friend: "
                                             "natural, warm, unhurried, conversational, with small pauses between "
                                             "paragraphs. Not an announcer, not salesy.")})


def duration(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)],
                         capture_output=True, text=True).stdout.strip()
    return float(out)


# ---------- text ----------
def paragraphs(script):
    return [re.sub(r"\s+", " ", p).strip() for p in re.split(r"\n\s*\n", script.strip()) if p.strip()]


def layout(paras, color):
    font = ImageFont.truetype(str(FONT), round(46 * W / 720))
    font.set_variation_by_name("ExtraBold")
    k = W / 720
    maxw, lh, gap, stroke = int(W * 0.86), round(56 * k), round(34 * k), round(5 * k)
    probe = ImageDraw.Draw(Image.new("RGBA", (1, 1)))
    blocks = []
    for p in paras:
        lines, cur = [], ""
        for w in p.split():
            t = (cur + " " + w).strip()
            if probe.textlength(t, font=font) > maxw and cur:
                lines.append(cur); cur = w
            else:
                cur = t
        lines.append(cur)
        blocks.append(lines)
    total = sum(len(b) * lh for b in blocks) + gap * (len(blocks) - 1) + round(40 * k)
    img = Image.new("RGBA", (W, total), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    tops, y = [], 10
    for lines in blocks:
        tops.append(y)
        for ln in lines:
            x = (W - d.textlength(ln, font=font)) / 2
            d.text((round(x), y), ln, font=font, fill=color, stroke_width=stroke, stroke_fill=(0, 0, 0))
            y += lh
        y += gap
    return img, tops, total


def chunks(paras, max_words=110):
    groups, cur, n = [], [], 0
    for i, p in enumerate(paras):
        cur.append(i); n += len(p.split())
        if n >= max_words:
            groups.append(cur); cur, n = [], 0
    if cur:
        groups.append(cur)
    return groups


def scroll_expr(tops, starts, total_dur, text_h, constant=False):
    """y(t) for the text layer. The text rises slowly from the first frame, like the reference ads.

    constant=True (music-only): one steady speed from the hook's start position to the CTA resting mid-screen.
    Otherwise (voice): piecewise-linear so paragraph i reaches READ_Y*H when its voice starts, except that
    anchors are skipped until the steady speed itself brings the text to the reading line (no fast jump at the start).
    """
    y0, end_y = START_Y * H - tops[0], H * 0.55 - text_h  # finish with the last lines (CTA) resting mid-screen
    pts = [(0.0, y0)]
    if constant:  # ease in: a third of the steady speed for the first EASE_S seconds, like the references
        v = (y0 - end_y) / total_dur
        pts.append((EASE_S, y0 - v * EASE_S / 3))
    if not constant:
        v = (y0 - end_y) / total_dur  # the steady speed (px/s)
        for top, t in zip(tops, starts):
            target = READ_Y * H - top
            if (y0 - target) / v > t:  # the steady scroll hasn't got this paragraph to the reading line yet
                continue
            if t > pts[-1][0] + 0.05:
                pts.append((t, target))
        end_y = min(pts[-1][1], end_y)
    pts.append((total_dur, end_y))
    expr = f"{pts[-1][1]:.2f}"
    for (t0, y0), (t1, y1) in reversed(list(zip(pts, pts[1:]))):
        slope = (y1 - y0) / max(t1 - t0, 1e-3)
        expr = f"if(lt(t,{t1:.3f}),{y0:.2f}+({slope:.4f})*(t-{t0:.3f}),{expr})"
    return expr


def integer_scroll(top0, text_h):
    """Frame-exact y(n) for music-only videos: 1px every EASE_EVERY frames for EASE_S seconds, then PX_PER_FRAME px
    every frame, ending with the last lines (CTA) resting mid-screen. Returns (ffmpeg expression in n, duration)."""
    y0, end_y = round(START_Y * H - top0), round(H * 0.55 - text_h)
    ef = int(EASE_S * FPS)
    ease_px = ef // EASE_EVERY
    steady_frames = max(0, (y0 - ease_px - end_y) // PX_PER_FRAME)
    total_frames = ef + steady_frames + int(3 * FPS)  # 3s rest on the CTA
    expr = (f"if(lt(n,{ef}),{y0}-floor(n/{EASE_EVERY}),"
            f"max({end_y},{y0 - ease_px}-{PX_PER_FRAME}*(n-{ef})))")
    return expr, total_frames / FPS


# ---------- pipeline ----------
def build(spec, out_root, only=None, music=None):
    vid = spec["id"]
    d = out_root / vid
    d.mkdir(parents=True, exist_ok=True)
    gender = "male" if spec.get("voice", "").lower().startswith("male") else "female"
    paras = paragraphs(spec["script"])
    music_only = spec.get("audio") == "music"
    if not music_only and only != "render" and (TTS == "elevenlabs" or (TTS == "kie" and eleven_key())) \
            and not all((d / f"vo_{gi:02d}.mp3").exists() for gi in range(len(chunks(paras)))):
        need = el_credits("\n\n".join(paras))
        ok, used = budget_claim(out_root, need)
        if not ok:
            print(f"  {vid}: ElevenLabs budget ({VOICE_BUDGET} credits/day) would be exceeded "
                  f"({used} used + {need} needed): rendering music-only", flush=True)
            music_only = True
            spec["audio_note"] = f"Voice skipped: ElevenLabs budget of {VOICE_BUDGET} credits per run reached."
        else:
            print(f"  {vid}: ElevenLabs credits reserved {need} (today {used}/{VOICE_BUDGET})", flush=True)
    # 1. voice by sections (skipped for music-only videos, which scroll at a fixed reading pace)
    groups = [] if music_only else chunks(paras)
    if only != "render" and not music_only:
        import concurrent.futures as cf
        kv = spec.get("kie_voice", "Rachel")

        def one(gi):
            p = d / f"vo_{gi:02d}.mp3"
            if p.exists():
                return "cached"
            text = "\n\n".join(paras[i] for i in groups[gi])
            if TTS == "elevenlabs" or (TTS == "kie" and eleven_key()):
                try:
                    tts_eleven(text, gender, p, spec.get("el_voice_id"))
                    return "elevenlabs-direct"
                except Exception as e:
                    print(f"  {vid} section {gi}: elevenlabs failed ({e}); falling back", flush=True)
            if TTS in ("kie", "elevenlabs"):
                for attempt in range(2):
                    try:
                        tts_kie(text, gender, p, voice=kv)
                        return "kie-elevenlabs"
                    except Exception as e:
                        print(f"  {vid} section {gi}: kie tts attempt {attempt + 1} failed ({e})", flush=True)
            tts_openai(text, gender, spec.get("voice", ""), p)
            return "openai-gpt-4o-mini-tts"

        with cf.ThreadPoolExecutor(4) as ex:
            engines = list(ex.map(one, range(len(groups))))
        (d / "voice_engine.txt").write_text(", ".join(f"s{i}:{e}" for i, e in enumerate(engines)))
    seg_paths = [d / f"vo_{gi:02d}.mp3" for gi in range(len(groups))]
    # paragraph start times: section start + share of its duration by word count
    starts, t = [], 0.6
    if music_only:
        t = 2.5  # (paragraph start times are only informational for music-only videos)
        for p_ in paras:
            starts.append(t); t += len(p_.split()) / MUSIC_WPS + 0.45
        total = None  # set from the scroll distance once the text layer is laid out
    else:
        durs = [duration(p) for p in seg_paths]
        for g, du in zip(groups, durs):
            words = [len(paras[i].split()) for i in g]
            acc = 0
            for i, w in zip(g, words):
                starts.append(t + du * acc / sum(words)); acc += w
            t += du + 0.35
        total = t + 2.5
    if spec.get("background_image"):
        img = d / "bg.jpg"
        if not img.exists() and only != "render":
            still_image(spec["background_image"], img)
        if only == "assets":
            return None, total or 0
    if only == "assets":
        for k, extra in enumerate(CLIP_ANGLES):
            c = d / f"bg_{k}.mp4"
            if not c.exists():
                veo_clip(spec["background"] + extra, c)
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", c, "-vf", "fps=2,scale=90:-2,tile=8x2", "-frames:v", "1",
                            d / f"bg_{k}_tiles.jpg"], check=True)
        return None, total
    # 2. background: a still image with a slow zoom, or Veo clips
    clips = []
    for k, extra in enumerate([] if spec.get("background_image") else CLIP_ANGLES):
        c = d / f"bg_{k}.mp4"
        if not c.exists() and only != "render":
            veo_clip(spec["background"] + extra, c)
        if c.exists():
            clips.append(c)
    if not clips and not spec.get("background_image"):
        raise RuntimeError("no background clips")
    # 3. text layer
    color = {"yellow": (255, 236, 64), "white": (255, 255, 255)}.get(spec.get("text_color", "white"))
    img, tops, text_h = layout(paras, color)
    img.save(d / "text.png")
    if music_only:
        yexpr, total = integer_scroll(tops[0], text_h)
    else:
        yexpr = f"floor({scroll_expr(tops, starts, total, text_h)})"
    (d / "scroll_expr.txt").write_text(yexpr)
    # 4. voice track (silence for music-only videos)
    vo = d / "voice.m4a"
    if music_only:
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo", "-t", f"{total:.2f}",
                        "-c:a", "aac", "-b:a", "160k", vo], check=True)
    lst = d / "vo_list.txt"
    sil = d / "sil.mp3"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", "anullsrc=r=44100:cl=mono", "-t", "0.35", sil], check=True)
    lines = [f"file '{sil.name}'"]
    for p in seg_paths:
        lines += [f"file '{p.name}'", f"file '{sil.name}'"]
    lst.write_text("\n".join(lines))
    if not music_only:
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-af", "adelay=250|250",
                        "-ar", "44100", "-ac", "2", "-c:a", "aac", "-b:a", "160k", vo], check=True, cwd=d)
    # 5. background loop: crossfade the clips, then loop to length
    bg = d / "bg_loop.mp4"
    if spec.get("background_image"):
        bg = d / "bg_still.png"  # a still frame: no zoom, because zoompan's whole-pixel steps look jittery
        Image.open(d / "bg.jpg").convert("RGB").resize((W, H), Image.LANCZOS).save(bg)
    elif len(clips) == 1:
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", clips[0], "-an", "-vf", f"scale={W}:{H},fps={FPS}", bg], check=True)
    else:
        inputs, fc, prev, off = [], [], "[0:v]", 0.0
        for i, c in enumerate(clips):
            inputs += ["-i", str(c)]
            fc.append(f"[{i}:v]scale={W}:{H},fps={FPS},setpts=PTS-STARTPTS[v{i}]")
        prev, off = "[v0]", duration(clips[0]) - 1.0
        for i in range(1, len(clips)):
            fc.append(f"{prev}[v{i}]xfade=transition=fade:duration=1:offset={off:.2f}[x{i}]")
            prev = f"[x{i}]"; off += duration(clips[i]) - 1.0
        subprocess.run(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", ";".join(fc), "-map", prev, "-an",
                        "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", bg], check=True)
    # 6. final composite
    final = out_root / f"{vid}.mp4"
    music = music or (d / "music.mp3")
    a_inputs = ["-i", str(vo)]
    if Path(music).exists():
        a_inputs += ["-stream_loop", "-1", "-i", str(music)]
        mdb = MUSIC_ONLY_DB if music_only else MUSIC_DB
        afc = (f"[2:a]volume=1.0[vo];[3:a]volume={10 ** (mdb / 20):.4f},afade=t=in:d=1.5,afade=t=out:st={total - 3:.2f}:d=3[mu];"
               f"[vo][mu]amix=inputs=2:duration=first:dropout_transition=0[a]")
    else:
        afc = "[2:a]anull[a]"
    vfc = (f"[0:v]eq=brightness=-0.06:saturation=0.95,format=yuv420p[bgv];"
           f"[bgv][1:v]overlay=x=0:y='{yexpr}':eval=frame:shortest=0,fps={FPS}[v]")
    bg_in = ["-loop", "1", "-framerate", str(FPS), "-i", str(bg)] if str(bg).endswith(".png") else ["-stream_loop", "-1", "-i", str(bg)]
    subprocess.run(["ffmpeg", "-v", "error", "-y", *bg_in, "-loop", "1", "-framerate", str(FPS), "-i", d / "text.png",
                    *a_inputs, "-filter_complex", vfc + ";" + afc, "-map", "[v]", "-map", "[a]",
                    "-t", f"{total:.2f}", "-r", str(FPS), "-c:v", "libx264", "-preset", "medium", "-crf", "17",
                    "-profile:v", "high", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart", final], check=True)
    return final, total


def main():
    global TTS, EL_MODEL, VOICE_BUDGET
    p = argparse.ArgumentParser()
    p.add_argument("--brand", default="comfortwear")
    p.add_argument("--spec", required=True)
    p.add_argument("--music", help="music bed for every video in this run (default: generate one per angle file)")
    p.add_argument("--only", choices=["render", "assets"])
    p.add_argument("--tts", choices=["elevenlabs", "kie", "openai"], default="kie",
                   help="elevenlabs = direct API (env ElevenLabKey); kie also tries direct ElevenLabs first when that key is set")
    p.add_argument("--el-model", default=EL_MODEL, choices=list(EL_RATE), help="ElevenLabs model (turbo = half the credits)")
    p.add_argument("--voice-budget", type=int, default=VOICE_BUDGET, help="max ElevenLabs credits per day across all runs")
    p.add_argument("ids", nargs="*")
    a = p.parse_args()
    TTS, EL_MODEL, VOICE_BUDGET = a.tts, a.el_model, a.voice_budget
    out_root = ADS / "brands" / a.brand / "output" / "scroll_videos"
    out_root.mkdir(parents=True, exist_ok=True)
    specs = json.loads(Path(a.spec).read_text())
    music = a.music
    if not music:  # one Suno bed per spec file, shared by its variations
        bed = Path(a.spec).with_name(Path(a.spec).stem + "_music.mp3")
        if not bed.exists() and a.only != "render":
            print(f"music bed: generating {bed.name}", flush=True)
            suno(specs[0].get("music_prompt", DEFAULT_MUSIC), bed)
        if bed.exists():
            music = str(bed)
    for s in specs:
        if a.ids and s["id"] not in a.ids:
            continue
        print(f"{s['id']}: building…", flush=True)
        f, t = build(s, out_root, a.only, music)
        print(f"  {f or 'assets ready'} ({t / 60:.1f} min)", flush=True)


if __name__ == "__main__":
    main()
