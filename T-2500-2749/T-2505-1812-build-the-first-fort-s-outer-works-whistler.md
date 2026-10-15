---
id: T-2505
title: 1812: build the first fort's outer works Whistler's draught indexes and T-2062 left unbuilt: the interpreter's house (19), armourer's shop (20), merchant's shop (21), bake house (22), the factor's-department house (23), the wharf (27) and the covered way (33)
state: claimed
epic: SOUTH_TIME
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-10-15
closed: null
pr: null
claimed_by: run 10/15/2026, 2:46:39 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38700277310
claimed_at: 2026-10-15T07:46:39.639Z
decision: null
decision_answer: null
---

1812: build the first fort's outer works Whistler's draught indexes and T-2062 left unbuilt: the interpreter's house (19), armourer's shop (20), merchant's shop (21), bake house (22), the factor's-department house (23), the wharf (27) and the covered way (33).

## Where it comes from

Ruled IN by T-2489 (the owner's ask of 2026-10-13 for every known structure of 1812; T-2489 directs a build ticket for each structure it rules in, filed under it). The reading is `docs/RESEARCH/1812_other_structures.md` (on dev once T-2489's PR merges). Every rule in T-2484's "How it is built" applies unchanged: dated to cover 1 and 14 August 1812 and close before 1835-07-01; never invent a source; the image gate where a picture exists; liberties numbered in `docs/LIBERTIES.md` and `data/liberties.json`; no human figure; gate, smoke by parts, both viewports, and a `changelog.d/<ticket>.json` entry.

## The evidence

Whistler's index (`data/traces/whistler_1808_fort_dearborn.json`) names, besides what T-2062 built: 19 Interpreters House (west-south-west of the fort; "Distance to the Main Gate is fortyeight Perches"), 20 Armerers Shop, 21 Merchants Shop, 22 Bake House, 23 House in Factors Dept., 27 Wharf of said River, and 33 Covered Way to procure Water ("Omited in their places"; Quaife: "From the northeast corner of the stockade a covered way led to the river"). T-2062's `outside_the_stockade.not_built` left no. 19 out because its stated 48 perches carries it to within 4 m of the 1812 river's edge, and the numerals 20-23 and 27 were not read.

## What to build

Read the sheet for 20-23 and 27 at a 4x crop first; build each house whose numeral can be read, by T-2062's rule, and record any that cannot be found as unread rather than placing it by guess. Seat no. 19 by the rule and resolve the river conflict honestly (the drafter's distances disagree by 3.3x and 6.8x: say which governs and why). The covered way is INFERRED from Quaife's text, from the north-east corner to the river, and never traced. `tools/read_whistler_1808.py --check` stays green and holds every new point.

**Acceptance:** every one of 19-23, 27 and 33 either stands in the 1812 scene with its card or is recorded on the trace as not found, with the reason; desktop and 390x780 shots, no page errors.
