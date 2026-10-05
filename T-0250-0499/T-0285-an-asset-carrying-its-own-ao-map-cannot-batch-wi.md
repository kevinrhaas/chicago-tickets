---
id: T-0285
title: An asset carrying its own AO map cannot batch with the town: +2 draw calls for one building
state: split
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-08-28
closed: 2026-10-04
pr: null
claimed_by: run 10/4/2026, 10:15:55 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-05T04:38:49.227Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37258515015
claimed_at: 2026-10-05T03:15:55.243Z
decision: null
decision_answer: null
---

An asset carrying its own AO map cannot batch with the town: +2 draw calls for one building.

Measured by T-0227, 2026-08-28. `sauganash_hotel` baked with `--ao` and swapped into
the source tree raised the draw count at **every** station and viewport by exactly two:
`sauganash` desktop 112 -> 114, mobile 104 -> 106; `sauganash_wing` desktop 139 -> 141,
mobile 122 -> 124. Triangles were identical in all four. The cause is not the texture,
it is the key: `materialKey()` in `renderers/web/js/buildings.js` includes
`m.aoMap?.uuid`, and it has to — a batch is one draw with one material, so a mapped
material cannot merge with an unmapped one.

**Why it matters to R-W3a and not only to this one asset.** Every master gets its own
baked 512² atlas, so every master gets its own `aoMap` uuid, so no two AO'd buildings
can batch with each other either. The town's whole batching strategy is built on
buildings sharing a handful of materials. Nobody has measured what a fully-AO'd town
costs in draws, and the ceilings are breached already (T-0223, T-0271) — so this
number has to exist before the cage parcel bakes 348 maps, not after.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- The draw-call cost of AO on the town is MEASURED, not reasoned: bake a
  representative set with `--ao` (or all of them) and read the draw count at the
  critic stations at both viewports, against the same tree without it.
- The answer names which of the three routes it implies — a shared atlas across
  masters, a per-batch atlas built at load, or AO per-vertex — and what each would
  cost. Refuting the concern (the town batches fine) is a legitimate outcome.
- The figure lands in `docs/ROADMAP.md` R-W3a beside the byte cost, so the cage
  parcel starts from both.


## Queue cleanup 2026-10-03 (owner: "clean out any tickets that … no longer need to be there or are obsolete")

**Merged into this ticket:** T-0286. Both are the AO map's cost: the batch break and the empty atlas space are one AO-pipeline unit.

### Folded in from T-0286 — The AO unwrap leaves 68.9 per cent of every atlas empty, and the map is priced as if it were full

The AO unwrap leaves 68.9 per cent of every atlas empty, and the map is priced as if it were full.

Measured by T-0158 and re-derived by T-0227, 2026-08-28, on `sauganash_hotel`:
`smart_project(angle_limit=1.15, island_margin=0.02)` writes **81,458 of 262,144**
texels — **31.1 % occupancy**. The bake is correct; the packing is not. The asset's
master goes 94,420 -> 202,292 bytes with AO on, so a ~107 KB occlusion PNG is spending
roughly 74 KB of itself on blank space.

`assets/gltf/` is 27 MB over 348 masters and the published tree stands at 23.53 MB
against a 25 MB `SITE_BUDGET_MB`. One 512² map each is a ~37 MB ask against ~1.5 MB of
headroom (T-0158's figures), which is what makes the empty two thirds a budget question
rather than a tidiness one: at full occupancy the same coverage fits a 288² atlas.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- Occupancy is measured across a representative set of masters, not one — one asset is
  an anecdote about one unwrap.
- One packing change is made and re-measured (island margin, angle limit, or a pack
  pass), with the before/after occupancy and byte figures stated.
- Texel DENSITY on the walls does not fall to buy the occupancy: state the texels per
  square metre on a named wall before and after, because a tighter pack that shrinks
  the islands has bought nothing.
- No claim about how the result looks without a `tools/measure_ao_frame.mjs` reading
  behind it (T-0227's rule: an atlas statistic is not a statement about the walls).
