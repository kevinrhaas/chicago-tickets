---
id: T-3017
title: 1904 parkway elms grown as the open-grown American elm: a forked trunk, arching limbs and hanging sprays in place of the fan-shaped leaf cards, then tuned for desktop and phone GPU
state: review
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-22
closed: null
pr: 1199
claimed_by: run 10/22/2026, 10:00:36 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-22T15:00:37.555Z
decision: null
decision_answer: null
---

1904 parkway elms grown as the open-grown American elm: a forked trunk, arching limbs and hanging sprays in place of the fan-shaped leaf cards, then tuned for desktop and phone GPU.

Owner, 2026-10-22 (thread "Realistic elm tree branching"), with his dev screenshot of Glessner's
front, two photographs of open-grown American elms and a close-up of a crown: *"the newer trees are
just OK ... they appear as fans of leaves and not branches with variation ... when I look at elm trees,
they honestly look more like earlier versions. I am not saying to replace your new trees ... I would like
those elms to look more realistic so take some runs and that and gpu and performance optimize them, so
they render nicely"*; then *"those ones from before weren't perfect, they had cut off trunks and limbs
that hung in the air so dont over correct on that"*.

**Finding.** The parkway elm (street-trees.js) is ARCH.ulmus_americana grown by tree-model.js: one
straight bole running up as a leader with 3-6 scaffolds off its top, under a round crown. On the phone
(no near level) and past 10 m on desktop every elm is the `mid` level, which draws every other leaf
clump as ONE card of the massed clump tile (leaf atlas tile 5), 1.5-2.6 m across, faced out of the
crown. That tile is a fan of sprays radiating from its foot, so a crown is a few hundred fans.

**Acceptance:**
- The 1904 parkway elm grows as the open-grown American elm: a clear bole to about a third of its
  height, a fork into 2-4 co-dominant stems that fork again, every limb arching out, branches sweeping
  out and down, hanging twigs, and a crown widest near its top over an open interior. Judged against the
  owner's two photographs.
- No limb or leaf floats: every branch starts on its parent's wood inside its radius; every leaf card
  grows from a twig.
- The leaf at every level is sprays hung from twigs and faced to the street and to a visitor under
  the tree, not fans; the far level reads as the same tree.
- Liberty recorded (docs/LIBERTIES.md), changelog entry.
- Before/after at the T-2948 stands, desktop (full) and phone (light, 390x780), plus the street-tree
  triangle and frame readings: phone memory and 1904 spawn triangles stay inside their ceilings, and
  the phone draws no more triangles under the elms than dev does.
