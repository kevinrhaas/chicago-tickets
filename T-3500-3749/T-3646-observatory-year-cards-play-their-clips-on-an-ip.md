---
id: T-3646
title: Observatory year cards play their clips on an iPhone in Low Power Mode
state: review
epic: META
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-11-17
closed: null
pr: 2170
claimed_by: run 11/17/2026, 4:39:49 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-17T22:39:50.894Z
decision: null
decision_answer: null
---

Observatory year cards play their clips on an iPhone in Low Power Mode.

**Acceptance:** with video refused (an iPhone in Low Power Mode), each of the three year cards still plays a moving clip, on phone and desktop, in every appearance; with video allowed nothing changes.

**Cause (2026-11-17):** nothing removed the clips. Kevin's phone was in Low Power Mode (yellow battery in his screenshot), where iOS refuses every video, and clips.js kept the still on a refusal. Fix: PR #2170, a grey frame-strip reel per clip that the card steps onto a canvas when video is refused.

**Before (left, dev) and after (right, PR #2170), video refused:**

![phone moving after](https://github.com/kevinrhaas/chicago-evidence/blob/772d4ff0f2b69adb536d8bd1d98d0ea507bd30a3/evidence/T-3646-year-card-clips/low-power-phone-after.gif?raw=true)

![phone control room](https://github.com/kevinrhaas/chicago-evidence/blob/772d4ff0f2b69adb536d8bd1d98d0ea507bd30a3/evidence/T-3646-year-card-clips/pair-phone-control-room.jpg?raw=true)

![phone brass](https://github.com/kevinrhaas/chicago-evidence/blob/772d4ff0f2b69adb536d8bd1d98d0ea507bd30a3/evidence/T-3646-year-card-clips/pair-phone-brass.jpg?raw=true)

![phone retro future](https://github.com/kevinrhaas/chicago-evidence/blob/772d4ff0f2b69adb536d8bd1d98d0ea507bd30a3/evidence/T-3646-year-card-clips/pair-phone-worlds-fair.jpg?raw=true)

![phone deep space](https://github.com/kevinrhaas/chicago-evidence/blob/772d4ff0f2b69adb536d8bd1d98d0ea507bd30a3/evidence/T-3646-year-card-clips/pair-phone-deep-space.jpg?raw=true)

![desktop control room](https://github.com/kevinrhaas/chicago-evidence/blob/772d4ff0f2b69adb536d8bd1d98d0ea507bd30a3/evidence/T-3646-year-card-clips/pair-desktop-control-room.jpg?raw=true)

![desktop brass](https://github.com/kevinrhaas/chicago-evidence/blob/772d4ff0f2b69adb536d8bd1d98d0ea507bd30a3/evidence/T-3646-year-card-clips/pair-desktop-brass.jpg?raw=true)
