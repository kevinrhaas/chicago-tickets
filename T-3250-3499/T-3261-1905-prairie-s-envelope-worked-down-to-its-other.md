---
id: T-3261
title: 1905 Prairie's envelope worked down to its other pictures (the c. 1905 Daily News view DN-0003324, the undated '923' print, the 1893 engraving): their cameras, the south-west corner's pavilion, the conservatory's glazing and its balcony, the rear and north faces, and the rear, roof and cost views the envelope's acceptance asks for
state: claimed
epic: SOUTH_TIME
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-1904
opened: 2026-10-30
closed: null
pr: null
claimed_by: run 10/30/2026, 5:14:23 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/41136042461
claimed_at: 2026-10-30T22:14:24.396Z
decision: null
decision_answer: null
---

1905 Prairie's envelope worked down to its other pictures (the c. 1905 Daily News view DN-0003324, the undated '923' print, the 1893 engraving): their cameras, the south-west corner's pavilion, the conservatory's glazing and its balcony, the rear and north faces, and the rear, roof and cost views the envelope's acceptance asks for.

Piece 2 of 2 of **T-1904 — Refine 1905 Marshall Field Sr. mansion envelope**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-1904 was split (2026-10-30T08:55:44.846Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 4m ago, run 10/30/2026, 3:52:12 AM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/41028688307) — held by the run that split it

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/41028688307) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

## Found by T-3260 (PR #1482), 2026-10-30

- **The canted south-west corner needs a K01 change first.** `form.cant_corner` (T-3186, 1901's) refuses any house that is not `construction: stone` under `k10.cornice.moulded_stone`, and it always cuts a window column into the face; 1905's face is brick, blank in both storeys between stone strips, under a bracketed cornice, with the largest dormer over it. The builder (`k01_frontage.py`) is in every K01 mesh's input hash, so letting the cut take brick restamps every K01 house (their GLBs should re-emit byte-identical). Through the plate's camera the cut is about 3.4 m back each way.
- **The plate's front reads about 3 m longer than the sheet's 15.25 m** through the camera (`data/reference_views/marshall_field_house_1905_prairie/pictorial_1893_plate.json`, 14.7 px RMS, eye height held at 1.6 m). Re-solve it with the Daily News view (DN-0003324) before moving the window columns, which are laid in proportion for now.
- The sheet's two-storey north range at the rear (u -2.5 to 4.25, v -4.5 to 0) stands beside the main body, not behind it, and K01's `rear_wings` refuse that; it is not built.

**Released 2026-10-30** (claim of run 10/30/2026, 7:46:18 AM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/41057253166): piece shipped and merged as PR #1490 (squash 23815a1, CI gate green; mobile smoke parts 1 and 3 and desktop part 1 PASS, zero page errors): the front's three iron balconies before the north, door and wide columns' chamber windows, on consoles at the chamber floor, and the low door hood withdrawn. Still open on the plate's match record: the door column's balcony 3.0 m against about 3.5 m and its tall consoles, the balconies behind the canted corner and on the conservatory roof, the canted south-west corner, the front's length, the mansard, the conservatory's glazing, the carving, the chamber windows' height; the Daily News, '923' and engraving cameras are not yet solved
