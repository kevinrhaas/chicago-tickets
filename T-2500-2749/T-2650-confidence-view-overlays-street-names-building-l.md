---
id: T-2650
title: Confidence view overlays: street names, building labels, people pins and the Jaunt route, each with its own toggle at the foot of the app
state: review
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: NAV-605
parent: null
opened: 2026-10-16
closed: null
pr: 1050
claimed_by: run 10/18/2026, 4:10:47 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-18T21:10:47.838Z
decision: null
decision_answer: null
---

Confidence view overlays: street names, building labels, people pins and the Jaunt route, each with its own toggle at the foot of the app.

**Navigator Mk II — NAV-605.** Filed by the owner, 2026-10-16, from his design doc "Field Navigator Mk II · Experience redesign" (Rev 1.0, base `dev` @ cc2e803): *"build all of the tickets necessary for this ... then we do all of this interface work, follow that with the balance of buildings in 1904"*. The doc is written for students aged 14–16, mostly on phones: fun and easy, never trading away honesty about sources. Full transcription, owner rulings on its open questions, the mockups (M1–M10) and the dev screenshots it cites: chicago-tickets `evidence/navigator-mk2-2026-10-16/` (`DESIGN.md`; open `original/Navigator Design Doc.dc.html` in a browser for the mockups).

## Depends on

- T-2647 (NAV-601) — do not claim this ticket until it has merged; take the next workable ticket instead.

## What to build

§09 "Overlays". People pins are plain markers on a record's place; a pin opens that person's card, with any
`review_required` note it carries.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- [ ] Each overlay toggles independently in 1835 and 1904 and costs no measurable frame time when off.
- [ ] Works on a 390x844 phone and a 1440x900 laptop, and the 390x780 mobile smoke (the release gate) passes.
- [ ] Works in all four machine skins and with reduced motion.
- [ ] No ids, file paths or snake_case visible to a visitor (NAV-1003's lint passes once it has landed).
- [ ] Locked terms used exactly: Attested, Inferred, Reconstructed, Confidence view, Liberties, Sources, Jaunts.
- [ ] Every element id the smoke reads is preserved, or the smoke is updated in the same PR.
- [ ] A changelog.d/<ticket>.json entry says what a visitor will see, within the What's-New budget.
