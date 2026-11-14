"""V2 shot list — rebuilt on the reference's rhythm (median ~1.6 s, cut on the noun, anatomy montages on every
symptom line, presenter resets, NUMBER cards, product reveal ~60 %). Headlines only where the reference has them:
hook box, serif build-up, NUMBER cards, product-name box, diagram labels. Everything else is captions.
Aggressive anatomy/nerve visuals stay on symptom lines (rows 1, 7, 21), never on a competitor shoe, never after the reveal.
"""
import json, re
from pathlib import Path
import captions
G = Path(__file__).resolve().parent / "gfx"
_t = {r["row"]: r for r in json.load(open(Path(__file__).resolve().parent / "vo_timing.json"))}
MUSIC_DB = -13.0      # music level relative to VO RMS (measured on the reference: -13 dB)

def W(row, word, nth=1):
    k = 0
    for i, w in enumerate(_t[row]["words"]):
        if w["w"].lower().strip(".,?!:;’'\"").startswith(word.lower()):
            k += 1
            if k == nth: return i
    raise KeyError(f"row {row}: {word}")
def S(row, w=0, **kw): return {"row": row, "w": W(row, w) if isinstance(w, str) else w, **kw}

VH = "visual.healthlab"; VH_BAND = [(860, 1270)]
MC = "medcafee7d9"; MC_BAND = [(1260, 1640)]
SH = "sharingcozymoments"; SH_BAND = [(1260, 1500)]
WH = ("whoosh", -0.06, 0.5); HIT = ("hit", 0.0, 0.5); ZAP = ("zap", 0.03, 0.35)
ILL = {"kind": "small", "text": "Illustration", "x": 140, "y": 1830, "pop": False}
def lab(t): return {"kind": "spaced", "text": t, "y": 1600, "t0": 0.15}
NAME = "COMFORTWEAR ORTHO STRETCH\nCUSHION SHOES"
def serif(lines, ys=(516, 780, 980, 1184), xs=(420, 640, 330, 560), step=0.33):
    return [{"kind": "serif", "text": t, "red": red, "y": ys[i], "x": xs[i], "t0": i * step} for i, (t, red) in enumerate(lines)]

