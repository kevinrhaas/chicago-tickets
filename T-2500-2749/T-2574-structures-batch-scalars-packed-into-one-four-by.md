---
id: T-2574
title: Structures batch scalars packed into one four-byte attribute: roughness, confidence, grain and the piece tone as Uint8x4, read by the roughness, wall-relief and confidence patches and the shared depth material, at most 24 bytes a vertex with pixel parity
state: open
epic: RENDERING
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: T-2571
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

Structures batch scalars packed into one four-byte attribute: roughness, confidence, grain and the piece tone as Uint8x4, read by the roughness, wall-relief and confidence patches and the shared depth material, at most 24 bytes a vertex with pixel parity.

Piece 1 of 2 of **T-2571 — Structures batch to at most 24 bytes a vertex: pack roughness, confidence, grain and the piece tone into one four-byte attribute and quantize positions to Int16x4 with the offset in the instance matrix, every stride a multiple of four for Metal, with pixel parity**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2571 was split (2026-10-16T08:20:59.025Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 2m ago, run 10/16/2026, 3:18:38 AM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/38871344208) — held by the run that split it

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/38871344208) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)
