---
id: T-2376
title: Match the Green Tree Tavern to its pictures
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
claimed_by: Codex Green Tree wagon bay and sash continuation 10/26/2026, 10:53:50 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-27T03:53:51.057Z
decision: null
decision_answer: null
---

Match the Green Tree Tavern to its pictures.

Owner, 2026-10-11: "if you have an image you should work towards it until it's a photographic representation of any images even drawings are ok, but it should look exactly perfectly like the image or drawing"; "redo any work already done to meet this high standard"; "you don't wrap the case until it matches the photo".

This building was built without being checked against its pictures (inventory of 2026-10-11, T-2368; compared before: partial). Open every picture listed here and read the building off the picture itself. Solve each one's camera into `data/reference_views/<structure_id>/<view>.json`, render with `node tools/photo_match.mjs`, and rebuild until the side-by-side shows nothing the picture shows differently: massing, bays, every opening's shape and height, ornament, cornice, porch and stoop, roof and chimneys, fence, materials and tone (AGENTS.md rule 11; `data/reference_views/README.md`). What the picture does not show stays reconstructed and recorded in `docs/LIBERTIES.md`.

Pictorial sources are tier 5: form only, never a coordinate. Several are drawn from memory or later (Andreas 1884, Kurz & Allison 1893), and some post-date 1835 (each is evidence of its own date, scene 1835-07-01, AGENTS.md rule 3): the build follows what each shows of the building as it stood then, and the match record says which picture governs where they disagree.

Pictures:
  source: `data/sources/andreas_1884_green_tree_hotel_plate.json`
  source: `data/sources/trowbridge_green_tree_1902.json`
  source: `data/sources/chm_green_tree_1859.json`
  source: `data/sources/kurz_allison_1893.json`
  picture: `chicago/reference/images/chicago/chicago_green_tree_tavern_1835.jpg`
  picture: `chicago/reference/images/chicago/chicago_green_tree_inn_1838.jpg`

**Acceptance:** every reference view of the building(s) below has its camera, its side-by-side from the GLB in the tree, and a match record with verdict `matches` and nothing open. The PR carries the before and after side-by-sides, plus desktop and 390x780 in-app shots with no page errors.

## Image gate
- green_tree_tavern


## Picture-review checkpoint — 2026-10-22

Both pictures show seven long-elevation bays; `_fenestration_gable_front` derives six and ignores `upper_windows`. Add an explicit optional eaves-bay count. Gable windows differ between Braunhold and Trowbridge; the off-centre entrance and low additions also need comparison.

No matching verdict or completion is claimed. See the [shared compound-render checkpoint](https://github.com/kevinrhaas/chicago/blob/steward/t3040-fort-reference-groups/chicago/4d/docs/RESEARCH/fort-reference-groups-T-3040/README.md) for source/date findings and the next implementation step.

**Released 2026-10-23** (claim of Codex frame picture-match integration 10/23/2026, 12:28:11 AM CT): First picture-led frame refinements and source corrections are saved in the GitHub recovery checkpoint aaeac5b0. Full image matches remain open. Shared generator and source prerequisites will be tracked separately; continue the original cases from the recorded previews.

**Released 2026-10-25** (claim of Codex Green Tree visible image-match continuation 10/25/2026, 5:38:41 PM CT): The bounded visible front correction is in PR #1328 (https://github.com/kevinrhaas/chicago/pull/1328), under final combined validation: two viewer-left sash, rightmost doorway, and matching native entrance/apron. T-2376 remains unfinished: the committed Andreas1838 discrepancy register still has visitor-visible annex massing and long-wall opening-pattern gaps. Conflicting upper/attic drawings and camera residuals are within tolerance under T-3153. No photo follow-up or false whole-case completion is filed.