SHOTS = [
    # 01 ─ HOOK: nerve on a real body + red hook box; serif build-up; lumbar sparks; side-bend nerve
    S(1, 0, src=347, ss=0.3, fx={"nerve": {"kf": [(0.5, [(540, 1250), (610, 1450), (665, 1660), (690, 1920)]), (2.5, [(500, 1110), (565, 1320), (630, 1570), (650, 1920)])], "start": 0.0, "band": 80},
      "zoom": (1.0, 1.08), "zc": (540, 1300), "flash": 0.7}, tags=[{"kind": "hook", "text": "IF YOU HAVE SCIATICA", "y": 892}], nocap=True, sfx=[ZAP]),
    S(1, "don", src=144, ss=0.5, fx={"blur": 16, "zoom": (1.05, 1.12)}, tags=serif([("DON'T BUY", False), ("YOUR NEXT", False), ("PAIR", True), ("UNTIL YOU", False)][:3]), nocap=True, sfx=[WH]),
    S(1, "someone", src=358, ss=2.2, fx={"nerve": {"pts": [(330, 1090), (370, 1330), (410, 1600), (440, 1920)], "start": 0.0, "band": 70}, "sparks": [{"c": (330, 1090)}], "zoom": (1.0, 1.06)}, sfx=[ZAP]),
    S(1, "back", src=182, ss=3.0, fx={"nerve": {"pts": [(430, 1190), (380, 1430), (330, 1690), (300, 1920)], "start": 0.0}, "zoom": (1.04, 1.0)}),
    # 02 ─ three packshots on the brand names (burgundy card system)
    S(2, 0, card={"type": "pack", "img": G / "clean_hoka_00.png"}, nocap=True, sfx=[WH]),
    S(2, "new", card={"type": "pack", "img": G / "clean_nb_00.png"}, nocap=True, sfx=[WH]),
    S(2, "brooks", card={"type": "pack", "img": G / "clean_brooks_30.png"}, nocap=True, sfx=[WH]),
    # 03 ─ money, then '3 things' serif build-up
    S(3, 0, src=289, ss=0.5, fx={"zoom": (1.0, 1.1)}),
    S(3, "there", src=310, ss=1.0, fx={"blur": 16, "zoom": (1.05, 1.1)}, tags=serif([("3 THINGS", False), ("YOU NEED", False), ("TO CHECK", True)]), nocap=True, sfx=[WH]),
    # 04 ─ over sixty, planning the day around standing
    S(4, 0, src=319, ss=3.0, fx={"zoom": (1.0, 1.06)}),
    S(4, "sixty", src=339, ss=0.3, fx={"zoom": (1.05, 1.1)}),
    S(4, "planning", src=286, ss=2.0, fx={"zoom": (1.05, 1.12)}),
    S(4, "stay", src=341, ss=5.5, fx={"zoom": (1.0, 1.06)}),
    # 05 ─ NUMBER 1
    S(5, 0, card={"type": "number", "n": 1, "imgs": [(G / "clean_hoka_00.png", None)]}, nocap=True, sfx=[WH, ("hit", 0.0, 0.35)]),
    # 06 ─ cushioning
    S(6, 0, src=382, ss=2.0, fx={"zoom": (1.0, 1.1), "zc": (540, 900)}),
    S(6, "think", src=382, ss=5.0, fx={"zoom": (1.2, 1.28), "zc": (540, 1000)}),
    S(6, "feel", src=382, ss=8.0, fx={"zoom": (1.1, 1.16), "zc": (540, 900)}),
    # 07 ─ SYMPTOM MONTAGE: shooting pain down the leg
    S(7, 0, src=VH, ss=5.0, fx={"inpaint": VH_BAND, "zoom": (1.0, 1.08), "zc": (540, 1050), "glows": [{"c": (560, 1090), "r": 150, "i": 0.5}], "zblur": True}, tags=[ILL]),
    S(7, "shooting", src=282, ss=1.0, fx={"nerve": {"pts": [(700, 330), (725, 640), (705, 900), (690, 1150)], "start": 0.0, "band": 60, "root_r": 90}, "zoom": (1.0, 1.1), "zc": (700, 700)}, sfx=[ZAP]),
    S(7, "leg", src=VH, ss=32.1, fx={"inpaint": VH_BAND, "zoom": (1.05, 1.15), "glows": [{"c": (420, 900), "r": 120, "i": 0.6}, {"c": (640, 1400), "r": 120, "i": 0.5}]}, tags=[ILL]),
    S(7, "understandable", src=240, ss=0.3, fx={"zoom": (1.0, 1.06)}),
    S(7, "soft", src=382, ss=10.5, fx={"zoom": (1.1, 1.18), "zc": (540, 1000)}),
    # 08 ─ presenter reset
    S(8, 0, src=168, ss=10, fx={"fx": 0.28, "zoom": (1.05, 1.1), "leak": 0}),
    S(8, "one", src=170, ss=4.0, fx={"fx": 0.57, "zoom": (1.1, 1.16)}),
    # 09-11 ─ movement checks
    S(9, 0, src=311, ss=0.5, fx={"zoom": (1.0, 1.1), "zc": (540, 1500)}),
    S(9, "feel", src=301, ss=2.0, fx={"zoom": (1.0, 1.06)}),
    S(10, 0, src=278, ss=2.0, fx={"zoom": (1.0, 1.06)}),
    S(11, 0, src=346, ss=1.0, fx={"zoom": (1.0, 1.06)}),
    S(11, "store", src=204, ss=1.0, fx={"zoom": (1.0, 1.05)}),
    # 12-13 ─ awkward / unsteady (non-CW shoes), presenter
    S(12, 0, src=310, ss=3.0, fx={"zoom": (1.05, 1.12)}),
    S(12, "unsteady", src=340, ss=5.0, fx={"zoom": (1.0, 1.06)}),
    S(12, "don", src=168, ss=30, fx={"fx": 0.3, "zoom": (1.08, 1.14)}),
    S(13, 0, src=342, ss=0.5, fx={"zoom": (1.0, 1.06)}),
    # 14 ─ NUMBER 2
    S(14, 0, card={"type": "number", "n": 2, "imgs": [(G / "clean_nb_00.png", None)]}, nocap=True, sfx=[WH, ("hit", 0.0, 0.35)]),
    S(15, 0, src=383, ss=1.0, fx={"zoom": (1.0, 1.08)}),
    S(15, "sensible", src=544, ss=8.0, fx={"zoom": (1.7, 1.8), "zc": (540, 1400)}),
    S(16, 0, src=383, ss=4.0, fx={"zoom": (1.05, 1.12)}),
    S(16, "tell", src=544, ss=15.0, fx={"zoom": (1.7, 1.8), "zc": (540, 1400)}),
    S(16, "right", src=383, ss=12.5, fx={"zoom": (1.15, 1.25), "zc": (540, 1300)}),
    S(17, 0, src=383, ss=13.5, fx={"zoom": (1.35, 1.5), "zc": (560, 1350)}),
    # 18 ─ generic fit illustration (no brand)
    S(18, 0, src=106, ss=1.5, fx={"zoom": (1.0, 1.05)}, tags=[ILL]),
    S(18, "pressing", src=106, ss=5.0, fx={"zoom": (1.05, 1.12), "zc": (540, 1100)}, tags=[ILL]),
    S(19, 0, src=383, ss=6.0, fx={"zoom": (1.2, 1.3), "zc": (540, 1300)}),
    S(19, "loosening", src=310, ss=0.8, fx={"zoom": (1.05, 1.12)}),
    S(20, 0, src=544, ss=22.0, fx={"zoom": (1.7, 1.8), "zc": (540, 1400)}),
    S(20, "widths", src=383, ss=3.0, fx={"zoom": (1.0, 1.08)}),
    S(20, "pair", src=383, ss=14.0, fx={"zoom": (1.1, 1.16)}),
    S(20, "completely", src=310, ss=12.0, fx={"zoom": (1.0, 1.06)}),
    # 21 ─ SYMPTOM MONTAGE: back and leg pain (anatomy, glows, nerve)
    S(21, 0, src=182, ss=6.0, fx={"nerve": {"pts": [(430, 1190), (380, 1430), (330, 1690), (300, 1920)], "start": 0.0}, "zoom": (1.0, 1.05)}, sfx=[ZAP]),
    S(21, "back", src=MC, ss=18.4, fx={"inpaint": MC_BAND, "zoom": (1.05, 1.15), "zc": (540, 1000), "sparks": [{"c": (560, 1180), "R": 220}]}, tags=[ILL]),
    S(21, "leg", src=121, ss=1.5, fx={"nerve": {"kf": [(1.0, [(250, 1240), (300, 1500), (320, 1700), (300, 1920)]), (5.0, [(330, 1050), (330, 1350), (330, 1640), (310, 1920)])], "start": 0.0}, "zoom": (1.0, 1.05)}),
    S(21, "last", src=358, ss=7.0, fx={"glows": [{"c": (330, 1100), "r": 170, "i": 0.9}], "sparks": [{"c": (330, 1100), "R": 240}], "zoom": (1.0, 1.06)}),
    S(21, "shoe", src=312, ss=6.0, fx={"zoom": (1.05, 1.12)}),
    S(21, "rubbing", src=238, ss=2.0, fx={"zoom": (1.0, 1.06)}),
    # 22 ─ NUMBER 3 (VS card, as reference)
    S(22, 0, card={"type": "number", "n": 3, "at": 0.55, "imgs": [(G / "clean_brooks_10.png", "Brooks Ghost"), (G / "clean_brooks_30.png", "Brooks Adrenaline\nGTS")]}, nocap=True, sfx=[WH, ("hit", 0.0, 0.35)]),
    S(23, 0, src=374, ss=3.9, fx={"zoom": (1.0, 1.08)}),
    S(23, "someone", src=539, ss=15.4, fx={"zoom": (1.1, 1.18), "zc": (540, 1100)}),
    S(23, "better", src=374, ss=17.0, fx={"zoom": (1.0, 1.06)}),
    S(24, 0, src=374, ss=15.0, fx={"zoom": (1.0, 1.06)}),
    S(24, "shop", src=374, ss=20.0, fx={"zoom": (1.05, 1.1)}),
    S(24, "whole", src=170, ss=3.0, fx={"fx": 0.57, "zoom": (1.1, 1.16)}),
    # 25-28 ─ everyday moments
    S(25, 0, src=346, ss=4.0, fx={"zoom": (1.05, 1.12)}),
    S(26, 0, src=115, ss=0.5, fx={"zoom": (1.0, 1.06)}),
    S(27, 0, src=308, ss=0.5),
    S(27, "sitting", src=306, ss=0.5),
    S(27, "getting", src=336, ss=0.5),
    S(28, 0, src=168, ss=60, fx={"fx": 0.3, "zoom": (1.05, 1.1)}),
    S(29, 0, src=317, ss=2.0, fx={"zoom": (1.0, 1.08)}),
    S(29, "uncomfortable", src=314, ss=3.0, fx={"zoom": (1.0, 1.06)}),
    S(29, "brand", src=382, ss=11.0, fx={"zoom": (1.1, 1.16), "zc": (540, 900)}),
    S(29, "experience", src=383, ss=15.0, fx={"zoom": (1.0, 1.06)}),
    # 30 ─ THE TURN
    S(30, 0, src=170, ss=4.0, fx={"fx": 0.57, "zoom": (1.1, 1.18), "leak": 1}, sfx=[("whoosh", -0.2, 0.5)]),
    # 31 ─ product name (reference: caption-style name box), real Ortho Stretch
    S(31, 0, src="orthostretch.5", ss=0.0, fx={"key": "0xECEBE8", "zoom": (1.0, 1.04)}, tags=[{"kind": "name", "text": NAME, "y": 1300, "t0": 0.25}], nocap=True, sfx=[HIT]),
    S(31, "ortho", src=215, ss=1.6, fx={"zoom": (1.0, 1.06)}, tags=[{"kind": "name", "text": NAME, "y": 1300, "pop": False}], nocap=True),
    # 32 ─ the treatment distinction: neutral, unhurried
    S(32, 0, src=78, ss=0.5, fx={"zoom": (1.0, 1.06)}),
    S(32, "option", src=168, ss=150, fx={"fx": 0.3, "zoom": (1.05, 1.1)}),
    S(32, "follow", src=170, ss=10.0, fx={"fx": 0.57, "zoom": (1.05, 1.1)}),
    S(33, 0, src=76, ss=1.0, fx={"zoom": (1.0, 1.08)}),
    # 34-38 ─ features on the actual shoe + diagram labels
    S(34, 0, src=13, ss=3.0, fx={"outline": {"pts": [(100, 1300), (150, 900), (230, 560), (380, 300), (560, 250), (760, 320), (860, 560), (880, 900), (870, 1150)], "start": 0.2, "dur": 0.8}}, tags=[lab("WIDE TOE BOX")]),
    S(34, "room", src=16, ss=1.0, fx={"zoom": (1.0, 1.06)}),
    S(35, 0, src=23, ss=1.0, fx={"zoom": (1.0, 1.08)}, tags=[lab("STRETCH KNIT UPPER")]),
    S(35, "forgiving", src=24, ss=1.0, fx={"zoom": (1.0, 1.06)}),
    S(36, 0, src=4, ss=1.0, fx={"zoom": (1.0, 1.08)}, tags=[lab("ARCH SUPPORT")]),
    S(36, "underneath", src=371, ss=2.0, fx={"zoom": (1.0, 1.05)}),
    S(36, "cushioning", src=7, ss=1.0, fx={"zoom": (1.0, 1.08)}, tags=[lab("HEEL CUSHION")]),
    S(36, "soften", src=372, ss=1.2),
    S(37, 0, src=73, ss=0.5, fx={"zoom": (1.0, 1.08)}),
    S(37, "bulk", src=343, ss=0.5, fx={"zoom": (1.0, 1.05)}),
    S(37, "move", src=355, ss=1.0),
    S(38, 0, src=19, ss=2.0, fx={"zoom": (1.0, 1.08)}, tags=[lab("BREATHABLE KNIT")]),
    S(38, "slip", src=350, ss=1.0, fx={"zoom": (1.0, 1.06)}, tags=[lab("SLIP-RESISTANT OUTSOLE")]),
    S(38, "grip", src=307, ss=0.5),
    # 39 ─ recap
    S(39, 0, src=17, ss=1.0, fx={"zoom": (1.0, 1.06)}),
    S(39, "support", src=5, ss=2.0, fx={"zoom": (1.0, 1.06)}),
    S(39, "comfortable", src=329, ss=1.0, fx={"zoom": (1.0, 1.06)}),
    S(39, "afternoon", src=291, ss=2.0, fx={"zoom": (1.0, 1.06)}),
    # 40-42 ─ emotional bridge + lifestyle (no pain FX after the reveal)
    S(40, 0, src=167, ss=36, fx={"fx": 0.62, "zoom": (1.05, 1.1)}),
    S(40, "you", src=313, ss=11.0, fx={"zoom": (1.0, 1.05)}),
    S(40, "uncomfortable", src=297, ss=0.5, fx={"zoom": (1.0, 1.06)}),
    S(40, "demanding", src=305, ss=1.0, fx={"zoom": (1.0, 1.06)}),
    S(41, 0, src=327, ss=3.0, fx={"zoom": (1.0, 1.06)}),
    S(41, "out", src=326, ss=1.0),
    S(41, "focus", src=342, ss=3.0),
    S(42, 0, src=204, ss=0.5),
    S(42, "lunch", src="hf_20261004_070629", ss=0.2, fx={"zoom": (1.0, 1.06)}),
    S(42, "afternoon", src="Picking up kids from park 02", ss=12.0, fx={"zoom": (1.0, 1.05)}),
    # 43 ─ recap criteria
    S(43, 0, src=303, ss=1.0, fx={"zoom": (1.0, 1.06)}),
    S(43, "soft", src=382, ss=8.0, fx={"zoom": (1.0, 1.1)}),
    S(43, "take", src=16, ss=3.0),
    S(43, "fit", src=23, ss=3.0),
    S(43, "features", src=7, ss=3.0),
    # 44 ─ CTA on the actual shoe
    S(44, 0, src=79, ss=0.5, fx={"zoom": (1.0, 1.1), "zc": (540, 900)}, tags=[{"kind": "name", "text": NAME, "y": 560, "t0": 0.2}]),
]

def caption_chunks(timing):
    """Reference behaviour: one caption per clause (split at punctuation); clauses longer than 2 lines are split
    into balanced 3-5 word pieces."""
    import math
    chunks = []
    for r in timing.values():
        clauses, cur = [], []
        for w in r["words"]:
            cur.append(w)
            if w["w"][-1] in ".,?!:;": clauses.append(cur); cur = []
        if cur: clauses.append(cur)
        for cl in clauses:
            txt = " ".join(x["w"] for x in cl)
            n = 1 if len(captions.wrap(txt)) <= 2 and len(cl) <= 7 else math.ceil(len(cl) / 5)
            size = math.ceil(len(cl) / n)
            for k in range(0, len(cl), size):
                part = cl[k:k + size]
                chunks.append({"s": part[0]["s"], "e": part[-1]["e"], "text": re.sub(r"[.,;:]$", "", " ".join(x["w"] for x in part))})
    for a, b in zip(chunks, chunks[1:]): a["e"] = b["s"] if b["s"] - a["e"] < 0.6 else a["e"] + 0.25
    chunks[-1]["e"] += 0.5
    return chunks
