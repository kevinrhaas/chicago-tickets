---
id: T-2128
title: gh-rest.sh pr-automerge merges without pinning the sha it gated, so a push that lands between its check read and its merge PUT goes into dev ungated
state: claimed
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-04
closed: null
pr: null
claimed_by: run 10/5/2026, 6:48:25 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37304844038
claimed_at: 2026-10-05T11:48:25.501Z
decision: null
decision_answer: null
---

gh-rest.sh pr-automerge merges without pinning the sha it gated, so a push that lands between its check read and its merge PUT goes into dev ungated.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 183 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> A gate bypass of the T-1572 class (#43), not a finding about an existing ticket: PR #450 was merged at head 0c99665 on the green checks of 2b461e2, because the PR API still reported the old head seconds after the push. The fix is one field: pass "sha" in the PUT pulls/N/merge payload so GitHub answers 409 when the head moved. (The merged tree was re-gated afterwards: check.sh 780/780 green on dev 1de230b.)

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

**Finding, 2026-10-05 (#468, T-2127):** seen live. After a push of `df31afc0` (a dev merge plus a changelog conflict fix), `pr-automerge` printed `every check on faecc49 is green — merging`, which was the PREVIOUS head, and merged `df31afc0` within seconds. The PR's head ref had not yet moved when the checks were read. Harmless this time: the delta was dev's own gated #467 plus a changelog the run had verified locally with `check-changelog.mjs`. It is the exact shape this ticket names, and it also happens when the run's OWN push races the read, not only a third party's.
