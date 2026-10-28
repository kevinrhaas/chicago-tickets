---
id: T-3225
title: 1904 utility poles and wires pass through alley coach houses
state: claimed
epic: META
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-10-27
closed: null
pr: null
claimed_by: run 10/27/2026, 10:51:50 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-28T03:51:51.685Z
decision: null
decision_answer: null
---

1904 utility poles and wires pass through alley coach houses.

The owner, 2026-10-28 (project thread, dev preview, 1904, looking up an alley): *"some of the electrical poles and lines are intersecting with buildings"*. His screenshot shows a wooden pole with its crossarm against the gable of a rock-faced stone coach house and the wire spans running through the building's roof edge and wall. T-3202 (PR 1388) laid the poles in tools/lay_prairie_1904_street_furniture.py and tested them only against elm trunks, lamps, hydrants and crossings, never against the 1904 structures.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

1. No utility pole, crossarm or wire span in data/street_furniture/1904.json intersects any 1904 structure (house, coach house, stable, fence), tested on the structures' baked models (plan raster with heights), the wires as sagging 3-D segments between crossarm pins. A wire passing over a low fence is fine; through a wall or roof is not.
2. A pole that stood in or against a structure is moved along its alley or into it (or dropped), and a span that crossed a building is re-routed or dropped; the tool says which.
3. `lay_prairie_1904_street_furniture.py --check` fails, naming the pole or span and the structure, whenever anything intersects, and a `--self-test` proves that by breaking it; both run in tools/check.sh.
4. The liberty L-prairie-utility-poles-3202 states the clearance rule.
