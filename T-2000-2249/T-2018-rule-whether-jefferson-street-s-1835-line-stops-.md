---
id: T-2018
title: Rule whether Jefferson Street's 1835 line stops at Kinzie: its committed reach north to Hubbard crosses Wabansia block 59, which Wright's 1834 survey draws whole
state: review
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-03
closed: null
pr: 501
claimed_by: run 10/6/2026, 12:25:20 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37501055984
claimed_at: 2026-10-06T17:25:20.882Z
decision: null
decision_answer: null
---

Rule whether Jefferson Street's 1835 line stops at Kinzie: its committed reach north to Hubbard crosses Wabansia block 59, which Wright's 1834 survey draws whole.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 211 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> T-1414 held Jefferson out of the platted corridor layer on this question and closes; T-1490, which carried the line north, is done, so no live ticket owns it and the street would stay out of the layer by silence

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## Finding (T-1414, 2026-10-03)

Measured when T-1414 put the West Division's tiers and Wabansia into the platted corridor
layer (`data/traces/street_control.json` § `west_bank`). Taken into the layer too,
Jefferson's committed line (local north -400 to +381.887, carried north by T-1490 on the
Kinzie and Hubbard junctions) puts both reconstructed Wabansia bodies on block 59
(`blk_wabansia_c_t7`) into a platted roadway: `wabansia_doctors_barn` 12.11 m deep and
`wabansia_doctors_house` 1.38 m. Wright 1834 draws block 59 whole and reads Wabansia's grid
east-west only (`data/traces/wabansia_streets.json` reads no north-south corridor), so
adopting the corridor asserts an 1835 street through a block the survey draws whole.

**Acceptance:** a ruling — from a source that shows the 1835 state of the ground between
Kinzie and Hubbard west of the North Branch — on whether Jefferson's 1835 line stops at
Kinzie. Then either cut the record's reach at Kinzie and add `jefferson` to
`west_bank.tiers.west_division.axis.ns`, or keep the reach with the reading that licenses
it and re-seat the two reconstructed bodies (they are placements under L316, not readings).
`measure_corridor_intrusion.py --gate` holds either way.

## Measured 2026-10-05 (slice 3/5 run 37360845139, claim released, nothing committed)

- **Block 59 holds the whole corridor.** `generate_plat_lots.wabansia()` seats `blk_wabansia_c_t7` at east -489.45..-394.11, north 276.13..382.09. Jefferson's committed line crosses it at east -407.3 (north 276) and -409.9 (north 381.9). With the 12.192 m half-corridor that is -419.5..-395.1, so all 24.4 m of the roadway lies inside a block Wright 1834 draws whole, 1 m clear of its east rule. The survey does not place the street at the block's edge.
- **The cut is cheap downstream.** `measure_corporation_limits.limits_ring()` extends the West Division line on its own bearing to Ohio, so ending it at Kinzie leaves the ring collinear and its area unchanged. Only the "Jefferson, north to Ohio" reach grows from 288.3 m to about 406 m, and that is the stretch `measure_jefferson_continuation.py` already reads as undrawn. That tool and `data/traces/jefferson_continuation.json` pin +381.887 and 288.3 and would need re-deriving. `CORRIDOR_NS` in `generate_plat_lots.py` feeds the corridor layer only, not block cutting, so adding `jefferson` to `west_bank.tiers.west_division.axis.ns` re-cuts no lot.
- **Why released: it is invisible.** `jefferson` is `opened: false` with `track_width_m: 0`, so `streets.js createStreets` draws nothing for it either way. The visible-progress cap was already spent by v1500 ("Nothing you can see"), so this run took a visible ticket. Pair this with a visible unit, or take it under exemption 3 if a parcel waits on the corridor layer.
