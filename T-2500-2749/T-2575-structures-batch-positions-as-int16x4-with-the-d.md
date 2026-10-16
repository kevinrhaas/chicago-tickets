---
id: T-2575
title: Structures batch positions as Int16x4 with the dequantize offset and scale in each instance matrix, and every reader of batch positions (backingTriangles, localBoxes, the occludesView matrix check, picking) on the composed matrix, with pixel parity
state: done
epic: RENDERING
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: T-2571
opened: 2026-10-16
closed: 2026-10-16
pr: 871
claimed_by: run 10/16/2026, 3:27:01 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-16T11:03:53Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38872274829
claimed_at: 2026-10-16T08:27:01.883Z
decision: null
decision_answer: null
---

Structures batch positions as Int16x4 with the dequantize offset and scale in each instance matrix, and every reader of batch positions (backingTriangles, localBoxes, the occludesView matrix check, picking) on the composed matrix, with pixel parity.

Piece 2 of 2 of **T-2571 — Structures batch to at most 24 bytes a vertex: pack roughness, confidence, grain and the piece tone into one four-byte attribute and quantize positions to Int16x4 with the offset in the instance matrix, every stride a multiple of four for Metal, with pixel parity**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2571 was split (2026-10-16T08:20:59.025Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 2m ago, run 10/16/2026, 3:18:38 AM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/38871344208) — held by the run that split it

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/38871344208) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)
