---
id: T-3630
title: Dev's smoke parts 8 and 9-12 are red on 'restores the frame' residuals: road aid, roughness, shadow reach and brightness aid leave a held frame changed
state: claimed
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-16
closed: null
pr: null
claimed_by: run 11/16/2026, 9:47:29 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/44011465623
claimed_at: 2026-11-17T03:47:30.187Z
decision: null
decision_answer: null
---

Dev's smoke parts 8 and 9-12 are red on 'restores the frame' residuals: road aid, roughness, shadow reach and brightness aid leave a held frame changed.

## FILED ABOVE BAND 9, BECAUSE IT BLOCKS

A follow-up goes to the foot of band 9 unless dev's gate is red on it or the build in hand cannot finish without it (owner, 2026-09-27). This one was placed above band 9 on this reason:

> dev's gate is red on it: the same residual-restore checks fail on unrelated PRs #2125 (69e93b9d2, jobs 133684045604/133684045724/133684045507) and #2129 (f01e96648, jobs 133734529937/133734530007/133734529966), while #2113's 5571776b passed parts 8 and 9-12 on 2026-11-16 16:57Z

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## Readings

| PR head | part | check | residual |
|---|---|---|---|
| #2125 69e93b9d2 | desktop 8 | dropping the road-legibility aid restores the default frame | mean 0.11, worst 35 (need <=0.1, <=3) |
| #2125 69e93b9d2 | desktop 8 | restoring the roughness channel restores the frame | mean 0.08, worst 16 |
| #2125 69e93b9d2 | desktop 9-12 | restoring the shadow reach restores the frame (±240 m) | mean 0.02, worst 5 |
| #2125 69e93b9d2 | mobile 9-12 | dropping the brightness aid restores the calibrated frame | mean 0.14, worst 4 |
| #2129 f01e96648 | desktop 8 | road-legibility aid / roughness channel | worst 47 / worst 10 |
| #2129 f01e96648 | desktop 9-12, mobile 9-12 | shadow reach (±240 m / ±120 m) | worst 4 / worst 5 |

Each of these captures twice with `setAnimationHold(true)`, so a residual means something in the frame is still moving or streaming under the hold. A first suspect, not yet checked: a layer that landed between 2026-11-16 16:57Z and 22:57Z and animates outside the hold (T-3612's vessels are the obvious candidate). Check `setAnimationHold` against every animated layer before loosening any tolerance.
