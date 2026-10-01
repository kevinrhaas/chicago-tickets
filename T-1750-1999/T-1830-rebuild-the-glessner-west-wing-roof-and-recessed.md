---
id: T-1830
title: Rebuild the Glessner west-wing roof and recessed north entrance from the elevations and floor plans
state: review
epic: PRAIRIE1904
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-10-01
closed: null
pr: 243
claimed_by: interactive Glessner follow-up 10/1/2026, 4:32:52 PM CT
blocked_on: null
needs_bake: true
closed_at: null
claimed_run: null
claimed_at: 2026-10-01T21:32:52.961Z
decision: null
decision_answer: null
---

Rebuild the Glessner west-wing roof and recessed north entrance from the elevations and floor plans.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 147 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> Owner explicitly requests this follow-up after T-1805, with ten reference images; no open ticket owns this roof and entrance correction.

**Acceptance:**
- Rebuild the west-wing roof as a connected, non-overlapping envelope: full northern west-facing gable, narrower north-facing carriage gable, lower rear range, flared west dormer/hood above four alley windows, and coherent east/south elevations.
- Remove the reported gable/roof overlap and exposed duplicate roof edges; preserve the documented carriage-door/loft/pigeon axis.
- Carve the north entrance alcove with its back wall/window, front steps, left-turn stair and side-facing entry door, sized against HABS sheets 2–3 and the supplied views.
- Keep attested plan dimensions distinct from reconstructed unmeasured heights/details; record liberty and evidence. Full/light share architectural geometry.
- Rebake full/light assets and recovery archive; inspect northwest, west, east, south and north entrance views. Run source preflight and required published desktop/mobile checks before merging to dev.
- Push progress checkpoints and recovery instructions during work.

Owner supplied ten images on 2026-10-01, from image(20261001-210139).png through image(20261001-212524).png. HABS sheets 2 and 3 are included; contemporary photographs bound reconstruction without asserting that modern details are original. No source image pixels are used as textures.

## Review checkpoint — 2026-10-01

PR: https://github.com/kevinrhaas/chicago/pull/243
Branch: steward/t-1830-glessner-west-wing-alcove
Source checkpoint ece92a8; complete model/recovery commit a8fac67. Six full-model views and matching decoded light views reviewed. Planar roof and aperture regressions pass; all mesh versions are fresh and the exact package verifies. Source preflight: 727 steps, none red. Full/light architecture matches; light 188,675 triangles.

Published browser checks on the complete commit are in progress, covering mobile and desktop stages 1–6 and 7–13. Keep the PR draft until they pass; then merge only to dev.
