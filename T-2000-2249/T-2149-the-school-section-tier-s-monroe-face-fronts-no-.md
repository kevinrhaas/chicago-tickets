---
id: T-2149
title: The School Section tier's Monroe face fronts no street: plat_corridors.py carries no corridor for Monroe, so the frontage census, placement policy and redeal audit read every Monroe-face roof on blocks 81/94/95/118/119 as fronting none (Madison, 98 m off, is the nearest), the audit re-families three of block 81's houses and measure_block_redeal_remedies --self-test goes red. Rule how Monroe enters the frontage reading
state: open
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-05
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

The School Section tier's Monroe face fronts no street: plat_corridors.py carries no corridor for Monroe, so the frontage census, placement policy and redeal audit read every Monroe-face roof on blocks 81/94/95/118/119 as fronting none (Madison, 98 m off, is the nearest), the audit re-families three of block 81's houses and measure_block_redeal_remedies --self-test goes red. Rule how Monroe enters the frontage reading.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 156 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> it blocks three builds (T-2145, T-2146, T-2147), not one, so a paragraph on any one of them would hide it from the other two

## FILED ABOVE BAND 9, BECAUSE IT BLOCKS

A follow-up goes to the foot of band 9 unless dev's gate is red on it or the build in hand cannot finish without it (owner, 2026-09-27). This one was placed above band 9 on this reason:

> T-2147's PR #493 gate is red on it, and T-2145/T-2146 build on the same Monroe face

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## Finding (T-2147's lap of PR #493, 2026-10-06)

Measured on `steward/t2147-school-section-block-81` after merging dev (T-2143):

- `tools/measure_frontage_fabric.py`'s `census()` reads `plat_corridors.corridors()`, which is
  `CORRIDOR_EW`/`CORRIDOR_NS` only. `monroe` is drawn in `data/streets/1835.json` (24.384 m
  corridor, N -655.83) but sits in `omitted_corridors()` — the School Section's survey, not the
  module's. So block 81's four Monroe-face roofs (`_d6_01`, `_d4_03`, `_d3_05`, `_d7_07`) read
  `street: null`, setback ~98.7 m (to Madison across the block). The census's own count went
  36 -> 40, restated on the branch with that reason.
- `placement_policy_1835._breaches` then refuses D3-D7 there ("fronts no street ... `yard` /
  `typology` setback, which is measured from one"), and `redeal_anonymous_roofs.py --build`
  writes `refamily` for `_d4_03` (-> A2), `_d6_01` (-> D1), `_d7_07` (-> D1). `_d3_05` is kept
  only because it is seated.
- `measure_block_redeal_remedies.py` sweeps those in (the phase is `phase3_platted_block_*`):
  outstanding 2 -> 5, `refused_by_the_parcel_gate` 0 -> 2, `inventory_class_moves` 0 -> 1,
  `ancillary_families_offered` 0 -> 1, and its `--self-test` fails all three assertions. That
  is the only red step left on PR #493 (781 of 782 green).

The two obvious readings, neither taken here because each moves every roof near an omitted
street: (a) Monroe (and the tier's other School Section lines) join the frontage census's
corridor set (not the plat's block-grid set — AGENTS.md rule 10, T-1726); (b) the census reads
`every_corridor()` for "which street does this roof front", keeping `corridors()` for the
block-face gates. Either needs the seating walked to its fixpoint after.
