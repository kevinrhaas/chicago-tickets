---
id: T-3492
title: 1812: raise the factor's house out of the ground on a stone underpinning with a doorstep, and seat the interpreter's house the same
state: claimed
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-07
closed: null
pr: null
claimed_by: run 11/7/2026, 3:20:52 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-07T21:20:53.096Z
decision: null
decision_answer: null
---

1812: raise the factor's house out of the ground on a stone underpinning with a doorstep, and seat the interpreter's house the same.

Owner, 2026-11-07, thread "Fix sunken 1812 house", with a screenshot looking west at
378 N Michigan Ave in 1812: *"this house looks sunken in 1812"*. The house is the US
factory (`first_fort_outer_factory`), west of the fort on the slope down to the river.

**Cause (measured):** the renderer beds a terrain-anchored building at the LOWEST ground
under its walls (buildings.js `groundUnder`, T-3029). The factory's walls stand on
0.93 m of relief (NW corner 1.53 m, SE corner 2.46 m on e1830_natural), so its east
front, door and ground-floor windows sit 0.5-0.9 m under the ground. The interpreter's
house has 0.32 m. Every other 1812 building has under 0.05 m.

**Acceptance:**
- The factory stands on a visible fieldstone underpinning under a hewn sill: its
  sill clears the ground at the uphill corner and the door sill clears the ground at
  the door, with a doorstep up to it; no wall, door or window is under the ground.
- The interpreter's house gets the same treatment for its 0.32 m.
- The heights are derived from the committed heightfield by a tool, re-checked in the
  gate, so a terrain change that buries a 1812 sill again turns the gate red.
- Every other 1812 building is checked and the result stated in the PR.
- Desktop and phone before/after shots from the owner's viewpoint.
- Reconstructed underpinning and step recorded as a liberty.
