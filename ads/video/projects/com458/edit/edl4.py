"""COM458 shot list — directed by StefanBrain (edit/STEFANBRAIN_DIRECTION_COM458.md), cut in COM376's style.
Shot ids in comments = StefanBrain shot numbers. Sources: edit/sourcing_{A,B,C}.json (NYC UGC from TikTok), Drive library
(product, via ../sciatica_v1), gen/ (AI doctor = Kling AI Avatar lip-synced to the VO; 3D animations = Kling 4.0),
COM376 itself for the brand's own offer stickers + end card (frames with no burned-in captions only)."""
import json
from pathlib import Path
E = Path(__file__).resolve().parent
MUSIC_DB = -13.0
_src = {}
for g in "ABC":
    for x in json.load(open(E / f"sourcing_{g}.json")):
        if x.get("file"): _src[str(x["shot"])] = (x["file"], float(x.get("in") or 0))
def U(shot, d=0.0):
    f, i = _src[shot]; return f, i + d
LIB = {4: "assets/lib/01_Cushion and Arch Support/OSCS_Arch Support 02.mov", 5: "assets/lib/01_Cushion and Arch Support/OSCS_Arch Support 04.MOV",
       7: "assets/lib/01_Cushion and Arch Support/OSCS_Cushion 01.MOV", 13: "assets/lib/02_Wide Toe Box/OSCS_Wide Toe Box 01.mov",
       16: "assets/lib/02_Wide Toe Box/OSCS_Wide Toe Box 04.mov", 19: "assets/lib/03_Adaptive Stretch Fabric/Brianna_Nurse_Showing fabric 01.mov",
       23: "assets/lib/03_Adaptive Stretch Fabric/OSCS_Fabric 01.MOV", 24: "assets/lib/03_Adaptive Stretch Fabric/OSCS_Fabric 02.MOV",
       73: "assets/lib/07_Montage/Larissa_Mom_Holding shoes 03.MOV", 78: "assets/lib/07_Montage/Larissa_Mom_Showing 3 OSCS.MOV",
       101: "assets/lib/09_Lifestyle/Larissa_Mom_Wearing shoes 01.MOV", 102: "assets/lib/09_Lifestyle/OSCS_Wearing Shoes 01.mov",
       227: "assets/misc/Others/Broll topview of the shoes.MOV", 343: "assets/misc/Seniors/Broll senior walking outside with CW shoes on.mov",
       350: "assets/misc/Seniors/Broll showing outsole of the shoes while being worn.mov", 355: "assets/misc/Seniors/Broll topview walking outside in black CW shoes.MOV",
       357: "assets/misc/Seniors/Senior massaging knees.mov", 282: "assets/misc/Seniors/Broll massaging leg back view.mov", 5: "assets/lib/01_Cushion and Arch Support/OSCS_Arch Support 04.MOV", 371: "assets/misc/sole new final.mp4", 373: "assets/misc/website showing 40_ off and products .MOV"}
R376 = "reference/COM376_HO1.mp4"

def S(sec, w, src, ss=0.0, z=1.08, **kw):
    fx = kw.pop("fx", {}); fx.setdefault("zoom", (z, z + 0.05))
    return {"sec": sec, "w": w, "src": src, "ss": ss, "fx": fx, **kw}
def UG(sec, w, shot, d=0.0, **kw):
    f, i = U(shot, d); return S(sec, w, f, i, **kw)
def LB(sec, w, i, ss=0.5, **kw): return S(sec, w, LIB[i], ss, **kw)

HOOK_TEXT = {"H1": (("HOKAS &", "ON CLOUDS"), ("ARE THE WORST SHOES", "FOR NEW YORK CITY")),
             "H2": (("YOU'LL REGRET", "PACKING"), ("HOKAS OR ON CLOUDS", "FOR YOUR NYC TRIP")),
             "H3": (("WHY NYC", "TOURISTS"), ("TAP OUT BY 2 PM",))}
def HK(h, **kw): return {"hook": HOOK_TEXT[h], "nocap": True, **kw}

