"""Local word-timestamped transcripts (faster-whisper) for every <analysis_root>/<stem>/audio.mp3 -> transcript.json + transcript.txt
    python ads/video/scripts/transcribe.py <analysis_root> [<analysis_root> ...]"""
import json, subprocess, sys
import numpy as np
from pathlib import Path
from faster_whisper import WhisperModel
m = WhisperModel("base", device="cpu", compute_type="int8", cpu_threads=2)
for root in sys.argv[1:]:
    for a in sorted(Path(root).glob("*/audio.mp3")):
        out = a.parent / "transcript.json"
        if out.exists(): continue
        pcm = subprocess.run(["ffmpeg", "-v", "quiet", "-i", str(a), "-f", "s16le", "-ac", "1", "-ar", "16000", "-"], capture_output=True).stdout
        segs, info = m.transcribe(np.frombuffer(pcm, np.int16).astype(np.float32) / 32768.0, word_timestamps=True, vad_filter=True)
        segs = [{"start": round(s.start, 2), "end": round(s.end, 2), "text": s.text.strip(),
                 "words": [{"w": w.word.strip(), "s": round(w.start, 2), "e": round(w.end, 2)} for w in (s.words or [])]} for s in segs]
        n = sum(len(s["words"]) for s in segs); dur = segs[-1]["end"] if segs else 0
        json.dump({"language": info.language, "segments": segs, "n_words": n, "wpm": round(60 * n / max(dur, 1), 1)}, open(out, "w"), indent=1)
        (a.parent / "transcript.txt").write_text(f"lang={info.language} words={n}\n" + "\n".join(f"[{s['start']:6.2f}-{s['end']:6.2f}] {s['text']}" for s in segs))
        print(a.parent.name, info.language, n, "words", flush=True)
