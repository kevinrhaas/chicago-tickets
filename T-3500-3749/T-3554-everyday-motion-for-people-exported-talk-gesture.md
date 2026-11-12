---
id: T-3554
title: Everyday motion for people: exported talk, gesture, carry and work clips on the shared rig, sweeping and leaning with their props, and contact shadows under feet and hat brims
state: claimed
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-11-12
closed: null
pr: null
claimed_by: run 11/12/2026, 11:41:34 AM CT
blocked_on: null
needs_bake: true
closed_at: null
claimed_run: null
claimed_at: 2026-11-12T17:41:35.930Z
decision: null
decision_answer: null
---

Everyday motion for people: exported talk, gesture, carry and work clips on the shared rig, sweeping and leaning with their props, and contact shadows under feet and hat brims.

## Why this ticket (owner, 2026-11-12)

Kevin asked for the people, horse and carriage tickets to be consolidated into a few that are faster to finish (thread "Consolidate ticket queue"). This ticket is what is left of the motion work. It replaces **T-1790** (animation library), **T-3420** (pairs, sweeping, carrying, leaning) and **T-3416** (contact shadows), which are withdrawn into it.

## Already done on dev — reuse it, don't rebuild it

- Idle and walk on all 248 exports; seated driving and its life layer (#1649, #1693, #1697, #1723); natural idle.
- The life layer on people on foot (human-life.js, T-3402, #1743) and arms (human-actions.js, T-3419, #1752): greeting, stance changes, arm swing.
- Talking hands (T-3490), carrying by the hand (T-3481), talks that gather and part and work between them in all three years (T-3505 #1878, T-3516), the gait work (T-3472).

## What is left

**Acceptance:** (the definition of done, never weakened to pass)

- [ ] **Exported clips**: a talk loop, a point or gesture, a carry or hold and one simple period work motion, authored on the shared rig and exported through the portable path with clip metadata (duration, looping, root motion, LOD, tags), so behaviour picks clips by meaning. An actor goes idle → walk → idle → gesture without a reload.
- [ ] **Sweeping and leaning**: a broom and a lean spot (a post, a door frame, a fence) used by people whose day already has that kind of job; feet planted, the prop held in the hand.
- [ ] **Contact shadows and occlusion**: a soft contact shadow under feet, a shade under hat brims, and darkening where clothes overlap, cheap enough for phones.
- [ ] CPU cost measured for one close person and a small group; which features drop at lower LODs written down.
- [ ] Desktop and phone (390×780) shots or short clips in the real scenes, before and after. No person is dropped at lower settings to pay for it.
