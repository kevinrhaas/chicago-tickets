---
id: T-2633
title: Navigator Go to follows the Confidence view: the 'Include reconstructed roofs' checkbox removed, and results of a hidden grade shown dimmed with the reason
state: done
epic: RENDERING
requested_by: owner
seen: true
effort: S
legacy_id: NAV-404
parent: null
opened: 2026-10-16
closed: 2026-10-17
pr: 965
claimed_by: run 10/17/2026, 3:58:39 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-17T11:28:27Z
claimed_run: null
claimed_at: 2026-10-17T08:58:39.183Z
decision: null
decision_answer: null
---

Navigator Go to follows the Confidence view: the 'Include reconstructed roofs' checkbox removed, and results of a hidden grade shown dimmed with the reason.

**Navigator Mk II — NAV-404.** Filed by the owner, 2026-10-16, from his design doc "Field Navigator Mk II · Experience redesign" (Rev 1.0, base `dev` @ cc2e803): *"build all of the tickets necessary for this ... then we do all of this interface work, follow that with the balance of buildings in 1904"*. The doc is written for students aged 14–16, mostly on phones: fun and easy, never trading away honesty about sources. Full transcription, owner rulings on its open questions, the mockups (M1–M10) and the dev screenshots it cites: chicago-tickets `evidence/navigator-mk2-2026-10-16/` (`DESIGN.md`; open `original/Navigator Design Doc.dc.html` in a browser for the mockups).

## Depends on

- T-2630 (NAV-401) — do not claim this ticket until it has merged; take the next workable ticket instead.

## What to build

§07. Remove "Include reconstructed roofs (0)". If Reconstructed is hidden in the Confidence view
(today's `#cm-reconstructed`; the app from NAV-601 (T-2647)), those results show dimmed and say why.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- [ ] With Reconstructed hidden, reconstructed results are dimmed with a one-line reason; shown again when the grade is shown.
- [ ] The checkbox is gone and no smoke step depends on it.
- [ ] Works on a 390x844 phone and a 1440x900 laptop, and the 390x780 mobile smoke (the release gate) passes.
- [ ] Works in all four machine skins and with reduced motion.
- [ ] No ids, file paths or snake_case visible to a visitor (NAV-1003's lint passes once it has landed).
- [ ] Locked terms used exactly: Attested, Inferred, Reconstructed, Confidence view, Liberties, Sources, Jaunts.
- [ ] Every element id the smoke reads is preserved, or the smoke is updated in the same PR.
- [ ] A changelog.d/<ticket>.json entry says what a visitor will see, within the What's-New budget.
