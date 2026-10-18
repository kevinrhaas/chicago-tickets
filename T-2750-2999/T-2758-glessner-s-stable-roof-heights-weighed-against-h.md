---
id: T-2758
title: Glessner's stable roof heights weighed against HABS photograph 1 and the Cornell view: whether the ~2 ft by which photograph 1 reads the whole stable roof low is camera or roof, the Cornell camera re-solved at the roof, and the cupola's centre parallax (about 4 ft north of S14.6) put to the owner if it holds
state: done
epic: SOUTH_TIME
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-2228
opened: 2026-10-18
closed: 2026-10-18
pr: 1017
claimed_by: run 10/18/2026, 8:42:26 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-18T15:28:56Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/39132201933
claimed_at: 2026-10-18T13:42:26.311Z
decision: null
decision_answer: null
---

Glessner's stable roof heights weighed against HABS photograph 1 and the Cornell view: whether the ~2 ft by which photograph 1 reads the whole stable roof low is camera or roof, the Cornell camera re-solved at the roof, and the cupola's centre parallax (about 4 ft north of S14.6) put to the owner if it holds.

Piece 2 of 5 of **T-2228 — Glessner: run final photographic comparison and evidence sign-off**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2228 was split (2026-10-18T09:32:42.378Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 40m ago, run 10/18/2026, 3:53:05 AM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/39112871207) — held by the run that split it
- branch `steward/t2228-glessner-final-comparison`

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/39112871207) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

## Finding on the lap of #1017 (2026-10-18)

The report did not re-derive off CI: on the steward runner `--check` went red on #1017's own unchanged head (same numpy 2.5.4 / scipy 1.18.1). Photograph 1's `doorway_aspect` fit has no minimum. With its controls nearly all in the north face, a level camera trades pixel aspect exactly against focal length and distance: RMS is 3.9229 px at every pinned aspect from 1.00 to 1.06. So the free fit stopped wherever rounding left it, which put the cupola at S11.3 in CI and S11.77 here. Along that valley the gable stays at 38.62 ft, so **camera, not roof** stands, but the cupola slides from S14.4 to S10.4. #1017 merged at a head that did not carry the fix; the follow-up PR walks the valley at pinned aspects and corrects the S11.3 in LIBERTIES.md, the habs-01 match record and the T-2228 README.
