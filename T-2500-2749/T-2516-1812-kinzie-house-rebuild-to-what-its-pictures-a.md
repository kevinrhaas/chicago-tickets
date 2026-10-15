---
id: T-2516
title: 1812 Kinzie house: rebuild to what its pictures agree on against the build — the piazza roof carried down from the main roof and its height, the gable-end lights, the length against the end — and solve Sarony's lithograph (Currey 1912 / Kirkland 1893) into a camera
state: review
epic: SOUTH_TIME
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-15
closed: null
pr: 829
claimed_by: run 10/15/2026, 10:22:42 AM CT
blocked_on: null
needs_bake: true
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38758995503
claimed_at: 2026-10-15T15:22:43.059Z
decision: null
decision_answer: null
---

1812 Kinzie house: rebuild to what its pictures agree on against the build — the piazza roof carried down from the main roof and its height, the gable-end lights, the length against the end — and solve Sarony's lithograph (Currey 1912 / Kirkland 1893) into a camera.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

Filed by T-2498, which solved the Cram 1893, Teich, Eastman 1820 and Gemmell cameras of `kinzie_house_1812` and read each against the build (`data/reference_views/kinzie_house_1812/*.match.json`). What the pictures say together, and the build does not:

- **Piazza roof.** Lossing 1869, Cram 1893 and the Teich painting carry the main roof down over the piazza in one plane; the 1857 engraving hangs a flatter roof under the main eave, and the build follows it (the Lossing record's ruling). Three of five against one is worth re-ruling. Sarony's lithograph (below) should be read for it before choosing.
- **Piazza height.** On the Cram plate every post stands about 1.7 times as tall against its bay as the build's (feet 6-10 px low, heads 7-10 px high from its camera). With a one-plane roof that is a taller front wall, a flatter pitch over the piazza or an engraver's stretch: measure it on Sarony too.
- **Gable lights.** The Teich painting draws a small square light high in the west gable; the 1857 engraving and Cram show something dark there; Eastman 1820 draws two windows in the east end at the eave. The archetype leaves both ends unpierced.
- **Length against the end.** Teich and Gemmell draw the front shorter against the end than the build's 40 ft x 22 ft (itself a liberty: Quaife 1928 not reached).
- **Roof colour.** Teich is the only colour picture (red-brown, shingle); a colour from it would be a reconstruction with a liberty.
- **Walls** are NOT this ticket: all four later pictures draw them light and smooth, and the standing ruling is squared log for 1812 (Moses and Kirkland; Lossing draws them coursed).
- **Sarony's lithograph** of Juliette Kinzie's sketch is in the library (`sarony_kinzie_residence_currey_1912_plate`, the Kirkland p. 73 copy `kirkland_1893_kinzie_mansion_1812_plate`) with no camera: solve it into `data/reference_views/kinzie_house_1812/`, as the picture drawn by a member of the household it should govern where the others disagree.

**Acceptance:** Sarony's camera solved and matched; the piazza roof, its height and the gable ends rebuilt (or ruled against, with the reason in each match record) and the house rebaked; every view of the house re-rendered from the new GLB, with its open items closed or ruled.

## Image gate
- kinzie_house_1812
