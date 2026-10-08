---
id: T-2186
title: Desktop smoke part 3 is red on dev: T-1727's 'the HUD and the card both name the version' finds the version chip with text 'version fixture' and tone 'active' but visible:false after enterTown — reproduced on a clean dev worktree at 16938b331 (102 pass, this the one red)
state: claimed
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-10-08
closed: null
pr: null
claimed_by: run 10/8/2026, 1:33:55 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37824821076
claimed_at: 2026-10-08T18:33:55.583Z
decision: null
decision_answer: null
---

Desktop smoke part 3 is red on dev: T-1727's 'the HUD and the card both name the version' finds the version chip with text 'version fixture' and tone 'active' but visible:false after enterTown — reproduced on a clean dev worktree at 16938b331 (102 pass, this the one red).

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 148 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> a red on dev's own gate that no ticket owns; every branch's part-3 leg inherits it and each run would otherwise re-derive whose it is (lapping #531 spent a leg proving it)

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
