---
id: T-2646
title: Confidence view renderer: per-grade color, mode and opacity uniforms on the batched materials, Ghost sorted last with depthWrite off, Dither reusing the Reconstructed path, 60 fps held at the mid-tier phone profile
state: done
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: NAV-603
parent: null
opened: 2026-10-16
closed: 2026-10-16
pr: 921
claimed_by: run 10/16/2026, 5:16:19 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-17T04:14:54Z
claimed_run: null
claimed_at: 2026-10-16T22:16:19.888Z
decision: null
decision_answer: null
---

Confidence view renderer: per-grade color, mode and opacity uniforms on the batched materials, Ghost sorted last with depthWrite off, Dither reusing the Reconstructed path, 60 fps held at the mid-tier phone profile.

**Navigator Mk II — NAV-603.** Filed by the owner, 2026-10-16, from his design doc "Field Navigator Mk II · Experience redesign" (Rev 1.0, base `dev` @ cc2e803): *"build all of the tickets necessary for this ... then we do all of this interface work, follow that with the balance of buildings in 1904"*. The doc is written for students aged 14–16, mostly on phones: fun and easy, never trading away honesty about sources. Full transcription, owner rulings on its open questions, the mockups (M1–M10) and the dev screenshots it cites: chicago-tickets `evidence/navigator-mk2-2026-10-16/` (`DESIGN.md`; open `original/Navigator Design Doc.dc.html` in a browser for the mockups).

## Depends on

- T-2671 (NAV-S04) — do not claim this ticket until it has merged; take the next workable ticket instead.

## What to build

§09 and §14 "Confidence view rendering". Per-grade uniforms in `js/confidence.js` and
`js/batch-material.js`: color (default gold / silver / bronze, NAV-S04 (T-2671)), mode (Tint / Ghost / Dither) and opacity. Ghost needs depthWrite off and
sorts last; Dither reuses today's Reconstructed massing path. No new draw calls per grade where the
batches already split by grade. Must not undo the performance group's budgets.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- [x] Each grade can be tinted, ghosted or dithered at any opacity from a test hook; hiding a grade removes its meshes as #cm-* does today.
- [ ] The smoke's frame and draw budgets hold with X-RAY on; 60 fps on the mid-tier phone profile.
- [ ] Works on a 390x844 phone and a 1440x900 laptop, and the 390x780 mobile smoke (the release gate) passes.
- [ ] Works in all four machine skins and with reduced motion.
- [x] No ids, file paths or snake_case visible to a visitor (NAV-1003's lint passes once it has landed).
- [x] Locked terms used exactly: Attested, Inferred, Reconstructed, Confidence view, Liberties, Sources, Jaunts.
- [x] Every element id the smoke reads is preserved, or the smoke is updated in the same PR.
- [x] A changelog.d/<ticket>.json entry says what a visitor will see, within the What's-New budget.
