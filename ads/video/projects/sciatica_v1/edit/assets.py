"""Resolve catalogue ids / tiktok names to file paths (handles originals replaced by .px.mp4 proxies)."""
import json, glob, os
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
_cat = {c["id"]: c for c in json.load(open(ROOT / "build/catalog/catalog.json"))}
def path(ref):
    if isinstance(ref, int):
        p = ROOT / _cat[ref]["path"]
        if p.exists(): return str(p)
        q = p.with_suffix(".px.mp4")
        if q.exists(): return str(q)
        raise FileNotFoundError(f"#{ref} {p}")
    hits = glob.glob(str(ROOT / "tiktok" / "**" / f"*{ref}*"), recursive=True) + glob.glob(str(ROOT / "assets" / "**" / f"*{ref}*"), recursive=True)
    if not hits: raise FileNotFoundError(ref)
    return hits[0]
def meta(ref): return _cat.get(ref, {}) if isinstance(ref, int) else {}
