---
id: T-2051
title: Time all 25 primary paths on the published mirror at the recommended mode, Fly and Instantly, with a harness that rides every leg through the travel controller
state: done
epic: RENDERING
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-2041
opened: 2026-10-03
closed: 2026-10-03
pr: 368
claimed_by: run 10/3/2026, 3:36:06 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-03T21:42:59Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37148395120
claimed_at: 2026-10-03T20:36:06.277Z
decision: null
decision_answer: null
---

Time all 25 primary paths on the published mirror at the recommended mode, Fly and Instantly, with a harness that rides every leg through the travel controller.

Piece 1 of 6 of **T-2041 — Time all 25 primary paths on the published mirror at the recommended mode and at Fly and Instantly, and re-cut any jaunt outside 3-6 minutes**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

**Acceptance:** `node tools/time_jaunts.mjs` rides every available jaunt's primary path on the published mirror through the travel controller (`travel.simulate`) at the recommended mode, Fly and Instantly — 75 runs — with zero page errors and no stalled ride, and writes docs/measurements/jaunt-timing.json and .md with the menu's estimate beside each reading. This is the measurement half of the split: the out-of-band jaunts are recorded red here and fixed in T-2052–T-2056, so the fix cannot redefine success.
