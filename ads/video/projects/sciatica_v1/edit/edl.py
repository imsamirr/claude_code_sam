"""Shot list for ComfortWear Sciatica V1 (brief: ComfortWear_Sciatica_Creative_Brief.md, 44 rows).

Each shot: row, w (cut on this word: index or a word prefix), src (catalogue id or tiktok/asset name substring) + ss
(source in-point, s), fx (zoom, nerve, glows, outline, crop focus fx/fy, z, speed, bw, key, flash...), tags (on-screen
emphasis overlays), card (full-frame graphic), cap_y (caption centre y), nocap, sfx [(kind, t_local)].
Aggressive sciatica visuals (nerve lightning, red glows, anatomy) are ONLY on symptom lines (rows 01, 07, 21) and never
next to a competitor shoe or after the ComfortWear reveal.
"""
import json
from pathlib import Path
G = Path(__file__).resolve().parent / "gfx"
_t = {r["row"]: r for r in json.load(open(Path(__file__).resolve().parent / "vo_timing.json"))}

def W(row, word, nth=1):
    """index of the nth word in `row` that starts with `word` (case-insensitive, punctuation ignored)."""
    k = 0
    for i, w in enumerate(_t[row]["words"]):
        if w["w"].lower().strip(".,?!:;’'\"").startswith(word.lower()):
            k += 1
            if k == nth: return i
    raise KeyError(f"row {row}: {word}")

def S(row, w=0, **kw):
    return {"row": row, "w": W(row, w) if isinstance(w, str) else w, **kw}

ILLU = {"text": "Illustration", "style": "small", "x": 40, "y": 1760, "align": "l", "pop": False}
LUMBAR_347 = [(0.5, [(540, 1250), (610, 1450), (665, 1660), (690, 1920)]),
              (2.5, [(500, 1110), (565, 1320), (630, 1570), (650, 1920)]),
              (4.5, [(530, 1170), (600, 1390), (675, 1630), (700, 1920)])]

def feat(text): return {"text": text, "style": "blue", "y": 330}

