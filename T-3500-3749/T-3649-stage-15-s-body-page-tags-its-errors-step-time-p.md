---
id: T-3649
title: Stage 15's body page tags its errors (step, time, page) and a smoke-side probe makes every loader's refused picture say why (createImageBitmap, blob read, KTX2 transcode), with zero page errors unchanged
state: done
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: T-3648
opened: 2026-11-18
closed: 2026-11-18
pr: 2182
claimed_by: run 11/18/2026, 3:16:06 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-11-18T11:34:13Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/44265113509
claimed_at: 2026-11-18T09:16:08.035Z
decision: null
decision_answer: null
---

Stage 15's body page tags its errors (step, time, page) and a smoke-side probe makes every loader's refused picture say why (createImageBitmap, blob read, KTX2 transcode), with zero page errors unchanged.

Piece 1 of 2 of **T-3648 — Fix the cause the T-3637 record names for the mobile stage-15 texture failures after the Jump checks, and bring dev's smoke (mobile, 15) to green without weakening zero page errors**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-3648 was split (2026-11-18T09:15:51.208Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 39m ago, run 11/18/2026, 2:36:51 AM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/44265113509) — held by the run that split it
- branch `steward/t3648-stage15-refusal-reasons` — the splitter's own

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/44265113509) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)
