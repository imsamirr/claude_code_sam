"""Build the health & sleep DR statics board: board/index.html, board/data.json, board/img/*.jpg.

    python3 build.py

Reads candidates/<brand>.txt (ad_id url days) and picks_<brand>.txt (index STAGE description),
images from img/<brand>/. CSS and filter script are shared with ../static_inspo/board (board/_style.html, _script.html).
"""
import html
import json
from pathlib import Path

from PIL import Image

HERE = Path(__file__).resolve().parent
B = HERE / "board"
(B / "img").mkdir(parents=True, exist_ok=True)
esc = lambda s: html.escape(s, quote=True)

GROUPS = [
    ("sleep", "Brands like Hears and Dore & Rose",
     "Premium sleep and hearing brands that test hard on Meta. Product-photo craft, persona hooks, limited colours as news.",
     [("hears", "Hears", "Dutch filtered earplugs for concerts, sleep and motorbikes. About 15,400 ads lifetime."),
      ("doreandrose", "Dore & Rose", "Dutch silk sleep masks and cotton pyjamas. Photography-led, press bar on almost everything. About 25,400 ads."),
      ("loop", "Loop", "Belgian earplugs and the biggest advertiser here (about 63,000 ads). Collabs, colour drops and a quiz."),
      ("manta", "Manta Sleep", "US blackout sleep masks and new sleep earplugs. Persona-led (night shift, athletes, travel), lots of native screenshots."),
      ("ozlo", "Ozlo Sleep", "US sleep earbuds, premium price. Press quotes, testimonials, HSA/FSA.")]),
    ("health", "Health & wellness, direct response",
     "Supplement brands known for aggressive DR statics. Cartoons, timelines, plain-text letters, apology sales. Most lean on weight-loss or medical claims, so borrow the format, not the claim.",
     [("bioma", "Bioma", "Probiotic / \"GLP-1 booster\". The most discount-heavy brand here, and the longest runners (400 days)."),
      ("arrae", "Arrae", "Women's supplements (creatine gummies, bloat, inositol). Editorial photography plus UGC captions; almost no discount ads."),
      ("gruns", "Grüns", "Greens gummies. Bold colour, emoji headlines, GLP-1-user angle, licensed Shrek and Minions editions (skip those)."),
      ("primalqueen", "Primal Queen", "Beef-organ supplement for women. Provocative hooks, illustration and 3D cartoons, anniversary sales."),
      ("create", "Create", "Creatine gummies positioned as candy. Clean still lifes, billboard mock-ups, subscribe-and-save bundles.")]),
]

