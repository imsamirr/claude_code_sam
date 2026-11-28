"""Scene-pacing analysis: why does an edit *feel* fast? Measures, per video:
 shot-length distribution (p10/p25/median, share < 1.0 / 1.2 / 1.5 s, longest run of sub-1.5 s shots),
 words of VO per shot, transition type at each cut (hard cut vs soft/dissolve/whip, from the frame-difference profile),
 'continuity' cuts (adjacent shots from the same scene/location: colour-histogram correlation),
 in-shot motion (camera/subject movement) and how often a cut lands mid-word.
    python ads/video/scripts/pacing.py <video.mp4> [transcript.json] ...  -> JSON lines on stdout"""
import json, subprocess, sys
import numpy as np

def frames(path, w=96, h=170, fps=30):
    raw = subprocess.run(["ffmpeg", "-v", "quiet", "-i", path, "-vf", f"fps={fps},scale={w}:{h}", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], capture_output=True).stdout
    return np.frombuffer(raw, np.uint8).reshape(-1, h, w, 3).astype(np.float32)

def hist(f):
    hs = [np.histogram(f[..., c], 16, (0, 256))[0] for c in range(3)]
    return np.concatenate(hs).astype(np.float32)

def analyse(path, tr=None):
    F = frames(path); n = len(F); fps = 30
    g = F.mean(3); d = np.abs(np.diff(g, axis=0)).mean((1, 2))          # luma change per frame
    H = np.array([hist(f) for f in F])
    hd = np.array([1 - np.corrcoef(H[i], H[i + 1])[0, 1] for i in range(n - 1)])
    score = d / (np.median(d) + 1e-3) + 40 * hd
    cuts = []
    for i in range(2, n - 3):                                          # hard cuts: isolated spike
        if score[i] > 9 and score[i] == score[max(0, i - 4):i + 5].max() and (not cuts or i - cuts[-1] > 6): cuts.append(i)
    # soft transitions: sustained change over 4-12 frames between two different-looking frames, no single spike
    soft = []
    i = 0
    while i < n - 14:
        if not any(abs(i - c) < 10 for c in cuts):
            for L in (6, 9, 12):
                a, b = H[i], H[i + L]
                if 1 - np.corrcoef(a, b)[0, 1] > 0.35 and score[i:i + L].max() < 9 and d[i:i + L].min() > 1.5 * np.median(d):
                    soft.append(i + L // 2); i += L; break
        i += 1
    allc = sorted(cuts + soft)
    b = [0] + allc + [n]; L = np.diff(b) / fps
    # continuity: shots on either side of a cut look alike (same location/clip family)
    cont = [1 - np.corrcoef(H[max(0, c - 3)], H[min(n - 1, c + 3)])[0, 1] < 0.12 for c in allc]
    # in-shot motion (exclude 4 frames around every cut)
    mask = np.ones(n - 1, bool)
    for c in allc: mask[max(0, c - 4):c + 4] = False
    motion = float(np.median(d[mask])) if mask.any() else 0
    runs, r = [], 0
    for x in L:
        r = r + 1 if x < 1.5 else 0; runs.append(r)
    out = {"file": path.split("/")[-1][:40], "dur": round(n / fps, 1), "shots": len(L), "p10": round(float(np.percentile(L, 10)), 2),
           "p25": round(float(np.percentile(L, 25)), 2), "med": round(float(np.median(L)), 2), "lt1.0": round(float((L < 1.0).mean()), 2),
           "lt1.2": round(float((L < 1.2).mean()), 2), "lt1.5": round(float((L < 1.5).mean()), 2), "max_fast_run": int(max(runs)),
           "soft_share": round(len(soft) / max(1, len(allc)), 2), "continuity_share": round(float(np.mean(cont)) if cont else 0, 2), "motion": round(motion, 2)}
    if tr:
        j = json.load(open(tr)); ws = j.get("words") or [w for s in j.get("segments", []) for w in s.get("words", [])]
        ws = [(w.get("start", w.get("s")), w.get("end", w.get("e"))) for w in ws if w.get("start", w.get("s")) is not None]
        if ws:
            out["words_per_shot"] = round(len(ws) / len(L), 2)
            st = np.array([w[0] for w in ws]); en = np.array([w[1] for w in ws])
            mid = sum(bool(((st < c / fps - 0.04) & (en > c / fps + 0.04)).any()) for c in allc)
            out["midword_cuts"] = round(mid / max(1, len(allc)), 2)
    return out

if __name__ == "__main__":
    a = sys.argv[1:]; i = 0
    while i < len(a):
        tr = a[i + 1] if i + 1 < len(a) and a[i + 1].endswith(".json") else None
        print(json.dumps(analyse(a[i], tr)), flush=True); i += 2 if tr else 1
