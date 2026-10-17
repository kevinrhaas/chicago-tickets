---
id: T-2694
title: The town's other spatial-batch callers prebuilt (yards' five surfaces, streets' three, the railway and the distant ground base): written at publish and uploaded by the page, byte parity with the page's own partition and boot phases quoted before and after
state: split
epic: RENDERING
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: T-2678
opened: 2026-10-16
closed: 2026-10-16
pr: null
claimed_by: run 10/16/2026, 9:16:31 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-17T02:23:01.084Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38993985220
claimed_at: 2026-10-17T02:16:31.711Z
decision: null
decision_answer: null
---

The town's other spatial-batch callers prebuilt (yards' five surfaces, streets' three, the railway and the distant ground base): written at publish and uploaded by the page, byte parity with the page's own partition and boot phases quoted before and after.

Piece 3 of 3 of **T-2678 — The spatial-batch chunks prebuilt the same way: the partitioned pieces of the spatialBatch callers written at publish and uploaded by the page, byte parity with the page's own partition and boot phases quoted before and after**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2678 was split (2026-10-16T22:58:09.524Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 4m ago, run 10/16/2026, 5:54:26 PM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/38977949584) — held by the run that split it

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/38977949584) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

## Finding from T-2693 (2026-10-17): the ground's bytes, and the budget this piece inherits

T-2693 made the page upload the prebuilt ground in place of the ground GLB. Measured on one
published tree with `tools/measure_boot_payload.mjs` with and without `--no-prebuilt-ground`,
the boot payload went **19.109 → 28.195 MB**. The published ground GLB is meshopt-packed and
costs only 1.26 MB on the wire; the prebuild is 10.63 MB gzipped plus a 0.21 MB index on the
wire. T-2692's note that it might replace a 30.5 MB GLB read the source GLB in `assets/`,
which the page never fetches. The boot payload budget was re-set to 29 MB in
docs/SITE-BUDGET.md § 4g, on the owner's T-2560 ruling, so **this piece starts with under
1 MB of room** and has to measure its own bytes against that number.

The lever that would give most of the ground's 9.1 MB back: ship the PARTITION, not the
float32 vertices. Each piece's source-vertex ids and local index compress to far less than
the vertices do, and the page would gather from the 1.26 MB GLB it already loads and
conforms (the conform is 135 ms of the 3.0 s at the phone profile). The batches would still
have to be byte-equal to the page's own cut. A data-saving or 3G connection already skips
the prebuild (terrain.js `fetchPrebuiltGround`).
