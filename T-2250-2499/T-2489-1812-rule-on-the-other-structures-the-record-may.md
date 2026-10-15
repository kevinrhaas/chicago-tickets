---
id: T-2489
title: 1812: rule on the other structures the record may place at Chicago before the evacuation (Guarie's North Branch trading house, Cobweb Castle's build date, Lalime's and Russell's dwellings) and file a build for each one ruled in
state: done
epic: SOUTH_TIME
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: null
opened: 2026-10-13
closed: 2026-10-15
pr: 808
claimed_by: run 10/15/2026, 1:05:27 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-15T08:17:08Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38689941138
claimed_at: 2026-10-15T06:05:27.525Z
decision: null
decision_answer: null
---

1812: rule on the other structures the record may place at Chicago before the evacuation (Guarie's North Branch trading house, Cobweb Castle's build date, Lalime's and Russell's dwellings) and file a build for each one ruled in.

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

## Rulings (2026-10-15)

Full reading: `docs/RESEARCH/1812_other_structures.md`. Sources read: Andreas 1884 v1 (archive.org full text, scan pp. 89-92), Quaife 1913 (Gutenberg), Moses and Kirkland v1 (committed text), Hubbard 1911, Wau-Bun (Gutenberg epub), Currey 1912 (Gutenberg 52346, now `currey_1912_old_fort_dearborn` — T-2484/T-2487: reuse this id), Kirkland 1893 (Gutenberg 59624, read but not cited; no source record). Lossing 1869 was not reached.

- **Guarie's trading house — OUT.** `data/exclusions.json` `guarie_trading_house` (scenes: 1812). Hubbard's tradition only ("prior to 1778"; "the first trader that followed La Salle"); corn-hills by 1818; Quaife p. 138 calls the tradition the whole of what is known. Currey's uncited "permanent residents" of 1804 is weighed and not followed.
- **Cobweb Castle — OUT for 1812.** `cobweb_castle_1812` (scenes: 1812, earliest 1835). Begun under Jouett 1816-18, finished by Wolcott 1820 (Andreas p. 90; Moses and Kirkland pp. 70-71). Mrs. Callis's pre-1812 house (Andreas p. 89: two rooms, twenty steps from the bank) is the Burns house Jouett occupied in 1817 (Moses and Kirkland p. 70; Wau-Bun fn. 30) — T-2487's.
- **Lalime's dwelling — IN.** One of the three no. 31 houses west of Kinzie's on Whistler's draught; Cooper names La Lime among their occupants in 1808 (Quaife pp. 148-50, 166). Filed: **T-2504** (with Le Mai's).
- **Russell — no separate house.** "Messrs. Russell and Lee's cabin" is one cabin; Quaife pp. 212-13: "aside from this fact nothing is known about him". Carried by T-2488.
- **The first fort's riverside works.** Wau-Bun's root-houses and gardens are the second fort's (1831) and do not count. Whistler's own wharf (27) and covered way (33) go into **T-2505** with the unbuilt outer houses 19-23; the 8-9 acre company garden and public cornfield by the forks into **T-2506**.
- **Anything else.** Le Mai's 1808 house → T-2504. Clark's house at the forks (Cooper), Whistler's two forks houses and Coursoll's house and field → **T-2506**. Bridges' house (occupied 1816) → held, weighed in T-2504. The horse mill → T-2485. The 1812 agency house already stands (`first_fort_outer_agents_house`).

The 1812 scene now lists the `exclusions` layer; entries carry `scenes` (tools/exclusion_scope.py), and an entry without it is the 1835 town's.
