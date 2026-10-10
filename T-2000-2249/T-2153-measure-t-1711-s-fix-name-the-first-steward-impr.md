---
id: T-2153
title: Measure T-1711's fix: name the first steward-improve run cancelled at its cap after polecat-platform#190, and the steward-focus run its kick dispatched within a minute
state: done
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-06
closed: 2026-10-10
pr: 192
claimed_by: run 10/9/2026, 11:36:27 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-10T04:45:09Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38024455247
claimed_at: 2026-10-10T04:36:27.236Z
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

## Closed 2026-10-10 — kevinrhaas/polecat-platform PR #192 (merged, 3ca1692)

`pr: 192` is polecat-platform's number, as on T-1711. `settle` reads kevinrhaas/chicago numbers, so this was closed by hand after the merge.

**The first cap cancel after #190: 37733398534** (chicago [4/5], 2026-10-08 05:38:36Z → 08:08:37Z). Its `Run steward` step had just finished (08:08:29Z), so the refill step saw `success` and logged `→ slot freed; kicking steward-focus` at 08:08:33Z. That kick started **steward-focus 37747883133** at 08:08:35Z, which dispatched **refill 37747901580** ([4/5]) at 08:08:45Z, **12 s from kick to refill**.

**The first kick through the `cancelled` branch: 37807547340** (chicago [3/5]). It logged `→ cancelled at 150m, the 150m cap; kicking steward-focus` at 18:47:39Z and started **steward-focus 37827023727** at 18:47:41Z. **That run dispatched nothing.** It listed the runs at 18:47:47Z, but the kicking job did not end until 18:47:53Z, so slot 3 still read `in_progress` and was counted as busy. The slot was refilled at 18:49:38Z (37827267592) by cron tick 37827243566, **1 m 59 s** after the kick.

All seven cap cancels from 2026-10-08 to 2026-10-10:

| cancelled run | kick | steward-focus | read vs job end | refill |
|---|---|---|---|---|
| 37733398534 [4/5] | 08:08:33 `slot freed` | 37747883133 | 08:08:40 vs :37 | 37747901580, 12 s |
| 37807547340 [3/5] | 18:47:39 cap | 37827023727 | 18:47:47 vs :53, **0 dispatched** | 37827267592 by cron, 1 m 59 s |
| 37844818872 [4/5] | 23:40:29 cap | 37860733942 | 23:40:37 vs :33 | 37860754500, 15 s |
| 37932683926 [5/5] | 15:21:14 cap | 37951096088 | 15:21:22 vs :20 | 37951120268, 14 s |
| 37943940399 [1/5] | 16:55:10 cap | 37962549547 | 16:55:21 vs :16 | 37962577087, 16 s |
| 38005649772 [4/7] | 02:11:56 cap | 38016075718 (queued) | 02:15:14 vs 02:12:00 | 38016287210, 3 m 24 s |
| 38008971882 [3/7] | 02:55:47 cap | 38018748358 | 02:55:54 vs :50 | 38018759813, 13 s |

No step logged `not kicking` on a cap cancel. Both the threshold and the start stamp are right.

**What the measurement found, and what PR #192 changed.** Whether a kick got a refill dispatched was a race: the kicking run is still `in_progress` through its own teardown, and the race was won by 2–5 s six times and lost by 6 s once. Successful runs kick the same way, so they hit the same race. Since #192, `refill-kick.sh` passes `freed_run=$GITHUB_RUN_ID`, steward-focus passes it to `dispatch-lanes.mjs` as `FREED_RUN`, and the dispatcher leaves that one run out of slot occupancy. `test-refill-kick.sh` and `test-lanes.mjs` (ci.yml) cover it. No live kick after #192 had been read when this was written. The next one should log `Run <id> kicked this tick, so its slot is free.` in steward-focus's "Dispatch app lanes" step.
