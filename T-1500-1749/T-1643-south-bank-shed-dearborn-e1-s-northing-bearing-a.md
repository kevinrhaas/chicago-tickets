---
id: T-1643
title: south_bank_shed_dearborn_e1's northing, bearing and wagon door were read off a road that has since moved off the reach: re-seat it, re-face it, or say in the record why it stands as it is
state: claimed
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-26
closed: null
pr: null
claimed_by: run 9/26/2026, 7:26:19 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/36282376499
claimed_at: 2026-09-27T00:26:19.648Z
decision: null
decision_answer: null
---

south_bank_shed_dearborn_e1's northing, bearing and wagon door were read off a road that has since moved off the reach: re-seat it, re-face it, or say in the record why it stands as it is.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## Reproduction found while validating T-1275 (2026-09-26)

The published mobile stage-2 smoke fails on **unmodified dev `b6c56c83f3b87b7a2f125eb5f396e067872b9541`**: `87 passed, 1 failed` (1 m 31 s). The same assertion and measurements fail with T-1275 applied. This is not a loading-card regression.

Command: `SMOKE_VIEWPORT=mobile SMOKE_STAGE=2 node tools/smoke_renderer.mjs --published` (Chromium 153 / software WebGL).

`the east end reads as planks underfoot, and walks on along the bank`: 2,976 plank vertices; walking from local E 809.4, N 14.2 at bearing 270 stops at **E 811.5**, instead of reaching E < 802; zero terrain-blocked strides; worst step 0.04 m. The shed's compiled collision footprint spans the test route: corners `(810.896,18.455)`, `(805.442,17.860)`, `(806.500,8.164)`, `(811.954,8.759)`. Its footprint covers the starting point and pushes the walker out east, preventing the westward river walk.

Include this route in the repositioning acceptance: preserve a traversable river plank walk, and pass the existing published stage-2 assertion without weakening its reach, step or obstruction checks. Keep the shed's placement evidence and declared reconstruction bounds.
