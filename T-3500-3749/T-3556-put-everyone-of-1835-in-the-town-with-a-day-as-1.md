---
id: T-3556
title: Put everyone of 1835 in the town with a day, as 1812 and 1904 have: the carded townspeople drawn at their homes and work, Mark Beaubien at the Sauganash among them, and the rest asked for at their doors
state: open
epic: TOWN
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
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: null
decision: null
decision_answer: null
---

Put everyone of 1835 in the town with a day, as 1812 and 1904 have: the carded townspeople drawn at their homes and work, Mark Beaubien at the Sauganash among them, and the rest asked for at their doors.

## Why this ticket (owner, 2026-11-12)

Kevin, thread "Consolidate ticket queue": "things like mark beaubien there are lots of tickets for just him and he should be part of filling out all the people in 1835 and giving them schedules just like we did in 1904 and 1812 but not a dedicated ticket for him at this point". This ticket replaces the three Mark Beaubien pieces **T-2673** (evidence sheet and Blender master), **T-2674** (browser actor) and **T-2675** (inspected in the 1835 scene), which are withdrawn into it. Their parent T-1791 keeps the read-first list for Mark.

## How 1812 and 1904 did it — follow the same path

- **1812**: every carded person in town (T-3461..T-3467, #1869; the gathering T-3500, #1877). `docs/RESEARCH/people-1812-town/{place_town,cards,looks}.py` write the drawn instances; `human-days.js` plays each `behaviour.day` (indoors at a building, or out at a job or a talk that gathers and parts); every door with someone inside is an Interact thing ("Ask for <name>"); people not drawn go in `data/humans/inside_1812.json`, asked for at their door. Doors from `tools/derive_doors_1812.py`.
- **1904**: the Prairie Avenue cast (T-3546..T-3550): `tools/prairie_people.py` writes `data/humans/prairie_1904.json` and `inside_1904.json`, seasonal reconstructed days, existing dresses reused by role.
- **1835 today**: only four people are drawn (Peck, Mary Flynn, Patrick Mahoney, Otis Bardwell; days in `docs/RESEARCH/people-days-1835-1904/days.py`, doors in `data/humans/doors_1835.json`). The housing deal already seats the town's households and boarders under roofs (T-3494, `tools/house_the_present_1835.py`), and the 1835 merchant and labourer dresses exist (#1824).

## What is left

**Acceptance:** (the definition of done, never weakened to pass)

- [ ] **Every carded 1835 person has a day** (1 July 1835): where they sleep, eat and work by the hour, from their card's trade, household and building; hours reconstructed and recorded as a liberty, people and trades their records'. Children walk or play; boarders live where the housing deal seats them.
- [ ] **A drawn sample in the street on every device**, as 1812's "card all, draw a sample": people at their work, talks that gather and part, breaks indoors. The rest listed at their doors in an `inside_1835.json`, asked for by name.
- [ ] **Mark Beaubien** drawn at the Sauganash with his tavern-keeper's day: a dated likeness sheet first (attested likeness, period analogy and reconstruction kept apart; a late-life portrait is not turned into an exact 1835 face), assembled from the existing kit, selectable and handing off to his card.
- [ ] Native and Métis people of 1835 follow the standing rulings (T-2672; Kevin: people must not look identical, reconstructed names and histories are fine). The August gathering stays out of 1 July 1835.
- [ ] Reuse existing dresses and figure GLBs by role; mind the site size budget (see 1812's levers in #1869). Desktop 1280×800 and phone 390×780 shots of a busy street, a door "Ask for" list and Mark at the Sauganash. Phones keep people, horses and wagons (T-3542 ceilings).

One PR if it fits, as 1812's #1869 did; more if the size budget needs it.
