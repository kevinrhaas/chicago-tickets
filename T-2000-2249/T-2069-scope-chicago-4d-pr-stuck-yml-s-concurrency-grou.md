---
id: T-2069
title: Scope chicago-4d-pr-stuck.yml's concurrency group per ref, so one branch's push stops cancelling another PR's report check and leaving it unstable (a workflow change; T-1520's reading)
state: open
epic: META
requested_by: loop
seen: false
effort: XS
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

Scope chicago-4d-pr-stuck.yml's concurrency group per ref, so one branch's push stops cancelling another PR's report check and leaving it unstable (a workflow change; T-1520's reading).

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 196 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> T-1520 closes when its PR merges and the cure it names is a workflow edit, which AGENTS.md puts outside a run's scope (owner-visible PR only); folded into T-1520 it would vanish with it

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

**Finding, 2026-10-05 (#455):** seen again in the merge path, not only on the report. Pushing ef74426 to #455 started a `stuck PR report` run (37270266231) that was cancelled 78 s in. `gh-rest.sh pr-automerge` read the cancelled `report` as a red check, refused (exit 3) and applied `resume` to a PR whose gate and moving-frames were still running green. Re-running that one report workflow cleared it, and the PR merged on the next lap. So this defect also costs a refusal and a resume lap on a PR that should have merged.
