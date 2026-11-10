---
id: T-3535
title: Use conservative shadow culling at Balanced detail
state: claimed
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-10
closed: null
pr: null
claimed_by: run 11/10/2026, 1:41:53 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-10T07:41:55.510Z
decision: null
decision_answer: null
---

Use conservative shadow culling at Balanced detail.

## FILED ABOVE BAND 9, BECAUSE IT BLOCKS

A follow-up goes to the foot of band 9 unless dev's gate is red on it or the build in hand cannot finish without it (owner, 2026-09-27). This one was placed above band 9 on this reason:

> T-3533 cannot pass the published desktop stage 5 gate: Balanced exceeds its unchanged triangle ceiling. The existing culler saves 66537 triangles at the failing view with zero changed pixels.

**Acceptance:**
- Balanced enables the existing conservative shadow-caster filter used by Full and Light; scene geometry, reaches, densities and ceilings are unchanged.
- The published 1835 West prairie view remains pixel-identical with the filter off/on, with a positive control that detects removed shadows, and falls below the existing Balanced triangle ceiling.
- Published stage 5 passes across all six stands and both release viewports; existing shadow-culling controls pass.
- The measured receipt and final smoke results are retained, and the PR remains unmerged until validation is green.
