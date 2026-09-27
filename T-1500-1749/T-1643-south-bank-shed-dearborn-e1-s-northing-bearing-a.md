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

## It fails at DESKTOP too, at the same measurements (2026-09-27, while re-gating PR #95)

The reproduction above was taken at mobile only. Re-gating the T-1637 branch on dev after
the Hathaway recut (PR #97) ran the assertion at both widths on the published mirror, and it
fails identically at each:

    mobile  390x780   2976 plank vertice(s), walked west to E 811.5, 0 blocked stride(s), worst step 0.04 m
    desktop 1280x800  2976 plank vertice(s), walked west to E 811.5, 0 blocked stride(s), worst step 0.04 m

Same vertex count, same stopping easting, same worst step. So the obstruction is in the
compiled collision footprint and not in anything viewport-dependent, and the acceptance
should be read at both widths rather than at mobile alone. Everything else in those legs is
green: mobile 1-3 241/1, desktop 2-3 171/1, mobile 11-12 105/0, `check.sh` 651 steps none
red. The recut of the south bank did not move these figures either, which is a second
reading that the cause is the shed and not the bank.
