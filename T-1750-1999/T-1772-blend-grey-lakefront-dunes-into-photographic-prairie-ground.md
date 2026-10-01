---
id: T-1772
title: Blend grey lakefront sand and gentle dune ridges into photographic-quality prairie grass without a sharp beach boundary
state: open
epic: GROUND
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-09-30
closed: null
pr: null
claimed_by: null
blocked_on: T-1769
needs_bake: true
closed_at: null
claimed_run: null
claimed_at: null
decision: null
decision_answer: null
---

Owner request, 2026-09-30: keep the fort's sandy setting, extend the shoreline character north and south along the lake, make it greyer, and blend a gentle dune-like ridge into grassy prairie. Improve the ground and prairie appearance throughout the 1835 scene in one shared terrain/vegetation treatment run.

**Acceptance:**
- Audit existing shoreline/heightfield evidence and soil/vegetation research; retain the historical lake edge, fort grades and river mouth. Use Chicago evidence to constrain sand extent and landforms; grey tone, ridge scale and unmeasured transitions are labelled reconstruction. Do not copy today's filled shoreline or assume uniform dunes along every reach.
- Carry natural subdued grey/buff sand along appropriate modelled lakefront reaches north and south of the fort, with restrained damp/dry differences, gentle irregular ridges and hollows where supported. Shape actual terrain where silhouette requires it, never just a bright beach stripe.
- Blend exposed sand through sparse dune vegetation and sandy soil into denser prairie using broad irregular spatial masks with fine patch variation. Avoid a hard sand/grass line, rectangular masks, repeating noise and sudden vegetation walls. Preserve local paths, worn work zones, wet ground and water exclusions.
- Consume T-1769/T-1450 assets through the ground/vegetation pipeline: physical texture scales; aligned albedo/normal/roughness; restrained grain and varied grass heights, clumps, tones, density and bare-soil exposure appropriate to July. Extend the demonstrated shared treatment across prairie ground; the distant landscape still reads as land (T-1631), with stable Light coverage and no shimmer or abrupt LOD popping.
- Inspect published walker views at the fort, north and south lakefront, the sand-to-prairie transition, a town-edge prairie closeup and aerial/wide views. Before/after comparisons must show both more natural relief and softer transitions. Record the Glessner techniques adapted and why the result reaches the photographic-quality benchmark.

**Stop condition:** the lakefront reads as a continuous natural sand/vegetation landform merging into prairie, and near/far prairie reads convincingly at both viewports; no sharp beach band, floating vegetation or newly flooded horizon.

**Owner's comparative references** (inspect these images; they are analogues, not Chicago-specific attestation):
- [St Louis Front Street, 1840](https://github.com/kevinrhaas/chicago/blob/main/chicago/reference/images/st_louis/st_louis_front_street_1840.jpg)
- [Detroit Jefferson Avenue at Griswold, 1837](https://github.com/kevinrhaas/chicago/blob/main/chicago/reference/images/detroit/detroit_jefferson_ave_griswold_st_1837.jpg)
- [Cincinnati Fourth Street east from Vine, 1835](https://github.com/kevinrhaas/chicago/blob/main/chicago/reference/images/cincinnati/cincinnati_wild_fourth_street_east_from_vine_1835.jpg)
- [Cincinnati Fourth Street west from Vine, 1835](https://github.com/kevinrhaas/chicago/blob/main/chicago/reference/images/cincinnati/cincinnati_wild_fourth_street_west_from_vine_1835.jpg)


**Common visual release requirement:** photographic quality, meeting and aiming to surpass the promoted Glessner House v4 benchmark (PR #201/#202 in the code repo). Read its texture research, material library and final QA alongside T-1769, T-1450 and `docs/RESEARCH/materials.md` / `texture_library.md`. Transfer reference-led iteration, metric texture scale, layered variation, physical relief and controlled lighting rather than mansion materials. Inspect actual exported/runtime output at 390×780 and 1280×800, close and context distances under fixed lighting/exposure, with reference comparisons and a written critique. Correct visible defects before closure; automated green checks or offline beauty renders alone do not meet this standard. Measure frame time, draw calls, triangles and texture memory before/after at worst stands and all detail tiers; preserve the Light floor and shared batching. Keep provenance/rights, tiers, seeds and reproducible recipes. Push interim commits so another run can resume. Needs bake includes changed terrain/model derivatives; publish the actual result and recheck collision/height sampling.

**Queue placement:** owner-requested scene improvement beside the finish preparation, below the current 5C builds. This is substantive city rendering work, not a loop follow-up.
