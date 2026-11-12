---
id: T-3558
title: Finish the photographic wagons and Brougham: the farm-box master qualified, the covered wagons upgraded but kept distinct, and the Brougham matched to its 1893 plate and qualified in town
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
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: null
decision: null
decision_answer: null
---

Finish the photographic wagons and Brougham: the farm-box master qualified, the covered wagons upgraded but kept distinct, and the Brougham matched to its 1893 plate and qualified in town.

## Why this ticket (owner, 2026-11-12)

Kevin asked for the people, horse and carriage tickets to be consolidated into a few that are faster to finish (thread "Consolidate ticket queue"). This ticket is what is left of the vehicle models. It replaces **T-2793** (articulated wagon master), **T-2980** (covered wagons), **T-3084** (Brougham to the 1893 catalogue) and **T-3085** (Brougham qualified in town), which are withdrawn into it.

## Already done on dev — reuse it, don't rebuild it

- The licensed farm-box master and its near/mid/far tooling (#1340), the timber wagons, distinct canvas and the Brougham (#1175), occupied loops and controls (#1649, #1697), the 1812 driven wagons (T-3497).
- Brougham lamp refinement (T-3083); draft PR #1335's coachwork and glass source work is on its branch, not on dev.

## What is left

**Acceptance:** (the definition of done, never weakened to pass)

- [ ] **Farm box**: `renderers/web/transport/farm-box-master/farm-box.json` loses `photographic_acceptance: false` honestly: matched-view renders beside its cleared references, ground and tree clearance, LODs and phone/desktop cost recorded.
- [ ] **Covered wagons**: a few older covered wagons replaced by better ones, each keeping its own finish, canvas ageing, seed and place, so no two look like clones.
- [ ] **Brougham**: body, wheels, steps, doors, seats and glass matched to the 1893 Studebaker plate at matched cameras, with a discrepancy register; then exported near/mid/far and loaded in the real 1904 scene with its seats, doors and anchors intact for the ride (T-3557).
- [ ] Before and after shots, desktop and phone, for each; triangles, draws, memory and bytes inside the phone ceilings.
