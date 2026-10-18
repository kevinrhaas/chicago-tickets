---
id: T-2773
title: Keith's lower courses built to the 1888 plate's reading: from the principal sill to grade four even courses (about 0.45 m) on the front and the bow where the model alternates, and the alternating rhythm above split about 0.44 / 0.23 m at the pair's unchanged 0.68 m pitch; the head band's projection weighed against the plate's deeper shadow under it; rebaked, and the four front views' joints items closed
state: done
epic: SOUTH_TIME
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-2770
opened: 2026-10-18
closed: 2026-10-18
pr: 1023
claimed_by: run 10/18/2026, 9:46:16 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-18T17:07:48Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/39137150673
claimed_at: 2026-10-18T14:46:16.105Z
decision: null
decision_answer: null
---

Keith's lower courses built to the 1888 plate's reading: from the principal sill to grade four even courses (about 0.45 m) on the front and the bow where the model alternates, and the alternating rhythm above split about 0.44 / 0.23 m at the pair's unchanged 0.68 m pitch; the head band's projection weighed against the plate's deeper shadow under it; rebaked, and the four front views' joints items closed.

Piece 2 of 2 of **T-2770 — Keith's front joints, bow colonnette capitals and head bands read from the 1888 plate, which resolves individual stones on the lower storeys: built or matched course by course once T-2762's level camera registers the render, and in the four front views each item built or ruled with its grain stated**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2770 was split (2026-10-18T13:11:06.129Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 8m ago, run 10/18/2026, 8:03:15 AM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/39129546246) — held by the run that split it

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/39129546246) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)
1. Up from the principal sill, the front's and the bow's courses laid deep and thin in turn at the print's split (T-2772 reads 33 / 18 px, about 0.44 / 0.24 m, against the model's 0.49 / 0.195 m, the pair's pitch unchanged), and the bow's beds laid level with the front's, as the print lays them (7 of 8 front beds have a bow bed within 3 px in print, 2 of 7 in the render).
2. From the principal sill to the pavement, three even courses (35-37 px in print, about 0.47-0.49 m) over a 49 px foot, on the front and the bow, where the model lays seven, thin and deep in turn over two base courses.
3. Rebaked, every Keith view re-rendered, and `python3 tools/keith_plate_grain_read.py` re-run on the new render: its print and render rows agree within 2 px a course, and the four front views' T-2772 joints items set `fixed`.

## Findings carried from T-2772's reading (2026-10-18)

- `tools/keith_plate_grain_read.py --write` and its table, `docs/RESEARCH/photo-match/keith_house_1808_prairie/inland-1888-grain-read.json`, hold every bed read. The print's beds are read where the front's south strip (x 272-322) and the bow's south flank (x 335-395) agree, so a rock face's own shadow is not taken for a joint.
- The head band's shadow came out 16.5 px deep in print against 12.6 at scale in the render, about 4 px (0.06 m) at 67 px/m. That is at the edge of this grain, so it is probably a ruling (`not shown`) rather than a build. Weigh it against a second shadow (the bow's moulded cap) before changing the band's projection.
- The basement's height is not this ticket's to rule. The print's sill bed stands about 157 px over the pavement and the render's about 198, which is T-2765's bow-lights question (the bow's principal and basement lights). Lay the even courses from wherever T-2765 leaves the sill.
