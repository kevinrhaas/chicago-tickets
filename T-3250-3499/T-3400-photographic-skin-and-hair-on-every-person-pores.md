---
id: T-3400
title: Photographic skin and hair on every person: pores, fine wrinkles, colour variation, soft subsurface glow, strand sheen
state: done
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-11-05
closed: 2026-11-06
pr: 1748
claimed_by: run 11/5/2026, 10:44:09 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-11-06T12:08:15Z
claimed_run: null
claimed_at: 2026-11-06T04:44:10.988Z
decision: null
decision_answer: null
---

Photographic skin and hair on every person: pores, fine wrinkles, colour variation, soft subsurface glow, strand sheen.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

Close up on dev (desktop and phone), Hans on the 1904 brougham and Otis Bardwell in
1835 show skin that is not one smooth surface: pores and fine creases that catch the
light, uneven colour (redder cheeks, nose, ears and knuckles), a soft translucent
glow where the light falls off, and hair that reads as strands with a sheen running
across them rather than plastic. Every portable human gets it, not only drivers. No
new textures; 1904 phone memory stays inside its ceiling.

## The ask (Kevin, 2026-11-06)

"and for hans, overall we look ok, but he looks odd still, hist clothing is form
fitting and he looks too smooth and not real, can you take a swing at improving the
quality of that human and set us on a path for all humans to look photographic
realistic?"

Split from T-3398 (which keeps the coat, hat and garment drape): this ticket is the
skin, face and hair surface, as a runtime shader patch beside fabric.js. It does not
touch driven-assembly-loader.js, fabric.js or the garment generator.
