---
id: T-1738
title: Generate and bake the e1871_postfire heightfield and its ground and water GLBs over the Prairie Avenue reach, wired into the terrain gates
state: claimed
epic: SOUTH_TIME
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: T-1252
opened: 2026-09-28
closed: null
pr: null
claimed_by: run 9/28/2026, 1:18:10 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-09-28T18:18:10.767Z
decision: null
decision_answer: null
---

Generate and bake the e1871_postfire heightfield and its ground and water GLBs over the Prairie Avenue reach, wired into the terrain gates.

Piece 1 of 2 of **T-1252 — Generate and bake the e1871_postfire heightfield over the Prairie Avenue reach**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

1. `data/terrain/epochs/e1871_postfire/heightfield.json` + `.bin` generated from T-1251's zone table
   (`terrain_spec.json`) and T-1250's scene line (`shoreline.geojson`) over the spec's box
   (E +1100..+1800, N -3800..-2900), by a committed generator; the land never leaves the crowns'
   range, the water stands east of the scene line, and the confidence channel is inferred only
   inside the confirmed reach.
2. **Baked** with the pinned Blender: `assets/gltf/terrain__e1871_postfire.glb` and
   `water__e1871_postfire.glb`, their web derivatives, and `assets/manifest.json` entries whose
   `inputs_sha256` `validate.py --stale` recomputes; the mesh-versus-heightfield fit is measured and
   stated.
3. The spec's blocks are wired into the ground gates (claims on the Evidence panel's enumeration,
   `CONSUMED` reads checked against the generator, a liberty covering every reconstructed claim), and
   `check.sh` green.
4. No scene selects the epoch yet - that is T-1739 - so nothing a visitor sees changes; say so.

Split out of T-1252 on 2026-09-28 because the bake and the landing are two demonstrations.
