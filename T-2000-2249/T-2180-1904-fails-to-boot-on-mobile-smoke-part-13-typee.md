---
id: T-2180
title: /1904/ fails to boot on mobile smoke part 13: TypeError in walk/js/spatial-batch.js:27 (BufferAttribute.getX on a null array) — first seen on PR #528's branch, which touches no 1904 data; spatial-batch.js last moved in #511
state: review
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-10-08
closed: null
pr: 530
claimed_by: run 10/8/2026, 11:09:00 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37805053909
claimed_at: 2026-10-08T16:09:00.508Z
decision: null
decision_answer: null
---

/1904/ fails to boot on mobile smoke part 13: TypeError in walk/js/spatial-batch.js:27 (BufferAttribute.getX on a null array) — first seen on PR #528's branch, which touches no 1904 data; spatial-batch.js last moved in #511.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 151 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> a red smoke leg on dev that no open ticket owns; every branch's part-13 leg will read red until it is fixed

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
