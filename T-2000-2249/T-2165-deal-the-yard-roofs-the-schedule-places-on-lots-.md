---
id: T-2165
title: Deal the yard roofs the schedule places on lots that can hold them: the North's stable on the Wolcott block, the South's barn on South Water-Wells and smokehouse on South Water-Dearborn
state: done
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: T-2156
opened: 2026-10-08
closed: 2026-10-08
pr: 518
claimed_by: run 10/8/2026, 1:20:16 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-08T09:23:25Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37733398534
claimed_at: 2026-10-08T06:20:16.665Z
decision: null
decision_answer: null
---

Deal the yard roofs the schedule places on lots that can hold them: the North's stable on the Wolcott block, the South's barn on South Water-Wells and smokehouse on South Water-Dearborn.

Piece 1 of 2 of **T-2156 — Build or re-budget the order book's barns_stables and small_outbuildings roofs (North, South, West), pricing the yard buildings against the dwellings they serve (T-1692)**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2156 was split (2026-10-08T06:19:58.375Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 38m ago, run 10/8/2026, 12:41:30 AM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/37733398534) — held by the run that split it
- branch `steward/t2156-yard-buildings` — the splitter's own

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/37733398534) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

## Finding, 2026-10-08 (T-2059's run, PR #513): dev's gate is red on the split until the owner tables move

`check.sh` on dev now fails one step: *"the book orders work from tickets nobody can claim"*.
The order book's owner tables still name **T-2156** for `structures/barns_stables/{north,south,west}`
and `structures/small_outbuildings/{south,west}`, and T-2156 has been `split` since 05:58Z.
Every PR's gate goes red on it, whatever the PR touches (#513 is parked on `resume`, waiting on this).
Sweep those rows onto the live successors (T-2165 / T-2166's pieces / T-2167) in the first PR that
lands, as T-1420 asks.
