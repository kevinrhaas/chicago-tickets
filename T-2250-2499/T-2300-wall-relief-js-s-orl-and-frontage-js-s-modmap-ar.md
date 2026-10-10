---
id: T-2300
title: wall-relief.js's orl and frontage.js's modMap are DataTextures (flipY false) sampled beside a flipY'd normal_gl Texture, so each 1835 wall and frontage tile's AO, roughness and grain is mirrored vertically against its relief
state: review
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-10
closed: null
pr: 638
claimed_by: run 10/10/2026, 3:13:49 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38036898271
claimed_at: 2026-10-10T08:13:49.967Z
decision: null
decision_answer: null
---

wall-relief.js's orl and frontage.js's modMap are DataTextures (flipY false) sampled beside a flipY'd normal_gl Texture, so each 1835 wall and frontage tile's AO, roughness and grain is mirrored vertically against its relief.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
