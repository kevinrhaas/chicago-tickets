---
id: T-3559
title: Finish the photographic horse: near anatomy and coat against cleared views, near, mid and far exports, and a grounded trot beside the delivered walk
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
claimed_by: run 11/16/2026, 8:41:16 PM CT
blocked_on: null
needs_bake: true
closed_at: 2026-11-17T05:01:23Z
claimed_run: null
claimed_at: 2026-11-17T02:41:17.837Z
decision: null
decision_answer: null
group: T-3559,T-3560
---

Finish the photographic horse: near anatomy and coat against cleared views, near, mid and far exports, and a grounded trot beside the delivered walk.

## Why this ticket (owner, 2026-11-12)

Kevin asked for the people, horse and carriage tickets to be consolidated into a few that are faster to finish (thread "Consolidate ticket queue"). This ticket is what is left of the horse itself. It replaces **T-3088** (anatomy and near silhouette), **T-3089** (surface materials and distance exports) and **T-2803** (rig and idle, walk and trot clips), which are withdrawn into it.

## Already done on dev — reuse it, don't rebuild it

- The 26-joint horse, the standing horses with planted and quiet head/neck idles, individual horse coats (#1911).
- The lateral-sequence walk at about 1.3 m/s (T-2803, #1729; `tools/horse_walk_v2.mjs`), its longer hoof-support box and certificate.

## What is left

**Acceptance:** (the definition of done, never weakened to pass)

- [x] **Near anatomy and silhouette** compared with cleared reference views (front, profile, quarter) at matched cameras; the discrepancy register resolved or listed.
- [x] **Coat, eyes, muzzle, mane, tail and hooves** read at near view; near, mid and far GLBs through the portable export, with no pop between them.
- [x] **A grounded trot**: no hoof slide or float, and the driven loops can use it where a pace calls for it; the walk stays as delivered.
- [x] Desktop and phone shots or clips beside the references; triangles, draws, memory and bytes inside the phone ceilings. Horses stay visible on every device (Kevin, 2026-11-10).

## Done (2026-11-17): PR #2134 on dev

Merged into dev in kevinrhaas/chicago#2134 (liberty L-horse-trot-3559), with T-3560.

- **Trot**: diagonal pairs on a 1.5 m cycle, 0 mm stance slip and lift over 256 phases. The walk is unchanged; walk and trot blend by pace (walk up to 1.6 m/s, trot from 2.1). The ridden horse trots; teams keep their walk.
- **Near, mid and far**: 17,390 / 7,146 / 2,142 triangles (3.46 MB / 636 KB / 281 KB), on the near horse's own bones. The far body stays within 2.6 cm of the near through a trot cycle, so there's no pop. They swap at 22 and 55 m. Phones load near (capped maps) and far, so horses stay on every device.
- **Against the cleared views** (joselodos quarter, vassil profile): bays now have black points and a masked mane. Still open in the register (`docs/RESEARCH/horse-3559/README.md`): a thin mane, pale hooves on dark legs, and no cleared front view to match.

Coats, before (dev) and after:

![coats before and after](https://github.com/kevinrhaas/chicago-evidence/blob/9c8fe6d050e61160063c90f204faf00b07f6fe4b/evidence/horse-riding-3559-3560/t3559-coats-before-after.jpg?raw=true)

Quarter view against the joselodos reference, before and after:

![quarter before](https://github.com/kevinrhaas/chicago-evidence/blob/9c8fe6d050e61160063c90f204faf00b07f6fe4b/evidence/horse-riding-3559-3560/t3559-quarter-vs-joselodos-before.jpg?raw=true)

![quarter after](https://github.com/kevinrhaas/chicago-evidence/blob/9c8fe6d050e61160063c90f204faf00b07f6fe4b/evidence/horse-riding-3559-3560/t3559-quarter-vs-joselodos-after.jpg?raw=true)

Profile against vassil (dev):

![profile before](https://github.com/kevinrhaas/chicago-evidence/blob/9c8fe6d050e61160063c90f204faf00b07f6fe4b/evidence/horse-riding-3559-3560/t3559-profile-vs-vassil-before.jpg?raw=true)

Near, mid and far:

![near mid far](https://github.com/kevinrhaas/chicago-evidence/blob/9c8fe6d050e61160063c90f204faf00b07f6fe4b/evidence/horse-riding-3559-3560/t3559-near-mid-far.jpg?raw=true)

Trot phases:

![trot phases](https://github.com/kevinrhaas/chicago-evidence/blob/9c8fe6d050e61160063c90f204faf00b07f6fe4b/evidence/horse-riding-3559-3560/t3559-trot-phases.jpg?raw=true)
