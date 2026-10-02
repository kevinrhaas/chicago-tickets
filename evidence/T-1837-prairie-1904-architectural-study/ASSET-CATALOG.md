# Reusable architectural assets and acceptance standard

Shared construction methods support unique houses. Reusing a sash profile or brick shader is desirable; repeating a complete generic mansion facade across the district is not. Specifications below are production requirements, not historical measurements.

## K01 · Metric asset contract and Glessner comparison slice · T-1843

Anchor every reusable part in metres with explicit grade/sill/storey datums; declare family parameters, sockets, material slots, stable component IDs, deterministic seeds and source/confidence attributes. Preserve the canonical Glessner asset. Prove a small 1808 frontage assembly beside it at street-eye and oblique views.

**Parts and parameters:** wall thickness; sill datum; eave/ridge datum; opening cutouts; handed variants; local/ENU placement; scale/UV contract.

**Visible acceptance:** No scale drift, hidden origin offsets or duplicated boundary faces; record baseline asset hashes and full/light mesh/texture costs.

**Dependencies:** none; programme resumed by owner on 2026-10-01.

## K02 · Stone, mortar and dressed masonry materials · T-1844

Provide rock-faced granite, warm brown sandstone, pale limestone/Lemont or Bedford variants, smooth dressed trim and foundation rubble, each with clean albedo, normal and roughness plus physical joint/edge profiles. Granites must not be painted onto every mansion.

**Parts and parameters:** stone courses; ashlar corner bonds; rusticated base; mortar recess; voussoir texture orientation; coping; sparse chipped edges.

**Visible acceptance:** Render rough wall plus smooth carving on the 1808 exemplar in raking and diffuse light; metric grain, subdued roughness and nonrepeating courses match scale.

**Dependencies:** T-1843.

## K03 · Pressed, common and rough brick materials · T-1845

Red pressed face brick, buff/common service brick, dark fired variants and Mayer rough/chipped brick; correct bonds, corner returns, soldier/segmental heads, mortar colour and shallow relief. Separate body clay from dirt.

**Parts and parameters:** brick bond; specials; string course; corner return; arch brick; soot/damp mask; back wall variants.

**Visible acceptance:** Build a facade/service-wall comparison on a named target; no Glessner courtyard colour applied indiscriminately, no checkerboard randomisation.

**Dependencies:** T-1843.

## K04 · Period roof coverings and drainage · T-1846

Slate rectangular/scalloped courses, documented terracotta tile only where supported, copper sheet/standing seams, lead/zinc/painted metal flashings, bounded low-slope service roof. Add gutters, outlets, downpipes and boots.

**Parts and parameters:** slate exposure/lap; cut edges; hip/ridge caps; valley flashing; dormer apron; gutter bracket; downpipe shoe.

**Visible acceptance:** Roof sample spans daylight and grazing angles with no oversized tiles, baked highlights or zipper-like seam shadows; drainage ends at actual ground.

**Dependencies:** T-1843.

## K05 · Mansard, hip, gable and tower roof construction · T-1847

Build data-driven roof planes and explicit valley/intersection trimming, convex/concave mansards, ordinary/stepped/ogee gables, polygonal/conical towers, dormers and chimney penetrations.

**Parts and parameters:** roof graph; fascia; soffit; verge; dormer cheeks; ridges; valleys; cross-gable return; watertight closure.

**Visible acceptance:** Demonstrate one representative house roof without roof planes crossing gable faces, floating cornices or doubled coplanar surfaces. This directly carries the lesson of Glessner repairs.

**Dependencies:** T-1843, T-1846.

## K06 · Windows, glazing and visible interior depth · T-1848

Rectangular sash, paired sash, segmental/round/pointed heads, transoms/fanlights, basement lights, grouped attic windows, limited leaded lights. Real wall openings, jambs/reveals, separate sash and glass with dark enclosed backing.

**Parts and parameters:** sash rails/stiles; muntin patterns; sill drip; arch spring; glazing plane; blinds; curtain edges; window well.

**Visible acceptance:** At 2-5 m the opening reads as a recess, glass reflects/transmits plausibly and blinds remain behind it; zero floating painted rectangles or unbounded transparency sorting.

**Dependencies:** T-1843.

## K07 · Entrances, stoops, porches and carriage doors · T-1849

Single/double panel doors, vestibules, timber/glazed doors, deep arched entrances, historic carriage leaves/hardware, stone straight/curved stoops, porch floors/posts and basement stairs.

**Parts and parameters:** door leaf; rail/stile; lock/hinge; transom; threshold; tread/riser; cheek wall; handrail socket; porch skirt.

**Visible acceptance:** Prototype touches grade and floor correctly and clears public walks; carriage opening has thickness and lintel, not a texture panel. Keep accessibility to the walk renderer functional.

**Dependencies:** T-1843, T-1848.

## K08 · Bays, oriels and towers · T-1850

