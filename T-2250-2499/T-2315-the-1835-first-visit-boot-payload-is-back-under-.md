---
id: T-2315
title: The 1835 first-visit boot payload is back under its 13 MB budget — dev publishes 14.513 MB, so smoke (desktop, 1-2) is red on every PR
state: claimed
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-10-10
closed: null
pr: null
claimed_by: run 10/10/2026, 7:31:27 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38052046036
claimed_at: 2026-10-10T12:31:27.824Z
decision: null
decision_answer: null
---

The 1835 first-visit boot payload is back under its 13 MB budget — dev publishes 14.513 MB, so smoke (desktop, 1-2) is red on every PR.

## FILED ABOVE BAND 9, BECAUSE IT BLOCKS

A follow-up goes to the foot of band 9 unless dev's gate is red on it or the build in hand cannot finish without it (owner, 2026-09-27). This one was placed above band 9 on this reason:

> dev's own published mirror fails measure_boot_payload.mjs --check (14.513 MB > 13.000 MB), so the content build's smoke (desktop, 1-2) is red on every PR whatever its diff — #643 measured byte-identical to dev

## Measured (2026-10-10, while lapping #643)

`./tools/publish.sh && node tools/measure_boot_payload.mjs --check` on `origin/dev` at `8e1634d54` (after #640 T-2270, #641, #645, #647): **14.513 MB > 13.000 MB**, exit 1. #643's head (`fc3d137`, which serves no new asset) gives the same total and an identical by-folder table, so the red belongs to dev. Heaviest folders: `/data/gltf/` 4.885 MB (687 files), `/data/sidecars/1835/` 3.739 MB (694), `/data/textures/chicago_1835_pbr/` 2.652 MB (20), `/walk/js/` 0.890 MB. Largest file: `terrain__e1834_harbor_cut.glb` 1.258 MB. CI shows it as `smoke (desktop, 1-2)` failing in its "Enforce the first-visit boot payload budget" step, run 38049641977.

Find which landing crossed 13 MB (bisect `measure_boot_payload.mjs` over the last dev merges), then bring the first visit back under budget by deferring or shrinking what it loads. Never raise the budget to pass: docs/SITE-BUDGET.md §4 is the project's number.

**Acceptance:** `node tools/measure_boot_payload.mjs --check` passes on a freshly published dev mirror, and the merge that crossed the line is named in the PR.
