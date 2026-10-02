---
id: T-1771
title: Shape South Water and the working riverfront as worn earth, low docks and connected ramps up to muddy streets
state: review
epic: GROUND
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-09-30
closed: null
pr: 265
claimed_by: run 10/2/2026, 3:07:46 AM CT
blocked_on: T-1770
needs_bake: true
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/36980175082
claimed_at: 2026-10-02T08:07:46.582Z
decision: null
decision_answer: null
---

Owner request, 2026-09-30: South Water's river work areas should be worn dirt, with low docks, smaller landings and ramps between river and street; grass survives mainly in unworn patches. One run applies a shared working-bank/landing rule to existing modelled river frontage, with South Water as the acceptance reach.

**Acceptance:**
- Read the peer-city references below, Chicago's committed 1834/1835 bank evidence, existing landing/wharf records and T-0041. Inventory South Water and other modelled working reaches. Preserve the settled waterline and supported dock records; distinguish local evidence from comparative reconstruction. Derive and label unknown small landing placements instead of asserting the images depict Chicago.
- Working aprons, haul routes and occupied bank edges are predominantly compacted/worn earth, muddy at appropriate low/wet spots. Sparse grass is confined to quieter margins and gaps; suppress meadow grass and trees on active dock approaches. Keep undeveloped bank vegetation differentiated rather than stripping every riverbank.
- Existing docks and evidenced/reconstructed small landings sit plausibly low relative to water, with timber thickness/supports and local damp wear. Earth or timber ramps connect docks to bank, muddy full-width streets and higher plank walks/entrances. Choose ramp form and gradient from evidence and labelled practical reconstruction; no continuous invented quay or identical repeated ramps along the whole river.
- Coordinate T-1770's grades and T-1211 frontage: warehouse doors, loading aprons, walk edges, ramps and dock decks meet with believable contact, traversable slopes and no floating timber, shoreline gaps, water clipping or buried structures. Retain warehouse picking/association.
- Render the connected system in the real browser: South Water along and across the bank, close dock/ramp views, an opposite-bank view and one other working landing. Use Glessner-level timber relief, roughness and contact shadows, together with T-1769's ground proof. Preserve shared materials and detail tiers.

**Stop condition:** South Water and the inventory's working reaches show connected dirt street–bank–ramp–low dock systems, with vegetation reflecting wear. Publish before/after captures, inventory coverage and historical tiers; green geometry checks alone are insufficient.

**Owner's comparative references** (inspect these images; they are analogues, not Chicago-specific attestation):
- [St Louis Front Street, 1840](https://github.com/kevinrhaas/chicago/blob/main/chicago/reference/images/st_louis/st_louis_front_street_1840.jpg)
- [Detroit Jefferson Avenue at Griswold, 1837](https://github.com/kevinrhaas/chicago/blob/main/chicago/reference/images/detroit/detroit_jefferson_ave_griswold_st_1837.jpg)
- [Cincinnati Fourth Street east from Vine, 1835](https://github.com/kevinrhaas/chicago/blob/main/chicago/reference/images/cincinnati/cincinnati_wild_fourth_street_east_from_vine_1835.jpg)
- [Cincinnati Fourth Street west from Vine, 1835](https://github.com/kevinrhaas/chicago/blob/main/chicago/reference/images/cincinnati/cincinnati_wild_fourth_street_west_from_vine_1835.jpg)


**Common visual release requirement:** photographic quality, meeting and aiming to surpass the promoted Glessner House v4 benchmark (PR #201/#202 in the code repo). Read its texture research, material library and final QA alongside T-1769, T-1450 and `docs/RESEARCH/materials.md` / `texture_library.md`. Transfer reference-led iteration, metric texture scale, layered variation, physical relief and controlled lighting rather than mansion materials. Inspect actual exported/runtime output at 390×780 and 1280×800, close and context distances under fixed lighting/exposure, with reference comparisons and a written critique. Correct visible defects before closure; automated green checks or offline beauty renders alone do not meet this standard. Measure frame time, draw calls, triangles and texture memory before/after at worst stands and all detail tiers; preserve the Light floor and shared batching. Keep provenance/rights, tiers, seeds and reproducible recipes. Push interim commits so another run can resume. Needs bake includes changed terrain/model derivatives; publish the actual result and recheck collision/height sampling.

**Queue placement:** owner-requested scene improvement beside the finish preparation, below the current 5C builds. This is substantive city rendering work, not a loop follow-up.

## Implementation evidence and coverage — 2026-10-01

Read [the shared ground brief](../evidence/1835-ground-photographic-quality-brief.md).
Reuse the existing wharf/landing work (including T-0062) and preserve the settled
T-1628–T-1630 bank/mouth corrections; do not duplicate docks or reshape the surveyed
bank to fit the St Louis illustration. Account for every active working-bank record,
including South Water from the forks toward the fort, with explicit exceptions.
Use the same height and wear masks for ramps, collision, timber contact and plant
exclusions. Show a measured cross-section from entrance/walk through road, apron,
ramp and low dock to water, alongside the close and wider browser comparisons.
