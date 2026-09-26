---
id: T-1628
title: The La Salle slough runs inland to Randolph off Conley/Stelzer, and the owner rules it to Wright and Hathaway: in from the river just past South Water Street and into the lot, no deeper
state: claimed
epic: GROUND
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-09-26
closed: null
pr: null
claimed_by: run 9/26/2026, 12:50:57 PM CT
blocked_on: null
needs_bake: true
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/36260347130
claimed_at: 2026-09-26T17:50:57.277Z
decision: null
decision_answer: null
---

The La Salle slough runs inland to Randolph off Conley/Stelzer, and the owner rules it to Wright and Hathaway: in from the river just past South Water Street and into the lot, no deeper.

**Owner report, 2026-09-26.** He flew the 1835 scene over the South Division river front and compared it against Wright 1834 (`wright_1834`, `wright_1834_nara_hup`) and Hathaway 1834 (`hathaway_1834`), with screenshots of both sheets over the Clark–State reach. His words: *"i think there is some river geometry that needs to be changed and a lot of it is not an issue but some of it may be an issue so we may want some of these tickets moved up."* Four tickets came from it: T-1628, T-1629, T-1630 and T-1631. They lead band 5A because the South Water Street river front (T-1200) is built on this bank. Its lots, landings and plank walk seat against the waterline, so the waterline is settled first.


## The owner's ruling

*"when you look down on the river, there is a bulge and then a slough just east of lasalle that goes very deep, the slough goes all the way to lake. that is not how it is depicted in the wright or hathaway map. i think its ok to depict the slough like the wright map, so it seems it should come in, just a bit past south water and then into the lot, but not deeper"*

## What stands now

`terrain_spec.json` → `swales` carries two entries. `lasalle_slough_lower` runs from Wright's traced re-entrant (E +462..+469, re-confirmed at E +449.9 by T-0795) up the west half of the La Salle–Clark block, open water to about N -93. `lasalle_slough_upper` carries it on as a dry swale past Lake Street to a terminus **just north of Randolph**. Both inland courses are inferred from **Conley/Stelzer 1933** (`asset_use: orientation`, a 20th-century pictorial reconstruction). T-0795 walked the whole NA/HUP sheet and found that **Wright draws no inland course here**, only the mouth notch. Hathaway draws none either, on the owner's reading.

## The work

1. **Cut the slough back to Wright.** The mouth stays where it is: Wright's re-entrant and T-0129's continuous drain through the South Water corridor, with `lasalle_slough_crossing` over it. The channel ends a short way into block 50's lot south of South Water Street, the owner's "just a bit past south water and then into the lot". Pick the head in writing, as a lot-depth figure off the committed block face, with the feather to zero the other slough heads use, so the ground closes over it and no trench is left open.
2. **Remove `lasalle_slough_upper`** and the part of `lasalle_slough_lower` inland of the new head. Their liberties (docs/LIBERTIES.md, `data/liberties.json`) move to resolved, citing this ruling. Conley/Stelzer stays on record as the reading that was set aside, not deleted from the research note (`docs/RESEARCH/main_branch_sloughs_1833.md` gets a dated amendment).
3. **Re-derive what stood on the old course.** The inland reach threaded committed roofs (T-0118: `old_bank_building` cleared by 2.4 m), and the La Salle–Clark block's lots were cut around it. Re-run the lot and derived layers (`publish.sh`, then `rederive.mjs --run`) and say what moved: ground that is now dry may hold roofs the water refused.
4. **Bake and verify.** The heightfield, water mask, collision and minimap move together (`needs_bake`). Check the Lake Street and Randolph corridors read as level prairie from the street at both widths.

**Acceptance:** the La Salle slough is visible only from the river to a head inside block 50's lot south of South Water Street, stated in metres off the block face. No cut remains north of it. The crossing still spans water. `check.sh` is green and the smoke legs `smoke_budget --for-diff` names pass at 390×780 and 1280×800. The liberties ledger records the change.
