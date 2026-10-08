---
id: T-2100
title: Re-pose town_backyard and town_south_water_store: both stand a metre from a wall, so their captures cannot show the yard or shop front T-2085..T-2087 are judged by
state: review
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-04
closed: null
pr: 527
claimed_by: run 10/8/2026, 8:06:51 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37781198980
claimed_at: 2026-10-08T13:06:51.460Z
decision: null
decision_answer: null
---

Re-pose town_backyard and town_south_water_store: both stand a metre from a wall, so their captures cannot show the yard or shop front T-2085..T-2087 are judged by.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 192 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> T-2085, T-2086 and T-2087 all take their visual acceptance from captures at these poses, and two of the three show only a wall (T-2092's reading)

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## What T-2092 found (2026-10-04)

`tools/measure_detail_ceilings.mjs` TOWN poses, captured at 1280x800 and 390x780 on production (main @ 2761a5ae) and dev (c602f498), welcome entered:

- `town_backyard` (local 385, -450, yaw 0, pitch -6) stands about a metre south of the back wall of a Washington Street house and looks into it. The capture is a wall; the yard behind the observer is not in frame.
- `town_south_water_store` (501, -2, yaw 180, pitch -6) stands about a metre from the front of the narrow store it was placed before (c3_12 / c3_13) and looks into its door and window.
- `town_lake_shoulder` is fine: it shows the shoulder, the plank walk and the store fronts, and it is the only one of the three that shows T-2091's change.

The captures are in `docs/measurements/settled-town-ground-2026-10/` (T-2092's PR).

## The work

Move or turn the two poses so the frame takes in the yard (house, outbuildings, fence line) and the store frontage (walk, door, ground before it) — e.g. turn the back-yard pose to face south down the lot toward the alley, and step the store pose back into South Water Street. Read the new poses' triangles/flora/calls at all tiers on dev beside the old ones, because T-2091 and T-2092's numbers were taken at the old coordinates and a re-posed stand is a new baseline, not a change. Keep the old ids or rename them, and say which in the tool's comment.
