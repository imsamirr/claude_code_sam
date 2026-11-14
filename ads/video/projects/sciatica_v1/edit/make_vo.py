"""Scratch VO (local Kokoro TTS) per script row + word timings aligned to the exact script words.
Output: edit/vo.wav (48k mono), edit/vo_timing.json [{row, start, end, words:[{w, s, e}]}]"""
import json, re, difflib, subprocess
import numpy as np, soundfile as sf
from kokoro_onnx import Kokoro
from faster_whisper import WhisperModel
M = "/home/user/claude_code_sam/ads/video/models/"
k = Kokoro(M + "kokoro-v1.0.onnx", M + "voices-v1.0.bin")
wm = WhisperModel("base.en", device="cpu", compute_type="int8")
rows = json.load(open("edit/script_rows.json"))
SPEED, SR = 0.82, 24000
LONG_AFTER = {4, 13, 21, 29, 32, 38, 43}; CARD = {5, 14, 22}
say = lambda t: t.replace("ComfortWear", "Comfort Wear").replace("Hokas", "Hokahs").replace("Hoka ", "Hokah ")
audio, timing, t = [], [], 0.25
audio.append(np.zeros(int(0.25 * SR), np.float32))
for r in rows:
    a, sr = k.create(say(r["vo"]), voice="af_heart", speed=SPEED, lang="en-us")
    a = a.astype(np.float32)
    # trim leading/trailing silence
    nz = np.where(np.abs(a) > 0.01)[0]; a = a[max(0, nz[0] - 600): nz[-1] + 1200]
    a16 = np.interp(np.arange(0, len(a), SR / 16000), np.arange(len(a)), a).astype(np.float32)  # whisper expects 16 kHz
    segs, _ = wm.transcribe(a16, word_timestamps=True, language="en")
    ww = [(w.word.strip(), w.start, w.end) for s in segs for w in s.words]
    script = r["vo"].split()
    norm = lambda x: re.sub(r"[^a-z0-9]", "", x.lower())
    sm = difflib.SequenceMatcher(a=[norm(x) for x in script], b=[norm(w[0]) for w in ww], autojunk=False)
    times = [None] * len(script)
    for blk in sm.get_matching_blocks():
        for i in range(blk.size): times[blk.a + i] = ww[blk.b + i][1:]
    dur = len(a) / SR
    # interpolate gaps
    for i in range(len(script)):
        if times[i] is None:
            prev = next((times[j][1] for j in range(i - 1, -1, -1) if times[j]), 0.0)
            nxt = next((times[j][0] for j in range(i + 1, len(script)) if times[j]), dur)
            times[i] = (prev, prev + max(0.12, (nxt - prev) / 2))
    words = [{"w": w, "s": round(t + s, 3), "e": round(t + e, 3)} for w, (s, e) in zip(script, times)]
    timing.append({"row": r["row"], "start": round(t, 3), "end": round(t + dur, 3), "words": words})
    gap = 0.55 if r["row"] in LONG_AFTER else 0.4 if r["row"] in CARD else 0.22
    audio += [a, np.zeros(int(gap * SR), np.float32)]; t += dur + gap
    print(r["row"], round(dur, 2), round(t, 2), flush=True)
audio.append(np.zeros(int(1.0 * SR), np.float32))
v = np.concatenate(audio); sf.write("edit/vo_24k.wav", v, SR)
subprocess.run(["ffmpeg", "-v", "quiet", "-y", "-i", "edit/vo_24k.wav", "-ar", "48000", "edit/vo.wav"])
json.dump(timing, open("edit/vo_timing.json", "w"), indent=0)
n = sum(len(x["words"]) for x in timing); print("TOTAL", round(len(v) / SR, 2), "s", n, "words", round(n / (len(v) / SR) * 60), "wpm")
