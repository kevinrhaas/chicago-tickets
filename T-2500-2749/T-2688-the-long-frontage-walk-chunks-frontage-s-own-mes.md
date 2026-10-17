---
id: T-2688
title: The long frontage walk chunks, frontage's own mesh, the far walk tops and the yard's woodpile chunk cut into pieces whose 16-bit grid keeps the millimetre, so every position in the three layers is 8 B
state: split
epic: RENDERING
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: T-2576
opened: 2026-10-16
closed: 2026-10-16
pr: null
claimed_by: run 10/16/2026, 6:58:46 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-17T00:28:50.299Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38983841004
claimed_at: 2026-10-16T23:58:46.972Z
decision: null
decision_answer: null
---

The long frontage walk chunks, frontage's own mesh, the far walk tops and the yard's woodpile chunk cut into pieces whose 16-bit grid keeps the millimetre, so every position in the three layers is 8 B.

Piece 2 of 3 of **T-2576 — Quantized positions in frontage, enclosures and yard: Int16x4 relative to each chunk with the offset and scale in its matrix, every probe and spatialBatch reader made to apply it, so the four layers reach T-2549's 40 %**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2576 was split (2026-10-16T21:15:16.902Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 5m ago, run 10/16/2026, 4:10:06 PM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/38966866392) — held by the run that split it

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/38966866392) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

## Finding (2026-10-17, slice 3/5) — the cut works and the draw-call budgets refuse it

Built and measured on branch `steward/t2688-cut-long-meshes` (pushed for reference, **no PR — do not salvage it as-is**). `compact-streams.js` gained `cutForQuantization` (bins a non-indexed mesh's triangles by centre into cells whose box the 16-bit grid keeps to the millimetre; each piece lists its source faces) and `rangesInPiece` (carries pick spans, lot-item spans and walk-top ranges onto a piece). Frontage's shared mesh went to 5 pieces, 21 street-edge chunks (half-extents 67.7 to 342.5 m — not three, as T-2687's PR said: sixteen sat at 67.7 to 71.4 m) to 61, the far walk tops to 40, the woodpile chunk to its cells; the reach banked each piece on its whole mesh's sphere so it held back exactly what it held back. Every frontage position read Int16 x 4 (`check_far_plank_tops` 11/11, `prebuild_layers --self-test` green, 172 meshes replayed equal), attributes 86.3 -> 82.3 MB in the Node build.

**Stage 5, mobile 390x780, published, same runner, same hour:**

| worst stand | dev 2d2353c07 | the cut | budget |
|---|---|---|---|
| full | 294 calls | **428** | 330 |
| balanced | 263 calls | **381** | 330 |
| light | 78 calls | **96** | 90 (owner's floor, 2026-08-28) |

One model matrix per draw is one box per draw, so millimetre positions across a 684 m mesh cost either more draws (this) or a decode in the vertex stage. Mobile 1-2 also read the highest flat-ground deck vertex at 0.180 m against the 0.18 m band once the long chunks were on the grid (a tolerance of the grid's own millimetre was added on the branch).

**What would ship it:** each mesh keeps ONE draw and its pieces' boxes are decoded in the vertex stage — a small box table (offset + uniform scale per piece) indexed from the position's padding lane (`w`, Int16 normalized: piece = round(w * 32767)), or a multi-draw batch with per-piece matrices. Every reader of a position has to apply it: the frontage-timber and yard materials, their shadow depth materials (standing chunks and woodpiles cast), `gpu-pick.js`, the CPU raycast fallback, `far-merge.js`, `createFarWalkTops`, `positionsInMetres`, and each mesh's bounding sphere set in metres. Acceptance for that route: positions at 8 B in all three layers, stage 5's call counts equal to dev's, pixel parity at T-2569's anchors, picks and probes unchanged.

Also read on dev 2d2353c07, stage 5 mobile, NOT this ticket's: `the far merge gives back draw calls down the axial street and moves no triangle doing it` is red on dev (90 calls saved over 11 of 41 clusters, -7380 triangles moved); `dev-smoke-state` still records part 5 as PASS from 2026-10-04.