Rectangular, canted and bowed bays; full-height projections and corbelled upper oriels; circular/polygonal corner towers; copper caps and independent facade openings.

**Parts and parameters:** plan polygon/radius; floor bands; piers; corbels; bay roof; wall interface; upper support.

**Visible acceptance:** A canted and a curved example preserve measured footprint and window rhythm without faceting at near view; light tier retains their silhouette.

**Dependencies:** T-1843, T-1847, T-1848.

## K09 · Carved entrances and classical or Gothic trim · T-1851

Parametric arch rings/voussoirs, moulding sweeps, lintels/hoods, colonnettes, column bases/capitals, Gothic tracery/crockets and original bounded foliate relief.

**Parts and parameters:** arch radius/rise; reveal; column order; capital profile; leaf relief; panel depth; repeated/unique motifs.

**Visible acceptance:** Compare a bespoke hero entrance and a restrained rowhouse surround. Generic carvings may support uncertain houses but cannot replace distinctive documented landmark carving.

**Dependencies:** T-1844, T-1848, T-1849.

## K10 · Cornices, parapets, dormer faces and cresting · T-1852

Bracketed timber/metal cornices, dentils, friezes, classical entablatures, carved stone parapets, balustrades, urns, pediments, shaped gable copings and roof cresting.

**Parts and parameters:** bracket spacing; soffit; dentil; coping; baluster; urn; finial; cresting panel; dormer pediment.

**Visible acceptance:** Continuous corner returns, no hanging ends or roof clashes; unique Wheeler/Mayer profiles authored from evidence rather than scaling a generic gable.

**Dependencies:** T-1843, T-1847, T-1851.

## K11 · Ironwork, gates, canopies and boundary walls · T-1853

Cast/wrought iron fence panels, spear/scroll variants, posts/piers, entry gates and hardware, area grilles, balcony/stair rails, iron-and-glass canopy and brick/stone boundary walls.

**Parts and parameters:** panel rhythm; picket section; rail joint; gate swing; hinge; wall cap; pier urn; canopy rib.

**Visible acceptance:** Silhouette reads at walking distance without wire shimmer; separate property patterns and height evidence; no fence crossing entrances or shared carriage drives.

**Dependencies:** T-1843, T-1844, T-1845, T-1849.

## K12 · Coach houses, stable fittings and service wings · T-1854

One/two-storey brick/frame/mixed service buildings, hay/loft doors, carriage bays, sash, roof ventilator only when supported, ramps, lean-tos and connecting wings.

**Parts and parameters:** rear footprint; party wall; carriage aperture; loft hatch; stable basement ramp; service stair; wall return.

**Visible acceptance:** Demonstrate one complete alley asset with all elevations and believable workyard connection; 1911 garage/auto labels are not 1904 use evidence.

**Dependencies:** T-1845, T-1846, T-1847, T-1848, T-1849.

## K13 · Conservatory and greenhouse assemblies · T-1855

Modular iron/timber glazing bars, curved roofs, pitched bays, lanterns, masonry plinths, doors, gutters and restrained internal plant backing. Site-specific Pullman shapes remain authored.

**Parts and parameters:** glasshouse bay; curved rib; ridge vent; lantern; plinth; door; gutter; low-detail glass substitute.

**Visible acceptance:** Glazing and frame hierarchy remain legible in browser; avoid overlapping transparency and a full interior plant scene; validate a Pullman service-garden bay.

**Dependencies:** T-1843, T-1846, T-1848.

## K14 · Age, surface variation and ground contact · T-1856

Shared authored material variants, roof/ground contact occlusion, mortar weathering, restrained soot near chimneys, water trails beneath outlets, timber grain/paint and yard surface transitions.

**Parts and parameters:** age mask; rain mask; soot; grass edge; masonry plinth dirt; path wear; independent per-property seed.

**Visible acceptance:** Condition represents each building in 1904, not modern ruin. Compare new Georgian work with 20-40-year-old houses under identical neutral lighting, preserving material identity.

**Dependencies:** T-1844, T-1845, T-1846, T-1848, T-1853, T-1854, T-1858.

## K15 · Chimneys, flues and roof service details · T-1857

Brick and dressed-stone stacks, corbelled caps, documented clay pots, grouped flues, crickets and stepped flashing. Respect source-specific number, height and position; a chimney is a major skyline feature, not a randomly scattered prop.

**Parts and parameters:** shaft width/height; corbel courses; cap projection; flue opening; pot profile; roof penetration; flashing steps; soot direction.

**Visible acceptance:** Demonstrate ordinary service stack and Sherman carved stack with credible roof junction, dark recessed flues and source-bounded silhouette; reduced tier retains location and height.

**Dependencies:** T-1844, T-1845, T-1846, T-1847.

## K16 · Frame cladding and exterior timber construction · T-1858

