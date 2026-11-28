---
id: T-3816
title: 1871 fire-night crowd stream: hundreds fleeing, carrying and watching in the streets round the fire front, on the instanced crowd at a phone's cost (running clip, flow along the streets, counter-currents)
state: open
epic: META
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-11-27
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

Kevin, 2026-11-27 (thread "Bring 1871 fire-night crowds and scenes to life"): *"The other thing in general for 1871 would there have been more people crowds running around existing buildings carrying things or dumping things into wagons or a runaway horse with a wagon on fire or other descriptions or likely actions and scenarios or mini scenes to integrate into jaunts and walk arounds to make it more realistic, you will need to be clever in rendering crowds of people so you don't blow rendering budgets you may have to start a crowd development stream along side this and do some analysis research on crowd dynamics and the best way to render groups of people who may be running or screaming or etc whatever was appropriate"*

Research: `docs/RESEARCH/fire-night-scenes-3814/README.md` (the scenes the accounts describe, by place and hour, with page locators; and the crowd dynamics and rendering analysis). Sister tickets T-3814..T-3817; the streetscape tickets T-3802..T-3807 are another thread's and are not touched.

**What:** the crowd development stream. The staged figures are whole people (a few each stop); the night's streets held thousands. Draw the many on the crowd layer that already draws the far town (crowd.js: one instanced body per dress animated from a vertex-animation texture, impostor cards beyond), fed by a fire-night source instead of the people's day:

- people coming away from the front along the streets (a flow along the street graph away from the fire, read from fire-map.js), carrying goods (a carried pose and its load baked into the shared body), and the "counter-currents" of sightseers going toward it (Goodspeed 1871: "a continual stream of curious people ... crowding eagerly forward ... The counter-currents, as they met, caused frightful mishaps");
- a running clip in the animation texture beside the walk, so a far runner runs;
- density and speed from the crowd literature (the speed-density relation; lanes in counterflow; jams at bridges and the LaSalle Street tunnel);
- caps by tier, measured on the light ceiling, the UHD 630 class and a phone.

**Acceptance:** at every Great Fire stop the streets in view carry the night's crowd to the far distance, moving the right way for the hour; the light tier stays in its ceiling; measured row in docs/measurements; before/after pictures desktop and phone.

**Free walk too (Kevin, 2026-11-27, decision card "Should the 1871 free walk also be able to show the fire night?": "Add a fire-night clock to free walk"):** the 1871 free walk gains a fire-night clock (a choice of hour from the barn at about nine on Sunday evening through Tuesday morning); set to one, the city burns as the jaunt's fire map has it at that hour, and this crowd fills the streets round the front. Left off, the free walk stays the pre-fire city of 8 October as now. Acceptance adds: the clock in the free walk, the city and crowd matching the hour picked, before/after pictures.

**Scenes repeated across the city, looping (Kevin, 2026-11-28: *"Yes you can do things like this on a loop through the blocks, and duplicate those scenes as appropriate in the city"*):** the close-up mini-scenes T-3814 built for the jaunt stops (goods carried on the shoulder, in the hand or dragged on a cord; the sick carried on a mattress; men loading a wagon at a store door that then drives off; goods set down in squares and open ground) are also placed block by block through the burning city, in the free walk's fire night as well as the jaunt. Each one loops on its own short cycle, and which blocks get which scene follows the hour: loading at stores and houses ahead of the front, flight away from it, and goods piled in open ground behind the people. They draw as whole near figures only close to the visitor and drop to this ticket's crowd layer further out, inside the same tier caps. Acceptance adds: walking several blocks in the fire night passes repeated, varied scenes of this kind, with no two neighbouring blocks playing the same one in step.
