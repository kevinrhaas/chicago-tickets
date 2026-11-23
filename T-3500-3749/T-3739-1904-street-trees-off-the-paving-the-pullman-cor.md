---
id: T-3739
title: 1904 street trees off the paving: the Pullman corner elm moved off the 18th Street walk's crossing, and the tree planter refuses any trunk on a walk, carriage walk, corner crossing or drive
state: done
epic: META
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-11-23
closed: 2026-11-23
pr: 2326
claimed_by: run 11/23/2026, 10:54:16 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-11-23T21:57:22Z
claimed_run: null
claimed_at: 2026-11-23T16:54:17.414Z
decision: null
decision_answer: null
---

1904 street trees off the paving: the Pullman corner elm moved off the 18th Street walk's crossing, and the tree planter refuses any trunk on a walk, carriage walk, corner crossing or drive.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

Kevin, 2026-11-23, with a screenshot of the east walk of Prairie Avenue at 18th Street, before the Pullman house: "i am not sure that tree would be in the middle of the sidewalk".

**What was wrong:** the tree is the pictured corner elm `prairie__prairie_ic_16_18#p04`, read off the Detroit print (`loc_det_4a08065_pullman_residence`) and Taylor's no. 1445 at 259.8 m along Prairie's east planting line. The corner crossing laid later (T-3200, `prairie__prairie_ic_16_18.x.e18th`, attested from the same Detroit print) carries the 18th Street walk across that parkway from 258.9 to 260.7 m, so the trunk stood 0.9 m inside the paving. The planter checked only carriage walks and alley mouths, never corner crossings or drives. A sweep of all 415 1904 trees against every walk, carriage walk, corner crossing and drive found no other trunk on paving.

**Acceptance:**
- Kevin, 2026-11-23: "i think you should keep the crossing and lose the elm in that scene", "unless you are certain about that elm and that crossing". Not certain (the readings were put on the planting line by assumption and the two cameras disagree by 2-4 m along this front), so the elm is withdrawn: marked `withdrawn` in pictured_1904.json with its reading kept, no tree planted, liberty L-pullman-corner-elm-withdrawn-3739. The crossing stays.
- `plant_prairie_1904_street_trees.py` keeps rule trees off corner crossings and drives as it does off carriage walks, and stops (so `--check` and the gate refuse) if any trunk touches a walk, carriage walk, crossing or drive.
- Desktop 1280x800 and phone 390x780 before and after pictures inline in the PR and on closing.
