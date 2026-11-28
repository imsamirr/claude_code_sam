"""Find burned-in text (creator captions, TikTok overlays) in every timeline shot so the engine can crop or inpaint it.
    python edit/textscan.py H1 H2 H3     -> build/textscan.json  {base_clip_name: [[x0,y0,x1,y1,text], ...]}"""
import json, subprocess, sys
from concurrent.futures import ThreadPoolExecutor
import numpy as np
import engine4 as E
from rapidocr_onnxruntime import RapidOCR

OUT = E.P / "build" / "textscan2.json"
ocr = RapidOCR()

def grab(path, n):
    """5 frames spread over the shot, at full res"""
    ks = sorted({int(n * f) for f in (0.02, 0.25, 0.5, 0.75, 0.97)})
    fr = []
    for k, f in enumerate(E.frames(path, n)):
        if k in ks: fr.append(f)
    return fr

def scan(path, n):
    boxes = []
    for k, f in enumerate(grab(path, n)):
        res, _ = ocr(np.ascontiguousarray(f[:, :, ::-1]), use_cls=False)
        for pts, txt, sc in res or []:
            if float(sc) < 0.6 or len(txt.strip()) < 2: continue
            xs, ys = [p[0] for p in pts], [p[1] for p in pts]
            boxes.append([int(min(xs)), int(min(ys)), int(max(xs)), int(max(ys)), txt, k])
    return boxes

if __name__ == "__main__":
    import edl4
    db = json.load(open(OUT)) if OUT.exists() else {}
    todo = {}
    for h in sys.argv[1:] or ["H1", "H2", "H3"]:
        audio, words, off, total = E.timeline_audio(h)
        for s in E.build([dict(x) for x in edl4.HOOKS[h] + edl4.BODY], words, total):
            if s["src"].startswith("gen/") or s["src"] == edl4.R376: continue
            todo[E.base_clip.__name__ + str(id(s))] = s
    shots = list(todo.values())
    with ThreadPoolExecutor(3) as ex: paths = list(ex.map(E.base_clip, shots))
    for s, p in zip(shots, paths):
        if p.name in db: continue
        db[p.name] = scan(p, s["n"])
        if db[p.name]: print(s["sec"], s.get("w"), s["src"].split("/")[-1][:40], [b[4][:25] for b in db[p.name]][:4], flush=True)
    json.dump(db, open(OUT, "w"))
    print("scanned", len(db), "with text:", sum(1 for v in db.values() if v))
