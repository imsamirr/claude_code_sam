# Retra product-page gallery (2000x2000): Chalk, Obsidian and Sol

Retra versions of seven competitor gallery layouts: hand-held hero, how-to grid, USB-C flat lay, front/back, filter grid, gift flat lay and what's in the box.
The reviews image is skipped until real Retra reviews exist. Contact sheet: `output/RET_gallery_contact_sheet.jpg`.

- Words: `gallery_copy.json`, written by StefanBrain (project "Retra Launch"); none of the competitor's wording is used.
- Type: landing-page gallery style. Tinos headlines at -0.04em and Inter labels, in navy #022B49, on cream #F3EEE4.
- Scenes: `render_gallery.py` (Kie Nano Banana Pro 2K, reference-guided from `assets/retra/product/`). The competitor's photos were never used as references.
- **`_RENDERED-BACK` files show the back, bottom and USB-C views, which have no real-photo reference.** They follow the landing page's existing Kie renders (`base/`): the back view is the landing page's own render, and the bottom view is that render recoloured pixel-by-pixel (`recolour_bottom.py`, ports untouched). Check them against a real unit before going live.
- Chalk front cutout: `cutout_chalk_front.py` uses a Kie green-screen copy as the mask.

Rebuild: `python3 compose_gallery.py` (raw renders are committed as JPEG; the 2K PNGs stay local).

- `filters_*_ILLUSTRATIVE`: the four sample photos are the landing page's Kie renders (`base/f-*.jpg`, upscaled), not photos taken with a Retra. Replace them with real samples when you have them.
- Gift and in-the-box images: the box carries only the gold "Retra" wordmark (Kie-invented packaging, per Sam). There's no gift offer, and the memory card capacity isn't stated.

## Packaging (in the style of Sam's box reference)
- `packaging/retra_box_front_<colour>.png`: box front panel, 2400x1500 (`packaging.py`). `packaging/retra_box_lid.png` is the lid, with branding only.
- Words by StefanBrain (`gallery_copy.json["packaging"]`); icons drawn in code. No eco or green claim (not substantiated).
- The gift and in-the-box gallery images show this artwork printed onto Kie-rendered blank boxes (`print_box.py`, `print_gift.py`; the face corners are in `picks.json`).

## Retropia-style set (macro, float, flow, split, portrait)
- `macro_*`, `float_*`, `flow_*`: Chalk, Obsidian and Sol. `split_ILLUSTRATIVE` and `portrait_ILLUSTRATIVE`: one version each.
- The split and portrait images are simulations: the landing page's Vintage look applied to Kie renders. The captions say
  "simulated" and never "shot with Retra". Replace them with real Retra photos when you have them.
- The flow image compares a generic, unbranded disposable camera with Retra. It doesn't imply Retra is built from disposable parts.
- Words by StefanBrain (`gallery_copy.json`). Fonts: Inter ExtraBold headline at -0.05em plus a Tinos serif subhead, in navy.