# Format ideas: (name, description, seen at, note, is_caveat)
FORMATS = {
    "TOF": [
        ("Plain-text letter or statement", "An \"official apology\", \"we got copied\" or a customer's story set as a letter on plain paper. No product photo, or a small one at the end.",
         "Hears, Grüns, Bioma, Primal Queen", "For Retra: \"An official apology to disposable cameras\" style. Copy from StefanBrain.", False),
        ("Native screenshot", "iMessage between friends or family, an X post, an Instagram or TikTok comment reply, even a ChatGPT answer recommending the product.",
         "Dore & Rose, Arrae, Manta, Grüns", "Use real customer words or make the brand the obvious speaker. Invented customer chats are fake testimonials.", True),
        ("UGC photo + caption overlay", "A phone photo with a \"POV:\" bar, TikTok caption stickers or a handwritten-style line on top.",
         "Hears, Ozlo, Arrae, Grüns, Create", "Needs real customer or creator photos.", True),
        ("Analogue notes", "Post-its on a bedside table, a handwritten note by the product, a whiteboard drawing, handwritten arrows drawn over a photo.",
         "Hears, Loop, Primal Queen, Ozlo, Arrae", "Cheap to make. Good fit for Retra's film-era feel.", False),
        ("Cartoon or comic", "A comic strip of one customer's story, a memoji 2x2 of the alternatives, a two-panel meme, 3D cartoon characters, a pencil sketch.",
         "Bioma, Hears, Manta, Primal Queen, Grüns", "Draw our own characters. Don't copy film or toy IP (Gru, Shrek, Minions, Barbie appear in the originals).", True),
        ("Surreal prop or scene", "Product in a vending machine, a bed in the middle of a crosswalk, a billboard in the clouds, product floating in a pool, a thermal-camera image.",
         "Hears, Ozlo, Create, Bioma, Primal Queen", "Highest scroll-stop. Easy to render with our cut-outs.", False),
        ("Reframe or enemy line", "One sentence that renames the problem or picks a villain: \"Not polyester pretending to be soft.\" \"You're not lazy.\" \"[Alternative]? Nah.\"",
         "Dore & Rose, Grüns, Primal Queen, Bioma, Hears, Manta", "For Retra the villain is the phone camera or the disposable. Lines from StefanBrain.", False),
        ("Objection as the headline", "The reader's own pushback in quotes, answered by the picture: \"I don't do earplugs.\" with a split of the Saturday with and without.",
         "Hears", None, False),
        ("Persona or occasion callout", "Name who it's for or when: night shift, college dorm, festival weekend, the snoring boyfriend, a gift for the light sleeper.",
         "Manta, Ozlo, Hears", "Name the persona every ad is written for.", False),
        ("Press or authority quote card", "A press quote in a frosted card, \"Better than [big brand]\", \"The Rolex of…\", a gift-list badge, an \"As seen in\" bar.",
         "Manta, Ozlo, Dore & Rose", "Only real press and real customer quotes.", True),
        ("Data or app UI as the visual", "A sound-meter card, a sleep-score before and after, a line chart, a big stat headline.",
         "Hears, Ozlo, Manta, Primal Queen, Grüns", "For Retra: photo counts per charge or per trip, never invented stats.", True),
        ("Timeline", "Day 1 / Day 7 / Day 21, month-by-month, \"If you start this month, by Christmas you'll…\", a week-by-week caption.",
         "Bioma (400 days live), Arrae, Primal Queen", "For Retra: a trip or a year in photos.", False),
        ("Split or visual metaphor", "Before/after, \"your Saturday on nothing vs on ours\", two shifts with two different results, a dried fruit vs a juicy one.",
         "Hears, Manta, Primal Queen, Bioma", "Body before/after shots are a Meta policy risk; object metaphors are safe.", True),
        ("Listicle card", "\"5 things that happen when…\", \"Things I found out in my 40s\", stacked \"Want…? Want…?\" questions, \"One product, five problems solved.\"",
         "Ozlo, Grüns, Arrae, Bioma", None, False),
        ("Photo-only, no copy", "A plain packshot, a lifestyle crop, a lo-fi top-down phone photo, an archival black-and-white photo.",
         "Dore & Rose, Ozlo, Primal Queen", "Some of the longest runners (Ozlo 138 days, Primal Queen 90).", False),
        ("Colour drop or collab as news", "A new colour on a matching texture, \"Just dropped\", \"Limited edition\", a co-designed edition with a partner.",
         "Loop, Dore & Rose, Hears", "Fits Retra's colourways.", False),
        ("Pun or wordplay", "\"Grape Expectations\", \"Pleasing to the eye. And the ears.\", circular type round the product (\"Best. Earplugs. Ever.\").",
         "Create, Loop, Manta", None, False),
        ("Warning or reverse psychology", "\"DO NOT take this if…⚠️\", \"Don't buy these if…\", a parody of the sensitive-content blur screen.",
         "Primal Queen", None, False),
    ],
    "MOF": [
        ("Ours vs theirs cards", "Two cards or columns: the cheap/old way with ✗ marks, ours with ✓ marks. Or a table over a lifestyle photo.",
         "Manta, Primal Queen, Create, Hears", "Retra vs disposable vs phone.", False),
        ("Chooser or quiz", "\"Which one do you need?\" product cards, \"Take our quiz\" grid, \"Is it right for you?\" icon row.",
         "Hears, Loop, Arrae", "For Retra: which colour or which filter is you.", False),
        ("Spec labels round the product", "Feature pills floating around the product, a basket of models with specs, stacked product with big-number callouts.",
         "Loop, Ozlo, Grüns", "500 photos per charge, no Wi-Fi/Bluetooth/app.", False),
        ("Problems / solution columns", "A list of problems on the left, the product on the right.",
         "Arrae", None, False),
        ("Venn diagram", "Three benefits as circles, the product in the overlap.",
         "Grüns", None, False),
        ("Objection first", "Lead with the doubt (\"Yes, it's pricey\") then show what's inside and the price.",
         "Bioma", None, False),
        ("Crossed-out list", "Old problems or alternatives struck through, then \"Meet…\" or \"Purpose-built for…\".",
         "Ozlo, Primal Queen", None, False),
        ("Launch numeral or range overview", "A giant \"2\" behind the product, the whole collection as flat illustrations, every flavour in a grid.",
         "Ozlo, Dore & Rose, Create", None, False),
    ],
    "BOF": [
        ("Apology or sell-out letter", "\"We're so sorry\" (selling fast, sale ending, forgot to tell you), \"We're shutting it down\", \"Clearance: we're no longer making these colours\".",
         "Grüns, Bioma, Primal Queen, Ozlo, Arrae, Dore & Rose", "Only true scarcity. Retra really is low on stock.", True),
        ("Cartoon offer", "A sketch of the customer \"waiting for a sale\" (\"This is the sale.\"), a \"SOLD OUT\" monster grabbing someone.",
         "Hears (199 days live), Grüns", None, False),
        ("Pay for 2, get 3", "A colour lineup lit on black, stacked offer banners, two hands holding three cases.",
         "Hears, Loop", "Natural fit for Retra's Buy 2, get 1 free.", False),
        ("Price card + gift list", "A struck-through price, a per-day price sticker, and free gifts / free shipping / guarantee as a ticked list.",
         "Dore & Rose, Grüns, Bioma, Primal Queen", "Compare-at prices must be real. No currency code on images.", True),
        ("Packaging as the offer", "The bundle shown as a retail blister pack with a price starburst.",
         "Loop, Manta", None, False),
        ("Native pop-up offer", "An iOS permission dialog: \"would like to share 20% off + a free gift\", Decline / Accept.",
         "Loop (183 days live)", None, False),
        ("Lo-fi scrawl", "An MS-Paint handwritten sale ad: \"…sorry, our designer is on vacation\".",
         "Primal Queen (82 days live)", None, False),
        ("Gift with purchase / occasion sale", "Product + free item joined by a \"+\", a birthday cake built from the product, \"It's our birthday and we lowered the price\", HSA/FSA reminders before year-end.",
         "Ozlo, Primal Queen, Grüns", "HSA/FSA is a Comfort Wear angle, not Retra.", True),
    ],
}

