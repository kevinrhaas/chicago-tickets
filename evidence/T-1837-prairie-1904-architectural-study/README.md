# Prairie Avenue 1904 architectural design study

**Current execution status — 2026-10-01:** owner approved “Go” and requested one group below the dev queue. All 110 child tickets are now open in that single group; the construction hold described in the original assessment below was lifted by this later ruling. Dependencies and bake requirements remain.

Prepared 2026-10-01 (America/Chicago). Parent: T-1837. Source revision: `b31dc146c63b11e550ce8536048f33dfefa606c5`.

## Decision

Build a coherent 16th–22nd Street Prairie Avenue streetscape at **1904-07-01**, matching the material depth and architectural specificity of Glessner. The remaining corridor needs both bespoke landmark architecture and a reusable library of period construction parts. The study decomposes this into **110 implementation tickets**: 16 shared-component packages, three sheet reconciliations, 73 front-building envelope/finish/assembly packages, seven rear/service packages, four named adjacent-context packages, four streetscape packages and three block acceptance packages.

This turn delivers the assessment and tickets, not new geometry. The existing hold on T-0475, T-0476 and T-0477 is preserved. T-1830/T-1833 retain Glessner repairs; T-1745 retains uncompleted legal-lot work; T-1728 owns existing road/sidewalk materials. Do not repeat those programmes.

## Read the study

- [Every named building](BUILDING-REGISTER.md): all 62 source records, phase decisions, architectural decomposition and work ownership.
- [Every mapped frontage](FRONTAGE-REGISTER.md): all 91 rows, including unnamed houses, aliases, empty-frontage observations and rear assignments.
- [Shared asset catalogue](ASSET-CATALOG.md): 16 component systems, detailed parts, material/export requirements and Glessner visual acceptance.
- [Reconstruction design rules](RECONSTRUCTION-RULES.md): proposed dimensions, composition rules and complete exterior checklist for sparse evidence.
- [Validation](VALIDATION.md): coverage, dependency and queue checks.
- [Ticket plan](TICKET-PLAN.md): complete staged implementation list and dependency order.
- [Machine-readable named register](building-register.csv), [frontage register](frontage-register.csv), [all 92 viewer parcels](parcel-coverage.csv), [coverage proof](coverage.json), [source fingerprints](source-snapshot.json).

## What the inventory does and does not count

| Existing layer | Count | Interpretation |
|---|---:|---|
| Named-building records | 62 | Includes four adjacent-context records (one aggregate of three houses), Glessner, excluded predecessors and Clarke's wrong 1904 site |
| Prairie map-frontage observations | 91 | Address readings from 1911, not 91 unique houses or complete rear-building count |
| Viewer parcels | 92 | Traced locator lots, not surveyed 1904 building footprints |
| Image/document references | 815 | Includes repeated negatives, portraits, text, maps, later photographs and discovery leads |
| Locally available image records | 199 | Storage availability is not a confidence or completeness score |
| Source-table records | 138 | Bibliographic/source entries; older statistics.md still says 110 |

Only Glessner currently has a post-1860 structure record in the canonical structure set inspected. The library/viewer is much richer than the rendered asset inventory. Named historic residents, mapped addresses, parcels and rendered buildings must be joined before asserting a final unique-house count. Every one of the three existing enumerations is assigned in this study; unnamed detached rear buildings and additional Indiana/Calumet background polygons still require a polygon census under the specified tickets. No exact total for those roofs is invented.

## Architectural reading

The street is not a row of Glessner-like rough-stone houses. Its defining contrast is between older frame/Italianate villas, stone-fronted urban houses, brick and stone Second Empire mansions, Gothic/Queen Anne towers and gables, Romanesque houses and newer Georgian/classical fronts. Shared component systems must preserve that contrast.

The most valuable first comparison ensemble is Glessner plus **1808 Keith/Field, 1812 Wheeler, 1801 Kimball and 1811 Coleman/Ames**: contiguous street relationships, contrasting stone/brick fabric, an ornate parapet, a shaped Dutch gable, a Chateauesque tower and a deep Romanesque entrance. It exercises nearly every shared part and exposes scale mismatches immediately. Next come Pullman, Field Sr./Jr., Doane, Lowden, Sherman, Rees and the southern rowhouse fabric. This is recommended production sequencing, not a change to the owner's current queue.

The second system is the service street: substantial two-storey coach houses, stable basements, brick rear wings, glasshouses, boundary walls and carriage drives. These are not optional tiny sheds. They give the oblique, aerial, courtyard and alley views their credibility. Principal houses own attached wings; seven service packages own detached structures with separate IDs, so ownership is explicit.

## Critical rulings and provisional choices

