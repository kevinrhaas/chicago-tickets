---
id: T-2583
title: KTX2 for the CPU-packed sheets: frontage's luminance ratio, wall-relief's orl pack and signage's grain derived at convert time and shipped as KTX2, captures at the anchors within the photo-match tolerance (any visible ETC1S loss moved to UASTC), measure_memory showing the sheets' GPU bytes down 4x on phone with the ceiling lowered, and SITE-BUDGET re-measured
state: open
epic: RENDERING
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: T-2551
opened: 2026-10-16
closed: null
pr: null
claimed_by: null
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: null
decision: null
decision_answer: null
---

KTX2 for the CPU-packed sheets: frontage's luminance ratio, wall-relief's orl pack and signage's grain derived at convert time and shipped as KTX2, captures at the anchors within the photo-match tolerance (any visible ETC1S loss moved to UASTC), measure_memory showing the sheets' GPU bytes down 4x on phone with the ceiling lowered, and SITE-BUDGET re-measured.

Piece 2 of 2 of **T-2551 — KTX2 in the renderer: vendor KTX2Loader and the Basis transcoder from the pinned three tarball, and ship the runtime library sheets GPU-compressed with mip 0 skipped on light**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

## Finding from T-2582 (2026-10-16)

- **The ground strip's sand basecolor is this piece's too.** `ground-strip.js` reads its pixels for `meanLinearLuma`, so it stays PNG and has no `.ktx2`. `tools/ktx2_sheets.py --check` refuses an orphan, so add it to that script's sheet list once its luma comes from somewhere else.
- **The boot budget will not fit this piece as it stands.** After T-2582, `measure_boot_payload.mjs --check` reads 12.858 of 13.000 MB. The roof KTX2s alone cost +0.403 MB over their WebPs, and UASTC data maps are bigger on the wire than lossless WebP. The wall sheets load at every 1835 boot. See SITE-BUDGET § 4c for the itemised cost and the named lever.
- The path is ready to use: `loadSheet(ktx2Beside(url), url, loader, { srgb })` from `js/ktx2.js`, the converter's codec choice, and `measure_memory.mjs --ktx2-off` for the before reading.
