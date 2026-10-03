---
id: T-2054
title: Bring the two wagon jaunts inside six minutes: outfit-for-the-west 9.0 and freight-for-the-store 6.1 min by wagon
state: open
epic: RENDERING
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-2041
opened: 2026-10-03
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

Bring the two wagon jaunts inside six minutes: outfit-for-the-west 9.0 and freight-for-the-store 6.1 min by wagon.

Piece 4 of 6 of **T-2041 — Time all 25 primary paths on the published mirror at the recommended mode and at Fly and Instantly, and re-cut any jaunt outside 3-6 minutes**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

**Acceptance:** `node tools/time_jaunts.mjs --only outfit-for-the-west,freight-for-the-store --out /tmp/t.json` reports each named jaunt's recommended-mode primary path at 3–6 min on the published mirror at 390×780 (the reference viewport; it reads a few seconds longer than 1280×800 on most paths), with Fly and Instantly still faster, and docs/measurements/jaunt-timing.md is regenerated with the new rows. Levers, per the parent: re-cut the text, choose a nearer supported stop, or change the recommended mode where the jaunt's own prose allows it. Never touch the estimate formula, and never shave a stop's `read_s` without shortening its text.

**Measured 2026-10-03 (T-2051), 390×780:** outfit-for-the-west 8.98 min by wagon (156 s reading + 383 s riding; on horseback it would still be about 6.1); freight-for-the-store 6.12 (182 + 185; 5.83 at 1280×800). Both are wagon errands by premise ("load the wagon"), so a pace change is the weakest lever here.
