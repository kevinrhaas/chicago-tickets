---
id: T-2488
title: 1812: build Lee's Place (Hardscrabble), the farm cabin and field on the South Branch three to four miles from the fort, beyond the west edge of the 1812 ground
state: split
epic: SOUTH_TIME
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-10-13
closed: 2026-10-15
pr: null
claimed_by: run 10/15/2026, 1:06:00 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-15T06:11:21.082Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38689931010
claimed_at: 2026-10-15T06:06:00.739Z
decision: null
decision_answer: null
---

1812: build Lee's Place (Hardscrabble), the farm cabin and field on the South Branch three to four miles from the fort, beyond the west edge of the 1812 ground.

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

Lee's Place, later Hardscrabble: the farm Charles Lee worked from about 1804 on the South Branch, with a log cabin where his hired men lived, where Liberty White and a Canadian (Debou) were killed on 6 April 1812.
- Captain Heald's letter of 15 April 1812: "Messrs. Russell and Lee's cabin, in a field on the Portage branch of the Chicago river, about three miles from the garrison" (`moses_kirkland_history_of_chicago_v1` p. 43, lines 6880-6895).
- "Lee's place, later known as Hardscrabble, was on the northwestern side of the South branch, near its forks" (same, lines 6865-6870). Currey 1912 ch. II: a farmhouse "on the west bank of the South Branch of the Chicago river some four miles from the mouth of the river, built some time after Fort Dearborn had been established", with an illustration captioned "Hardscrabble".
- Hurlbut: John Crafts's trading house of 1817-1822 stood "about half a mile below Bridgeport, ('Hardscrabble' - the same premises, where in April 1812, two murders were committed by the Indians) on the north side of the river" (`hurlbut_chicago_antiquities`, pp. 28-36, text line 59). Hubbard lists "a log cabin near the present Bridgeport, called 'Hard-scrabble'" in 1818 (`hubbard_autobiography_1911`, bk_hub_066). Wau-Bun ch. XVIII: haystacks and cattle on the opposite bank, and the men's canoe.

**The site is off the 1812 ground.** The e1830_natural heightfield's west edge is local E -705 m, about 1.9 km west of the fort; the forks near Bridgeport are several kilometres further west and south. So the first part of this ticket is a ruling, written here before building: extend the 1812 ground along the South Branch to the site (a terrain spec change, to be split off as its own ticket if it is more than one run), or stand the farm on a detached patch of ground with its own anchor. Either way the farm's position is a stated reading of the three distances (three miles, four miles, half a mile below Bridgeport) and never a pin.

## Ruling (2026-10-15, the run that claimed this ticket): EXTEND the 1812 ground, and not on a detached patch

The farm stands on the 1812 ground carried down the South Branch to it, and not on a detached patch. There are three reasons, and each one can be checked:

1. **No detached patch exists to stand it on.** Outside the e1830_natural box (E -705..1700, N -3800..1120) the renderer's `heightfield.sample()` returns its 0 m fallback (`renderers/web/js/terrain.js`), and `buildings.js` `groundUnder()` seats a footprint on that value. Around E -1500, N -4300 the drawn apron is flat at 1.31 m, which is the box edge's height carried outward. So a cabin there would stand 1.3 m under the ground a visitor sees, and the walker's eye would be 0.37 m above it. `tools/measure_anchors.mjs --gate` also refuses any anchor outside the box. The only sampler that reads outside a box is 1904's `contextCoast`. A patch is therefore new renderer machinery either way, and it is no cheaper than carrying the ground out.
2. **Every account of the farm puts it on the river bank.** Heald has it "in a field on the Portage branch", Wau-Bun has haystacks and cattle on the opposite bank and the men's canoe, and Moses and Kirkland put it on the "northwestern side of the South branch, near its forks". A patch with no river beside it would draw a farm that no source describes.
3. **The river's course to the farm is already in the corpus.** Rees & Rucker 1849 is georeferenced (data/traces/gcp/rees_rucker_1849_gcps.json, RMS 25.0 m) and draws the South Branch from Cermak Road west to the forks at Bridgeport, where the canal meets it. So the channel can be traced from a source and does not have to be invented.

**The site** will be a stated reading of the four placings (Heald's three miles from the garrison, Currey's four miles from the mouth, Hurlbut's half a mile below Bridgeport on the north side, and Moses and Kirkland's northwestern bank near the forks), measured against that trace. It is never a pin. It is more than one run's work, so this ticket is split: (1) the trace and the site reading, (2) the ground carried to the site, (3) the farm built on it. Piece 2 chooses how the ground is carried, either the box extended or an apron sampler like 1904's.

Pictures:
  not yet in the library: Currey 1912 "Hardscrabble". Bring it in with attribution if reachable, otherwise ask Kevin for it; once it is in, the cabin is image-gated on it.

**Acceptance:** the cabin, its field fence and haystacks stand at the ruled site in the 1812 scene with a camera anchor there, a card citing the sources above and their disagreement over the distance, and liberties for everything not given; the image gate is added and passed once the Currey picture is in the library.
