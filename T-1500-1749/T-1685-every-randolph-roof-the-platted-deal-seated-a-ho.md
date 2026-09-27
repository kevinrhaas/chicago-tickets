---
id: T-1685
title: Every Randolph roof the platted deal seated a household on names its keeper: occupants and resident_assignment written from the seat, and the refusals said on the roof with the ruling that refuses them
state: claimed
epic: TOWN
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-1202
opened: 2026-09-27
closed: null
pr: null
claimed_by: run 9/27/2026, 3:29:56 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/36347870531
claimed_at: 2026-09-27T20:29:56.570Z
decision: null
decision_answer: null
---

Every Randolph roof the platted deal seated a household on names its keeper: occupants and resident_assignment written from the seat, and the refusals said on the roof with the ruling that refuses them.

Piece 1 of 4 of **T-1202 — Build the Randolph–Washington tier and the public square's neighbours to their seats: the professional and merchant houses (H1/H2), the churches and schools the civic band established, the log jail and the estray pen as they stand, the dwellings falling southward**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

**Acceptance:** the forty Randolph seats of the platted deal are each answered — written
onto the roof, or refused in writing with the ruling that refuses them — deterministically,
re-derived by a `--check` in `check.sh`, and nothing is raised or baked.

- `tools/name_the_keepers_1835.py` takes a LIST of districts rather than one, each carrying
  the ticket that ran it, so a Randolph roof's prose names T-1685 and a South Water roof's
  still names T-1638 — byte-identical for the nine already written.
- The written roofs carry `occupants` (graded `reconstructed`, citing only the sources that
  carry the household's NAME) and `resident_assignment` with `status: assigned` and
  `household_id`; the id is NOT in the `occupants` prose.
- Every refused seat this pass owns says so ON the roof, with the ruling and the measured
  headroom, and names no household.
- A THIRD refusal, found in the doing: seven household cards are still NAMED a letter-list
  name while their person's `letter_list_only` has been correctly cleared, and one of them
  (`hh_bradford_harriet`) is seated on a Randolph roof. Neither statement is published; the
  stale naming is filed as T-1689.
- No mesh moves — `generators/mesh_inputs.py` hashes archetype parameters, not prose — so
  this piece is bake-free even though the parent is not.
- **Visible:** the Keepers row on fourteen building cards a visitor opens on the Randolph
  and Washington blocks.
- LIBERTIES: L276 restated, 9 → 23.

**Stop condition:** no Randolph seat of the platted deal is silent in both directions.
