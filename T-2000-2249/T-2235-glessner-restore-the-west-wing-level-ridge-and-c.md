---
id: T-2235
title: Glessner: restore the west-wing level ridge and courtyard awning after T-2231
state: done
epic: SOUTH_TIME
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-10-08
closed: 2026-10-08
pr: 557
claimed_by: run 10/8/2026, 9:42:05 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-09T04:05:34Z
claimed_run: null
claimed_at: 2026-10-09T02:42:05.369Z
decision: null
decision_answer: null
---

Glessner: restore the west-wing level ridge and courtyard awning after T-2231.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 149 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> Explicit owner-reported regression in T-2231; immediate correction of the west-wing ridge, south gable and courtyard eave, separate from the held broad audit.

**Acceptance:** Restore a single level west-wing ridge at the existing front peak's height through to the rear/south gable. Reconcile the prior connected-roof diagram and all relevant west/northwest/courtyard references with the owner's new screenshot; do not preserve the mistaken 25.5-ft rear peak from T-2231. Provide a projecting roof eave/awning on the courtyard side, consistent with the adjoining north courtyard eave. Keep the measured footprint and recent openings/glass/courtyard-bay fixes. Validate actual rebuilt full/light geometry from courtyard, overhead, south, west and northwest, including explicit whole-ridge height, end-gable, courtyard eave and window-clearance checks. Record reconstructed controls and any revised interpretation. Run repository and applicable published desktop/mobile checks, merge to dev, and verify deployment.

**Completed:** PR #557 merged to dev as `d5aea1daff6c2b237136006bd675f12896f3a2ff` on 2026-10-09T04:05:34Z. All 794 source checks, published desktop/mobile stage 13 (126 each), and the GitHub source/browser/report checks passed. Full/light actual-model and photo/diagram comparisons are in `docs/RESEARCH/glessner-courtyard-roof-2235/README.md`. This ticket alone was settled from the verified merged-PR receipt because the tickets repository settlement workflow was failing; no other ticket state was changed.
