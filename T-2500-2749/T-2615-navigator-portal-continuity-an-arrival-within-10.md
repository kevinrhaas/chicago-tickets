---
id: T-2615
title: Navigator portal continuity: an arrival within 10 s of the Observatory's transfer opens with the ring's tail still expanding, so the jump reads as one shot
state: open
epic: RENDERING
requested_by: owner
seen: true
effort: S
legacy_id: NAV-106
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

Navigator portal continuity: an arrival within 10 s of the Observatory's transfer opens with the ring's tail still expanding, so the jump reads as one shot.

**Navigator Mk II — NAV-106.** Filed by the owner, 2026-10-16, from his design doc "Field Navigator Mk II · Experience redesign" (Rev 1.0, base `dev` @ cc2e803): *"build all of the tickets necessary for this ... then we do all of this interface work, follow that with the balance of buildings in 1904"*. The doc is written for students aged 14–16, mostly on phones: fun and easy, never trading away honesty about sources. Full transcription, owner rulings on its open questions, the mockups (M1–M10) and the dev screenshots it cites: chicago-tickets `evidence/navigator-mk2-2026-10-16/` (`DESIGN.md`; open `original/Navigator Design Doc.dc.html` in a browser for the mockups).

## What to build

§14 "Portal continuity". `portal.js` already writes `sessionStorage['chicago4d.transfer']`. If it is
less than 10 s old, the arrival page starts with the ring's tail on screen. Reduced motion skips it.
Wrap storage access in try/catch.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- [ ] Jumping from the Observatory shows the ring's tail on the arrival page; opening the arrival URL directly (or after 10 s) does not.
- [ ] No error when sessionStorage is unavailable.
- [ ] Works on a 390x844 phone and a 1440x900 laptop, and the 390x780 mobile smoke (the release gate) passes.
- [ ] Works in all four machine skins and with reduced motion.
- [ ] No ids, file paths or snake_case visible to a visitor (NAV-1003's lint passes once it has landed).
- [ ] Locked terms used exactly: Attested, Inferred, Reconstructed, Confidence view, Liberties, Sources, Jaunts.
- [ ] Every element id the smoke reads is preserved, or the smoke is updated in the same PR.
- [ ] A changelog.d/<ticket>.json entry says what a visitor will see, within the What's-New budget.
