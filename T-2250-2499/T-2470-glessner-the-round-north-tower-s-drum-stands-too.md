---
id: T-2470
title: Glessner: the round north tower's drum stands too tall over the north range roof; bring its cone down to sit nearly on the roof as HABS photograph 1 shows
state: done
epic: SOUTH_TIME
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-10-13
closed: 2026-10-13
pr: 789
claimed_by: interactive north-tower correction 10/13/2026, 3:08:15 PM CT
blocked_on: null
needs_bake: true
closed_at: 2026-10-13T21:18:24Z
claimed_run: null
claimed_at: 2026-10-13T20:08:15.707Z
decision: null
decision_answer: null
---

Glessner: the round north tower's drum stands too tall over the north range roof; bring its cone down to sit nearly on the roof as HABS photograph 1 shows.

## The owner's report

Owner, 2026-10-13, in the project thread, with HABS photograph 1, a crop of it, and a phone screenshot of the model on 18th Street:

> On Glessner maybe you already have this planned in your matches to photoessay but the round tower you have in the center appears too tall, you have stone facing and the image has almost none of that wall, make sure there is a ticket for this

Side by side: [habs-01-vs-model-phone.jpg](../evidence/glessner-north-tower-T-2470/habs-01-vs-model-phone.jpg) (photograph left, the model on dev right).

No open Glessner ticket covered this. T-2206 audited the tower's height and retained it pending cross-view reconciliation; T-2228 is the final sign-off and should not be the first place it is fixed.

## What differs

The tower is `tower_north` in `data/sidecars/1904/glessner_house.json`: the round tower at the junction of the east wing and the north range, just west of the east wing's 18th Street gable. Not the courtyard stair tower (`tower_stair`).

- **The model:** a full rock-faced granite drum stands clear of the north range roof all the way round. Base 20.0 ft (buried in the range), wall top 32.9 ft, cone apex 43.9 ft, finial 2 ft. The 18th Street eave is about 24 ft and the north ridge 34.1 ft, so about 9 ft of stone drum shows above the eave and the cone's eave sits at about ridge height. From the street the drum reads as a stone cylinder about as tall as the cone.
- **HABS photograph 1:** the cone sits almost down on the main roof. On the uphill side the north range's slope climbs nearly to the cone's eave. Only a short band of drum shows between roof and eave, in shade, deepest at the street-side front where the downpipe drops from the cone's eave. The cone also reads broader against its drum than ours, with a flared eave.
- **The T-2200 instrument already flags it.** In view `north-inclined` (HABS photograph 14), the `north-tower-apex` check point has the view's largest residual: 206 px, with the model's apex projecting about 195 px above the photograph's (`data/comparisons/glessner/report.json`). That camera's fit is loose (check RMS 125 px), so this is a flag, not a measurement. Don't convert the pixels straight to feet (T-2206).

## Sources and tiers

- **HABS photograph 1**, Cervin Robinson, 1963-07-23, "Exterior from northwest", HABS IL-1015 (https://hdl.loc.gov/loc.pnp/hhh.il0118/photos.060903p). This is the owner's photograph. Tier 1, no known restrictions. Web copy: `chicago/prairie_1904_v1/research/public/glessner-habs-photo-01.jpg`; source record `data/sources/habs_glessner_photo_01_nw_1963.json`; T-2200 view `northwest-stable`.
- **HABS photographs 13 and 14** (Borchers, 1965 plates) show the curved rock-faced drum at the junction (`habs_glessner_photo_13_north_1965`, `..._14_north_inclined_1965`).
- **HABS sheet 4** (section) is where 32.9 / 43.9 ft come from: a masonry mass "beyond the section plane", eave and apex read off the sheet. T-2206's section readings put the cone's rise at 10.3 ft on the sheet against 11.0 in the model. Where the dated photographs and this reading disagree, reconcile them and write down which reading of the sheet was wrong and why. A sheet reading is not kept over three photographs without a stated reason.
- **Tiers:** `tower_north` is `inferred`. `tower_north_plan` (centre W 35.0, S 8.6, drum r 7.35 ft, eave r 8.35 ft) is `reconstructed`, under liberty L295. The plan position decides how much drum shows: how far back from the 18th Street wall the drum stands sets where the roof slope meets it. So the photograph bounds the plan as well as the heights.

## Acceptance

1. **A reference camera** for HABS photograph 1 at `data/reference_views/glessner_house/habs-01-northwest.json`, solved per `data/reference_views/README.md` (reuse T-2200's `northwest-stable` picks where they help). Render it with `tools/photo_match.mjs`. In its match record the tower's differences are each `fixed`: drum height showing above the roof, cone eave height, cone rise and eave width, and where the drum meets the roof slope. The view's other differences are written down `open` for T-2228, not fixed here.
2. **A cross-check from photograph 14 or 13:** state the `north-tower-apex` residual before and after. It must fall.
3. **Data:** new `tower_north` / `tower_north_plan` values in `glessner_house.json`, with sources and a note saying how the photograph and sheet 4 were reconciled. Update L295 in `docs/LIBERTIES.md`, and re-run the `data/comparisons/glessner` tables if their checks require it.
4. **Rebake** Glessner, full and light (phone), with before/after from the owner's viewpoint: 18th Street looking at the tower, at 390x780 and desktop. The north range roof meets the drum with no gap or hole. The cone's eave cap, the roof-edge pass and the downpipes follow the new height.
5. The Glessner roof-envelope, roof-edge and rainwater checks and the full gate pass.

## Coordination

- This is in the one-at-a-time Glessner chain: it waits on T-2216, and T-2217 now waits on this ticket.
- T-2469 (grey-greige granite as the default) bakes Glessner too. Build on dev after it lands, so this rebake keeps its stone colour.

**Unblocked 2026-10-13:** T-2216 merged (PR #776); this took its place in the queue. The block read: T-2216 — one Glessner House PR at a time (owner, 2026-10-11: group released to the loop and chained so lanes do not rebuild the same house in parallel)

## Owner clarification, 2026-10-13

The owner supplied a close crop of HABS 01 and directed that the north-facing gable wall continue flat into the tower, concealing the erroneous exposed curved front. The north elevation windows also differ: correct their positions, sizes, grouping and alignment against the photographs as part of this ticket. The owner requires photographic agreement, not merely an improved tower height. Re-read HABS 01, 13, 14 and the available north elevation drawing; validate the wall/tower junction and windows together in corresponding views before marking them fixed.

The owner also identified two defects in the review preview: the curved drum has a regular vertical grid instead of staggered rough-faced courses, and the tower eave projects across the sloping gable. Correct both in this ticket. Preserve the visible stone gable at the roof junction and remove any residual host-roof strip crossing a north window.
