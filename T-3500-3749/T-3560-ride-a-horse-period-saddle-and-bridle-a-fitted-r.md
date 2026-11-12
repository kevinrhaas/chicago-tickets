---
id: T-3560
title: Ride a horse: period saddle and bridle, a fitted rider at walk and trot, and mount, steer and dismount by keyboard and touch
state: open
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-11-12
closed: null
pr: null
claimed_by: null
blocked_on: null
needs_bake: true
closed_at: null
claimed_run: null
claimed_at: null
decision: null
decision_answer: null
---

Ride a horse: period saddle and bridle, a fitted rider at walk and trot, and mount, steer and dismount by keyboard and touch.

## Why this ticket (owner, 2026-11-12)

Kevin asked for the people, horse and carriage tickets to be consolidated into a few that are faster to finish (thread "Consolidate ticket queue"). This ticket is the riding work, last in the horse band. It replaces **T-2802** (riding saddles, bridles and gear), **T-2804** (riders and drivers fitted to horses and vehicles) and **T-2805** (mount, ride, steer and dismount), which are withdrawn into it.

## Already done on dev — reuse it, don't rebuild it

- Seated drivers with their life layer and livery (#1723, #1733, #1739); the draft tack (`draft-hitch.js`). Mounted riders do not exist yet.
- The horse and its walk (T-3559 finishes the trot; take this after it).

## What is left

**Acceptance:** (the definition of done, never weakened to pass)

- [ ] A period riding saddle, bridle and stirrups fitted to the existing horse, with eligibility by year kept apart (1812, 1835, 1904).
- [ ] A portable-human rider seated in the saddle, feet in the stirrups and hands on the reins, moving with the horse at walk and trot without clipping.
- [ ] The visitor mounts, rides, steers and dismounts by keyboard and touch, with safe mount and dismount spots, reduced motion respected, and no stranded camera on reload or a year switch.
- [ ] Desktop and phone (390×780) clip in a real scene, with frame cost.
