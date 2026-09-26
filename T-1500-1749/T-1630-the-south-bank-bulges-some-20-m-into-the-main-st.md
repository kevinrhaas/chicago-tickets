---
id: T-1630
title: The south bank bulges some 20 m into the main stem from E +260 to the La Salle slough mouth: bring it level with the rest of the reach as Hathaway draws it, and run the outer plank walk straight along it
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
claimed_by: run 9/26/2026, 12:28:09 PM CT
blocked_on: null
needs_bake: true
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/36258994691
claimed_at: 2026-09-26T17:28:09.876Z
decision: pending
decision_answer: null
---

The south bank bulges some 20 m into the main stem from E +260 to the La Salle slough mouth: bring it level with the rest of the reach as Hathaway draws it, and run the outer plank walk straight along it.

**Owner report, 2026-09-26.** He flew the 1835 scene over the South Division river front and compared it against Wright 1834 (`wright_1834`, `wright_1834_nara_hup`) and Hathaway 1834 (`hathaway_1834`), with screenshots of both sheets over the Clark–State reach. His words: *"i think there is some river geometry that needs to be changed and a lot of it is not an issue but some of it may be an issue so we may want some of these tickets moved up."* Four tickets came from it: T-1628, T-1629, T-1630 and T-1631. They lead band 5A because the South Water Street river front (T-1200) is built on this bank. Its lots, landings and plank walk seat against the waterline, so the waterline is settled first.


## The owner's ruling

*"you i think have too strong of a bulge of the river coming out as it approaches the slough, i think it should be fairly even with the rest of the river, like the hathaway map, but recognizing and using the slough location from the wright map, i have marked it roughly with a red line., the outer plank walk should be able to run roughly straight to follow the river bank, not curve like that"*

His red line ran along the south bank from the west, level through the La Salle slough mouth and on east: one straight, even bank.

## What stands now, measured

The South Division bank (`river.geojson` "South Division shore", then `shoreline.geojson` "South shore" from E +314) sits at these northings, taking the northernmost vertex in each 20 m of easting:

| E | +220 | +260 | +300 | +380 | +440 | +480 | +520 | +600 | +660 | +720 |
|---|---|---|---|---|---|---|---|---|---|---|
| bank N | +24 | +35 | +43 | +44 | +40 | +28 | +23 | +20 | +16 | +18 |

So the bank swells about **15–20 m** into the channel over E +260..+450 and falls back at the slough mouth. That is the bulge the owner sees, and it is why the river-walk frontage (`data/frontage/river_walk_frontage.json`, T-0119) bends around it. `docs/RESEARCH/clark_reach_bulge_1834.md` fixed a worse loop of the same kind further east (the outline lettering of CHICAGO RIVER read as dry ground). Test first whether this swell is lettering or wash too.

## The work

1. **Read the reach on Hathaway 1834 and on the NA/HUP Wright sheet**, E +200..+520, and measure the drawn bank against the trace. If the swell is in neither sheet's ink, it is a tracing artefact. Re-trace or correct the run so the bank stays even with the reach either side, keeping Wright's La Salle re-entrant as the one break in it (the owner: "recognizing and using the slough location from the wright map").
2. If a sheet does draw a swell, record that reading in the research note as the one the owner's ruling set aside, and log the change in docs/LIBERTIES.md. Build to his line either way. He has ruled on it twice (below), so this is not an `ask`.
3. **Straighten the outer plank walk.** Re-derive `river_walk_frontage.json` against the corrected bank so it runs roughly straight along it, as the owner asked, with its crossing at the slough mouth.
4. Re-derive what fronts the bank (South Water corridor, wharves, landings, block faces) and bake (`needs_bake`). Say what moved.

**Acceptance:** between E +220 and E +720 the south bank departs from a straight fit through the reach by no more than the georeference's own tolerance, stated as a number, except at the La Salle mouth. The plank walk follows it without the bend. `check.sh` and the named smoke legs are green at both widths.

## Owner confirmation, 2026-09-26 (with a screenshot looking along South Water Street from the west, red line drawn)

*"ok yes and dont forget about adjusting this river width and removing the extra land in the river west of the slight around the bend, the walk should go straight and cross straght just like the water street road and follow the bank of the river just like east of the slough, of course the docks will move in south as you move that river bank aling south water south so it is even with the bank to the east"*

His red line runs straight along South Water Street's river side, from the west edge of his view to the La Salle slough mouth and on east, level with the bank east of the slough. Everything north of it on this reach is the extra land: the wooded strip, the three landing sheds standing out on it, and the rounded point where the plank walk curves south to the crossing.

