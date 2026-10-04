---
id: T-2080
title: Move location_reconciliation.py above its two readers (location_spend.py, report_convergence_coverage.py) and gate the edge, so a merged tree with a moved seat passes --run without a hand step
state: claimed
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: T-2065
opened: 2026-10-04
closed: null
pr: null
claimed_by: run 10/4/2026, 5:53:41 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37196588788
claimed_at: 2026-10-04T10:53:41.956Z
decision: null
decision_answer: null
---

Move location_reconciliation.py above its two readers (location_spend.py, report_convergence_coverage.py) and gate the edge, so a merged tree with a moved seat passes --run without a hand step.

Piece 1 of 3 of **T-2065 — The derived manifest's in-sequence lags T-1602 left: location_spend reads the reconciliation a later step rebuilds, the seating passes sit outside the manifest, and nothing gates the 84-132 answer**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2065 was split (2026-10-04T10:53:32.875Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 1m ago, run 10/4/2026, 5:52:08 AM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/37196588788) — held by the run that split it
- branch `steward/t2065-manifest-lags` — the splitter's own

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/37196588788) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)
