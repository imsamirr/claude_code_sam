"""V3 shot list — mirrors the Hike/HF Flow reference shot-for-shot (ref shot numbers in comments, see
reference_analysis.md + /reference/ref/cuts.json). Rules from user feedback on V2:
 - competitor brands shown as FULL clips (number cards play the real clip in a panel; no cut-outs)
 - bigger captions; NO headlines except the reference's own devices (red hook box, serif build-up, NUMBER cards)
 - presenter = Dr. Jesse talking to camera (#152), returning between montages exactly where the reference cuts to its presenter
 - B&W + red X device on the 'uncomfortable shoes' line (ref #79-84)
Aggressive anatomy/nerve stays on symptom lines (rows 1, 7, 21), never on a competitor shoe, never after the reveal.
"""
import json, re, math
from pathlib import Path
import captions
G = Path(__file__).resolve().parent / "gfx"
_t = {r["row"]: r for r in json.load(open(Path(__file__).resolve().parent / "vo_timing.json"))}
MUSIC_DB = -13.0

def W(row, word, nth=1):
    k = 0
    for i, w in enumerate(_t[row]["words"]):
        if w["w"].lower().strip(".,?!:;’'\"").startswith(word.lower()):
            k += 1
            if k == nth: return i
    raise KeyError(f"row {row}: {word}")
def S(row, w=0, **kw): return {"row": row, "w": W(row, w) if isinstance(w, str) else w, **kw}

VH, VHB = "visual.healthlab", [(860, 1270)]
MC, MCB = "medcafee7d9", [(1260, 1640)]
SH, SHB = "sharingcozymoments", [(1260, 1500)]
RF = "rafaelgoncalves"
WH = ("whoosh", -0.06, 0.5); HIT = ("hit", 0.0, 0.5); ZAP = ("zap", 0.03, 0.35)
_pss = iter([3, 7, 11, 15, 19, 23, 5, 9, 13, 17, 21, 4, 8, 12, 16, 20, 6, 10, 14, 18, 22])
def PRES(row, w=0, leak=None, tight=False, **kw):
    """presenter medium close-up (reference: lab presenter, face ~25% from top, cut mid-torso)."""
    z = (1.28, 1.33) if tight else (1.16, 1.21)
    fx = {"fx": 0.42, "zoom": z, "zc": (540, 560)}
    if leak is not None: fx["leak"] = leak
    return S(row, w, src=152, ss=next(_pss), fx=fx, **kw)
def NUM(row, n, src, ss, **c): return S(row, 0, src=src, ss=ss, card={"type": "numpanel", "n": n, "at": 0.5, **c}, nocap=True, sfx=[WH, ("hit", 0.0, 0.35)])
SERIF = [{"kind": "serif", "text": "DON'T BUY", "x": 400, "y": 520, "t0": 0.0},
         {"kind": "serif", "text": "YOUR NEXT", "x": 660, "y": 790, "t0": 0.5},
         {"kind": "serif", "text": "PAIR", "red": True, "x": 270, "y": 990, "t0": 0.9},
         {"kind": "serif", "text": "OF SHOES", "x": 520, "y": 1190, "t0": 1.2}]

