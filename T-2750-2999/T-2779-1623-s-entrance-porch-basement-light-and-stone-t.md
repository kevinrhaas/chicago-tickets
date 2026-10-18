---
id: T-2779
title: 1623's entrance porch, basement light and stone: the entrance arch as broad as the window's (about 1.85 m) springing from a carved band at about 3.4 m, the door and stoop about 1.3 m north of its axis at the back of the porch with the landing's iron guard, the 1.8 m segmental basement light behind its grille, the smoother coursed stone above the springing; K01 rebaked and 1623's match record brought to matches
state: claimed
epic: SOUTH_TIME
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-2729
opened: 2026-10-18
closed: null
pr: null
claimed_by: run 10/18/2026, 2:48:21 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/39160097151
claimed_at: 2026-10-18T19:48:21.623Z
decision: null
decision_answer: null
---

1623's entrance porch, basement light and stone: the entrance arch as broad as the window's (about 1.85 m) springing from a carved band at about 3.4 m, the door and stoop about 1.3 m north of its axis at the back of the porch with the landing's iron guard, the 1.8 m segmental basement light behind its grille, the smoother coursed stone above the springing; K01 rebaked and 1623's match record brought to matches.

Piece 3 of 3 of **T-2729 — 1623's oriel at the drawing's size: K01 lays openings under a street-front oriel and lets its upper stage, carved frieze and conical roof rise past the main cornice, the oriel about 4.8 m at the wall and 0.9 m out with four front lights and lit cants, and the window and entrance arches at the drawing's places; K01 rebaked, and 1623's match record brought to matches**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2729 was split (2026-10-18T15:10:53.379Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 1m ago, run 10/18/2026, 10:09:51 AM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/39138026180) — held by the run that split it

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/39138026180) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

## Findings carried from T-2777 (2026-10-18)

The oriel now stands at the drawing's size (4.8 m at the wall, 3.4 m of front, 0.65 m out) over arches at 1.55 and 4.6 m (PR #1025). One new open row in `building_budget_front.match.json` is this piece's: **the drawing places the oriel's front about 0.35 m north of the middle of its wall junctions**. Its cants are drawn 20 px (north) and 51 px (south) across, where a symmetric oriel through the solved camera draws 31 and 28, so the build's front lights stand 16-18 px south of the drawn ones. A level camera north of the oriel's axis cannot widen the south cant past the north one, so the cause is either the pen perspective (rule it as the drawing's and mark the row accordingly) or an oriel whose front stands north of its middle, which would need a K01 change: `_bays` takes only a symmetric canted plan. The cant lights are also 0.35 m, narrower than drawn: a 0.96 m cant holds no wider light with its recess in front of the house wall (`check_bay_kit` recess and pier rules).
