"""Scratch VO (local Kokoro TTS) + word timings aligned to the exact script words.

V2 fixes the V1 glitches: no hard trims (keep natural decay, trim only silence below -50 dB with 120 ms
margins), 12 ms raised-cosine fades on every join, natural speed (no slow-down warble), gaps sized by
punctuation/structure, and Whisper alignment fed real 16 kHz audio.
Output: edit/vo.wav (48 kHz mono), edit/vo_timing.json [{row, start, end, words:[{w, s, e}]}]
"""
import json, re, difflib, subprocess
import numpy as np, soundfile as sf
from kokoro_onnx import Kokoro
from faster_whisper import WhisperModel
from scipy.signal import resample_poly

M = "/home/user/claude_code_sam/ads/video/models/"
k = Kokoro(M + "kokoro-v1.0.onnx", M + "voices-v1.0.bin")
wm = WhisperModel("base.en", device="cpu", compute_type="int8")
rows = json.load(open("edit/script_rows.json"))
SR, SPEED, VOICE = 24000, 0.94, "af_heart"
CARD = {5, 14, 22}                    # chapter cards: beat before and after
BIG = {4, 13, 21, 29, 32, 39, 43}     # end of a section: longer breath
say = lambda t: t.replace("ComfortWear", "Comfort Wear").replace("Hokas", "Hoka's").replace("—", ", ")

def trim(a, thr_db=-50, margin=0.12):
    env = np.convolve(np.abs(a), np.ones(240) / 240, "same"); thr = 10 ** (thr_db / 20)
    nz = np.where(env > thr)[0]
    s, e = max(0, nz[0] - int(margin * SR)), min(len(a), nz[-1] + int(margin * SR))
    a = a[s:e].copy(); f = int(0.012 * SR); w = 0.5 - 0.5 * np.cos(np.linspace(0, np.pi, f))
    a[:f] *= w; a[-f:] *= w[::-1]
    return a

norm = lambda x: re.sub(r"[^a-z0-9]", "", x.lower())
audio, timing, t = [np.zeros(int(0.2 * SR), np.float32)], [], 0.2
for r in rows:
    a, _ = k.create(say(r["vo"]), voice=VOICE, speed=SPEED, lang="en-us")
    a = trim(a.astype(np.float32))
    a16 = resample_poly(a, 2, 3).astype(np.float32)
    segs, _ = wm.transcribe(a16, word_timestamps=True, language="en")
    ww = [(w.word.strip(), w.start, w.end) for s in segs for w in s.words]
    script = r["vo"].split(); times = [None] * len(script)
    sm = difflib.SequenceMatcher(a=[norm(x) for x in script], b=[norm(w[0]) for w in ww], autojunk=False)
    for blk in sm.get_matching_blocks():
        for i in range(blk.size): times[blk.a + i] = ww[blk.b + i][1:]
    dur = len(a) / SR
    for i in range(len(script)):
        if times[i] is None:
            prev = next((times[j][1] for j in range(i - 1, -1, -1) if times[j]), 0.05)
            nxt = next((times[j][0] for j in range(i + 1, len(script)) if times[j]), dur)
            times[i] = (prev, prev + max(0.12, (nxt - prev) / 2))
    timing.append({"row": r["row"], "start": round(t, 3), "end": round(t + dur, 3),
                   "words": [{"w": w, "s": round(t + s, 3), "e": round(t + e, 3)} for w, (s, e) in zip(script, times)]})
    gap = 0.45 if r["row"] in BIG or r["row"] + 1 in CARD else 0.3 if r["row"] in CARD else 0.12
    audio += [a, np.zeros(int(gap * SR), np.float32)]; t += dur + gap
    print(r["row"], round(dur, 2), round(t, 2), flush=True)
audio.append(np.zeros(int(1.0 * SR), np.float32))
v = np.concatenate(audio); v = v / np.abs(v).max() * 0.9
sf.write("edit/vo_24k.wav", v, SR)
subprocess.run(["ffmpeg", "-v", "quiet", "-y", "-i", "edit/vo_24k.wav", "-af", "aresample=48000:resampler=soxr", "edit/vo.wav"])
json.dump(timing, open("edit/vo_timing.json", "w"), indent=0)
n = sum(len(x["words"]) for x in timing); print("TOTAL", round(len(v) / SR, 2), "s", n, "words", round(n / (len(v) / SR) * 60), "wpm")
