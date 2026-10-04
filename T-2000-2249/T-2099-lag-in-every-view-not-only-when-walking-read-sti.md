---
id: T-2099
title: Lag in every view, not only when walking: read still-frame GPU and CPU time at every stand, the aerial and overview, arrival and jaunt views and the 1812 and 1904 scenes, attribute it by layer and pass, fix the largest causes, and hold a frame-time ceiling per tier
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

Lag in every view, not only when walking: read still-frame GPU and CPU time at every stand, the aerial and overview, arrival and jaunt views and the 1812 and 1904 scenes, attribute it by layer and pass, fix the largest causes, and hold a frame-time ceiling per tier.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 191 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> Owner, 2026-10-04: lag is everywhere, not only walking; T-2096 owns the moving cost, this owns the still-frame render cost in every view and year

## Why this ticket exists (owner, 2026-10-04)

Kevin, 17:18 UTC: "when you walk it is laggy now", then at 17:25: "that lag is all over not just walking of course". T-2096 owns the cost of MOVING: rebuilds that fire when you walk, turn or fly. This ticket owns the cost of a FRAME when nothing is being rebuilt: standing still, looking around a stand, the overview and aerial views, the arrival and jaunt screens, and the other years (1812, 1904 Prairie Avenue with the Glessner house). If standing still is laggy too, the plant recompute cannot be the whole story, and the steady per-frame render cost is the other half.

## What is known (read 2026-10-04 on dev; numbers from committed measurements, the rest inferred)

- Triangles at T-0135's worst stand, desktop, measured for T-1975/T-1959: `full` about 1.78 M, `balanced` 1.55 M, `light` about 0.94 M before T-1976's trim; up to 224 draw calls at `full` (docs/measurements/t-1975-*.json, t-1959-*.json, `main.js` ~540–600). Those are ceilings on a still frame's GEOMETRY. Nobody has read a still frame's TIME, on the GPU or the CPU, at any stand.
- Per-frame costs that do not show in a triangle count: soft PCF shadows (`world.js` ~614, `PCFSoftShadowMap` unless lowSpec) and the shadow pass's own geometry; the per-fragment road, grit, turf and grain shaders added this week (T-1811, T-2085, T-2089, T-2090); the alpha-tested foliage and card overdraw; pixel ratio (`main.js` ~1362: up to 2 on desktop and 1.5 on touch, set by Image sharpness); and the CPU side of 200+ draw calls with per-frame uniform updates.
- Kevin tests on an iPhone (Chrome on iOS), where the GPU and thermal limits bind first.

## The work

1. **Read still-frame time everywhere**, with the same tool T-2096 builds (or `tools/measure_stand_budget.mjs` extended): GPU frame time (via `EXT_disjoint_timer_query_webgl2` where available, otherwise rAF intervals with nothing moving), CPU frame time and draw calls. Take it at T-0135's five stands, T-2084's in-town poses, the open aerial and overview, the arrival screen, a jaunt view, and the 1812 and 1904 scenes' own landing stands. Use 1280x800 and 390x780, the latter throttled as a phone stand-in, at every Scene detail tier and Image sharpness setting. Commit the table.
2. **Attribute the cost** by turning layers and passes off one at a time (shadows, flora, trees, frontage, streets, yards, terrain shaders, post), in the style of `tools/measure_layer_share.mjs`, so the table says what each one costs in milliseconds and not only in triangles.
3. **Fix the largest one or two causes** the table names, at whichever tier and viewport they bind: for example, cheaper shadows at `balanced`/`light`, a lower default pixel ratio on phones, overdraw trimmed, or draw calls merged. Do not change what is drawn where unless the owner agrees. A change a visitor would notice in a screenshot is put to the owner first.
4. **Hold it**: a still-frame time ceiling per tier at the worst stand, next to T-1975's triangle ceilings, so the next parcel that makes every frame slower is caught.

## Acceptance

- The committed table, before and after, covering every view and year listed above.
- At `light` on the throttled phone profile and at `full` on desktop, the worst still-frame time falls by a stated amount, and no view gets slower.
- Smoke is green at 390x780 and 1280x800, and phone JS heap does not rise (T-2063).
- A changelog entry that says plainly what got faster and by how much.

## Coordination

T-2096 covers moving (walking, turning, flying), and this ticket covers still frames. Build one measuring tool for both, whichever ticket is taken first. T-2092 is reading the new town ground's cost at the same stands, so share its poses.
