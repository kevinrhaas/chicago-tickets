---
id: T-3695
title: 1812 frames take seconds once the Jaunts list has opened
state: done
epic: META
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-11-19
closed: 2026-11-19
pr: 2227
claimed_by: run 11/19/2026, 11:30:28 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-11-19T19:53:29Z
claimed_run: null
claimed_at: 2026-11-19T17:30:29.911Z
decision: null
decision_answer: null
---

1812 frames take seconds once the Jaunts list has opened.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## Result (PR #2227)

Kevin, 2026-11-19, on his Mac: 1812 on dev went to seconds between frames once he had opened Jaunts. Opening the list builds the route grid. From then on, two people's rounds asked every half second for a doorstep in a closed pocket of the fort, and each failed plan searched 5.8 million cells (2.2 to 2.6 s). route.js now refuses such a goal with a short look back from it, and remembers any search that ran out. Routes are unchanged: 392 plans on a fixture came out identical to the old planner.

Fort parade after Jaunts: desktop went from 3.1 frames a second (stalls of 4.2 to 4.4 s) to 53 a second, median 17 ms. The UHD 630 profile went from 3.3 a second (stalls of 4.4 to 4.7 s) to 54 a second, median 17 ms. The numbers are in `docs/measurements/T-3695-frames.json`.

Before (orange) and after (blue), frames drawn each second, desktop and UHD 630 profile:

![1812 frames after opening Jaunts, before and after](https://github.com/kevinrhaas/chicago-evidence/blob/e7248bd25e820747e87026c28e7d31b9d61f4a3d/evidence/2026-11-19-t3695-frames/frames-chart.png?raw=true)
