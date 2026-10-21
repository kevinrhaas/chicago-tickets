---
id: T-2970
title: Draw-call budgets count driver draws, not renderer.info.calls: three counts a BatchedMesh multi-draw as one call though every kept instance is a driver draw (T-2927 read 27,895 GL draws where renderer.info said 339 at the 1904 flight), so the 90-call cap, measure_walk_frames, the detail ceilings and the smoke's draw checks move to a counted GL-call figure, re-baselined after T-2927's coalescing
state: done
epic: RENDERING
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-20
closed: 2026-10-21
pr: 1163
claimed_by: run 10/20/2026, 6:34:08 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-21T08:04:57Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/39514737095
claimed_at: 2026-10-20T23:34:09.334Z
decision: null
decision_answer: null
---

Draw-call budgets count driver draws, not renderer.info.calls: three counts a BatchedMesh multi-draw as one call though every kept instance is a driver draw (T-2927 read 27,895 GL draws where renderer.info said 339 at the 1904 flight), so the 90-call cap, measure_walk_frames, the detail ceilings and the smoke's draw checks move to a counted GL-call figure, re-baselined after T-2927's coalescing.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 145 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> found by T-2927's run; every draw budget reads a counter that undercounts by up to ~80x, so no gate saw the 1904 flight's real cost

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
