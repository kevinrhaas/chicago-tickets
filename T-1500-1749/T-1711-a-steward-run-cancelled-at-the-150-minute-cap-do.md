---
id: T-1711
title: A steward run cancelled at the 150-minute cap does not tell the scheduler its slot is free, so the lane sits empty until a cron tick that arrives 20-40 minutes apart
state: open
epic: PIPELINE
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-09-27
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

A steward run cancelled at the 150-minute cap does not tell the scheduler its slot is free, so the lane sits empty until a cron tick that arrives 20-40 minutes apart.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 141 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> owner asked for it filed as a band-9 ticket, 2026-09-27 10:50 PM CT

## What happened (2026-09-27, measured)

Steward improve — chicago [1/4], run 36364699185, started 01:06Z and was cancelled at the job's
`timeout-minutes: 150` at 03:36Z. It had already done its work: T-1588 went to `review` with
PR #145 at 03:18Z, and the salvage step found nothing unpushed. It ran out of clock on the
work after the PR was open.

Its last step, `Free this slot, and tell the scheduler to refill it`
(polecat-platform `.github/workflows/steward-improve.yml`), is gated
`if: always() && job.status == 'success' && …`, so a cancelled run SKIPS it. The slot
then waits for the `*/10` steward-focus cron. That night the scheduled ticks landed at
02:01, 02:40, 03:02 and 03:33Z, 20-40 minutes apart, and the last one came three minutes
BEFORE the cancel. Lane 1 sat empty with lanes 2-4 running until the owner saw it on the
Actions page at about 03:40Z; a hand dispatch of steward-focus.yml refilled it at 03:42Z
(run 36374769688).

The success gate is there on purpose: an unconditional re-dispatch let a week of failing
analytics runs burn the shared quota (tech-sweep issue #106). A run cancelled at the cap is
not that case. It is the ceiling, and the workflow's own comments say every cancellation
measured so far was the ceiling.

## The fix, and where it lives

The fix is in kevinrhaas/polecat-platform, not in this repo. This ticket lives here because
the chicago lanes are the ones that pay for it.

**Acceptance:**

1. A steward-improve run that ends `cancelled` kicks steward-focus exactly as a `success` does.
   A `failure` still does not, and the cron still refills it (#106's reasoning stands and
   the step's comment says why the two differ).
2. The kick stays `continue-on-error`, and the scheduler stays idempotent: a kick that finds
   no empty slot dispatches nothing. A redundant kick is harmless and must stay harmless.
3. A cancel that is NOT the cap (someone pressing Cancel, or a concurrency supersede) must not
   restart a lane that was stopped on purpose. Either tell the cases apart (e.g. the
   `Run steward` step's elapsed time against the cap), or show that the scheduler's roster
   already refuses a lane that is switched off, and record which.
4. Measured: one cancelled run's slot is refilled within about a minute, with the run IDs
   recorded here.

Band 9 (owner, 2026-09-27: "file it as a band 9 ticket").
