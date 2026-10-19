---
id: T-1792
title: Scale portable humans beyond the first NPC: browser LOD, culling, animation budgets and population assembly
state: claimed
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-09-30
closed: null
pr: null
claimed_by: parallel human population budgets 10/18/2026, 10:06:51 PM CT
blocked_on: null
needs_bake: true
closed_at: null
claimed_run: https://github.com/kevinrhaas/chicago/pull/1041
claimed_at: 2026-10-19T03:06:51.995Z
decision: null
decision_answer: null
---

After one accepted period-qualified person proves the path, make the same architecture safe for a living town rather than
copying a hero-cost actor hundreds of times. Implementation target:
`kevinrhaas/chicago` **dev**.

**Acceptance:**

- Add a population assembly layer that combines shared bodies/heads/hair/garments/material
  variants with existing person IDs and historical metadata. Named people may override
  components; anonymous visual variety must not mint historical residents or facts.
- Establish measured distance tiers for close interactive, nearby animated, street-crowd
  and distant representation. Gate facial morphs, shadows, update frequency and animation
  by tier; cull actors not relevant to the camera/scene.
- Reuse loaded skeleton/mesh/texture resources and clone safely. Investigate GPU/CPU
  instancing or baked animation only where compatible with skinned people and the current
  three.js runtime; choose from measurements rather than assuming every crowd technique
  fits.
- Benchmark representative counts on Full/Balanced/Light and mobile/desktop, recording
  frame time, draw calls, triangles, animation CPU, GPU memory and shipped bytes. Define
  enforceable budgets for the next human-population tickets.
- Prevent the People directory and scene actors from diverging: actor selection resolves
  the canonical person record; scene-year and review restrictions remain authoritative.
- Keep the export/runtime data engine-neutral. Document what Unreal can later consume
  directly and what runtime behavior will need an Unreal-specific implementation, without
  moving canonical assets or person state into Unreal.

**Stop condition:** the next programme can add more named residents and ambient street
population using measured budgets and reusable assets rather than revisiting the pipeline.

## Depends on — owner steering, 2026-10-18

T-2672 policy and the portable asset/export/runtime prerequisites still apply. Prefer an accepted asset based on an existing attested, inferred or reconstructed person and record its period/wardrobe eligibility and measured browser cost. Mark Beaubien (T-2675) is one suitable route, not a mandatory identity for all work. If no suitable existing person can serve, T-2823 permits a specifically documented anonymous adult fallback with accepted period-qualified asset/wardrobe and a recorded no-suitable-person basis. An empty-eligibility profile, CI fixture or unreviewed placeholder cannot satisfy this prerequisite. No resident records or facts may be invented to populate the scene.
