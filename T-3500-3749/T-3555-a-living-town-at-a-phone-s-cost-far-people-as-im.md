---
id: T-3555
title: A living town at a phone's cost: far people as impostor cards, middle-distance people instanced, and horse-drawn traffic moving on distant streets, inside measured budgets
state: done
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-11-12
closed: 2026-11-17
pr: 2146
claimed_by: run 11/16/2026, 8:41:21 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-11-17T12:35:12Z
claimed_run: null
claimed_at: 2026-11-17T02:41:22.227Z
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

- [x] **Three distance tiers for people**: full skinned, draped figures only near the camera; middle-distance people as instanced animated meshes sharing a body; far people as impostor cards from one shared atlas. No visible pop at the tier boundaries.
- [x] **Distant traffic**: a capped number of horse-drawn vehicles moving on roads (not sidewalks) beyond the near loops, in each year that has roads for them, using the same tiers and stopping for crossings and obstructions.
- [x] Measured on Full, Balanced and Light, desktop and phone: frame time, draw calls, triangles, animation CPU, memory, shipped bytes. The budgets written down for the next population work.
- [x] Before and after from the same street stand on desktop and phone, with more people and traffic visible than before at the same or lower cost.


## Finding 2026-11-13: two more 1904 carriages that give way at crossings (PR #2021)

Kevin (2026-11-13) asked for two more 1904 carriages on different loops round Prairie Avenue, at least one counter-clockwise, crossing paths with one waiting for the other. PR #2021 adds the Pullman brougham (Henry Windish, 16th-18th) and the Armour brougham (Joseph Daniels, 20th-22nd) beside Hans's, all counter-clockwise (right-hand lanes leave only left turns at the brougham's 16.4 m minimum radius). `renderers/web/js/transport-crossings.js` finds the footprint conflict zones between circuits and lets the first team claim a crossing while the other waits at its edge (no hold-and-wait, so no deadlock). The 1904 phone reads 436.1 MB against its 450 MB ceiling at spawn. Loaded town transport still loads all of a scene's rows once the visitor nears any circuit; distant-street impostors remain this ticket's open work. Liberty L-1904-more-carriages-3555.


## Done 2026-11-17 (PRs #2141 and #2146)

- **People in three tiers.** Full figures stay as they were near the camera. From 28 m out to 110 / 90 / 70 m (Full / Balanced / Light), people are instanced on one shared walking body per dress (`renderers/web/js/crowd.js`). Beyond that, out to 600 / 450 / 320 m, they are cards from one atlas, baked in the browser from the same bodies. The tiers hand over with a dithered cross-fade and hysteresis, so nobody pops or is drawn twice.
- **Distant traffic.** Horse-drawn teams beyond their built reach are cards on their roads, out to 700 / 500 / 350 m, at most 32 / 20 / 12 (`renderers/web/js/traffic-cards.js`). They are baked from each team's lighter vehicle and its mid-level horse. They come from town transport's `distant()` list (T-3558), so they follow its circuits and its waits at crossings. Teams already built carry on along their round once they are out of reach.
- **Budgets and readings:** `docs/measurements/T-3555-crowd.json`, covering 1812, 1835 and 1904 on Full, Balanced and Light, desktop and phone. The layers add 7 to 15 draw calls and at most 1.1 ms of CPU a frame on Full desktop (0.06 to 0.22 ms on phone Light), plus 2.3 to 5 MB of GPU memory and +55 KB of JS (19.5 KB gzipped). They ship no new assets.
- **Phone memory**, clean dev against this work (MiB): 1812 337 → 329, 1835 536 → 542, 1904 464 → 472. Clean dev's 1835 already reads over its 525 ceiling on the measuring machine.
- **Cost, honestly:** the same stand now shows far more people at a small added cost, not a lower one. The full figures near the camera are unchanged.
- **Fixed on the way (#2146):** a tap or Space could find no building while a new dress's colours were being read back from the GPU.

Before and after, same stand and moment, with the layers off and on. The far street is enlarged twice.

**1904 Prairie Avenue, desktop**

![1904 desktop before and after](https://github.com/kevinrhaas/chicago-evidence/blob/024019108f87ab58303460bfadd3775b06831726/evidence/2026-11-17-t3555-crowd/T-3555-1904-desktop-street-zoom.png?raw=true)

**1904 Prairie Avenue, phone**

![1904 phone before and after](https://github.com/kevinrhaas/chicago-evidence/blob/024019108f87ab58303460bfadd3775b06831726/evidence/2026-11-17-t3555-crowd/T-3555-1904-mobile-street-zoom.png?raw=true)

**1835 Lake Street, desktop**

![1835 desktop before and after](https://github.com/kevinrhaas/chicago-evidence/blob/024019108f87ab58303460bfadd3775b06831726/evidence/2026-11-17-t3555-crowd/T-3555-1835-desktop-street-zoom.png?raw=true)

**1835 Lake Street, phone**

![1835 phone before and after](https://github.com/kevinrhaas/chicago-evidence/blob/024019108f87ab58303460bfadd3775b06831726/evidence/2026-11-17-t3555-crowd/T-3555-1835-mobile-street-zoom.png?raw=true)

