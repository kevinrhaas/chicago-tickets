---
id: T-1792
title: Scale portable humans beyond the first NPC: browser LOD, culling, animation budgets and population assembly
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

## Parallel checkpoint — 2026-10-19

Actual fixture desktop/mobile 12 cases pass functional skin/morph, scheduling and logical resource cleanup, including disposal during pending parse. One mobile framing gap remains. Outside-app source archive follows; no named-resident/photo or town admission acceptance. See evidence/period-transport-2026-10-18/parallel-refinement-2026-10-19/ and CHECKPOINT.md. PR1041 remains draft; conditional dev merge awaits green final-head gates.

**Released 2026-10-21** (claim of parallel human population budgets 10/18/2026, 10:06:51 PM CT): Claims audit: reopen stale inactive work; reference and carriage work immediately reassigned individually for independent parallel completion

## The crowd stage of the photographic-humans plan (owner, 2026-11-06)

Kevin agreed the plan "Photographic humans: the path" (https://claude.ai/artifact/V87s9knPesndaBs2C5aLgq):
"Agreed on your recommendations, proceed". Its stage 6, a crowd at a phone's cost, belongs to this ticket:
far people as impostor cards from one shared atlas, middle-distance people as instanced animated
meshes sharing one body, and full skinned, draped figures only near the camera. It comes after the
people memory pool (T-3408) is freed, and after a handful of people are done fully
(T-3409, T-3410, T-3412..T-3417).
