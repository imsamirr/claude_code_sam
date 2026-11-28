"""COM458 edit engine: hook variant + shared body, COM376 text system, Laura VO, 1080x1920@30.
    python edit/engine4.py H1 [--preview] [--only P1-P3] [--out file]
Shot lists live in edl4.py (HOOKS[h] and BODY), each shot: dict(sec, w=word index/prefix, src, ss, fx, text overlays...)."""
import argparse, hashlib, json, math, re, subprocess, sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import numpy as np, cv2, soundfile as sf
HERE = Path(__file__).resolve().parent; P = HERE.parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(P.parent / "sciatica_v1" / "edit"))
import text376 as T, fxlib
FPS, W, H = 30, 1080, 1920
BUILD = P / "build" / "shots"; BUILD.mkdir(parents=True, exist_ok=True)
SR = 48000
norm = lambda s: re.sub(r"[^a-z0-9']", "", s.lower())

def timeline_audio(hook, gap=0.12):
    """concatenate hook + P1..P7 wavs; return words with global times and section offsets"""
    secs = [hook] + [f"P{i}" for i in range(1, 8)]
    words, off, chunks, t = {}, {}, [], 0.15
    chunks.append(np.zeros(int(0.15 * SR)))
    for s in secs:
        a, sr = sf.read(HERE / "vo" / f"{s}.wav"); a = a if a.ndim == 1 else a.mean(1)
        j = json.load(open(HERE / "vo" / f"{s}.json"))
        off[s] = t; words[s] = [{**w, "s": w["s"] + t, "e": w["e"] + t} for w in j["words"]]
        g = 0.3 if s == hook else 0.14
        chunks += [a, np.zeros(int(g * SR))]; t += len(a) / SR + g
    chunks.append(np.zeros(int(3.0 * SR)))
    return np.concatenate(chunks), words, off, t + 2.4          # end card holds ~3 s like COM376

def wi(words, sec, w):
    if isinstance(w, int): return w
    toks = [norm(x) for x in w.split()]; nth = 1
    if "#" in w: w, nth = w.split("#"); toks = [norm(x) for x in w.split()]; nth = int(nth)
    k = 0
    for i in range(len(words[sec]) - len(toks) + 1):
        if [norm(x["w"]) for x in words[sec][i:i + len(toks)]] == toks:
            k += 1
            if k == nth: return i
    raise KeyError(f"{sec}: {w}")

def build(shots, words, total):
    out = []
    for s in shots: s["t"] = words[s["sec"]][wi(words, s["sec"], s.get("w", 0))]["s"] - 0.03 + s.get("dt", 0)
    shots[0]["t"] = 0.0
    for i, s in enumerate(shots):
        t1 = shots[i + 1]["t"] if i + 1 < len(shots) else total
        f0, f1 = round(s["t"] * FPS), round(t1 * FPS)
        if f1 <= f0: raise ValueError(f"no duration: {s}")
        out.append({**s, "i": i, "f0": f0, "n": f1 - f0, "t0": f0 / FPS})
    return out

def resolve(src):
    p = P / src
    if p.exists(): return str(p)
    q = P.parent / "sciatica_v1" / src
    if q.exists(): return str(q)
    for b in (p, q):
        r = b.with_suffix(".px.mp4")
        if r.exists(): return str(r)
    raise FileNotFoundError(src)

def base_clip(s):
    fx = s.get("fx", {}); src = resolve(s["src"])
    key = hashlib.md5(json.dumps([src, s.get("ss", 0), s["n"], {k: fx.get(k) for k in ("fx", "fy", "z", "speed", "bw", "hflip", "crop", "rev", "blur")}], sort_keys=True).encode()).hexdigest()[:12]
    out = BUILD / f"{key}.mp4"
    if out.exists(): return out
    ch = []
    if fx.get("rev"): ch.append("reverse")
    ch += [f"setpts=PTS/{fx.get('speed', 1.0)}", f"fps={FPS}"]
    if fx.get("crop"): x, y, w, h = fx["crop"]; ch.append(f"crop=iw*{w}:ih*{h}:iw*{x}:ih*{y}")
    z = fx.get("z", 1.0)
    ch += [f"scale=w='if(gt(a,{W}/{H}),-2,{int(W*z)})':h='if(gt(a,{W}/{H}),{int(H*z)},-2)'",
           f"crop={W}:{H}:(iw-{W})*{fx.get('fx',0.5)}:(ih-{H})*{fx.get('fy',0.5)}"]
    if fx.get("bw"): ch.append("hue=s=0")
    if fx.get("blur"): ch.append(f"gblur=sigma={fx['blur']}")
    ch += ["tpad=stop_mode=clone:stop_duration=30", "format=yuv420p"]
    dur = s["n"] / FPS / fx.get("speed", 1.0) + 1.0
    pre = ["-ss", str(s.get("ss", 0)), "-t", f"{dur + (0 if not fx.get('rev') else 0):.2f}"]
    r = subprocess.run(["ffmpeg", "-v", "error", "-y", *pre, "-i", src, "-vf", ",".join(ch), "-frames:v", str(s["n"]), "-an", "-c:v", "libx264", "-preset", "veryfast", "-crf", "15", str(out)], capture_output=True, text=True)
    if r.returncode or not out.exists(): raise RuntimeError(f"{s['src']}: {r.stderr[-300:]}")
    return out