SHOTS = [
    # 01 ─ ref #1 anatomy-on-body + red hook box │ #2 serif build over held shoe, rack-blur │ #3 grimace w/ red │ #4 anatomy close
    S(1, 0, src=347, ss=0.3, fx={"nerve": {"kf": [(0.5, [(540, 1250), (610, 1450), (665, 1660), (690, 1920)]), (2.5, [(500, 1110), (565, 1320), (630, 1570), (650, 1920)])], "start": 0.0, "band": 90},
      "glows": [{"c": (540, 1220), "r": 200, "i": 0.8}], "zoom": (1.0, 1.06), "zc": (540, 1300), "flash": 0.7}, tags=[{"kind": "hook", "text": "IF YOU HAVE SCIATICA", "y": 892}], nocap=True, sfx=[ZAP]),
    S(1, "don", src=138, ss=2.0, fx={"blur_ramp": (1.0, 9.0, 1.4), "zoom": (1.05, 1.12), "zc": (540, 1300)}, tags=SERIF, nocap=True, sfx=[WH]),
    S(1, "just", src=359, ss=2.5, fx={"glows": [{"c": (700, 980), "r": 190, "i": 1.0}], "sparks": [{"c": (700, 980), "R": 240}], "zoom": (1.0, 1.06)}, sfx=[ZAP]),
    S(1, "best", src=VH, ss=5.0, fx={"inpaint": VHB, "zoom": (1.05, 1.14), "zc": (540, 1050)}),
    # 02 ─ the three brands as FULL clips (hard cuts on the names)
    S(2, 0, src=382, ss=0.8, fx={"zoom": (1.0, 1.05)}, sfx=[WH]),
    S(2, "new", src=544, ss=13.0, fx={"zoom": (1.5, 1.55), "zc": (540, 1300)}, sfx=[WH]),
    S(2, "brooks", src=539, ss=12.4, fx={"zoom": (1.0, 1.04)}, sfx=[WH]),
    # 03 ─ ref #5-6 presenter (leak), punch-in
    PRES(3, 0, leak=0),
    PRES(3, "there", tight=True),
    # 04 ─ ref #7 older woman seated │ #8 walker / elderly walking
    S(4, 0, src=316, ss=0.5, fx={"zoom": (1.0, 1.05)}),
    S(4, "already", src=341, ss=5.0, fx={"zoom": (1.0, 1.06)}),
    S(4, "around", src=339, ss=0.3, fx={"zoom": (1.05, 1.1)}),
    # 05 ─ ref #9-10 NUMBER 1 card — full Hoka clip in panel
    NUM(5, 1, 382, 3.0),
    # 06 ─ ref #11 patient in the shoes (long hold) │ #12 presenter │ #13 walking in the shoes
    S(6, 0, src=382, ss=6.0, fx={"zoom": (1.08, 1.14), "zc": (540, 900)}),
    PRES(6, "think"),
    S(6, "feel", src=540, ss=40.0, fx={"fy": 0.0, "zoom": (1.3, 1.34), "zc": (540, 700)}),
    # 07 ─ ref #14-#18 anatomy montage: lightning leg │ skeleton spark │ 0.2 s flashes │ nerve down leg │ #19 woman
    S(7, 0, src=358, ss=2.0, fx={"nerve": {"pts": [(330, 1090), (370, 1330), (410, 1600), (440, 1920)], "start": 0.0, "band": 80}, "sparks": [{"c": (330, 1090)}], "zoom": (1.0, 1.06)}, sfx=[ZAP]),
    S(7, "shooting", src=VH, ss=43.0, fx={"inpaint": VHB, "zoom": (1.05, 1.12), "sparks": [{"c": (540, 1150), "R": 300}]}),
    S(7, "down", src=MC, ss=19.2, fx={"inpaint": MCB, "zoom": (1.1, 1.15)}),
    S(7, "your", src=SH, ss=50.2, fx={"inpaint": SHB, "zoom": (1.0, 1.05)}),
    S(7, "leg", src=282, ss=1.0, fx={"nerve": {"pts": [(700, 330), (725, 640), (705, 900), (690, 1150)], "start": 0.0, "band": 70, "root_r": 100}, "zoom": (1.0, 1.1), "zc": (700, 700)}, sfx=[ZAP]),
    S(7, "understandable", src=240, ss=0.3, fx={"zoom": (1.0, 1.06)}),
    S(7, "something", src=234, ss=0.5, fx={"zoom": (1.0, 1.06)}),
    # 08 ─ ref #27 presenter
    PRES(8, 0),
    # 09-11 ─ ref #28-31 women moving at home / outdoors
    S(9, 0, src=311, ss=0.5, fx={"zoom": (1.0, 1.1), "zc": (540, 1500)}),
    S(9, "feel", src=301, ss=2.0, fx={"zoom": (1.0, 1.06)}),
    S(10, 0, src=278, ss=2.0, fx={"zoom": (1.0, 1.06)}),
    S(11, 0, src=346, ss=1.0, fx={"zoom": (1.0, 1.06)}),
    S(11, "store", src=204, ss=1.0, fx={"zoom": (1.0, 1.05)}),
    # 12-13 ─ ref #33 woman struggling at home │ presenter
    S(12, 0, src=310, ss=3.0, fx={"zoom": (1.05, 1.12)}),
    S(12, "unsteady", src=340, ss=5.0, fx={"zoom": (1.0, 1.06)}),
    PRES(12, "don"),
    S(13, 0, src=342, ss=0.5, fx={"zoom": (1.0, 1.06)}),
    # 14 ─ ref #32 NUMBER 2 — full New Balance clip
    NUM(14, 2, 383, 1.0),
    # 15-17 ─ ref #34-#38 on-feet close-ups, finger on the upper
    S(15, 0, src=383, ss=3.0, fx={"zoom": (1.0, 1.08)}),
    S(15, "sensible", src=544, ss=8.0, fx={"zoom": (1.7, 1.8), "zc": (540, 1400)}),
    S(16, 0, src=383, ss=6.0, fx={"zoom": (1.05, 1.12)}),
    PRES(16, "tell"),
    S(16, "right", src=383, ss=12.5, fx={"zoom": (1.15, 1.25), "zc": (540, 1300)}),
    S(17, 0, src=383, ss=13.5, fx={"zoom": (1.35, 1.5), "zc": (560, 1350)}),
    # 18 ─ ref #20-23 anatomy-in-shoe → generic toe-crowding animation
    S(18, 0, src=106, ss=1.5, fx={"zoom": (1.0, 1.05)}),
    S(18, "pressing", src=106, ss=5.0, fx={"zoom": (1.05, 1.12), "zc": (540, 1100)}),
    S(19, 0, src=383, ss=8.0, fx={"zoom": (1.25, 1.35), "zc": (540, 1300)}),
    S(19, "or", src=310, ss=0.8, fx={"zoom": (1.05, 1.12)}),
    PRES(20, 0),
    S(20, "widths", src=383, ss=14.5, fx={"zoom": (1.0, 1.08)}),
    S(20, "pair", src=544, ss=22.0, fx={"zoom": (1.7, 1.8), "zc": (540, 1400)}),
    S(20, "completely", src=310, ss=12.0, fx={"zoom": (1.0, 1.06)}),
    # 21 ─ ref #40-#43 anatomy: numb glitter foot │ long red nerve render │ presenter │ woman with red spine
    S(21, 0, src=182, ss=6.0, fx={"nerve": {"pts": [(430, 1190), (380, 1430), (330, 1690), (300, 1920)], "start": 0.0}, "zoom": (1.0, 1.05)}, sfx=[ZAP]),
    S(21, "back", src=MC, ss=18.4, fx={"inpaint": MCB, "zoom": (1.05, 1.15), "zc": (540, 1000), "sparks": [{"c": (560, 1180), "R": 220}]}),
    S(21, "leg", src=121, ss=1.5, fx={"nerve": {"kf": [(1.0, [(250, 1240), (300, 1500), (320, 1700), (300, 1920)]), (5.0, [(330, 1050), (330, 1350), (330, 1640), (310, 1920)])], "start": 0.0}, "zoom": (1.0, 1.05)}),
    PRES(21, "last"),
    S(21, "shoe", src=VH, ss=38.6, fx={"inpaint": VHB, "zoom": (1.05, 1.12), "glows": [{"c": (540, 1000), "r": 160, "i": 0.5}]}),
    S(21, "rubbing", src=238, ss=2.0, fx={"zoom": (1.0, 1.06)}),
    # 22 ─ ref #32 VS card — full Brooks clips (Ghost 18 | Adrenaline GTS), labels per the creator's own clip
    S(22, 0, src="brooks_vs", ss=0.0, card={"type": "numpanel", "n": 3, "at": 0.55, "vs": [("Brooks Ghost", 280), ("Brooks Adrenaline\nGTS", 800)]}, nocap=True, sfx=[WH, ("hit", 0.0, 0.35)]),
    # 23-24 ─ ref #45 presenter │ #46 clinician+patient │ #47 finger on shoe │ #50 walking
    PRES(23, 0),
    S(23, "shortlist", src=374, ss=3.9, fx={"zoom": (1.0, 1.08)}),
    S(23, "someone", src=167, ss=60, fx={"fx": 0.62, "zoom": (1.05, 1.1)}),
    S(23, "invest", src=539, ss=10.3, fx={"zoom": (1.1, 1.15), "zc": (540, 1250)}),
    S(24, 0, src=374, ss=21.0, fx={"zoom": (1.0, 1.06)}),
    S(24, "shop", src=374, ss=24.0, fx={"zoom": (1.05, 1.1)}),
    PRES(24, "whole", leak=1),
    # 25-28 ─ everyday moments (ref #50-#54 walking/real life)
    S(25, 0, src=346, ss=4.0, fx={"zoom": (1.05, 1.12)}),
    S(26, 0, src=115, ss=0.5, fx={"zoom": (1.0, 1.06)}),
    S(27, 0, src=308, ss=0.5),
    S(27, "sitting", src=306, ss=0.5),
    S(27, "getting", src=336, ss=0.5),
    PRES(28, 0),
    S(29, 0, src=317, ss=2.0, fx={"zoom": (1.0, 1.08)}),
    S(29, "uncomfortable", src=314, ss=3.0, fx={"zoom": (1.0, 1.06)}),
    S(29, "brand", src=382, ss=11.0, fx={"zoom": (1.1, 1.16), "zc": (540, 900)}),
    S(29, "experience", src=383, ss=15.0, fx={"zoom": (1.0, 1.06)}),
    # 30 ─ ref #63-#65 the long presenter hold before the reveal
    PRES(30, 0, tight=True, sfx=[("whoosh", -0.2, 0.5)]),
    # 31 ─ ref #66 shoes top-down │ #67 on feet (name is in the caption box, as reference)
    S(31, 0, src=227, ss=2.0, fx={"zoom": (1.0, 1.06)}, sfx=[HIT]),
    S(31, "ortho", src=102, ss=8.0, fx={"zoom": (1.0, 1.06)}),
    # 32 ─ ref #68 presenter
    PRES(32, 0),
    S(32, "option", src=78, ss=0.5, fx={"zoom": (1.0, 1.06)}),
    PRES(32, "follow"),
    S(33, 0, src=76, ss=1.0, fx={"zoom": (1.0, 1.08)}),
    # 34-38 ─ ref #69-#77 feature section: animation-heavy, alternating with real demo
    S(34, 0, src=13, ss=3.0, fx={"outline": {"pts": [(100, 1300), (150, 900), (230, 560), (380, 300), (560, 250), (760, 320), (860, 560), (880, 900), (870, 1150)], "start": 0.2, "dur": 0.8}}),
    S(34, "room", src=16, ss=1.0, fx={"zoom": (1.0, 1.06)}),
    S(35, 0, src=23, ss=1.0, fx={"zoom": (1.0, 1.08)}),
    S(35, "forgiving", src=24, ss=1.0, fx={"zoom": (1.0, 1.06)}),
    S(36, 0, src=4, ss=1.0, fx={"zoom": (1.0, 1.08)}),
    S(36, "underneath", src=371, ss=2.0, fx={"zoom": (1.0, 1.05)}),
    S(36, "cushioning", src=7, ss=1.0, fx={"zoom": (1.0, 1.08)}),
    S(36, "soften", src=372, ss=1.2),
    S(37, 0, src=73, ss=0.5, fx={"zoom": (1.0, 1.08)}),
    S(37, "bulk", src=208, ss=19.0, fx={"zoom": (1.0, 1.05)}),
    S(37, "move", src=355, ss=1.0),
    S(38, 0, src=19, ss=2.0, fx={"zoom": (1.0, 1.08)}),
    S(38, "slip", src=350, ss=1.0, fx={"zoom": (1.0, 1.06)}),
    S(38, "grip", src=307, ss=0.5),
    S(39, 0, src=17, ss=1.0, fx={"zoom": (1.0, 1.06)}),
    S(39, "support", src=5, ss=2.0, fx={"zoom": (1.0, 1.06)}),
    S(39, "comfortable", src=329, ss=1.0, fx={"zoom": (1.0, 1.06)}),
    S(39, "afternoon", src=291, ss=2.0, fx={"zoom": (1.0, 1.06)}),
    # 40 ─ presenter │ ref #79-#84 B&W + big red X on the old-shoe struggle
    PRES(40, 0),
    S(40, "you", src=310, ss=0.8, fx={"bw": True, "zoom": (1.0, 1.04), "x": True, "x_at": 0.1}),
    S(40, "uncomfortable", src=312, ss=6.0, fx={"bw": True, "zoom": (1.0, 1.04), "x": True, "x_at": 0.1}),
    S(40, "demanding", src=310, ss=12.0, fx={"bw": True, "zoom": (1.04, 1.08), "x": True, "x_at": 0.1}),
    # 41-42 ─ ref #85-#96 slide-in, out the door, freedom montage, grocery, family
    S(41, 0, src=38, ss=5.0, fx={"zoom": (1.0, 1.06)}),
    S(41, "out", src=326, ss=1.0),
    S(41, "focus", src=268, ss=1.5),
    S(42, 0, src=114, ss=1.0),
    S(42, "lunch", src="hf_20261004_070629", ss=0.2, fx={"zoom": (1.0, 1.06)}),
    S(42, "afternoon", src="Picking up kids from park 02", ss=12.0, fx={"zoom": (1.0, 1.05)}),
    # 43 ─ ref #97 sofa │ #98 shoes on stairs │ #99 walking out
    S(43, 0, src=336, ss=0.5, fx={"zoom": (1.0, 1.05)}),
    S(43, "soft", src=382, ss=8.0, fx={"zoom": (1.0, 1.1)}),
    S(43, "take", src=301, ss=2.0, fx={"zoom": (1.0, 1.05)}),
    S(43, "fit", src=13, ss=3.0),
    S(43, "features", src=297, ss=0.5, fx={"zoom": (1.0, 1.05)}),
    # 44 ─ ref #100 top-down pair, caption 'at the link below', no end card
    S(44, 0, src=227, ss=5.0, fx={"zoom": (1.0, 1.08)}),
]

