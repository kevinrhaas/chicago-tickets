---
id: T-2864
title: Season setting in every year: 1812 and 1835 get spring, fall and winter for woods, prairie, ground and sun
state: review
epic: META
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-10-19
closed: null
pr: 1089
claimed_by: run 10/19/2026, 7:56:36 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-19T12:56:36.480Z
decision: null
decision_answer: null
---

Season setting in every year: 1812 and 1835 get spring, fall and winter for woods, prairie, ground and sun.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 150 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> owner asked directly in the project thread (2026-10-19): Season should be offered in all years

## The owner's ask (2026-10-19, project thread "Season setting on dev")

> We had a season setting before and we had all the seasons I could not find that in dev am I missing it or did you lose it?
> I am in 1812 and don't see it
> We would expect it for all years, so add that

Settings › Season (T-2481, PR 792) is only offered where there are parkway elms, so 1904 alone.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- Settings › Season is offered in 1812, 1835 and 1904 (Street trees stays 1904-only).
- In 1812 and 1835 each season changes the sun's date (summer = the scene's own date), the ground
  (snow, sward, leaves via season.js), the grown woods (spring first leaf, fall thinner and turned,
  winter bare limbs), the thickets/shrub sprays and the prairie sward (fresh / tawny / straw), and
  the buildings' roofs take snow as 1904's do.
- The labels no longer claim 1 July 1904 in other years; the liberty is recorded for the new years.
- Summer is unchanged pixel for pixel; no budget regression at summer; the gate is green.
