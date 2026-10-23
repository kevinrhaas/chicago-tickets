---
id: T-3078
title: Buildings overlap each other and fences end inside them (1835 Lake and Canal) — separate them and gate it in every year
state: review
epic: META
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-10-23
closed: null
pr: 1250
claimed_by: run 10/23/2026, 2:34:19 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-23T19:34:20.604Z
decision: null
decision_answer: null
---

The owner, 2026-10-23, with a screenshot from 35 ft over Lake and Canal in 1835 (dev): *"Not right make sure this does not happen again."* Two shops stood inside each other on the south-east corner — Goss & Cobb's saddlery and Pierce's blacksmith shop, each record taking that corner independently — with the Lake Street rail fence running into them.

Sweep of 1812, 1835 and 1904 found, in 1835 only: three pairs of buildings inside each other (that corner; the Exchange Coffee House and the New York House at Lake and Wells; a north-bank shed built through the agency striker's cabin), fences and dooryard pickets through four houses turned to 90 degrees, and woodpiles and one outbuilding inside rear ells. Root cause of the fences: tools/generate_dooryard_pickets.py `footprint_world` turned footprints counter-clockwise, the opposite of the renderer, and three other generators import it.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
- The Lake and Canal corner shows two separate shops, and no fence runs into either.
- No building stands inside another, and no fence, walk or yard prop stands inside a building, in any scene — checked by a gate in tools/check.sh that fails on a new case, with a self-test that proves it fires.
- Before/after screenshots at the owner's view, desktop and phone.
