---
id: T-3365
title: 2009 Prairie's remaining front detailing to its pictures: the oriel's carved apron, the windows' hoods and the gable's pendant, the north corner's quoins, the gable's carved crest, the basement's three lights, the door's pinnacles, the near stack's place, and a camera solved on Monroe's 1896 plate
state: claimed
epic: SOUTH_TIME
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-1914
opened: 2026-11-03
closed: null
pr: null
claimed_by: run 11/6/2026, 9:41:08 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/42334574759
claimed_at: 2026-11-07T03:41:08.386Z
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
