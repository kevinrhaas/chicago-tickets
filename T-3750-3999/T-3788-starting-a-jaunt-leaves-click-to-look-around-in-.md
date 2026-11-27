---
id: T-3788
title: Starting a jaunt leaves Click to look around in front of the visitor: hide the look tag for the whole jaunt
state: review
epic: META
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: null
opened: 2026-11-26
closed: null
pr: 2392
claimed_by: run 11/26/2026, 11:21:23 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-27T05:21:24.577Z
decision: null
decision_answer: null
---

Starting a jaunt leaves Click to look around in front of the visitor: hide the look tag for the whole jaunt.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
On a computer, the CLICK TO LOOK AROUND tag never shows while a Jaunt is under way; it comes back after the Jaunt only for a visitor who has still not clicked the scene. Phones never showed it.

## Done — PR #2392, merged into dev as d8dab9277

The gesture gate's `lookTagVisible` takes `onJaunt`, set from the Jaunt runtime's render (a Jaunt loaded and not parked at Home). `tools/test_arrival.mjs` holds the tag away on a Jaunt and back after it.

Desktop, 1280×800, The Glessner Household started from Home on first entry (before: production; after: the PR):

<img src="https://github.com/kevinrhaas/chicago-evidence/blob/b8a8051c2d618c29f04ebbd5516f8603a0e6e7ed/evidence/T-3788/desktop-jaunt-start-before-after.jpg?raw=true" width="900">

Phone, 390×780 (no tag before or after):

<img src="https://github.com/kevinrhaas/chicago-evidence/blob/b8a8051c2d618c29f04ebbd5516f8603a0e6e7ed/evidence/T-3788/phone-jaunt-start-before-after.jpg?raw=true" width="640">
