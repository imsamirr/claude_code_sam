"""Natural doctor VO (v2 of the read): ElevenLabs eleven_v3, voice Sarah (mature, reassuring).
The whole body P1-P7 is ONE take (no joins inside the body); each hook is its own take.
    python make_vo_v3.py body H1 H2 H3
Out: vo3/<take>.wav (48k mono) + vo3/<take>.json {"sections": {sec: [{w,s,e}]}, "dur": ..}"""
import json, os, re, difflib, subprocess, sys
import numpy as np, requests
from faster_whisper import WhisperModel
VOICE = "EXAVITQu4vr4xnSDxMaL"   # Sarah
SPEED = 1.08                      # natural ~170 wpm (old read was 200 wpm and flat)
os.makedirs("vo3", exist_ok=True)
wm = WhisperModel("small.en", device="cpu", compute_type="int8")
norm = lambda x: re.sub(r"[^a-z0-9]", "", x.lower())
say = lambda t: t.replace("Comfortwear", "Comfort Wear").replace("20,000", "twenty thousand").replace("40 dollars", "forty dollars")
SCRIPT = {r["id"]: r["text"] for r in json.load(open("vo_script.json"))}
TAKES = {"body": [f"P{i}" for i in range(1, 8)], "H1": ["H1"], "H2": ["H2"], "H3": ["H3"]}

def tts(text, out):
    r = requests.post(f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE}", headers={"xi-api-key": os.environ["ElevenLabKey"]},
                      json={"text": text, "model_id": "eleven_v3", "voice_settings": {"stability": 0.5, "similarity_boost": 0.8, "speed": SPEED}}, timeout=600)
    if r.status_code != 200: raise SystemExit(f"{r.status_code} {r.text[:300]}")
    open(out, "wb").write(r.content)

for take in sys.argv[1:] or list(TAKES):
    secs = TAKES[take]; mp3, wav = f"vo3/{take}.mp3", f"vo3/{take}.wav"
    if not os.path.exists(mp3): tts("\n\n".join(say(SCRIPT[s]) for s in secs), mp3)
    subprocess.run(["ffmpeg", "-v", "quiet", "-y", "-i", mp3, "-af", "silenceremove=start_periods=1:start_threshold=-50dB,areverse,silenceremove=start_periods=1:start_threshold=-50dB,areverse,aresample=48000", "-ac", "1", wav])
    pcm = subprocess.run(["ffmpeg", "-v", "quiet", "-i", wav, "-f", "s16le", "-ac", "1", "-ar", "16000", "-"], capture_output=True).stdout
    a = np.frombuffer(pcm, np.int16).astype(np.float32) / 32768; dur = len(a) / 16000
    segs, _ = wm.transcribe(a, word_timestamps=True, language="en")
    ww = [(w.word.strip(), w.start, w.end) for s in segs for w in s.words]
    words = [(sec, w) for sec in secs for w in SCRIPT[sec].split()]; times = [None] * len(words)
    sm = difflib.SequenceMatcher(a=[norm(w) for _, w in words], b=[norm(w[0]) for w in ww], autojunk=False)
    for b in sm.get_matching_blocks():
        for i in range(b.size): times[b.a + i] = ww[b.b + i][1:]
    miss = sum(t is None for t in times)
    for i in range(len(words)):
        if times[i] is None:
            p = next((times[j][1] for j in range(i - 1, -1, -1) if times[j]), 0.0)
            n = next((times[j][0] for j in range(i + 1, len(words)) if times[j]), dur)
            times[i] = (p, p + max(0.1, (n - p) / 2))
    out = {s: [] for s in secs}
    for (sec, w), (s, e) in zip(words, times): out[sec].append({"w": w, "s": round(s, 3), "e": round(e, 3)})
    # break check: long silences inside a sentence = a glitch/stall in the read
    gaps = [(words[i][1], round(times[i + 1][0] - times[i][1], 2)) for i in range(len(words) - 1)
            if times[i + 1][0] - times[i][1] > 0.55 and not re.search(r"[.,?!:;]$", words[i][1])]
    json.dump({"take": take, "dur": round(dur, 3), "sections": out, "unaligned": miss, "midsentence_gaps": gaps}, open(f"vo3/{take}.json", "w"))
    print(take, f"{dur:.1f}s", round(len(words) / dur * 60), "wpm", "unaligned", miss, "gaps", gaps, flush=True)

# ---- tighten: cap pauses at MAXGAP (cut only true silence, 20 ms fades) and lift tempo slightly; rewrite word times
MAXGAP, TEMPO = 0.42, 1.05
import soundfile as sf
def tighten(take):
    j = json.load(open(f"vo3/{take}.json")); a, sr = sf.read(f"vo3/{take}.wav")
    ws = [w for s in j["sections"].values() for w in s]; cuts = []
    for x, y in zip(ws, ws[1:]):
        g = y["s"] - x["e"]
        if g > MAXGAP:
            c0, c1 = x["e"] + 0.5 * MAXGAP, y["s"] - 0.5 * MAXGAP
            seg = a[int(c0 * sr):int(c1 * sr)]
            if len(seg) and np.sqrt(np.mean(seg ** 2)) < 0.01: cuts.append((c0, c1))
    keep, t, f = [], 0.0, int(0.02 * sr)
    for c0, c1 in cuts + [(len(a) / sr, len(a) / sr)]:
        p = a[int(t * sr):int(c0 * sr)].copy()
        if len(p) > 2 * f: p[:f] *= np.linspace(0, 1, f); p[-f:] *= np.linspace(1, 0, f)
        keep.append(p); t = c1
    b = np.concatenate(keep); sf.write(f"vo3/{take}_cut.wav", b, sr)
    def remap(x):
        return x - sum(min(c1, max(x, c0)) - c0 for c0, c1 in cuts)
    subprocess.run(["ffmpeg", "-v", "quiet", "-y", "-i", f"vo3/{take}_cut.wav", "-af", f"atempo={TEMPO}", "-ar", "48000", "-ac", "1", f"vo3/{take}_final.wav"], check=True)
    for s in j["sections"].values():
        for w in s: w["s"], w["e"] = round(remap(w["s"]) / TEMPO, 3), round(remap(w["e"]) / TEMPO, 3)
    j["dur"] = round(len(b) / sr / TEMPO, 3); j["cuts"] = len(cuts)
    json.dump(j, open(f"vo3/{take}_final.json", "w")); print(take, "tightened", len(cuts), "pauses ->", f"{j['dur']:.1f}s")
for take in sys.argv[1:] or list(TAKES): tighten(take)
