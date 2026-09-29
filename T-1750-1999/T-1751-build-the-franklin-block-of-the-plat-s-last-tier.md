---
id: T-1751
title: Build the Franklin block of the plat's last tier to its seats: the seven cottages and yard buildings the platted deal holds on blk_washington_franklin
state: review
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-28
closed: null
pr: 198
claimed_by: run 9/29/2026, 7:11:38 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-09-29T12:11:38.258Z
decision: null
decision_answer: null
---

Build the Franklin block of the plat's last tier to its seats: the seven cottages and yard buildings the platted deal holds on blk_washington_franklin.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 140 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> the queue stands at its ceiling of 140 lines, and this line is filed over it because the cell above needs a LIVE owner inside this pull request: after it merges the red is dev's and is nobody's diff.

## FILED ABOVE BAND 9, BECAUSE IT BLOCKS

A follow-up goes to the foot of band 9 unless dev's gate is red on it or the build in hand cannot finish without it (owner, 2026-09-27). This one was placed above band 9 on this reason:

> dev's gate goes red on the order book the moment T-1708 closes: the reconstruction order book's structures/ordinary_dwellings/south cell still owes 59 roofs and T-1708 is the ticket that orders them, so on close the book would order work nobody can claim (T-1420) and every re-derivation on dev fails on that row. T-1203's whole subtree closes with T-1708, and T-1735 and T-1736 — the tier's other two dealt blocks — are both already in review, so no live ticket is left to own the cell. This ticket is its next live owner.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
