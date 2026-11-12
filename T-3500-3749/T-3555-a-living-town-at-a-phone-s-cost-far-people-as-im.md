---
id: T-3555
title: A living town at a phone's cost: far people as impostor cards, middle-distance people instanced, and horse-drawn traffic moving on distant streets, inside measured budgets
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

A living town at a phone's cost: far people as impostor cards, middle-distance people instanced, and horse-drawn traffic moving on distant streets, inside measured budgets.

## Why this ticket (owner, 2026-11-12)

Kevin asked for the people, horse and carriage tickets to be consolidated into a few that are faster to finish (thread "Consolidate ticket queue"). This ticket joins the crowd and traffic work, which share one budget. It replaces **T-1792** (scale portable humans: LOD, culling, budgets) and **T-2796** (horse-drawn traffic on distant streets), which are withdrawn into it.

Standing rule (Kevin, 2026-11-10): every device keeps the living town. People, horses, carriages and wagons are a core feature and are never dropped at lower settings, on phones too; lower resolution or blur instead.

## Already done on dev — reuse it, don't rebuild it

- The phone people memory pool (T-3408), LOD parking (T-3439), phones keeping people and teams at Light (T-3542, #1930), integrated-GPU desktops at Balanced (T-3537, #1923).
- The 1812 town and gathering (226 drawn, 520 asked for at their doors; #1869, #1877), the Prairie Avenue cast (T-3546..T-3550), and the drawn-sample rule (Kevin, 2026-11-08: "card all, draw a sample").
- Driven loops: Hans's brougham in 1904, the 1812 wagons on their roads (T-3497), Otis's wagon in 1835, the waiting Glessner team.

## What is left

**Acceptance:** (the definition of done, never weakened to pass)

- [ ] **Three distance tiers for people**: full skinned, draped figures only near the camera; middle-distance people as instanced animated meshes sharing a body; far people as impostor cards from one shared atlas. No visible pop at the tier boundaries.
- [ ] **Distant traffic**: a capped number of horse-drawn vehicles moving on roads (not sidewalks) beyond the near loops, in each year that has roads for them, using the same tiers and stopping for crossings and obstructions.
- [ ] Measured on Full, Balanced and Light, desktop and phone: frame time, draw calls, triangles, animation CPU, memory, shipped bytes. The budgets written down for the next population work.
- [ ] Before and after from the same street stand on desktop and phone, with more people and traffic visible than before at the same or lower cost.
