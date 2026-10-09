"""Generates the JSON templates and section groups for the portrait theme.

Run: python3 tools/build_templates.py   (from the portrait-theme directory)
All copy here is placeholder text meant to be replaced in the theme editor.
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def strip_empty(obj):
    """Drop empty-string settings; Shopify rejects blank richtext/url values."""
    if isinstance(obj, dict):
        return {k: strip_empty(v) for k, v in obj.items() if v != ""}
    if isinstance(obj, list):
        return [strip_empty(v) for v in obj]
    return obj


def write(path, data):
    data = strip_empty(data)
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


def blocks(prefix, items):
    """items: list of (type, settings) -> (blocks dict, order list)"""
    out, order = {}, []
    for i, (btype, settings) in enumerate(items, 1):
        key = f"{prefix}_{i}"
        out[key] = {"type": btype, "settings": settings}
        order.append(key)
    return out, order


def section(stype, settings, items=None, prefix="b"):
    s = {"type": stype, "settings": settings}
    if items:
        s["blocks"], s["block_order"] = blocks(prefix, items)
    return s


# ---------------------------------------------------------------- shared copy
REVIEW_ITEMS = [
    ("review", {"name": "Customer Name", "date": "08/30/2026", "placeholder_ratio": "3 / 4", "text": "<p>Placeholder review. Replace with a real customer review about how their portrait looks.</p>"}),
    ("review", {"name": "Customer Name", "date": "08/30/2026", "placeholder_ratio": "3 / 4", "text": "<p>Placeholder review. Very happy with our pictures, they both came out great.</p>"}),
    ("review", {"name": "Customer Name", "date": "09/06/2026", "placeholder_ratio": "2 / 3", "text": "<p>Placeholder review. Share a longer story here about who the portrait was for and what the moment meant to the family receiving it.</p>"}),
    ("review", {"name": "Customer Name", "date": "09/03/2026", "placeholder_ratio": "2 / 3", "text": "<p>Placeholder review. Longer reviews are clamped to six lines with a Read more link, so customers can tell their whole story without the card growing too tall. Add as much detail as you like here and it will be revealed when the shopper taps Read more below.</p>"}),
    ("review", {"name": "Customer Name", "date": "08/31/2026", "placeholder_ratio": "2 / 3", "text": "<p>Placeholder review. The picture came out amazing, exactly what I expected.</p>"}),
    ("review", {"name": "Customer Name", "date": "08/31/2026", "placeholder_ratio": "2 / 3", "text": "<p>Placeholder review. This is where an emotional customer story goes — what they felt when they opened the package and saw the portrait for the first time. Other family members ordered too after seeing it.</p>"}),
    ("review", {"name": "Customer Name", "date": "08/31/2026", "placeholder_ratio": "2 / 3", "text": "<p>Placeholder review. It's beautiful! I finally feel a sense of peace looking at my picture.</p>"}),
    ("review", {"name": "Customer Name", "date": "08/30/2026", "placeholder_ratio": "3 / 4", "text": "<p>Placeholder review. Absolutely love the picture, best purchase I've made.</p>"}),
    ("review", {"name": "Customer Name", "date": "08/30/2026", "placeholder_ratio": "2 / 3", "text": "<p>Placeholder review. Love the photo of my sweet little girl.</p>", "item": "Fine Art Poster"}),
]

FAQ_PRINTS = [
    ("How long until my order arrives?", "<p>Digital files arrive by email within minutes of checkout, worldwide. Printed gifts are made to order: allow 5-8 days within the USA, or an estimated 2-3 weeks for international delivery.</p>"),
    ("What's the difference between the poster and the canvas?", "<p>The poster is printed on museum-quality archival paper and arrives rolled, ready for a frame of your choosing. The canvas is printed on gallery-wrapped cotton canvas and arrives ready to hang.</p>"),
    ("Do you ship internationally?", "<p>Digital portraits are available worldwide. We offer fine art posters internationally, subject to the delivery options at checkout, in 12×18″, 16×24″ and 24×36″.</p>"),
    ("How much does shipping cost?", "<p>Shipping is calculated at checkout and shown before you pay, so nothing is added afterwards. Digital files have nothing to ship at all.</p>"),
    ("Will I get a tracking number?", "<p>Yes. As soon as your poster or canvas ships we'll email you a tracking number so you can follow it right to your door.</p>"),
    ("What does Skip the Line do?", "<p>It moves your order to the front of the day's queue, so yours is made ahead of the orders waiting in front of it. You can add it to any format at checkout.</p>"),
    ("How is the digital download delivered?", "<p>By email, within minutes of checkout. You'll get a link to download your full-resolution, watermark-free portrait, and it stays yours to download again whenever you need it.</p>"),
    ("What size should I print my digital download at?", "<p>Our digital files are high-resolution and look great from 8×12″ up to 24×36″. For the sharpest result, print at 300 DPI.</p>"),
]

FAQ_SUNCATCHER = [
    ("What exactly do I receive?", "<p>A round disc of glass printed with your artwork, set in a gold-tone metal rim with a chain to hang it by. It's made to order, one at a time, from the preview you approve.</p>"),
    ("Which size should I pick?", "<p>The 6 inch is the one most people choose — big enough that every face reads clearly from across the room. The 4 inch suits a small kitchen window, and the 10 inch makes a statement piece.</p>"),
    ("How long until it arrives?", "<p>It's made to order and arrives in 5-8 days within the USA, or 2-3 weeks elsewhere, and you'll get a tracking number as soon as it goes out.</p>"),
    ("Do you ship internationally?", "<p>Suncatchers are available in the United States only. Elsewhere, digital portraits and posters are available, subject to the delivery options at checkout.</p>"),
    ("Will the faces still look like them?", "<p>Yes. The background and clothing are built from panes of coloured glass, but the faces and hands are kept true to your photo so every person is recognisable.</p>"),
    ("Is the preview really free?", "<p>Yes. Upload a photo, pick a scene, and see your suncatcher in under a minute. No payment, no sign-up, and no obligation to order.</p>"),
    ("What if it arrives damaged?", "<p>Send us a photo of the item and the packaging within 14 days of delivery and we'll replace it free of charge or refund you.</p>"),
]


def faq(heading, qa):
    return section("sg-faq", {"heading": heading, "anchor": "faq", "schema_markup": True},
                   [("question", {"question": q, "answer": a}) for q, a in qa], "q")


def reviews(button=True):
    return section("sg-reviews", {
        "heading": "Reviews", "uppercase": True, "page_heading": False, "intro": "",
        "rating": "4.8", "count_text": "based on 506 verified reviews", "item_label": "Item type:",
        "button_label": "Read all 506 reviews" if button else "",
        "button_link": "/pages/reviews" if button else "",
    }, REVIEW_ITEMS, "r")


def before_after(sub):
    return section("sg-before-after", {
        "heading": "See the Magic", "subheading": sub, "before_label": "Before", "after_label": "After",
        "start": 50, "caption": "Drag the slider to reveal each transformation.", "anchor": "examples",
    }, [("pair", {"before_alt": "Original photo", "after_alt": "Finished portrait"})] * 4, "p")


def how(sub, steps):
    return section("sg-how-it-works", {"heading": "How it works", "subheading": sub, "anchor": "how-it-works"},
                   [("step", {"icon": i, "title": t, "text": f"<p>{x}</p>"}) for i, t, x in steps], "s")


PORTRAIT_STEPS = [
    ("cloud-upload", "Upload your photo", "Add a clear photo of yourself, your family, or a loved one. Solo, couple, or the whole group."),
    ("sparkles", "Choose a style", "Pick a style — a warm portrait, a walk at golden hour, a storytelling scene, or a memorial tribute."),
    ("download", "Get your free preview", "See your portrait in under a minute. Love it? Download the full high-resolution art."),
]
SUN_STEPS = [
    ("cloud-upload", "Upload your photo", "A clear, well-lit photo of one or two faces works best — the disc is round, so the closer the faces, the more of them it holds."),
    ("sparkles", "Choose your scene", "Pick from our scenes — each one built as a real leaded stained glass window."),
    ("eye", "See it in the glass", "Your free preview arrives in under a minute, already hanging in the window. Love it? Pick your size and we'll make it."),
]


def hero(product=None, heading="", subtitle="", style_label="Choose your portrait style", styles=(), badge="Customer portrait"):
    settings = {
        "heading": heading, "heading_tag": "h1", "subtitle": subtitle,
        "cta_label": "Generate My Portrait", "cta_pill": "Free preview", "sticky_label": "Upload your photo",
        "show_proof": True, "rating": "4.8", "review_count_text": "506 verified reviews", "reviews_link": "#reviews",
        "badge": badge, "meta_1": "<strong>4.8/5</strong> customer rating", "meta_2": "<strong>Free</strong> preview",
        "style_label": style_label, "style_property": "Style",
        "enable_upload": True, "upload_required": True, "reveal_after_upload": True, "photo_property": "Photo",
        "upload_title": "Click to Upload Clear, Well-Lit Photos", "upload_note_strong": "Free preview",
        "upload_note": "— no credit card required", "upload_change_label": "Change photo",
        "upload_error": "Please upload a photo before adding to cart.",
        "private_strong": "100% Private & Secure", "private_text": "— your photos are never shared",
        "format_label": "Choose your format", "total_label": "Total", "button_label": "Add to cart",
        "show_dynamic_checkout": False, "buy_note": "Secure checkout · Made to order · Ships tracked",
    }
    if product:
        settings["product"] = product
    items = []
    for i, s in enumerate(styles):
        name, badge_txt = (s if isinstance(s, tuple) else (s, ""))
        items.append(("style", {"name": name, "badge": badge_txt, "slide": 0}))
    return section("sg-hero-product", settings, items, "style")


def template(sections_list):
    secs, order = {}, []
    for key, sec in sections_list:
        secs[key] = sec
        order.append(key)
    return {"sections": secs, "order": order}


PORTRAIT_STYLES = [("Warm", "Best Seller"), "Walking", "Preaching", "Memorial"]

# ---------------------------------------------------------------- home
write("templates/index.json", template([
    ("hero", hero("classic-portrait", "Bless Your Loved Ones With a Beautiful Custom Portrait",
                  "Ready in About 60 Seconds — No Payment or Sign-Up Required", styles=PORTRAIT_STYLES)),
    ("examples", before_after("Four real Warm transformations")),
    ("how", how("Three simple steps to a portrait your family will treasure.", PORTRAIT_STEPS)),
    ("reviews", reviews()),
    ("faq", faq("Shipping & Ordering Questions", FAQ_PRINTS)),
]))

# ---------------------------------------------------------------- product pages
LANDINGS = {
    "product.json": ("", "Ready in About 60 Seconds — No Payment or Sign-Up Required", PORTRAIT_STYLES, "Four real Warm transformations"),
    "product.kids.json": ("Turn Your Child Into a Storybook Cartoon", "A Keepsake They'll Treasure — Free Preview in About 60 Seconds", [("Riverside", "Best Seller"), "Playtime", "Bedtime", "Adventure"], "Four real storybook transformations"),
    "product.pets.json": ("Celebrate Your Pet With a Beautiful Portrait", "Ready in About 60 Seconds — No Payment or Sign-Up Required", [("Warm", "Best Seller"), "Garden", "Rainbow Bridge", "Memorial"], "Four real pet transformations"),
    "product.wedding.json": ("Your Wedding, Turned Into Timeless Art", "Ready in About 60 Seconds — No Payment or Sign-Up Required", [("Sacred Vows", "Best Seller"), "Golden Hour", "First Dance", "Anniversary"], "Four real wedding transformations"),
}
for fname, (heading, sub, styles, ba_sub) in LANDINGS.items():
    write(f"templates/{fname}", template([
        ("main", hero(None, heading, sub, styles=styles)),
        ("examples", before_after(ba_sub)),
        ("how", how("Three simple steps to a portrait your family will treasure.", PORTRAIT_STEPS)),
        ("reviews", reviews()),
        ("faq", faq("Shipping & Ordering Questions", FAQ_PRINTS)),
    ]))

SUNCATCHERS = {
    "product.suncatcher.json": ("Your Photo, Set in Glass and Lit by the Sun", [("Warm", "Best Seller"), "Walking", "Memorial"]),
    "product.pet-suncatcher.json": ("Your Pet, Set in Glass and Lit by the Sun", [("Warm", "Best Seller"), "Halo", "Memorial"]),
}
for fname, (heading, styles) in SUNCATCHERS.items():
    h = hero(None, heading, "Free Preview in About 60 Seconds — Made to Order in Real Glass",
             style_label="Choose your scene", styles=styles, badge="Customer suncatcher")
    h["settings"]["cta_label"] = "Create My Suncatcher"
    h["settings"]["format_label"] = "Choose your size"
    write(f"templates/{fname}", template([
        ("main", h),
        ("showcase", section("sg-video-showcase", {
            "heading": "See It in the Light",
            "subheading": "Real glass, a gold rim and a chain — turned in the hand so you can see it move."})),
        ("how", how("Three simple steps to a suncatcher your family will treasure.", SUN_STEPS)),
        ("reviews", reviews()),
        ("faq", faq("Questions About Your Suncatcher", FAQ_SUNCATCHER)),
    ]))

# ---------------------------------------------------------------- pages
FOOT = '<p>Questions? Email <a href="mailto:support@yourstore.com">support@yourstore.com</a> or call <a href="tel:+15555555555">+1 (555) 555-5555</a>.</p>'
DOC_SETTINGS = {"show_title": True, "title": "", "show_updated": True, "updated_label": "Last updated:", "updated_date": "", "foot": FOOT}

write("templates/page.json", template([
    ("main", section("sg-doc", dict(DOC_SETTINGS), [("page_content", {})], "c")),
]))

write("templates/page.contact.json", template([
    ("main", section("sg-doc", dict(DOC_SETTINGS, title="Contact Us"), [
        ("intro", {"text": "<p>Questions about a portrait, an order or anything else? Our customer care team is happy to help.</p>"}),
        ("text", {"heading": "Email", "text": '<p>The fastest way to reach us is by email at <a href="mailto:support@yourstore.com">support@yourstore.com</a>. We answer every message and typically reply within one business day.</p>'}),
        ("text", {"heading": "Phone", "text": '<p>Call us at <a href="tel:+15555555555">+1 (555) 555-5555</a>. Phone support is available Monday to Friday, 9:00 AM–6:00 PM (EST).</p>'}),
        ("text", {"heading": "Mailing address", "text": "<p>Your Store Name<br>123 Main Street<br>City, ST 00000<br>United States</p>"}),
        ("text", {"heading": "Help with an existing order or creation", "text": '<p>Include your order number so we can find your portraits quickly.</p><p>For delivery timelines see the <a href="/pages/shipping-ordering">Shipping &amp; Ordering page</a>, and for refund or replacement requests see the <a href="/pages/refunds-replacements">Refunds &amp; Replacements policy</a>. To change or cancel an order within 8 hours, see our <a href="/pages/cancellation-policy">Cancellation Policy</a>.</p>'}),
        ("contact_form", {"heading": "Send us a message", "order_label": "Order number (optional)"}),
        ("page_content", {}),
    ], "c")),
]))

write("templates/page.how-it-works.json", template([
    ("main", section("sg-doc", dict(DOC_SETTINGS), [
        ("intro", {"text": "<p>Turning a photo into a keepsake portrait takes three steps and about a minute for your first look.</p>"}),
        ("steps", {
            "icon_1": "cloud-upload", "title_1": "1. Upload your photo",
            "text_1": "<p>Add a clear photo of your family, a loved one, or a pet. Solo, couple, or the whole group — you can upload multiple photos of different people and we'll merge everyone into one scene.</p>",
            "icon_2": "sparkles", "title_2": "2. Choose a style",
            "text_2": "<p>Pick a style — Warm, Walking, Preaching, or Memorial, a tribute portrait in loving memory.</p>",
            "icon_3": "download", "title_3": "3. Get your free preview",
            "text_3": "<p>See your portrait in under a minute, watermarked so you can judge the result risk-free. Love it? Purchase to unlock the full high-resolution, watermark-free artwork.</p>",
        }),
        ("text", {"heading": "Free daily generations", "text": "<p>You can generate up to <strong>6 free previews per day</strong>. If a preview doesn't come out the way you hoped, try a brighter or more clearly lit photo, or simply generate again.</p>"}),
        ("text", {"heading": "Want a small change instead of starting over?", "text": "<p>Once a preview is ready, click <strong>Edit this photo</strong> under it and describe exactly what you'd like changed. We'll apply just that change to your existing portrait.</p>"}),
        ("icon_list", {
            "heading": "After you purchase",
            "icon_1": "shield", "text_1": "<p>Digital downloads unlock instantly — a clean, full-resolution, watermark-free file delivered to your email right after checkout.</p>",
            "icon_2": "clock", "text_2": '<p>Fine art prints are made to order and ship tracked — see our <a href="/pages/shipping-ordering">Shipping &amp; Ordering</a> page for timelines.</p>',
        }),
        ("page_content", {}),
    ], "c")),
]))

write("templates/page.track.json", template([
    ("main", section("sg-track", {
        "title": "Track your order",
        "subtitle": "See your shipping status or re-download your portrait — just enter your email.",
        "email_label": "Email", "placeholder": "you@example.com", "help": "The email you used at checkout.",
        "note": "We'll email you a one-time code to keep your portraits and orders private.",
        "button_label": "Email me a code",
        "foot": '<p>Prints arrive in 5–8 days within the USA, or 2–3 weeks elsewhere. Digital images are ready to download within minutes of checkout. Still stuck? Email <a href="mailto:support@yourstore.com">support@yourstore.com</a> or call <a href="tel:+15555555555">+1 (555) 555-5555</a>.</p>',
    })),
]))

rv = reviews(button=False)
rv["settings"].update({
    "heading": "Thousands of Positive Reviews", "uppercase": False, "page_heading": True,
    "intro": "<p>With so many happy customers who love what they received, you can be sure you'll be happy too. Check what our <a href=\"#reviews\">amazing customers</a> are saying about us below.</p>",
})
rv["blocks"].update({f"r_{i}": {"type": "review", "settings": dict(REVIEW_ITEMS[(i - 1) % 9][1])} for i in range(10, 16)})
rv["block_order"] += [f"r_{i}" for i in range(10, 16)]
write("templates/page.reviews.json", template([("main", rv)]))

# ---------------------------------------------------------------- section groups
DRAWER = [
    ("drawer_item", {"title": "Classic Portrait", "link": "/"}),
    ("drawer_item", {"title": "Kids", "link": "/products/kids-cartoon-portrait"}),
    ("drawer_item", {"title": "Pets", "link": "/products/pet-portrait"}),
    ("drawer_item", {"title": "Suncatcher", "link": "/products/photo-suncatcher"}),
    ("drawer_item", {"title": "Pet Suncatcher", "link": "/products/pet-suncatcher"}),
    ("drawer_item", {"title": "Wedding", "link": "/products/wedding-portrait"}),
    ("drawer_link", {"title": "Track My Order", "link": "/pages/track"}),
    ("drawer_link", {"title": "My Portraits", "link": "/account"}),
    ("drawer_link", {"title": "Contact", "link": "/pages/contact"}),
]
write("sections/header-group.json", {
    "name": "Header",
    "type": "header",
    "sections": {
        "announcement": section("sg-announcement", {"text": "SITEWIDE SALE | 30% OFF EVERYTHING", "link": "", "bg": "#3F2D6B", "color": "#FFFCF7"}),
        "topbar": section("sg-topbar", {
            "hide_on_pages": True, "tabs_label": "Product types",
            "subbar_text": "Free Preview · Pay Only If You Love It", "subbar_link_label": "Track My Order", "subbar_link": "/pages/track",
        }, [
            ("tab", {"label": "Prints", "icon": "frame", "link": "/", "match_handle": "classic-portrait"}),
            ("tab", {"label": "Suncatcher", "icon": "sun", "link": "/products/photo-suncatcher", "match_handle": "photo-suncatcher"}),
        ], "tab"),
        "header": section("sg-header", {
            "logo_width": 241, "logo_width_mobile": 160, "cart_visibility": "items", "show_account": False,
            "drawer_title": "Menu", "simple_on_pages": True, "logo_width_simple": 112, "back_label": "Back to home",
        }, DRAWER, "menu"),
    },
    "order": ["announcement", "topbar", "header"],
})

write("sections/footer-group.json", {
    "name": "Footer",
    "type": "footer",
    "sections": {
        "footer": section("sg-footer", {
            "logo_width": 169, "care_heading": "Customer care", "email": "support@yourstore.com",
            "phone": "+1 (555) 555-5555", "hours": "Hours: 9:00 AM–6:00 PM (EST)", "days": "Monday to Friday",
            "address": "123 Main Street\nCity, ST 00000",
            "menu_1_heading": "Explore", "menu_1": "footer-explore",
            "menu_2_heading": "Support", "menu_2": "footer-support",
            "menu_3_heading": "Legal", "menu_3": "footer-legal",
            "show_newsletter": True, "newsletter_heading": "Join our email list",
            "newsletter_text": "Get early access to new portrait styles and special offers.",
            "show_payments": True, "payments_label": "Secure payments",
            "note": "", "show_language": True, "copyright": "All rights reserved.",
        }),
    },
    "order": ["footer"],
})
print("templates written")
