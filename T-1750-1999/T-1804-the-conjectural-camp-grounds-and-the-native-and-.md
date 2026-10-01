---
id: T-1804
title: The conjectural camp grounds and the Native and Métis camps: the land-sale crowd south of the fort, the immigrants' wagons at the west approach, and the trading families from T-1177's evidence (review_required + touches_removal), with the screenshot from the fort's south-west corner
state: open
epic: TOWN
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-1214
opened: 2026-10-01
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

The conjectural camp grounds and the Native and Métis camps: the land-sale crowd south of the fort, the immigrants' wagons at the west approach, and the trading families from T-1177's evidence (review_required + touches_removal), with the screenshot from the fort's south-west corner.

Piece 2 of 2 of **T-1214 — Build the camps of the summer of 1835: a tent and wagon-camp archetype, the encampments on the grounds the transient ticket evidenced — the land-sale crowd south of the fort, the immigrants' wagons at the west approach, the pier gang at the river mouth — bounded, labelled, and empty of figures**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

## Handed on from T-1803 (2026-10-01)

T-1803 shipped the `camp` archetype (`generators/archetypes/camp.py` + `camp_params.py`:
wall/wedge tents, covered wagons, brush shelters, fire rings, woodpiles, baggage heaps;
`row`/`ring`/`scatter`) and the two landing-place camps (`landing_camp_west`,
`landing_camp_east`, L321) placed by `tools/place_landing_camps_1835.py`. What it left:

- **No `X1` family was added to the building inventory.** `family_targets` must sum to the
  668-roof total (`reprogramme_roofs_1835.py`, `reconcile_665.py`, `generate_inferred_infill.py`
  all hold it), and `1835_camp_grounds.json` rules a tent is not a building. Camps enter
  `1835_existing_roof_reconciliation.json` at zero roofs. If a camp family is still wanted, it
  belongs on a transient ledger, not in the roof programme.
- **The camp households' `lodged_at` still names the candidate ground**, not the camp records
  (`reconstruct_transients_1835.py` writes it). Pointing the 28 at `landing_camp_*` is a
  re-derivation of that stage.
- **A lodge form** is not in the archetype; add one only where T-1177's evidence describes one.
- Registering a NEW archetype in `generators/emit.py` re-stales the whole town (it is hashed
  into every mesh); the full rebake takes about two minutes here. Adding camp RECORDS needs no
  emit.py change.
