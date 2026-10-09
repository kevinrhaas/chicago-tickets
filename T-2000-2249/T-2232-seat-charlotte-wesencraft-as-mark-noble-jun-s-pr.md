---
id: T-2232
title: Seat Charlotte Wesencraft as Mark Noble jun.'s printed wife and land the column-title sex readings (Mark jun. male, Charlotte, Anne Maria Barney female, Alson Woodruff male): the code is on steward/t2230-noble-brides; re-derive the layer, carrying the T-2021 families the flips withdraw through the modelled-families / women-and-children / re-family-rule fixpoint, the seating and any rebake, and gate
state: review
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: T-2230
opened: 2026-10-08
closed: null
pr: 554
claimed_by: null
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: null
decision: null
decision_answer: null
---

Seat Charlotte Wesencraft as Mark Noble jun.'s printed wife and land the column-title sex readings (Mark jun. male, Charlotte, Anne Maria Barney female, Alson Woodruff male): the code is on steward/t2230-noble-brides; re-derive the layer, carrying the T-2021 families the flips withdraw through the modelled-families / women-and-children / re-family-rule fixpoint, the seating and any rebake, and gate.

Piece 1 of 2 of **T-2230 — Seat the two brides of the Democrat's 3 December 1833 MARRIED column: Charlotte Wesencraft as Mark Noble jun.'s wife and Mary Noble as George Bickerdyke's (where T-2020 folded Bridget Ryan in), reading the column's Mr. and Miss onto the two cards drawn the wrong sex ('Jun Marknoble' drawn female; Charlotte drawn male, heading a modelled wife and sons)**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2230 was split (2026-10-09T01:22:25.521Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 10m ago, run 10/8/2026, 8:12:10 PM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/37868324385) — held by the run that split it
- branch `steward/t2230-noble-brides` — the splitter's own

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/37868324385) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

## The step T-2234 built for this, measured on #554's tree (2026-10-09)

T-2234's PR #555 (`steward/t2234-family-cycle-fixpoint`) adds `tools/settle_family_cycle.py`. It had a green gate when it was handed on with `resume`, for a changelog-only conflict with dev. Once it is on dev, #554's lap needs nothing but this: merge dev, run the sex pass (`rebuild_resident_index.py --write`, `reconstruct_sex_age.py --build`, `spend_person_sex_age.py`), then run `python3 tools/settle_family_cycle.py --build --strict`, then `rederive.mjs --tail tools/compile_scene.py`, rebake anything stale, and gate.

Measured with #555's code on #554 over dev: lap 1 moved, lap 2 moved nothing. The book (owner gate on) and all six stages re-derive. Two things in #555 are what made it settle:

- **The withdrawn admissions.** `hh_barney_anne_maria` (read female) and `hh_wesencraft_charlotte` (the printed bride) were admitted by T-2021's frozen ruling. They now take their five ordered cells with them, and nobody is ruled in their place. That leaves 154 admitted, where there were 156.
- **T-2019's female-headed promise** now nets out a printed bride's own folded house, which moved the count from 128/1448 to the promised 129/1449.

Women-and-children's deal does not move at all, and the re-family rule changes by 8 lines.
