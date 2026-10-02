---
id: T-1988
title: The ten empty anonymous outbuildings (six stables and barns, two sheds, a privy, a stable yard on the north fringe) each given a stated use naming the seated dwelling it serves, or why it serves none, bounded by the recipe's own yard_group, the lot ledger or T-1794's farmstead pairing; the audit's outbuilding_naming_no_yard count at zero
state: done
epic: TOWN
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-1986
opened: 2026-10-02
closed: 2026-10-02
pr: 293
claimed_by: run 10/2/2026, 12:37:51 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-02T19:18:09Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37038248704
claimed_at: 2026-10-02T17:37:51.346Z
decision: null
decision_answer: null
---

The ten empty anonymous outbuildings (six stables and barns, two sheds, a privy, a stable yard on the north fringe) each given a stated use naming the seated dwelling it serves, or why it serves none, bounded by the recipe's own yard_group, the lot ledger or T-1794's farmstead pairing; the audit's outbuilding_naming_no_yard count at zero.

Piece 1 of 2 of **T-1986 — The anonymous programme roofs left empty (stables, barns, sheds, a privy and four trade buildings) each tied to the dwelling or establishment it serves by T-1980's part_of, or given a stated use, the audit's empty count at zero**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

**Acceptance:** (stated before working)

`python3 tools/audit_town_completion_1835.py` reports `occupied.empty_owing_somebody.outbuilding_naming_no_yard` at **0**, and none of these ten ids in `occupied.empty`: recon_1835_north_a1_047, recon_1835_south_a2_037, recon_1835_west_012, _013, _022, _023, _024, _025, _053, _055. Each one gets a row in `data/reconstruction/1835_stated_uses.json` (T-1782's ledger, spent by tools/inferred_occupancy.py through the generator that owns the roof). Its `serves` is a SEATED dwelling only where something committed ties the two: the West recipe's own `yard_group`, a shared lot in the lot ledger, or T-1794's farmstead pairing. Where nothing does (the north fringe's stable yard, the T-1781 stable on the teamster approach), `serves` is null and the row says so. No row names a person or a household. The generators' `--check` stays drift-free, check.sh is green, and the outbuilding's card shows the stated use.

**Acceptance, amended in the run with its reason (a finding, not a weakening):** nine of the ten get their stated use, and `outbuilding_naming_no_yard` stands at **1**. The tenth, recon_1835_west_013, must not be given one: the roof redeal re-families it to a D2 dwelling, and a stated use would seat nobody there while blocking that refamily. It is carried on T-1989 (see the section there).
