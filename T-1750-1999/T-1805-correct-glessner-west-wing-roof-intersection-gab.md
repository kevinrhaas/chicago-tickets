---
id: T-1805
title: Correct Glessner west-wing roof intersection, gable openings and sidewalk corner
state: done
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-10-01
closed: 2026-10-01
pr: 230
claimed_by: run 10/1/2026, 9:06:57 AM CT
blocked_on: null
needs_bake: true
closed_at: 2026-10-01T19:16:49Z
claimed_run: null
claimed_at: 2026-10-01T14:06:57.735Z
decision: null
decision_answer: null
---

Correct Glessner west-wing roof intersection, gable openings and sidewalk corner.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 145 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> Owner-reported visible defect in the shipped Glessner model, with supplied reference photos and sidewalk screenshot; the original Glessner ticket is already done.

**Acceptance:** The 18th Street roof resumes at both feet of the stable gable, with a source-bounded pitch and the loft/pigeon openings aligned beneath the peak. No north-range roof skin crosses the gable face or its openings. The sidewalk corner has no raised projecting patch. Rebuild full/light models, inspect north/northwest/elevated views at desktop and mobile sizes, run repository gates, and merge a green PR into dev.

**References:** Owner attachments 7BDB6525 (historical north-west view), EDA9BB5B and D020980B (current app roof), 15E6A751 (sidewalk), received 2026-10-01. Compare existing public-domain HABS photographs 1 and 15; retain 1904 openings rather than the 1946 replacements.

**Recovery:** Branch `steward/glessner-west-roof-repair`. Push periodic verified checkpoints and record any incomplete bake or validation explicitly.

## Recovery — 2026-10-01

Owner requested continuation of the interrupted session on the same branch. Recovered both remote source checkpoint `e643f977` and the later local full/light bake, cornice trim, sidewalk depth-bias correction and completed Blender review renders. The earlier CI bake failed at 208,041 light triangles; the recovered correction measures 196,687 against the unchanged 200,000 limit. Package and mesh-staleness checks pass. Full source gate and published desktop/mobile browser verification are still outstanding; no PR or merge is claimed yet.

Recovery update: PR #230 is open as a draft. Full preflight passed with all 717 source checks green. Published mobile/desktop checks are running on GitHub; a subsequent dev merge is being integrated before final validation. Production promotion remains out of scope.

## Completed — 2026-10-01

Recovered repair merged into `dev` as `750391af` in [PR #230](https://github.com/kevinrhaas/chicago/pull/230) at 19:16:49 UTC. Gable/eave return, opening alignment, roof intersection, alley cornice and sidewalk depth artifact are corrected; full/light models rebuilt and reviewed from north, northwest and alley, including portrait views. Light remains 196,687 triangles under 200,000. Final source gate [36911663962](https://github.com/kevinrhaas/chicago/actions/runs/36911663962) passed all 719 steps on `b9da9dc2`. Published desktop/mobile Chromium coverage passed with zero page errors; final affected-stage runs [36905832670](https://github.com/kevinrhaas/chicago/actions/runs/36905832670) and [36904172019](https://github.com/kevinrhaas/chicago/actions/runs/36904172019) report zero misplaced structures. Complete dated receipts are in `tools/dev-smoke-state.json`, review renders and reproducible geometry are committed, and PR #230 records the narrowly scoped integration fixes. Photo-derived dimensions remain reconstructed under L305. Production promotion remains owner-controlled.
