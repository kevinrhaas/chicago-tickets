---
id: T-1210
title: Deal building fabric, finish and weathering by who lived and worked there: a physician's or forwarder's house painted and glazed, a tradesman's cottage weathered clapboard, a labourer's cabin unpainted and patched — the rule set on the material sheet, applied to every dwelling and business, no attested finish moved
state: open
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-09-16
closed: null
pr: null
claimed_by: null
blocked_on: null
needs_bake: true
closed_at: null
claimed_run: null
---

The owner: *"be precise where you can and make sure that businesses and residences are correctly
designed with the correct building materials and correct surfaces, weathered appropriately, based
on the type of person living there, like a doctor or financial person, trader might have a nice
house … or a laborer might have a small not as nice house … provide nice details for them
including all historically appropriate features."* The material sheet (`generators/common/
materials.py`, `docs/RESEARCH/materials.md`, T-0007) deals finish by family and age
(`finish_key`, `roof_condition`, `age_state`) and knows nothing about the occupant; T-0002
(weathered facades) is split and open.

**Acceptance:**

- A **fabric-by-household rule** added to the sheet and to `1835_placement_policy.json`
  (T-1195): for each household wealth/trade class × archetype family — construction
  (balloon vs braced frame, hewn vs round log, brick only where attested), cladding, `paint`
  (white paint stays attested-only — the Sauganash; whitewash, ochre, red oxide and unpainted
  per the sheet's rows), `siding_exposure_m`, glazing (`fenestration` sash counts and pane
  sizes), shutters, porch/stoop, trim, `roof_condition` and `age_state` from the household's
  ARRIVAL YEAR (a house raised in 1835 is fresh timber; an 1831 cabin is weathered), chimney
  fabric (L168) — each rule with its evidence (the documented records that show it: the Sauganash's
  paint, the Green Tree, the Kinzie house, Harmon's hewn logs, the "mere shell" Tremont) and the
  liberty it extends (L22/L23/L157/L196).
- `tools/deal_fabric_1835.py --build|--check` applies it to every dwelling and business record
  whose `form` attributes are `reconstructed`, writing the values and a `fabric_basis` note
  naming the household and the rule; attested/inferred form values never move (self-test).
- T-0002's per-building board-tone jitter, weathering by phase age and board-width irregularity
  land in `materials.py` under the same rule; `measure_stack_fabric.py` / `measure_stack_ordinance.py`
  green.
- Bake (`needs_bake: true`): `materials.py` stales the whole town — the full bake runs;
  `lake_market` and `south_water` critic frames (T-0002's acceptance) show neighbouring facades
  visibly distinct and the wealth gradient readable from Lake Street to the additions.
- **Visible:** the building card's "Built" line names the fabric and its basis ("weathered
  clapboard — a carpenter's cottage of 1834, rule F-D3-trade").

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

**Fabric-specific acceptance:** wall boards/logs and roof coverings have coherent
physical modules, grain direction, believable seams/edges and bounded irregularity.
Recessed openings, glazing, sash, trim, shutters, chimney joints and roof junctions
must read as constructed surfaces rather than flat painted panels. Weathering follows
phase age, exposure, substrate and maintenance; occupant class bounds a reconstruction
rather than proving paint or decay. Test fresh, maintained and weathered examples.
Avoid noise-only colour, oversized grain, obvious repeating tiles and arbitrary
rainbow variation. Apply T-1769's shared texture/tint strategy without silently
breaking the material-sheet or draw-call contract.

**Stop condition:** no two neighbouring reconstructed buildings share a finish by default, and
every finish says whose house it is.

**Links:** T-0002 · T-0007 · T-0126 · T-1195 · `docs/RESEARCH/materials.md` ·
`docs/RESEARCH/chimneys.md` · L157 · L168 · L196.
