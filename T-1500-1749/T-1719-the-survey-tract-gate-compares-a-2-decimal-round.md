---
id: T-1719
title: The survey-tract gate compares a 2-decimal round of a reprojected coordinate for exact equality, and T-1707 moved the Original Town's east bound onto the knife edge: 825.045 rounds to 825.05 on the steward runner and 825.04 in CI, so no machine can commit a green tract layer
state: review
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-28
closed: null
pr: 156
claimed_by: run 9/28/2026, 5:12:33 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/36407976777
claimed_at: 2026-09-28T10:12:33.396Z
decision: null
decision_answer: null
---

The survey-tract gate compares a 2-decimal round of a reprojected coordinate for exact equality, and T-1707 moved the Original Town's east bound onto the knife edge: 825.045 rounds to 825.05 on the steward runner and 825.04 in CI, so no machine can commit a green tract layer.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 142 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> A MERGE THAT CANNOT LAND, which the queue header reserves band 0 for. It cannot be a finding on T-1707 because T-1707 settles to done when #154 merges, which is the thing this prevents.

## FILED ABOVE BAND 9, BECAUSE IT BLOCKS

A follow-up goes to the foot of band 9 unless dev's gate is red on it or the build in hand cannot finish without it (owner, 2026-09-27). This one was placed above band 9 on this reason:

> PR #154 (T-1707) cannot merge without it: check.sh is 679/679 green on the steward runner and red in CI on this one step, and the disagreement is one centimetre on one bound whose raw value is exactly 825.045000000000 — round-half-to-even over the binary double, decided by an ULP of PROJ. Whichever machine commits the value, the other's gate refuses it, so it also blocks every later branch that re-derives the tract layer.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
