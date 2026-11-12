---
id: T-3365
title: 2009 Prairie's remaining front detailing to its pictures: the oriel's carved apron, the windows' hoods and the gable's pendant, the north corner's quoins, the gable's carved crest, the basement's three lights, the door's pinnacles, the near stack's place, and a camera solved on Monroe's 1896 plate
state: review
epic: SOUTH_TIME
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-1914
opened: 2026-11-03
closed: null
pr: 1965
claimed_by: run 11/12/2026, 12:43:33 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/43280483740
claimed_at: 2026-11-12T18:43:33.750Z
decision: null
decision_answer: null
---

2009 Prairie's remaining front detailing to its pictures: the oriel's carved apron, the windows' hoods and the gable's pendant, the north corner's quoins, the gable's carved crest, the basement's three lights, the door's pinnacles, the near stack's place, and a camera solved on Monroe's 1896 plate.

Piece 2 of 2 of **T-1914 — Finish 2009 Mayer-Meyer French Gothic house architecture**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-1914 was split (2026-11-04T00:04:51.673Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 42m ago, run 11/3/2026, 5:22:55 PM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/41737884762) — held by the run that split it
- branch `steward/t1914-meyer-entrance-oriel-frieze` — the splitter's own

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/41737884762) may be working one of the pieces now.

## Image gate stays on T-1914

T-1914 carries an `## Image gate` section. The last of these pieces to close is refused (`done`) until every building it names matches every one of its reference views, so a slice that leaves a difference open says so in the match record.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

**Released 2026-11-06** (claim of run 11/6/2026, 1:18:16 PM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/42275101954): PR #1786 (resume: gate still running, nothing red) builds 2009 Prairie's carved crest on a flat-topped gable (K01 shaped_gable finial form 'crest') and the door's three pinnacles (arch.pilasters.pinnacles); both items fixed in the chicagology_photo record. Still open there: the near stack's place and corbelled cap (needs an outside-wall stack on a hip; one camera cannot fix its depth), the base's top (the print's rock face to ~1.25 m and smooth band to ~1.9 m lie outside the K02 sandstone_brown/dressed_trim ranges), the oriel's carved apron, the windows' hoods and the gable's pendant, the gable's south foot, and Monroe's 1896 plate camera. Not split: the gate stays on T-1914.

**Landed 2026-11-06:** PR #1786 merged to `dev` (squash c0405a0c8): the gable's carved crest (K01 `shaped_gable.finial.form: "crest"`) and the door's three pinnacles (`entrance_kit.arch.pilasters.pinnacles`) are built and marked `fixed` in `mayer_house_2009_prairie/chicagology_photo.match.json` (8 open differences down to 6). Do not rebuild them. Still open on this ticket, per that record: the gable's south foot, the oriel's carved apron, the windows' hoods and the gable's pendant, the base's top, the near stack's place and corbelled cap; plus the north corner's quoins, the basement's three lights and the Monroe 1896 camera from the title. `done` stays refused by T-1914's image gate until the record matches.

**Released 2026-11-06** (claim of run 11/6/2026, 4:12:32 PM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/42295885341): PR #1795 (resume: gate still running, nothing red — 6 of 8 CI parts green when handed on) lays 2009 Prairie's basement to the print: three rock-faced courses to 1.38 m under a smooth band to 1.84 m (base_top_m 1.84; K02 sandstone_brown base courses widened to 1-3); match record's 'base's top' fixed, band foot +0.12 m within tolerance, 5 open. Do not rebuild it. Still open: the near stack's place and corbelled cap (needs a K01 stack on a hip roof's wall line — on_cornice and the k15 head are mansard-only today), the oriel's carved apron, the hoods and pendant, the gable's south foot, and the Monroe 1896 camera.

**Released 2026-11-06** (claim of run 11/6/2026, 6:15:33 PM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/42315517668): PR #1802 lays the oriel's carved apron: a K08 apron_band (5.55-5.89 m, under the lights' sill stones) carrying 17 rosettes in two staggered rows at 0.38 m, as the Chicagology print shows; match record item fixed, relief shallower than the print within tolerance; 4 open left. Do not rebuild it. Still open: the near stack's place and corbelled cap (a K01 stack on a hip roof's wall line), the windows' hoods and the gable's pendant, the gable's south foot, and the Monroe 1896 camera. The image gate stays on T-1914.

**Released 2026-11-06** (claim of run 11/6/2026, 8:13:39 PM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/42327509750): PR #1805 merged to dev: 2009 Prairie's windows' moulded hoods and the gable's pendant built (K01 street_front_windows.hoods: the paired light's drip mould with label stops and a carved pendant to 12.96 m, consoles under the oriel either side of the ground window, a splayed key block over the small light) and the street gutter taken off the gable's foot (shaped_gable.takes_gutter); match record item fixed, carving drawn as blocks within tolerance; 3 open left. Do not rebuild them. Still open: the near stack's place and corbelled cap (a K01 stack on a hip roof's wall line), the gable's south foot, and the Monroe 1896 camera. The image gate stays on T-1914.

