---
id: T-1529
title: Build the tenth physician the re-cut bracket now orders: businesses/physician stands at 9 of 10 since the parish register's 120 residents moved the town model, and T-1418 has closed
state: blocked-tech
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-09-24
closed: null
pr: null
claimed_by: run 9/24/2026, 3:41:16 AM CT
blocked_on: T-1525 has not landed. On dev the bracket still reads scene_date_population_low 2353, so businesses/physician orders target 9, known 8, to_reconstruct 1, filled 1 — the order is SATISFIED and there is no tenth physician to build. The 9 -> 10 re-cut exists only on steward/t1525-recut-order-book (PR #12, labelled hold, mergeable false), which raises the low end to 2363. Building a tenth now would put 10 drawn against an order of 9 — the exact over-supply T-1506 exists to retire. Unblock when PR #12 merges.
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/35976447879
claimed_at: 2026-09-24T08:41:17.339Z
decision: null
decision_answer: null
---

Build the tenth physician the re-cut bracket now orders: businesses/physician stands at 9 of 10 since the parish register's 120 residents moved the town model, and T-1418 has closed.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

**Added by T-2001 (2026-10-02): the blocked reason above is stale, and the bucket now owes two.** T-1525 (#12) LANDED on 2026-09-25. On dev `businesses/physician` reads target 10, known 8, to_reconstruct 2, filled 0, owning_ticket T-1529. Landing it also retired `rcb_mcguire_physician`: the row moved from T-1418 to T-1529 and no group of `tools/reconstruct_businesses_1835.py` spends a T-1529 row (`GROUPS` keys each group to one book ticket), so the office the one drawn physician head kept stopped being written. That head, Dr John McGuire (`rc_mcguire_john`), now reads `keeps_their_own_house` with no house in the employment coverage. What stands in the way of building is not the order but the heads: the book orders 2 and the resident band drew 1 physician head, and `build_group` refuses to half-fill a count by design. So unblocking this needs (a) a group that spends the T-1529 row and (b) a second physician head from the resident band, or a ruling that the order is 1. T-2001 did not take either and left McGuire owed by name.
