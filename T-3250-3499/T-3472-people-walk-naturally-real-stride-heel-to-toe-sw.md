---
id: T-3472
title: People walk naturally: real stride, heel to toe, swinging arms and skirts
state: open
epic: META
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-11-07
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

People walk naturally: real stride, heel to toe, swinging arms and skirts.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

Kevin, 2026-11-07 (thread "Make people's walking look natural"): "their walking is not very natural please send some agents out on that to make them more natural" (e.g. Frances Glessner when followed).

Every figure walks the same baked clip (tools/human_grounded_gait.py): a mechanical flat-foot shuffle at 0.6 m/s with 0.36 m steps, straight knees through stance, no heel strike or push-off, a level pelvis, a stiff trunk, and skirts skinned to the thighs and calves so they part like trousers.

**Acceptance:**
- A runtime gait layer (renderers/web/js/human-gait.js) walks every person on foot at a real speed and stride for their height, sex, age and dress (about 1.2-1.4 m/s, 0.6-0.75 m steps), heel strike to toe-off, knees flexing through loading and swing, the stance foot planted in the world (no slide, no sink), the pelvis bobbing, swaying, rotating and tipping, with a closing step when they stop.
- Arms swing opposite the legs in time with the gait, elbows soft, the chest counter-rotating against the pelvis.
- Women's skirts swing as one bell, pushed by the leading knee, never parting around the legs.
- Bounded by published gait reference (cited in docs/LIBERTIES.md); liberty recorded.
- Gate test (feet planted, no penetration, joint ranges); desktop and phone stills of a walk, before and after.
