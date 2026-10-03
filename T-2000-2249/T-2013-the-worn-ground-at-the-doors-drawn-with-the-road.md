---
id: T-2013
title: The worn ground at the doors drawn with the road's own surface: same grit, tone and colour, no pixel blocks
state: claimed
epic: META
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: null
opened: 2026-10-02
closed: null
pr: null
claimed_by: run 10/2/2026, 11:31:13 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-03T04:31:13.919Z
decision: null
decision_answer: null
---

The worn ground at the doors drawn with the road's own surface: same grit, tone and colour, no pixel blocks.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 238 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> the owner asked for it directly on 2026-10-03, a follow-up to T-1984 he is looking at on dev

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## The owner's words (2026-10-03, on dev, Matthias Mason & Co. on Lake Street)

> the road looks overall good and i like the way that you put stuff in front of places that were worn dirt but that texture is not nearly as nice as the road texture and it shows through so make those areas with dirt the same as where the road is the same texture color so it does not look pixely and jagged

## Cause

T-1984's worn ground (`data/enclosures/town_entrance_aprons.json`) is drawn by `yards.js` as `trodden_earth`, the estray pen's surface: a 128 px canvas of 2 px hash blocks over 3.1 m, darker than the road. Next to T-1811's road (256 px grit over 1.6 m, shaded per fragment in the road's tones) it reads as blocky and a different dirt.

## Done when

The door ground is drawn from the road's own grit tile and dirt tones in world coordinates, so a path that meets the road continues it with no seam in texture or colour, and its edge into the grass is soft.
