"""COM459 (Japan) shot list. Built from StefanBrain's director's cut (edit/sb_shots.json, parsed from
STEFANBRAIN_DIRECTION_COM459.md): one EDL shot per StefanBrain shot, anchored on the first VO words it covers.
Footage: Japan TikTok UGC (edit/sourcing_{A,B,C}.json), COM458 Hoka/On clips, Drive product library (via ../sciatica_v1),
gen/ (AI podiatrist lip-synced = Kie Kling avatar; 3D foam/toe animations from COM458), COM376 offer stickers + end card.
Pacing rules: research/scene_pacing_top_ads.md (≈5 VO words per shot, continuous takes only, min 1.2 s)."""
import json, re
from pathlib import Path
E = Path(__file__).resolve().parent; P = E.parent
MUSIC_DB = -13.0
R376 = "reference/COM376_HO1.mp4"
norm = lambda x: re.sub(r"[^a-z0-9']", "", x.lower())

SB = json.load(open(E / "sb_shots.json"))
SRC = {}
for g in "ABC":
    f = E / f"sourcing_{g}.json"
    if f.exists():
        for x in json.load(open(f)):
            if x.get("file"): SRC[str(x["shot"])] = (x["file"], float(x.get("in") or 0), x)
WORDS = {}
for take in ("H1", "H2", "H3", "body"):
    for sec, ws in json.load(open(E / "vo3" / f"{take}_final.json"))["sections"].items(): WORDS[sec] = ws
DOC = json.load(open(P / "gen" / "doctor_lines.json"))          # name: [take, sec, first, last, s0, s1]

LIB = {4: "assets/lib/01_Cushion and Arch Support/OSCS_Arch Support 02.mov", 5: "assets/lib/01_Cushion and Arch Support/OSCS_Arch Support 04.MOV",
       7: "assets/lib/01_Cushion and Arch Support/OSCS_Cushion 01.MOV", 8: "assets/lib/01_Cushion and Arch Support/OSCS_Nurse_Arch Support 01.MOV",
       12: "assets/lib/02_Wide Toe Box/OSCS_Nurse_Wide Toe Box 01.MOV", 13: "assets/lib/02_Wide Toe Box/OSCS_Wide Toe Box 01.mov",
       16: "assets/lib/02_Wide Toe Box/OSCS_Wide Toe Box 04.mov", 23: "assets/lib/03_Adaptive Stretch Fabric/OSCS_Fabric 01.MOV",
       24: "assets/lib/03_Adaptive Stretch Fabric/OSCS_Fabric 02.MOV", 25: "assets/lib/04_Slip-resistant/OSCS_Nurse_Slip Resistant 01.MOV",
       27: "assets/lib/04_Slip-resistant/OSCS_Slip Resistant 03.MOV", 28: "assets/lib/04_Slip-resistant/OSCS_Slip resistant 01.mp4",
       34: "assets/lib/05_Slip On/OSCS_Nurse_Slip on 01.MOV", 78: "assets/lib/07_Montage/Larissa_Mom_Showing 3 OSCS.MOV",
       101: "assets/lib/09_Lifestyle/Larissa_Mom_Wearing shoes 01.MOV", 102: "assets/lib/09_Lifestyle/OSCS_Wearing Shoes 01.mov",
       187: "assets/misc/Nurses/Broll nurse in CW shoes doing tiptoe, hop, walk in place .MOV",
       190: "assets/misc/Nurses/Broll nurse pushing an elderly in a wheelchair while wearing CW shoes.MOV",
       191: "assets/misc/Nurses/Broll nurse showing insole the shoes.MOV", 193: "assets/misc/Nurses/Broll nurse topview walking out side.MOV",
       227: "assets/misc/Others/Broll topview of the shoes.MOV", 343: "assets/misc/Seniors/Broll senior walking outside with CW shoes on.mov",
       350: "assets/misc/Seniors/Broll showing outsole of the shoes while being worn.mov", 355: "assets/misc/Seniors/Broll topview walking outside in black CW shoes.MOV",
       371: "assets/misc/sole new final.mp4", 373: "assets/misc/website showing 40_ off and products .MOV"}

