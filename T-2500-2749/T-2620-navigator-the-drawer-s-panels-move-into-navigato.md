---
id: T-2620
title: Navigator: the drawer's panels move into Navigator apps, goto, people, businesses, evidence and settings mounted inside apps with every element id the smoke reads intact, and the hamburger drawer retired
state: review
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: NAV-206
parent: null
opened: 2026-10-16
closed: null
pr: 942
claimed_by: run 10/17/2026, 1:54:04 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-17T06:54:04.931Z
decision: null
decision_answer: null
---

Navigator: the drawer's panels move into Navigator apps, goto, people, businesses, evidence and settings mounted inside apps with every element id the smoke reads intact, and the hamburger drawer retired.

**Navigator Mk II — NAV-206.** Filed by the owner, 2026-10-16, from his design doc "Field Navigator Mk II · Experience redesign" (Rev 1.0, base `dev` @ cc2e803): *"build all of the tickets necessary for this ... then we do all of this interface work, follow that with the balance of buildings in 1904"*. The doc is written for students aged 14–16, mostly on phones: fun and easy, never trading away honesty about sources. Full transcription, owner rulings on its open questions, the mockups (M1–M10) and the dev screenshots it cites: chicago-tickets `evidence/navigator-mk2-2026-10-16/` (`DESIGN.md`; open `original/Navigator Design Doc.dc.html` in a browser for the mockups).

## Depends on

- T-2618 (NAV-202) — do not claim this ticket until it has merged; take the next workable ticket instead.

## What to build

§14 "App registry": existing `goto.js`, `people.js`, `businesses.js`, settings and `evidence.js`
mounts become apps and keep their element ids, so the smoke gate still passes. This ticket moves
them as they are; their redesigns are their own tickets (Jaunts/Go to E4, People, Settings NAV-903 (T-2656),
Evidence → Guide NAV-1002 (T-2667)). What's new moves into Settings (its dot on the Settings icon). The eight
sideways-scrolling menu tabs (MED finding) are gone with the drawer.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- [ ] Every panel the drawer had is reachable from a rail app; the drawer and the hamburger are gone.
- [ ] Every id the smoke reads still resolves, and the smoke passes desktop and mobile.
- [ ] Works on a 390x844 phone and a 1440x900 laptop, and the 390x780 mobile smoke (the release gate) passes.
- [ ] Works in all four machine skins and with reduced motion.
- [ ] No ids, file paths or snake_case visible to a visitor (NAV-1003's lint passes once it has landed).
- [ ] Locked terms used exactly: Attested, Inferred, Reconstructed, Confidence view, Liberties, Sources, Jaunts.
- [ ] Every element id the smoke reads is preserved, or the smoke is updated in the same PR.
- [ ] A changelog.d/<ticket>.json entry says what a visitor will see, within the What's-New budget.
