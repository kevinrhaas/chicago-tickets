---
id: T-2118
title: north_bank_shed_dearborn_e1, an invented freight shed, laps Dearborn North's platted corridor by 6.63 m with its centroid inside it, banked in the corridor baseline and refused in writing nowhere — the act T-0253 refuses on the south bank
state: open
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-10-04
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

north_bank_shed_dearborn_e1, an invented freight shed, laps Dearborn North's platted corridor by 6.63 m with its centroid inside it, banked in the corridor baseline and refused in writing nowhere — the act T-0253 refuses on the south bank.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 184 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> T-0253 closes when its PR merges and this is a provenance defect in a committed record it measured but may not move; folded into T-0253 it would vanish with it

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## What was measured (T-0253, 2026-10-05)

`python3 tools/measure_corridor_intrusion.py` lists 23 placed phases lapping a platted corridor.
One of them is `north_bank_shed_dearborn_e1` (T-0133, `docs/LIBERTIES.md` L164): position graded
`reconstructed`, lap 6.63 m into `dearborn_north`, centroid IN. Its `position.note` argues the
SOUTH bank's absence from corridor ground and says nothing of its own lap; no written refusal
(T-0195) covers it. T-0253 settled that an invented building may not stand in a platted
corridor, and T-2012 withdrew `south_bank_shed_dearborn_e1` for exactly that.

**Acceptance:** the shed is re-seated clear of `dearborn_north`'s corridor (re-baked, the
corridor baseline re-banked with `--write-baseline` as a repair), or withdrawn with its L164
`Covers:` tokens struck — or, if the corridor itself is wrong there, that is shown against the
plat and the corridor moves instead. `measure_corridor_intrusion.py --gate` green either way.
