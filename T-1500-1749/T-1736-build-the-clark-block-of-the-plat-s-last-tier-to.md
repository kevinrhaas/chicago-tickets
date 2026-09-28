---
id: T-1736
title: Build the Clark block of the plat's last tier to its seats: the seven cottages and yard buildings the platted deal holds on blk_washington_clark
state: review
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-28
closed: null
pr: 172
claimed_by: run 9/28/2026, 12:29:55 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/36458113242
claimed_at: 2026-09-28T17:29:55.162Z
decision: null
decision_answer: null
---

Build the Clark block of the plat's last tier to its seats: the seven cottages and yard buildings the platted deal holds on blk_washington_clark.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 144 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> The cell needs an owner that OUTLIVES this pull request, and no open ticket can be given the finding instead: T-1735 is the cell's designated next owner and it closes here, T-1708's subtree is closed, and T-1710 — the successor build_order_book_1835.py names in writing — is in state split. The work itself is measured rather than assumed: the re-derived platted deal slots seven households onto blk_washington_clark by name, and three more Washington-tier blocks carry seven apiece behind it.

## FILED ABOVE BAND 9, BECAUSE IT BLOCKS

A follow-up goes to the foot of band 9 unless dev's gate is red on it or the build in hand cannot finish without it (owner, 2026-09-27). This one was placed above band 9 on this reason:

> dev's gate goes red on the order book the moment T-1708 and T-1735 both close: structures/ordinary_dwellings/south still owes 62 roofs after T-1735's deal, T-1708's subtree (T-1203 -> T-1707/T-1708/T-1709/T-1710) is closed or closing with it, and T-1735 goes to review in the same pull request that builds its block. This ticket is the next live owner of that cell.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
