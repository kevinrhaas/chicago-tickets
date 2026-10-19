---
id: T-2686
title: Grade every structure by its pictures: Attested when a reasonable picture of it exists, Inferred when only maps or text record it, Reconstructed when our model of the town placed it; the 1835 streets drawn on the plat are Attested
state: done
epic: META
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-10-16
closed: 2026-10-16
pr: 907
claimed_by: run 10/16/2026, 3:56:52 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-16T22:23:34Z
claimed_run: null
claimed_at: 2026-10-16T20:56:52.465Z
decision: null
decision_answer: null
---

Grade every structure by its pictures: Attested when a reasonable picture of it exists, Inferred when only maps or text record it, Reconstructed when our model of the town placed it; the 1835 streets drawn on the plat are Attested.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 184 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> the owner asked for this grading rule directly on 2026-10-16 (thread: structure grading); it is worked now in an interactive session

## The owner's words (2026-10-16)

> for a structure if there is an image of it that is reasonable, not just like a corner or side, but even the robert hall house we did earlier, that is attested, something inferred would be like we only have the sanborn map level description, or some text description of it, but nothing to visually depict its size or scope or appearance, and then reconstructed will be where we made a determined choice that there should have been, based on model of town or other guiding research that there could have or would have been a structure of that type and form and appearance there, make sure we add that level of consideration to how we are grading structures. and aside like for 1835, all the streets should be attested

("the robert hall house" is Robert Law's house, 1620 Prairie, built to its 1874 engraving.)

## What changes

Today a building's one grade is `documented_range.confidence` — whether a source says it stood
there — and it is what the HUD counts, Go to filters and the card's Standing row read. Under that
reading a Sanborn footprint makes a house attested and a photograph adds nothing. The owner's
rule is a structure grade on its own axis:

- **Attested** — a reasonable picture of it exists: a photograph, print or drawing showing the
  building whole (a front, oblique, side or rear view), or any picture an image-gate camera has
  been solved on. Not a detail, an interior, a plan, or a street view it sits in the corner of.
- **Inferred** — maps (Sanborn and the like) or text record it, but nothing shows how it looked.
- **Reconstructed** — our model of the town placed it (its existence is reconstructed) and no
  picture shows it.

Per-attribute grades do not change. The 1835 streets drawn on the 1830 plat or the 1834 surveys
are Attested; the three roads no map draws keep their grade.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- [ ] AGENTS.md carries the rule as hard rule 12, beside the image gate; docs/PROVENANCE.md explains it.
- [ ] One tool derives every structure's grade in every scene by that rule, from the picture join the Images tab uses, the image-gate cameras and a committed rulings file whose every entry says why; its self-test breaks each branch.
- [ ] compile_scene writes the grade into each sidecar and each 1835 street; check.sh holds it.
- [ ] The card shows the grade and why; the Confidence menu counts and Go to read it.
- [ ] 1904, 1835 and 1812 regraded; the counts are in the PR.
- [ ] A changelog.d/T-2686.json entry, within the What's-New budget.