# StefanBrain PRODUCT / ANIMATION / un-generated AI shots -> our footage  (src, in-point, extra)
OWN = {
 "P2.9": ("gen/anim_foam.mp4", 0.3, {}), "P2.12": ("gen/anim_foam.mp4", 1.6, {"z": 1.15}), "P2.13": ("gen/anim_foam.mp4", 2.4, {}),
 "P2.14": ("gen/anim_foam.mp4", 3.2, {"z": 1.08}),
 "P3.19": (LIB[27], 3.0, {}), "P3.20": (LIB[28], 3.0, {}), "P3.21": (LIB[350], 0.5, {}),
 "P4.8": ("gen/anim_toes.mp4", 0.3, {}), "P4.9": ("gen/anim_toes.mp4", 2.4, {}), "P4.13": ("gen/anim_toes.mp4", 3.6, {"z": 1.12}),
 "P5.1": (LIB[102], 8.0, {}), "P5.2": (LIB[78], 1.0, {}), "P5.4": (LIB[34], 3.0, {}), "P5.5": (LIB[190], 5.0, {}), "P5.6": (LIB[190], 15.0, {}),
 "P5.9": (LIB[12], 10.0, {}), "P5.10": (LIB[16], 1.0, {}), "P5.12": (LIB[23], 1.0, {}), "P5.13": (LIB[24], 1.0, {}), "P5.14": (LIB[193], 6.0, {}),
 "P5.15": (LIB[191], 15.0, {}), "P5.16": (LIB[371], 1.5, {}), "P5.17": (LIB[355], 1.0, {}), "P5.18": (LIB[25], 6.0, {}), "P5.20": (LIB[28], 6.0, {}),
 "P6.15": (LIB[187], 18.0, {}),
 "P7.1": (LIB[227], 2.0, {}), "P7.2": (R376, 122.85, {"nocap": True, "z": 1.0}), "P7.3": (R376, 124.05, {"nocap": True, "z": 1.0}),
 "P7.4": (LIB[373], 2.0, {"keep_text": True}), "P7.5": (R376, 125.0, {"nocap": True, "z": 1.0, "fx": {"speed": 0.8, "zoom": (1.0, 1.0)}}),
 "P7.6": (LIB[101], 3.0, {}), "P7.7": (LIB[343], 1.0, {}), "P7.8": (LIB[355], 4.0, {}), "P7.10": (LIB[13], 3.0, {}), "P7.11": (LIB[102], 3.0, {}),
 "P7.12": (LIB[78], 4.0, {}), "P7.13": (LIB[227], 6.0, {}), "P7.14": (LIB[78], 7.0, {}),
}
# AI podiatrist (lip-synced clips in gen/): StefanBrain AI shots we generated
DOCSHOT = {"H1.3": "D_H1", "H1.5": "D_H1", "H2.5": "D_H2", "H3.4": "D_H3", "P1.14": "D_P1", "P2.2": "D_P2", "P3.13": "D_P3", "P4.11": "D_P4"}
DOC_FROM = {"H2.5": "take them out"}          # doctor covers the whole line "take them out of your suitcase right now."
SKIP = {"H2.4"}                              # (merged into the doctor line above)
LP = "../com458/tiktok/nyc_hoods/lonelyplanet_7489594060038999302.mp4"     # its iPhone Health / watch screens (COM458)
FALLBACK = {   # sourcing gaps -> (file, in), or None = no shot (previous scene holds longer, which also slows the pace)
 "P1.2": None, "P1.4": (LP, 89.9), "H3.7": None,      # LP 4-9 s is a fast montage (no clean take for the watch)
 # de-duplicate windows that two sourcing groups picked from the same clip
 "H1.4": ("../com458/tiktok/hoka/nichos.home_7551553313515261198.mp4", 67.0), "P3.17": ("tiktok/jp_stairs/jin1495__7474470941687418119.mp4", 5.0),
 "P6.7": ("tiktok/jp_pain/taylortakesprague_7364318564121087275.mp4", 8.0), "P4.12": ("tiktok/jp_pain/mvshelle_7528084781142166814.mp4", 3.5),
 "P7.9": ("tiktok/jp_pack/rileejsmith_7564913888785960222.mp4", 150.0), "P3.14": ("../com458/tiktok/oncloud/cchungy__7214168808423050538.mp4", 2.0),
 "P3.12": ("tiktok/jp_winter/kaaatastrophe_7368524673115589893.mp4", 40.0),
 "P1.12": None, "P2.6": None, "P2.15": None, "P4.14": None, "P5.19": None, "P6.6": None, "P6.8": None, "P6.9": None,
}

