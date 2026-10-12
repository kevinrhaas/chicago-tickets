---
id: T-2423
title: 1638 Prairie's gable from its photograph: the pointed twin windows under their cusped hood mould and finial, the oculus, and the photograph's camera solved into its first match record
state: done
epic: SOUTH_TIME
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-1865
opened: 2026-10-12
closed: 2026-10-12
pr: 746
claimed_by: run 10/12/2026, 4:20:12 PM CT
blocked_on: null
needs_bake: true
closed_at: 2026-10-12T22:23:18Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38309473841
claimed_at: 2026-10-12T21:20:12.685Z
decision: null
decision_answer: null
---

1638 Prairie's gable from its photograph: the pointed twin windows under their cusped hood mould and finial, the oculus, and the photograph's camera solved into its first match record.

Piece 1 of 4 of **T-1865 — Finish 1638 Shortall-Gregory Gothic house architecture**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-1865 was split (2026-10-12T21:20:02.432Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 1m ago, run 10/12/2026, 4:19:02 PM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/38309473841) — held by the run that split it

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/38309473841) may be working one of the pieces now.

**Acceptance:** the gable of `shortall_gregory_house_1638_prairie_front` carries what the photograph (`a16-cgy-1638-gothic-photo`, source `chicagology_1638_prairie_photo`) shows on it: the twin windows' heads POINTED (not the kit's flat heads), under one hood mould that rises to a finial between them, and the round oculus cut high in the gable — baked into the GLB in the tree. The photograph's camera is solved into `data/reference_views/shortall_gregory_house_1638_prairie_front/chicagology_front.json` and `tools/photo_match.mjs` writes its first match record and side-by-side; the gable's differences read `fixed`, and everything the later pieces own (bay, entrance, fence) is listed `open` so they inherit a written list. Needs a bake (`./tools/bake.sh --only shortall_gregory_house_1638_prairie_front`).
