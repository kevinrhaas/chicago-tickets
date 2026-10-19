---
id: T-1789
title: Build the first modular 1835 human library in Blender on the shared portable rig
state: claimed
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-09-30
closed: null
pr: 1046
claimed_by: generic-human-master 10/18/2026, 3:42:42 PM CT
blocked_on: null
needs_bake: true
closed_at: null
claimed_run: null
claimed_at: 2026-10-18T20:42:42.076Z
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
  test residents rendered in Blender and exported through the real Chicago GLB path.
  Prefer existing attested, inferred or reconstructed person records as references and
  model assignments. Anonymous figures are permitted only when no suitable existing
  person can be used (owner, 2026-10-18). Pipeline proofs never mint new biographies or
  upgrade reconstructed identities or appearance into attested likenesses.

**Stop condition:** Mark Beaubien can be built mostly by assembling/refining this library
rather than creating an unrelated one-off rig.

## Owner steering — 2026-10-18

“Ok generally if you can use assign existing attested inferred or reconstructed people
as the reference and model, don’t make generic people unless you have no other choice.”

First study references: rc_bardwell_otis (teamster20–29), rc_dufresne_joseph
(livery stable keeper30–39), rc_flynn_martin (teamster30–39), all already reconstructed
in the1835 dataset. Body/skin/garment choices remain separately reconstructed. Two
adult shape studies and color variants do not complete the different-person or
photographic-quality acceptance. The checked code checkpoint is e6f72ceb489dd625554dcabdbaced064c0b7e214,
pushed to steward/generic-teamster-humans in draft PR1046. Full local preflight
passed all973 steps, zero failed, plus changelog and ticket-ID checks. Canonical
CI build39168738942 is running; no actual resident GLB acceptance, new scene
instances or named likenesses are claimed.

## Checked preparation follow-up

Commit6ae3c766f174546a53c34db02c024abfd2667517 is pushed in PR1046 after
all973 checks/preflight passed. It fixes the reproduced Python3.11/3.12 reduction
difference without weakening exact-byte comparison. Eleven source tests pass; all
three inputs also reproduce with Python3.13. Corrected canonical CI39169918123 is
running. No actual resident exports or photographic/driver acceptance yet.


## Actual surface authoring failure, 2026-10-19

2679d6c98 local preflight991/0 and postcommit changelog passed, but canonical39184480142 failed on the first resident body custom-normal readback guard. Numeric error was not logged before raise; later resident master/export/hair/hierarchy/browser checks skipped. Legacy fixture job passed separately. Bounded diagnostic-only code now precedes the unchanged1e-3guard in the combined PR1041 WIP. Pinned Blender codec analysis proves1e-3 is not a universal quantizer bound under ordinary ideal frames, but supplies no complete floating-point/fallback replacement or actual resident error/seam measurements. No threshold waiver or photographic acceptance. Failure logs/source analysis and unapplied alternatives are archived beside CHECKPOINT.md. PR1046 is a preserved source checkpoint for consolidation, not a separate merge target.
