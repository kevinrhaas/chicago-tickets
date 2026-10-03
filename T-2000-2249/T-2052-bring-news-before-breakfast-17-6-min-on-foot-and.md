---
id: T-2052
title: Bring news-before-breakfast (17.6 min on foot) and new-in-chicago (10.4 min on foot) inside six minutes: nearer stops, or a recommended pace their prose allows
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

Bring news-before-breakfast (17.6 min on foot) and new-in-chicago (10.4 min on foot) inside six minutes: nearer stops, or a recommended pace their prose allows.

Piece 2 of 6 of **T-2041 — Time all 25 primary paths on the published mirror at the recommended mode and at Fly and Instantly, and re-cut any jaunt outside 3-6 minutes**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

**Acceptance:** `node tools/time_jaunts.mjs --only news-before-breakfast,new-in-chicago --out /tmp/t.json` reports each named jaunt's recommended-mode primary path at 3–6 min on the published mirror at 390×780 (the reference viewport; it reads a few seconds longer than 1280×800 on most paths), with Fly and Instantly still faster, and docs/measurements/jaunt-timing.md is regenerated with the new rows. Levers, per the parent: re-cut the text, choose a nearer supported stop, or change the recommended mode where the jaunt's own prose allows it. Never touch the estimate formula, and never shave a stop's `read_s` without shortening its text.

**Measured 2026-10-03 (T-2051), 390×780:** news-before-breakfast 17.65 min on foot = 204 s of reading + 855 s of walking; even on horseback the walking would be about 190 s, so about 6.6 min, which means a pace change alone cannot fix it. It needs nearer stops. new-in-chicago 10.42 min on foot = 126 s + 499 s; by wagon about 5.4 min, on horseback about 3.9, but its opening reads "Walk the river street", so a pace change means re-cutting that line too.
