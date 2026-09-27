---
id: T-1647
title: The Dearborn block's South Water frontage run: the bakery and the wholesale house standing in cottages at the bridge head re-familied to the store families the ground allows, migrated, baked and published
state: done
epic: TOWN
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-1639
opened: 2026-09-26
closed: 2026-09-26
pr: 103
claimed_by: run 9/26/2026, 8:06:41 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-09-27T02:50:31Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/36283733454
claimed_at: 2026-09-27T01:06:41.242Z
decision: null
decision_answer: null
---

The Dearborn block's South Water frontage run: the bakery and the wholesale house standing in cottages at the bridge head re-familied to the store families the ground allows, migrated, baked and published.

Piece 1 of 3 of **T-1639 — The South Water street line stands as stores and warehouses and not cottages: the C2-C4 store fronts and F1-F3 warehouses at the crosswalk's required variants, raised on the party lines and baked**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

**Acceptance:** (stated before working — one demonstration, never weakened to pass)

The parent asked for stores and warehouses to be RAISED on the South Water party lines.
There is no ground to raise them on, and that is this piece's first finding: the owner's
ruling of 2026-09-26 on T-1623 (option a) reserves the one genuinely vacant lot each of
`blk_south_water_dearborn` and `blk_south_water_wells` still holds, and the other three
South Water blocks stand at capacity in the 665-roof programme. So the street line's
composition can only change by re-familying what already stands on it.

Measured on the committed tree, the frontage run — the party-line row on the town's
declared business front — holds **28 roofs: 23 cottages, 5 stores, no warehouse**, while
T-0213's documented trade share on a `principal` street reads 0.65. Two of those cottages
carry a documented trade on their own card:

- `recon_1835_blk_south_water_dearborn_d5_07`, a **deep-plan frame cottage**, is D. Graves's
  bakery.
- `recon_1835_blk_south_water_dearborn_d3_08`, a **one-room frame cottage**, is Harmon,
  Loomis & Co. — wholesale and retail dry goods, groceries, hardware and crockery.

- Both slots are re-familied in `1835_platted_block_parcels.json` to the largest store
  family the GROUND admits, and the refusal of every larger one is measured and written
  beside the deal rather than asserted. No confidence is upgraded: both roofs stay
  `reconstructed` anonymous count-units, and the occupant each carries is the one the
  business layer already gave it.
- The record ids move with the family (`_d5_07` → `_c2_07`, `_d3_08` → `_c1_08`); every
  file naming them is renamed, re-derived or refused in writing, on T-1483's taxonomy.
- Baked (`tools/bake.sh --only`) — the archetype moves from `frame_dwelling` to
  `frame_storefront`, so the mesh is stale until it is regenerated in this commit —
  published, and `check.sh` green.
- **Visible:** two cottages on the South Water frontage become shopfronts, in the view
  west along South Water from the foot of the Dearborn Street drawbridge.

**Stop condition:** no roof on this block's business front carries a documented store on a
cottage's silhouette without the record saying why.
