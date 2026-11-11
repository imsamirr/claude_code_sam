# Comfort Wear: winning prospecting angles (source for long-form statics)

**Pulled:** 2026-11-11 with `python ads/atria_pull.py longform --brand comfortwear --transcribe`. Raw data, with full copy and transcripts, is in `data/longform_winners.md` and `data/longform_winners.csv`.

**Window:** 2026-08-13 to 2026-11-10. Prospecting only; retargeting is excluded because warm-audience ROAS says nothing about the angle.

**Baseline:** prospecting ROAS is **1.43**. A family qualifies at ≥ $3k spend and ≥ 1.36 ROAS. Families are ranked by spend × ROAS/baseline, so a winner needs both scale and efficiency. 13 of 51 script families qualify.

## 1. Angles ranked (families rolled up)

| Rank | Angle | Families (spend · ROAS · CPA) | Total spend | Signal |
|---|---|---|---|---|
| **A** | **Travel / Disney: "we tested the shoes people actually pack"**, a comparison teardown | Kyro369v2 travel test ($75.4k · 1.40 · $70) + COM211 Disney cut ($2.8k · 1.72) · COM320 Disney 7-shoe test ($8.9k · **1.97** · $52) · **COM284 plus-size Disney survey ($5.1k · 3.22 · $33)** · NH3 plus-size park day ($4.9k · 1.59) · COM374 plus-size ($3.0k · 1.54) | **~$100k** | Biggest scaler in the account. The **plus-size + Disney** version is the most efficient ad in the account. |
| **B** | **Nurse: "running shoes are built for a 5k, not a 12-hour shift"** | Aubrey "Don't waste money" UGC ($19.6k · 1.43) · Kyro390 testimonial-led ($13.9k · 1.61) · NurseNotRunners ($12.9k · 1.55) · COM225 Spanish scoreboard ($7.2k · 1.94 · $49) | **~$54k** | Steady, several scripts. Spanish is the most efficient. |
| **C** | **Teacher: "you're not walking, you're planted"** | Teacher Hook1 test ($18.4k · 1.40) · TeacherTested scoreboard ($9.4k · 1.69) · COM51 teacher test ($4.7k · 1.49) | **~$32.5k** | Scoreboard format (scores + prices) beats the plain test. |
| D | General foot pain listicle static (neuropathy/PF callouts) | Task158 ($5.4k · 1.37) | $5.4k | Weak, borderline. Not used. |

**Below the bar** (for reference, don't build on these): TravelRetiree over-50 ($2.75k · 1.32), Hokas & Brooks worst for work, Spanish ($2.9k · 1.14), Nurse-wants-to-quit drama ($2.8k · 1.04), all PFParkDayHeel and Grandparents-at-Disney cuts (< $400, ROAS < 1).

## 2. The DNA every winner shares

Long-form copy must carry these. They are what Meta is buying.

1. **Job/occasion framing: "built for people who stand for a living."**
   - "Comfortwear doesn't make shoes for athletes. They make shoes for people whose feet have to survive real life."
   - "Built for the shift, not the 5k."
   - "Not built for a runner, a lab, or a weekend."
2. **Named competitors, priced, each with its own failure mode.** This is the main body of every winner. Reuse these exact failure modes (they're already approved and running):

   | Shoe | Price used | Failure mode (winner wording) |
   |---|---|---|
   | Hoka | $165–180 | "Felt great for 2 hours"; foam built for straight-down impact, so "on uneven ground your foot rolls side to side"; "almost twice the weight", so "knees hurt more than their feet"; unstable when you crouch |
   | Brooks (Ghost) | $140 | Built to move a runner forward; narrow tapered toe box "presses a bunion exactly where it hurts"; "a hole worn clean through at the bunion" |
   | On Cloud | $180 | "Triangle-shaped toe box, not made for your feet; real tight by lunch" |
   | Nike Air Max | $130 | Built for "running tracks and gym floors"; narrow toe box; "the air bubble is there for the look, not your arch" |
   | Skechers memory foam | $70–90 | "Compresses under your weight and doesn't recover until you take them off", so "least support right when you need it most" |
   | Dansko clogs | — | Rigid footbed "rock hard from day one", heaviest |
   | Vionic | $130 | "Rigid mold, one fixed shape, and feet don't hold one shape. They swell." |
   | Birkenstock | $110 | Cork "takes your foot shape and none of its impact"; backless, so "toes clench all day" |
3. **The mechanism: walking ≠ standing.**
   - "Your feet aren't wrecked from walking, they're wrecked from standing."
   - Running foam is "tuned to spring you through a stride, not hold you up standing still", so it "packs flat by hour four".
   - Feet **swell (up to half a size)**, so a narrow toe box squeezes: "swollen like sausages by mid-shift", "the shoe that fit at breakfast feels two sizes smaller".
   - Heavy shoes get lifted 20,000 times.
   - Wet or mopped floors.
4. **Solution features, mapped one-to-one to the failures:**
   - firm-but-flexible sole
   - structural arch support built in ("nothing to pack down")
   - **stretch knit upper that gives as feet swell**
   - wide toe box
   - slip-resistant grip
   - light
   - "looks like a clean, normal sneaker, not orthopedic"
5. **Price inversion.** "$60 outscored the $180 pair." "The highest score on my board at the lowest price on it."
6. **Outcome language** (the identity payoff, not "less pain"):
   - "Not hurt less. Didn't hurt."
   - "You're not the one sitting on a bench watching other people see what you flew there to see."
   - "Getting to the last bell with something left."
   - "Picked up an extra shift because I felt good enough to."
7. **Wasted-money opener** (Aubrey, $19.6k): "$180 for Hokas, $200 for Danskos, $150 for Brooks. All sitting in my closet."
8. **Close:**
   - 40% off (Black Friday: 60% + free gifts)
   - free shipping
   - HSA/FSA
   - "wear them for 30 days on your hardest days, and if they don't change how your feet feel, send them back"
   - "500,000+"

## 3. What the first long-form draft got wrong

`output/longform/disney_bench_grandma_v1.md` is superseded.
- It was built on the weakest Disney cuts (NH3, MO2), not on the travel test or COM284.
- It removed the competitor teardown, which is the core of every winner.
- It hid the mechanism inside a made-up mentor.
- It dropped the trial/guarantee that every winner closes on.

## 4. Claims decision needed (flagged to the user)

`brand.json → claims_to_avoid` bans money-back guarantees, "500,000+" style counts, star ratings and "podiatrist recommended". Every winning video uses the first three (and two use a podiatrist narrator).

The new copies use:
- the **trial line** ("wear them 30 days… send them back"), marked `[GUARANTEE]` so it's one edit to remove;
- the count, marked `[COUNT]`;
- **no podiatrist persona**, no condition cures, and no star ratings.
