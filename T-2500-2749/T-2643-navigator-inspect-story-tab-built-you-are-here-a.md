---
id: T-2643
title: Navigator Inspect Story tab: BUILT, YOU ARE HERE and TODAY on a timeline from design to today, filtered by the scene's era
state: claimed
epic: RENDERING
requested_by: owner
seen: true
effort: S
legacy_id: NAV-507
parent: null
opened: 2026-10-16
closed: null
pr: null
claimed_by: run 10/18/2026, 6:13:47 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-18T11:13:47.986Z
decision: null
decision_answer: null
---

Navigator Inspect Story tab: BUILT, YOU ARE HERE and TODAY on a timeline from design to today, filtered by the scene's era.

**Navigator Mk II — NAV-507.** Filed by the owner, 2026-10-16, from his design doc "Field Navigator Mk II · Experience redesign" (Rev 1.0, base `dev` @ cc2e803): *"build all of the tickets necessary for this ... then we do all of this interface work, follow that with the balance of buildings in 1904"*. The doc is written for students aged 14–16, mostly on phones: fun and easy, never trading away honesty about sources. Full transcription, owner rulings on its open questions, the mockups (M1–M10) and the dev screenshots it cites: chicago-tickets `evidence/navigator-mk2-2026-10-16/` (`DESIGN.md`; open `original/Navigator Design Doc.dc.html` in a browser for the mockups).

## Depends on

- T-2639 (NAV-504) — do not claim this ticket until it has merged; take the next workable ticket instead.

## What to build

§08 "Story" and §12. Modeled phase dates move here ("Stood here"); Present status becomes "Today".
Content tagged with another scene's era never renders (the filter NAV-509 (T-2609) put on the card).
Post-scene facts (Today, the museum) are labelled as after your visit.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- [ ] Glessner's Story tab runs from design to today with YOU ARE HERE at 1904; no 1835 civic rule renders on any 1904 building (QA-09).
- [ ] Works on a 390x844 phone and a 1440x900 laptop, and the 390x780 mobile smoke (the release gate) passes.
- [ ] Works in all four machine skins and with reduced motion.
- [ ] No ids, file paths or snake_case visible to a visitor (NAV-1003's lint passes once it has landed).
- [ ] Locked terms used exactly: Attested, Inferred, Reconstructed, Confidence view, Liberties, Sources, Jaunts.
- [ ] Every element id the smoke reads is preserved, or the smoke is updated in the same PR.
- [ ] A changelog.d/<ticket>.json entry says what a visitor will see, within the What's-New budget.
