---
id: T-1788
title: Give Chicago 4D a reusable browser human actor: skeletal animation, morphs, LODs and interaction hooks
state: open
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-09-30
closed: null
pr: null
claimed_by: null
blocked_on: T-1787
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: null
decision: null
decision_answer: null
---

Prepare the existing three.js browser renderer to display and interact with portable
humans rather than treating the People drawer as the only representation of a resident.
Implementation target: `kevinrhaas/chicago` **dev**.

**Acceptance:**

- Add a reusable human-actor module using the project's existing `GLTFLoader`,
  `SkeletonUtils` and scene lifecycle. Load a T-1786 human instance by existing person ID,
  clone skinned assets safely, place it on terrain, update it and dispose it without leaks.
- Support named skeletal clips at minimum: idle, walk and one gesture; support morph-target
  weights for blink/jaw/basic expression when present, while degrading cleanly when a
  lightweight LOD omits them.
- Implement deterministic distance/quality LOD selection tied to the project's Full/
  Balanced/Light concepts. Far people do not pay close-person face, shadow or animation
  costs. Avoid per-frame work for actors outside the relevant update range.
- Add interaction hooks without inventing the final conversation system: hover/select or
  focus, approach/use trigger, person ID, current state, optional interaction radius and a
  callback/event that can open the existing resident card or future dialogue.
- Keep identity/data separate from visuals. The actor resolves `beaubien_mark` or another
  existing person record; it does not create a second resident database.
- Add browser tests and smoke coverage for desktop and mobile: load, animation, LOD swap,
  selection, route/terrain coexistence, scene-year gating, no human assets in a year that
  does not request them, and no regressions to existing building GLBs.

**Stop condition:** the browser can host one fully rigged interactive human as a normal
Chicago 4D scene object before a historical person is authored.
