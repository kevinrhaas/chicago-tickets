---
id: T-1638
title: Every South Water roof the platted deal seated a household on names its keeper: occupants and resident_assignment written from the seat, and the letter-list names refused in writing with the ruling that refuses them
state: done
epic: TOWN
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-1200
opened: 2026-09-26
closed: 2026-09-26
pr: 98
claimed_by: run 9/26/2026, 5:38:29 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-09-27T00:33:47Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/36276009189
claimed_at: 2026-09-26T22:38:29.946Z
decision: null
decision_answer: null
---

Every South Water roof the platted deal seated a household on names its keeper: occupants and resident_assignment written from the seat, and the letter-list names refused in writing with the ruling that refuses them.

Piece 1 of 4 of **T-1200 — Build the South Water Street river front to its seats: the forwarding houses, warehouses, stores and store-residences on the party lines from Market to State, the freight sheds and landings behind, every roof with its firm and its keeper**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

**Acceptance:** the twenty South Water seats of the platted deal are each answered — written
onto the roof, or refused in writing with the ruling that refuses them — deterministically,
re-derived by a `--check` in `check.sh`, and nothing is raised or baked.

- `data/reconstruction/1835_roof_keepers.json`, derived by `tools/name_the_keepers_1835.py`:
  every ADOPTED seat of `1835_platted_seats.json` written, refused or owed, never dropped.
- The written roofs carry `occupants` (graded `reconstructed`, citing only the sources that
  carry the household's NAME) and `resident_assignment` with `status: assigned` and
  `household_id`. The id is NOT in the `occupants` prose: `generate_dooryard_pickets.py`
  admits a lot for a garden on an id appearing there, and a keeper is not a garden.
- The letter-list cohort is REFUSED, with the owner's ruling of 2026-08-30 (T-0379) named.
  60 of the deal's 108 adopted seats are that cohort — the deal seats them and the ruling
  refuses them a roof, which is a disagreement this ticket files and does not settle.
- `seat_platted_ground_1835.py --check` still re-derives the deal unchanged: its occupancy
  refusal now recognises its own writing, so a roof it has seated stays adoptable by that
  household and by no other. Any other pass's occupancy still holds a roof back.
- No mesh moves — `generators/mesh_inputs.py` hashes archetype parameters, not prose — so
  this piece is bake-free even though the parent is not.
- **Visible:** the Keepers row on nine building cards a visitor opens on South Water Street.
- LIBERTIES: L276, over L270's invention.

**Stop condition:** no South Water seat of the platted deal is silent in both directions.
