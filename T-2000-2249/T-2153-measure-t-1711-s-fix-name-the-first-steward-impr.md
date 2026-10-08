---
id: T-2153
title: Measure T-1711's fix: name the first steward-improve run cancelled at its cap after polecat-platform#190, and the steward-focus run its kick dispatched within a minute
state: claimed
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-06
closed: null
pr: null
claimed_by: run 10/7/2026, 11:07:22 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37725706091
claimed_at: 2026-10-08T04:07:22.739Z
decision: null
decision_answer: null
---

Measure T-1711's fix: name the first steward-improve run cancelled at its cap after polecat-platform#190, and the steward-focus run its kick dispatched within a minute.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 155 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> T-1711's acceptance 4 (a measured refill with run IDs) can only be met by a real cap cancel after its merge; T-1711 leaves the queue in the same pass, so the line count is unchanged

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## What to record

polecat-platform PR #190 (merged 2026-10-06, 18b586a) lets a steward-improve run cancelled
within 10 minutes of its 150-minute cap kick steward-focus, via `.github/steward/refill-kick.sh`.
The first such run's `Free this slot…` step should log `→ cancelled at NNNm, the 150m cap;
kicking steward-focus`. Record that run's id, the steward-focus run it dispatched, and the
refill run's start time, and write them into T-1711 under its acceptance item 4. If the step
logs `not kicking` on a cap cancel, the threshold or the start stamp is wrong: say which.
