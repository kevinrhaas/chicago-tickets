---
id: T-1684
title: The W2-W4 mechanics' shops have no State or Dearborn face to take: no platted-block slot in the whole recipe is dealt onto a cross-street face, and every Lake-Randolph block reads at_capacity
state: open
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-27
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

The W2-W4 mechanics' shops have no State or Dearborn face to take: no platted-block slot in the whole recipe is dealt onto a cross-street face, and every Lake-Randolph block reads at_capacity.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

**Measured on the committed tree, 2026-09-27, in the course of T-1682.** T-1201's ask
included "the mechanics' shops on State and Dearborn" and T-1682 carried "the W2-W4 shops
take their State and Dearborn faces". Neither can be spent as written, and the reason is
the instrument rather than the evidence:

- `data/reconstruction/1835_platted_block_parcels.json` deals 22 block entries and the
  whole `fronts` vocabulary they use is `lake`, `randolph`, `south_water`, `washington` —
  the four LONG faces. Not one slot in the programme's history has ever been dealt onto a
  cross-street face, and the recipe's own `placement_rule` describes a principal roof
  "standing back from its own street frontage, its facade to the street", which on this lot
  grid is the long face. So a W2-W4 shop on State or Dearborn needs a corner-lot / short-face
  term the recipe does not have.
- The blocks concerned have no room either. `blk_lake_dearborn` (13 standing of 31),
  `blk_lake_clark` (16) and `blk_south_water_dearborn` all read `at_capacity` or deal no W
  head: `blk_south_water_dearborn`'s 4 of headroom is dealt `A3, D6, D7, H1`.
- The only W-family roof this town holds anywhere is `recon_1835_north_w5_040`, in the North
  Division, so there is no standing shop on either face to re-family into one.

So this is a placement-rule question and not a re-family: either the recipe learns a
short-face term (and `check_non_dwelling_slot`'s better-face clause learns what it means for
a cross street), or the shops go somewhere the grid already admits and this ask is withdrawn
in writing. Both are more than a field edit, which is why T-1682 did not invent one.

**Links:** T-1682 · T-1201 · T-0024 · `tools/generate_block_infill.py`
`check_non_dwelling_slot` · `data/reconstruction/1835_platted_block_parcels.json`.
