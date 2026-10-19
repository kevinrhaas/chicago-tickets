---
id: T-2880
title: Glessner's sheet-4 terrace readings carried onto the plan's frame (re-zeroed on the printed 26'-10" court face, about +0.65 ft): the coping's section profile, the two terrace grilles and the east-court garden light moved with the habs04-terrace-section camera re-zeroed on the same control, the coping's terminal built into the plan's post, rebaked and habs04-terrace-section brought to matches
state: open
epic: SOUTH_TIME
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-2860
opened: 2026-10-19
closed: null
pr: null
claimed_by: null
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: null
decision: null
decision_answer: null
---

Glessner's sheet-4 terrace readings carried onto the plan's frame (re-zeroed on the printed 26'-10" court face, about +0.65 ft): the coping's section profile, the two terrace grilles and the east-court garden light moved with the habs04-terrace-section camera re-zeroed on the same control, the coping's terminal built into the plan's post, rebaked and habs04-terrace-section brought to matches.

Piece 2 of 2 of **T-2860 — Glessner's courtyard plan-against-section ruled - HABS sheet 2 against sheet 4 along S at the bow's flanks (sheet 4 draws the bow at about S 26.3-38.6 against the plan's 26.8-39.3), the stair tower (0.63 ft, radius 0.3 ft) and the terrace's terminal post (about 1.1 ft) - and the ruling built in the bow, the tower and the coping's terminal at the post; rebaked and habs04-terrace-section brought to matches**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2860 was split (2026-10-19T19:30:38.067Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 21m ago, run 10/19/2026, 2:09:33 PM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/39307905632) — held by the run that split it

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/39307905632) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

## Handed on by T-2879 (2026-10-19): the ruling to build on

T-2879 ruled the plan against the section. The readings and reasoning are in `docs/RESEARCH/glessner-court-ruling-T-2879/` in the code repo, with `read_court.py` to reproduce them. Sheet 2's printed court chain (12'-6" + 12'-0" + 10'-0" + 12'-8" = 47'-2") governs S. Sheet 4's court is the same court shifted north by **+0.65 ft ± 0.05**, not rescaled: its face reads 26.21 against the printed 26.83, its bow flank 38.66 against 39.33, and its bow is 12.45 ft across against the printed 12.5. Its tower drum is drawn 1.1 ft too wide, so it is not adopted. The bow, the tower and the post stay where the plan has them.

This piece also carries the structure record's notes. Every byte of `data/structures/glessner_house.json` is part of the Light derivative's recipe (`generators/common/versions.py` `lod_recipe_sha`), so T-2879 left the record untouched. When this piece rewrites the record and rebuilds:
- `tower_stair.note`: replace "HABS4 suggests S56.73/r5.55; this cross-sheet disagreement is retained…" with the ruling. The printed 10'-0" mass runs S51.33-61.33, and r5.25 at W27.3 meets the W26.5 face at S50.91-61.29. Sheet 4's 11.09-ft drum, re-zeroed, runs S51.86-62.95.
- `hall_bow.note`: add the printed 12'-6" from the court face (26.83) to the bow's tangent (39.33).
- `bow_terrace` (v4_detail): `cap_section_profile`, `window_S` and the east-court garden light were read at sheet 4's un-re-zeroed S. Move them +0.65 together with the habs04-terrace-section camera, and check habs04-court-exterior and habs04-hood-section, which read the same sheet.
