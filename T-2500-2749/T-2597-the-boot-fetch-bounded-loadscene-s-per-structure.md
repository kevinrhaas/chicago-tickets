---
id: T-2597
title: The boot fetch bounded: loadScene's per-structure loads run through a concurrency pool instead of an unbounded Promise.all, and the boot-time peak of GLB bytes held at once measured before and after and quoted
state: open
epic: RENDERING
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: T-2554
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

The boot fetch bounded: loadScene's per-structure loads run through a concurrency pool instead of an unbounded Promise.all, and the boot-time peak of GLB bytes held at once measured before and after and quoted.

Piece 1 of 2 of **T-2554 — 1904 texture residency: textured houses resident by distance under a per-tier texture budget, uploads paced per frame, and the boot fetch bounded**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2554 was split (2026-10-16T14:03:56.849Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 1m ago, run 10/16/2026, 9:03:51 AM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/38910758330) — held by the run that split it

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/38910758330) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)
