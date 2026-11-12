"""Free local transcription fallback (use only when Atria has no cached transcript).

Usage: python3 transcribe.py <lang|auto> <video.mp4> [more.mp4 ...]
Writes <video>.txt next to each file with [start-end] timestamped lines.
Audio is piped through ffmpeg into numpy because PyAV file opening is broken
in some cloud containers.
"""
import subprocess, sys
try:
    from faster_whisper import WhisperModel
except ImportError:
    subprocess.run([sys.executable, "-m", "pip", "install", "-q", "faster-whisper"], check=True)
    from faster_whisper import WhisperModel
import numpy as np

lang, files = sys.argv[1], sys.argv[2:]
model = WhisperModel("small", device="cpu", compute_type="int8")
for f in files:
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", f, "-f", "s16le", "-ac", "1", "-ar", "16000", "-"],
                         capture_output=True, check=True).stdout
    audio = np.frombuffer(raw, np.int16).astype(np.float32) / 32768.0
    segs, info = model.transcribe(audio, language=None if lang == "auto" else lang)
    out = f.rsplit(".", 1)[0] + ".txt"
    with open(out, "w") as o:
        for s in segs:
            o.write(f"[{s.start:6.1f}-{s.end:6.1f}] {s.text.strip()}\n")
    print("wrote", out, "lang", info.language)
