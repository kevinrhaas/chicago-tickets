---
id: T-3360
title: 1835 buildings stand on plank walks and in alleys: move them back onto their lots, give St. Mary's an entrance off the walk
state: claimed
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-03
closed: null
pr: null
claimed_by: run 11/3/2026, 1:55:00 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-03T19:55:11.643Z
decision: null
decision_answer: null
---

1835 buildings stand on plank walks and in alleys: move them back onto their lots, give St. Mary's an entrance off the walk.

The owner, 2026-11-03, with a screenshot over State and Lake in 1835: "for buildings like this there are 2 here but i imagine there are others that are placed in the middle of the walkways or alleys, go ahead and if it makes sense either move the building in so the plank walks continue normally or dont block the alleyway and then there are entrances for st marys for example or if you are dead certain that the building was there and then they would have built the walk around it, do that and provide an entrance for st marys".

Swept on dev: 6 buildings stand on a street-edge walk line (st_marys_church, chappel_infant_school, tremont_house_1, bates_auction_room, exchange_coffee_house, first_presbyterian_church) and 17 stand inside a platted alley strip (bates_auction_room and 16 anonymous recon_1835_* roofs).

**Acceptance:**
- `tools/check_structure_clearance.py` gains question D: no 1835 building on a march-able walk line, none more than 0.05 m inside a platted alley; a RULED_ON_WAY ruling only where a source fixes the building's spot; self-test fires both.
- Every building it lists is moved back onto its lot (no source fixes any of them to a coordinate), its position note saying how far and why; the gate is green with no ruling.
- St. Mary's (and First Presbyterian, the town's other church) take a stoop at the door down to the Lake Street walk.
- Re-derived; check.sh green; smoke parts for the diff run; 390x780 checked.
