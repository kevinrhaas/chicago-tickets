---
id: T-2690
title: Prairie draft sweep: rebuild the unworked 1904 drafts' thin full-height slivers and tower-like bodies into normal period houses until their refine passes
state: claimed
epic: SOUTH_TIME
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-10-16
closed: null
pr: null
claimed_by: run 10/16/2026, 4:27:22 PM CT
blocked_on: null
needs_bake: true
closed_at: null
claimed_run: null
claimed_at: 2026-10-16T21:27:22.927Z
decision: null
decision_answer: null
---

Prairie draft sweep: rebuild the unworked 1904 drafts' thin full-height slivers and tower-like bodies into normal period houses until their refine passes.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 185 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> The owner asked for exactly one ticket for a light sweep of the unworked Prairie Avenue drafts (2026-10-16, thread 'Prairie draft sweep': 'this is not a sensible structure, there are several tall towers ... i only want one ticket here'). It is worked interactively at once, so it never waits in the queue.

**The ask (owner, 2026-10-16, thread "Prairie draft sweep"):** "a light sweep of the unworked buildings on prairie, for example this is not a sensible structure, there are several tall towers, etc. i only want one ticket here, so it should be a quick sweep to find the most egregious structures and then if possible fix them to some reasonable historical match otherwise make a reasonable judgement to make them look normal until we get to a deep pass." His screenshot is 1729 (Pullman) from the corner of 18th, looking north-east.

**What the sweep found.** The "towers" are the draft fit's leftovers, built full height under their own cornices: 140 strips under 2.5 m thick, at two or more storeys, along the sides of 68 drafts (a slightly skewed Sanborn outline fills as its largest rectangle plus side strips), pieces standing clear in front of the street wall (1729's Prairie portico, traced as a range, stood 3.75 m out on the lawn as a three-storey 1.2 x 2.3 m shaft), and street bodies 3 to 4.8 m wide (2013, 1736, 2000, 2010, 2011).

**Acceptance:**
1. Fixed in the shared builder (`tools/draft_prairie_1904.py` and the rules' `fit`), not house by house: a strip under 2.5 m folds into the rectangle it lies against when the joint box is >= 90 % inside the traced fill; a strip nothing can take is one storey; a piece more than 2 m clear in front of the street wall is a one-storey porch; a bay or porch the fit left short of the wall stands against it; a street body under 5.5 m is widened to 5.5 m inside its lot.
2. Strips under 2.5 m at two or more storeys: 140 before, 0 after (only the 1.2 m stone-front veneers remain thin, and they are facades, not pieces).
3. No geometry added: the drafts' part count falls (421 to 344), so the 1904 spawn's triangles fall too.
4. Records whose refine is claimed, refined on the builder (1801 Kimball) or built on another kit are untouched; grades are not changed.
5. The liberty is amended under `L-draft-prairie-18-20-west-2329` (which every later block's liberty quotes) and the builder's self-test proves the fold and that a real notch stays a notch.
6. Before and after from the street at desktop and phone width in the project folder `prairie-draft-sweep/`.
