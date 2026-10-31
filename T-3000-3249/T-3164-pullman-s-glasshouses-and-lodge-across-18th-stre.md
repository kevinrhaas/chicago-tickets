---
id: T-3164
title: Pullman's glasshouses and lodge across 18th Street: the north-south and east-west GREEN HO. ranges traced off Sanborn sheet 28 and stood from the K13 kit's span form, the east range's rounded end, and the two-storey brick lodge at their angle
state: open
epic: SOUTH_TIME
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: T-1934
opened: 2026-10-25
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

Pullman's glasshouses and lodge across 18th Street: the north-south and east-west GREEN HO. ranges traced off Sanborn sheet 28 and stood from the K13 kit's span form, the east range's rounded end, and the two-storey brick lodge at their angle.

Piece 1 of 2 of **T-1934 — Refine Pullman stable, additions and conservatory estate**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-1934 was split (2026-10-26T00:45:37.590Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 1m ago, run 10/25/2026, 7:45:30 PM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/40249667168) — held by the run that split it

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/40249667168) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)
1. The 1911 sheet's two "GREEN HO." ranges and the "D" between them, on the 1800 Calumet ground across 18th Street (`s28-pullman-greenhouse-north`, `s28-pullman-greenhouse-east`, `s28-pullman-garden-lodge` in the sheet-28 census), are traced through the sheet's fitted transform by `tools/trace_prairie_1904_footprints.py` like every other Prairie footprint, and each traced outline carries the census's tier.
2. The two ranges stand in the 1904 scene as glasshouses from the K13 kit (glazed roofs, low opaque base walls), the east range's rounded east end kept; the lodge stands as a two-storey brick service building. A visitor walking 18th Street east of Prairie sees the estate's glasshouse ground where there was empty grass.
3. Provenance per attribute (outline inferred from the 1911 sheet; glazing form and heights reconstructed, bounded by the K13 kit and the census), a `docs/LIBERTIES.md` entry, the draft liberty `L-draft-prairie-16-18-east-2335` updated for what this supersedes, the structures baked, and the result checked in the browser at 1280x800 and 390x780.

Matching the glasshouses to the 1894 plates and the photographs is T-3165's, not this piece's.

## Reopened (owner, 2026-10-28)

Owner, 2026-10-28: *"in looking at 1729 prairie, the pullman estate it seems like tickets are closed and the gate is exited, but it is still way off from a photographic match, the stepped front, the south face, the entire greenhouses and the stable are all way off, not to mention the greenhouse area south of 18th, am i wrong? did you consider it done? because its not and you need to reenter the photographic match on that one if not"*.

