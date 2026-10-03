---
id: T-2016
title: Reconcile Glessner connected roof plan, courtyard bay and north chimneys
state: review
epic: META
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-10-03
closed: null
pr: 334
claimed_by: run 10/3/2026, 1:09:24 AM CT
blocked_on: null
needs_bake: true
closed_at: null
claimed_run: null
claimed_at: 2026-10-03T06:09:24.138Z
decision: null
decision_answer: null
---

Reconcile Glessner connected roof plan, courtyard bay and north chimneys.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 214 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> Owner requested one coordinated repair after T-1999 merged; the new aerial reference supersedes the lower rear roof and adds roof continuity and courtyard bay junction corrections.

**Acceptance — one connected-roof demonstration:**

- The north ridge runs straight to the west wall, with planar courtyard slopes.
- The stable roof runs at the north gable ridge height to a solid south gable, with a complete courtyard-facing slope; retain the prior north openings, west window schedule and stone courses.
- The stable turret sits at the roof intersection. The west dormer connects continuously to its host roof and carries matching ridge decoration.
- Review the Prairie Avenue research archive for the two missing north-range courtyard chimneys; record evidence and any reconstruction.
- Connect the round courtyard bay's copper cap to the paired triangular tiled roofs; continue copper through the inside east/north courtyard corner without a gap (owner follow-ups).
- Bake full/light models, inspect overhead/north/west/south/courtyard views and published desktop/mobile, pass relevant geometry and source gates, PR/merge into dev.

## References and recovery

Owner-supplied Pasted Graphic 30.png (current dev model) and Pasted Graphic 31.png (aerial roof reference), conversation 6ac01267-0258-83ea-b4df-13cd2d4befa1; continue merged T-1999 / chicago#306. New aerial controls connected roof topology; earlier west elevation fabric remains applicable. Modern-image topology is reconstructed for 1904, not represented as surveyed historic roof dimensions.

Work branch: steward/t-2016-glessner-roof-plan. Push implementation and review checkpoints periodically.

## Review checkpoint

PR chicago#334 contains the connected roof model, full/light assets, roof-plan drawing and exported/browser views. The owner later allowed skipping the two service stacks if their absence in 1904 could reasonably be established. The archive review did not establish that absence; the stacks remain explicitly reconstructed, with their historical dating unresolved.

750 source checks and initial preflight pass. Desktop/full and mobile/light load, review and detail switching pass with no page errors, failed requests or loader problems. Integration with newer dev commits and official stage 13 are in progress; the PR remains draft until those checks finish.
