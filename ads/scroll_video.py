"""Scrolling long-form video ads: a looping background, a long story scrolling up from the bottom in big
bold outlined text, and a voice-over that reads it (synced section by section), with a soft music bed.

Format studied from Atria long-runners (a vet's "40 senior cats", FluffCo's hotel pillow, a physical
therapist on sciatica): 720x1280, 4-5 minutes, centered white/yellow text with a heavy black outline, the
hook on screen at second 0 in the lower half, short paragraphs.

    python ads/scroll_video.py --brand comfortwear --spec <variations.json> [IDs]   # full pipeline
    python ads/scroll_video.py --brand comfortwear --spec x.json LV01 --only render  # reuse assets

Spec (list): {"id","script","voice","background","caption","headline","landing_page", optional "text_color"}.
Assets land in ads/brands/<brand>/output/scroll_videos/<ID>/ and the final video in .../<ID>.mp4.
Kie.ai (KIE_AI): veo3_fast for 3 background clips per video, Suno V4_5 for the music bed,
ElevenLabs turbo for the voice; falls back to OpenAI gpt-4o-mini-tts (OPENAI_API_KEY) if Kie TTS fails.
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
W, H, FPS = 720, 1280, 30
START_Y = 0.60      # the hook's top sits here at t=0 (fraction of H), like the examples
READ_Y = 0.30       # a paragraph's top sits here when the voice starts reading it
MUSIC_DB = -24      # music bed under the voice
NO_VOICE = False    # --no-voice: music-only render
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
    font = ImageFont.truetype(str(FONT), 46)
    font.set_variation_by_name("ExtraBold")
    maxw, lh, gap, stroke = int(W * 0.86), 56, 34, 5
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
    total = sum(len(b) * lh for b in blocks) + gap * (len(blocks) - 1) + 40
    img = Image.new("RGBA", (W, total), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    tops, y = [], 10
    for lines in blocks:
        tops.append(y)
        for ln in lines:
            x = (W - d.textlength(ln, font=font)) / 2
            d.text((x, y), ln, font=font, fill=color, stroke_width=stroke, stroke_fill=(0, 0, 0))
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


def scroll_expr(tops, starts, total_dur, text_h):
    """Piecewise-linear y(t) for the text layer: paragraph i's top reaches READ_Y*H when its voice starts."""
    pts = [(0.0, START_Y * H - tops[0])]
    for top, t in zip(tops, starts):
        if t > pts[-1][0] + 0.05:
            pts.append((t, READ_Y * H - top))
    end_y = min(pts[-1][1], H * 0.55 - text_h)  # finish with the last lines (CTA) resting mid-screen
    pts.append((total_dur, end_y))
    expr = f"{pts[-1][1]:.2f}"
    for (t0, y0), (t1, y1) in reversed(list(zip(pts, pts[1:]))):
        slope = (y1 - y0) / max(t1 - t0, 1e-3)
        expr = f"if(lt(t,{t1:.3f}),{y0:.2f}+({slope:.4f})*(t-{t0:.3f}),{expr})"
    return expr


# ---------- music-only (no voice-over), like the FluffCo hotel-pillow ad ----------
WPS = 2.4  # reading pace, words per second


def build_music_only(spec, d, out_root, paras, only, music):
    vid = spec["id"]
    starts, t = [], 1.2
    for p in paras:
        starts.append(t)
        t += len(p.split()) / WPS + 0.5
    total = t + 3.0
    clips = [c for c in (d / "bg_0.mp4", d / "bg_1.mp4") if c.exists()]
    if not clips:
        raise RuntimeError("no background clips")
    color = {"yellow": (255, 236, 64), "white": (255, 255, 255)}.get(spec.get("text_color", "white"))
    img, tops, text_h = layout(paras, color)
    img.save(d / "text.png")
    yexpr = scroll_expr(tops, starts, total, text_h)
    bg = make_bg_loop(d, clips)
    final = out_root / f"{vid}.mp4"
    music = music or (d / "music.mp3")
    fc = (f"[0:v]eq=brightness=-0.06:saturation=0.95,format=yuv420p[bgv];"
          f"[bgv][1:v]overlay=x=0:y='{yexpr}':eval=frame:shortest=0[v];"
          f"[2:a]volume=0.55,afade=t=in:st=0:d=1.5,afade=t=out:st={total - 3:.2f}:d=3[a]")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-stream_loop", "-1", "-i", bg, "-loop", "1", "-i", d / "text.png",
                    "-stream_loop", "-1", "-i", str(music), "-filter_complex", fc, "-map", "[v]", "-map", "[a]",
                    "-t", f"{total:.2f}", "-r", str(FPS), "-c:v", "libx264", "-preset", "veryfast", "-crf", "23",
                    "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart", final], check=True)
    (d / "voice_engine.txt").write_text("none (music only)")
    return final, total


def make_bg_loop(d, clips):
    bg = d / "bg_loop.mp4"
    if len(clips) == 1:
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", clips[0], "-an", "-vf", f"scale={W}:{H},fps={FPS}",
                        "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", bg], check=True)
        return bg
    inputs, fc = [], []
    for i, c in enumerate(clips):
        inputs += ["-i", str(c)]
        fc.append(f"[{i}:v]scale={W}:{H},fps={FPS},setpts=PTS-STARTPTS[v{i}]")
    prev, off = "[v0]", duration(clips[0]) - 1.0
    for i in range(1, len(clips)):
        fc.append(f"{prev}[v{i}]xfade=transition=fade:duration=1:offset={off:.2f}[x{i}]")
        prev = f"[x{i}]"; off += duration(clips[i]) - 1.0
    subprocess.run(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", ";".join(fc), "-map", prev, "-an",
                    "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", bg], check=True)
    return bg