This ticket closed without passing its image gate: `ticket.mjs split` closed it without asking the gate, and the pieces it minted carried no `## Image gate` section, so none of their `done`s asked it either (fixed by T-3235: a split parent's gate is now asked by its last piece). On 2026-10-28 its match records read:

- `pullman_glasshouse_1800_calumet_pavilion`: inland_1894_conservatory differs, lowe_c1897_conservatory differs
- `pullman_lodge_1800_calumet`: no reference view solved

The owner names the greenhouse ground south of 18th Street. Against Lowe's c. 1897 photograph and the 1894 Inland conservatory plate, the long range renders as a blank wall with square holes, the lodge in red brick, and the pavilion's great arched glass front as an opaque gable over a black opening, where the pictures show a glazed range with arched lights on a rusticated stone base, a stone lodge, and a glass front on a stone podium with its arched doorway. The north and east ranges are judged inside the pavilion's group views (their `rendered_members`); the lodge needs a view of its own.

Owner, 2026-10-28, the same thread: *"the surrounding wall/fence around the property also should be included in the match, as well as the flora"*. So each view also judges the lot's boundary (the coping walls, piers, posts and balustrades on Prairie Avenue, 18th Street and Calumet Avenue, and the garden wall round the glasshouse ground) and its planting (the ivy on the walls, the shrubs and beds, the yard and parkway trees as far as the picture shows them in its season), and a difference in either is `open` by the same bar.

It is reopened in place, not refiled. Read every picture itself, solve a camera for each one not yet solved, and work every view to `matches` under the T-3153 bar: an element missing or the wrong shape, a wrong count, a wrong material or colour, or a gap over about 0.3 m is `open`, never `within tolerance`. If it must be split again, its gate stays on it and the last piece closes it.

## Image gate (owner, 2026-10-28)

`ticket.mjs done` refuses this ticket until every building below matches every one of its reference views.

- pullman_glasshouse_1800_calumet_pavilion
- pullman_lodge_1800_calumet

**Released 2026-10-29** (claim of run 10/29/2026, 12:56:31 AM CT): no reason given

**Released 2026-10-29** (claim of run 10/29/2026, 3:08:23 AM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/40838159535): piece shipped as PR #1434 (resume: gate still running when the run's merge laps ended): the conservatory's arch smoothed and the transept cresting/finials built; the image gate stays open on the range's coping cresting, the transept lights' tracery, the podium, the dome offset, the lodge and the grounds, so the ticket cannot close yet

**Released 2026-10-29** (claim of run 10/29/2026, 5:26:10 AM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/40856813803): piece shipped as PR #1439 (resume: CI gate still running when the run's two merge laps ended): the transept arms' lights drawn round-headed over a transom as both pictures show them, and the 'range coping cresting' difference re-read off the pictures as plain coping (the lattice was the lodge deck's balustrade). The image gate stays open on the podium's rustication and panels, the dome's 0.6 m offset, the lodge (east face over the range, bowed corner, balcony, columns, second roof) and the gate piers and planting, so the ticket cannot close yet

**PR #1439 merged 2026-10-29** (squash 0ea85bcc, lapped by slice 1/5: dev merged in, manifest resolved by merge_asset_registry.py, source-use report rebuilt, gate green). The transept lights are on dev; the image gate above is still open on the podium, the dome offset, the lodge, and the gate piers and planting.

**Released 2026-10-29** (claim of run 10/29/2026, 8:03:33 AM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/40876689246): piece shipped as PR #1442 (resume: CI gate still running when the run's two merge laps on the merged head ended): the dome and drum stood at u 4.5, 1.8 m north of the transept's middle, where both pictures put them, at the re-read heights, with the turned finial both pictures show. The image gate stays open on the podium's rustication and panels, the lodge (east face over the range, bowed corner, balcony, columns, second roof) and the gate piers and planting, so the ticket cannot close yet

**Released 2026-10-29** (claim of run 10/29/2026, 10:18:56 AM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/40899306091): this piece (the lodge's bowed corner, balcony, round columns and deck spires) is complete in PR #1446, awaiting its CI gate under resume; the image gate keeps T-3164 open for the lodge's lower west roof, its east face and the gate piers and planting

**Released 2026-10-29** (claim of run 10/29/2026, 12:58:06 PM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/40924940614): piece shipped as PR #1452 (resume: CI gate still running when the run's two merge laps ended): the lodge's front in two parts, the west part under its own lower hipped roof and the loggia block set 2 m behind it. The image gate stays open on the lodge's east face, a pointed form over the new roof, the podium's rustication, and the gate piers and planting, so the ticket cannot close yet

**Released 2026-10-29** (claim of run 10/29/2026, 2:37:10 PM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/40940979678): piece shipped as PR #1457 (resume: CI gate still running when the run's two merge laps ended): the estate's 18th Street gate, two stone piers with scroll wings, placed through the plate's camera. The image gate stays open on the gate's carving, the walks and planting, the lodge's east face, the pointed form over its west roof and the podium's rustication, so the ticket cannot close yet

**Released 2026-10-29** (claim of run 10/29/2026, 4:47:22 PM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/40957064250): PR #1457 merged 2026-10-29 (squash 191c10da; finished by slice 5/5: CI gate green on 486bb41, mobile smoke parts 1 and 3 PASS 95/95 and 107/107 with zero page errors): the estate's 18th Street gate, two stone piers with scroll wings, is on dev. The image gate stays open on the gate's carving, the walks and planting, the lodge's east face, the pointed form over its west roof and the podium's rustication, so the ticket cannot close yet

**Released 2026-10-29** (claim of run 10/29/2026, 5:54:04 PM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/40968796590): piece shipped as PR #1462 (resume: CI gate still running when the run's two merge laps ended): the gate's carving built off both pictures — each wing's street-face C-scroll, its trailing leafage and the base fillet, and the sunk panel in each pier's shaft. The image gate stays open on the walks and planting, the lodge's east face, the pointed form over its west roof and the podium's rustication, so the ticket cannot close yet

**Released 2026-10-29** (claim of run 10/29/2026, 9:51:24 PM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/40992851944): piece shipped as PR #1472: the conservatory's podium dressed (cap and base courses, corner piers, banded rustication in a darker field) and the lodge's spirelet on its west roof, both off the plate and Lowe's print. The image gate stays open on the lodge's east face (the sheet's 11.6 m depth against both pictures, unresolved), the range's pilasters and the colonnade's columns, and the walks and planting, so the ticket cannot close yet

**Released 2026-10-30** (claim of run 10/30/2026, 12:32:16 AM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/41008373600): piece shipped as PR #1477 (resume: CI gate still running when the run's two merge laps ended): the east-end colonnade re-proportioned off both pictures (podium 1.6 m, entablature from 4.65 m, carrying on the range's string courses), and 'pilasters and columns heavier than built' re-read at the plate's scale as within tolerance. The image gate stays open on the lodge's east face and the walks and planting, so the ticket cannot close yet

**Released 2026-10-30** (claim of run 10/30/2026, 3:25:09 AM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/41025813349): piece shipped as PR #1481 (resume: CI gate still running when the run's two merge laps ended): the conservatory garden's planting read through the plate's and Lowe's cameras — two boxed standards with their masses, and the tall shrubs along the drive — drawn into all four views. The image gate stays open on the lodge's east face, the drive and walks, and the parkway trees (the plate's and Lowe's tree left of the gate, missing at e 1479.6, n -3212.0; Taylor's #p00 about 1 m east of their reading), so the ticket cannot close yet

**Released 2026-10-30** (claim of run 10/30/2026, 10:11:23 AM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/41077302883): piece shipped as PR #1492 (resume: CI gate still running when the run's two merge laps ended): the gate's two parkway trees placed and sized off the 1894 conservatory plate and Lowe's print (the tree left of the gate planted on Calumet's parkway; the corner tree moved 1.7 m west, off the west pier; both at scale 0.6, read off their trunks). The image gate stays open on the lodge's east face, the drive and walks, and the parkway trees' crown form (the street-tree layer grows only the vase elm), so the ticket cannot close yet

**Released 2026-10-30** (claim of run 10/30/2026, 2:44:49 PM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/41115846184): piece shipped as PR #1503 (resume: CI gate still running when the run's two merge laps ended): the glasshouse ground's gravel drive between the gate's wings, the walk east of the east pier to a forecourt along the conservatory's north front, and the stone coping on the lot line west of the gate, all read through the plate's and Lowe's cameras; 'the drive, the walks and the lawn's edges' is fixed on all four views. The image gate stays open on the lodge's east face, the parkway trees' crown form, and the pale line along the lawn's far side (read, not built), so the ticket cannot close yet

## Owner's report, 2026-10-30: Taylor 16554

Owner, 2026-10-30 (project thread "Match Pullman estate rear to Taylor photo"), on Taylor's 16554 (AIC, artic contentdm mqc/id/29313): *"you are still missing a number of things from the picture, the walkways to the greehouse, the border wall along the road, the whole back of the pullman house needs to be worked, stepped and there is a balcony and the center white area currently is probably more like the color of the rest of the house and you still have a fair amount of detail work to do on the glass atrium and the stable is still not have much surface detail"*; *"the cupola on the stable also"*; *"you have a side on the stable that is facing the lake that i think is not in that pic"*; *"there is a hydrant in that photo"*.

This ticket's part: 16554's foreground is this ground (the camera stands inside it, about 26 m south of 18th Street's south curb, east of the gate): the lawn, its curved stone border along 18th Street and round the Calumet curve, and the walks across it toward the glasshouses. Judge PR #1503's drive, walk and coping through 16554 as well as the plate and Lowe's print.

**Released 2026-10-30** (claim of run 10/30/2026, 9:56:19 PM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/41158397500): PR #1503 (drive, walks, forecourt, coping) is merged to dev. The ticket cannot close yet: all four reference views (inland_1894_lodge, lowe_c1897_lodge, inland_1894_conservatory, lowe_c1897_conservatory) still hold 3 OPEN differences — the lodge's missing east face/slope over the east range's coping (the 11.6 m-deep 1911 outline), the parkway trees' broad low heads left of the gate, and the pale walk/drive-turn line west of the drive. T-1934's merge (#1510) has also moved the Pullman plantings, so each match's flora_sha256 is stale: re-run photo_match on all four when those are worked.