def frames(path, n):
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-i", str(path), "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE); last = None
    for _ in range(n):
        b = p.stdout.read(W * H * 3)
        if len(b) == W * H * 3: last = np.frombuffer(b, np.uint8).reshape(H, W, 3)
        yield last.copy() if last is not None else np.zeros((H, W, 3), np.uint8)
    p.stdout.close(); p.wait()

_TS = None
SCENE = re.compile(r"^(h.?.?ka|ka|hok|on|cloud|oncloud|nike|asics|brooks|noble.*|\W+|\d{1,2})$", re.I)
def overlay_like(b, allb):
    """burned-in captions sit still on screen while the footage moves: same box (or same centred line) in another sampled frame.
    single-frame hits only count when centred multi-word lines (fast karaoke captions)"""
    x0, y0, x1, y1, t, k = b[:6]; xc = (x0 + x1) / 2
    still = any(o[5] != k and abs(o[1] - y0) < 9 and abs(o[3] - y1) < 9 and abs((o[0] + o[2]) / 2 - xc) < 14 for o in allb)
    karaoke = abs(xc - W / 2) < 90 and any(o[5] != k and abs((o[1] + o[3]) / 2 - (y0 + y1) / 2) < 14 and abs((o[0] + o[2]) / 2 - W / 2) < 90 for o in allb)
    return still or karaoke or (len(t.split()) >= 3 and abs(xc - W / 2) < 60)

def plan_clean(s, base):
    """remove burned-in creator captions found by textscan.py: crop them out with a zoom window if that costs <=1.45x, else inpaint"""
    global _TS
    if _TS is None:
        f = P / "build" / "textscan2.json"; _TS = json.load(open(f)) if f.exists() else {}
    if s.get("keep_text") or s["src"].startswith("gen/") or s["src"].startswith("reference/"): return None
    allb = _TS.get(Path(base).name, [])
    bx = [b for b in allb if overlay_like(b, allb) and not SCENE.match(b[4].strip())]
    s["fx"] = dict(s.get("fx", {}))
    bx += [list(b) + ["manual"] for b in s.get("rm_boxes", [])]
    fx0 = s.get("fx", {})
    if "zc" in fx0:                       # manual framing: only text that stays visible matters; map it to output coords
        z = fx0.get("zoom", (1.0,))[0]; cx, cy = fx0["zc"]; T_ = lambda v, c: c + z * (v - c)
        bx = [[T_(b[0], cx), T_(b[1], cy), T_(b[2], cx), T_(b[3], cy)] + list(b[4:]) for b in bx]
        bx = [b for b in bx if b[3] > 0 and b[1] < H and b[2] > 0 and b[0] < W]
        s["inp_after_zoom"] = True
    if not bx: return None
    big = [b for b in bx if b[3] - b[1] >= 34]; small = [b for b in bx if b[3] - b[1] < 34]
    fx = s.setdefault("fx", {}); s["inp_boxes"] = list(small)
    if not big: return "inpaint-small"
    iv = []
    for a, b in sorted((max(0, b[1] - 22), min(H, b[3] + 22)) for b in big):
        if iv and a <= iv[-1][1]: iv[-1][1] = max(iv[-1][1], b)
        else: iv.append([a, b])
    gaps, prev = [], 0
    for a, b in iv: gaps.append((prev, a)); prev = b
    gaps.append((prev, H)); a, b = max(gaps, key=lambda g: g[1] - g[0])
    z = H / max(b - a, 1) * 1.01; cur = fx.get("zoom", (1.0, 1.0))
    if z <= 1.5 and "zc" not in fx:
        z = max(z, cur[0]); cy = 0.0 if a <= 0 else (float(H) if b >= H else a / (1 - 1 / z))
        fx["zoom"] = (z, z + 0.035); fx["zc"] = (W / 2, cy); return f"crop z{z:.2f} win {a}-{b}"
    s["inp_boxes"] += big
    yb = max(iv, key=lambda v: v[1] - v[0]); yc = (yb[0] + yb[1]) / 2
    if 650 < yc < 1550 and "cap_y" not in s: s["cap_y"] = int(yc)          # our caption box sits over the cleaned band
    return f"INPAINT-BIG {len(big)} ({b - a}px free) cap@{s.get('cap_y')}"

