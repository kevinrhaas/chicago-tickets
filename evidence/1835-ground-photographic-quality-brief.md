# Owner ground and waterfront rendering brief — 2026-09-30

Implementation parcels: **T-1770 streets**, **T-1771 working riverbanks/landings**,
**T-1772 lakefront dunes/prairie**. All are owner-requested 1835 visible work.
Photographic quality is the standard; the successful Glessner v4 process is
the benchmark to meet and surpass. T-1769 supplies shared material-development
findings. This brief records the request and reference reading; it does not
turn the illustrations or the owner's interpretation into a measured Chicago survey.

## The requested result

1. South Water and other opened streets should have a broad worked, packed-dirt
   roadbed. Walks and their supporting shelf, sometimes wider than the boards,
   sit near building-entrance level; the carriageway is locally graded down with
   appropriate drainage. Traffic leaves many irregular paths/ruts rather than
   the repeated pair of tread bands now drawn.
2. South Water's river side is predominantly worn working earth: low docks,
   smaller landings, ramps up to streets and freight aprons, higher walks toward
   the buildings, mud according to wetness and use, sparse grass in unworn places.
   Use that rule on the other active riverbank records; preserve natural margins.
3. Fort sand continues north and south along the historical lake shore.
   Cooler grey/beige sand, low dune ridges and gradual inland slopes transition
   through sand prairie into grass. Remove the conspicuous beach/prairie line;
   improve the surrounding prairie material and grass as well.

4. **Sidewalk colour correction:** ordinary plank walks should never read as
   white paint. Use worn grey, brown, grey-brown and dark grey-brown timber,
   coherently varied by owner, age, maintenance, exposure and wetness. Fix the
   material/lighting cause of the white appearance and compare actual adjacent
   walks in the published scene. T-1211 owns this explicit acceptance.

## Four references inspected

These links point to the supplied committed files. Dates below identify the
depicted scene from the filename/caption; verify catalogue publication dates
and source rights during implementation before creating source/asset records.

| Image | Useful visible guidance | Limit on the analogy |
| --- | --- | --- |
| [St Louis, Front Street, 1840](https://github.com/kevinrhaas/chicago/blob/main/chicago/reference/images/st_louis/st_louis_front_street_1840.jpg) | Broad active freight frontage, irregular rough bank descending toward boats, distinct low landings and working access; buildings and bank do not form a uniformly high quay. | Different river scale and relief, later than Chicago's scene; illustrated/coloured surfaces cannot establish Chicago elevations, exact substrate or colour. |
| [Detroit, Jefferson Avenue and Griswold, 1837](https://github.com/kevinrhaas/chicago/blob/main/chicago/reference/images/detroit/detroit_jefferson_ave_griswold_st_1837.jpg) | Broad carriageway, visibly separate entrance-level board walks, connected store approaches; road use spreads across the width. | Plate caption depicts 1837; visible copyright is **1883, Silas Farmer**, from an original sketch by Wm. A. Raymond. Treat this as a retrospective printed witness, not an 1837 photograph. Engraved marks do not prove dirt versus paving or exact rut depth. |
| [Cincinnati, Wild, Fourth Street east from Vine, 1835](https://github.com/kevinrhaas/chicago/blob/main/chicago/reference/images/cincinnati/cincinnati_wild_fourth_street_east_from_vine_1835.jpg) | Continuous broad street plane, separated higher pedestrian edges, entrances integrated with that edge, no default pair of vehicle treads. | Its more finished pedestrian edges/curbs and architecture are not instructions to put stone curbs or Cincinnati paving into frontier Chicago. Colour is not measured reflectance. |
| [Cincinnati, Wild, Fourth Street west from Vine, 1835](https://github.com/kevinrhaas/chicago/blob/main/chicago/reference/images/cincinnati/cincinnati_wild_fourth_street_west_from_vine_1835.jpg) | Reverse view corroborates the broad section and continuous pedestrian-to-entrance relationship. | Same date/material/grade limits as the eastward view; no source here prints Chicago dimensions. |

These are **comparison-city visual analogies**, not local attestation. Each
implementation reads existing Chicago primary-source records and registers any
new source honestly. Use bounded reconstructions where dimensions or exact
appearance remain missing; no separate indefinite research ticket is needed.
Source-image pixels are not material maps; inspect rights before deriving assets.

## Current implementation findings

- `renderers/web/js/streets.js::roadTexture` makes the reported pair explicit:
  two Gaussian rut bands at normalized widths **0.29 and 0.71**, repeated
  down a 128×256 canvas. The translucent body lets the prairie show through.
  The geometry uses `track_width_m`, not the full surveyed corridor. This
  needs a new street-section/coverage rule, not another road-contrast boost.
- Streets currently drape `terrain.surfaceHeight()` rather than changing the
  terrain. A lowered roadbed therefore needs actual terrain/collision coordination;
  a darker texture or raised sidewalk floating over grass is insufficient.
- `terrain.js` already has a 50 m substrate edge ramp. The requested improvement
  is shore-following shape plus coordinated material, terrain and plant density;
  simply claiming a blend was added, or increasing one global ramp, is insufficient.
- Existing Chicago research leads: `docs/research/01-terrain-hydrology.md`,
  `docs/research/04-structures-south.md`, Wright/Hathaway records, street grading/
  ordinance records, `shoreline_states.json`, lake-sand/sand-prairie zone records
  and existing wharf/landing evidence. Dossiers are leads until backed by resolving
  source records. Preserve T-1628–T-1630's settled bank/mouth corrections and
  AGENTS.md's distinct drawn versus control lines.
- T-1450 and `docs/RESEARCH/texture_library.md` held ground/waterfront maps back
  for a separate parcel. These owner-requested ground tickets supply that parcel:
  audit `muddy_rutted_street`, `packed_black_loam`, `wet_prairie_muck`,
  `lake_michigan_dune_sand` and waterfront timber before replacing them.

## Glessner methods to carry forward

Read `docs/RESEARCH/glessner_house_v4.md`,
`assets/textures/glessner-v4/README.md`, its map inventory and final QA/promotion
records (code paths relative to `chicago/4d/`). Transfer metric texture scale,
original albedo/normal/roughness, geometry for visible shape, restrained variants,
controlled neutral/scene-light trials and actual published-browser review.
Its successful 4 m lawn study addressed the uniform olive mat with coherent
0.5–2 m growth/thatch variation. Adapt that lesson to tall July prairie and
natural sand communities; a mown 1904 courtyard lawn is not their ecology.

Keep recipes/seeds or original generated-image prompts/hashes, aligned channels,
licensing and historical confidence. Screenshots must identify the served
commit/assets, fixed stands, scene/detail tier and viewport. Review likeness,
ground contact, seams, tiling, shimmer and transition continuity alongside
performance/loading, and correct defects before closing. Photographic-looking
reconstructed material remains reconstructed, and automated checks alone cannot
establish photographic quality.
