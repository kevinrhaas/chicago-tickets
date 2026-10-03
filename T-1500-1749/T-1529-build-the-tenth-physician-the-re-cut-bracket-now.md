---
id: T-1529
title: Build the tenth physician the re-cut bracket now orders: businesses/physician stands at 9 of 10 since the parish register's 120 residents moved the town model, and T-1418 has closed
state: open
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
blocked_on: null
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

## Queue cleanup 2026-10-03 (owner: "see if there are any tickets that were blocked in the queue from before but now can be worked")

**Unblocked.** T-1525 landed (#12) on 2026-09-25; on dev businesses/physician now owes two (target 10, known 8), see T-2001's note above.
