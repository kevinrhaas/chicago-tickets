---
id: T-2059
title: The mobile flora heartbeat went from 140 to 340-390 ms with T-2015's leaf-scale trees, past the 250 ms check
state: claimed
epic: RENDERING
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-10-03
closed: null
pr: null
claimed_by: run 10/8/2026, 12:44:01 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37733590223
claimed_at: 2026-10-08T05:44:01.839Z
decision: null
decision_answer: null
---

The mobile flora heartbeat went from 140 to 340-390 ms with T-2015's leaf-scale trees, past the 250 ms check.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 202 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> T-1272's acceptance requires every unmet budget to leave as a named successor, and no open ticket owns this: T-2047 measured it

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## Found by T-2047 (2026-10-04), the measurement this ticket starts from

`node tools/measure_boot_phases.mjs --published --quick --json` (mobile 390×780, light,
cold and warm), each tree published by its own `publish.sh` and measured by dev's tool
with `--root`, on one steward runner:

| tree | flora max paint gap, cold / warm | flora phase, cold |
|---|---|---|
| `b06a063a^` (before T-2014) | 136 / 167 ms | 6.19 s |
| `d90c7ed2^` (before T-2015, after T-2014) | 143 / 137 ms | 6.47 s |
| `d90c7ed2` (T-2015, #333) | **339 / 388 ms** | 7.06 s |
| dev `cb56e2e4` | 320 / 356 ms | 7.04 s |

T-1246's `--check` holds the mobile light gap to **≤ 250 ms**; it fails on dev and passed
the commit before T-2015. The 12-cell run shows the same on every cell (320-427 ms).
Not the arrival section: `c2dd2ea1`, the tree before it, reads 140 ms, and `49d0a226`,
with the arrival in it, 124 ms.
