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
