---
id: T-1679
title: Haddock's Tavern may stand one lot east of its seat: five printings of G. Spring's notice put it one lot west of plat lot 7 of block 16, and mansion_house's own position declares a lot's width of slack
state: review
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-27
closed: null
pr: 396
claimed_by: run 10/4/2026, 2:21:06 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37185337889
claimed_at: 2026-10-04T07:21:06.777Z
decision: null
decision_answer: null
---

Haddock's Tavern may stand one lot east of its seat: five printings of G. Spring's notice put it one lot west of plat lot 7 of block 16, and mansion_house's own position declares a lot's width of slack.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)


**Where the evidence already is.** T-1624 did the plat work and wrote it up in
`chicago/4d/docs/RESEARCH/plat_level_building_placements_1833_34.md` § "The one placement question
this pass opens, and does not take". In short:

- Block 16 is `blk_south_water_dearborn` (Dearborn to State, South Water to Lake) on
  `data/traces/thompson_block_numbering.json`; its `lot_numbering` scheme runs 5 6 7 8 across the
  south row west to east, so plat lot 7 is `blk_south_water_dearborn#05`, face south, fronting Lake.
- `mansion_house` — which carries "Haddock's Tavern" and "Haddock's Mansion House" among its names —
  stands on `blk_south_water_dearborn#01`, plat **lot 5**, the south row's west end at Dearborn.
- G. Spring's For-Sale notice sells lot 7 "one lot east of Haddock's Tavern", which puts the tavern
  on lot **6**. Five legible settings: 1834-06-18 c006, 1834-07-02 c053 (tavern name cut),
  1834-07-09 c024 ("Maddock's"), 1834-09-03 c005, 1834-10-15 c006.
- The structure record invites exactly this: "THE POSITION ALONG THE BLOCK IS THIS RECORD'S CHOICE",
  with a declared working uncertainty of "AT LEAST A LOT'S WIDTH ALONG LAKE STREET" because "'near
  Dearborn' is not 'at the corner'". It was placed 2026-08-11, months before any block or lot
  numeral was read onto this grid, so the notice is evidence the record has never seen.
- The tavern's spelling is already settled as Haddock's in the record's own research note, and the
  Graves → Haddock succession is bracketed there, so the 1834 notices are about this building.

**What makes this its own ticket rather than a line in T-1624.** It is a structure MOVE: a new
coordinate for a placed record, a re-derived lot assignment, a bake, and the frame budget measured
after it. T-1624 was a register pass and refused on principle to move anything.

**Two things the run that takes this has to decide, not assume.** Whether "one lot east" is a
measurement or a loose phrase for "next door" — the notice is a for-sale advertisement, not a
survey. And whether an 1834 notice may refine the POSITION of a building the town already stands on
other evidence, given that the ladder ratified 2026-09-03 forbids it ASSERTING an 1835 fact:
existence and position are not the same claim, and that distinction is the argument this ticket
turns on. If it goes the other way, the refusal is the finding and this ticket closes on it.

**Links:** T-1624 · T-0358 · T-0788 · T-0324 · `data/structures/mansion_house.json` ·
`data/traces/thompson_block_numbering.json` · `data/reconstruction/1835_lot_ledger.json`.
