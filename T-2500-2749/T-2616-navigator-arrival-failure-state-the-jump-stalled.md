---
id: T-2616
title: Navigator arrival failure state: 'The jump stalled somewhere around 1950.' with TRY AGAIN and BACK TO THE OBSERVATORY, and the error detail collapsed under 'Details for your teacher'
state: review
epic: RENDERING
requested_by: owner
seen: true
effort: S
legacy_id: NAV-107
parent: null
opened: 2026-10-16
closed: null
pr: 902
claimed_by: run 10/16/2026, 2:37:35 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-16T19:37:35.205Z
decision: null
decision_answer: null
---

Navigator arrival failure state: 'The jump stalled somewhere around 1950.' with TRY AGAIN and BACK TO THE OBSERVATORY, and the error detail collapsed under 'Details for your teacher'.

**Navigator Mk II — NAV-107.** Filed by the owner, 2026-10-16, from his design doc "Field Navigator Mk II · Experience redesign" (Rev 1.0, base `dev` @ cc2e803): *"build all of the tickets necessary for this ... then we do all of this interface work, follow that with the balance of buildings in 1904"*. The doc is written for students aged 14–16, mostly on phones: fun and easy, never trading away honesty about sources. Full transcription, owner rulings on its open questions, the mockups (M1–M10) and the dev screenshots it cites: chicago-tickets `evidence/navigator-mk2-2026-10-16/` (`DESIGN.md`; open `original/Navigator Design Doc.dc.html` in a browser for the mockups).

## What to build

§05 "Failure state". The year in the message is the ticker year at the stall. The technical detail
(what failed to load) sits in a collapsed "Details for your teacher" section. TRY AGAIN reloads the
destination; BACK TO THE OBSERVATORY returns to the portal.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- [x] Forcing a boot failure (blocked scene file) shows the stalled message with the ticker's year, both buttons work, and the detail is collapsed by default.
- [x] No raw stack trace or file path outside the collapsed details.
- [ ] Works on a 390x844 phone and a 1440x900 laptop, and the 390x780 mobile smoke (the release gate) passes.
- [x] Works in all four machine skins and with reduced motion.
- [x] No ids, file paths or snake_case visible to a visitor (NAV-1003's lint passes once it has landed).
- [x] Locked terms used exactly: Attested, Inferred, Reconstructed, Confidence view, Liberties, Sources, Jaunts.
- [x] Every element id the smoke reads is preserved, or the smoke is updated in the same PR.
- [x] A changelog.d/<ticket>.json entry says what a visitor will see, within the What's-New budget.
