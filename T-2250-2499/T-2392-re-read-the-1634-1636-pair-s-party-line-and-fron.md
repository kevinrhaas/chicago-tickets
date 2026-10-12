---
id: T-2392
title: Re-read the 1634/1636 pair's party line and front line once for both, and move the K01 bodies onto them
state: review
epic: SOUTH_TIME
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-10-11
closed: null
pr: 719
claimed_by: run 10/11/2026, 9:40:16 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38196413412
claimed_at: 2026-10-12T02:40:16.702Z
decision: null
decision_answer: null
---

Re-read the 1634/1636 pair's party line and front line once for both, and move the K01 bodies onto them.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

Carried out of T-2347 (the finding T-2348 wrote into it, 2026-10-12), so it outlives that ticket's close.

Read back through the sheet's fit (T-1250) in each record's own frame:

- **1634's south wall stands 0.6-0.7 m inside the party line.** The trace's shared line with 1636 is
  at v -0.4 to -0.73 in 1634's frame (the whole outline, main body and rear wing, runs along v -0.7);
  its K01 south wall is at v 0. 1636 (T-2348, #713) puts its north wall on the line, so the pair
  shows a ~0.7 m slot between two blank party walls. T-2347 built 1634's rear wing flush with the
  main body's south wall (v 0), not on the line, so moving the body moves the wing with it: its
  rects are in the record's frame.
- **Both fronts stand 1.6 m behind the traced outline.** The trace's front edge is at u 15.3-15.4 in
  both houses (the outer side of the blue band the sheet draws along the pair's fronts); the draft's
  fit and both K01 bodies stop at u 13.75. Whether the wall face is the band's outer or inner side
  is one question for the pair, answered once for both.

1634's origin is re-derived from the trace by `tools/draft_prairie_1904.py --check` (its position
note), so the move is made where that derivation is, not by hand-editing `position`.

**Acceptance:** the pair meets on one party line with no slot, and its fronts stand on the line the
ticket argues for, in /1904/, with the reasoning in a RESEARCH note and the liberties updated.
