---
id: T-2486
title: 1812: build Antoine Ouilmette's house and garden close behind the Kinzie house, and Pettell's small cabin near it
state: blocked-tech
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
blocked_on: T-2485 — same site, one PR at a time (owner, 2026-10-10): Ouilmette's and Pettell's houses stand behind the Kinzie establishment
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: null
decision: null
decision_answer: null
---

1812: build Antoine Ouilmette's house and garden close behind the Kinzie house, and Pettell's small cabin near it.

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

- **Antoine Ouilmette's house and garden**, "situated close in the rear of the Kinzie house" (Currey 1912 ch. II); "the house of Ouilmette, a Frenchman with a half-breed wife, who formed a part of the establishment of Mr. Kinzie and whose dwelling was close at hand", with a garden of currant bushes and "a small back window" (`kinzie_waubun_1856` ch. XIX, the narrative of 15-16 August 1812). Victoire (Mirandeau) Porthier says her family stayed in "the Ouilmette house across the river from the fort" before it burned (`moses_kirkland_history_of_chicago_v1` lines 6776-6779). Ouilmette had been at Chicago since 1790 by his own account, and Hubbard still lists "a cabin on the north side occupied by Antoine Ouilmette" in 1818 (`hubbard_autobiography_1911`, the inventory at bk_hub_066). The 1835 exclusion `ouilmette_cabin` stays: this record closes in the later 1820s.
- **Pettell's cabin**: "A man named Pettell also had a small cabin near the Kinzie house" (Currey 1912 ch. II); Mrs. William Whistler counted "four rude huts or traders' cabins" in 1803, "among them Le Mai, Ouillemette and Pettell" (`moses_kirkland_history_of_chicago_v1` p. 35, lines 5578-5584). Whether Pettell's cabin still stood in 1812 is inferred: Moses and Kirkland think Pettell was among the twelve militia killed on 15 August (line 7027). Write the ruling in the note.

No picture is known to show either house by name. The 1820 Eastman view shows small buildings beside the Kinzie farmstead; read it for whether either is there, and if one is, gate it.

The Ouilmette household was Métis; its card carries `review_required` and `touches_removal` with its sentence (AGENTS.md standing constraint). Waits for T-2485 (same site, one PR at a time).

**Acceptance:** both stand behind and beside the Kinzie house in 1812 with cards citing the sources above; footprints, heights and positions not given by any source are liberties; any picture that shows either one is matched.
