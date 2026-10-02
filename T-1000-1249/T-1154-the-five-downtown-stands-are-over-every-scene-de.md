---
id: T-1154
title: The five downtown stands are over every scene-detail ceiling at both viewports, and the town has been over since some point after 6 September
state: split
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-15
closed: 2026-09-17
pr: null
claimed_by: run 9/17/2026, 8:03:58 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-09-17T13:35:31.026Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/35224144036
---

The five downtown stands are over every scene-detail ceiling at both viewports, and the
town has been over since some point after 6 September.

**Acceptance:** (state it before working -- the definition of done, never weakened to pass)

Found by T-1148, which went looking for a SOUTHERN ceiling problem and found a town-wide
one underneath it. Read on `tools/measure_detail_ceilings.mjs` against the published
mirror of dev on 2026-09-15, committed in `data/render/southern_stand_ceilings.json`:

| tier | ceiling | worst downtown, desktop | worst downtown, mobile |
| --- | --- | --- | --- |
| `full` | 1,460,000 | 1,883,619 (Lake at Canal) | 1,674,254 (Lake at Canal) |
| `balanced` | 1,280,000 | 1,738,020 (Lake at Canal) | 1,522,359 (Lake at Canal) |
| `light` | 825,000 | 1,287,059 (Lake at Canal) | 1,136,437 (Lake and Market) |

This is not one instrument's opinion. `tools/measure_ground_tiling.mjs` read four of the
same stands on the same day and agrees to within 0.7 per cent -- 1,880,503 against
1,883,619 at Lake at Canal, desktop `full`. Its own `what_this_is_not` doubted its
calibration against the gate; the doubt was unnecessary, and the two instruments
disagreeing with the CEILING rather than with each other is the whole finding.

`tools/dev-smoke-state.json`'s newest desktop part-4 reading is a PASS of
2026-09-06T00:44:54Z. So the breach arrived in the nine days after it, and the first
place to look -- not yet the answer -- is the southern field (T-0464) landing inside
every downtown frustum, which is the change of that period that adds geometry nothing
culls from Lake Street.

**What this ticket is not:** a re-budget. The ceilings were argued once, on a town that
fitted inside them, and a ceiling raised to meet a regression is the ceiling being moved
to fit -- which T-1148's acceptance forbids and this one inherits. The answer is a trim,
and it is owed where the triangles were added.

**Acceptance:** the nine days are bisected and the change that put the town over is
named with a measured before and after; the trim is made where that change is, not at
the ceiling; and the downtown five read inside all three ceilings at both viewports on
`tools/measure_detail_ceilings.mjs`, with the reading committed beside this one.
Whatever the southern four do afterwards is T-1148's successor question and belongs with
T-0467, not here.

## Reconciled, 2026-10-02 (T-1975)

Re-read on `tools/measure_detail_ceilings.mjs`, published mirror of dev @ 652ca8ea, both viewports
(committed in the code repo as `docs/measurements/t-1975-detail-ceilings-{desktop,mobile}.json`):

| tier | 2026-09-15 worst, desktop | 2026-10-02 worst, desktop | 2026-10-02 worst, mobile |
| --- | --- | --- | --- |
| `full` | 1,883,619 (Lake at Canal) | 1,705,768 (Lake at Canal) | 1,556,676 (Lake at Canal) |
| `balanced` | 1,738,020 (Lake at Canal) | 1,472,889 (Lake at Canal) | 1,332,135 (Lake at Canal) |
| `light` | 1,287,059 (Lake at Canal) | 944,550 (the forks) | 845,385 (Lake at Canal) |

What this ticket asked for was done by its children: the town came back inside all three ceilings by
trims (the 2026-09-26 reading in `main.js` had `full` at 1,383,428 worst, 76,572 clear). The breach
that stands today is NEW and is not this ticket's nine days: `full` grew 322,340 over about sixty
owner-requested parcels of 2026-09-26..10-02 (T-1215's convergence), none of them a regression.

So this ticket's "a re-budget is forbidden" no longer governs `full` and `balanced`: the owner asked
in T-1215 for "the budgets re-measured and set", and AGENTS.md's 2026-08-21 ruling makes the scene he
asked for the justification. T-1975 sets them to the measured worst plus T-0672's recorded headroom
(1,725,000 / 1,490,000; calls 215 -> 240). It still governs `light`, which AGENTS.md keeps as the
floor: `light` is not raised, and T-1976 owns the trim that brings it back under 825,000.
