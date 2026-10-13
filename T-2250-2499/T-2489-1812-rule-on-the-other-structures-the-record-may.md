---
id: T-2489
title: 1812: rule on the other structures the record may place at Chicago before the evacuation (Guarie's North Branch trading house, Cobweb Castle's build date, Lalime's and Russell's dwellings) and file a build for each one ruled in
state: open
epic: SOUTH_TIME
requested_by: owner
seen: true
effort: S
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

1812: rule on the other structures the record may place at Chicago before the evacuation (Guarie's North Branch trading house, Cobweb Castle's build date, Lalime's and Russell's dwellings) and file a build for each one ruled in.

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

## What to rule on

Each of these is named somewhere in the record as being at Chicago before 15 August 1812, on weaker evidence than the houses T-2484..T-2488 build. For each, read the sources, write a ruling (in, out, or held) with its source ids, and either file a build ticket directly under this one (same band, `--after`) or add a researched-and-excluded entry to `data/exclusions.json` the way `john_dean_house` is written.

- **Guarie's trading house on the North Branch.** Currey 1912 ch. II: "Over on the North Branch another trader named Guarie had a trading house which had been there from a time previous to the year 1778", on the west bank about where Fulton Street ends. Hubbard, in 1818, saw only Guarie's old corn hills (`moses_kirkland_history_of_chicago_v1` footnote, line 5109) and does not list a house (`hubbard_autobiography_1911`, bk_hub_066). Likely out for 1812: rule on it.
- **Cobweb Castle's build date.** In the 1835 data it is `cobweb_castle.log_1820` and on the watch list. Kirkland 1893 quotes Mrs. Callis: "the house in which my father lived, was built before the massacre of 1812", and says the name came after 1816. If the house was standing in 1812, it belongs in this scene too (and Burns's house stood near it). Rule on the claim against the agency's own dates.
- **Lalime's dwelling.** Jean Lalime, the post's interpreter, was killed by John Kinzie outside the fort gate in spring 1812 (`moses_kirkland_history_of_chicago_v1` pp. 41-42, lines 6595-6800). Where he lived is not stated in what has been read; find out or record that no source says.
- **Russell.** Heald's letter names "Messrs. Russell and Lee's cabin" (T-2488). Did Russell keep a separate house at the fort?
- **The first fort's own riverside works** that Whistler's draught does not draw (a landing, root cellars, the garrison's fields): the Wau-Bun description of root-houses and company gardens is of the second fort in 1831 (ch. XVII), so it does not count for 1812. Say so.
- Anything else the corpus places at Chicago in 1803-1812 (Andreas 1884 v1 pp. 70-110, Quaife 1913 chs. VI-X, Currey 1912 chs. I-III, Kirkland 1893): list each, with what was found.

Not ruled on here: Potawatomi lodges. The owner ruled on 2026-10-13 that they are built as documented; that is T-2490.

**Acceptance:** one ruling per candidate in the ticket and in the data (a build ticket filed, or an exclusion entry with its sources); nothing ruled in on a source that was not read.
