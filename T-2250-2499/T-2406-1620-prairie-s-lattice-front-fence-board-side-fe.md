---
id: T-2406
title: 1620 Prairie's lattice front fence, board side fence, front chimney stack and slated mansard from its pictures, and both match records brought to matches
state: open
epic: SOUTH_TIME
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: T-2370
opened: 2026-10-12
closed: null
pr: null
claimed_by: null
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: null
decision: null
decision_answer: null
---

1620 Prairie's lattice front fence, board side fence, front chimney stack and slated mansard from its pictures, and both match records brought to matches.

Piece 4 of 4 of **T-2370 — Match 1620 Prairie (Law) to its pictures: the 1874 landowner engraving and the 1898 Tribune view**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2370 was split (2026-10-12T05:42:39.827Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 24m ago, run 10/12/2026, 12:18:18 AM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/38206913932) — held by the run that split it
- branch `steward/t2370-1620-law-pictures` — the splitter's own

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/38206913932) may be working one of the pieces now.

The pictures, their cameras and the match records (every difference, `fixed` or `open`) are in `data/reference_views/law_house_1620_prairie/` (T-2403); the pictures' source records are `land_owner_1874_05_homes_of_chicago_1620_law` and `chicago_tribune_1898_01_09_prairie_widows`. Read the pictures themselves, not the summary, and render with `node tools/photo_match.mjs`.

**Acceptance:** the `fence`, `chimney` and `roof covering` differences `fixed` (the interlaced-arch lattice on a base with square piers, the board fence on the north side, the tall stack at the front of the north wall, the lower faces slated), and BOTH match records `matches` with nothing open; `ticket.mjs done` enforces it through the image gate below.

## Image gate
- law_house_1620_prairie

## Finding from T-2409 (2026-10-12): the 1874 camera's height datum

Building the entrance against the May 1874 engraving, the front's lower parts all sit about 1.5-2 m LOWER against the house than `landowner_1874_from_northeast.json` puts them: through that camera the porch's balustrade top reads about 0.25 m over grade, the south bay's principal-storey sills about 0.36 m and the pavilion's about 0.5 m, where the record has a 1.4 m principal floor (sills about 2.0 m); the fence's base at the street line reads about -2.25 m. The offset is the same under the bay and under the porch, so it is the camera's vertical datum (its eye 0.7 m under grade, read off the north wall's foot, which the board fence may hide), not any one feature. Horizontal readings are unaffected (x is independent of height). It matters to this ticket because the wall head (`storey_heights_m`, 8.2 m) was read through the same camera from the cornice: if the engraving's principal floor is at its porch level, its floor-to-cornice is nearer 8.5 m than the 6.8 m built. Re-solve the camera's height with the porch/stoop head as a second vertical control before the 1874 record is brought to `matches`.

## Finding from T-2404 (2026-10-12)

T-2404 (PR #729) stood the north pavilion, its crown and the crown's round-headed dormer, and marked the engraving's `north pavilion` and `crown` differences and the Tribune's `north pavilion` difference fixed. It added one OPEN difference to `landowner_1874_from_northeast.match.json`, and this ticket owns it because it closes both records: **corner strip** — the light strip the engraving draws down the pavilion's north corner (a stone or painted quoin); the pavilion turns that corner in its own brick. The pavilion is a K08 `k08.projection.full_height` on the street front with `flush_corner: "right"`, so a quoin strip there is a strip on the projection's north cheek/front corner, not on the K01 north wall.
