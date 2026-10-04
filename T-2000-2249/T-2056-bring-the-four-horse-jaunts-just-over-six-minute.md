---
id: T-2056
title: Bring the four horse jaunts just over six minutes inside it: sunday-circuit 6.6, schoolday-errand 6.4, work-on-waterfront 6.2, materials-for-a-roof 6.1 min
state: review
epic: RENDERING
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-2041
opened: 2026-10-03
closed: null
pr: 375
claimed_by: run 10/3/2026, 6:38:11 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37162225136
claimed_at: 2026-10-03T23:38:11.657Z
decision: null
decision_answer: null
---

Bring the four horse jaunts just over six minutes inside it: sunday-circuit 6.6, schoolday-errand 6.4, work-on-waterfront 6.2, materials-for-a-roof 6.1 min.

Piece 6 of 6 of **T-2041 — Time all 25 primary paths on the published mirror at the recommended mode and at Fly and Instantly, and re-cut any jaunt outside 3-6 minutes**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

**Acceptance:** `node tools/time_jaunts.mjs --only sunday-circuit,schoolday-errand,work-on-waterfront,materials-for-a-roof --out /tmp/t.json` reports each named jaunt's recommended-mode primary path at 3–6 min on the published mirror at 390×780 (the reference viewport; it reads a few seconds longer than 1280×800 on most paths), with Fly and Instantly still faster, and docs/measurements/jaunt-timing.md is regenerated with the new rows. Levers, per the parent: re-cut the text, choose a nearer supported stop, or change the recommended mode where the jaunt's own prose allows it. Never touch the estimate formula, and never shave a stop's `read_s` without shortening its text.

**Measured 2026-10-03 (T-2051), 390×780:** sunday-circuit 6.55 min on horseback (120 s reading + 273 s riding); schoolday-errand 6.35 (179 + 202); work-on-waterfront 6.23 (198 + 176; 6.05 at 1280×800); materials-for-a-roof 6.07 (166 + 198; 6.10 at 1280×800). Each is 4–33 s over, so a text trim or one nearer stop should be enough. Horse is the fastest ground pace.
