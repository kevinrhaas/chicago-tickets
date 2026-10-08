---
id: T-2171
title: 1812: remove the unsupported lake-facing notch at the sand spit
state: claimed
epic: TERRAIN
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-10-08
closed: null
pr: null
claimed_by: shoreline-session 10/8/2026, 4:04:54 AM CT
blocked_on: null
needs_bake: true
closed_at: null
claimed_run: null
claimed_at: 2026-10-08T09:04:54.964Z
decision: null
decision_answer: null
---

1812: remove the unsupported lake-facing notch at the sand spit.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 154 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> Direct owner-requested correction after map comparison; preserve the southward river channel.

**Acceptance:** continuous lake-facing shoreline at the 1812 sand spit, with the river-side bank, southward bend and outlet unchanged; exact join labelled reconstructed with map comparison and liberty; regenerate terrain and compressed assets; green check/preflight and published desktop/mobile 1812 validation; merge to dev.

## Recovery checkpoint

Owner approved correction after comparing Whistler 1808, retrospective Andreas 1812, Harrison 1830 and Wright 1834. The current 100 ft ribbon plus root-to-north-shore chord creates the unsupported V-shaped lake notch. Work branch: `steward/1812-lakeshore`, based on dev b6aef1c7. Replace only the outer lake join with a bounded smooth curve; preserve the river-side offset and lower spit. No exact 1812 contour is claimed.

## Implementation checkpoint — 2026-10-08 09:30 UTC

The continuous outer curve is implemented locally, preserving the river-side attachment, outlet and every lower-spit vertex. Pinned Blender 4.5.3 rebuild passed: max 6 mm mesh/heightfield error over 210,897 rays, zero misses. Published /1812/ desktop/full and mobile/light both pass with zero page errors or failed responses; the old notch samples at +1.23 m while retained river/lake samples remain underwater. Mobile stage-3 smoke: 103 passed, 0 failed. Desktop smoke and final sequential full gate are still running. L403 and source-use records are updated.

GitHub connector payload ceiling prevents a direct 30 MB terrain-master upload. A lossless xz copy (sha-verified) has been uploaded as blob 8474a94ce75a7d6d87e6b90599d29f4b20f7422b. Planned branch-only transfer receipt in tools/bake.sh lets the existing bake workflow materialize and push that exact blob, with the full gate still required; remove receipt/archive before dev merge. Do not merge a partial transfer tree. Worktree: /workspace/scratch/4cc376320721/chicago-shore.