# ---------- pipeline ----------
def build(spec, out_root, only=None, music=None):
    vid = spec["id"]
    d = out_root / vid
    d.mkdir(parents=True, exist_ok=True)
    gender = "male" if spec.get("voice", "").lower().startswith("male") else "female"
    paras = paragraphs(spec["script"])
    # 1. voice by sections
    groups = chunks(paras)
    if only != "render":
        import concurrent.futures as cf
        kv = spec.get("kie_voice", "Rachel")

        def one(gi):
            p = d / f"vo_{gi:02d}.mp3"
            if p.exists():
                return "cached"
            text = "\n\n".join(paras[i] for i in groups[gi])
            if TTS == "kie":
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
    if NO_VOICE or not all(p.exists() for p in seg_paths):
        return build_music_only(spec, d, out_root, paras, only, music)
    # paragraph start times: section start + share of its duration by word count
    starts, t = [], 0.6
    durs = [duration(p) for p in seg_paths]
    for g, du in zip(groups, durs):
        words = [len(paras[i].split()) for i in g]
        acc = 0
        for i, w in zip(g, words):
            starts.append(t + du * acc / sum(words)); acc += w
        t += du + 0.35
    total = t + 2.5
    if only == "assets":
        for k, extra in enumerate(CLIP_ANGLES):
            c = d / f"bg_{k}.mp4"
            if not c.exists():
                veo_clip(spec["background"] + extra, c)
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", c, "-vf", "fps=2,scale=90:-2,tile=8x2", "-frames:v", "1",
                            d / f"bg_{k}_tiles.jpg"], check=True)
        return None, total
    # 2. background clips
    clips = []
    for k, extra in enumerate(CLIP_ANGLES):
        c = d / f"bg_{k}.mp4"
        if not c.exists() and only != "render":
            veo_clip(spec["background"] + extra, c)
        if c.exists():
            clips.append(c)
    if not clips:
        raise RuntimeError("no background clips")
    # 3. text layer
    color = {"yellow": (255, 236, 64), "white": (255, 255, 255)}.get(spec.get("text_color", "white"))
    img, tops, text_h = layout(paras, color)
    img.save(d / "text.png")
    yexpr = scroll_expr(tops, starts, total, text_h)
    (d / "scroll_expr.txt").write_text(yexpr)
    # 4. voice track
    lst = d / "vo_list.txt"
    sil = d / "sil.mp3"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", "anullsrc=r=44100:cl=mono", "-t", "0.35", sil], check=True)
    lines = [f"file '{sil.name}'"]
    for p in seg_paths:
        lines += [f"file '{p.name}'", f"file '{sil.name}'"]
    lst.write_text("\n".join(lines))
    vo = d / "voice.m4a"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-af", "adelay=250|250",
                    "-ar", "44100", "-ac", "2", "-c:a", "aac", "-b:a", "160k", vo], check=True, cwd=d)
    # 5. background loop: crossfade the clips, then loop to length
    bg = d / "bg_loop.mp4"
    if len(clips) == 1:
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
        afc = (f"[2:a]volume=1.0[vo];[3:a]volume={10 ** (MUSIC_DB / 20):.4f},afade=t=out:st={total - 3:.2f}:d=3[mu];"
               f"[vo][mu]amix=inputs=2:duration=first:dropout_transition=0[a]")
    else:
        afc = "[2:a]anull[a]"
    vfc = (f"[0:v]eq=brightness=-0.06:saturation=0.95,format=yuv420p[bgv];"
           f"[bgv][1:v]overlay=x=0:y='{yexpr}':eval=frame:shortest=0[v]")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-stream_loop", "-1", "-i", bg, "-loop", "1", "-i", d / "text.png",
                    *a_inputs, "-filter_complex", vfc + ";" + afc, "-map", "[v]", "-map", "[a]",
                    "-t", f"{total:.2f}", "-r", str(FPS), "-c:v", "libx264", "-preset", "veryfast", "-crf", "23",
                    "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart", final], check=True)
    return final, total


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--brand", default="comfortwear")
    p.add_argument("--spec", required=True)
    p.add_argument("--music", help="music bed for every video in this run (default: generate one per angle file)")
    p.add_argument("--only", choices=["render", "assets"])
    p.add_argument("--tts", choices=["kie", "openai"], default="kie")
    p.add_argument("--no-voice", action="store_true", help="music-only render, scrolled at reading pace")
    p.add_argument("ids", nargs="*")
    a = p.parse_args()
    global TTS, NO_VOICE
    TTS = a.tts
    NO_VOICE = a.no_voice
    out_root = ADS / "brands" / a.brand / "output" / "scroll_videos"
    out_root.mkdir(parents=True, exist_ok=True)
    specs = json.loads(Path(a.spec).read_text())
    music = a.music
    for s in specs:
        if a.ids and s["id"] not in a.ids:
            continue
        print(f"{s['id']}: building…", flush=True)
        f, t = build(s, out_root, a.only, music)
        print(f"  {f or 'assets ready'} ({t / 60:.1f} min)", flush=True)


if __name__ == "__main__":
    main()
