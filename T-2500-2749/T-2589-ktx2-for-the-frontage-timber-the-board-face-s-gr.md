---
id: T-2589
title: KTX2 for the frontage timber: the board face's grain modulation derived at convert time and shipped with its normal and orm as KTX2, the canvas pack kept as fallback, captures within tolerance and measure_memory down on phone
state: done
epic: RENDERING
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: T-2583
opened: 2026-10-16
closed: 2026-10-16
pr: 877
claimed_by: run 10/16/2026, 6:59:58 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-16T14:45:36Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38897112925
claimed_at: 2026-10-16T11:59:58.911Z
decision: null
decision_answer: null
---

KTX2 for the frontage timber: the board face's grain modulation derived at convert time and shipped with its normal and orm as KTX2, the canvas pack kept as fallback, captures within tolerance and measure_memory down on phone.

Piece 2 of 3 of **T-2583 — KTX2 for the CPU-packed sheets: frontage's luminance ratio, wall-relief's orl pack and signage's grain derived at convert time and shipped as KTX2, captures at the anchors within the photo-match tolerance (any visible ETC1S loss moved to UASTC), measure_memory showing the sheets' GPU bytes down 4x on phone with the ceiling lowered, and SITE-BUDGET re-measured**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2583 was split (2026-10-16T11:49:21.146Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 1m ago, run 10/16/2026, 6:48:50 AM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/38894669804) — held by the run that split it

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/38894669804) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

## Finding from T-2588 (2026-10-16)

- **Frontage can bind the walls' KTX2 pair and ship nothing new.** `frontage.js` RELIEF_DIR is `walls/clapboard_board_face`, the same sheet the wall relief binds, and since T-2588 that sheet carries `clapboard_board_face_normal_gl.ktx2` and `clapboard_board_face_orl.ktx2` (R = AO, G = roughness, B = 0.5 * L / mean(L), bottom row first). Frontage's `packGrain` modulation is `1 + GRAIN_STRENGTH * (L / mean - 1)` = `1 + GRAIN_STRENGTH * (2 * orl.B - 1)` (orl.B clamps L / mean at 2), and its `orm` slots read only R and G. So one shader edit lets frontage sample the orl the walls already fetched.
- **That is the boot budget's lever.** T-2588 left `measure_boot_payload.mjs` at 12.906 of 13.000 MiB (+48 KB) only because frontage still fetches the clapboard's three WebPs (0.433 MB) beside the walls' KTX2 pair; once frontage binds the pair, those three leave the boot.
