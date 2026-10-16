---
id: T-2636
title: Building fallback summary: a building with no summary record gets one templated from its sidecar, never raw fields, never ids, paths or snake_case
state: claimed
epic: RENDERING
requested_by: owner
seen: true
effort: S
legacy_id: NAV-503
parent: null
opened: 2026-10-16
closed: null
pr: null
claimed_by: run 10/16/2026, 4:42:14 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-16T21:42:14.765Z
decision: null
decision_answer: null
---

Building fallback summary: a building with no summary record gets one templated from its sidecar, never raw fields, never ids, paths or snake_case.

**Navigator Mk II — NAV-503.** Filed by the owner, 2026-10-16, from his design doc "Field Navigator Mk II · Experience redesign" (Rev 1.0, base `dev` @ cc2e803): *"build all of the tickets necessary for this ... then we do all of this interface work, follow that with the balance of buildings in 1904"*. The doc is written for students aged 14–16, mostly on phones: fun and easy, never trading away honesty about sources. Full transcription, owner rulings on its open questions, the mockups (M1–M10) and the dev screenshots it cites: chicago-tickets `evidence/navigator-mk2-2026-10-16/` (`DESIGN.md`; open `original/Navigator Design Doc.dc.html` in a browser for the mockups).

## Depends on

- T-2635 (NAV-502) — do not claim this ticket until it has merged; take the next workable ticket instead.

## What to build

§12: structures without a record get a generated fallback built from the sidecar using templates,
never raw fields. Fixes the card opening with "(data/street_grid/1904.json)" and "parcel prairie_1800"
and the address three times (HIGH finding, `IMG_6942`).

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- [ ] QA-08: inspect a building with no summary file; the fallback renders with no ids, paths or snake_case, and gives the address once.
- [ ] A test runs the template over every 1904 and 1835 structure and finds no id, path or snake_case in the output.
- [ ] Works on a 390x844 phone and a 1440x900 laptop, and the 390x780 mobile smoke (the release gate) passes.
- [ ] Works in all four machine skins and with reduced motion.
- [ ] No ids, file paths or snake_case visible to a visitor (NAV-1003's lint passes once it has landed).
- [ ] Locked terms used exactly: Attested, Inferred, Reconstructed, Confidence view, Liberties, Sources, Jaunts.
- [ ] Every element id the smoke reads is preserved, or the smoke is updated in the same PR.
- [ ] A changelog.d/<ticket>.json entry says what a visitor will see, within the What's-New budget.
