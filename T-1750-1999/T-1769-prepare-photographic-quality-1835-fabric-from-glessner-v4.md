---
id: T-1769
title: Prepare photographic-quality 1835 fabric from the Glessner v4 benchmark: audit textures, transfer proven techniques and publish a reusable proof package
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
claimed_by: run 10/1/2026, 5:19:50 AM CT
blocked_on: null
needs_bake: true
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/36848142612
claimed_at: 2026-10-01T10:19:50.483Z
decision: null
decision_answer: null
---

Owner-requested prerequisite for **T-1210–T-1213**, immediately before the finish
band; existing district builds keep their order. The owner: *"we said photographic
quality and i think that is a good standard."* Glessner House v4 in 1904 is the
visual benchmark to live up to and surpass. This is one bounded preparation run
plus a proof bake, not another open-ended texture-research programme.

**Acceptance:**

- Read the promoted Glessner default and its v4 development/QA records. Extract
  the successful methods: reference-led opening/fabric audits; physical relief and
  recesses; metric UVs preserved through export; original PBR albedo/normal/roughness;
  restrained material variants; actual glass and enclosed recesses; controlled
  render comparisons; matching Full/Light architecture and browser review.
  Record corrections that worked (oversized granite grain, excessive brick mosaic,
  flat lawn, open-pane artifacts and shallow recesses), residual limitations and
  what transfers to 1835. Transfer craft and pipeline, not 1904 mansion finishes.
- Audit the existing 25-material `assets/textures/chicago_1835_pbr/` library,
  T-1450, `docs/RESEARCH/texture_library.md` and the current material sheet/runtime.
  Publish `docs/RESEARCH/1835_photographic_fabric_preparation.md` with a
  reuse/regenerate/new decision per substrate needed by the four tickets: painted,
  whitewashed and bare wood, logs/chinking, shingles/boards, period brick/mortar
  and chimney daub, plank walks, timber/iron props, signboard/paint, soil/vegetation.
  Each row names metric module/span, texel density, map channels/colour spaces,
  GL/DX convention, seed/recipe, license/provenance, historical tier, remaining gap
  and consuming ticket. Reuse existing evidence and sources; date and distinguish
  historical evidence, surviving-fabric references and generic material studies.
- Prepare or improve only the missing maps needed for **one representative proof
  assembly**: clapboard and log wall samples, a recessed sash, adjacent plank walk
  and painted signboard. Use existing maps where they work. Keep source maps,
  reproducible recipes (or original generated images with prompts/hashes), aligned
  channels, contact sheet and license entries. No baked directional lighting;
  third-party photographic pixels require usable rights, and Glessner's limited
  rights exception does not license new texture extraction.
- Bake/export that assembly through the real glTF/web-derivative path; inspect
  the actual imported GLB under fixed neutral and scene lighting, then in the
  browser at both viewports. Compare the current 1835 treatment, proposed treatment
  and Glessner baseline at comparable distances/exposure. Preserve captures and
  commands/hashes; critique scale, grain, seams, relief, glazing depth, roughness,
  colour restraint, repeat/shimmer and contact shadows. Iterate visible defects.
  The proof demonstrates reusable rendering methods, not an attested 1835 building.
- Resolve the integration difference explicitly: 1835 currently shares substrate
  relief maps with per-vertex colour/roughness; Glessner uses richer albedos and
  geometric detail on one house. Price shared albedo modulation/atlases, seeded
  variation and geometry/normal-map division; choose a demonstrated strategy that
  preserves household finish control and town batching, or document a deliberate
  measured contract revision. Supply Full/Balanced/Light costs (calls, triangles,
  textures/bytes, loading) and the consuming tickets' integration/bake steps.
  Do not apply Glessner's per-building geometry cost or Full allowance to every roof.

**Stop condition:** T-1210–T-1213 can start implementation from an inspected,
reproducible photographic-quality proof and an explicit material/integration map.
A memo or green gate alone is insufficient. Preparation does not close those
tickets or claim that the town already meets the standard. Preserve resumable
checkpoints and keep this run's scope to the common package.

**Read first** (code-repository paths relative to `chicago/4d/`):
`docs/RESEARCH/glessner_house_v4.md` · `docs/RESEARCH/glessner_v4_work.md` ·
`assets/textures/glessner-v4/README.md` and `material-library.json` ·
`generators/archetypes/masonry_house_v4_detail.py` and `masonry_house_v4_materials.py` ·
`docs/RESEARCH/glessner-v4-qa/refined-06-final-review.md` and `default-promotion.md` ·
`tools/_glessner_lod.py` · `assets/textures/chicago_1835_pbr/RESEARCH_NOTES.md` ·
`docs/RESEARCH/materials.md` · `docs/RESEARCH/texture_library.md` · T-1450.

**Glessner implementation:** [PR #201](https://github.com/kevinrhaas/chicago/pull/201),
[promotion #202](https://github.com/kevinrhaas/chicago/pull/202);
[1904 default](https://chicago.polecat.live/4d/dev/1904/?anchor=glessner_house&structure=glessner_house).


## Ground and worn-plank extension — owner, 2026-09-30

The preparation also serves T-1770–T-1772: audit the existing soil, mud, sand,
riverbank and prairie maps (T-1450 explicitly deferred the ground integration).
Include a compact ground strip adjoining the existing proof assembly: full-width
packed dirt with irregular wear, worn bank soil, subdued grey/buff sand blending
into sparse grass and prairie. Prove multi-scale masks and the selected maps in
the real terrain/runtime-canvas path; do not bind building materials to ground
without a demonstrated integration change. Supply reusable recipes and measured
costs; the consuming tickets own citywide grading, docks and rollout.

The proof's plank walk must be worn grey/brown/grey-brown/dark grey-brown, varied
by owner/use, with grain, worn edges and grime. No default white boards, and no
lit bleaching back to white. Pass these palette/roughness findings to T-1211 and
T-1770–T-1771. This extension is part of the same bounded proof package, not a
new open-ended research programme.

## Reference and integration handoff — 2026-10-01

Read [the ground photographic-quality brief](../evidence/1835-ground-photographic-quality-brief.md)
for the inspected peer-city views, current renderer findings and limits on transferring
Glessner's lawn techniques to July prairie. Its material and runtime findings belong
in this package's reusable decisions and compact proof, rather than a second research
programme. The consuming tickets retain responsibility for grading and citywide rollout.