1. **1609–1611 and 1620:** use the earlier Robinson outlines for the expert-specified 1904 corrections. The paired yellow rectangles are on lot 6, not the neighbouring pink pair. Reconstruct undocumented elevations honestly. The later commercial loft and empty 1620 frontage do not belong in 1904.
2. **1700/1702/1706:** two Glessner-family Georgian townhouses, with an address relationship to resolve; do not build a third house at a reused number or restore the demolished Staples/Harvey predecessor. The museum's collection history independently supports the paired design and 1902 move-in.
3. **1719/1721 Dexter:** the map and named record may describe the same altered property. Use the post-1889 front shown in the 1891 plate, not the pre-addition winter photo. Keep one provisional association until reconciled.
4. **1936 Allerton:** the 1911 frontage transcription calls the corner vacant, but the museum's 1887 street-view account dates demolition to 1915. The nearby map label 1916 (1930) complicates the join. Preserve the conflict, reserve Allerton as a required 1904 house, and resolve its footprint before placing any additional villa. The study visually checked the original sheet label and the period corner images; it has not conclusively solved that address crosswalk.
5. **1900 versus 1906 Keith:** the same exterior photo has conflicting attributions. Museum caption and surviving facade support 1900 as the working interpretation. Do not copy that image-derived facade at both houses.
6. **Jones 1834, Marsh 1824, Sears/Meeker 1815, Field Jr. 1919:** alteration phases matter more than initial construction years. Preserve the 1886 Jones mansard, post-1880 Marsh front, 1902 Meeker work where supported and Field Jr.'s post-1902 enlargement. Their earlier pictures are not automatically the target facade.
7. **Robbins 2126:** completed May 1905 publication does not settle 1 July 1904. A 1904 reconstruction may need construction-state geometry; set a replaceable phase with an explicit assumption if no month can be established. Keep reported 1904/1905 conflict. Do not silently shift the entire scene date.
8. **2140 Tucker/Smith:** flat-topped crested towers and tall spires represent different states. Retain one documented working phase, bounded by photos; do not combine them. The exact 1904 roof state remains unresolved.
9. **2108/2110 coach house:** one shared building, divided by ownership, not two overlapping stable assets. Rees belongs at historical 2110, not its relocated modern site.
10. **Excluded:** Clarke is absent from this site in 1904; old Staples/Harvey 1702, Hitchcock/Galloway predecessors at 1804–1808, Williams 1709 and early frame double house at 1726–1728 are not the 1904 buildings. Forsyth 1635 has an unresolved loss/date/parcel question, not a license to create a house on its neighbour.
11. **1911 use labels:** garage, auto repair, medical college, institute and dressmaking labels are observations of 1911. They do not prove those functions, signage or alterations existed in 1904. Map material/story annotations constrain envelopes only after temporal review.
12. **Missing named assets:** 1945 Armour/Corwith and the photographed Romanesque neighbour at 2011 need canonical identities even though they are absent from the 62-name list. The map-only rows are all owned by explicit frontage packages.

## Inference policy: build the missing fabric

A missing photograph does not postpone the house indefinitely. Preserve map-bound footprint, construction family and storey reading; infer roof and floor datums from actual local analogues and available street silhouette; choose a restrained period facade with realistic windows, joints, eaves and entry; document its bounds and alternative. Colour from monochrome images, exact window subdivisions, hidden rear openings, fine carving, soot and garden planting normally remain reconstructed. Reuse construction components, not a famous neighbour's whole facade. At a disputed identity, resolve the site association first so a plausible model does not become a duplicated building.

Record `tier`, `basis`, `source locator`, `date interval`, `seed` for stochastic choices, `uncertainty/range` and `replaceable_by` on attributes. Derived measurements state map/photo scale, control and residuals. Do not present a typed Sanborn storey code, an oblique-photo pixel count or a 25-foot lot frontage as an exact building dimension.

## Review performed and limits

Read the current source tables, research gaps, map guidance, image metadata, Glessner material/geometry/QA records and current ticket ownership. Visually inspected the three complete Sanborn sheets, the Allerton label/detail crop, 99 locally available image/drawing contact entries (including duplicate/obsolete views), 20 additional selected linked exterior images and the archived Glessner entrance close-up. Contact-sheet inspection establishes broad form, not exact moulding dimensions; tickets require full-resolution inspection at authoring time. Later images and link-only references remain dated/rights-qualified in their source records. No new measured footprint survey, permit transcription or image-rights clearance is claimed.

The live viewer library.json and images.json exactly match the pinned repository versions by SHA-256; hashes are recorded in source-snapshot.json. The library’s in-period image flag extends through 1911, so it is not itself a 1904 phase guarantee. Existing research already supplies most discovery work; this study spends it on architectural decisions instead of claiming each reference is a newly verified primary observation. The residual work is finite per sheet/property and attached to build deliverables.

## Primary and institutional checks made for this study

- [Glessner House: Prairie Avenue 1887](https://www.glessnerhouse.org/prairie-avenue-1887): Allerton survival/demolition conflict and identification of 1945 Armour/Corwith.
- [Glessner House: The Collection](https://www.glessnerhouse.org/the-collection): 1700/1706 mirror-image Georgian townhouses, 1901 design and 1902 occupancy history.
- [Art Institute architectural monograph index](https://artic.contentdm.oclc.org/digital/api/collection/findingaids/id/16290/download): Robbins rebuild dated 1904; this still does not determine completion month.
- Source-owned image/drawing catalog URLs are listed per property; map originals and CSV rows are pinned to the repository revision above.

## Completion test

No unexplained blank frontage, duplicated address building, missing mapped service roof or unassigned visible background polygon; all 1904 phase decisions explicit; distinctive architecture readable from both sidewalks and alleys; shared material scale coherent; full/light architecture consistent; whole-block browser cost measured. All three block acceptance tickets must pass before claiming a complete photographic-quality streetscape.

## Reproduce the assessment tables

`build_study.py` reads this pinned version of the source library from a sibling `chicago` checkout, or the `CHICAGO_CODE_DIR` path. With that checkout at the source revision above, run `python build_study.py`; `ticket-ids.json` retains the published package-to-ticket mapping. This regenerates evidence tables only, never ticket state or queue order. Live source hashes are retained in `live-check.json`.
