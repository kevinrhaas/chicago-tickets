---
id: T-1613
title: The lot ledger the seating deals from, and the platted ground seated on it: every lot of the committed plat enumerated with its block, frontage, street class, standing roofs and multi-building rule, and every reconstructed household and business the policy puts inside the plat dealt onto a named lot, party-line packed to the density standard, order-book buckets decremented
state: review
epic: TOWN
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-1199
opened: 2026-09-26
closed: null
pr: 71
claimed_by: run 9/26/2026, 3:29:44 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/36229532871
claimed_at: 2026-09-26T08:29:44.362Z
decision: null
decision_answer: null
---

The lot ledger the seating deals from, and the platted ground seated on it: every lot of the committed plat enumerated with its block, frontage, street class, standing roofs and multi-building rule, and every reconstructed household and business the policy puts inside the plat dealt onto a named lot, party-line packed to the density standard, order-book buckets decremented.

Piece 1 of 3 of **T-1199 — Seat every reconstructed household, business, lodging house and camp by the placement policy into the extended lot grid: multiple buildings per main-street lot, single roofs on the back streets, labourers on the small lots and fringes, the noxious trades on the branches — deterministic, order-book-counted**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

- `data/reconstruction/1835_lot_ledger.json` enumerates every lot of the committed plat —
  226 over 37 blocks — each with its block, grid, district, plat lot number and that
  number's confidence, the face it takes, the street that face fronts and that street's
  traffic class, whether it turns a corner, its frontage and depth, the block's ground
  reading, the multi-building rule the placement policy puts on a lot of that class, what
  stands on it, how many of those are principal roofs, and whether it bars another. Every
  field a JOIN over a committed record; nothing asserted.
- The multi-building-lot rate on the principal streets is PRINTED against the density
  standard, as a reading of the committed town rather than a target.
- `data/reconstruction/1835_platted_seats.json` offers the plat to every household the
  address book leaves at a band, in the placement policy's own clause order: a standing
  anonymous roof of an admitted family is ADOPTED before any slot is asked for, a slot is
  raised only inside an open block's committed family plan and headroom, and every row the
  plat cannot hold is handed to T-1614 with its reason in writing. No row blank, none
  dropped, none seated twice.
- Documented buildings are never re-tenanted, a roof whose record states its occupancy is
  left alone, and no household is seated in an ancillary family. Each refusal counted and
  named in the record.
- An adoption raises no roof and draws nothing off the order book; a slot draws exactly one
  roof of one family from one open block's plan, and never past its headroom. No structure
  record is touched and nothing is baked.
- Deterministic; `--check` and `--self-test` in `check.sh`; `docs/LIBERTIES.md` L270 carries
  the invention with its scope, counted by the register's own gate.

**Not this ticket:** the off-plat ground (T-1614), and carrying the seats through to the
infill recipes and the People/Businesses views (T-1615).
