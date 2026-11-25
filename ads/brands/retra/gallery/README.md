# Retra product-page gallery (2000x2000): Chalk, Obsidian and Sol

Retra versions of four competitor gallery layouts (hand-held hero, how-to grid, USB-C flat lay, front/back).
The reviews image is skipped until real Retra reviews exist. Contact sheet: `output/RET_gallery_contact_sheet.jpg`.

- Words: `gallery_copy.json`, written by StefanBrain (project "Retra Launch"); none of the competitor's wording is used.
- Type: landing-page gallery style. Tinos headlines at -0.04em and Inter labels, in navy #022B49, on cream #F3EEE4.
- Scenes: `render_gallery.py` (Kie Nano Banana Pro 2K, reference-guided from `assets/retra/product/`). The competitor's photos were never used as references.
- **`_RENDERED-BACK` files show the back, bottom and USB-C views, which have no real-photo reference.** They follow the landing page's existing Kie renders (`base/`): the back view is the landing page's own render, and the bottom view is that render recoloured pixel-by-pixel (`recolour_bottom.py`, ports untouched). Check them against a real unit before going live.
- Chalk front cutout: `cutout_chalk_front.py` uses a Kie green-screen copy as the mask.

Rebuild: `python3 compose_gallery.py` (raw renders are committed as JPEG; the 2K PNGs stay local).
