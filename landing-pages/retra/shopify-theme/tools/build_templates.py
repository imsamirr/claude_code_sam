"""Builds templates/index.json and templates/product.retra.json for the Retra theme.
Copy: StefanBrain (copy/11-15 and copy/16-stefanbrain-shopify-slots.md)."""
import json, os, html

IMG = lambda f: f"shopify://shop_images/retra-{f}"
OUT = os.path.join(os.path.dirname(__file__), '..', 'templates')

FAQ = [
 ("How does Retra work?", "Turn it on, choose your filter, look through the optical viewfinder, and press the shutter button. There is no back screen to review your shots. When you want to see your photos, plug Retra into your phone or laptop with the included USB-C cable."),
 ("I have an iPhone with a Lightning port. How do I transfer photos?", "iPhones with a Lightning port cannot transfer photos over a direct USB-C to Lightning cable. You can insert the included SD card into a Lightning card reader adapter to import directly, or plug Retra into a computer and sync the files."),
 ("What is the image quality like?", "Retra is built with a nostalgic, film-like aesthetic rather than smartphone sharpness. Images feature warm color tones, gentle grain, and retro digital character reminiscent of classic point-and-shoot cameras."),
 ("Do I need to buy film or pay a lab for developing?", "No. Retra is fully digital, so there are no film rolls to buy and zero development fees. All photos save as standard JPEG files to the included SD memory card."),
 ("How many photos can I take on one charge?", "The built-in rechargeable lithium battery powers about 500 shots per charge, and the included memory card holds roughly 500 photos. Once you offload your photos to a computer or phone, simply clear the card and shoot again."),
 ("What comes inside the box?", "Every box includes your Retra camera, an SD memory card, a USB charging and transfer cable, a wrist strap, a quick start guide, and a complimentary gift ribbon."),
 ("Does the camera have a flash for night photos?", "Yes. Retra includes a built-in LED flash that gives evening gatherings, parties, and night walks that classic, high-contrast direct-flash film look."),
 ("Can I change between filters while shooting?", "Yes. You can switch between Natural, Vintage, Black & White, and Film whenever you like. The selected profile applies straight to each JPEG photo as you take it."),
]
E = html.escape
SPECS = ["Screen-free design: live in the moment without screens", "4 built-in filters (Natural, Vintage, Black & White, Film)", "8MP image resolution (3264 x 2448)", "Fixed-focus lens (0.5 m to infinity)", "Built-in LED flash", "Built-in rechargeable lithium battery (about 500 shots per charge)", "OLED shot counter", "Memory card support (JPEG format)", 'Pocket-sized design: 4.5" x 2.6" x 1.3" (115 x 65 x 33.5 mm)']
SHIP = ("<p>All orders ship within 1-2 business days.</p>"
        "<p>All orders ship with tracked delivery. As soon as your package leaves our studio, you will receive a tracking link via email to follow its progress right to your door.</p>"
        "<p>Love your Retra or return it. We offer a 30-day hassle-free return window on all orders. If you need assistance with an order or a return, reach out directly through our <a href=\"/pages/contact\" title=\"Contact page\">Contact page</a>.</p>")

REVIEWS = [
 ("rv-florence.jpg", "Julian K.", "Brought two of these for our train trip through northern Italy. Not checking my phone every five minutes made the whole vacation feel twice as long. The warm vintage tones on the cobblestones looked incredible."),
 ("m-carousel.jpg", "Sarah P.", "We spent three full days at the theme parks with our two kids. The battery lasted through twelve hours of rides and evening fireworks without dying once."),
 ("rv-seville.jpg", "Sophie L.", "Took this all through Spain. It feels just like using a disposable camera, but with zero film lab fees. Everyone kept asking where we got it."),
 ("m-beach.jpg", "Chloe H.", "Lived in my beach tote all week in San Diego. Zero glare issues in bright sunlight because you just look through the viewfinder."),
 ("rv-scotland.jpg", "Marcus T.", "The surprise of plugging it into my laptop when I got home was the best part. Captured the entire rail trip across the UK without draining my phone."),
 ("rv-parade.jpg", "Mike B.", "The built-in flash makes nighttime parade shots look like classic 90s family albums. Handed it to our eight-year-old and let him be the trip photographer."),
 ("rv-amsterdam.jpg", "Clara M.", "Rode bikes around Amsterdam for four days with this strapped to my wrist. Super lightweight, simple to use, and the black and white filter is gorgeous."),
 ("rv-boat.jpg", "Liam N.", "Tossed it around between four friends on the boat all afternoon. The film filter gives that perfect golden summer look."),
 ("rv-venice.jpg", "David R.", "We left our phones locked in the hotel room safe and just carried this around Venice. The photos have that authentic retro grain you just cannot get from an iPhone filter."),
 ("rv-castle.jpg", "Jessica W.", "Took our family to the big theme park for spring break. It was so refreshing to watch the castle fireworks with my own eyes instead of staring through a screen."),
 ("rv-footprints.jpg", "Emma D.", "Bought the 2-pack for a beach trip to the coast. Plugging it into my phone at the beach house each evening felt like unwrapping presents."),
 ("rv-dog.jpg", "Ben S.", "Keep this sitting on the kitchen counter for quiet mornings at home. Snaps candid moments of our dog that we would normally miss while unlocking a phone."),
]

