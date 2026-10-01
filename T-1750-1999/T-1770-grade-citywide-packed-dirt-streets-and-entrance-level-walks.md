---
id: T-1770
title: Grade citywide packed-dirt streets with irregular traffic wear and entrance-level plank walks, beginning with South Water
state: split
epic: GROUND
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-09-30
closed: 2026-10-01
pr: null
claimed_by: run 10/1/2026, 10:24:07 AM CT
blocked_on: T-1769
needs_bake: true
closed_at: 2026-10-01T15:24:52.361Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/36878737957
claimed_at: 2026-10-01T15:24:07.704Z
decision: null
decision_answer: null
---

Owner request, 2026-09-30: replace the paired-tread appearance with a full dirt roadway, graded below the building-front walking shelf. South Water is the proof station; apply the demonstrated shared rule across the modelled city in this run.

**Acceptance:**
- Inspect the four owner-supplied peer-city images below, current Chicago street/terrain/frontage generators, Chicago sidewalk notices and ordinances. Record visible observations separately from Chicago-attested geometry and labelled reconstruction. Do not copy another city's grades or dimensions as Chicago facts.
- The whole active roadway is packed earth: broad compacted traffic areas with overlapping irregular wheel tracks, hoof/foot paths, shallow ruts and restrained local mud. Remove the universal two clean parallel strips and grassy median appearance on worked urban streets; retain sparse peripheral tracks only where evidence/use supports them.
- Resolve street cross-sections from door thresholds, existing ground and frontage records: plank walk and a modest adjacent shelf at entrance level where appropriate; roadway gently graded lower with irregular shoulders and plausible drainage. Record derived widths, rises and slopes; do not import the later wholesale raising of Chicago or install modern kerbs/asphalt. Preserve attested entrances and documented sidewalks; entrances, crossings and intersections connect without floating boards, buried doors, steps into voids or abrupt terrain seams.
- Consume T-1769's ground proof, T-1450's existing mud maps and material research through the actual terrain/runtime-canvas pipeline. Keep metric texture scale, low-frequency wear masks plus fine relief, subdued dry/wet roughness variation, reproducible seeds and shared materials. Normal maps cannot substitute for cross-section geometry.
- Apply the rule to South/North/West streets and alleys with intensity by traffic/use; enumerate all modelled corridors, exceptions and reasons. Review South Water, Lake, a North street and West approach at walker height and overhead. Coordinate T-1211's plank works and T-1771's river ramps using one grade contract.

**Stop condition:** the published 1835 city's streets visibly read as full-width worked dirt with coherent entrance-level walks. Include fixed before/after browser captures and corridor coverage report; a South Water-only patch does not close citywide work.

**Owner's comparative references** (inspect these images; they are analogues, not Chicago-specific attestation):
- [St Louis Front Street, 1840](https://github.com/kevinrhaas/chicago/blob/main/chicago/reference/images/st_louis/st_louis_front_street_1840.jpg)
- [Detroit Jefferson Avenue at Griswold, 1837](https://github.com/kevinrhaas/chicago/blob/main/chicago/reference/images/detroit/detroit_jefferson_ave_griswold_st_1837.jpg)
- [Cincinnati Fourth Street east from Vine, 1835](https://github.com/kevinrhaas/chicago/blob/main/chicago/reference/images/cincinnati/cincinnati_wild_fourth_street_east_from_vine_1835.jpg)
- [Cincinnati Fourth Street west from Vine, 1835](https://github.com/kevinrhaas/chicago/blob/main/chicago/reference/images/cincinnati/cincinnati_wild_fourth_street_west_from_vine_1835.jpg)


**Common visual release requirement:** photographic quality, meeting and aiming to surpass the promoted Glessner House v4 benchmark (PR #201/#202 in the code repo). Read its texture research, material library and final QA alongside T-1769, T-1450 and `docs/RESEARCH/materials.md` / `texture_library.md`. Transfer reference-led iteration, metric texture scale, layered variation, physical relief and controlled lighting rather than mansion materials. Inspect actual exported/runtime output at 390×780 and 1280×800, close and context distances under fixed lighting/exposure, with reference comparisons and a written critique. Correct visible defects before closure; automated green checks or offline beauty renders alone do not meet this standard. Measure frame time, draw calls, triangles and texture memory before/after at worst stands and all detail tiers; preserve the Light floor and shared batching. Keep provenance/rights, tiers, seeds and reproducible recipes. Push interim commits so another run can resume. Needs bake includes changed terrain/model derivatives; publish the actual result and recheck collision/height sampling.

**Queue placement:** owner-requested scene improvement beside the finish preparation, below the current 5C builds. This is substantive city rendering work, not a loop follow-up.


## Owner correction — plank colour, 2026-09-30

Plank sidewalks must not read as white. Default to visibly worn grey, brown,
grey-brown and dark grey-brown timber, with bounded differences by owner/frontage,
maintenance, age, exposure and traffic; do not assign one uniform pale material
citywide. Show grain, end grain, board-to-board variation, worn edges, local grime
and darker damp areas without extreme random colours. A white/painted finish
requires specific supporting evidence. Inspect albedo and the lit browser result:
lighting, tone mapping and roughness must not bleach the boards back to white.
Compare adjacent owners under the same exposure; preserve documented finishes and
record inferred/reconstructed variation. Coordinate T-1770/T-1771's entrance and
ramp grades. This is an explicit closure requirement for this street ticket and T-1211.

## Implementation evidence and coverage — 2026-10-01

Read [the shared ground brief](../evidence/1835-ground-photographic-quality-brief.md).
The current `streets.js::roadTexture` explicitly draws rut bands at 0.29/0.71 and
allows prairie through the translucent road; the mesh uses `track_width_m` and
drapes existing terrain. Replace that shared rule with actual broad worked-road
coverage and a coherent graded section. Keep surveyed street positions/corridors;
enumerate opened versus merely platted corridors, and do not clear unopened land
just because it is mapped. Sand approaches retain their appropriate substrate.
Use one authoritative elevation and wear contract for rendered terrain, walker
collision, doorstep/walk connections and vegetation exclusion. Include a measured
South Water section in the acceptance evidence; avoid a uniform citywide trench.
