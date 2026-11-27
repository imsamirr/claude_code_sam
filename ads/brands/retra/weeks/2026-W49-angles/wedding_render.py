"""4K Kie scenes for the wedding-memories statics (W1-W5; formats from Sam's RTR / The Knot / Olive & Piper refs).
python3 wedding_render.py [ids...]   (W5 uses the existing white product photo, no render)"""
import sys
from concurrent.futures import ThreadPoolExecutor
import render, batch2

G = batch2.GRIP
FLASH = render.FLASH
PARTY = "Direct on-camera flash party photo, hard flash, dark falloff, warm skin, mild grain, slight motion blur."
J = {
    "w1": dict(refs=["blossom"], ar="9:16", style=PARTY, prompt=(
        "Two women friends in their late 20s at a wedding reception pose cheek to cheek against a teal velvet curtain,"
        " pulling playful silly faces (tongue out, peace sign over one eye), one in a black polka-dot slip dress, one in a"
        " bright blue satin dress; the one on the right holds the raspberry-red Retra camera up near her face, front"
        " facing the viewer. Faces in the upper half; the lower 45% is their dresses and the curtain." + G)),
    "w2": dict(refs=["chalk"], ar="9:16", style=PARTY, prompt=(
        "A wedding reception dance floor at night: the bride in a white satin gown and a bridesmaid in white dance and"
        " laugh mid-spin, guests blurred behind; in the foreground a guest's hand holds up the off-white Retra camera"
        " to photograph them, front facing the viewer. Lower 40% of the frame is darker floor and blurred guests." + G)),
    "w3": dict(refs=[], ar="9:16", style="Wedding reception photo with on-camera flash, dark background, warm tones, grain.",
        prompt=("A happy newlywed couple sharing their first dance at an evening wedding reception: the bride in a lace"
        " gown with small flowers in her hair, the groom in a navy suit and bow tie, smiling at each other, her arm"
        " around his shoulders. Dark reception hall behind them. The top third of the frame is dark and empty.")),
    "w4": dict(refs=["obsidian"], ar="9:16", style=PARTY + " 1990s film snapshot feel, warm.", prompt=(
        "A just-married couple in their late 20s sit close on a retro patterned orange lounge sofa, both in black"
        " sunglasses, grinning; the groom in a black suit holds the black Retra camera in one hand at chest height, front"
        " facing the viewer; the bride holds a big white bouquet, veil and white dress. Candid, slightly tilted." + G)),
}
orig = render.build_prompt


def bp(job, fix=""):
    p = orig(job, fix)
    if not job["refs"]:
        p = p.replace(", except the gold serif 'Retra' wordmark printed on the camera exactly as in the reference.",
                      ". No cameras, brand names, wordmarks, logos or lettering anywhere.")
    return p


render.build_prompt = bp
render.JOBS.update(J)
# through-the-lens set (W6-W9): what the shooter sees, so no camera in frame
LENS = "Wedding photo with direct on-camera flash, warm, grain, dark background falloff."
J.update({
    "w6": dict(refs=[], ar="9:16", style=LENS, prompt=(
        "Night sparkler send-off: a just-married couple run hand in hand toward the camera through two lines of guests"
        " holding glowing sparklers, the bride laughing with her head thrown back, the groom grinning; trails of sparks,"
        " faces lit warm. Couple in the centre of the frame.")),
    "w7": dict(refs=[], ar="9:16", style=LENS, prompt=(
        "Wedding reception dance floor: four bridesmaids in sage-green dresses and two groomsmen in suits dance wildly"
        " and pose for the camera - one groomsman mid-jump, a bridesmaid pointing straight at the camera laughing,"
        " ties loosened, shoes off. Group in the centre of the frame.")),
    "w8": dict(refs=[], ar="9:16", style="Bright daytime wedding photo with fill flash, soft grain.", prompt=(
        "Ceremony exit: a newlywed couple walk up the aisle toward the camera mid-laugh as guests on both sides throw"
        " white and pink paper confetti and dried petals over them; the groom kisses the bride's temple. Couple in the"
        " centre of the frame.")),
    "w9": dict(refs=[], ar="9:16", style=LENS, prompt=(
        "A round wedding reception table seen from the head of the table: eight guests in their late 20s and 30s raise"
        " glasses in a toast and laugh straight at the camera, candles, flowers, half-eaten dessert, one guest wiping"
        " a happy tear. Guests fill the centre of the frame.")),
})
render.JOBS.update(J)

if __name__ == "__main__":
    ids = sys.argv[1:] or list(J)
    for i in ids:
        for c in J[i]["refs"]:
            render.ref_url(c)
    with ThreadPoolExecutor(8) as ex:
        list(ex.map(render.render, ids))
