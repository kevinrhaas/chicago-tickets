---
id: T-1745
title: The 1904 grid's remaining lots: Robinson 1886 legal lot numbers on 16th-18th Prairie, and the Indiana and Calumet frontage lots
state: split
epic: SOUTH_TIME
requested_by: steward
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-09-28
closed: 2026-10-04
pr: null
claimed_by: run 10/4/2026, 7:38:05 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-05T00:49:18.704Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37248032401
claimed_at: 2026-10-05T00:38:06.010Z
decision: null
decision_answer: null
---

The 1904 grid's remaining lots: Robinson 1886 legal lot numbers on 16th-18th Prairie, and the Indiana and Calumet frontage lots.

Follow-up of **T-0474** (PR #179), which laid out the 1904 grid in `data/street_grid/1904.json`
(`tools/trace_prairie_1904_grid.py`): streets, block faces, alleys, and the 92 lots the Sanborn 1911
sheets 20, 28 and 35 draw on BOTH FACES OF PRAIRIE, 16th to 22nd. Two things were left, listed in
`docs/RESEARCH/prairie_1904_street_grid.md` § 6:

1. **Legal lot numbers.** The parcels are the lots the Sanborn sheets draw (ownership parcels).
   Robinson 1886 plate 10 (`robinson_1886_chicago_plate_10`, georeferenced by T-1250) prints the
   subdivision and lot numbers for 16th-18th. Read them onto the 16th-18th Prairie parcels as a
   `legal_lots` attribute with its tier. South of 18th only HABS's legal description of 1800 Prairie
   is in hand (Block 9, lots 39, 40 and the north 17 ft of lot 38); it goes on `prairie_1800`.
2. **The Indiana and Calumet frontage lots.** The blocks are laid out, but the lot lines between the
   alleys and Indiana (sheets 20, 35) and Calumet (sheets 28, 35) are not read. Add them to the
   tool's FACES with their printed addresses (sheet 27, Indiana 18th-20th, was not supplied; say so).

**Acceptance:** both land in `data/street_grid/1904.json` through the tool (picks on the committed
rasters, `--check` and `--self-test` green); each lot carries source and tier; a card opened on a
16th-18th Prairie lot at `/4d/1904/` shows its Robinson lot number.
