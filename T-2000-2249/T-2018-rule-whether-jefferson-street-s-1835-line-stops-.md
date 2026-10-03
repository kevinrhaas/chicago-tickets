---
id: T-2018
title: Rule whether Jefferson Street's 1835 line stops at Kinzie: its committed reach north to Hubbard crosses Wabansia block 59, which Wright's 1834 survey draws whole
state: open
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-03
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
