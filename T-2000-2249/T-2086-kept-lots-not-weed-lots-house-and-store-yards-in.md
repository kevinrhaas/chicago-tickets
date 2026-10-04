---
id: T-2086
title: Kept lots, not weed lots: house and store yards in short grazed turf with worn paths, weeds and flowers moved to fence lines, corners and dooryard beds, vacant lots left as flowering prairie remnant
state: done
epic: TOWN
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-10-04
closed: 2026-10-04
pr: 416
claimed_by: run 10/4/2026, 11:16:28 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-04T17:57:37Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37215922897
claimed_at: 2026-10-04T16:16:28.040Z
decision: null
decision_answer: null
---

Kept lots, not weed lots: house and store yards in short grazed turf with worn paths, weeds and flowers moved to fence lines, corners and dooryard beds, vacant lots left as flowering prairie remnant.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 189 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> Owner asked on 2026-10-04 for detailed tickets for tidier town ground cover, placed at the top of the queue; he prefers several well-scoped tickets filed now over one split later

## Why this ticket exists (owner, 2026-10-04)

Third of four for the owner's town-ground ask. Kevin: "less 'weedy' in the town area, in front of stores and houses, and in the house back yards and properties", but "I don't want you to go crazy and cut all the beautiful plants and grass and flowers ... I think we can improve the rendering and make it look more realistic and accurate." T-2084 puts the town on settled-town ground and T-2085 draws short turf cheaply. This one decides WHERE on a lot the ground is kept short and where the weeds and flowers survive, so the town looks lived in and the flowers are kept where a working 1835 lot would actually have them.

## What the data says today

- `z10_settled_town` grows one undifferentiated mix everywhere it reaches: *Poa*, plantain, knotweed and white clover as the low layer, and lamb's-quarters, pigweed, ragweed, cocklebur, curled dock and white vervain at 0.3–1.2 m as forbs. Its note says the composition is "inferred throughout: every species in it is a regional weed list, not a Chicago record". Spread evenly over every lot, the tall weeds are what reads as "weedy".
- The lot furniture this needs is already in the data: lot-line fences (`data/enclosures/town_lot_line_{pickets,boards,rails}.json`), dooryard gardens on every house lot (T-1958, `yards.js` `dooryard_garden`), woodpiles, wells, privies and stables by household (T-1959, T-1960, `data/yard/`), trade yards (`town_trade_yards.json`). The plat lots come from `tools/generate_plat_lots.py`.

## The work

1. **Kept ground by use, on the lot.** Within a built lot: the yard between the house and its outbuildings is short grazed/trodden turf (T-2085's texture); worn earth on the paths between door, well, privy, woodpile and stable; and the weeds and flowers move to where scythe, hoof and foot do not reach: along fence lines and lot lines (a 0.5–1 m strip), in the lot's back corners, and around the outbuildings' foundations. The dooryard garden keeps its beds. A store's or tavern's working yard stays worn earth (T-0067's `worn_earth`).
2. **Vacant lots are not yards.** A platted lot with no building stays grazed prairie remnant: shorter and patchier than the open prairie outside the town (the record's grazing halo), with its flowers, so the "beautiful plants" are still in town between the houses.
3. **Data, not a renderer rule.** Whether this is a per-lot ground record written by a generator (re-derived byte for byte by `check.sh`, like `generate_frontage_works.py`) or two communities (kept lot vs settled-town commons) selected by the derived extent, the decision of which ground gets which treatment lives in `data/`, and the renderer only reads it. The kept-lot pattern is `reconstructed` and gets a liberty in `docs/LIBERTIES.md` (next free L number taken at merge time from dev and the open PRs; do not reserve one now). The 1835 evidence for grazed commons (the 7 Nov 1833 ordinance on wandering pigs, cattle on the unfenced commons) is already in the zone record and is the basis; a mown lawn is not 1835 (docs/RESEARCH/1835_photographic_fabric_preparation.md), so the short ground is cropped, not striped.
4. **Cost stays inside what T-2085 freed.** Fence-strip and corner forbs are near-ring plants at most, with flower heads only where the record's July state allows (the July gate in flora.js stands).

## Acceptance

- Captures at both viewports from the backyard pose and two new ones (a store's back yard on South Water, a vacant lot between two houses): short turf in the yard, worn paths to the outbuildings, flowers and weeds along the fences and in the corners, a vacant lot still visibly a flowering remnant.
- Triangles and draw calls at the in-town poses and T-0135's stands reported against T-2085's after-reading; neither rises past it at any tier; phone heap does not rise.
- `check.sh` re-derives whatever record this writes; T-2087 finishes the strips between the lots and the road. The liberty is recorded; changelog entry.

## Coordination

T-1943 (north-block boundaries, gardens and frontage fittings) is open and touches the same lots north of the river: read it first and do not duplicate its fences or gardens; this ticket only decides the ground between them.
