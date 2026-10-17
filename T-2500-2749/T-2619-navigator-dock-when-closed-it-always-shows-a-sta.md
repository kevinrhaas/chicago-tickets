---
id: T-2619
title: Navigator dock: when closed it always shows a status lamp, the NAVIGATOR label, the year and the current app's icon, and one tap or swipe up opens the last app at HALF
state: claimed
epic: RENDERING
requested_by: owner
seen: true
effort: S
legacy_id: NAV-203
parent: null
opened: 2026-10-16
closed: null
pr: null
claimed_by: run 10/17/2026, 1:41:16 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-17T06:41:16.248Z
decision: null
decision_answer: null
---

Navigator dock: when closed it always shows a status lamp, the NAVIGATOR label, the year and the current app's icon, and one tap or swipe up opens the last app at HALF.

**Navigator Mk II — NAV-203.** Filed by the owner, 2026-10-16, from his design doc "Field Navigator Mk II · Experience redesign" (Rev 1.0, base `dev` @ cc2e803): *"build all of the tickets necessary for this ... then we do all of this interface work, follow that with the balance of buildings in 1904"*. The doc is written for students aged 14–16, mostly on phones: fun and easy, never trading away honesty about sources. Full transcription, owner rulings on its open questions, the mockups (M1–M10) and the dev screenshots it cites: chicago-tickets `evidence/navigator-mk2-2026-10-16/` (`DESIGN.md`; open `original/Navigator Design Doc.dc.html` in a browser for the mockups).

## Depends on

- T-2617 (NAV-201) — do not claim this ticket until it has merged; take the next workable ticket instead.

## What to build

§06 "DOCK · 64 px" and NAV-203. Bottom centre on phones (respecting safe areas), the rail on desktop.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- [ ] Closed state always visible on phone and desktop; one tap opens the last-used app at HALF.
- [ ] Swipe up from the dock opens it; the dock never overlaps the joystick area on a 390×844 phone.
- [ ] Works on a 390x844 phone and a 1440x900 laptop, and the 390x780 mobile smoke (the release gate) passes.
- [ ] Works in all four machine skins and with reduced motion.
- [ ] No ids, file paths or snake_case visible to a visitor (NAV-1003's lint passes once it has landed).
- [ ] Locked terms used exactly: Attested, Inferred, Reconstructed, Confidence view, Liberties, Sources, Jaunts.
- [ ] Every element id the smoke reads is preserved, or the smoke is updated in the same PR.
- [ ] A changelog.d/<ticket>.json entry says what a visitor will see, within the What's-New budget.
