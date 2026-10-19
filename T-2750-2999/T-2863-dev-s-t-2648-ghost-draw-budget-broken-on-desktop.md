---
id: T-2863
title: dev's T-2648 ghost draw budget broken on desktop since #1067 (T-2809 fruit trees): 'a grade row's Look ghosts the grade live, inside the draw budget' reads 331 calls against BUDGET.drawCalls 330 (main.js) in desktop smoke stage 13; win the call back or argue the budget with the reading
state: open
epic: RENDERING
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-19
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

dev's T-2648 ghost draw budget broken on desktop since #1067 (T-2809 fruit trees): 'a grade row's Look ghosts the grade live, inside the draw budget' reads 331 calls against BUDGET.drawCalls 330 (main.js) in desktop smoke stage 13; win the call back or argue the budget with the reading.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 150 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> dev's own desktop smoke is red, so every PR whose smoke runs stage 13 at desktop is refused on a check its diff cannot move (#1061, #1063, #1064 on 2026-10-19)

## FILED ABOVE BAND 9, BECAUSE IT BLOCKS

A follow-up goes to the foot of band 9 unless dev's gate is red on it or the build in hand cannot finish without it (owner, 2026-09-27). This one was placed above band 9 on this reason:

> dev's desktop smoke stage 13 is red on T-2648's ghost draw-budget check: #1061, #1063 and #1064 (text and UI only) all fail it alone since #1067 merged at 2026-10-19 03:37Z, and it passed on #1054, #1062 and #1061's earlier head before

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