Clapboard and board-and-batten families, supported decorative shingles, corner boards, water tables, timber fascia/brackets, porch lattice and pierced Gothic woodwork. Separate painted softwood from stained joinery and exposed end grain; frame walls retain plausible thickness.

**Parts and parameters:** board exposure/thickness; lap; joint stagger; corner trim; window casing; water table; bracket profile; lattice pitch; paint wear.

**Visible acceptance:** One ordinary frame-wall/porch sample and a 1638 Gothic detail retain actual board scale, cutout depth and coherent joinery in full/light exports. Do not apply masonry thickness or stone texture to a timber facade.

**Dependencies:** T-1843, T-1848, T-1849.

## Cross-cutting numerical proposals — calibrate, do not call them measurements

| Subject | Proposed starting policy | Why / limit |
|---|---|---|
| Units and origins | Metres in glTF; architectural feet retained in evidence; one conversion at import | Never scale a building to fit a screenshot |
| Near-view geometry | Model visible reveals, ledges, roof laps, cornice/arch silhouette and material boundaries | Fine grain comes from texture/normal maps; block edges remain geometry near the walker |
| Surface texture | Start 2K albedo / 1K normal+roughness for shared wall/roof families; trim atlases by screen need | Reuse Glessner transport conventions, not its exact texel/grain scale on every material |
| Colour channels | Albedo sRGB; normal/roughness/AO linear; OpenGL tangent normals | No baked sun or painted reflections; verify exported compressed maps |
| Glass | Start dielectric IOR about 1.5; tune transmission against browser/export behavior | A shader value alone is not acceptance; dark backing and reveals are necessary |
| Close inspection | 2-5 m details; 10-25 m whole facade; 40-80 m street composition | Proposed review distances; compare actual viewing scale on mobile as well |
| Confidence | Per attribute: attested / inferred with reasoning / reconstructed with bounds, seed and replacement source | A crisp texture must not imply documentary certainty |
| LOD | Preserve all meaningful openings and distinctive roofs; reduce microrelief, invisible interior and distant small ironwork | Never flatten a tower, erase a side wing or turn windows into flat stickers to meet budget |
| Age | Condition at 1904: new Georgian brick versus older Victorian material | Do not sample present-day ruin and call it historical weathering |

## Glessner comparison protocol

1. Freeze the accepted current canonical Glessner GLB/sidecar hashes after the live roof-repair tickets settle. The archived refined-06 frames are the reviewed material/depth reference, not proof that the latest repairs are final.
2. Render the same asset under neutral diffuse illumination and raking sunlight at front, two obliques, rear/yard and aerial. Include a close entrance and roof-intersection detail. Use a repeatable camera, sun, exposure and background; retain before/after images.
3. Judge silhouette and proportions first, then opening depth, stone/brick scale, roof junctions, glass, ornament, believable age and ground contact. Compare full-size image detail, not only thumbnails. A written defect list accompanies every hero house.
4. Verify the actual published compressed GLB at 1280×800 desktop and 390×780 mobile, full/balanced/light. No unexpected page/network errors, no texture loss, no LOD pop that changes architectural identity. Record load size, GPU texture memory estimate, triangles, draws, frame-time distribution and device/renderer. Software-rendered budget readings are not phone FPS claims.
5. Price the WHOLE visible block and adjoining view, including shadow draws, before adding the next assets. Glessner once used roughly 3.43 million full-tier scene triangles and 0.80 million at reduced tier in its archived QA: that is a measured comparison build, not a per-building budget to multiply by 90. Use shared materials, atlases, instancing, reduced rear detail at distance and streaming; measure actual allocation before changing any project ceiling.
6. Preserve existing light-tier floor. Any full/balanced ceiling change needs written measurements at the tightest street stands and the repo-defined budget update. Do not silently weaken a test or use a cinematic offline render as browser acceptance.
7. Deliver parameter data, generator/authored asset provenance, master GLB, compressed derivatives, confidence/source sidecars, material/licenses, LIBERTIES entries and recovery checkpoint commands. No hardcoded renderer-only architecture.

## Unseen rear elevations and sparse evidence

For each elevation, state whether the plan, a photo or neither controls it. Begin with mapped footprint/material/storeys; establish grade and floor heights from the nearest defensible measured analogue; derive roof volume that fits documented street silhouette; set window spacing from room/structural rhythm rather than copying the front to the rear. Use restrained service brick, simple sash, lintels, doors, gutters and chimneys with individually declared uncertainty. Record reasonable alternatives and the evidence that would replace the working model. Missing precision is permission for an honest reconstruction, not for leaving the lot blank.

Rights are separate from confidence. A rights-unresolved reference may be linked/described in the study; do not embed its pixels or derive shipping assets where the project rights gate prohibits that use. Prefer cleared primary images/drawings, independently authored generic PBR and recorded design reasoning. The narrow existing Glessner rights exception does not automatically extend to other properties.
