---
id: T-1735
title: Build the La Salle block of the plat's last tier to its seats: the seven cottages and yard buildings the platted deal holds on blk_washington_lasalle
state: claimed
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-28
closed: null
pr: null
claimed_by: run 9/28/2026, 5:53:41 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/36494676475
claimed_at: 2026-09-28T22:53:41.052Z
decision: null
decision_answer: null
---

Build the La Salle block of the plat's last tier to its seats: the seven cottages and yard buildings the platted deal holds on blk_washington_lasalle.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 145 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> The order book's south/ordinary_dwellings cell needs a LIVE owner in this pull request or dev goes red on T-1708's close; T-1203's whole subtree is now closed and no other open ticket raises an ordinary dwelling in the South Division.

## FILED ABOVE BAND 9, BECAUSE IT BLOCKS

A follow-up goes to the foot of band 9 unless dev's gate is red on it or the build in hand cannot finish without it (owner, 2026-09-27). This one was placed above band 9 on this reason:

> dev's gate goes red on the order book the moment T-1708 closes: structures/ordinary_dwellings/south owes 64 roofs and its owning ticket's whole subtree (T-1203 -> T-1707/T-1708/T-1709/T-1710) is closed with it, so the cell would order work nobody can claim. This ticket is the next live owner of that cell.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
