---
id: T-2084
title: The town stands in wet prairie: carry the settled-town ground from the 1835 forks polygon over every built block, street corridor and alley by a derived extent, trees held, with a before reading at three in-town poses
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
claimed_by: run 10/4/2026, 9:03:15 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37205826122
claimed_at: 2026-10-04T14:03:15.243Z
decision: null
decision_answer: null
---

The town stands in wet prairie: carry the settled-town ground from the 1835 forks polygon over every built block, street corridor and alley by a derived extent, trees held, with a before reading at three in-town poses.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 187 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> Owner asked on 2026-10-04 for detailed tickets for tidier town ground cover, placed at the top of the queue; he prefers several well-scoped tickets filed now over one split later

## Why this ticket exists (owner, 2026-10-04)

Kevin, walking the 1835 town: in backyards, along the sides of the roads, in front of stores and houses, in the alleys and on the paths, the ground is still "dense foliage, and a lot of grass and flowers". He expects the town's ground to be lower and kept, "less weedy", so the town reads as lived in and not "just dropped on a prairie", and he wants the same change to ease the triangle budget and the lag. Not fewer trees, and not cutting all the beautiful plants. This is the first of four tickets for that ask: T-2084 (this one, the ground), T-2085 (the turf drawn cheaply, with the Scene detail setting), T-2086 (kept lots), T-2087 (road shoulders, alleys, frontages and paths).

## What the code does today (read 2026-10-04 on dev @ 4413ff04)

- The settled-town community `data/flora/zones/z10_settled_town.json` is the only sward in the dataset that is already the right thing: "a cropped, hoof-poached, dusty weedy halo", `cover.matrix_fraction` 0.45, `bare_soil_fraction` 0.45, matrix *Poa pratensis* at 0.05–0.20 m. Its extent is a hand-drawn polygon (E -160..186, N -186..16, priority 60) whose own note says it was "drawn around the eight structures the 1835 scene actually places".
- The scene now places **560 structures with a position; 19 of them stand inside that polygon** (measured 2026-10-04 by projecting every `data/structures/*.json` first-phase `position` through `data/datum.json`'s origin and testing it against the polygon with the same point-in-polygon rule `flora.js` `matches()` uses). Every other house, store and yard stands in a prairie community chosen by the terrain (`z01_wet_prairie` matrix is cordgrass 1.2–2.0 m, bluejoint, big bluestem; forbs include prairie dock at 2–3 m). That is exactly what the owner walked through.
- `flora.js` places plants by community (`zoneFinder` / `matches`, flora.js ~3207–3290) and only refuses a station through `growthBlocked`, which `main.js` ~1982 composes as `streets.blocksGrowth` (the worn track plus a 0.65 m shoulder, streets.js ~2027) `|| yards.suppressesSward` (fenced yards and the T-1958 dooryard gardens) `|| stripBlocks || workingBank.blocksGrowth`. Everything else in the town grows the prairie.
- `trees.js` also reads `z10_settled_town` (TIMBER_ZONES, ~line 87; relict cottonwood / elm / black willow by density, plus the planted Lombardy rows held per zone ~583). Growing the extent therefore changes where relict timber may stand, not only the sward.

## The work

1. **Measure before changing** (this is what stops the change redefining success). With `tools/measure_stand_budget.mjs` and `tools/measure_detail_ceilings.mjs`, at T-0135's five stands AND three new in-town poses added to `measure_detail_ceilings.mjs` (a house backyard on a back-street block, a road edge on Lake or Randolph, a storefront on South Water), at 1280x800 and 390x780, at `full`, `balanced` and `light`: triangles and draw calls with the `flora` layer's share broken out, frame time, and on the phone profile the JS heap (T-2063's lesson: watch heap when 1835 content changes). Commit the reading under `docs/measurements/`. Take before captures from the three in-town poses.
2. **Derive the settled-town extent instead of hand-carrying it**, the way T-1722 derived the North Division ring (`tools/measure_northern_ground.py`): a tool that builds the polygon(s) from the committed plat (`tools/generate_plat_lots.py` blocks, `data/streets/1835.json` corridors and alleys) and the committed footprints, buffered by the dossier's grazed halo at its low end (50 m, `docs/research/02-flora.md` ZONE 10, the record's own note), writes it into `z10_settled_town.json` and the flora manifest together, and fails `check.sh` when they drift. The next district a run builds then gets town ground for free. Rewrite the extent note: the "eight structures" sentence and "isolated buildings ... stand in open prairie" are stale.
3. **Hold the trees where they are**, unless the owner says otherwise: the relict-timber density is evidence about part-cleared blocks at the forks, not about every lot in the plat. Either keep the woody layer reading the old polygon (a separate `timber_extent`, or the same tool writing both) or show with a stem count that the tree population and the frame cost do not move. "Not fewer trees" is the owner's instruction; "not suddenly more" is the measurement's.
4. Re-run the measurement in 1. The after captures from the same three poses go in the PR.

## Acceptance

- The three in-town poses, before and after, at both viewports: no prairie grass above knee height inside a house or store lot or on a corridor shoulder; prairie stays outside the halo, and dooryard gardens, planted rows and trees are where they were.
- The derived extent covers every built block (count of structure positions inside: 560 of 560, or each one outside is named with its reason), and `check.sh` refuses a hand edit of it.
- The flora layer's triangles at the in-town poses and at T-0135's stands are reported before and after per tier; neither total rises. Draw calls do not rise at any tier (`light`'s 90-call floor). Phone heap does not rise.
- Changelog entry (new on top, `v: null, ts: ''`, stamped); visible change, so the visible-progress rule is met. The extent grows on the dossier's evidence (an `inferred` extent), so no new liberty is expected; if one is needed, take the next free L number from dev and the open PRs at merge time, not now.

## Not this ticket

How the short ground is DRAWN (texture, tufts, tiers) is T-2085; which parts of a lot are kept vs weedy is T-2086; road shoulders, alleys, store aprons and door paths are T-2087. T-1974/T-1975 own the ceiling numbers; this ticket reports into them and does not re-set them.
