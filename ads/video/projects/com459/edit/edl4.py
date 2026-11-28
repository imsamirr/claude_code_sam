"""engine adapter: exposes COM459's edl5 shot list in the HOOKS/BODY/SECTIONS shape engine4.py expects."""
from edl5 import build_shots, sections, MUSIC_DB, R376
HOOKS = {h: [s for s in build_shots(h) if s["sec"] == h] for h in ("H1", "H2", "H3")}
BODY = [s for s in build_shots("H1") if s["sec"].startswith("P")]
SECTIONS = sections()
