---
id: T-2692
title: Ground tiles built in Node: tools/prebuild_layers.mjs --layer ground runs terrain.js's own loadGlbMesh, conformGroundToField, tileGround and the spatial-batch partition for 1835 and writes each tile's pieces with an input hash, byte-equal to the page's ground batches (read from the live page), its determinism and stale-input refusal gated in check.sh
state: review
epic: RENDERING
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: T-2678
opened: 2026-10-16
closed: null
pr: 920
claimed_by: run 10/16/2026, 5:58:20 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38977949584
claimed_at: 2026-10-16T22:58:20.479Z
decision: null
decision_answer: null
---

Ground tiles built in Node: tools/prebuild_layers.mjs --layer ground runs terrain.js's own loadGlbMesh, conformGroundToField, tileGround and the spatial-batch partition for 1835 and writes each tile's pieces with an input hash, byte-equal to the page's ground batches (read from the live page), its determinism and stale-input refusal gated in check.sh.

Piece 1 of 3 of **T-2678 — The spatial-batch chunks prebuilt the same way: the partitioned pieces of the spatialBatch callers written at publish and uploaded by the page, byte parity with the page's own partition and boot phases quoted before and after**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2678 was split (2026-10-16T22:58:09.524Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 4m ago, run 10/16/2026, 5:54:26 PM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/38977949584) — held by the run that split it

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/38977949584) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)
