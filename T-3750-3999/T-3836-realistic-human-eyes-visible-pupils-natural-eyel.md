---
id: T-3836
title: Realistic human eyes: visible pupils, natural eyelids and convincing wet reflections
state: claimed
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-11-28
closed: null
pr: null
claimed_by: Codex eye realism 11/28/2026, 8:22:49 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-28T14:22:50.347Z
decision: null
decision_answer: null
---

Realistic human eyes: visible pupils, natural eyelids and convincing wet reflections.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- Owner, 28 November 2026: "definitely work on eyes to make them perfectly realistic".
- Work independently of PR #2371, whose merge belongs to the other session.
- Correct fitted eye rotation and close-range binocular focus without changing a person's
  head fit, recorded colouring, source portraits or identity mapping. Preserve full blinks.
- Inspect actual published-app front and oblique images of William Grey, a photographed
  adult and a child, including Full, Balanced and Light; state remaining visible defects.
- Add no eye geometry, textures, lights or draw passes. Verify geometry and residency budgets;
  software-rendered stills do not establish physical-GPU crowd performance.
- Run meaningful geometry/gaze regressions and the repository's complete native gate before
  a source commit; use the required desktop/mobile published checks before a dev merge.