def inpaint_rect(fr, b):
    x0, y0, x1, y1 = max(0, b[0] - 10), max(0, b[1] - 8), min(W, b[2] + 10), min(H, b[3] + 8)
    reg = fr[y0:y1, x0:x1]
    m = fxlib.text_mask(reg)
    if m.mean() < 0.04: m = np.ones(reg.shape[:2], np.uint8)
    m = cv2.dilate(m, np.ones((5, 5), np.uint8))
    sm = cv2.resize(reg, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    ms = cv2.resize(m, (sm.shape[1], sm.shape[0]), interpolation=cv2.INTER_NEAREST)
    fixed = cv2.resize(cv2.inpaint(sm, ms, 7, cv2.INPAINT_TELEA), (reg.shape[1], reg.shape[0]))
    mm = cv2.GaussianBlur(m.astype(np.float32), (0, 0), 3)[..., None]
    fr[y0:y1, x0:x1] = (fixed * mm + reg * (1 - mm)).astype(np.uint8)
    return fr

def fx_frame(fr, s, tl):
    fx = s.get("fx", {})
    if not s.get("inp_after_zoom"):
        for b in s.get("inp_boxes", []): fr = inpaint_rect(fr, b)
    for band in fx.get("inpaint", []): fr = fxlib.inpaint_band(fr, *band)
    if "zoom" in fx:
        z0, z1 = fx["zoom"]; z = z0 + (z1 - z0) * min(1, tl / max(s["n"] / FPS, 1e-3)); cx, cy = fx.get("zc", (W / 2, H / 2))
        fr = cv2.warpAffine(fr, np.float32([[z, 0, cx - z * cx], [0, z, cy - z * cy]]), (W, H), borderMode=cv2.BORDER_REFLECT)
    if s.get("inp_after_zoom"):
        for b in s.get("inp_boxes", []): fr = inpaint_rect(fr, [int(max(0, min(W if i % 2 == 0 else H, v))) for i, v in enumerate(b[:4])])
    f = fr.astype(np.float32)
    if fx.get("flash") and tl < 0.1: f = f + (255 - f) * (1 - tl / 0.1) * fx["flash"]
    if fx.get("leak") is not None: f = fxlib.light_leak(f, tl, side=fx["leak"])
    if fx.get("x"): f = fxlib.red_x(f, tl, 0.08).astype(np.float32)
    return np.clip(f, 0, 255).astype(np.uint8)

def overlays(fr, s, tl, gt, sec_heads):
    if s.get("hook"):
        a = T.hook_box(*s["hook"]); fxlib.blit(fr, a, W / 2, s.get("hook_y", 980), 1.0)
    if s.get("doctor") and tl > 0.15: fxlib.blit(fr, T.doctor_label(), 380, 1030, 1.0)
    for st, en, lines in sec_heads:
        if st <= gt < en: fxlib.blit(fr, T.section(lines), W / 2, 470, 1.0)
    for g in s.get("stickers", []):
        if tl >= g.get("t0", 0): fxlib.blit(fr, g["img"], g.get("x", W / 2), g.get("y", 900), g.get("sc", 1.0) * (0.8 + 0.2 * fxlib.ease((tl - g.get("t0", 0)) / 0.15)))

def caption_chunks(words, secs):
    """COM376 rhythm: 2-5 words per caption, break at punctuation, max 2 lines"""
    out = []
    for sec in secs:
        cur = []; ws = words[sec]
        for i, w in enumerate(ws):
            cur.append(w); txt = " ".join(x["w"] for x in cur)
            p = w["w"][-1] in ".,?!:;"; nxt = ws[i + 1]["w"] if i + 1 < len(ws) else None
            if p or nxt is None or len(cur) >= 4 or (len(cur) >= 3 and len(T.wrap(txt + " " + nxt, T.F(T.CAP["size"]), T.CAP["track"], T.CAP["maxw"])) > 2):
                out.append({"s": cur[0]["s"], "e": cur[-1]["e"], "text": re.sub(r"[.,;:]$", "", txt)}); cur = []
    for a, b in zip(out, out[1:]): a["e"] = b["s"] if b["s"] - a["e"] < 0.6 else a["e"] + 0.2
    return out

def render(hook, only=None, preview=False, out=None):
    import edl4
    audio, words, off, total = timeline_audio(hook)
    shots = build([dict(x) for x in edl4.HOOKS[hook] + edl4.BODY], words, total)
    heads = [(words[sec][wi(words, sec, a)]["s"], words[sec][wi(words, sec, b)]["s"], lines) for sec, a, b, lines in edl4.SECTIONS]
    chunks = [c for c in caption_chunks(words, [hook] + [f"P{i}" for i in range(1, 8)])]
    sel = [s for s in shots if only is None or s["sec"] in only]
    with ThreadPoolExecutor(3) as ex: bases = dict(zip([s["i"] for s in sel], ex.map(base_clip, sel)))
    rep = []
    for s in sel:
        r = plan_clean(s, bases[s["i"]])
        if r: rep.append(f"{s['i']:3d} {s['t0']:6.1f}s {s['sec']} {str(s.get('w'))[:22]:22s} {r}")
    (P / "build" / f"clean_{hook}.txt").write_text("\n".join(rep)); print(len(rep), "shots cleaned;", sum("BIG" in r for r in rep), "big inpaints")
    # audio mix: VO + music bed + sfx
    n = int(total * SR); mix = np.zeros(n); L = min(n, len(audio)); mix[:L] += audio[:L] / (np.sqrt(np.mean(audio[np.abs(audio) > 1e-4] ** 2)) + 1e-9) * 0.12
    mpath = P / "build" / "music.wav"
    if mpath.exists():
        m, _ = sf.read(mpath); m = m if m.ndim == 1 else m.mean(1); m = np.tile(m, int(n / len(m)) + 1)[:n]
        m = m / (np.sqrt(np.mean(m[np.abs(m) > 1e-4] ** 2)) + 1e-9) * 0.12 * 10 ** (edl4.MUSIC_DB / 20); fade = np.ones(n); fade[-int(1.5 * SR):] = np.linspace(1, 0, int(1.5 * SR)); mix += m * fade
    pk = np.abs(mix).max(); mix = mix / pk * 0.9 if pk > 0.9 else mix
    wav = P / "build" / f"mix_{hook}.wav"; sf.write(wav, mix.astype(np.float32), SR)
    f0, f1 = sel[0]["f0"], sel[-1]["f0"] + sel[-1]["n"]
    out = Path(out) if out else P / "out" / f"COM458_{hook}{'_preview' if preview or only else ''}.mp4"
    enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                            "-ss", f"{f0 / FPS:.3f}", "-t", f"{(f1 - f0) / FPS:.3f}", "-i", str(wav), "-c:v", "libx264", "-preset", "veryfast" if preview else "medium",
                            "-crf", "21" if preview else "17", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", str(out)], stdin=subprocess.PIPE)
    for s in sel:
        for k, fr in enumerate(frames(bases[s["i"]], s["n"])):
            tl = k / FPS; gt = (s["f0"] + k) / FPS
            fr = fx_frame(fr, s, tl); overlays(fr, s, tl, gt, heads)
            if not s.get("nocap"):
                for c in chunks:
                    if c["s"] - 0.02 <= gt < c["e"]: fxlib.blit(fr, T.caption(c["text"]), W / 2, s.get("cap_y", 1320)); break
            enc.stdin.write(np.ascontiguousarray(fr).tobytes())
    enc.stdin.close(); enc.wait(); print("wrote", out, f"{(f1 - f0) / FPS:.1f}s", len(sel), "shots")
    return shots

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("hook"); ap.add_argument("--preview", action="store_true"); ap.add_argument("--only"); ap.add_argument("--out")
    a = ap.parse_args(); render(a.hook, a.only.split(",") if a.only else None, a.preview, a.out)
