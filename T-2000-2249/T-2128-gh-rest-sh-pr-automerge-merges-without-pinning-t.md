---
id: T-2128
title: gh-rest.sh pr-automerge merges without pinning the sha it gated, so a push that lands between its check read and its merge PUT goes into dev ungated
state: open
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-04
closed: null
pr: null
claimed_by: null
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: null
decision: null
decision_answer: null
---

gh-rest.sh pr-automerge merges without pinning the sha it gated, so a push that lands between its check read and its merge PUT goes into dev ungated.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 183 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> A gate bypass of the T-1572 class (#43), not a finding about an existing ticket: PR #450 was merged at head 0c99665 on the green checks of 2b461e2, because the PR API still reported the old head seconds after the push. The fix is one field: pass "sha" in the PUT pulls/N/merge payload so GitHub answers 409 when the head moved. (The merged tree was re-gated afterwards: check.sh 780/780 green on dev 1de230b.)

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