SHOTS = [
    # 01 ─ HOOK: symptom recognition, aggressive nerve visual on a real body (no shoes in frame)
    S(1, 0, src=347, ss=0.3, fx={"nerve": {"kf": LUMBAR_347, "start": 0.10, "band": 80}, "zoom": (1.0, 1.08), "zc": (540, 1300), "flash": 0.8},
      tags=[{"text": "IF YOU HAVE SCIATICA", "style": "hook", "y": 520, "t0": 0.05}], nocap=True, sfx=[("zap", 0.08), ("hit", 0.08)]),
    S(1, "don", src=168, ss=10, fx={"fx": 0.28, "zoom": (1.05, 1.12)}, tags=[{"text": "BEFORE YOUR\nNEXT PAIR", "style": "white", "y": 360}]),
    S(1, "best", src=336, ss=4.0, fx={"nerve": {"kf": [(4.0, [(560, 1250), (590, 1480), (610, 1700), (620, 1920)]), (7.0, [(690, 1290), (705, 1520), (720, 1720), (730, 1920)])], "start": 0.06, "intensity": 0.9}, "zoom": (1.06, 1.0)},
      cap_y=760, sfx=[("zap", 0.05)]),
    # 02 ─ three packshots on identical neutral background, hard cuts on the brand names
    S(2, 0, card={"type": "pack", "img": G / "cut_hoka_a.png", "brand": "HOKA"}, nocap=True, sfx=[("whoosh", -0.05)]),
    S(2, "new", card={"type": "pack", "img": G / "cut_nb_b2.png", "brand": "NEW BALANCE"}, nocap=True, sfx=[("whoosh", -0.05)]),
    S(2, "brooks", card={"type": "pack", "img": G / "pack_brooks.png", "brand": "BROOKS", "feather": True}, nocap=True, sfx=[("whoosh", -0.05)]),
    # 03 ─ money + 3 criteria card
    S(3, 0, src=289, ss=0.5, fx={"zoom": (1.0, 1.1)}, cap_y=1450),
    S(3, "three", card={"type": "criteria", "at": [0.25, 0.75, 1.25]}, cap_y=1600, sfx=[("whoosh", 0.0)]),
    # 04 ─ over sixty, planning the day
    S(4, 0, src=290, ss=1.0, fx={"zoom": (1.0, 1.06)}, cap_y=1450),
    S(4, "planning", src=286, ss=2.0, fx={"zoom": (1.05, 1.12)}, cap_y=1450),
    S(4, "stay", src=339, ss=0.2, fx={"zoom": (1.0, 1.06)}, tags=[{"text": "COMFORT FOR\nYOUR EVERYDAY", "style": "white", "y": 360, "t0": 0.2}], cap_y=1450),
    # 05 ─ NUMBER 1 / HOKA
    S(5, 0, card={"type": "number", "n": 1, "brand": "HOKA", "imgs": [(G / "cut_hoka_a.png", None)]}, nocap=True, sfx=[("whoosh", -0.1), ("hit", 0.05)]),
    # 06 ─ cushioning (accurate, no altered sole)
    S(6, 0, src=382, ss=2.0, fx={"zoom": (1.0, 1.12), "zc": (540, 900)}, tags=[{"text": "CUSHIONING", "style": "white", "y": 330}], cap_y=1500),
    S(6, "that", src=382, ss=7.0, fx={"zoom": (1.12, 1.2), "zc": (540, 900)}, cap_y=1500),
    # 07 ─ symptom context: shooting pain down the leg (aggressive, separate from any shoe)
    S(7, 0, src="visual.healthlab", ss=45.2, fx={"zoom": (1.1, 1.18), "zc": (540, 1100), "glows": [{"c": (560, 1150), "r": 170, "i": 0.6}]}, tags=[ILLU], cap_y=1100),
    S(7, "shooting", src=282, ss=1.0, fx={"nerve": {"pts": [(700, 330), (725, 640), (705, 900), (690, 1150)], "start": 0.05, "band": 60, "root_r": 90}, "zoom": (1.0, 1.1), "zc": (700, 700)},
      cap_y=1450, sfx=[("zap", 0.04)]),
    S(7, "leg", src=240, ss=0.2, fx={"zoom": (1.0, 1.06)}, cap_y=600),
    S(7, "understandable", src=306, ss=1.0, fx={"zoom": (1.0, 1.08)}, tags=[{"text": "LOOKING FOR\nCOMFORT", "style": "white", "y": 230}], cap_y=1500),
    # 08 ─ first explanatory reset (clinic)
    S(8, 0, src=167, ss=60, fx={"fx": 0.68, "zoom": (1.08, 1.16)}, tags=[{"text": "SOFTNESS IS\nONE PART", "style": "white", "y": 360, "t0": 0.6}], cap_y=1450),
    # 09-11 ─ movement checks
        S(9, 0, src=311, ss=0.5, fx={"zoom": (1.0, 1.1), "zc": (540, 1500)}, cap_y=1450),
    S(10, 0, src=278, ss=2.0, fx={"zoom": (1.0, 1.06)}, cap_y=1450),
    S(11, 0, src=346, ss=1.0, fx={"zoom": (1.0, 1.06)}, tags=[{"text": "REAL-LIFE\nMOVEMENT", "style": "white", "y": 360}], cap_y=1450),
    S(11, "store", src=204, ss=1.0, fx={"zoom": (1.0, 1.05)}, cap_y=1450),
    # 12-13 ─ your fit matters
    S(12, 0, src=168, ss=30, fx={"fx": 0.3, "zoom": (1.08, 1.14)}, cap_y=1450),
    S(12, "don", src=310, ss=3.0, fx={"zoom": (1.05, 1.12)}, tags=[{"text": "YOUR FIT\nMATTERS", "style": "white", "y": 360}], cap_y=1450),
    S(13, 0, src=342, ss=0.5, fx={"zoom": (1.0, 1.06)}, tags=[{"text": "THROUGH\nYOUR DAY", "style": "white", "y": 360}], cap_y=1450),
    # 14 ─ NUMBER 2 / NEW BALANCE
    S(14, 0, card={"type": "number", "n": 2, "brand": "NEW BALANCE", "imgs": [(G / "cut_nb_b2.png", None)]}, nocap=True, sfx=[("whoosh", -0.1), ("hit", 0.05)]),
    S(15, 0, src=544, ss=8.0, fx={"zoom": (1.7, 1.8), "zc": (540, 1400)}, cap_y=1500),
    S(15, "sensible", src=383, ss=9.0, fx={"zoom": (1.0, 1.06)}, cap_y=1450),
    S(16, 0, src=543, ss=24.0, fx={"zoom": (1.0, 1.1)}, cap_y=1215),
    S(16, "right", src=383, ss=12.5, fx={"zoom": (1.1, 1.2), "zc": (540, 1300)}, tags=[{"text": "CHECK THE FIT", "style": "white", "y": 330}], cap_y=700),
    S(17, 0, src=383, ss=13.5, fx={"zoom": (1.3, 1.45), "zc": (560, 1350)}, cap_y=700),
    S(18, 0, card={"type": "fit"}, cap_y=1730),
    S(19, 0, src=195, ss=0.5, fx={"zoom": (1.0, 1.08)}, cap_y=1450),
    S(19, "loosening", src=276, ss=3.0, fx={"zoom": (1.0, 1.06)}, cap_y=1500),
    S(20, 0, src=383, ss=3.0, fx={"zoom": (1.0, 1.08)}, tags=[{"text": "MODEL + WIDTH + FIT", "style": "white", "y": 330}], cap_y=1450),
    S(20, "pair", src=544, ss=22.0, fx={"zoom": (1.7, 1.8), "zc": (540, 1400)}, tags=[{"text": "MODEL + WIDTH + FIT", "style": "white", "y": 330, "pop": False}], cap_y=1500),
    # 21 ─ symptom context again (aggressive), then local foot comfort only
    S(21, 0, src=121, ss=1.0, fx={"nerve": {"kf": [(1.0, [(250, 1240), (300, 1500), (320, 1700), (300, 1920)]), (5.0, [(330, 1050), (330, 1350), (330, 1640), (310, 1920)])], "start": 0.05}, "zoom": (1.0, 1.05)},
      cap_y=700, sfx=[("zap", 0.04)]),
    S(21, "back", src="visual.healthlab", ss=39.2, fx={"zoom": (1.08, 1.14), "zc": (540, 1100), "glows": [{"c": (540, 1150), "r": 150, "i": 0.5}]}, tags=[ILLU], cap_y=1100),
    S(21, "last", src=316, ss=1.0, fx={"zoom": (1.0, 1.06)}, cap_y=1450),
    S(21, "pressure", src=312, ss=6.0, fx={"zoom": (1.05, 1.12)}, tags=[{"text": "AVOID PRESSURE\n& RUBBING", "style": "white", "y": 360}], cap_y=1450),
    # 22 ─ NUMBER 3 / BROOKS (Ghost 18 + Adrenaline GTS 25)
    S(22, 0, card={"type": "number", "n": 3, "brand": "BROOKS", "imgs": [(G / "brooks_ghost18.png", "Ghost 18"), (G / "brooks_adrenaline.png", "Adrenaline GTS 25")]}, nocap=True, sfx=[("whoosh", -0.1), ("hit", 0.05)]),
    S(23, 0, src=374, ss=4.0, fx={"zoom": (1.0, 1.08)}, tags=[{"text": "A COMMON\nSHORTLIST", "style": "white", "y": 360}], cap_y=1450),
    S(23, "invest", src=539, ss=45.0, fx={"zoom": (1.75, 1.85), "zc": (540, 1450)}, cap_y=1650),
    S(24, 0, src=374, ss=15.0, fx={"zoom": (1.0, 1.06)}, cap_y=1450),
    S(24, "whole", src=170, ss=3.0, fx={"fx": 0.57, "zoom": (1.1, 1.16)}, tags=[{"text": "MORE THAN A\nQUICK TRY-ON", "style": "white", "y": 360}], cap_y=1450),
    # 25-28 ─ everyday moments
    S(25, 0, src=346, ss=4.0, fx={"zoom": (1.05, 1.12)}, cap_y=1500),
    S(26, 0, src=115, ss=0.5, fx={"zoom": (1.0, 1.06)}, cap_y=1500),
    S(27, 0, src=308, ss=0.5, tags=[{"text": "WALK", "style": "white", "y": 330}], cap_y=1500),
    S(27, "sitting", src=306, ss=0.5, tags=[{"text": "SIT", "style": "white", "y": 330}], cap_y=1500),
    S(27, "getting", src=297, ss=0.5, tags=[{"text": "STAND", "style": "white", "y": 330}], cap_y=1500),
    S(28, 0, src=167, ss=229, fx={"fx": 0.38, "zoom": (1.05, 1.1)}, tags=[{"text": "YOUR EVERYDAY\nROUTINE", "style": "white", "y": 360}], cap_y=1450),
    S(29, 0, src=317, ss=2.0, fx={"zoom": (1.0, 1.08)}, tags=[{"text": "10 MINUTES → LATER", "style": "white", "y": 330, "t0": 0.8}], cap_y=1500),
    S(29, "brand", src=543, ss=24.6, fx={"zoom": (1.0, 1.1)}, tags=[{"text": "HOW DO THEY\nFEEL LATER?", "style": "white", "y": 360}], cap_y=1500),
    # 30 ─ THE TURN (music lift)
    S(30, 0, src=170, ss=4.0, fx={"fx": 0.57, "zoom": (1.1, 1.18)}, tags=[{"text": "WHAT ABOUT\nCOMFORTWEAR?", "style": "blue", "y": 380}], cap_y=1450, sfx=[("whoosh", -0.2)]),
    # 31 ─ product name, hero (actual Ortho Stretch)
    S(31, 0, src=215, ss=0.3, fx={"zoom": (1.0, 1.1)},
      tags=[{"text": "COMFORTWEAR", "style": "dark", "y": 330, "t0": 0.1}, {"text": "ORTHO STRETCH\nCUSHION SHOES", "style": "white", "y": 480, "t0": 0.35}], nocap=True, sfx=[("hit", 0.02)]),
    # 32 ─ the treatment distinction: neutral visuals, full caption, unhurried
    S(32, 0, src=78, ss=0.5, fx={"zoom": (1.0, 1.06)}, tags=[{"text": "EVERYDAY FOOT\nCOMFORT", "style": "blue", "y": 380, "t0": 3.4}], cap_y=1450),
    S(32, "follow", src=168, ss=150, fx={"fx": 0.3, "zoom": (1.05, 1.1)}, tags=[{"text": "EVERYDAY FOOT\nCOMFORT", "style": "blue", "y": 380, "pop": False}], cap_y=1450),
    S(33, 0, src=76, ss=1.0, fx={"zoom": (1.0, 1.08)}, tags=[{"text": "LET'S LOOK CLOSER", "style": "white", "y": 330}], cap_y=1500),
    # 34-38 ─ feature demonstrations on the actual shoe, blue labels, cut on the feature word
    S(34, 0, src=13, ss=3.0, fx={"outline": {"pts": [(100, 1300), (150, 900), (230, 560), (380, 300), (560, 250), (760, 320), (860, 560), (880, 900), (870, 1150)], "start": 0.25, "dur": 0.8}},
      tags=[feat("WIDE TOE BOX")], cap_y=1650),
    S(34, "room", src=16, ss=1.0, fx={"zoom": (1.0, 1.06)}, tags=[feat("WIDE TOE BOX")], cap_y=1500),
    S(35, 0, src=23, ss=1.0, fx={"zoom": (1.0, 1.08)}, tags=[feat("STRETCHY KNIT UPPER")], cap_y=1500),
    S(35, "forgiving", src=24, ss=1.0, fx={"zoom": (1.0, 1.06)}, tags=[feat("STRETCHY KNIT UPPER")], cap_y=1500),
    S(36, 0, src=4, ss=1.0, fx={"zoom": (1.0, 1.08)}, tags=[feat("ARCH SUPPORT")], cap_y=1500),
    S(36, "cushioning", src=7, ss=1.0, fx={"zoom": (1.0, 1.08)}, tags=[feat("HEEL CUSHIONING")], cap_y=1500),
    S(36, "soften", src=343, ss=0.5, fx={"zoom": (1.0, 1.05)}, tags=[feat("HEEL CUSHIONING")], cap_y=1500),
    S(37, 0, src=73, ss=0.5, fx={"zoom": (1.0, 1.08)}, tags=[feat("LIGHTWEIGHT DESIGN")], cap_y=1500),
    S(37, "move", src=355, ss=1.0, tags=[feat("LIGHTWEIGHT DESIGN")], cap_y=1500),
    S(38, 0, src=19, ss=2.0, fx={"zoom": (1.0, 1.08)}, tags=[feat("BREATHABLE KNIT")], cap_y=1500),
    S(38, "slip", src=350, ss=1.0, fx={"zoom": (1.0, 1.06)}, tags=[feat("SLIP-RESISTANT OUTSOLE")], cap_y=1500),
    S(38, "everyday", src=307, ss=0.5, tags=[feat("SLIP-RESISTANT OUTSOLE")], cap_y=1500),
    # 39 ─ recap
    S(39, 0, src=17, ss=1.0, fx={"zoom": (1.0, 1.06)}, tags=[{"text": "ROOM", "style": "blue", "y": 330}], cap_y=1500),
    S(39, "support", src=5, ss=2.0, fx={"zoom": (1.0, 1.06)}, tags=[{"text": "SUPPORT", "style": "blue", "y": 330}], cap_y=1500),
    S(39, "comfortable", src=329, ss=1.0, fx={"zoom": (1.0, 1.06)}, tags=[{"text": "COMFORT", "style": "blue", "y": 330}], cap_y=1500),
    # 40-42 ─ emotional bridge + lifestyle (no pain imagery after the reveal)
    S(40, 0, src=167, ss=36, fx={"fx": 0.62, "zoom": (1.05, 1.1)}, cap_y=1450),
    S(40, "uncomfortable", src=305, ss=1.0, fx={"zoom": (1.0, 1.06)}, tags=[{"text": "ONE LESS\nDISTRACTION", "style": "white", "y": 360}], cap_y=1500),
    S(41, 0, src=327, ss=3.0, fx={"zoom": (1.0, 1.06)}, cap_y=1500),
    S(41, "out", src=326, ss=1.0, tags=[{"text": "GET ON WITH\nYOUR DAY", "style": "white", "y": 360}], cap_y=1500),
    S(41, "focus", src=342, ss=3.0, cap_y=1500),
    S(42, 0, src=204, ss=0.5, tags=[{"text": "GROCERIES", "style": "white", "y": 330}], cap_y=1500),
    S(42, "lunch", src="hf_20261004_070629", ss=0.2, fx={"zoom": (1.0, 1.06)}, tags=[{"text": "LUNCH", "style": "white", "y": 330}], cap_y=1500),
    S(42, "afternoon", src="Picking up kids from park 02", ss=12.0, fx={"zoom": (1.0, 1.05)}, tags=[{"text": "FAMILY TIME", "style": "white", "y": 330}], cap_y=1500),
    # 43 ─ recap criteria
    S(43, 0, src=303, ss=1.0, fx={"zoom": (1.0, 1.06)}, tags=[{"text": "LOOK AT THE\nFIT & FEATURES", "style": "white", "y": 360, "t0": 4.5}], cap_y=1450),
    S(43, "soft", src=382, ss=8.0, fx={"zoom": (1.0, 1.1)}, cap_y=1500),
    S(43, "take", src=16, ss=3.0, tags=[{"text": "LOOK AT THE\nFIT & FEATURES", "style": "white", "y": 360, "pop": False}], cap_y=1500),
    S(43, "fit", src=23, ss=3.0, tags=[{"text": "LOOK AT THE\nFIT & FEATURES", "style": "white", "y": 360, "pop": False}], cap_y=1500),
    S(43, "features", src=7, ss=3.0, tags=[{"text": "LOOK AT THE\nFIT & FEATURES", "style": "white", "y": 360, "pop": False}], cap_y=1500),
    # 44 ─ CTA: actual shoe, product name, single CTA, held after VO
    S(44, 0, src=79, ss=0.5, fx={"zoom": (1.0, 1.1), "zc": (540, 900)}, nocap=True,
      tags=[{"text": "COMFORTWEAR", "style": "dark", "y": 330}, {"text": "ORTHO STRETCH\nCUSHION SHOES", "style": "white", "y": 480},
            {"text": "TAP TO SHOP ↓", "style": "blue", "y": 1520, "t0": 1.2}]),
]