HOOKS = {
 "H1": [
    UG("H1", 0, "H1.1", **HK("H1")),                                   # H1.1 Hoka + On side by side
    UG("H1", "are the worst", "H1.2", **HK("H1")),                     # H1.2 Hokas stepping
    UG("H1", "for new york", "H1.3", **HK("H1")),                      # H1.3 NYC POV
    S("H1", "I know", "gen/D3_H1.mp4", 0.05, z=1.0, doctor=True),       # H1.4-6 AI podiatrist (lip-synced)
 ],
 "H2": [
    UG("H2", 0, "H2.1", **HK("H2")),                                   # unboxing Hokas
    UG("H2", "on hokas or", "H2.2", fx={"zoom": (1.48, 1.51), "zc": (540, 1920)}, keep_text=True, **HK("H2")),   # creator caption (upper third) cropped out                       # packing for NYC
    S("H2", "do not put", "tiktok/nyc_packing/maxieelise_7332662870708145450.mp4", 58.0, fx={"rev": True}),   # pulling them back out (reverse)
    S("H2", "Those plush", "gen/D3_H2.mp4", 0.05, z=1.0, doctor=True),  # doctor: plush gym shoes / 40 min
    UG("H2", "on a treadmill", "H2.5"),                                # treadmill
    UG("H2", "not 20,000", "H2.6"),                                    # step counter
    UG("H2", "on unforgiving", "H2.7"),                                # NYC concrete
 ],
 "H3": [
    UG("H3", 0, "H3.1", fx={"zoom": (1.2, 1.23), "zc": (540, 1920)}, **HK("H3")),   # price pill (top) cropped out                                   # crowded midtown POV
    UG("H3", "wearing hokas", "H1.2", keep=True, **HK("H3")),         # feedback: show the Hokas...
    UG("H3", "or On Clouds", "27", keep=True, **HK("H3")),            # ...and the On Clouds right after the NYC opener
    S("H3", "around two", "tiktok/nyc_subway/carterrodney_6990015792951676165.mp4", 23.0, keep_text=True),   # head in hands on platform
    UG("H3", "They'll be either", "H3.4", fx={"zoom": (1.36, 1.40), "zc": (540, 1920)}, keep_text=True),
    UG("H3", "or paying", "H3.5"),
    UG("H3", "because their feet", "H3.6"),
 ],
}

