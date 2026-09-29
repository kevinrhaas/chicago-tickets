---
id: T-1728
title: The 1904 Prairie Avenue street surfaces: carriageway paving, curbs, sidewalks and parkways as sourced materials on T-0474's layout
state: claimed
epic: SOUTH_TIME
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-28
closed: null
pr: null
claimed_by: run 9/28/2026, 9:22:33 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-09-29T02:22:34.002Z
decision: null
decision_answer: null
---

The 1904 Prairie Avenue street surfaces: carriageway paving, curbs, sidewalks and parkways as sourced materials on T-0474's layout.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 140 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> owner asked for the 1904 Prairie Avenue / Glessner House render path, 2026-09-28

Source library: **`chicago/prairie_1904_v1/`**, viewable at https://chicago.polecat.live/prairie-1904/viewer/. Read its README and `docs/research-gaps.md` first; cite library rows and dossier entries by id.

**Why (owner, 2026-09-28):** *"make sure we have the street and materials and how the road and
sidewalks were laid out"*. T-0474 lays out the geometry. This ticket gives each surface its period
material.

**Acceptance:** (one demonstration, never weakened to pass)

1. For each street face 16th–22nd, both sides of Prairie plus the cross streets the scene shows,
   assign the **carriageway surface**, **curb**, **parkway strip** and **sidewalk** a material with
   an existence range bounding 1 July 1904 and a tier.
2. **Evidence rule.** The library's `civic-dossier.json` holds the 1904 *Report to the Street Paving
   Committee … on the street paving problem of Chicago* (`civic-paving-1904`). The library itself
   warns that **"a citywide paving report does not identify a particular block's surface"**. It can
   **bound** the plausible materials; it can't **assert** one for a block. A block-level claim needs
   a dated photograph, an ordinance or special-assessment record for that street, or the Glessner
   House's own records for its frontage. Where none exists, the material is `reconstructed` and
   recorded in LIBERTIES. Sanborn 1911 sheets 20, 28 and 35 give hydrants, mains and the
   "Prairie Av. Blvd." designation, and the boulevard status should be researched: which authority
   paved and kept a boulevard in 1904.
3. **PBR textures** for each material, in the style of the 1835 `chicago_1835_pbr` set, with their
   provenance recorded. The tiling reads correctly from the T-1252 landing pose at both viewports.
4. The frame budget is measured before and after.

Blocked on **T-0474**, whose layout this ticket paints.
