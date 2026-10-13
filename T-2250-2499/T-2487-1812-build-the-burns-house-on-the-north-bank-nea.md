---
id: T-2487
title: 1812: build the Burns house on the north bank near the foot of State Street and the Lee family's house on the lake shore near the fort
state: open
epic: SOUTH_TIME
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-10-13
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

1812: build the Burns house on the north bank near the foot of State Street and the Lee family's house on the lake shore near the fort.

## The owner's ask (2026-10-13, project thread "1812 structures")

> For 1812 did I ask you to build the other buildings from that era the kinzie former dusable estate, ouillmettes house, there are certainly other structures in 1812, the Lee house etc. all known structures from history

Until now the 1812 scene has drawn only the first Fort Dearborn and its outer buildings (the 14 `first_fort_dearborn_*` and 7 `first_fort_outer_*` records, from Whistler's 1808 draught: T-2049, T-2062). No settler's house stands. The inventory this ticket comes from is the thread's reply; the settlement the histories put across and around the fort in 1803-1812 is the Kinzie house (the former Point du Sable house) and its establishment, Ouilmette's and Pettell's houses behind it, the Burns house up the north bank, the Lee family's house on the lake shore, and Lee's Place (Hardscrabble) on the South Branch.

## How it is built (applies to every 1812 settlement ticket)

- **Dated so it resolves in 1812 and not in 1835.** Each record's `documented_range` covers the 1812 scene date (1 August 1812 until T-2490 moves it to 14 August, owner 2026-10-13: cover both) and closes before 1835-07-01. `data/exclusions.json` already rules `kinzie_house` and `ouilmette_cabin` gone by 1835: keep those entries, and have the new records' closing dates agree with them. `tools/read_whistler_1808.py --check` and the scene-date checks must stay green.
- **Never invent a source** (AGENTS.md rule 1). Every `source_id` resolves in `data/sources/`. Sources this ticket needs that are not yet records get one first, with tier and `rights_status`: J. Seymour Currey, *The Story of Old Fort Dearborn* (1912, Project Gutenberg 52346); Joseph Kirkland, *The Chicago Massacre of 1812* (1893, Gutenberg 59624, catalogued at `chicago/reference/chicago-massacre-1812.yaml`); Benson J. Lossing, *Pictorial Field-Book of the War of 1812* (1869). Where a source cannot be reached from the run's container, say so in the ticket rather than citing it from memory.
- **The image gate** (AGENTS.md rule 11, `data/reference_views/README.md`): every picture of the building is read off the picture itself, its camera solved into `data/reference_views/<structure_id>/`, rendered with `node tools/photo_match.mjs`, and worked until it matches. Pictures are tier 5: form only, never a coordinate. Most are retrospective (1857-1912) or show a later year (1820, 1832); each is evidence of its own date, and the match record says which picture governs where they disagree.
- **What no source gives is a numbered liberty** in `docs/LIBERTIES.md` and `data/liberties.json` (check dev and open PRs for the next free number before merging), carried on the attribute as `reconstructed`.
- **No human figure is drawn** (standing constraint). Cards that name Native or Métis people carry `review_required` and `touches_removal` with their own sentence. The 1812 scene is already held for that review (T-0472) and stays unreleased.
- Gate (`tools/check.sh`), smoke by parts, desktop and 390x780 shots with no page errors, and a `changelog.d/<ticket>.json` entry.

## What to build

- **The Burns house.** A log house on the north side of the river "some two or three hundred yards from the lake and twenty steps from the river bank", which Hurlbut judged to be the Burns house (`moses_kirkland_history_of_chicago_v1` p. 36, lines 5630-5636); "Burns's house stood near the spot where the Agency Building, or 'Cobweb Castle,' was afterwards erected, at the foot of N. State Street" (`kinzie_waubun_1856` ch. XVIII, footnote 30); "near what is now the southwest corner of North State (formerly Wolcott) and Water streets" (`moses_kirkland_history_of_chicago_v1` lines 9797-9800). On 7 April 1812 the alarm from Lee's Place was shouted across to it, and Ensign Ronan's party brought the family, the mother and her day-old baby, down to the fort by boat. Moses and Kirkland identify the occupant as Thomas Burns, a discharged soldier on the 1810 muster roll (lines 8548-8556); Currey 1912 calls him John Burns. Record the disagreement. The positions conflict too (Hurlbut's 200-300 yards from the lake versus the foot of State Street): the record takes one, says why, and makes the other a stated alternative.
- **The Lee family's house.** "The family of Mr. Lee had resided in a house on the Lake shore, not far from the fort. Mr. Lee was the owner of Lee's Place" (`kinzie_waubun_1856` ch. XIX); Currey 1912 ch. II puts it "near the fort on the bank of the river", near the later Madison Street and Michigan Avenue. Those two disagree (lake shore or river bank); rule on them against the 1812 shoreline (`data/terrain/epochs/e1830_natural/shoreline.geojson`), where the river ran south behind the spit. Charles Lee, his son and the household except his wife and daughter died on 15 August (Wau-Bun ch. XIX).

No picture of either house is known. Both are small log dwellings, built at the `log_dwelling` archetype with footprints, heights and positions as liberties.

**Acceptance:** both houses stand in the 1812 scene at their ruled positions, inside the 1812 ground, with cards citing these sources and stating where the sources disagree; no 1835 view shows them.
