---
id: T-2629
title: Dev chrome off the phone screen: the DEV pill and build stamp move to Settings › About on phones
state: claimed
epic: RENDERING
requested_by: owner
seen: true
effort: XS
legacy_id: NAV-305
parent: null
opened: 2026-10-16
closed: null
pr: null
claimed_by: run 10/18/2026, 4:14:35 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-18T09:14:35.526Z
decision: null
decision_answer: null
---

Dev chrome off the phone screen: the DEV pill and build stamp move to Settings › About on phones.

**Navigator Mk II — NAV-305.** Filed by the owner, 2026-10-16, from his design doc "Field Navigator Mk II · Experience redesign" (Rev 1.0, base `dev` @ cc2e803): *"build all of the tickets necessary for this ... then we do all of this interface work, follow that with the balance of buildings in 1904"*. The doc is written for students aged 14–16, mostly on phones: fun and easy, never trading away honesty about sources. Full transcription, owner rulings on its open questions, the mockups (M1–M10) and the dev screenshots it cites: chicago-tickets `evidence/navigator-mk2-2026-10-16/` (`DESIGN.md`; open `original/Navigator Design Doc.dc.html` in a browser for the mockups).

## Depends on

- T-2620 (NAV-206) — do not claim this ticket until it has merged; take the next workable ticket instead.

## What to build

§01 LOW finding: the DEV pill and build stamp overlap the device on phones (`#gate-build`). On phones
they live in Settings › About (dev builds only); desktop may keep a small stamp.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- [ ] At 390x844 no DEV pill or build stamp overlaps the HUD or Navigator; Settings › About shows both on dev builds.
- [ ] Works on a 390x844 phone and a 1440x900 laptop, and the 390x780 mobile smoke (the release gate) passes.
- [ ] Works in all four machine skins and with reduced motion.
- [ ] No ids, file paths or snake_case visible to a visitor (NAV-1003's lint passes once it has landed).
- [ ] Locked terms used exactly: Attested, Inferred, Reconstructed, Confidence view, Liberties, Sources, Jaunts.
- [ ] Every element id the smoke reads is preserved, or the smoke is updated in the same PR.
- [ ] A changelog.d/<ticket>.json entry says what a visitor will see, within the What's-New budget.
