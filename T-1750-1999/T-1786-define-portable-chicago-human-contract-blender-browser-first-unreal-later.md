---
id: T-1786
title: Define the portable Chicago human contract: Blender masters, browser GLB first, Unreal export later
state: open
epic: RENDERING
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: null
opened: 2026-09-30
closed: null
pr: null
claimed_by: null
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: null
decision: null
decision_answer: null
---

Owner-requested start of the **portable humans** programme. The Chicago 4D project must
not make MetaHuman, Unreal Control Rig, Unreal materials, Unreal groom hair or any other
engine-specific representation the canonical person. Author once in Blender, render first
in the existing browser/three.js Chicago 4D runtime, and preserve a clean path to Unreal
later.

Implementation target is `kevinrhaas/chicago` **dev**.

**Acceptance:**

- Publish `chicago/4d/docs/HUMAN-ASSET-CONTRACT.md` defining the canonical source and
  export contract: Blender `.blend` masters; metres and axis conventions; rest pose;
  skeleton/bone names and hierarchy; skin weights; material slots; UV policy; facial
  shape-key/morph names; animation clip naming; attachment points; collision/interaction
  bounds; identity metadata; historical-confidence/provenance fields; and LOD naming.
- Define one stable humanoid skeleton intended to serve ordinary residents and named
  historical people. The contract must distinguish appearance, animation and behavior so
  a person record is not welded to a renderer or engine.
- Define browser delivery as glTF/GLB, with Meshopt where supported and KTX2 only after the
  renderer actually configures `KTX2Loader`; document the current loader constraint in
  `web_derivatives.sh` rather than shipping an asset the browser cannot open.
- Define an Unreal handoff without making Unreal authoritative: FBX and/or glTF export from
  the same Blender master, stable skeleton names, textures and animation clips. No ticket
  in this programme may require MetaHuman assets to complete.
- Define a compact human-instance schema that binds a visual asset to the existing person
  ID and supports position, orientation, current animation/state, interaction flags,
  clothing/material variants, LOD policy and provenance. It must be usable by 1835 now and
  other years later.
- Add validation fixtures/tests for the schema and contract. A future exporter must fail
  clearly on incompatible skeletons, missing required material/morph channels, duplicate
  clip names, non-metric scale or missing provenance/licensing.

**Stop condition:** the next tickets can build a Blender human and a browser actor without
making new naming, skeleton, coordinate, identity or engine-portability decisions.
