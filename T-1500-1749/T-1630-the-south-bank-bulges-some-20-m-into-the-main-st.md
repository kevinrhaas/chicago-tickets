---
id: T-1630
title: The south bank bulges some 20 m into the main stem from E +260 to the La Salle slough mouth: bring it level with the rest of the reach as Hathaway draws it, and run the outer plank walk straight along it
state: open
epic: GROUND
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-09-26
closed: null
pr: null
claimed_by: null
blocked_on: null
needs_bake: true
closed_at: null
claimed_run: null
claimed_at: null
decision: null
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
2. If a sheet does draw a swell, record the reading and ask the owner (`ticket.mjs ask`) before building against his line.
3. **Straighten the outer plank walk.** Re-derive `river_walk_frontage.json` against the corrected bank so it runs roughly straight along it, as the owner asked, with its crossing at the slough mouth.
4. Re-derive what fronts the bank (South Water corridor, wharves, landings, block faces) and bake (`needs_bake`). Say what moved.

**Acceptance:** between E +220 and E +720 the south bank departs from a straight fit through the reach by no more than the georeference's own tolerance, stated as a number, except at the La Salle mouth. The plank walk follows it without the bend. `check.sh` and the named smoke legs are green at both widths.
