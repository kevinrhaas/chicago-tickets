---
id: T-3648
title: Fix the cause the T-3637 record names for the mobile stage-15 texture failures after the Jump checks, and bring dev's smoke (mobile, 15) to green without weakening zero page errors
state: open
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: T-3637
opened: 2026-11-17
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

Fix the cause the T-3637 record names for the mobile stage-15 texture failures after the Jump checks, and bring dev's smoke (mobile, 15) to green without weakening zero page errors.

Piece 2 of 2 of **T-3637 — Dev's mobile smoke stage 15 is intermittently red on zero page errors: THREE.GLTFLoader couldn't load texture blob:… URLs after the Jump checks**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-3637 was split (2026-11-18T00:56:35.485Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 29m ago, run 11/17/2026, 6:27:38 PM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/44202593731) — held by the run that split it

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/44202593731) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)
