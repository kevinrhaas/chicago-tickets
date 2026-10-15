---
id: T-2499
title: 1808 Prairie's flat top, height and bow from the 1888 Inland Architect plate: the hip, dormer and cresting replaced by a flat roof behind a front parapet standing over Glessner's ridge, the bow stopped at the second storey under a flat moulded cap, and the third storey run flat across the front as a six-light arcade
state: review
epic: SOUTH_TIME
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-1882
opened: 2026-10-15
closed: null
pr: 809
claimed_by: run 10/15/2026, 1:09:17 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38689904278
claimed_at: 2026-10-15T06:09:17.922Z
decision: null
decision_answer: null
---

1808 Prairie's flat top, height and bow from the 1888 Inland Architect plate: the hip, dormer and cresting replaced by a flat roof behind a front parapet standing over Glessner's ridge, the bow stopped at the second storey under a flat moulded cap, and the third storey run flat across the front as a six-light arcade.

Piece 1 of 2 of **T-1882 — Refine 1808 Keith-Field neighbour of Glessner envelope**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-1882 was split (2026-10-15T06:09:08.823Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 5m ago, run 10/15/2026, 1:04:29 AM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/38689904278) — held by the run that split it

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/38689904278) may be working one of the pieces now.

**Acceptance:** (stated before building, 2026-10-15) — one demonstration, in the published /1904/ app at 1280x800 and 390x780, from the same four stands before and after (`tools/qa_k01_t2499.mjs`):

1. No hip, slate, dormer or cresting: a flat top behind a front parapet whose top stands over Glessner's ridge (15.5 m), with the floors and the wall head where the 1888 plate's courses put them, each reading `inferred` on `inland_architect_1888_02_keith_plate`.
2. The south bow sized from the plan under the plate and stopped at floor 3 under a moulded cap, with the plate's three principal-storey and four second-storey lights; the third storey runs flat across the front over it as a six-light arcade.
3. The K01 measure stays clean (no coincident or degenerate faces), every other K01/K12/K13/K16/draft mesh re-emits byte-identical, and `check.sh` is green.
4. What is reconstructed (parapet height rule, deck, stacks, arcade spacing) and what is deferred (principal floor at 1.5 m, the loggia and stair to T-2500, the finish to T-1883) are written in docs/LIBERTIES.md.

Not in this piece: the plate's camera for the image gate (its scan is `check_required`), which stays with T-1883.
