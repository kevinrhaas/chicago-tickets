---
id: T-2571
title: Structures batch to at most 24 bytes a vertex: pack roughness, confidence, grain and the piece tone into one four-byte attribute and quantize positions to Int16x4 with the offset in the instance matrix, every stride a multiple of four for Metal, with pixel parity
state: split
epic: RENDERING
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: T-2568
opened: 2026-10-16
closed: 2026-10-16
pr: null
claimed_by: run 10/16/2026, 3:18:38 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-16T08:21:03.026Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38871344208
claimed_at: 2026-10-16T08:18:38.533Z
decision: null
decision_answer: null
---

Structures batch to at most 24 bytes a vertex: pack roughness, confidence, grain and the piece tone into one four-byte attribute and quantize positions to Int16x4 with the offset in the instance matrix, every stride a multiple of four for Metal, with pixel parity.

Piece 2 of 2 of **T-2568 — Compact vertex formats in the structures batch: the colour per instance, normals, uv, roughness and confidence in compact normalized formats, at most 24 bytes a vertex with pixel parity**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2568 was split (2026-10-16T06:55:32.182Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 32m ago, run 10/16/2026, 1:23:23 AM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/38859370867) — held by the run that split it

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/38859370867) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

## What T-2570 found (2026-10-16)

- Measured on `/1835/` at 390x780: the structures batches hold 1,265,459 vertices at 52.8 B (74.4 MB with the index). T-2570 takes them to 32.4 B (48.6 MB) with no shader change. The other three layers of T-2549 are T-2569.
- **Every stride must be a multiple of four bytes.** Safari's WebGL runs on Metal, and ANGLE meets a 1-, 2- or 3-byte vertex stride by converting the attribute into a second, aligned buffer at upload. A lone `Uint8` `_roughness` would cost an iPhone more than the float32 it replaced. So the scalars (`_roughness`, `_confidence`, `_grain`, the piece tone) have to be PACKED into one four-byte attribute, which means the shaders that read them change: `confidence.js` (shared by every layer), `wall-relief.js`, `perVertexRoughness` in buildings.js, and the shared depth material. `compact-attributes.js` refuses a misaligned rule.
- **The piece tone exceeds 1 on 1835** (three of five batches carry it; 948,627 vertices), so it stays float32 x3 there today (12 B on 75 % of the vertices). Packed as one byte it needs a scale (e.g. `k / K` with the instance colour times `K`).
- `_confidence` at 0.5 is not exact as a normalized byte (0.50196): `chicago_wInferred` reads 0.992. Decide whether that is inside the tolerance, or carry the three levels another way.
- Positions as Int16x4 (8 B, padded) need the dequantize offset and scale in each instance matrix; `backingTriangles`, `localBoxes`, the `occludesView` matrix comparison and anything reading batch positions against `placements` must then use the composed matrix.
