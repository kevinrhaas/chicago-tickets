---
id: T-3559
title: Finish the photographic horse: near anatomy and coat against cleared views, near, mid and far exports, and a grounded trot beside the delivered walk
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

Finish the photographic horse: near anatomy and coat against cleared views, near, mid and far exports, and a grounded trot beside the delivered walk.

## Why this ticket (owner, 2026-11-12)

Kevin asked for the people, horse and carriage tickets to be consolidated into a few that are faster to finish (thread "Consolidate ticket queue"). This ticket is what is left of the horse itself. It replaces **T-3088** (anatomy and near silhouette), **T-3089** (surface materials and distance exports) and **T-2803** (rig and idle, walk and trot clips), which are withdrawn into it.

## Already done on dev — reuse it, don't rebuild it

- The 26-joint horse, the standing horses with planted and quiet head/neck idles, individual horse coats (#1911).
- The lateral-sequence walk at about 1.3 m/s (T-2803, #1729; `tools/horse_walk_v2.mjs`), its longer hoof-support box and certificate.

## What is left

**Acceptance:** (the definition of done, never weakened to pass)

- [ ] **Near anatomy and silhouette** compared with cleared reference views (front, profile, quarter) at matched cameras; the discrepancy register resolved or listed.
- [ ] **Coat, eyes, muzzle, mane, tail and hooves** read at near view; near, mid and far GLBs through the portable export, with no pop between them.
- [ ] **A grounded trot**: no hoof slide or float, and the driven loops can use it where a pace calls for it; the walk stays as delivered.
- [ ] Desktop and phone shots or clips beside the references; triangles, draws, memory and bytes inside the phone ceilings. Horses stay visible on every device (Kevin, 2026-11-10).
