---
id: T-1987
title: No ground rises through any road at any distance: base ground holed under the detail tiles, panels laid on the cell ridge at full and balanced, the road texture continuous across panels
state: done
epic: TOWN
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-10-02
closed: 2026-10-02
pr: 289
claimed_by: run 10/2/2026, 11:29:20 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-02T21:15:10Z
claimed_run: null
claimed_at: 2026-10-02T16:29:20.961Z
decision: null
decision_answer: null
---

No ground rises through any road at any distance: base ground holed under the detail tiles, panels laid on the cell ridge at full and balanced, the road texture continuous across panels.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 252 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> The owner's own report of 2026-10-02 (grass growing over the dirt as he walks up to it, Lake and Market, South Water and Lake), worked in its own project thread and PR; no open ticket owns the road drape

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

The owner, 2026-10-02, verbatim: "as you walk on dev, the grass area seems to grow and show up over the dirt road as you approach it, please review and walk and fly and cover all the roads and make sure there are no visual artifacts, mistakes like this or misjoined roads".

1. The coarse base ground draws nothing within the detail tiles' reach (less a 10 m overlap), so it can never stand above a road the detail tiles carry. Measured before: up to 239 mm above the road at 20 % of road points.
2. At full and balanced, no street triangle sags under the drawn ground: probed town-wide against each cell's ridge (the upper triangulation, which bounds the baked ground), the worst sink stays under 18 mm, the 22 mm lift less the bake's 4 mm. The smoke reads it at the boot tier and asserts the road follows the detail level.
3. `light` keeps the refined grids and stays at dev's street triangle count; full and balanced carry the cost at a ceiling moved at its definition with the measurement written there.
4. The road texture's across-coordinate is each column's own fraction, so the shoulders, lanes and sod islands no longer jump at every panel edge.
5. Every junction and street end walked and flown, with before/after shots, and whatever misjoin it finds fixed or recorded here.
6. check.sh and the smoke by parts green at 1280x800 and 390x780.

## Checked for an existing ticket (owner's question, 2026-10-02)

No open ticket owns this. The street work it follows is T-1770 (split), whose children T-1811 (the worked roadway surface) and T-1812 (the graded street section) are both done; T-1812's lattice-column grids and graded bed are what this ticket re-lays. T-1771 (the working bank, done) is the layer that drew grass over South Water's river edge. T-1856 is a 1904 Prairie Avenue materials package and does not reach the 1835 streets.
