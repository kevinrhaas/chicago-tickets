---
id: T-2488
title: 1812: build Lee's Place (Hardscrabble), the farm cabin and field on the South Branch three to four miles from the fort, beyond the west edge of the 1812 ground
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

1812: build Lee's Place (Hardscrabble), the farm cabin and field on the South Branch three to four miles from the fort, beyond the west edge of the 1812 ground.

## The owner's ask (2026-10-13, project thread "1812 structures")

> For 1812 did I ask you to build the other buildings from that era the kinzie former dusable estate, ouillmettes house, there are certainly other structures in 1812, the Lee house etc. all known structures from history

Until now the 1812 scene has drawn only the first Fort Dearborn and its outer buildings (the 14 `first_fort_dearborn_*` and 7 `first_fort_outer_*` records, from Whistler's 1808 draught: T-2049, T-2062). No settler's house stands. The inventory this ticket comes from is the thread's reply; the settlement the histories put across and around the fort in 1803-1812 is the Kinzie house (the former Point du Sable house) and its establishment, Ouilmette's and Pettell's houses behind it, the Burns house up the north bank, the Lee family's house on the lake shore, and Lee's Place (Hardscrabble) on the South Branch.

## How it is built (applies to every 1812 settlement ticket)

- **Dated so it resolves in 1812 and not in 1835.** Each record's `documented_range` covers 1812-08-01 and closes before 1835-07-01. `data/exclusions.json` already rules `kinzie_house` and `ouilmette_cabin` gone by 1835: keep those entries, and have the new records' closing dates agree with them. `tools/read_whistler_1808.py --check` and the scene-date checks must stay green.
- **Never invent a source** (AGENTS.md rule 1). Every `source_id` resolves in `data/sources/`. Sources this ticket needs that are not yet records get one first, with tier and `rights_status`: J. Seymour Currey, *The Story of Old Fort Dearborn* (1912, Project Gutenberg 52346); Joseph Kirkland, *The Chicago Massacre of 1812* (1893, Gutenberg 59624, catalogued at `chicago/reference/chicago-massacre-1812.yaml`); Benson J. Lossing, *Pictorial Field-Book of the War of 1812* (1869). Where a source cannot be reached from the run's container, say so in the ticket rather than citing it from memory.
- **The image gate** (AGENTS.md rule 11, `data/reference_views/README.md`): every picture of the building is read off the picture itself, its camera solved into `data/reference_views/<structure_id>/`, rendered with `node tools/photo_match.mjs`, and worked until it matches. Pictures are tier 5: form only, never a coordinate. Most are retrospective (1857-1912) or show a later year (1820, 1832); each is evidence of its own date, and the match record says which picture governs where they disagree.
- **What no source gives is a numbered liberty** in `docs/LIBERTIES.md` and `data/liberties.json` (check dev and open PRs for the next free number before merging), carried on the attribute as `reconstructed`.
- **No human figure is drawn** (standing constraint). Cards that name Native or Métis people carry `review_required` and `touches_removal` with their own sentence. The 1812 scene is already held for that review (T-0472) and stays unreleased.
- Gate (`tools/check.sh`), smoke by parts, desktop and 390x780 shots with no page errors, and a `changelog.d/<ticket>.json` entry.

## What to build

Lee's Place, later Hardscrabble: the farm Charles Lee worked from about 1804 on the South Branch, with a log cabin where his hired men lived, where Liberty White and a Canadian (Debou) were killed on 6 April 1812.
- Captain Heald's letter of 15 April 1812: "Messrs. Russell and Lee's cabin, in a field on the Portage branch of the Chicago river, about three miles from the garrison" (`moses_kirkland_history_of_chicago_v1` p. 43, lines 6880-6895).
- "Lee's place, later known as Hardscrabble, was on the northwestern side of the South branch, near its forks" (same, lines 6865-6870). Currey 1912 ch. II: a farmhouse "on the west bank of the South Branch of the Chicago river some four miles from the mouth of the river, built some time after Fort Dearborn had been established", with an illustration captioned "Hardscrabble".
- Hurlbut: John Crafts's trading house of 1817-1822 stood "about half a mile below Bridgeport, ('Hardscrabble' - the same premises, where in April 1812, two murders were committed by the Indians) on the north side of the river" (`hurlbut_chicago_antiquities`, pp. 28-36, text line 59). Hubbard lists "a log cabin near the present Bridgeport, called 'Hard-scrabble'" in 1818 (`hubbard_autobiography_1911`, bk_hub_066). Wau-Bun ch. XVIII: haystacks and cattle on the opposite bank, and the men's canoe.

**The site is off the 1812 ground.** The e1830_natural heightfield's west edge is local E -705 m, about 1.9 km west of the fort; the forks near Bridgeport are several kilometres further west and south. So the first part of this ticket is a ruling, written here before building: extend the 1812 ground along the South Branch to the site (a terrain spec change, to be split off as its own ticket if it is more than one run), or stand the farm on a detached patch of ground with its own anchor. Either way the farm's position is a stated reading of the three distances (three miles, four miles, half a mile below Bridgeport) and never a pin.

Pictures:
  not yet in the library: Currey 1912 "Hardscrabble". Bring it in with attribution if reachable, otherwise ask Kevin for it; once it is in, the cabin is image-gated on it.

**Acceptance:** the cabin, its field fence and haystacks stand at the ruled site in the 1812 scene with a camera anchor there, a card citing the sources above and their disagreement over the distance, and liberties for everything not given; the image gate is added and passed once the Currey picture is in the library.
