---
id: T-1640
title: The freight sheds and landings behind South Water, on the river-bank band the south-bank ground rule allows
state: claimed
epic: TOWN
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-1200
opened: 2026-09-26
closed: null
pr: null
claimed_by: run 9/27/2026, 8:56:43 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/36323826023
claimed_at: 2026-09-27T13:56:43.996Z
decision: null
decision_answer: null
---

The freight sheds and landings behind South Water, on the river-bank band the south-bank ground rule allows.

Piece 3 of 4 of **T-1200 — Build the South Water Street river front to its seats: the forwarding houses, warehouses, stores and store-residences on the party lines from Market to State, the freight sheds and landings behind, every roof with its firm and its keeper**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

## The order book's `('south','warehouses_freight')` row names this ticket alone, and that is worth a second look (2026-09-27)

Two runs fixed that stale row within an hour of T-1200's split and resolved it differently.
`dev`'s own T-1420 sweep wrote `"T-1640"`; PR #95's wrote `("T-1639", "T-1640")`, on the
reasoning that T-1639's title asks for the **F1-F3 warehouses on the street line** while this
ticket owns the freight sheds and landings behind them, and the inventory holds both halves
in one cell it does not cut. PR #95 kept the tuple through its merge; PR #98 (T-1638) landed
after it and `dev` now reads `"T-1640"` again, so the single-ticket answer is the committed
one.

Nothing is broken by that — the book re-derives and `ticket_liveness` is green either way,
and the gate proves it on both. But whoever spends this bucket should decide deliberately
whether the 6 remaining roofs of the group are all this ticket's, or whether T-1639 owes the
street-line warehouses among them, and state the answer at the row rather than letting the
next sweep flip it a third time. `owning_tickets` (the tuple form) is already what the book
uses for ground, where the same "more than one live run owes one cell" is true.
