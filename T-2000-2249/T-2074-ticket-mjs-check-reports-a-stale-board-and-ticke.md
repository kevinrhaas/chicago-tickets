---
id: T-2074
title: ticket.mjs check reports a stale board and tickets.json instead of repairing them, writing nothing on a consistent or a stale tree
state: review
epic: META
requested_by: steward
seen: false
effort: S
legacy_id: null
parent: T-1341
opened: 2026-10-04
closed: null
pr: 391
claimed_by: run 10/4/2026, 2:35:41 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37185951501
claimed_at: 2026-10-04T07:35:42.003Z
decision: null
decision_answer: null
---

ticket.mjs check reports a stale board and tickets.json instead of repairing them, writing nothing on a consistent or a stale tree.

Piece 1 of 2 of **T-1341 — ticket.mjs --check REPAIRS the mirror it is checking, so on any branch that adds a ticket the gate's queue step mutates tickets.json while the pool reads it — the T-0856 check-that-repairs fault, one tool over**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

1. `node tools/ticket.mjs check` writes NOTHING, on a consistent tree and on a stale one
   alike. It reports the staleness and exits non-zero; repairing is `board`'s job.
2. Measured the way it was found: the T-1339 probe (`tools/isolation_probe/node_probe.js`)
   over a consistent tree AND over a deliberately stale one, with `wrote: []` on both.
3. The gate step that runs it still catches a stale board — it REPORTS it instead of
   quietly mending it — and `tools/test_ticket_mirror.mjs` proves both halves on a sandbox.

The parent's reasoning (T-0856 one tool over; the live race inside check.sh's job pool)
is in T-1341.
