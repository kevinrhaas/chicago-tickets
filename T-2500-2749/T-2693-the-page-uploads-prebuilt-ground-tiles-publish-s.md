---
id: T-2693
title: The page uploads prebuilt ground tiles: publish.sh writes them into site/4d/data/prebuilt/1835/, terrain.js batches them when their input hash is current and builds in the browser when missing or stale, check_published.mjs refuses a stale one, and measure_boot_phases --published quotes terrain's phase and longest task at the phone profile before and after, cold and warm, with SITE-BUDGET re-measured
state: open
epic: RENDERING
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: T-2678
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

The page uploads prebuilt ground tiles: publish.sh writes them into site/4d/data/prebuilt/1835/, terrain.js batches them when their input hash is current and builds in the browser when missing or stale, check_published.mjs refuses a stale one, and measure_boot_phases --published quotes terrain's phase and longest task at the phone profile before and after, cold and warm, with SITE-BUDGET re-measured.

Piece 2 of 3 of **T-2678 — The spatial-batch chunks prebuilt the same way: the partitioned pieces of the spatialBatch callers written at publish and uploaded by the page, byte parity with the page's own partition and boot phases quoted before and after**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2678 was split (2026-10-16T22:58:09.524Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 4m ago, run 10/16/2026, 5:54:26 PM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/38977949584) — held by the run that split it

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/38977949584) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)