BODY = [
 # P1 setup
 UG("P1", 0, "07"), UG("P1", "for forty minutes", "08"), UG("P1", "not for someone", "09"),
 UG("P1", "When you are visiting", "10"), UG("P1", "you are not just", "11"), UG("P1", "You are pounding", "12"),
 UG("P1", "climbing three", "13"), UG("P1", "navigating cracked", "14"), UG("P1", "standing in lines", "15"),
 S("P1", "and doing it all", "tiktok/nyc_subway/carterrodney_6990015792951676165.mp4", 24.3, keep_text=True), UG("P1", "eight, nine", "10", 2.0),
 UG("P1", "sometimes ten", "12", 2.5),
 S("P1", "Three things people", "gen/D3_P1.mp4", 0.05, z=1.0, doctor=True), UG("P1", "already in the city", "32", 2.0),                      # 17 doctor counts 3
 # P2 #1 soft foam
 UG("P2", 0, "18"), UG("P2", "and those bouncy", "19", fx={"zoom": (1.5, 1.53), "zc": (540, 0)}), UG("P2", "do not tell", "27", 1.5), UG("P2", "With Hokas, that", "20", fx={"zoom": (1.3, 1.33), "zc": (540, 1920)}), UG("P2", "is made to spring", "20", 1.6, fx={"zoom": (1.3, 1.33), "zc": (540, 1920)}), UG("P2", "on a jog", "H2.5"),
 UG("P2", "But New York means", "21"), UG("P2", "standing in line for a bagel", "22"), UG("P2", "waiting on a concrete", "23", keep_text=True),
 UG("P2", "and standing through", "24"), UG("P2", "because the line", "15", 0.6),
 S("P2", "when your feet start", "gen/anim_foam.mp4", 0.3, z=1.0), S("P2", "from the foam", "gen/anim_foam.mp4", 1.8, z=1.2),                  # 26 3D foam packs flat
 UG("P2", "And with On Clouds", "27"), UG("P2", "pods compress", "19", 2.0, fx={"zoom": (1.5, 1.53), "zc": (540, 0)}), UG("P2", "under constant", "15", 5.0),
 S("P2", "leaving your arch", "gen/anim_foam.mp4", 2.6, z=1.05),                    # 29 arch red
 # P3 #2 wobble & slippery
 UG("P3", 0, "30"), UG("P3", "were not built", "31"), S("P3", "and winter hazards", "tiktok/nyc_winter/rtlaktuell_7610126598804688150.mp4", 5.5), UG("P3", "In New York, you", "32"), UG("P3", "across cracked", "14", 0.5), UG("P3", "stepping off icy", "33", fx={"zoom": (1.45, 1.48), "zc": (540, 1920)}, keep_text=True),
 S("P3", "and hurrying down", "tiktok/nyc_subway/justkingkev_7560843798507457806.mp4", 6.0), UG("P3", "subway stairs for", "13", 26.5), S("P3", "You want to feel", "tiktok/nyc_wsp/shayla.quinn_7429698760479051054.mp4", 7.0), UG("P3", "With Hokas, that massive", "36", fx={"zoom": (1.3, 1.33), "zc": (540, 1920)}),
 UG("P3", "shifts your balance", "37"), UG("P3", "making you wobble", "38", fx={"zoom": (1.3, 1.33), "zc": (540, 1920)}), LB("P3", "and putting extra", 357, 0.5), LB("P3", "on your knees", 282, 1.0),
 UG("P3", "Plus, all that", "40"), UG("P3", "over twenty thousand", "H2.6"), UG("P3", "And with On Clouds, those smooth", "42", fx={"zoom": (1.5, 1.53), "zc": (540, 0)}),
 UG("P3", "turn into literal", "43", 0.7, fx={"zoom": (1.25, 1.3)}), UG("P3", "the second winter", "44"), UG("P3", "or freezing rain", "44", 1.2), S("P3", "hits polished", "tiktok/nyc_subway/realmikemizzle_7289093713815440682.mp4", 19.0, fx={"zoom": (1.45, 1.48), "zc": (540, 0)}, keep_text=True),
 UG("P3", "and metal subway", "46"),
 S("P3", "That is where", "gen/D3_P3.mp4", 0.05, z=1.0, doctor=True),                            # 47 doctor
 LB("P3", "You want a shoe", 350, 0.5), UG("P3", "not an unstable", "49"), UG("P3", "on freezing streets", "31", 1.5),
 # P4 #3 narrow toe box
 UG("P4", 0, "50"), UG("P4", "and it does not", "51", fx={"zoom": (1.5, 1.53), "zc": (540, 0)}), UG("P4", "On Clouds are notoriously", "52"), S("P4", "and Hokas taper", "tiktok/hoka/psaprockyxoxo11_7518821487051148574.mp4", 0.4),
 UG("P4", "If they squeeze", "54"), UG("P4", "before you have", "54", 1.5), UG("P4", "After hours of", "56"), UG("P4", "across the city", "21", 1.5),
 S("P4", "your feet naturally", "gen/anim_toes.mp4", 0.3, z=1.0),                   # 57 3D swelling
 S("P4", "A tight fit", "gen/anim_toes.mp4", 2.6, z=1.05), S("P4", "the only thing", "tiktok/nyc_pain/hemali.mistry_7091420320992595206.mp4", 4.0),                         # 58 toes glowing red
 UG("P4", "Your toes feel", "59"), UG("P4", "rubbing blisters", "60"), UG("P4", "You are loosening", "61", keep_text=True),
 S("P4", "and you have still", "tiktok/nyc_hoods/hungryartistny_7116933626977062190.mp4", 6.5), UG("P4", "and a Broadway", "62", keep_text=True),
 # P5 solution (product proof word-for-word)
 LB("P5", 0, 102, 8.0), LB("P5", "built the opposite", 101, 3.0), LB("P5", "made for people", 78, 1.0), UG("P5", "real life", "88", 0.5), UG("P5", "nurses", "64"), UG("P5", "healthcare workers", "65"), UG("P5", "and travelers who", "66"),
 LB("P5", "A roomy toe box", 16, 1.0), LB("P5", "instead of getting", 13, 3.0), LB("P5", "A flexible stretch", 23, 1.0),
 LB("P5", "as they swell", 24, 1.0), LB("P5", "Comfortable cushioning", 4, 1.0), LB("P5", "and built-in", 5, 2.0), LB("P5", "work together", 355, 1.0), LB("P5", "so the support", 7, 1.0),
 LB("P5", "paired with a", 350, 1.5), S("P5", "on wet crosswalks", "tiktok/nyc_winter/rtlaktuell_7610126598804688150.mp4", 8.0), UG("P5", "subway stairs, and", "75"),
 UG("P5", "and metal grates", "46", 4.0),
 # P6 payoff
 UG("P6", 0, "77"), UG("P6", "sitting on a bench", "78"), UG("P6", "watching everyone", "09", 3.5), UG("P6", "or tapping out", "H3.5", 2.0), UG("P6", "back to the hotel", "54", 3.0),
 UG("P6", "You want to be walking", "80", 6.0, fx={"zoom": (1.36, 1.39), "zc": (540, 0)}),
 S("P6", "exploring every", "tiktok/nyc_hoods/hungryartistny_7116933626977062190.mp4", 5.0),
 S("P6", "neighborhood", "tiktok/nyc_hoods/nyclovesnyc_7322839897486855470.mp4", 1.0),
 UG("P6", "and there when", "82", keep_text=True),
 # P7 offer (COM376's own sticker animations, no captions under stickers)
 LB("P7", 0, 227, 2.0),
 S("P7", "Comfortwear is up", R376, 122.85, z=1.0, nocap=True),
 S("P7", "with free shipping", R376, 124.05, z=1.0, nocap=True),
 LB("P7", "putting them under", 373, 2.0, keep_text=True),
 S("P7", "and you get thirty", R376, 125.0, z=1.0, nocap=True, fx={"speed": 0.8, "zoom": (1.0, 1.0)}),
 UG("P7", "Put them through", "88"), LB("P7", "walking days", 355, 4.0), LB("P7", "If they are not", 343, 1.0), LB("P7", "Tap below", 227, 6.0),
 UG("P7", "before you pack", "91"),
 S("P7", "York", R376, 131.0, z=1.0, nocap=True, dt=0.45),                         # end card (COM376)
]

# section headlines (StefanBrain): (section, from words, until words, lines) — held over the first 3-4 shots
SECTIONS = [("P2", 0, "With Hokas, that", ("#1 - SOFT FOAM", "PACKS FLAT")),          # COM376 holds "#1" ~3-4 shots
            ("P3", 0, "In New York, you", ("#2 - WOBBLE &", "SLIPPERY OUTSOLES")),
            ("P4", 0, "On Clouds are notoriously", ("#3 - NARROW TOE BOX", "& BLISTERS"))]
