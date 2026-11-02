---
id: T-3316
title: 1701 Hibbard's rear stable and its 1½-storey south stable to the Chicagology photograph that shows them (a hipped roof under a square lantern, a gabled dormer, oculi, a gabled south wing; the image gate), on the parallelogram plan the 1911 sheet draws
state: open
epic: SOUTH_TIME
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-3310
opened: 2026-11-02
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

1701 Hibbard's rear stable and its 1½-storey south stable to the Chicagology photograph that shows them (a hipped roof under a square lantern, a gabled dormer, oculi, a gabled south wing; the image gate), on the parallelogram plan the 1911 sheet draws.

Piece 2 of 2 of **T-3310 — 1701 Hibbard's and 1721 Dexter's coach houses onto K12 to their pictures (the image gate), and every sheet-20 east rear polygon linked to its property or recorded unresolved (acceptance 1)**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-3310 was split (2026-11-02T15:28:06.866Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 10m ago, run 11/2/2026, 9:17:40 AM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/41469290120) — held by the run that split it
- branch `steward/t3310-dexter-1721-k12-stable` — the splitter's own

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/41469290120) may be working one of the pieces now.

## Image gate stays on T-3310

T-3310 carries an `## Image gate` section. The last of these pieces to close is refused (`done`) until every building it names matches every one of its reference views, so a slice that leaves a difference open says so in the match record.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

## What the splitting run found (T-3310 → T-3315, 2026-11-02)

- **The photograph shows this building.** Projected through the house's own solved camera (`data/reference_views/hibbard_house_1701_prairie/chicagology_front.json`, T-3240), the 1911 sheet's rear outline s20fp-1701-b2 falls at x ≈ 1555-1820 px (north part, 64-74 m off) and beyond the right edge (south part); 1709's stable falls off-frame (x > 3000). The building at the picture's right edge (x ≈ 1590-1945, eave ≈ y 880-900, lantern top ≈ y 760) is therefore 1701's own: a brick building, hipped roof, a square lantern with arched openings under a pyramidal cap and finial on the ridge, a central curved/pedimented gable dormer over a stone-framed window on the yard (west) face, round oculi low in the walls, stacks on the ridge, and at the right a lower gabled wing with a lunette in its gable and an oculus. Eave ≈ 6 m (185 px at ≈ 31 px/m).
- **The sheet** (1911, sheet 20, raster crop around px 4450-5200 × 3450-4050): r1 a '2'-storey brick parallelogram from row ≈ 3553 to ≈ 3816, west wall slanting ≈ 0.30 px east per px south, east wall on the right-of-way; r2 a '1½' brick stable crossed X joined to its south end, rows ≈ 3818-3936, its west wall ≈ 2.5 m west of r1's line, its south wall on the 1701/1709 lot line with the key's fire-wall sign at its west end. Robinson 1886 plate 10 crosses a brick stable over the whole outline.
- **The K12 kit cannot build it** (gable only; `ventilator` refused). The prairie_draft archetype has `hip` roofs, `lantern`, `dormers`, `stacks` (as Field's coach house, T-1936) but builds rectangles, not the sheet's parallelogram — choose between teaching one or the other the missing piece.
- 1721's piece (T-3315) shipped the K12 stable and its Detroit-photograph view (not shown: hidden behind the Pullman house).

**Released 2026-11-02** (claim of run 11/2/2026, 9:59:58 AM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/41474346700): PR #1617 (resume: gate still running, nothing red) stands 1701's stable on the 1911 sheet's parallelogram (the draft builder's new skew_per_m, 0.29) with the Chicagology photograph's hipped roof, bracketed cornice, square lantern (three arched lights a face), curved wall gable over a framed window, oculi, stacks and the wing's gable with its lunette, through the house's camera re-anchored into the stable's frame. Still open in the match record: the stable renders about 165 px (about 4 m along the wall) right of where the print shows it, since no camera fits the house's corners and the wing both and the house's own fit already disagrees with the sheet by up to 2.5 m on its bay; and the print's wing gable is narrower (about 2.4-3.3 m) than the sheet's 6.1 m end. Resolving it needs a better house camera solve or a second picture.

**Released 2026-11-02** (claim of run 11/2/2026, 12:34:46 PM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/41501004225): Camera re-solve tried, not resolvable from this one photograph; nothing built. (1) Focal freed: a joint fit of the house's 4 solve points + the stable's 6 features (wing corner, lantern, wall gable, 3 oculi) fits all within 9 px at eye (61.04, 31.89) stable frame, yaw 220.74, f 1616 (was 2182; the house's 4-point fit cannot fix f). It also nearly hides the 17.7 m rear range, which the current camera draws at x 1592-1754 up to y 557 where the print shows sky and the lantern. But it reads the house's SW cornice bed at 8.3 m against the rear camera's 10.8 m, and the bay junctions do not improve (v 9.6 vs the sheet's 8.3). (2) The house's own lines disagree with both cameras: the fence foot gives a street-front vanishing point near x -1500 and the flank cornice one near x +4100 (f about 2800), and the front cornice's north end reads y 412 in the print against 529 through the current camera. A longer lens pushes the sheet's stable further right (+390 px). (3) Moving the stable north to suit the photograph would cross the 1701/1637 lot line (sheet: lot line row 3535, stable north wall 3553), so the sheet's place stands. (4) Re-reading the wing: the flat eave at y 945 from x about 1793 to 1880 under r1's cornice may be r2's yard eave (a low hip), with a 2.9 m gabled hay dormer (apex x 1918, y 905, about 32 degrees) rather than a 6.1 m end gable. Measured from that corner the lantern sits near v 8 (r1's middle), not 4.2. Needs a second picture or a better-fitting house camera before building.
