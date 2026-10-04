---
id: T-2096
title: Walking lag: measure a scripted walk through the town at both viewports and every tier on a throttled phone profile, fix the largest per-frame cost it names (the flora lattice rebuilt synchronously every 0.6 m and every small turn is the suspect), and hold the walk's p95 frame time
state: open
epic: RENDERING
requested_by: owner
seen: true
effort: M
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

Walking lag: measure a scripted walk through the town at both viewports and every tier on a throttled phone profile, fix the largest per-frame cost it names (the flora lattice rebuilt synchronously every 0.6 m and every small turn is the suspect), and hold the walk's p95 frame time.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 188 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> Owner, 2026-10-04: walking is laggy now; asked for focused effort on lag at the top. No open ticket measures walking frame time; T-1969/T-1975/T-1976 set still-frame triangle ceilings only

## Why this ticket exists (owner, 2026-10-04)

Kevin, 17:18 UTC: "when you walk it is laggy now. i think some of the flora tickets will help but maybe some focused effort on that will help as well." The town-ground tickets (T-2092, T-2086, T-2094, T-2095) cut what the town DRAWS. This ticket is about what WALKING costs, frame by frame, on desktop and on his iPhone (Chrome on iOS). Nothing open in the queue measures or owns it: T-1969 / T-1975 / T-1976 set triangle and draw-call ceilings at fixed stands, which is a still frame, not a walk.

## What the code does on every step (read 2026-10-04 on dev @ 55a68416; inferred, not yet measured)

- `flora.js` `update()` (~2160–2205), called every frame from `main.js` ~3226: when the walker has moved more than the near ring's `step` (0.6 m, `TUNE.step` ~347), turned more than `CONE_YAW_STEP` (0.20 rad), or changed pitch or eye height, it runs `rebuildAll()` to completion **synchronously, inside that frame** ("runtime synchronous path"). `rebuildAll` re-deals every near, mid, forb and head slot in the placement cone, calls `station()` (terrain height, water, footprints, `growthBlocked`) for each, and rewrites the instance buffers. The far-shrub band does the same on its own step. At walking pace (~1.4 m/s), that is a full rebuild about every 0.4 s, plus one on every small turn. That pattern matches "laggy when you walk, fine when you stand".
- `growthBlocked` (`main.js` ~1982) asks streets, yards, the ground strip and the working bank for every station, and T-2091 added the derived town extent to the zone lookup. Both are per-slot costs inside that rebuild.
- `trees.update()` runs next (`main.js` ~3227). Furniture reach, shadows and the other layers have their own per-frame work that nobody has timed during a walk.

## The work

1. **Measure a walk, not a stand.** Add a tool (or extend `tools/measure_stand_budget.mjs`) that drives a fixed, scripted walk through the town (for example along Lake Street from Canal, then into a back lot, with a few turns) on the published mirror at 1280x800 and at 390x780. Run the mobile one under a CPU throttle that stands in for an iPhone (state the factor and why). Record the frame-time distribution (median, p95, p99, and the count of frames over 33 ms and 50 ms), long tasks, and per-layer time per frame (flora rebuild, trees, streets/yards lookups, render), at all three Scene detail tiers. Commit the reading under `docs/measurements/`.
2. **Fix the biggest cause the reading names.** If it is the flora rebuild, the likely fixes are: spread the rebuild over several frames, since `rebuildAll` is already a generator and the boot path already iterates it; rebuild only the ring band that changed instead of the whole cone; cache `station()` answers per lattice cell, since the lattice is world-anchored; or move the deal off the main thread. Keep flora.js's invariants: the same plant at the same slot (world lattice, fixed seed) and no plant popping in inside the nine-metre verge (`tools/measure_near_verge.mjs`). If the reading names something else, fix that instead and say why.
3. **Hold the gain.** Add the walk's p95 frame time (or over-budget frame count) as a measured number with a ceiling, the way T-1975 holds triangles, so the next layer that makes walking worse is caught before it merges.

## Acceptance

- The before and after walk readings at both viewports and every tier, committed. On the throttled phone profile at `light` (the tier a phone boots into), p95 frame time and the count of frames over 50 ms fall by a stated amount. No rebuild hitch remains that is visible at walking pace.
- No visible change in where plants stand, no pop-in inside the verge, smoke green at 390x780 and 1280x800, phone JS heap does not rise (T-2063).
- The changelog entry says plainly that walking is smoother and by how much.

## Coordination

Placed above the town-ground tickets on the owner's word. T-2092 is reading the derived town ground's cost; share its stands and the in-town poses. If T-2086 / T-2094 / T-2095 change what rebuilds per step, re-run the walk tool on them.
