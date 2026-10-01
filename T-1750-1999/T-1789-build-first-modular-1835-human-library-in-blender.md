---
id: T-1789
title: Build the first modular 1835 human library in Blender on the shared portable rig
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
blocked_on: T-1786
needs_bake: true
closed_at: null
claimed_run: null
claimed_at: null
decision: null
decision_answer: null
---

Create the reusable Blender-side human kit from which named and ambient 1835 residents
can be assembled. The checked/reproducible Blender assets are canonical; browser GLBs are
exports, and Unreal is a later consumer. Implementation target: `kevinrhaas/chicago` **dev**.

**Acceptance:**

- Build a clean shared-rig Blender library with a bounded first set of adult body/head
  bases, period-appropriate hair/facial-hair options and modular garments/accessories
  sufficient to produce visibly different 1835 residents without unique modelling for
  every person.
- Begin with reusable period categories, not a costume catalog: shirt, waistcoat, trousers,
  work/outer coat, dress/skirt/bodice forms, apron/shawl and common hat/bonnet families as
  evidence supports. Keep garments swappable on the T-1786 skeleton with controlled skin
  weights and clipping checks.
- Use reusable PBR materials/atlases and restrained variants for skin, hair, linen/wool/
  cotton/leather/wood/metal as appropriate. Keep material-slot count and transparency
  modest; prefer hair cards/geometry suitable for the browser over expensive strand hair.
- Record provenance and rights for every base mesh, texture, brush or source asset. Prefer
  project-authored or clearly redistributable inputs; do not introduce a human generator
  whose license prevents publishing the browser derivative.
- Author LODs following T-1787's measured contract. Close views retain hands/face and
  silhouette; distant tiers simplify hair, fingers, garment detail and materials without
  changing the person's scale or identity.
- Provide a Blender collection/assembly recipe and at least three deliberately different
  anonymous test residents rendered in Blender and exported through the real Chicago GLB
  path. These are pipeline proofs, not historical assertions or new residents.

**Stop condition:** Mark Beaubien can be built mostly by assembling/refining this library
rather than creating an unrelated one-off rig.
