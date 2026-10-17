---
id: T-2621
title: Navigator deep links and back: ?nav=app[:id]&tab= opens that app after landing, and the browser back button closes the current app before leaving the page
state: claimed
epic: RENDERING
requested_by: owner
seen: true
effort: S
legacy_id: NAV-204
parent: null
opened: 2026-10-16
closed: null
pr: null
claimed_by: run 10/17/2026, 1:53:57 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-17T06:53:57.705Z
decision: null
decision_answer: null
---

Navigator deep links and back: ?nav=app[:id]&tab= opens that app after landing, and the browser back button closes the current app before leaving the page.

**Navigator Mk II — NAV-204.** Filed by the owner, 2026-10-16, from his design doc "Field Navigator Mk II · Experience redesign" (Rev 1.0, base `dev` @ cc2e803): *"build all of the tickets necessary for this ... then we do all of this interface work, follow that with the balance of buildings in 1904"*. The doc is written for students aged 14–16, mostly on phones: fun and easy, never trading away honesty about sources. Full transcription, owner rulings on its open questions, the mockups (M1–M10) and the dev screenshots it cites: chicago-tickets `evidence/navigator-mk2-2026-10-16/` (`DESIGN.md`; open `original/Navigator Design Doc.dc.html` in a browser for the mockups).

## Depends on

- T-2618 (NAV-202) — do not claim this ticket until it has merged; take the next workable ticket instead.

## What to build

§14 "Deep links". `/1904/?nav=inspect:glessner_house&tab=design` opens after landing. Teachers can share
any screen. Back closes the current app first. Unknown apps or ids are ignored quietly.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- [ ] ?nav=jaunts and ?nav=map open their apps after landing; QA-15 (inspect:glessner_house&tab=design) passes once NAV-501 (T-2638)/504 land, and this ticket ships the routing for it.
- [ ] With an app open, browser Back closes it and stays on the page; a second Back leaves.
- [ ] Works on a 390x844 phone and a 1440x900 laptop, and the 390x780 mobile smoke (the release gate) passes.
- [ ] Works in all four machine skins and with reduced motion.
- [ ] No ids, file paths or snake_case visible to a visitor (NAV-1003's lint passes once it has landed).
- [ ] Locked terms used exactly: Attested, Inferred, Reconstructed, Confidence view, Liberties, Sources, Jaunts.
- [ ] Every element id the smoke reads is preserved, or the smoke is updated in the same PR.
- [ ] A changelog.d/<ticket>.json entry says what a visitor will see, within the What's-New budget.