TAKEAWAYS = [
    ("Plain text wins long.", "Letters, apologies and story cards with no design run for months: Bioma's \"if you start this month\" card has run 400 days, Hears' cartoon sale ad 199, Loop's iOS pop-up 183."),
    ("Native beats polished for TOF.", "Every brand except Dore & Rose leans on screenshots, caption stickers, Post-its and handwriting. These are cheap to make from our existing cut-outs."),
    ("The two groups split.", "Sleep and hearing brands sell with product-photo craft, personas and colour drops. The health brands sell with cartoons, timelines, enemies and apology sales."),
    ("Borrow formats, not claims.", "Most health ads rest on weight-loss or medical claims and body before/afters. Copy the layout and write Retra's own true line (through StefanBrain)."),
]


def stage_counts(items):
    return {s: sum(1 for i in items if i["stage"] == s) for s in ("TOF", "MOF", "BOF")}


def main():
    data, total = [], {"TOF": 0, "MOF": 0, "BOF": 0}
    for gkey, gname, gnote, brands in GROUPS:
        for key, name, note in brands:
            cand = [l.split() for l in open(HERE / "candidates" / f"{key}.txt") if l.strip()]
            items = []
            for line in open(HERE / f"picks_{key}.txt"):
                if not line.strip():
                    continue
                idx, stage, desc = line.rstrip("\n").split(" ", 2)
                ad, _, days = cand[int(idx)]
                im = Image.open(HERE / "img" / key / f"{ad}.jpg").convert("RGB")
                im.thumbnail((440, 700), Image.LANCZOS)
                im.save(B / "img" / f"{ad}.jpg", quality=80, optimize=True)
                items.append(dict(ad=ad, stage=stage, desc=desc, days=int(days), img=f"img/{ad}.jpg", w=im.width, h=im.height))
                total[stage] += 1
            data.append(dict(group=gkey, key=key, name=name, note=note, items=items))
    json.dump(data, open(B / "data.json", "w"), ensure_ascii=False, indent=1)

    out = [
        "<title>Health & Sleep DR Statics</title>",
        '<meta name="claude:viewport-fit-sides" content="cover">',
        '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>',
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;700;800&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@500&display=swap">',
        open(B / "_style.html").read().replace("</style>", EXTRA_CSS + "</style>"),
        '<header class="strip"><div class="wrap">',
        '<div class="eyebrow">Retra · static format research · Meta, via Atria · 26 Nov 2026</div>',
        "<h1>Health &amp; sleep DR statics</h1>",
        '<p class="lede">200 static ads from ten brands: five like Hears and Dore &amp; Rose, and five direct-response health and wellness brands. '
        "Each brand's top image ads by Atria impression rank, 20 per brand, split 70% top, 15% middle and 15% bottom of funnel. Formats come first, then the ads.</p>",
        f'<div class="stats"><span class="chip tof">TOF {total["TOF"]}</span><span class="chip mof">MOF {total["MOF"]}</span><span class="chip bof">BOF {total["BOF"]}</span></div>',
        '<nav class="brands" aria-label="Sections"><a href="#takeaways">Takeaways</a><a href="#formats">Format ideas</a>'
        + "".join(f'<a href="#{k}">{esc(n)}</a>' for _, _, _, bs in GROUPS for k, n, _ in bs) + "</nav>",
        "</div></header>",
        '<main class="wrap">',
        '<div class="filters" role="group" aria-label="Filter ads by funnel stage"><span>Show</span>'
        '<button type="button" data-f="all" aria-pressed="true">All</button>'
        '<button type="button" data-f="TOF" aria-pressed="false">Top of funnel</button>'
        '<button type="button" data-f="MOF" aria-pressed="false">Middle</button>'
        '<button type="button" data-f="BOF" aria-pressed="false">Bottom</button></div>',
        '<section class="takeaways" id="takeaways"><h2>What stands out</h2><ol>'
        + "".join(f"<li><strong>{esc(a)}</strong> {esc(b)}</li>" for a, b in TAKEAWAYS) + "</ol></section>",
        '<section class="formats" id="formats"><h2>Format ideas</h2>'
        '<p class="intro">Recurring formats across all ten brands, by funnel stage. Plain notes say how a format could fit Retra; red notes are rules to follow before using it.</p><div class="fgrid">',
    ]
    labels = {"TOF": "Top of funnel", "MOF": "Middle of funnel", "BOF": "Bottom of funnel"}
    for st, fs in FORMATS.items():
        out.append(f'<div class="fcol"><h3><span class="chip {st.lower()}">{st}</span> {labels[st]} <span class="count">{len(fs)} formats</span></h3><ul class="flist">')
        for name, desc, seen, note, cav in fs:
            n = f'<p class="{"caveat" if cav else "fit"}">{esc(note)}</p>' if note else ""
            out.append(f"<li><h4>{esc(name)}</h4><p>{esc(desc)}</p><p class=\"src\">Seen at {esc(seen)}</p>{n}</li>")
        out.append("</ul></div>")
    out.append("</div></section>")

    for gkey, gname, gnote, _ in GROUPS:
        out.append(f'<div class="group" id="g-{gkey}"><h2>{esc(gname)}</h2><p class="note">{esc(gnote)}</p></div>')
        for b in [d for d in data if d["group"] == gkey]:
            c = stage_counts(b["items"])
            out.append(f'<section class="brand" id="{b["key"]}"><header class="bh"><div><h2>{esc(b["name"])}</h2><p class="note">{esc(b["note"])}</p></div>'
                       f'<p class="split"><span class="chip tof">TOF {c["TOF"]}</span><span class="chip mof">MOF {c["MOF"]}</span><span class="chip bof">BOF {c["BOF"]}</span></p></header><div class="grid">')
            for i in b["items"]:
                s = i["stage"].lower()
                out.append(f'<figure class="ad" data-stage="{i["stage"]}"><div class="shot"><img src="{i["img"]}" width="{i["w"]}" height="{i["h"]}" loading="lazy" alt="{esc(b["name"])} static ad: {esc(i["desc"])}"></div>'
                           f'<figcaption><div class="meta"><span class="chip {s}">{i["stage"]}</span><span class="days">{i["days"]} days running</span></div><p>{esc(i["desc"])}</p></figcaption></figure>')
            out.append("</div></section>")

    out.append('<footer><p>Selection: for each brand, image ads ordered by Atria impression rank, one row per creative, 40 candidates, then 20 picked for format variety at 14 top / 3 middle / 3 bottom of funnel. '
               "For the eight brands beyond Hears and Dore &amp; Rose, only ads live 14+ days were considered; Loop was limited to English ads. Days running is how long Atria has seen each ad live. "
               "Ostrichpillow was checked but isn't in Atria; Ozlo Sleep took its place. Several originals use licensed or borrowed IP (Shrek, Minions, Gru, Barbie-style dolls) and many make weight-loss or medical claims: "
               "the format notes say what to keep and what to leave.</p></footer></main>")
    out.append(open(B / "_script.html").read())
    (B / "index.html").write_text("\n".join(out))
    print(total, sum(len(d["items"]) for d in data), "ads")


EXTRA_CSS = """
main [id] { scroll-margin-top:72px }
@media (max-width:480px) { main [id] { scroll-margin-top:110px } }
section.takeaways { margin-top:28px }
section.takeaways ol { margin:12px 0 0; padding-left:1.3em; display:grid; gap:8px; max-width:80ch }
.flist .fit { margin-top:6px; font-size:13px; color:var(--tof) }
.group { margin-top:56px; padding:18px 0 6px; border-top:8px solid var(--fg) }
.group h2 { font-size:clamp(24px, 4vw, 34px) }
.group + section.brand { border-top-width:1px; margin-top:20px }
"""

if __name__ == "__main__":
    main()
