---
id: T-1718
title: The survey-tract gate compares a 2-decimal round of a reprojected coordinate for exact equality, and T-1707 moved the Original Town's east bound onto the knife edge: 825.045 rounds to 825.05 on the steward runner and 825.04 in CI, so no machine can commit a green tract layer
state: withdrawn
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-28
closed: 2026-09-28
pr: null
claimed_by: null
blocked_on: misfiled: filed --after T-1707 without --blocks, so it went to the foot of band 9 where a merge-blocker is never reached. Re-filed identically as T-1719, directly under T-1707, with the blocking reason stated. No work was done under this id.
needs_bake: false
closed_at: 2026-09-28T08:41:38.700Z
claimed_run: null
claimed_at: null
decision: null
decision_answer: null
---

The survey-tract gate compares a 2-decimal round of a reprojected coordinate for exact equality, and T-1707 moved the Original Town's east bound onto the knife edge: 825.045 rounds to 825.05 on the steward runner and 825.04 in CI, so no machine can commit a green tract layer.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 141 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> A MERGE THAT CANNOT LAND, which the queue header reserves band 0 for. PR #154 is green on the steward runner (check.sh 679/679) and red in CI on this one step, and the disagreement is one centimetre on one bound whose raw value is exactly 825.045000000000 — a round-half-to-even over the binary double, decided by an ULP of PROJ. Whichever machine commits the value, the other's gate refuses it, so this blocks #154 and every later branch that re-derives the tract layer. It cannot be a finding on T-1707 because T-1707 settles to done when #154 merges, which is the thing this prevents.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
