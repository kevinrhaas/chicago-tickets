---
id: T-2386
title: Match the Wolf Point Tavern to its pictures
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
claimed_by: T2386 Wolf Point native picture signoff 10/25/2026, 8:35:11 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-26T01:35:12.067Z
decision: null
decision_answer: null
---

Match the Wolf Point Tavern to its pictures.

Owner, 2026-10-11: "if you have an image you should work towards it until it's a photographic representation of any images even drawings are ok, but it should look exactly perfectly like the image or drawing"; "redo any work already done to meet this high standard"; "you don't wrap the case until it matches the photo".

This building was built without being checked against its pictures (inventory of 2026-10-11, T-2368; compared before: partial). Open every picture listed here and read the building off the picture itself. Solve each one's camera into `data/reference_views/<structure_id>/<view>.json`, render with `node tools/photo_match.mjs`, and rebuild until the side-by-side shows nothing the picture shows differently: massing, bays, every opening's shape and height, ornament, cornice, porch and stoop, roof and chimneys, fence, materials and tone (AGENTS.md rule 11; `data/reference_views/README.md`). What the picture does not show stays reconstructed and recorded in `docs/LIBERTIES.md`.

Pictorial sources are tier 5: form only, never a coordinate. Several are drawn from memory or later (Andreas 1884, Kurz & Allison 1893), and some post-date 1835 (each is evidence of its own date, scene 1835-07-01, AGENTS.md rule 3): the build follows what each shows of the building as it stood then, and the match record says which picture governs where they disagree.

Pictures:
  picture: `chicago/reference/images/chicago/chicago_wolf_point_1833.jpg`
  picture: `chicago/reference/images/chicago/chicago_wolf_point_1830.jpg`
  picture: `chicago/reference/images/chicago/chicago_wolf_point_1830_and_1833_engravings.jpg`
  picture: `chicago/reference/images/chicago/chicago_wolf_point_1832.jpg`
  picture: `chicago/reference/images/chicago/chicago_wolf_tavern_miller_house_1832.jpg`
  picture: `chicago/reference/images/chicago/chicago_town_view_1833_colbert.jpg`
  picture: `chicago/reference/images/chicago/chicago_wolf_point_1833_hammon.jpg`
  picture: `chicago/reference/images/chicago/chicago_wolf_point_1833_nypl.jpg`

**Acceptance:** every reference view of the building(s) below has its camera, its side-by-side from the GLB in the tree, and a match record with verdict `matches` and nothing open. The PR carries the before and after side-by-sides, plus desktop and 390x780 in-app shots with no page errors.

## Image gate
- wolf_point_tavern


## Picture-review checkpoint — 2026-10-22

The inspected NYPL Blanchard/Shober lithograph bears a legible 1867 publication line. Pictures show parallel gable-front volumes with two entrances and roof-piercing stacks; current model puts core/addition inline. Register that specific source and implement opt-in ridge/entrance composition before solving.

No matching verdict or completion is claimed. See the [shared compound-render checkpoint](https://github.com/kevinrhaas/chicago/blob/steward/t3040-fort-reference-groups/chicago/4d/docs/RESEARCH/fort-reference-groups-T-3040/README.md) for source/date findings and the next implementation step.

**Released 2026-10-23** (claim of school_lighthouse_castle_bridge 10/23/2026, 7:14:35 AM CT): Run wrapped after verified frozen recovery at https://github.com/kevinrhaas/chicago-evidence/blob/3575ef6/evidence/image-match-2026-10-22/final-parallel-recovery-20261023T1430/RECOVERY.md . School recess is prepared UNRUN; Wolf Point latest actual door/log comparison differs. Original full picture-match acceptance remains unfinished and unchanged; no matches or completion claimed. Source-origin identity/date uncertainty and owner-approved attributed school use are preserved.
