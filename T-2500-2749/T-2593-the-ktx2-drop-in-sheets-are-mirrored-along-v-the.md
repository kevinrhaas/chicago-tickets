---
id: T-2593
title: The KTX2 drop-in sheets are mirrored along v: the roof relief, the 1904 street surfaces and the muck written top row first, so three lays them upside down against their WebPs
state: claimed
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-10-16
closed: null
pr: null
claimed_by: run 10/16/2026, 9:52:39 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38916797385
claimed_at: 2026-10-16T14:52:39.412Z
decision: null
decision_answer: null
---

The KTX2 drop-in sheets are mirrored along v: the roof relief, the 1904 street surfaces and the muck written top row first, so three lays them upside down against their WebPs.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## What was measured (T-2588, 2026-10-16)

- **three uploads a KTX2 with its first row at v = 0 and cannot flip a compressed texture; an image texture goes up `flipY`, its top row at v = 1.** A 64 px test sheet, top half red and bottom half blue, written by `ktx create` exactly as `tools/ktx2_sheets.py` writes the drop-ins, and drawn on a full-screen quad in headless Chromium through the vendored KTX2Loader: the pixel near the top of the screen read **blue** from the `.ktx2` and **red** from the PNG.
- So every drop-in T-2582 shipped — the two roof coverings' `normal_gl` and `orm`, the 1904 street surfaces' basecolor/normal/ORM and the wet prairie muck — is the image MIRRORED along v on the KTX2 path. On a normal map that also inverts the relief's up-slope (the T-2300 defect class): shingle butts lit from the wrong side.
- Seen in the scene: `tools/wall_relief_shots.mjs --compare ktx2`, desktop `close-fresh` (recon_1835_blk_lake_market_d4_02), roof band (x 300-1000, y 10-150): **29-30 dB** between `?ktx2=0` and the KTX2 path, with the course lines at visibly different places, where the walls on T-2588's bottom-row-first sheets read 50-51 dB.

## The fix

`master()` in `tools/ktx2_sheets.py` already takes `rows`; give the drop-ins `rows='bottom'` (the walls carry it since T-2588), re-convert, and re-shoot the roof stands and a 1904 street with `--compare ktx2` until the roof band reads as the walls do. Then the photo-match records that rest on the 1904 streets.
