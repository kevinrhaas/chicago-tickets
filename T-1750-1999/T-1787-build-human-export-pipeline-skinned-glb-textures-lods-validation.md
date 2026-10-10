---
id: T-1787
title: Build the portable human export pipeline: skinned GLB, textures, LODs and validation from Blender to Chicago 4D
state: open
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-09-30
closed: null
pr: null
claimed_by: null
blocked_on: null
needs_bake: true
closed_at: null
claimed_run: null
claimed_at: null
decision: null
decision_answer: null
---

Build the reproducible asset path that turns the Blender source-of-truth human into a
browser-deliverable Chicago 4D asset. Implementation target: `kevinrhaas/chicago` **dev**.

**Acceptance:**

- Add a documented/reproducible Blender export path that preserves the T-1786 skeleton,
  skinning, named animation clips, morph targets, material slots, scale and attachment
  transforms in GLB. Do not require an interactive hand-export with undocumented toggles.
- Extend the existing GLB/web-derivative toolchain rather than creating a parallel asset
  island. Validate GLB structure, joint/weight counts, animation clips, morph targets,
  bounds, triangle counts, texture dimensions, material count and total shipped bytes.
- Wire Meshopt compression through the existing loader path where beneficial. If KTX2 is
  adopted, configure and test `KTX2Loader` in the actual renderer first; the existing
  `web_derivatives.sh` warning that KTX2 assets currently throw must be resolved, not
  bypassed. Preserve a safe fallback for unsupported clients.
- Support authored LOD0/LOD1/LOD2/LOD3 human exports (or an equally explicit generated
  strategy) while preserving the same skeleton/identity contract. Publish measured
  triangle/material/texture budgets for each tier rather than a guessed global limit.
- Keep source textures and licensing/provenance beside the Blender master; generated
  derivatives are reproducible and never become the only copy of an asset.
- Add one tiny non-historical rigged fixture to CI proving Blender -> GLB -> web loader:
  skinning deforms, at least one animation plays, one morph target changes, materials load,
  and every declared LOD opens without console errors.

**Stop condition:** a human asset can be built from Blender and validated/published by the
normal Chicago 4D tooling with no Unreal dependency and no manual post-export surgery.
