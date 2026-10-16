---
id: T-2588
title: KTX2 for the wall relief: the clapboard and hewn-log orl derived at convert time and shipped with their normals as KTX2 through loadSheet, the canvas pack kept as the fallback, captures at the wall anchors within tolerance, measure_memory showing the wall sheets' GPU bytes down on phone, and the boot payload still under its ceiling
state: done
epic: RENDERING
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: T-2583
opened: 2026-10-16
closed: 2026-10-16
pr: 879
claimed_by: run 10/16/2026, 6:49:33 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-16T13:37:22Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38894669804
claimed_at: 2026-10-16T11:49:33.914Z
decision: null
decision_answer: null
---

KTX2 for the wall relief: the clapboard and hewn-log orl derived at convert time and shipped with their normals as KTX2 through loadSheet, the canvas pack kept as the fallback, captures at the wall anchors within tolerance, measure_memory showing the wall sheets' GPU bytes down on phone, and the boot payload still under its ceiling.

Piece 1 of 3 of **T-2583 — KTX2 for the CPU-packed sheets: frontage's luminance ratio, wall-relief's orl pack and signage's grain derived at convert time and shipped as KTX2, captures at the anchors within the photo-match tolerance (any visible ETC1S loss moved to UASTC), measure_memory showing the sheets' GPU bytes down 4x on phone with the ceiling lowered, and SITE-BUDGET re-measured**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2583 was split (2026-10-16T11:49:21.146Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 1m ago, run 10/16/2026, 6:48:50 AM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/38894669804) — held by the run that split it

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/38894669804) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

## Finding from T-2589 (2026-10-16) — the clapboard face is already in KTX2, and the boot needs the wall to use it

- **`clapboard_board_face_normal_gl.ktx2`, `_orm.ktx2` and `_grain.ktx2` are on T-2589's branch** (`steward/t2589-ktx2-frontage-timber`), written by `tools/ktx2_sheets.py` **bottom row first** (`FLIP_V`): a compressed texture uploads with flipY false, so a KTX2 written top-first lands mirrored along v against the flipY'd WebP, and a `normal_gl` mirrored without its green negated is lit upside down across the board. Flipped, the KTX2 path samples the texel the image path did — measured, the frontage captures match within 57-76 dB PSNR. Write the hewn log face (and any orl) the same way, or the wall's maps and the frontage's will disagree.
- **The boot budget only fits if the wall stops fetching the clapboard WebPs.** With the frontage on KTX2 and the wall still on `normal_gl.webp`/`orm.webp`/`basecolor.webp`, the boot reads **13.273 MB of 13.000** (12.861 before): the WebPs come down anyway. T-2589 waits on this ticket for that reason (SITE-BUDGET § 4d).
- **The clapboard wall needs no new file.** AO and roughness are the trio's `orm` R and G; the albedo ratio is the grain read back, `L / mean = 1 + (grain * 1.6 - 1) / 0.65` (frontage.js `GRAIN_HEADROOM`, `GRAIN_STRENGTH`; grain spans 107-195 of 255, so L / mean 0.49-1.34, about 0.0097 a level against the orl's 0.0078). Binding those three, the clapboard pair costs the boot about 1 KB over the WebPs it replaces; only the hewn log face needs files of its own.

## Acceptance, stated before the work, and the result (PR #879, merged)

1. The wall relief's normal and `orl` ship as KTX2, packed at convert time, with the canvas pack as the fallback. Done: the `orl` on ETC1S q255, the normal on UASTC, both bottom row first, and `<id>_orl.json` held by `--check`.
2. `wall_relief_shots.mjs --compare ktx2`, the wall band within codec tolerance, zero page errors. Done: 39-67 dB at 390x780 and 50.7-51.0 dB at 1280x800.
3. The walls' GPU bytes down on the 1835 phone, with the ceiling lowered. Done: 5.4 → 1.4 MB; merged reading 607.5 MB; ceiling 700 → 675 MiB.
4. The boot payload under 13.000 MiB. Done: 12.906 MiB (+48 KB). Frontage's clapboard WebPs are T-2589's lever.

Found: the T-2582 drop-ins are mirrored along v (T-2593).
