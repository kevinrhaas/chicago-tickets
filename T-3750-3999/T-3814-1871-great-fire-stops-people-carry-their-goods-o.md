---
id: T-3814
title: 1871 Great Fire stops: people carry their goods out (bundles, trunks dragged on cords, bird cages, feather beds, a sick person in a doubled mattress) and wagons load at the stores, from the accounts
state: review
epic: META
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-11-27
closed: null
pr: 2419
claimed_by: run 11/27/2026, 3:19:57 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-27T21:19:58.100Z
decision: null
decision_answer: null
---

Kevin, 2026-11-27 (thread "Bring 1871 fire-night crowds and scenes to life"): *"The other thing in general for 1871 would there have been more people crowds running around existing buildings carrying things or dumping things into wagons or a runaway horse with a wagon on fire or other descriptions or likely actions and scenarios or mini scenes to integrate into jaunts and walk arounds to make it more realistic, you will need to be clever in rendering crowds of people so you don't blow rendering budgets you may have to start a crowd development stream along side this and do some analysis research on crowd dynamics and the best way to render groups of people who may be running or screaming or etc whatever was appropriate"*

Research: `docs/RESEARCH/fire-night-scenes-3814/README.md` (the scenes the accounts describe, by place and hour, with page locators; and the crowd dynamics and rendering analysis). Sister tickets T-3814..T-3817; the streetscape tickets T-3802..T-3807 are another thread's and are not touched.

**What:** at the Great Fire stops, the staged people do what the accounts say people did at that hour and place, instead of only watching or hurrying off empty-handed.

- A castmate may `carry` a load (data/jaunts/schema.json): a bundle on the shoulder, a trunk dragged on a cord behind them, a bird cage or a basket in the hand, a feather bed on the back; the arm holds it (human-actions.js), and the thing is drawn from stage-props.js.
- Two castmates may bear a sick person "half concealed in a mattress doubled up" between them (Andreas p. 734), as the 1812 bier is borne.
- Stage teams may carry a `load` on the bed (trunks, bundles, boxes, a bureau), and castmates carry goods from a door to a wagon: Field, Leiter and Co.'s men "carrying goods out of the lower floor into wagons" at stop 10, which the stop's words say and the scene does not show today.
- Each stop's cast rebuilt in docs/RESEARCH/jaunt-great-fire-3691/build.py, the grade-band and 18+ versions re-derived, and tools/check_fire_jaunt.mjs taught the new state.

**Acceptance:** at every stop where the words or the accounts put people with goods, they are there with them, desktop and phone (light keeps fewer, never none); stop 10 shows wagons being loaded; before/after pictures; no light-tier ceiling breached; liberties recorded (the props' make is reconstructed).
