# Retra Shopify product images: backdrop recoloured to #F2EEE3

Product: "Retra Screen-Free Camera" (RECLAIM NUTRA), 16 media.
- `original/`: backups of the 16 images as they were on Shopify (2026-11-26).
- `recoloured/`: the same 16 images with the backdrop moved to #F2EEE3 (the cream of the front/back gallery image).
  The gallery images use the latest local versions (printed Retra box with the navy wordmark).
- `recolour_bg.py`: the method. The backdrop is grown from the image edge and stopped by hard object edges, so
  shadows keep their shape. The hand photo (`retra-g6-hand.jpg`) uses a colour-only mask because the skin
  matches the old tan backdrop.
- `media.json`: Shopify MediaImage id -> file name. The plan is to replace each file in place with `fileUpdate`
  (originalSource), so variant images and gallery order stay the same.

Uploaded 2026-11-26 (Sam approved): all 16 replaced in place with fileUpdate. Same media IDs, variant images and order; verified the live backgrounds are #F2EEE3 (+/-2 from JPEG). To roll back, re-upload the files in original/ the same way.
