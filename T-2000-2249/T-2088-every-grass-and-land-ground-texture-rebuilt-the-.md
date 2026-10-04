---
id: T-2088
title: Every grass and land ground texture rebuilt the road's way: the prairie tile, the sand, marsh and sedge ground, the bank soil and the yard canvases get T-1811's shared grain-and-normal tile with world-space multi-scale variation and recorded tones
state: claimed
epic: TOWN
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-10-04
closed: null
pr: null
claimed_by: run 10/4/2026, 8:40:42 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37206300067
claimed_at: 2026-10-04T13:40:42.305Z
decision: null
decision_answer: null
---

Every grass and land ground texture rebuilt the road's way: the prairie tile, the sand, marsh and sedge ground, the bank soil and the yard canvases get T-1811's shared grain-and-normal tile with world-space multi-scale variation and recorded tones.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 191 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> Owner, 2026-10-04: upgrade the other grass and land textures the way the road texture was done; filed beside his town-ground tickets at the top

## Why this ticket exists (owner, 2026-10-04)

Kevin, after the town-ground tickets (T-2084..T-2087) were filed: "we learned a lot about textures and the road texture is beautiful I am thinking you can update and improve all the other grass and land textures in the same way also and that may help." A ground that carries its own grain, clumping and tone needs fewer plants standing on it to read as grass, so this also helps T-2085's triangle goal.

## The road's method (what "the same way" means)

The streets were rebuilt by T-1797 (the ground-strip proof) and T-1811 (the worked roadway), and the doors got the same surface by T-2013. Read `renderers/web/js/streets.js` `roadGrit()` (~1591) and `ROAD_FRAGMENT` (~1622), and `ground-strip-mask.js` `gritTilePixels`:

- **One small shared tile for fine relief**: 256 px over 1.6 m, seeded and deterministic, R = height read as grain and G/B = the normal, built once as a canvas, so it costs no image fetch and no wire bytes. Every street samples the same tile in WORLD coordinates, so nothing stretches across the bake's planar dissolves.
- **Everything coarser is procedural value noise in the shader** at stated scales: 11 x 1.3 m and 4 x 0.55 m lanes, 0.6–2 m clumps, 7–18 m wet patches, a 35 m tone. Nothing repeats at walking distance.
- **Colour is recorded tones x the grain over its own mean**, not a photo. The tones come from the 1835 library (`assets/textures/chicago_1835_pbr`) and the fabric map (docs/RESEARCH/1835_photographic_fabric_preparation.md § 4, § 8). The relief is lit with the real sun, which is what makes the road look photographic.
- The library maps whose relief T-1797 measured flat (loam, muck, sand) were not used for relief. Their colour was reused and the generated grit carried the grain.

## What still uses the old way

- The terrain's prairie ground: `prairie-tile.js` (256 px over 11 m, colour only, no normal), drawn by `terrain.js` `prairieTexture()` (~1698) and tinted per community through `substrateZones()` (~1304). T-1825 improved its colour (thatch and loam minorities), but it still has no grain or normal and no world-space clumping. That covers the wet, mesic, sand prairie, sedge meadow, marsh edge and lake sand ground as seen from a distance.
- `yards.js`'s canvases: `worn_earth`, `trodden_earth`, `dooryard_garden`'s beds and `dooryard_green` (PERIOD_M ~403). `road_earth` already uses the grit since T-2013.
- The worked river bank (`working-bank.js`) and the grey sand to prairie edges (T-1819, T-1824).

## The work

1. **A grass grain tile** in the grit's format (height + normal, seeded, world-space): blade-and-thatch grain at a fine metric scale. Plus a soil/sand variant if the grit itself does not serve.
2. **The terrain ground on that method**: per community, a recorded tone pair x the grain, with world-space clumping (0.5–2 m, the Glessner lawn-study scale), mid-scale patches (bare loam, thatch, wet where the record says wet) and a broad tone, lit through the normal. Carried by the existing substrate path, so it adds no draw call. Each zone's mean albedo still comes out at the triple its flora record states (that is what `prairie-tile.js` exists to measure, so keep that gate).
3. **The yard treatments on the same tile**: worn and trodden earth reuse the road's grit and tones the way `road_earth` does; the dooryard green and T-2085's town turf use the grass grain. T-2085 builds the turf; whichever of the two lands second adopts the other's tile rather than keeping two.
4. **The bank soil and sand edges** take the same grain where they meet grass, so no seam is left between the road's dirt, the yard, the turf and the prairie.

## Acceptance

- Before/after captures at both viewports (390x780, 1280x800) from T-0135's stands, T-2084's three in-town poses, the open aerial and the west prairie flora-review pose: the ground reads as grass, soil and sand with visible grain and clumping at walking distance, no visible tiling at 20 m, and no seam at a road, yard or zone edge.
- Each zone's mean albedo gate stays green. No new draw calls at any tier, and texture memory and boot payload are reported (12 MB boot budget, docs/SITE-BUDGET.md). Frame time at the in-town poses and phone JS heap do not rise.
- Changelog entry. The procedural look is `reconstructed`, so it gets a liberty (next free L number taken from dev and the open PRs at merge time, not reserved now). Any new library map gets its `assets/LICENSES.md` entry.

## Coordination

T-2085 (turf) and this ticket share one grass tile. The road's own surface stays T-1811's and is not re-tuned here.