So, settled:
- **The bank moves SOUTH to his line**, even with the bank east of the slough, from the bend in the west to the La Salle mouth. The river gets **wider** on this reach by exactly that amount. The water polygon, the waterline run, the heightfield bank, the water mask and collision all move together. The north bank does not move.
- **The extra land goes.** Remove the ground standing in the river west of the slough, round the bend, and whatever is planted on it (the shrub and tree belt on the point) with it. Re-derive the flora so nothing grows in water.
- **The outer plank walk runs straight** along the new bank and **crosses the slough straight**, parallel to the Water Street road's own crossing (`lasalle_slough_crossing`), not by curving round a point. East of the slough it already follows the bank, and west of it should read the same.
- **The docks move south with the bank.** Every landing, wharf and freight shed on this reach (`data/wharves/`, the river-front sheds) re-seats against the new waterline at the same relation to the bank the ones east of the slough keep. Say each one's move in metres.
- **Acceptance adds:** the bank from the western bend to the La Salle mouth stands on the owner's line, stated as the northing, within the georeference tolerance. No land and no planting stands north of it. The walk and the docks sit on it.

## Owner, third message, 2026-09-26: Wright is the guide, and do not overcorrect

*"yes that's the right bend, follow wright in general, bring it in appropriately per my request but dont go crazy on either way, im sure wright is right bit that bend and the river does not appear correct compared to it"*

This sets the order of evidence for the whole ticket:
- **The bend is the one near the forks**, where the south bank turns (E ≈ +160..+260, bank rising from N +1 to +35). The corrected run goes from that turn east to the La Salle mouth.
- **Wright 1834's drawn bank is the target, not the red line.** The owner's reading is that Wright is right and the model's river no longer matches it through the bend and the swell. So step 1 comes first and decides the answer: measure the committed run against Wright's inked bank (both scans, NA/HUP and BPL) from the bend to the La Salle mouth, and find where and why they part. The Clark-reach loop was lettering read as ground, so check the same failure here.
- **Re-trace to Wright's ink.** Where the committed bank stands north of it, bring it in to the ink. Where it already sits on the ink, leave it. The owner's red line shows the direction and rough size of the change (south, level with the bank east of the slough). It is not a coordinate to force onto the map: "dont go crazy on either way". A correction that goes past Wright's ink is as wrong as the swell.
- Hathaway corroborates. It does not override Wright.
- **Acceptance, amended:** from the bend to the La Salle mouth, the south bank sits on Wright's inked bank within the trace's own ink-distance tolerance (report median and p90 against the ink, as `shoreline.geojson` already does). The swell is gone. The walk, the crossing and the docks follow that bank as above.

## Decision needed

**Question:** The committed south bank IS Wright's inked bank (median 1.87 m, p90 3.96 m over 103 stations, measured on the NA/HUP scan under its own registration — PR #88). Wright himself draws the swell: the ground he puts between his bank and his block tier runs 34.9 / 39.0 / 31.7 / 19.8 m across blocks 20, 19, 18, 17, where Hathaway's runs 29.3 / 28.2 / 24.2 / 21.3 m with no maximum in it. So the bank cannot be brought in to your line without going PAST Wright's ink, which your third message forbids. Which governs on this reach?

- (a) Keep Wright. The waterline stays on the ink of the sheet the datum, the plat and the block grid are all fitted to. The swell stays; the walk keeps its bend and the docks do not move. T-1630 closes on the reading.
- (b) Follow Hathaway on this reach. Re-cut the bank to Hathaway's even taper from the bend to the La Salle mouth — about 6 to 11 m south, peaking at block 19 — keeping Wright's La Salle re-entrant. The bank's grade drops from a documented trace to reconstructed and goes in LIBERTIES; the walk straightens, the sheds and planting on the point come off, the docks re-seat south, and it needs a bake.
- (c) Split the difference: hold the bank but fix only what does not depend on it — straighten the plank walk and its crossing where the bank allows, and re-seat anything standing proud of the waterline.

**Recommendation:** (a) Keep Wright. The waterline stays on the ink of the sheet the datum, the plat and the block grid are all fitted to. The swell stays; the walk keeps its bend and the docks do not move. T-1630 closes on the reading. — The reconstruction's waterline is fitted to the same survey as its datum, its plat and all 41 of its blocks; departing from that sheet on one reach, on the eye rather than on evidence, buys 6-11 m of evenness for a documented line downgraded to an invention, on exactly the reach T-1200 is about to build its lots, landings and plank walk against. The 20 m read off the scene is about half Wright-vs-Hathaway and about half the block grid's own 8.58 m corridor-line offset, which T-0419 already refused to move.

**Asked:** 2026-09-26 by https://github.com/kevinrhaas/polecat-platform/actions/runs/36258994691. Answer on Manager's 4D Board, or set `decision: answered` and `decision_answer: <letter>` in this file.
