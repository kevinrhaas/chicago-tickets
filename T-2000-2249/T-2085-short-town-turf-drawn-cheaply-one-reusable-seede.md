---
id: T-2085
title: Short town turf drawn cheaply: one reusable seeded 1835 turf texture under the settled-town ground, near tufts only on turf, the Scene detail tiers made town-aware, and the full and balanced ceilings taken back down
state: open
epic: TOWN
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

Short town turf drawn cheaply: one reusable seeded 1835 turf texture under the settled-town ground, near tufts only on turf, the Scene detail tiers made town-aware, and the full and balanced ceilings taken back down.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 188 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> Owner asked on 2026-10-04 for detailed tickets for tidier town ground cover, placed at the top of the queue; he prefers several well-scoped tickets filed now over one split later

## Why this ticket exists (owner, 2026-10-04)

Second of four for the owner's town-ground ask, after T-2084 (the settled-town ground carried over every built block). He asked for "a lower grass that might be easier for you to depict and render with some strong textures and be reusable so you don't have to spend much rendering on it", to "alleviate your triangle concerns and reduce lagginess", and asked that the existing reduce-plants setting be considered as one leg of it. That setting is **Settings > Performance > Scene detail** (`index.html` ~566: Full "every plant and tree", Balanced "fewer plants", Light "fewest, for slow machines"), read by `main.js` (`DETAIL_ORDER` ~945, rebuild on change ~2061) and applied to the sward by `flora.js` `mergeTune()` (~2253) through the `MID` (~817) and `LOW` (~750) presets.

## What the renderer does today

- The sward is three bands (flora.js header): NEAR blade geometry to ~8 m, MID camera-facing clump cards to ~27 m (18 m at Balanced, 13 m at Light), and a FAR card band out to 120–150 m, with flower heads per recorded inflorescence. Beyond that, the terrain's procedural prairie tile (`prairie-tile.js`, 256 px over 11 m; `terrain.js` `prairieTexture()` ~1698) carries the colour, tinted per community by `ground.rgb` through `substrateZones()` (~1304).
- `flora.js` MID's own comment says what binds: "at full detail the CAPS ARE NOT WHAT BINDS — the ring radii are ... the mid ring's area". On short turf the mid and far card bands are spending triangles on something a texture can carry: a 0.05–0.20 m sward is a fraction of a pixel tall at 10 m.
- There is already a short curated green on the ground: `yards.js`'s `dooryard_green` treatment (PERIOD_M ~403) inside the T-1958 dooryard gardens. And the 1904 library's `prairie_1904_pbr/parkway/grass_plat` plus Glessner's 4 m lawn study (docs/RESEARCH/1835_photographic_fabric_preparation.md § 1–4: "coherent 0.5–2 m growth/thatch variation") are the method precedent. The same document is explicit that "a mown lawn is not 1835 Chicago": the 1835 turf is cropped by grazing and feet, with bare patches, dung-dark and dusty spots, clover and plantain, not a striped lawn.

## The work

1. **One reusable 1835 short-turf ground texture**, seeded and deterministic, at metric scale, sampled in world space like the prairie tile so it never stretches: grazed *Poa*/clover/plantain turf with 0.5–2 m coherent variation (thinner and dustier where trodden, the record's 45 % bare soil). Either a runtime canvas like `prairie-tile.js` (no image asset, zero wire bytes) or a library map with its `assets/LICENSES.md` entry, chosen by measured cost; if it needs Blender, it goes through the steward runners. It is bound where the settled-town community is, through the substrate path `terrain.js` already has, so it costs no draw call.
2. **Fewer, cheaper plants on that ground.** In the settled-town community: the near ring keeps low tufts (short, few triangles, no forb heads except the record's flowering weeds); the MID and FAR card bands draw nothing on turf, because the texture now carries it; trees and the prairie outside the town are untouched. Keep `flora.js`'s rule that a species, its July state and its abundance are evidence: this changes how far and in what form plants are DRAWN, never which community grows there.
3. **The Scene detail tiers, town-aware.** Full keeps near tufts on turf; Balanced and Light show turf as texture only past a short radius, so a slow phone in the town spends almost nothing on ground cover. The prairie outside the town keeps today's tiers. Update the three option labels only if their meaning changes, and keep the setting's storage key.
4. **Measure, and give the room back.** Re-run T-2084's sweep (T-0135's stands + the three in-town poses, both viewports, all tiers): flora triangles, draw calls, frame time, phone JS heap. Then apply T-1975's rule in `main.js` (worst stand plus T-0672's absolute headroom, rounded to 5,000) and take the `full` and `balanced` ceilings DOWN to what the town now costs, and say how far `light` sits inside its 825,000 / 90-call floor. T-0672 has owed the return of the 2026-09-03 raise; record whether this pays it.

## Acceptance

- Captures from the three in-town poses at both viewports and all three tiers: the yards and lots read as short kept turf with a strong, non-repeating texture at walking distance and from the open aerial; no visible tiling period at 20 m; no seam where turf meets prairie (the halo grades, as the prairie tile's thatch and loam do).
- Flora triangles at each in-town pose fall at every tier, by a number the PR states; total triangles at T-0135's worst stand fall; draw calls do not rise at any tier; frame time at the in-town poses is reported before and after; phone JS heap does not rise.
- `full` and `balanced` ceilings re-set downward in `main.js` with the measurement committed; smoke green at 390x780 and 1280x800 (mobile is a release gate).
- Changelog entry; the texture's look is `reconstructed` and gets a liberty (next free L number taken at merge time from dev and the open PRs; do not reserve one now).

## Not this ticket

Which parts of a lot are kept and which stay weedy or flowered is T-2086. Road shoulders, alleys, store aprons and door paths are T-2087.
