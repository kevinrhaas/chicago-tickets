---
id: T-2737
title: dev's still-frame (desktop) ceiling broken on 1835 town_backyard since 529f58a61: full 15664 ms vs 13750, balanced 10659 vs 10500, light 7015 vs 7000 (frame-time run 39057019019); find the landing that slowed every frame and either win it back or argue the ceiling in still_frame_ceilings.json with the reading
state: open
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-17
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

dev's still-frame (desktop) ceiling broken on 1835 town_backyard since 529f58a61: full 15664 ms vs 13750, balanced 10659 vs 10500, light 7015 vs 7000 (frame-time run 39057019019); find the landing that slowed every frame and either win it back or argue the ceiling in still_frame_ceilings.json with the reading.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 147 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> dev's own frame-time gate is red, so every PR whose push runs chicago-4d-frame-time.yml is refused on a check its diff cannot move (PR #978 twice on 2026-10-17)

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
