---
id: T-3029
title: Set the Green Tree Tavern on its ground in 1835
state: done
epic: META
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-10-22
closed: 2026-10-22
pr: 1207
claimed_by: claude (project thread) 10/22/2026, 11:29:06 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-22T19:32:19Z
claimed_run: null
claimed_at: 2026-10-22T16:29:07.949Z
decision: null
decision_answer: null
---

Set the Green Tree Tavern on its ground in 1835.

Owner, 2026-10-22, with a screenshot of the inn in the 1835 scene: "green tree tavern in 1835 is sunken, it needs to be on the ground".

**What was wrong (measured):** the renderer beds a building on the lowest ground under it, sampled on a 5 x 5 grid over the mesh's bounding box. The Green Tree's rear ell (form.rear_ell, T-0083) runs 4.5 m east of the footprint down the South Branch bank, and the box's corner beside the ell lands on ground 0.09 m over the water, while the front door's ground is 0.99 m. So the inn stood 0.88 m sunk. The T-0141 seat was measured on the footprint polygon alone and never saw the ell.

**Fix:** (1) buildings.js beds a structure on the ground under its walls' feet (the triangle edges on y = 0, building-feet.js), not under its bounding box; 1904 does not move, 13 of 677 structures in 1835 and 5 in 1812 move by more than 2 cm, the Wolf Point Tavern lifts 0.27 m. (2) The Green Tree is re-seated 5.80 m west by the T-0141 rule with the ell included: the first seat at which every wall foot meets the ground within 0.10 m (the relief 95% of the 1835 town stands on). Its walk, yard goods, woodpile, sidecar and the `green_tree` stand follow.

**Acceptance:** the Green Tree's anchor is within 0.10 m of the ground at its front and side doors; before/after shots desktop and 390x780 from the same stands; gate green; the smoke parts that cover buildings, frontage and yard goods green.
