---
id: T-2654
title: Navigator Map app: the whole field inside the device with your arrow, tap a building to preview it then Go, Jaunt routes dotted, and a legend in the Confidence view colors
state: review
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: NAV-901
parent: null
opened: 2026-10-16
closed: null
pr: 968
claimed_by: run 10/17/2026, 3:43:21 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-17T08:43:21.407Z
decision: null
decision_answer: null
---

Navigator Map app: the whole field inside the device with your arrow, tap a building to preview it then Go, Jaunt routes dotted, and a legend in the Confidence view colors.

**Navigator Mk II — NAV-901.** Filed by the owner, 2026-10-16, from his design doc "Field Navigator Mk II · Experience redesign" (Rev 1.0, base `dev` @ cc2e803): *"build all of the tickets necessary for this ... then we do all of this interface work, follow that with the balance of buildings in 1904"*. The doc is written for students aged 14–16, mostly on phones: fun and easy, never trading away honesty about sources. Full transcription, owner rulings on its open questions, the mockups (M1–M10) and the dev screenshots it cites: chicago-tickets `evidence/navigator-mk2-2026-10-16/` (`DESIGN.md`; open `original/Navigator Design Doc.dc.html` in a browser for the mockups).

## Depends on

- T-2618 (NAV-202) — do not claim this ticket until it has merged; take the next workable ticket instead.

## What to build

§07 "Map". The current whole-field map moves inside the Navigator (a scope panel). Tap a building to
preview, then Go (using the getting-there style). Jaunt routes are dotted lines. A legend toggle uses
the Confidence view colors. The round HUD instrument (NAV-302 (T-2626)) opens it.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- [ ] The map shows your position and heading live; tap a building → preview → Go travels there; the active Jaunt route is drawn.
- [ ] Works on a 390x844 phone and a 1440x900 laptop, and the 390x780 mobile smoke (the release gate) passes.
- [ ] Works in all four machine skins and with reduced motion.
- [ ] No ids, file paths or snake_case visible to a visitor (NAV-1003's lint passes once it has landed).
- [ ] Locked terms used exactly: Attested, Inferred, Reconstructed, Confidence view, Liberties, Sources, Jaunts.
- [ ] Every element id the smoke reads is preserved, or the smoke is updated in the same PR.
- [ ] A changelog.d/<ticket>.json entry says what a visitor will see, within the What's-New budget.
