"""ElevenLabs VO (Laura, closest to COM376 narrator) per section + Whisper word alignment to the exact script words.
Out: vo/<id>.wav (48k mono) and vo/<id>.json words [{w,s,e}]"""
import json, os, re, difflib, subprocess, sys
import numpy as np, requests, soundfile as sf
from faster_whisper import WhisperModel
VOICE = "FGY2WhTYpPnrIDTdsKH5"   # Laura
os.makedirs("vo", exist_ok=True)
wm = WhisperModel("base.en", device="cpu", compute_type="int8")
norm = lambda x: re.sub(r"[^a-z0-9]", "", x.lower())
say = lambda t: t.replace("Comfortwear", "Comfort Wear").replace("20,000", "twenty thousand").replace("40 dollars", "forty dollars")
for r in json.load(open("vo_script.json")):
    if sys.argv[1:] and r["id"] not in sys.argv[1:]: continue
    mp3 = f"vo/{r['id']}.mp3"
    resp = requests.post(f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE}", headers={"xi-api-key": os.environ["ElevenLabKey"]},
        json={"text": say(r["text"]), "model_id": "eleven_multilingual_v2",
              "voice_settings": {"stability": 0.45, "similarity_boost": 0.8, "style": 0.15, "use_speaker_boost": True, "speed": 1.12}}, timeout=300)
    resp.raise_for_status(); open(mp3, "wb").write(resp.content)
    subprocess.run(["ffmpeg", "-v", "quiet", "-y", "-i", mp3, "-af", "silenceremove=start_periods=1:start_threshold=-50dB,areverse,silenceremove=start_periods=1:start_threshold=-50dB,areverse,aresample=48000", "-ac", "1", f"vo/{r['id']}.wav"])
    pcm = subprocess.run(["ffmpeg", "-v", "quiet", "-i", f"vo/{r['id']}.wav", "-f", "s16le", "-ac", "1", "-ar", "16000", "-"], capture_output=True).stdout
    a = np.frombuffer(pcm, np.int16).astype(np.float32) / 32768; dur = len(a) / 16000
    segs, _ = wm.transcribe(a, word_timestamps=True, language="en")
    ww = [(w.word.strip(), w.start, w.end) for s in segs for w in s.words]
    script = r["text"].split(); times = [None] * len(script)
    sm = difflib.SequenceMatcher(a=[norm(x) for x in script], b=[norm(w[0]) for w in ww], autojunk=False)
    for b in sm.get_matching_blocks():
        for i in range(b.size): times[b.a + i] = ww[b.b + i][1:]
    for i in range(len(script)):
        if times[i] is None:
            p = next((times[j][1] for j in range(i - 1, -1, -1) if times[j]), 0.0)
            n = next((times[j][0] for j in range(i + 1, len(script)) if times[j]), dur)
            times[i] = (p, p + max(0.1, (n - p) / 2))
    json.dump({"id": r["id"], "dur": round(dur, 3), "words": [{"w": w, "s": round(s, 3), "e": round(e, 3)} for w, (s, e) in zip(script, times)]}, open(f"vo/{r['id']}.json", "w"))
    print(r["id"], round(dur, 1), "s", round(len(script) / dur * 60), "wpm", flush=True)
