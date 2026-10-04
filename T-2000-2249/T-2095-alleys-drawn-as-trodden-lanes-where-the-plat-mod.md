---
id: T-2095
title: Alleys drawn as trodden lanes where the plat model places an alley strip, and the lot paths meeting the road shoulder with no seam
state: review
epic: TOWN
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-2087
opened: 2026-10-04
closed: null
pr: 420
claimed_by: run 10/4/2026, 12:19:56 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37219896047
claimed_at: 2026-10-04T17:19:56.406Z
decision: null
decision_answer: null
---

Alleys drawn as trodden lanes where the plat model places an alley strip, and the lot paths meeting the road shoulder with no seam.

Piece 2 of 2 of **T-2087 — Road shoulders, alleys, store frontages and paths go to trodden earth grading into turf, replacing the prairie left in the 80-foot corridor beside the wagon track**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2087 was split (2026-10-04T17:18:19.326Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 2m ago, run 10/4/2026, 12:16:26 PM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/37219697905) — held by the run that split it

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/37219697905) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

## Found while building (2026-10-04, PR #420)

Ten reconstructed houses on the Lake Street blocks from Franklin to State (`recon_1835_south_d5_023`, `d4_026`, `h1_029`, `d5_028`, `d1_032`, `d6_031`, `d4_030`, `d7_035`, `d5_034`, `d1_033`) stand with their backs inside the plat model's alley strip, so the lanes on `blk_lake_franklin` … `blk_lake_dearborn` stop at each one. The full list, with spans, is `cut_by_structures` in `data/enclosures/town_alley_lanes.json`. Five other cuts are at alley mouths or on the West Division (`bates_auction_room`, `chappel_infant_school`, `recon_1835_west_018`, `_023`, `_034`). Not filed as its own ticket: the queue is over its ceiling. L377's "How to resolve" names it: a re-seating that moves those houses out of the strip lets the lanes run through, and `generate_alley_lanes.py` will draw them without a change.
