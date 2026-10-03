---
id: T-2053
title: Bring the three on-foot jaunts just over six minutes inside it: inspect-a-lot 6.8, shopping-south-water 6.6, fort-dearborn-errand 6.2 min
state: done
epic: RENDERING
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-2041
opened: 2026-10-03
closed: 2026-10-03
pr: 373
claimed_by: run 10/3/2026, 5:28:21 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-03T23:34:02Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37158382852
claimed_at: 2026-10-03T22:28:21.928Z
decision: null
decision_answer: null
---

Bring the three on-foot jaunts just over six minutes inside it: inspect-a-lot 6.8, shopping-south-water 6.6, fort-dearborn-errand 6.2 min.

Piece 3 of 6 of **T-2041 — Time all 25 primary paths on the published mirror at the recommended mode and at Fly and Instantly, and re-cut any jaunt outside 3-6 minutes**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

**Acceptance:** `node tools/time_jaunts.mjs --only inspect-a-lot,shopping-south-water,fort-dearborn-errand --out /tmp/t.json` reports each named jaunt's recommended-mode primary path at 3–6 min on the published mirror at 390×780 (the reference viewport; it reads a few seconds longer than 1280×800 on most paths), with Fly and Instantly still faster, and docs/measurements/jaunt-timing.md is regenerated with the new rows. Levers, per the parent: re-cut the text, choose a nearer supported stop, or change the recommended mode where the jaunt's own prose allows it. Never touch the estimate formula, and never shave a stop's `read_s` without shortening its text.

**Measured 2026-10-03 (T-2051), 390×780:** inspect-a-lot 6.78 min (137 s reading + 270 s walking; a choice at its last stop promises to "walk its own ground"); shopping-south-water 6.60 (124 + 272; its last stop begins "Walk up to Lake Street"); fort-dearborn-errand 6.37 after T-1743 moved Beaubien's homestead off the fort road (112 + 270; 6.23 at 1280×800; it read 6.18 before T-1743). By wagon each would be about 3.6–4.1 min, but the first two are written as walks.
