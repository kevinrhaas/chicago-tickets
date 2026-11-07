---
id: T-3471
title: Follow trails right behind the person and keeps out of walls
state: done
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-07
closed: 2026-11-07
pr: 1844
claimed_by: run 11/7/2026, 12:10:09 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-11-07T19:56:49Z
claimed_run: null
claimed_at: 2026-11-07T18:10:10.944Z
decision: null
decision_answer: null
---

Kevin, 2026-11-07: "when i follow someone like frances, i get stuck on walls, maybe when we follow we should go right behind them by default instead of along side?" (screenshot: Following Frances M. Glessner by 1800 Prairie, the eye pressed into the granite wall).

Follow (follow.js, T-3404) stands 4 m to one side of the person; by houses, walls and fences that stand is inside a wall, the walker presses against it and the eye looks at the person through the stone.

**Acceptance:**
- Follow stands right behind the person by default (behind their way of travel; behind their back when they stand), for every person in every year (1812, 1835, 1904 on foot; drivers behind and just off their carriage).
- When a wall, fence or house is in the way the stand pulls in toward the person (or swings round them) to the farthest point with a clear line to them; never inside a wall.
- A follower held against a wall finds its way (along the person's own trail) or is set down at the stand; it never stays pressed on a wall looking through it.
- Gate case in tools/test_person_interaction.mjs; phone and desktop browser check.
