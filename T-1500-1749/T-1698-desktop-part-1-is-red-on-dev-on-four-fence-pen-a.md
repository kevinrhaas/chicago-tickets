---
id: T-1698
title: Desktop part 1 is red on dev on four fence, pen and dooryard visibility checks, and the smoke record still says PASS
state: withdrawn
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-27
closed: 2026-10-03
pr: null
claimed_by: null
blocked_on: "obsolete: Its four fence/pen checks pass: desktop parts 1-6 294/0 on 2026-10-01."
needs_bake: false
closed_at: 2026-10-03T04:52:33.000Z
claimed_run: null
claimed_at: null
decision: null
decision_answer: null
---

Desktop part 1 is red on dev on four fence, pen and dooryard visibility checks, and the smoke record still says PASS.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

**Measured twice on 2026-09-27, on a steward runner with 4 cpu, both readings at
`SMOKE_VIEWPORT=desktop SMOKE_STAGE=1 node tools/smoke_renderer.mjs --published`:**

| tree | result |
|---|---|
| the T-1681 re-cut branch (dev d8b5137c + the Lake/Clark re-family) | 76 passed, 4 failed, 5 m 15 s |
| clean `origin/dev` at d8b5137c, published fresh | 76 passed, 4 failed, 5 m 19 s |

The same four, in the same order, on both:

* `desktop 1280x800: the yard fence reaches the screen from inside the yard`
* `desktop 1280x800: the pen reaches the screen from inside the pen`
* `desktop 1280x800: aiming at the pen's fence still opens the pen's card`
* `desktop 1280x800: the garden fence reaches the screen from the dooryard`

**So the red is dev's own and not the diff's** — which is the whole reason for taking
the second reading, and the reason this is filed rather than left for the next branch
to rediscover as its own fault. The re-cut touched `data/enclosures/*`,
`data/flora/plantings/*` and `data/frontage/town_street_edge.json`, so "it might be
mine" was a live possibility until dev was read on its own.

**The record is the second half of the finding.** `tools/dev-smoke-state.mjs ask
--viewport desktop --stage 1` answers **PASS**, dated `2026-09-27T19:28:45.339Z`, on a
tree that is no longer dev's. A run that asks the record before spending a leg is told
this part is good, spends the leg anyway, and reads its own four reds as a regression
it caused. That is exactly the waste `ask` exists to prevent, so the fix has two parts:
find and fix whatever took these four red, and file the readings above so the record
stops disagreeing with the tree.

**Not investigated here**, because this run's budget went on the re-cut it was taking
the reading for: which landing took them red. The candidates visible in the window are
the enclosure, dooryard and frontage layers, which several 2026-09-27 landings
re-derived. `dev` was green at this part at 19:28Z and red by 23:50Z.

## Queue cleanup 2026-10-03 (owner: "clean out any tickets that … no longer need to be there or are obsolete")

**Withdrawn as obsolete.** Its four fence/pen checks pass: desktop parts 1-6 294/0 on 2026-10-01.
