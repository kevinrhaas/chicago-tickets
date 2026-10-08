---
id: T-2069
title: Scope chicago-4d-pr-stuck.yml's concurrency group per ref, so one branch's push stops cancelling another PR's report check and leaving it unstable (a workflow change; T-1520's reading)
state: done
epic: META
requested_by: loop
seen: false
effort: XS
legacy_id: null
parent: null
opened: 2026-10-04
closed: 2026-10-08
pr: 534
claimed_by: run 10/8/2026, 1:02:48 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-08T18:31:41Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37819437880
claimed_at: 2026-10-08T18:02:48.723Z
decision: null
decision_answer: null
---

Scope chicago-4d-pr-stuck.yml's concurrency group per ref, so one branch's push stops cancelling another PR's report check and leaving it unstable (a workflow change; T-1520's reading).

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 196 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> T-1520 closes when its PR merges and the cure it names is a workflow edit, which AGENTS.md puts outside a run's scope (owner-visible PR only); folded into T-1520 it would vanish with it

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

**Finding, 2026-10-05 (#455):** seen again in the merge path, not only on the report. Pushing ef74426 to #455 started a `stuck PR report` run (37270266231) that was cancelled 78 s in. `gh-rest.sh pr-automerge` read the cancelled `report` as a red check, refused (exit 3) and applied `resume` to a PR whose gate and moving-frames were still running green. Re-running that one report workflow cleared it, and the PR merged on the next lap. So this defect also costs a refusal and a resume lap on a PR that should have merged.

**Finding, 2026-10-05 (#488, T-2132):** the same defect, twice on one PR. The `stuck PR report` run 37363856560 was cancelled on push, so `pr-automerge` refused (exit 3) and applied `resume` while `gate` and `moving-frames` were still running. Its re-run (attempt 2) was cancelled again while it sat queued. A third attempt, started after the gate went green, held, and the PR merged on that lap. Cost: two refusals, one stray `resume` label and about ten minutes, on a PR whose real checks never went red.

## Finding, 2026-10-05 (loop, lapping #491): not every `cancelled` gate is this defect

#491's `gate` (run 37370208875, attempt 1) read `cancelled` after 15 min, and the
resume note called it a timeout. It was neither a timeout nor this concurrency
group: the job annotation says **"The job was not acquired by Runner of type hosted
even after multiple attempts"** — no runner ever took it. A REST re-run
(`POST …/actions/runs/37370208875/rerun`) got a runner at once, and then spent
**24 of its 31 minutes in `actions/checkout@v4`** (21:24:41 → 21:48:56Z, the
`fetch-depth: 0` full-history clone) before `check.sh` passed in about 6 min. It
merged green on the second `pr-automerge` lap. So, when you take this ticket: (1) a
gate `cancelled` with that annotation needs a re-run, not a fix, and a report that
said so would save the next run reading the job; (2) the gate's full-history clone is
now the slowest step on a busy day, and C4D_GATE_REQUIRE_BASE only needs the merge
base. A bounded `fetch-depth` plus a `git fetch --deepen` fallback may be worth
measuring.

**Finding, 2026-10-08 (#530, T-2180):** again. `stuck PR report` run 37811301944 was cancelled while `gate` and `moving-frames` were in progress; `pr-automerge` refused (exit 3) and applied `resume` to a PR gated green locally (check.sh 790/790, smoke parts mobile 13/3 and desktop 3). The run re-ran the report via REST and left the merge to the next lap.

**Finding, 2026-10-08 (#525, T-2174) — a second workflow, same refusal:** after the PR was lapped over T-2068 (#533), `chicago-4d-bake.yml`'s `warranted` job ran on the branch push and was **cancelled** by its own `timeout-minutes: 5`. The job's `push: paths` filter matches the workflow file, and the lap merge carried T-2068's edit to it. The job never got past `actions/checkout` with `fetch-depth: 0`, fetching every ref of a 4 GB repository (17:35:48 → 17:40:47). `pr-automerge` refused (exit 3) on that cancelled check while `gate`, `report` and `moving-frames` all went green on the same head. It was merged with `GH_REST_MERGE_BLIND=1`, and the reason is on the PR. Expect this on every branch first pushed after a merge of dev over T-2068. Candidate fixes: `warranted` only needs `origin/dev` plus the merge base, so a shallow fetch with `--deepen`, or `pr-automerge` treating a cancelled check from a non-gate workflow as not-a-verdict. The queue was at its ceiling (147/140), so this was folded here rather than filed as a new ticket.
