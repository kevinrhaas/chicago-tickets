---
id: T-2630
title: Navigator Jaunts app: Jaunts · Go to · Free roam segments, opened from the Home choices and the rail, the Welcome card's three choices kept permanently
state: review
epic: RENDERING
requested_by: owner
seen: true
effort: S
legacy_id: NAV-401
parent: null
opened: 2026-10-16
closed: null
pr: 954
claimed_by: run 10/17/2026, 2:17:34 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-17T07:17:34.274Z
decision: null
decision_answer: null
---

Navigator Jaunts app: Jaunts · Go to · Free roam segments, opened from the Home choices and the rail, the Welcome card's three choices kept permanently.

**Navigator Mk II — NAV-401.** Filed by the owner, 2026-10-16, from his design doc "Field Navigator Mk II · Experience redesign" (Rev 1.0, base `dev` @ cc2e803): *"build all of the tickets necessary for this ... then we do all of this interface work, follow that with the balance of buildings in 1904"*. The doc is written for students aged 14–16, mostly on phones: fun and easy, never trading away honesty about sources. Full transcription, owner rulings on its open questions, the mockups (M1–M10) and the dev screenshots it cites: chicago-tickets `evidence/navigator-mk2-2026-10-16/` (`DESIGN.md`; open `original/Navigator Design Doc.dc.html` in a browser for the mockups).

## Depends on

- T-2618 (NAV-202) — do not claim this ticket until it has merged; take the next workable ticket instead.

## What to build

§07 "Jaunts", M5. Segments Jaunts · Go to · Free roam. Home's three choices open the matching segment.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- [ ] The Jaunts app opens from the rail and from each Home choice on the right segment, phone and desktop.
- [ ] Works on a 390x844 phone and a 1440x900 laptop, and the 390x780 mobile smoke (the release gate) passes.
- [ ] Works in all four machine skins and with reduced motion.
- [ ] No ids, file paths or snake_case visible to a visitor (NAV-1003's lint passes once it has landed).
- [ ] Locked terms used exactly: Attested, Inferred, Reconstructed, Confidence view, Liberties, Sources, Jaunts.
- [ ] Every element id the smoke reads is preserved, or the smoke is updated in the same PR.
- [ ] A changelog.d/<ticket>.json entry says what a visitor will see, within the What's-New budget.
