---
id: T-2485
title: 1812: build the Kinzie establishment behind the house: dairy, bake-house, the Frenchmen's lodging house, stables, garden, and whatever of du Sable's 1800 bill of sale still stood
state: claimed
epic: SOUTH_TIME
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-10-13
closed: null
pr: null
claimed_by: run 10/21/2026, 11:03:23 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-22T04:03:24.834Z
decision: null
decision_answer: null
---

1812: build the Kinzie establishment behind the house: dairy, bake-house, the Frenchmen's lodging house, stables, garden, and whatever of du Sable's 1800 bill of sale still stood.

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

The working establishment around the Kinzie house in 1812, each building its own record, sited from the pictures and the descriptions (positions reconstructed):
- Wau-Bun, ch. XVII: "A fine, well-cultivated garden extended to the north of the dwelling, and surrounding it were various buildings appertaining to the establishment—dairy, bake-house, lodging-house for the Frenchmen, and stables" (`kinzie_waubun_1856`; describes 1831, so standing in 1812 is inferred and the note says so).
- Du Sable's 1800 bill of sale (Quaife 1928, see T-2484) lists, besides the house, two barns, a horse mill, a bakehouse, a poultry house, a dairy and a smokehouse, with livestock. Read the bill itself for each building's dimensions; do not take them from a summary. Which of them still stood twelve years and two owners later is a ruling the ticket writes down, building by building.
- Wau-Bun ch. XVIII-XIX: two old pirogues moored near the house, the family's escape across the river in April 1812 (boats are optional props here, not structures).

The 1820 views show outbuildings, a picket line and horses on the farmstead; the 1832 and 1833 views show a second building behind the house. Use them for the massing they show.

Pictures:
  picture: `chicago/reference/images/chicago/chicago_settlement_1820_2.jpg`
  picture: `chicago/reference/images/chicago/chicago_settlement_view_1820.jpg`
  picture: `chicago/reference/images/chicago/chicago_kinzie_mansion_1832_and_1845_view.jpg`
  picture: `chicago/reference/images/chicago/chicago_kinzie_house_1804.jpg`

Same site as T-2484: it waits for that PR (one PR at a time on the same house, owner 2026-10-10). Any building none of the pictures shows carries no image gate and is a liberty.

**Acceptance:** each building the ticket rules in stands in 1812 with its card; each one a picture shows matches it (match records at `matches`); the rulings on the bill of sale's buildings are written in the records' notes.

Before `done`, the builder adds an `## Image gate` section here naming every outbuilding a picture shows.

## Found at T-2504 (2026-10-15)

A building with the numeral '32' (the horse mill, index no. 32, `not_located`) is drawn between the easternmost no. 31 house and Kinzie's kitchen garden, at about sheet px [1177, 427, 1215, 455], its '32' under it near (1190, 460). The register's `north_bank` rule (anchored on kinzie_house_1812) can seat it.

## Image gate

- `kinzie_stable_1812` — Eastman 1820 (`eastman_1820`): matches. Sarony, Cram and Teich draw a whitewashed gabled building end-on at the same place about 1831; no one heading draws both it and Eastman's log stable, so those three fix only the stable's place and carry no camera for it. Eastman, drawn on the spot in 1820, governs the form.
- `kinzie_lodging_house_1812` — Eastman 1820 (`eastman_1820`): differs, 1 open item. Eastman draws the far roof end as a hipped end; `log_dwelling` builds no hip on a log building (it refuses one as an invention), so a gable stands, its apex 9 px right of the drawn ridge end. Needs a decision: is this one 1820 plate enough for a hipped log house, or a different archetype?
- `kinzie_bake_house_1812` — Sarony (`sarony_1912`), Cram (`cram_1893`), Teich (`teich_postcard`): all three match. Its narrow, low oven flue needed two new optional `log_dwelling` attributes, `ridge_stack_w_m` and `ridge_stack_head_m`. Every other log asset rebuilds byte-identical.
- No camera: Gemmell's 1820 plate (`chicago_settlement_view_1820.jpg`) is too blurred to make out any outbuilding. No picture sees the dairy (it is behind the house and its cottonwoods), the horse mill (gone before the 1830s pictures, and Eastman's view does not reach it) or the garden fence. All three are reconstructed liberties (L420).

## Sources at T-2485

- **Read:** Wau-Bun ch. XVII and VI (local epub), Currey 1912, Kirkland 1893, the five pictures through the house's solved cameras, and Whistler's index no. 32 through Quaife 1913 note 413.
- **Not reachable:** Quaife 1928, "Property of Jean Baptiste Point Sable" (MVHR 15:1), which prints du Sable's 1800 bill of sale. JSTOR sits behind a script wall, and HathiTrust and archive.org are both blocked from the run's container. So the bill was **not read**: no record cites it, and none of its dimensions are used. Its building list is T-2484's report of it.
- **Not re-read:** the Whistler sheet image, because the Gutenberg image host is blocked. The horse mill is seated on T-2504's box for no. 32 (above), and its record says so.
- **Rulings** (records and `docs/RESEARCH/1812_other_structures.md`):
  - Stand: the horse mill, the bakehouse, the dairy, and one barn (as the stable).
  - Not built for 1812: the second barn, the poultry house and the smokehouse (`data/exclusions.json`).
