---
id: T-2081
title: Place the seating chain (seat_known_1835 -> seat_platted_ground_1835 -> seat_off_plat_ground_1835 -> build_order_book_1835) in the manifest in hand-off order, measured under _must_reproduce, or say in writer_inventory.json why it cannot be — seat_known_1835 reads the order book and both seat files back, so the chain is a cycle and wants its own measured pass
state: open
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: T-2065
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

Place the seating chain (seat_known_1835 -> seat_platted_ground_1835 -> seat_off_plat_ground_1835 -> build_order_book_1835) in the manifest in hand-off order, measured under _must_reproduce, or say in writer_inventory.json why it cannot be — seat_known_1835 reads the order book and both seat files back, so the chain is a cycle and wants its own measured pass.

Piece 2 of 3 of **T-2065 — The derived manifest's in-sequence lags T-1602 left: location_spend reads the reconciliation a later step rebuilds, the seating passes sit outside the manifest, and nothing gates the 84-132 answer**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2065 was split (2026-10-04T10:53:32.875Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 1m ago, run 10/4/2026, 5:52:08 AM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/37196588788) — held by the run that split it
- branch `steward/t2065-manifest-lags` — the splitter's own

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/37196588788) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)
