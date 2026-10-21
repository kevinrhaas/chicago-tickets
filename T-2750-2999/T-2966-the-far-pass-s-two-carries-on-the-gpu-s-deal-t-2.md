---
id: T-2966
title: The far pass's two carries on the GPU's deal (T-2896's first slice): flora-near-carry and flora-mid-carry dealt in GLSL against a kept carry tile, 137,562 instances bit-identical at 72 phone poses, far pass median 28-40 to 13-18 ms walking; the streets' growth test asked per 16 m bin
state: claimed
epic: RENDERING
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: T-2896
opened: 2026-10-20
closed: null
pr: 1162
claimed_by: run 10/20/2026, 9:57:55 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-21T02:57:56.205Z
decision: null
decision_answer: null
---

The far pass's two carries on the GPU's deal (T-2896's first slice): flora-near-carry and flora-mid-carry dealt in GLSL against a kept carry tile, 137,562 instances bit-identical at 72 phone poses, far pass median 28-40 to 13-18 ms walking; the streets' growth test asked per 16 m bin.

Piece 1 of 4 of **T-2896 — The far shrubs, the carry sets and the far band on the GPU's deal, so the near re-deal reaches the GPU pass's own cost alone; read with the CPU profile and the near re-deal line at the throttled phone profile**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2896 was split (2026-10-20T19:52:04.443Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 28m ago, run 10/20/2026, 2:23:49 PM CT — held by the run that split it

The run that split it (by hand) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

## 2026-10-20 — taken back out of PR #1161: worst moving frames over the ceilings

CI's moving-frames gate on #1161 read flora's worst moving frame over the ceiling at every tier with this slice in: full turn 73.3 ms (ceiling 60), balanced turn 48.1 (32), light travel 43.6 (21). Each spike is a far pass DRAINED in one frame with every carry read-back reaped inside it (`36 reaped 227 ms` over the full turn; far pass max 79.6 ms). The median far pass fell (as measured) but the worst frame rose, and the slice's readings only measured medians. Reverted from #1161 (65860fc4d); the work is commit 20e8175d4 (wt/near, also d8843ce38 on the integration branch).

**Added acceptance:** `node tools/measure_walk_frames.mjs --gate` (the CI moving-frames reading, every tier and move) holds flora's worst moving frame under each tier's ceiling — never reap the carries all at once in a drained pass; amortize the reap (and the keeper's landing, T-2969) across frames.
