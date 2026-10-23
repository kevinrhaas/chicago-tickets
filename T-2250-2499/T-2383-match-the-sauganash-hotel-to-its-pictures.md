---
id: T-2383
title: Match the Sauganash Hotel to its pictures
state: claimed
epic: TOWN
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-11
closed: null
pr: null
claimed_by: Codex frame picture-match integration 10/23/2026, 12:28:11 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-23T05:28:12.626Z
decision: null
decision_answer: null
group: T-2376,T-2383,T-2384,T-2385
---

Match the Sauganash Hotel to its pictures.

Owner, 2026-10-11: "if you have an image you should work towards it until it's a photographic representation of any images even drawings are ok, but it should look exactly perfectly like the image or drawing"; "redo any work already done to meet this high standard"; "you don't wrap the case until it matches the photo".

This building was built without being checked against its pictures (inventory of 2026-10-11, T-2368; compared before: partial). Open every picture listed here and read the building off the picture itself. Solve each one's camera into `data/reference_views/<structure_id>/<view>.json`, render with `node tools/photo_match.mjs`, and rebuild until the side-by-side shows nothing the picture shows differently: massing, bays, every opening's shape and height, ornament, cornice, porch and stoop, roof and chimneys, fence, materials and tone (AGENTS.md rule 11; `data/reference_views/README.md`). What the picture does not show stays reconstructed and recorded in `docs/LIBERTIES.md`.

Pictorial sources are tier 5: form only, never a coordinate. Several are drawn from memory or later (Andreas 1884, Kurz & Allison 1893), and some post-date 1835 (each is evidence of its own date, scene 1835-07-01, AGENTS.md rule 3): the build follows what each shows of the building as it stood then, and the match record says which picture governs where they disagree.

Pictures:
  source: `data/sources/andreas_1884_sauganash_hotel_plate.json`
  source: `data/sources/trowbridge_sauganash_hotel.json`
  source: `data/sources/kurz_allison_1893.json`
  picture: `chicago/reference/images/chicago/chicago_sauganash_hotel_1831_petford.jpg`
  picture: `chicago/reference/images/chicago/chicago_sauganash_hotel_1831.jpg`
  picture: `chicago/reference/images/chicago/chicago_sauganash_tavern_1835.jpg`
  picture: `chicago/reference/images/chicago/chicago_wolf_point_1833.jpg`

**Acceptance:** every reference view of the building(s) below has its camera, its side-by-side from the GLB in the tree, and a match record with verdict `matches` and nothing open. The PR carries the before and after side-by-sides, plus desktop and 390x780 in-app shots with no page errors.

## Image gate
- sauganash_hotel


## Picture-review checkpoint — 2026-10-22

Group with Carpenter. `sauganash_plate_baseline.json` supplies measured vanishing points (−1467.2, 6462.5), focal 3664.7 px and horizon 917.5 on 2017×1296. Fit translation against the render. Measured 2.392 m doorcase/1.923 m opening and 45 px transom are not fully consumed by `_frontispiece`. Braunhold/Petford/Trowbridge are related compositions, not independent witnesses.

No matching verdict or completion is claimed. See the [shared compound-render checkpoint](https://github.com/kevinrhaas/chicago/blob/steward/t3040-fort-reference-groups/chicago/4d/docs/RESEARCH/fort-reference-groups-T-3040/README.md) for source/date findings and the next implementation step.
