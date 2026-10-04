---
id: T-2055
title: Bring the three long horse jaunts inside six minutes: from-prairie-to-town 9.4, boots-and-leather 7.7, soap-and-candles 7.1 min on horseback
state: done
epic: RENDERING
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-2041
opened: 2026-10-03
closed: 2026-10-04
pr: 371
claimed_by: run 10/3/2026, 5:17:04 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-04T05:53:57Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37157538464
claimed_at: 2026-10-03T22:17:04.667Z
decision: null
decision_answer: null
---

Bring the three long horse jaunts inside six minutes: from-prairie-to-town 9.4, boots-and-leather 7.7, soap-and-candles 7.1 min on horseback.

Piece 5 of 6 of **T-2041 — Time all 25 primary paths on the published mirror at the recommended mode and at Fly and Instantly, and re-cut any jaunt outside 3-6 minutes**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

**Acceptance:** `node tools/time_jaunts.mjs --only from-prairie-to-town,boots-and-leather,soap-and-candles --out /tmp/t.json` reports each named jaunt's recommended-mode primary path at 3–6 min on the published mirror at 390×780 (the reference viewport; it reads a few seconds longer than 1280×800 on most paths), with Fly and Instantly still faster, and docs/measurements/jaunt-timing.md is regenerated with the new rows. Levers, per the parent: re-cut the text, choose a nearer supported stop, or change the recommended mode where the jaunt's own prose allows it. Never touch the estimate formula, and never shave a stop's `read_s` without shortening its text.

**Measured 2026-10-03 (T-2051), 390×780:** from-prairie-to-town 9.35 min on horseback (114 s reading + 447 s riding; its estimate reads 10.20, 51 s above the ride, the widest gap in the library); boots-and-leather 7.73 (171 + 293); soap-and-candles 7.13 (168 + 260). Horse is the fastest ground pace, so this takes nearer stops or a shorter route.

## Found during the run (2026-10-03, PR #371)

At **1280×800** the Boots, Leather and the Road ride from Holbrook's store to the Wolf Point viewpoint (`anchor:forks`) arrives after **261 m and 42.8 s**. The straight line is 826 m, and the same ride at 390×780 is 1,040 m and 161 s. It reproduced on a second run (`node tools/time_jaunts.mjs --modes recommended --viewport 1280x800 --only boots-and-leather`), so the desktop reading of this jaunt is 3.93 min against 5.87 at the reference viewport. This looks like a travel-controller question, not a property of the route: an anchor ride that ends early on desktop. It was not chased in this content PR. Filed here rather than as a new line because the queue is over its ceiling. Whoever takes T-2041's remaining pieces or the travel controller next should pick it up.