HOOK_TEXT = {"H1": (("HOKAS & ON CLOUDS",), ("ARE THE WORST SHOES", "FOR JAPAN ❌")),
             "H2": (("STOP PACKING",), ("HOKAS AND ON CLOUDS", "FOR JAPAN 🛑")),
             "H3": (("THE #1 FOOTWEAR", "MISTAKE"), ("TRAVELERS MAKE IN JAPAN ✈️",))}
SECTION_TEXT = {"P2": ("#1 - SOFT FOAM PACKS FLAT", "WHILE STANDING 📉"), "P3": ("#2 - DANGEROUS ON SLICK", "TILES, ICE & SNOW ❄️"),
                "P4": ("#3 - NARROW TOE BOXES", "CRUSH SWELLING FEET 🦶")}

def anchor(sec, phrase, cur):
    """word index of phrase in section (first occurrence at/after cur) -> 'phrase#n' for the engine"""
    ws = WORDS[sec]; toks = [norm(t) for t in phrase.split()][:3]
    toks = [t for t in toks if t] or [norm(ws[cur]["w"])]
    for i in range(cur, len(ws) - len(toks) + 1):
        if [norm(w["w"]) for w in ws[i:i + len(toks)]] == toks:
            n = sum(1 for k in range(i) if [norm(w["w"]) for w in ws[k:k + len(toks)]] == toks) + 1
            return i, (" ".join(w["w"] for w in ws[i:i + len(toks)]) + (f"#{n}" if n > 1 else ""))
    raise KeyError(f"{sec}: {phrase} after {cur}")

def shot(sb, cur):
    sid = sb["shot"]; sec = sid.split(".")[0]
    if sid in SKIP or sb["vo"].startswith("*"): return None, cur
    i, w = anchor(sec, DOC_FROM.get(sid, sb["vo"]), cur)
    if sid in FALLBACK and FALLBACK[sid] is None and sid not in OWN: return None, i
    if i == 0: w = 0
    s = {"sec": sec, "w": w, "sb": sid, "fx": {"zoom": (1.08, 1.13)}}
    if sid in DOCSHOT:
        d = DOC[DOCSHOT[sid]]; s.update(src=f"gen/{DOCSHOT[sid]}.mp4", ss=max(0.05, WORDS[sec][i]["s"] - d[4] - 0.05), doctor=True, fx={"zoom": (1.0, 1.03)})
    elif sid in OWN:
        f, ss, ex = OWN[sid]; s.update(src=f, ss=ss); ex = dict(ex)
        if "fx" in ex: s["fx"] = ex.pop("fx")
        if "z" in ex: z = ex.pop("z"); s["fx"]["zoom"] = (z, z + 0.04)
        s.update(ex)
    else:
        k = FALLBACK.get(sid, sid)
        if isinstance(k, tuple): s.update(src=k[0], ss=k[1])
        elif k in SRC:
            f, ss, meta = SRC[k]; s.update(src=f, ss=ss)
        else: s["missing"] = True; s.update(src=None, ss=0)
    return s, i

def build_shots(hook):
    out, cur = [], {}
    for sb in SB:
        sec = sb["shot"].split(".")[0]
        if sec.startswith("H") and sec != hook: continue
        s, i = shot(sb, cur.get(sec, 0))
        if s is None:
            if i: cur[sec] = i + 1
            continue
        cur[sec] = i + 1; out.append(s)
    for s in out:                                            # hook card on the opening shots (COM376: until the doctor / ~3.5 s)
        if s["sec"] == hook and not s.get("doctor"):
            s.update(hook=HOOK_TEXT[hook], nocap=True)
        if s["sec"] == hook and s.get("doctor"): break
    return out

def sections():
    """(section, from words, until words, lines): headline held over the first 4 shots of each numbered part"""
    out = []
    for sec, lines in SECTION_TEXT.items():
        ss = [s for s in SB if s["shot"].startswith(sec + ".")]
        _, end = anchor(sec, ss[4]["vo"], 0)
        out.append((sec, 0, end, lines))
    return out

if __name__ == "__main__":
    for h in ("H1", "H2", "H3"):
        sh = build_shots(h); miss = [s["sb"] for s in sh if s.get("missing")]
        print(h, len(sh), "shots; missing:", miss)
