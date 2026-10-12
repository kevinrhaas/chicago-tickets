---
id: T-2398
title: 1601 Prairie as a whole K16 clapboard frame house: the traced two-storey main block and its south-side wing closed in timber, gable roof, sash, door, porch and stack
state: review
epic: SOUTH_TIME
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-1866
opened: 2026-10-11
closed: null
pr: 722
claimed_by: run 10/11/2026, 10:58:55 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38201670760
claimed_at: 2026-10-12T03:58:55.299Z
decision: null
decision_answer: null
---

1601 Prairie as a whole K16 clapboard frame house: the traced two-storey main block and its south-side wing closed in timber, gable roof, sash, door, porch and stack.

Piece 1 of 2 of **T-1866 — Refine 1601 house and 1603 station-side envelope**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-1866 was split (2026-10-12T03:58:43.969Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 1m ago, run 10/11/2026, 10:58:12 PM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/38201670760) — held by the run that split it

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/38201670760) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)
1. `house_1601_prairie` keeps its id, placement and traced main-body rectangle and changes from the draft (`prairie_draft`) to a `k16_timber` `frame_house`, as 1630 did in T-2357: every wall of the main block and the traced south-side wing (`r2`) closed in clapboard with corner boards, sash on every face, a door, a porch, a stack and declared roofs, so the draft's grey stand-in is gone from the 16th Street corner.
2. Each attribute carries its tier: the plan, storeys and frame are the sheet's; roof, openings, porch and colours are reconstructed in a liberty (`L-k16-1601-frame-house-2398`), and 1601 is retired from the draft's block liberty.
3. `check.sh` green, the K16 GLB baked by command, and the published `/1904/` app read before and after from front, both obliques, rear and roof at 1280×800 and 390×780 with 0 page errors, costs recorded in `docs/RESEARCH/`.
