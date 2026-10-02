---
id: T-1212
title: Yards for every household: lot-line and dooryard fences, gardens, woodpiles, wells, privies and stables assigned by household type, wagons and barrels and trade goods at the shops by trade — the enclosure, yard and outbuilding layers extended to the reconstructed town
state: split
epic: TOWN
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: null
opened: 2026-09-16
closed: 2026-10-02
pr: null
claimed_by: run 10/2/2026, 3:39:20 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-02T08:43:30.824Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/36985027465
claimed_at: 2026-10-02T08:39:20.863Z
decision: null
decision_answer: null
---

The enclosure layer (`data/enclosures/town_lot_line_*.json`, `town_dooryard_pickets.json`, T-0038,
`enclosure_owners.py` — "a home by lives_at, a workplace by works_at"), the yard-goods layer
(`data/yard/`, T-0040), the wells layer (2 records) and the dooryard-garden rule
(`docs/RESEARCH/dooryard-garden-admission-rule.md`) are dealt to the documented households. Now
every household has a lot and a type. Drawn at load — no bake for the layers; the A-family
outbuildings themselves are raised by the build tickets.

**Acceptance:**

- A **yard-by-household rule** (in the policy file): per household type × wealth class — fence
  kind (pickets at the better houses, boards, rails, none at the shanties), dooryard garden
  (the admission rule extended to reconstructed households at its own tier), woodpile, a well
  where the lot's household class and the wells research allow (`docs/RESEARCH/wells.md`),
  privy placement off the alley, stable/barn for the households that kept a horse (merchants,
  forwarders, physicians, teamsters, the taverns); per business — the trade goods and vehicles
  of T-0040 by trade (barrels at the coopers and packers, wagons at the forwarders and the
  teamsters, lumber at the joiners, hides at the tannery, hay at the stables within the hay
  limits).
- Applied town-wide by the existing generators (`generate_lot_line_fences.py`,
  `generate_yard_goods.py`, `generate_lot_building_material.py`, a wells generator added on the
  same pattern), every record `belongs_to` a household or business; `--check` green; the hay
  ordinance gate (`1835_hay_limits.json`) honoured.
- **Visible:** a screenshot of a back-street block shows fenced yards, gardens, privies and
  woodpiles that differ house to house.

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

**Yard-specific acceptance:** fences, woodpiles, wells, privies, stable fronts,
barrels, wagons and trade goods need believable scale, material boundaries, joinery,
edge wear and contact with the terrain. Gardens and vegetation vary at plant and
patch scales, avoiding a uniform coloured mat or tiled noise. Ground, goods and
outbuildings must form a coherent yard under the scene lighting. Compare a maintained
household yard, a modest cabin yard and a working trade yard; do not import Glessner's
1904 planting, gravel treatment or architectural details as 1835 evidence.

**Stop condition:** no lot in the town is bare ground by default.

**Links:** T-0003 · T-0038 · T-0040 · `docs/RESEARCH/dooryard-garden-admission-rule.md` ·
`docs/RESEARCH/wells.md` · `data/reconstruction/1835_hay_limits.json` · T-1195.
