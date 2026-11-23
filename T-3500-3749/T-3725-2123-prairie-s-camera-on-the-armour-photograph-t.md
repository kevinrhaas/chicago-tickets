---
id: T-3725
title: 2123 Prairie's camera on the Armour photograph, the photo-match worked down and the image-gate sign-off (after the piece before it)
state: open
epic: SOUTH_TIME
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-1930
opened: 2026-11-22
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

2123 Prairie's camera on the Armour photograph, the photo-match worked down and the image-gate sign-off (after the piece before it).

Piece 3 of 3 of **T-1930 — Refine 2123 masonry and 2125 frame neighbours**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-1930 was split (2026-11-22T12:16:49.327Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 2m ago, run 11/22/2026, 6:15:13 AM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/45020665665) — held by the run that split it

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/45020665665) may be working one of the pieces now.

## Image gate stays on T-1930

T-1930 carries an `## Image gate` section. The last of these pieces to close is refused (`done`) until every building it names matches every one of its reference views, so a slice that leaves a difference open says so in the match record.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

**Released 2026-11-23** (claim of run 11/23/2026, 5:27:07 AM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/45158990805): Camera solved and the photo-match worked down on branch steward/t3725-2123-armour-camera (storeys, basement, mansard, dormers, flank dormer and stack now stand on the print's). Two differences stay open in data/reference_views/house_2123_prairie/chicagology_armour_photo.match.json, so the image gate cannot sign off: the skyline steps ~0.45 m down south of the bow with a corniced, crested head over the second street dormer (K01's front crown refuses the print's north-flank dormer inside its depth; its hooded dormer takes only a flat-headed sash where the print's is round-headed), and the front's south end turns its mansard down at the print's right edge (the sheet's cut entrance corner, liberty L-k01-2123-prairie-3724, not built). The next run on this ticket needs a K01 change for one of those, not more reading.