**Released 2026-11-06** (claim of run 11/6/2026, 9:41:08 PM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/42334574759): PR #1809 merged to dev (squash bf26279da): 2009 Prairie's near north stack built astride the north wall where the Chicagology print centres it (K01 chimneys.stacks[].astride_wall, a hip's stack with its breast carried up the flank from the ground; render shaft x 327-410 px vs the print's 331-409, top within 0.1 m), and both stacks given a K15 head (band, proud stage, stone cap); match record item fixed. Do not rebuild it. Still open: the gable's south foot; the stacks' buff brick where the print draws them as dark as the front's brick (recorded open, a tone in a monochrome print — wants a colour source); the Monroe 1896 camera. The breast below the eave is 'not shown' (trees in both pictures; L-k01-2009-meyer-north-stack-3365). The image gate stays on T-1914.

**Released 2026-11-07** (claim of run 11/6/2026, 11:09:05 PM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/42340483841): PR #1820 lays 2009 Prairie's gable south foot to the Chicagology print: K01 shaped_gable.run_on carries the coping down the print's line to the party wall at about 10.3 m (read row by row), the front, party wall and hip eave cut down under it to a brick cheek 0.9 m back (L-k01-2009-meyer-gable-run-on-3365); match record item fixed. Do not rebuild it. Still open: the stacks' buff brick where the print draws them dark (a tone in a monochrome print, wants a colour source), and the Monroe 1896 camera. The image gate stays on T-1914.

**Released 2026-11-12** (claim of run 11/12/2026, 12:38:38 AM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/43168092462): PR #1936 merged to dev (squash ad9c75409): Monroe's 1896 plate solved as a camera (data/reference_views/mayer_house_2009_prairie/monroe_1896_plate.json; its front fits the photograph's at one scale, 23 points, 3.8 px RMS; the eye is the photograph's, fixed by the rear stack the plate does not draw) and its match record written (verdict differs). Do not re-solve it. NEW, open in BOTH records: the course at about 9.1 m and the paired light's group over it fall to the south in both pictures (the photograph's course from about 9.84 m at x 500 px to a point at about 9.08 m at x 1055 px, short of the party line; the hood top y 545 to 590 px) while the front's verticals stand plumb; the build lays them level, about 0.6 m low at the north end. Not built: the plate is drawn from about the photograph's place, so it may inherit a sheared print; settling building-or-print wants a third picture of the front or a reading of the brick's bed joints across that storey. Still open besides: the stacks' brick colour (wants a colour source) and the trees (not the house's). The image gate stays on T-1914.

**Released 2026-11-12** (claim of run 11/12/2026, 2:10:11 AM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/43179179198): PR #1941 (resume: gate still running, nothing red) re-solves the Chicagology camera as a view turned 22.4 degrees south of square: the course and hood that fell to the south are level (9.2 m, 11.3 m), so the falling-course item is fixed. Through it the oriel (crown 8.45 m, 0.5 m of brick under the course), paired light (9.4-11.0 m), hood (11.0-11.3 m), pendant (to 12.15 m) and attic light (13.2-14.0 m) are lowered to the print. Do not re-solve the camera. Still open: the near stack's top (16.3 m in the print against about 17.8 m built) and the north corner's wall head (about 11.3 m against 11.97 m), which come from the third storey's height and want doing together; a turned refit of Monroe's plate camera; and the stacks' brick colour. The image gate stays on T-1914.

**Released 2026-11-12** (claim of run 11/12/2026, 4:10:51 AM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/43197074733): PR #1941 merged: the Chicagology camera re-solved as a turned view (22.4° south of square) and the upper front (oriel, paired light, hood, pendant, attic light) re-read and lowered through it. Still open on chicagology_photo: the north corner's wall head (~0.65 m high, 11.97 m built vs ~11.3 m in the print) and the near stack's top (~1.5 m high) — lower them together, wall head first; and the stacks' brick colour wants a colour source. Trees are not this record's.

**Released 2026-11-12** (claim of run 11/12/2026, 4:51:27 AM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/43201272709): PR #1946 (resume: gate still running — gate 8/8 green, only the humans check in progress; nothing red) lowers 2009 Prairie's north corner and near stack to the turned Chicagology camera: third storey 2.75 -> 2.22 m (wall head 11.42 m against the print's ~11.3 m; the paired light's top under the gable slab's foot holds it there), ledge 11.45 m, slab foot 11.0 m, stacks 0.75 m over the ridge (near stack's cap y 108-121 px vs the print's 107). Both items fixed in chicagology_photo.match.json; Monroe plate's stack and corner re-read within tolerance. Do not rebuild them. Still open: the stacks' brick colour (wants a colour source) and the trees (not the house's). The image gate stays on T-1914.
