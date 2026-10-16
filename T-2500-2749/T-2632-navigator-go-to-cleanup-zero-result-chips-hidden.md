---
id: T-2632
title: Navigator Go to cleanup: zero-result chips hidden, titles wrapping to two lines, every row showing distance and bearing, filters Places · People · Shops & work · Viewpoints
state: open
epic: RENDERING
requested_by: owner
seen: true
effort: S
legacy_id: NAV-403
parent: null
opened: 2026-10-16
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

Navigator Go to cleanup: zero-result chips hidden, titles wrapping to two lines, every row showing distance and bearing, filters Places · People · Shops & work · Viewpoints.

**Navigator Mk II — NAV-403.** Filed by the owner, 2026-10-16, from his design doc "Field Navigator Mk II · Experience redesign" (Rev 1.0, base `dev` @ cc2e803): *"build all of the tickets necessary for this ... then we do all of this interface work, follow that with the balance of buildings in 1904"*. The doc is written for students aged 14–16, mostly on phones: fun and easy, never trading away honesty about sources. Full transcription, owner rulings on its open questions, the mockups (M1–M10) and the dev screenshots it cites: chicago-tickets `evidence/navigator-mk2-2026-10-16/` (`DESIGN.md`; open `original/Navigator Design Doc.dc.html` in a browser for the mockups).

## Depends on

- T-2630 (NAV-401) — do not claim this ticket until it has merged; take the next workable ticket instead.

## What to build

§07, MED finding (`IMG_6947`: "Corners 0", cut-off titles). Search stays `js/destinations.js` /
`js/goto.js`; filters Places · People · Shops & work · Viewpoints.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- [ ] QA-14: open Go to in 1904; no zero-count chips, long titles wrap to two lines.
- [ ] Each result row shows distance and bearing from where you stand.
- [ ] Works on a 390x844 phone and a 1440x900 laptop, and the 390x780 mobile smoke (the release gate) passes.
- [ ] Works in all four machine skins and with reduced motion.
- [ ] No ids, file paths or snake_case visible to a visitor (NAV-1003's lint passes once it has landed).
- [ ] Locked terms used exactly: Attested, Inferred, Reconstructed, Confidence view, Liberties, Sources, Jaunts.
- [ ] Every element id the smoke reads is preserved, or the smoke is updated in the same PR.
- [ ] A changelog.d/<ticket>.json entry says what a visitor will see, within the What's-New budget.
