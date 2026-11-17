---
id: T-3560
title: Ride a horse: period saddle and bridle, a fitted rider at walk and trot, and mount, steer and dismount by keyboard and touch
state: done
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-11-12
closed: 2026-11-16
pr: 2134
claimed_by: run 11/16/2026, 8:41:24 PM CT
blocked_on: null
needs_bake: true
closed_at: 2026-11-17T05:01:23Z
claimed_run: null
claimed_at: 2026-11-17T02:41:24.979Z
decision: null
decision_answer: null
group: T-3559,T-3560
---

Ride a horse: period saddle and bridle, a fitted rider at walk and trot, and mount, steer and dismount by keyboard and touch.

## Why this ticket (owner, 2026-11-12)

Kevin asked for the people, horse and carriage tickets to be consolidated into a few that are faster to finish (thread "Consolidate ticket queue"). This ticket is the riding work, last in the horse band. It replaces **T-2802** (riding saddles, bridles and gear), **T-2804** (riders and drivers fitted to horses and vehicles) and **T-2805** (mount, ride, steer and dismount), which are withdrawn into it.

## Already done on dev — reuse it, don't rebuild it

- Seated drivers with their life layer and livery (#1723, #1733, #1739); the draft tack (`draft-hitch.js`). Mounted riders do not exist yet.
- The horse and its walk (T-3559 finishes the trot; take this after it).

## What is left

**Acceptance:** (the definition of done, never weakened to pass)

- [x] A period riding saddle, bridle and stirrups fitted to the existing horse, with eligibility by year kept apart (1812, 1835, 1904).
- [x] A portable-human rider seated in the saddle, feet in the stirrups and hands on the reins, moving with the horse at walk and trot without clipping.
- [x] The visitor mounts, rides, steers and dismounts by keyboard and touch, with safe mount and dismount spots, reduced motion respected, and no stranded camera on reload or a year switch.
- [x] Desktop and phone (390×780) clip in a real scene, with frame cost.

## Done (2026-11-17): PR #2134 on dev

Merged into dev in kevinrhaas/chicago#2134 (liberty L-riding-tack-3560), with T-3559.

A saddled horse stands near where you arrive in 1812, 1835 and 1904. Interact on it to Mount. W walks, Shift+W trots, S pulls up (hold it to back up), A/D turn. On a phone the stick does all of this. V switches between the view from behind and the view from the saddle. Get down is on the travel bar and in Interact, and sets you on clear ground beside the horse. The horse only goes where you could stand. Reduced motion keeps the saddle view level. Riding ends on Go to, Follow and flying, and nothing is saved, so a reload or a year switch starts you on your feet.

The tack is fitted to the horse's own coat. Each year has its own: 1812 a hunting-pattern saddle on a blanket with a crupper, 1835 a hunting saddle on a square cloth, 1904 a flat saddle, numnah, breastplate and double bridle. The rider is posed into the saddle every frame. `tools/test_riding.mjs` finds 0 of about 10,000 skin points per year more than 1 cm inside the horse, at 8 phases of walk and trot.

Frame cost (SwiftShader): the ride's update takes 0.66 ms a frame on phone and 3.8 ms on desktop (the desktop figure includes the rider's first build). The horse, rider and tack draw 36 meshes and 33,470 triangles. There were 0 page errors.

1835, desktop: standing, mounted, at the trot, from the saddle:

![1835 standing](https://github.com/kevinrhaas/chicago-evidence/blob/9c8fe6d050e61160063c90f204faf00b07f6fe4b/evidence/horse-riding-3559-3560/t3560-1835-desktop-0-stood.jpg?raw=true)

![1835 mounted](https://github.com/kevinrhaas/chicago-evidence/blob/9c8fe6d050e61160063c90f204faf00b07f6fe4b/evidence/horse-riding-3559-3560/t3560-1835-desktop-1-mounted.jpg?raw=true)

![1835 trot](https://github.com/kevinrhaas/chicago-evidence/blob/9c8fe6d050e61160063c90f204faf00b07f6fe4b/evidence/horse-riding-3559-3560/t3560-1835-desktop-3-trot.jpg?raw=true)

![1835 saddle view](https://github.com/kevinrhaas/chicago-evidence/blob/9c8fe6d050e61160063c90f204faf00b07f6fe4b/evidence/horse-riding-3559-3560/t3560-1835-desktop-4-saddle.jpg?raw=true)

1904, phone 390×780: standing, mounted, trotting, from the saddle, down again:

<img src="https://github.com/kevinrhaas/chicago-evidence/blob/9c8fe6d050e61160063c90f204faf00b07f6fe4b/evidence/horse-riding-3559-3560/t3560-1904-phone-0-stood.jpg?raw=true" width="180" alt="t3560-1904-phone-0-stood"> <img src="https://github.com/kevinrhaas/chicago-evidence/blob/9c8fe6d050e61160063c90f204faf00b07f6fe4b/evidence/horse-riding-3559-3560/t3560-1904-phone-1-mounted.jpg?raw=true" width="180" alt="t3560-1904-phone-1-mounted"> <img src="https://github.com/kevinrhaas/chicago-evidence/blob/9c8fe6d050e61160063c90f204faf00b07f6fe4b/evidence/horse-riding-3559-3560/t3560-1904-phone-3-trot.jpg?raw=true" width="180" alt="t3560-1904-phone-3-trot"> <img src="https://github.com/kevinrhaas/chicago-evidence/blob/9c8fe6d050e61160063c90f204faf00b07f6fe4b/evidence/horse-riding-3559-3560/t3560-1904-phone-4-saddle.jpg?raw=true" width="180" alt="t3560-1904-phone-4-saddle"> <img src="https://github.com/kevinrhaas/chicago-evidence/blob/9c8fe6d050e61160063c90f204faf00b07f6fe4b/evidence/horse-riding-3559-3560/t3560-1904-phone-5-down.jpg?raw=true" width="180" alt="t3560-1904-phone-5-down">

Tack by year, and the riders:

![tack by year](https://github.com/kevinrhaas/chicago-evidence/blob/9c8fe6d050e61160063c90f204faf00b07f6fe4b/evidence/horse-riding-3559-3560/t3560-tack-by-year.jpg?raw=true)

![riders 1904 and 1835](https://github.com/kevinrhaas/chicago-evidence/blob/9c8fe6d050e61160063c90f204faf00b07f6fe4b/evidence/horse-riding-3559-3560/t3560-riders-1904-1835.jpg?raw=true)

![rider 1812](https://github.com/kevinrhaas/chicago-evidence/blob/9c8fe6d050e61160063c90f204faf00b07f6fe4b/evidence/horse-riding-3559-3560/t3560-rider-1812-side-front.jpg?raw=true)
