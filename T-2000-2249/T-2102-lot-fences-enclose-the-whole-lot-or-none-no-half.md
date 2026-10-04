---
id: T-2102
title: Lot fences enclose the whole lot or none: no half-built yard fences open to the street
state: open
epic: META
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-10-04
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

Lot fences enclose the whole lot or none: no half-built yard fences open to the street.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 189 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> owner-reported bug (Kevin, 2026-10-04, project thread): yard fences stop partway up the side lot lines and leave the sides and street open; no existing ticket holds it

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

1. Every lot `tools/generate_lot_line_fences.py` fences is enclosed on all sides: both side lot lines run their whole length, front line to rear line, and the rear (alley) line keeps its cart gateway. Nothing stops partway up a side line any more.
2. The street face is left open where a building on the lot fronts that street (stands in the front half of the lot), so the house or store is seen from the road. A lot whose buildings stand only at the back gets its street line fenced too, with a street gateway.
3. A lot with no room for a yard behind its buildings, and every unimproved lot, still carries no fence: not every building gets a fence (owner, 2026-10-04: "i do like that not every building has a full fence around it").
4. A new run that shadows a fence already standing (dooryard garden pickets, T-0069's street-edge fences) gives up only the overlapping span, not the whole run, so the shadowing rule cannot recreate a half fence.
5. Recorded as a numbered liberty (next free L at merge time), resting on the 26 Nov 1833 Chicago Democrat ordinance that lets ringed hogs run at large in the town: a fence open on one side keeps nothing out.
6. Triangle and draw cost measured at both viewports; the smoke's fence counts updated deliberately if this changes them.

## Owner's words (2026-10-04)

> you have fences nicely at the rear of the properties each lot area but the sides and front are open all across. we would likely have these fenced in unless there is a frontage on that street so you see the properties, they should have a contiguous fences,, right? ... i do like that not every building has a full fence around it, that is logical, but the half built fence seems odd if there is no facing of a building on that street

## Cause

The yard rule (L161, T-0068) fences only the rear 40 ft of each lot: side fences start at `max(back of the front building + 10 ft, depth − 40 ft)`, so on a 150–180 ft lot the side fences cover a quarter of the line and the 80–110 ft between the house and the yard is open to both neighbours and the street. Nothing in the sources asks for that; it was the yard-depth cap.
