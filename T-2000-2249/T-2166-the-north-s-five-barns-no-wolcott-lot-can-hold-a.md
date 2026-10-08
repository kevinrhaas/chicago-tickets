---
id: T-2166
title: The North's five barns no Wolcott lot can hold and the West's seven yard roofs: stand them behind the houses they serve or re-budget the rows, priced against the dwellings (T-1692)
state: open
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: T-2156
opened: 2026-10-08
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

The North's five barns no Wolcott lot can hold and the West's seven yard roofs: stand them behind the houses they serve or re-budget the rows, priced against the dwellings (T-1692).

Piece 2 of 2 of **T-2156 — Build or re-budget the order book's barns_stables and small_outbuildings roofs (North, South, West), pricing the yard buildings against the dwellings they serve (T-1692)**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2156 was split (2026-10-08T06:19:58.375Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 38m ago, run 10/8/2026, 12:41:30 AM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/37733398534) — held by the run that split it
- branch `steward/t2156-yard-buildings` — the splitter's own

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/37733398534) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

## Measured by T-2165 (2026-10-08) — why the North's five barns are not on the Wolcott block

The 668-roof schedule places the North's whole remainder — one A1 stable and five A2 barns or carriage sheds — on `blk_indiana_north_wolcott`, its only platted North block with ancillary room. That room is counted in roofs, not ground. Every lot there is 14.71 m × 31.33 m (`data/traces/vectors/thompson_lots.json`); each of the four cottage lots already keeps a woodshed or privy off the alley; and `tools/generate_block_infill.py` holds a footprint 1.5 m off its lot line (`LOT_MARGIN_M`) and 3.0 m off every other building (`MIN_SEPARATION_M`). That leaves 4.85-5.55 m of width beside each existing yard building, against an A2's 18 ft (5.49 m) narrowest band — and every A2 the recipe deals there samples 6.2-7.9 m wide. Between the yard building and the cottage there is at most 7.6 m of depth, against an A2's 26 ft (7.9 m) minimum. The open lots are refused by the north-division memo and the block's own open-lot reasons. T-2165 built the A1 stable (lot 9); the five A2 stay owed here.

**Priced against the dwellings (T-1692), before T-2165:** North 31 yard roofs / 84 ordinary dwellings = 0.37; West 27 / 75 = 0.36; South 80 / 150 = 0.53 (A1+A2 = barns_stables, A3-A5 = small_outbuildings, from `tools/measure_group_district_rows.py`). The North and West are the short divisions, so the honest home for their barns is behind the houses of the Kinzie core and the West's built blocks — which the schedule gives no ancillary room — rather than a cut to the rows. The fix is likely in `tools/reconcile_665.py`'s ancillary room (it should price a yard building against the yard it stands in), or a re-budget with this reasoning written into `district_group_matrix_note`.

The West's seven: `blk_washington_clinton` (A2, A3, A4, A5 — T-2148 already dealt eight yard buildings there; mind T-2150's open PR #510 on the same block) and `west_division_beyond_committed_control` (A2, A4, A5, a balance with no block).
