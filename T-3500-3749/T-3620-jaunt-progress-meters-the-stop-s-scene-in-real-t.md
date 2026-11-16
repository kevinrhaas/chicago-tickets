---
id: T-3620
title: Jaunt progress meters: the stop's scene in real time and the whole jaunt
state: done
epic: META
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-11-16
closed: 2026-11-16
pr: 2120
claimed_by: run 11/16/2026, 12:15:38 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-11-16T20:41:19Z
claimed_run: null
claimed_at: 2026-11-16T18:15:39.872Z
decision: null
decision_answer: null
---

Jaunt progress meters: the stop's scene in real time and the whole jaunt.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## Completion (2026-11-16, PR #2120 into dev)

A hairline meter on the jaunt panel: one segment a stop, those behind full, the current one filling in real time with its scene (the voice as heard, else the reading time, and any stage to its last beat), the scene's time left beside it; the same line along the collapsed bar. The PR also makes narration.js import nothing again, which the dev voicing run needs (#2118's run failed on it). Gate green on CI (8 of 8); smoke part 15 passed at desktop and phone width.

Before and after:

<img src="https://github.com/kevinrhaas/chicago-evidence/blob/a4a8a80f290bfa287d35d653d8d62abe606c3f39/evidence/T3620-jaunt-meter/desktop-before-first-stop.jpg?raw=true" width="420"> <img src="https://github.com/kevinrhaas/chicago-evidence/blob/a4a8a80f290bfa287d35d653d8d62abe606c3f39/evidence/T3620-jaunt-meter/desktop-m2-stop1.jpg?raw=true" width="420">

Stop 2 filling, and the collapsed bar on a phone:

<img src="https://github.com/kevinrhaas/chicago-evidence/blob/a4a8a80f290bfa287d35d653d8d62abe606c3f39/evidence/T3620-jaunt-meter/desktop-m5-stop2.jpg?raw=true" width="420"> <img src="https://github.com/kevinrhaas/chicago-evidence/blob/a4a8a80f290bfa287d35d653d8d62abe606c3f39/evidence/T3620-jaunt-meter/phone-m3-collapsed.jpg?raw=true" width="200">
