---
id: T-2153
title: Measure T-1711's fix: name the first steward-improve run cancelled at its cap after polecat-platform#190, and the steward-focus run its kick dispatched within a minute
state: open
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-06
closed: null
pr: null
claimed_by: run 10/7/2026, 11:07:22 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37725706091
claimed_at: 2026-10-08T04:07:22.739Z
decision: null
decision_answer: null
---

Measure T-1711's fix: name the first steward-improve run cancelled at its cap after polecat-platform#190, and the steward-focus run its kick dispatched within a minute.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 155 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> T-1711's acceptance 4 (a measured refill with run IDs) can only be met by a real cap cancel after its merge; T-1711 leaves the queue in the same pass, so the line count is unchanged

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## What to record

polecat-platform PR #190 (merged 2026-10-06, 18b586a) lets a steward-improve run cancelled
within 10 minutes of its 150-minute cap kick steward-focus, via `.github/steward/refill-kick.sh`.
The first such run's `Free this slot…` step should log `→ cancelled at NNNm, the 150m cap;
kicking steward-focus`. Record that run's id, the steward-focus run it dispatched, and the
refill run's start time, and write them into T-1711 under its acceptance item 4. If the step
logs `not kicking` on a cap cancel, the threshold or the start stamp is wrong: say which.

## Reading, 2026-10-08 04:15Z — no cap cancel yet, so blocked on one (slice 3/5)

Nothing to name yet. Every steward-improve run created since #190 merged
(2026-10-06T19:59:48Z) up to this batch's dispatch at 2026-10-08T04:04Z — 61 runs, read
from `GET /actions/workflows/steward-improve.yml/runs` — ended `success` or `failure`. Not
one ended `cancelled`. The only cancel since 2026-10-06 is 37393918679 (chicago [4/5],
00:25Z → 02:56Z, 150 min), which ran on the old workflow, before the fix.

**The success path through the same step works, with run IDs.** Run 37523361307
(chicago [3/5]) ended `success` at 21:58:43Z. Its step 22, `Free this slot…`, ran
`refill-kick.sh "success" "1791316926" "150"`, logged `→ slot freed; kicking steward-focus`,
and dispatched steward-focus 37537576369 at 21:58:45Z. That run started the refill,
steward-improve 37537597325 (chicago [3/5]), at 21:58:56Z: **13 s from the kick to the
refill starting.** `STEWARD_JOB_T0` and `REFILL_CAP_MINUTES: 150` are both set in that step's env, so a
cap cancel will reach the elapsed-time branch with real numbers and not the "no start
stamp" branch. What is still unproven is only the `cancelled` branch itself, live.

**Why no run reached the cap.** The lane hit the weekly usage limit at 22:17:09Z on
2026-10-06 (run 37527558501 logged `You've hit your weekly limit · resets Oct 8, 4am (UTC)`
at 100 min). From 22:12Z to 23:57Z the scheduler dispatched 37 more runs; each one failed
inside ~1.5 min on the same rejection, with 0 tool calls, and its step 22 was `skipped`, as
designed for a `failure`. After 23:57Z nothing was dispatched until the reset. A cap cancel
needs a 150-minute run, so none could happen inside that window.

**What unblocks it.** The first steward-improve run that ends `cancelled` at 140+ minutes.
To read it: list `?status=cancelled&created=>=2026-10-06T19:59:48Z`, pull that run's job log
(`gh api --allow-escape-sequences …/actions/jobs/<id>/logs`), grep `kicking\|not kicking`.
The line after the kick is the steward-focus run's URL. The refill is the next
steward-improve run with the same `[k/N]` title. About 6 tool calls in all.

## Queue cleanup 2026-10-10 (owner: "are there any other held tickets that can be cleared")

Unblocked: the event this waited for has happened. polecat-platform `steward-improve.yml` runs **38005649772** (created 2026-10-09T23:41:27Z, cancelled at 2026-10-10T02:12:01Z) and **38008971882** (00:25:18Z, cancelled at 02:55:51Z) both ran about 150.5 minutes and were cancelled at the cap. Only the newest 60 completed runs were listed, so an earlier cap cancel after 2026-10-06T19:59:48Z may exist; find the first one, then the steward-focus run its kick dispatched.