def caption_chunks(timing):
    """one caption per clause; long clauses split evenly into ≤4-word pieces (bigger V3 text = fewer words)."""
    chunks = []
    for r in timing.values():
        clauses, cur = [], []
        for w in r["words"]:
            cur.append(w)
            if w["w"][-1] in ".,?!:;": clauses.append(cur); cur = []
        if cur: clauses.append(cur)
        for cl in clauses:
            txt = " ".join(x["w"] for x in cl)
            n = 1 if (len(captions.wrap(txt)) <= 2 and len(cl) <= 5) else math.ceil(len(cl) / 4)
            cuts = [round(k * len(cl) / n) for k in range(n + 1)]
            for a_, b_ in zip(cuts, cuts[1:]):
                part = cl[a_:b_]
                chunks.append({"s": part[0]["s"], "e": part[-1]["e"], "text": re.sub(r"[.,;:]$", "", " ".join(x["w"] for x in part))})
    for a, b in zip(chunks, chunks[1:]): a["e"] = b["s"] if b["s"] - a["e"] < 0.6 else a["e"] + 0.25
    chunks[-1]["e"] += 0.5
    return chunks


# ── presenter in-points: only windows of #152 where he talks to camera with nothing in his hands
_WIN = [(3.4, 7.5), (9.8, 14.6), (19.4, 21.4), (26.8, 29.4), (43.2, 47.6), (50.6, 55.4), (85.6, 89.4)]
def _assign_presenter():
    def start(sh):
        r = _t[sh["row"]]; return 0.0 if (sh["row"] == 1 and sh["w"] == 0) else r["words"][sh["w"]]["s"] - 0.03
    end_all = max(r["end"] for r in _t.values()) + 2.6
    win = [list(w) for w in _WIN]; k = 0
    for i, sh in enumerate(SHOTS):
        if sh.get("src") != 152: continue
        dur = (start(SHOTS[i + 1]) if i + 1 < len(SHOTS) else end_all) - start(sh) + 0.1
        for _ in range(len(win)):
            a, b = win[k % len(win)]
            if b - a >= dur: sh["ss"] = round(a, 2); win[k % len(win)][0] = a + dur; k += 1; break
            k += 1
        else:   # all windows used: start again with fresh in-points (offset so repeats aren't identical frames)
            win = [[a + 0.5, b] for a, b in _WIN]; a, b = next(w for w in win if w[1] - w[0] >= dur)
            sh["ss"] = round(a, 2); [w for w in win if w[0] == a][0][0] = a + dur
_assign_presenter()
