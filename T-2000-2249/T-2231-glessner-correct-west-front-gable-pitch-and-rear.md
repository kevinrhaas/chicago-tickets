---
id: T-2231
title: Glessner: correct west front gable pitch and rear width from owner photographs
state: review
epic: SOUTH_TIME
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-10-08
closed: null
pr: 553
claimed_by: run 10/8/2026, 7:36:13 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-09T00:36:13.518Z
decision: null
decision_answer: null
---

Glessner: correct west front gable pitch and rear width from owner photographs.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 149 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> Explicit owner correction selected for immediate work; bounded west/northwest geometry repair while the broader audit group remains manually held.

## Acceptance

Correct the taller front west gable slope and its transition to the lower rear section using the two owner-supplied west and northwest images (9 October 2026). The owner clarified that the front gable angle is the roof defect. Keep the measured stable footprint; correct the relative frontage allocated to the tall gable and rear roof. Record any inferred/reconstructed dimensions explicitly.

Validate actual rebuilt full/light geometry against both references, with repeatable west and northwest before/after renders and a control-point/proportion table. Check roof continuity and aperture clearances, preserve the recent courtyard/window/dark-glass work, run repository source and applicable published desktop/mobile gates, then merge into dev. No production promotion.

This is the specifically authorized repair; the broader T-2206 audit and other manually held programme tickets remain held.

## Implementation and validation

PR #553 corrects the west front gable to approximately 36/53-degree slopes,
with its apex at 30.8% of the measured frontage and the rear section at 41.4%.
The measured footprint remains fixed. The lower roof, cornice, northwest
shoulder, dormer and cupola follow the revised profile. These are explicitly
reconstructed photographic proportions.

Final actual-model west and northwest views were compared with both owner
references. Full/light assets and the recovery package are rebuilt. Roof and
masonry/glass tests, focused published desktop/mobile review, and both published
stage-13 smoke runs pass (126 checks each). Final preflight integrated with dev
35dae52e passes all 792 repository steps. Browser receipts state their timing
relative to the independent dev updates; Glessner geometry is unchanged.

[Before/after views and receipts](https://github.com/kevinrhaas/chicago/blob/6c7fa0925de800fd368563d721bdfb68380ec050/chicago/4d/docs/RESEARCH/glessner-west-profile-2231/README.md).
[Dev PR #553](https://github.com/kevinrhaas/chicago/pull/553). The PR's merge is
the completion receipt; production promotion is outside this repair.
