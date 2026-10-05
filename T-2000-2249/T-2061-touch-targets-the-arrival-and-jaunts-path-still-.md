---
id: T-2061
title: Touch targets the arrival-and-jaunts path still reaches under 44px: HUD chips 38px, the drawer's Back and Close 30px and its tabs 37px wide at 320, the place card's 'why' toggles 19x17
state: review
epic: RENDERING
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-10-03
closed: null
pr: 437
claimed_by: run 10/4/2026, 5:27:55 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37239878195
claimed_at: 2026-10-04T22:27:55.031Z
decision: null
decision_answer: null
---

Touch targets the arrival-and-jaunts path still reaches under 44px: HUD chips 38px, the drawer's Back and Close 30px and its tabs 37px wide at 320, the place card's 'why' toggles 19x17.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 204 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> T-2046's layout reading measures these on the path but they belong to the HUD, drawer and card contracts; T-2047, the report that names this section's successors, merged while T-2046 was in flight, so no live ticket owns the finding

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## The reading (T-2046, 2026-10-04)

`node tools/measure_arrival_layouts.mjs --layout <name>` lists these per layout under
`elsewhere` in `docs/measurements/arrival-layouts.json`. It reports them and does not gate them:

- HUD chips 38px tall at every touch layout (Start / Jaunts, Confidence, ▾ 26px wide, Walk,
  Fly, theme, Menu). Raising them to 44 moves the wrapped HUD's foot from ~92px to ~104px,
  so the jaunt panel's and the overlays' `100px` top at ≤900px must move with it.
- The drawer's Back and Close 30x30; its eight tabs 37px wide at 320px.
- The place card's inline `why` toggles 19x17 (its firm buttons went to 44 on touch in T-2046).

**Acceptance:** move each surface into the tool's owned set (`owned` in
`readLayout`) and all four layouts still PASS.