def blocks(items):
    b, order = {}, []
    for i, (t, s) in enumerate(items, 1):
        k = f"{t}_{i}"; b[k] = {"type": t, "settings": s}; order.append(k)
    return b, order

def section(type_, settings, items=()):
    s = {"type": type_, "settings": settings}
    if items:
        s["blocks"], s["block_order"] = blocks(items)
    return s

def page(product_handle):
    buy_items = [
        ("badge", {"icon": IMG("ic-screen.png"), "text": "Screen-Free"}),
        ("badge", {"icon": IMG("ic-usb.png"), "text": "Instant USB-C Transfer"}),
        ("badge", {"icon": IMG("ic-battery.png"), "text": "500 Shots on One Charge"}),
        ("badge", {"icon": IMG("ic-eco.png"), "text": "Reusable & Rechargeable"}),
        ("accordion", {"title": "Product Details", "icon": "info", "use_description": True, "faq_style": False, "content": ""}),
        ("accordion", {"title": "Specs", "icon": "camera", "use_description": False, "faq_style": False, "content": "<ul>" + "".join(f"<li>{E(x)}</li>" for x in SPECS) + "</ul>"}),
        ("accordion", {"title": "Shipping & Returns", "icon": "truck", "use_description": False, "faq_style": False, "content": SHIP}),
        ("accordion", {"title": "FAQ's", "icon": "question", "use_description": False, "faq_style": True, "content": "".join(f"<p><strong>{E(q)}</strong></p><p>{E(a)}</p>" for q, a in FAQ)}),
    ]
    buy = {
        "product": product_handle or "",
        "default_color": "Aegean",
        "rating_text": "Rated <strong>4.8</strong>/5 stars out of <strong>1,753 reviews</strong>",
        "offer_pill": "BUY 1, GET 1 FREE",
        "stock_text": "Almost sold out",
        "color_label": "Choose your color:",
        "atc_label": "Add to Cart",
        "added_label": "Added to Cart ✓",
        "error_label": "Could not add to cart. Please check your connection and try again.",
        "pay_image": IMG("payments.png"),
        "pay_alt": "Accepted payments: Apple Pay, Google Pay, PayPal, American Express, Visa, Mastercard, Maestro and more",
        "returns_note": "Enjoy <strong>30 days of hassle-free returns</strong> if you do not love shooting with Retra.",
        "sticky_show": True,
        "sticky_sub": "Buy 1, Get 1 Free",
        "sticky_label": "Claim BOGO Offer",
    }
    if not product_handle:
        del buy["product"]
    sections = {
        "buybox": section("retra-buybox", buy, buy_items),
        "why": section("retra-why", {"kicker": "Built for presence", "heading": "Why Retra works.", "heading_2": "", "pad_top": 24}, [
            ("item", {"image": IMG("ic-screen.png"), "label": "SCREEN-FREE"}),
            ("item", {"image": IMG("ic-roll.png"), "label": "NO CAMERA ROLL"}),
            ("item", {"image": IMG("ic-storage.png"), "label": "PRE-LOADED STORAGE"}),
            ("item", {"image": IMG("ic-battery.png"), "label": "RECHARGEABLE BATTERY"}),
            ("item", {"image": IMG("ic-film.png"), "label": "VINTAGE FILM STYLE"}),
            ("item", {"image": IMG("ic-eco.png"), "label": "ECO FRIENDLY"})]),
        "looks": section("retra-looks", {"kicker": "Built-in film profiles", "heading": "Four classic looks,", "heading_2": "for every moment.", "button_label": "Shop now", "button_link": "#buy", "pad_top": 40}, [
            ("item", {"image": IMG("fl-natural.jpg"), "label": "Natural"}),
            ("item", {"image": IMG("fl-vintage.jpg"), "label": "Vintage"}),
            ("item", {"image": IMG("fl-bw.jpg"), "label": "Black & White"}),
            ("item", {"image": IMG("fl-film.jpg"), "label": "Film"})]),
        "how": section("retra-how", {"kicker": "Simple by design", "heading": "Four simple steps,", "heading_2": "from pocket to photos.", "pad_top": 20}, [
            ("step", {"image": IMG("how-1.jpg"), "title": "Turn on", "text": "Press the power switch."}),
            ("step", {"image": IMG("how-2.jpg"), "title": "Choose your filter", "text": "Natural, Vintage, B&W, or Film."}),
            ("step", {"image": IMG("how-3.jpg"), "title": "Shoot", "text": "Press the shutter. No preview screen."}),
            ("step", {"image": IMG("how-4.jpg"), "title": "Transfer via USB-C", "text": "Plug into your phone or laptop."})]),
        "compare": section("retra-compare", {"kicker": "Three ways to remember", "heading": "The magic of film,", "heading_2": "without the lab fees.",
            "text": "Disposables create ongoing lab costs and plastic waste. Phones pull you into notifications and editing apps. Retra delivers the analog surprise of film with the ease of digital.",
            "feature_label": "Feature", "img_1": IMG("cmp-retra.png"), "name_1": "Retra", "img_2": IMG("cmp-disposable.png"), "name_2": "Disposable", "img_3": IMG("cmp-phone.png"), "name_3": "Phone Camera", "pad_top": 20}, [
            ("row", {"label": "Screen & distraction free", "col_1": "yes", "col_2": "yes", "col_3": "no"}),
            ("row", {"label": "Authentic retro film look", "col_1": "yes", "col_2": "yes", "col_3": "no"}),
            ("row", {"label": "Reusable & rechargeable", "col_1": "yes", "col_2": "no", "col_3": "yes"}),
            ("row", {"label": "Zero film developing fees", "col_1": "yes", "col_2": "no", "col_3": "yes"}),
            ("row", {"label": "500 shots per charge", "col_1": "yes", "col_2": "no", "col_3": "no"}),
            ("row", {"label": "Instant USB-C transfer", "col_1": "yes", "col_2": "no", "col_3": "yes"}),
            ("row", {"label": "Price", "col_1": "low", "col_2": "high", "col_3": "low"})]),
        "reviews": section("retra-reviews", {"kicker": "Tested in the field", "heading": "Honest memories,", "heading_2": "captured without screens.",
            "rating_text": "Rated <strong>4.8</strong>/5 stars based on <strong>1,753+ customer stories.</strong>", "sample_note": "Sample reviews",
            "more_label": "Read more", "less_label": "Read less", "pad_top": 20},
            [("review", {"image": IMG(img), "name": n, "label": "Sample", "stars": 5, "text": f"“{t}”"}) for img, n, t in REVIEWS]),
        "moments": section("retra-moments", {"kicker": "Built for real life", "heading": "Built for memories,", "heading_2": "not for your feed.", "button_label": "Shop now", "button_link": "#buy", "pad_top": 20}, [
            ("item", {"image": IMG("mo-europe.jpg"), "label": "EUROPE", "big": False}),
            ("item", {"image": IMG("mo-themepark.jpg"), "label": "THEME PARKS", "big": False}),
            ("item", {"image": IMG("mo-beach.jpg"), "label": "BEACH", "big": False}),
            ("item", {"image": IMG("mo-roadtrip.jpg"), "label": "ROAD TRIPS", "big": False}),
            ("item", {"image": IMG("mo-party.jpg"), "label": "CELEBRATIONS", "big": True}),
            ("item", {"image": IMG("mo-everyday.jpg"), "label": "EVERYDAY", "big": True})]),
        "guarantee": section("retra-guarantee", {"kicker": "Risk-free field trial", "heading": "Take it on your travels, risk-free.",
            "text": "Take Retra on your next trip for 30 days. Experience what it feels like to leave your phone in your pocket, shoot without distraction, and rediscover your photos later. If you do not love the photos or the feeling of staying present, email our studio team. We will help you return it for a complete refund without hassle.",
            "more_label": "Read more", "less_label": "Read less", "image_left": IMG("rv-footprints.jpg"), "image_right": IMG("m-roadtrip.jpg"),
            "button_label": "Try Retra for 30 days risk-free", "button_link": "#buy"}, [
            ("row", {"icon": "returns", "title": "30-day field trial", "text": "Try it on your travels and return it easily if it is not for you."}),
            ("row", {"icon": "truck", "title": "Tracked delivery", "text": "Dispatched in 1-2 business days with full online door-to-door tracking."}),
            ("row", {"icon": "headset", "title": "A real person can help", "text": "Have a question about your camera or order? Send a message through our <a href=\"/pages/contact\" title=\"Contact page\">Contact page</a>."})]),
        "faq": section("retra-faq", {"heading": "Frequently asked questions", "open_first": True,
            "collage_1": IMG("rv-venice.jpg"), "collage_2": IMG("rv-amsterdam.jpg"), "collage_3": IMG("rv-scotland.jpg"),
            "collage_4": IMG("rv-seville.jpg"), "collage_5": IMG("rv-boat.jpg"), "collage_6": IMG("m-carousel.jpg")},
            [("question", {"question": q, "answer": f"<p>{E(a)}</p>"}) for q, a in FAQ]),
    }
    return {"layout": "retra", "sections": sections, "order": list(sections)}

for name, handle in (("index.json", "retra-screen-free-camera"), ("product.retra.json", None)):
    with open(os.path.join(OUT, name), "w") as f:
        json.dump(page(handle), f, ensure_ascii=False, indent=2)
    print("wrote", name, os.path.getsize(os.path.join(OUT, name)))
