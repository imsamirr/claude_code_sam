"""Download selected public-Drive files (from gdown folder listings) into a project assets dir, 4 at a time.
    python drive_pull.py <listing.json> <prefix-or-regex> <outdir> [--regex]"""
import json, re, subprocess, sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
lst, pat, out = sys.argv[1], sys.argv[2], Path(sys.argv[3]); rx = "--regex" in sys.argv
fs = json.load(open(lst))
sel = [f for f in fs if (re.search(pat, f["path"], re.I) if rx else f["path"].startswith(pat))
       and re.search(r"\.(mov|mp4|m4v|gif|mp3|wav|png|jpe?g)$", f["path"], re.I)]
def get(f):
    dst = out / f["path"]; dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists() and dst.stat().st_size > 0: return f["path"], "skip"
    r = subprocess.run(["gdown", "-q", f["id"], "-O", str(dst)], capture_output=True, text=True)
    return f["path"], "ok" if dst.exists() else "FAIL " + r.stderr[-200:]
with ThreadPoolExecutor(4) as ex:
    for p, st in ex.map(get, sel): print(st, p, flush=True)
print("DONE", len(sel))
