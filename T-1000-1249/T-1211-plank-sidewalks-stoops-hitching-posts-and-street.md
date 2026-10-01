---
id: T-1211
title: Plank sidewalks, stoops, hitching posts and street crossings for every business face, varied by the business — a forwarding house's wide decked walk, a store's board walk and stoop, a smithy's bare ground and rail, a tavern's posts and mounting block — extended to the new fronts town-wide
state: claimed
epic: TOWN
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: null
opened: 2026-09-16
closed: 2026-09-29
pr: null
claimed_by: run 10/1/2026, 11:33:39 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/36882927031
claimed_at: 2026-10-01T16:33:40.102Z
decision: null
decision_answer: null
---

The owner: *"include their correct plank sidewalks for each business that varies because business
vary and fill it in so it is complete."* The street-edge layer (`data/frontage/town_street_edge.json`,
`tools/generate_frontage_works.py`, `renderers/web/js/frontage.js`) holds 77 walks, 31 fences
and 16 posts, dealt to the documented fronts; the new business fronts of the build tickets have
none. Drawn at load — no bake.

**Acceptance:**

- A **frontage-by-business rule** in `generate_frontage_works.py` (and recorded in the placement
  policy): per business type — walk kind (decked plank walk / board walk / none), width, plank
  run and step, rise, stoop or none, hitching posts (count by trade: taverns, stores, the livery),
  a mounting block at the inns, a crossing at the corners of the principal streets, the bare
  ground and rail at the works trades, the wagon apron at the warehouses and forwarding houses —
  each with its evidence (the documented walks, the *American*'s sidewalk notices, the 1835
  ordinances the layer already cites) and tier.
- Applied to every business face in the address book (attested, inferred, reconstructed), the
  record naming the business it serves (`belongs_to`) and the rule; the documented 77 unchanged
  unless the rule finds one inconsistent with its own evidence (stated, not silently moved).
- `generate_frontage_works.py --check` green; walks never enter a corridor's roadway beyond the
  kerb rule; **visible** at both viewports: a walk along the whole of South Water and Lake, and
  the variety readable from one screenshot.

## Photographic-quality benchmark — owner, 2026-09-30

The owner sets **photographic quality** as the standard: the successful Glessner
House v4 rendering in the 1904 scene is the minimum visual benchmark to live up
to and surpass. Complete and consume **T-1769's preparation package before closing
this ticket**. Reuse its proven methods and shared assets where appropriate;
adapt them to July 1835 materials, construction, age and use.

Acceptance also requires inspection of the **actual published browser output** at
390×780 and 1280×800: fixed walker's-eye views, closeups and a wider context view,
with before/after captures, reference comparisons and a written visual critique.
Compare against the promoted Glessner v4 baseline and record which techniques
were reused, adapted or rejected, why, and which qualities match or improve on it.
Review physical scale, relief/silhouette, joinery, surface response, variation,
contact/depth shadows, tiling and shimmer. A green validator, a texture contact
sheet or an offline beauty render alone cannot establish photographic quality;
visible shortcomings must be corrected before closure.

Preserve historical tiers and attested/inferred facts. Photograph-like appearance
does not make reconstructed detail attested. Measure town-wide costs before and
after at the relevant worst stands and all detail tiers; retain the Light floor,
shared-material batching and deliberate, measured re-budgeting under AGENTS.md.
Glessner's local Full allowance is not a town-wide budget.

**Street-edge-specific acceptance:** planks have period scale and direction,
board seams, end grain, worn edges and restrained variation; stoops, posts, mounting
blocks and rails have convincing thickness, joinery, ground contact and shadows.
Near-view detail must support silhouettes and depth where a normal map cannot.
Compare a forwarding frontage, store and tavern/smithy under the same camera and
lighting settings; remove floating boards, repeated noise and texture stretching.
Use shared timber/iron materials and bounded seeded variations.

**Stop condition:** every business front has the street edge its trade would have had.

**Links:** T-0003 · T-0038 · `data/frontage/` · T-1190 · T-1195.


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
ramp grades. This is an explicit closure requirement for T-1211.
