---
id: T-2665
title: Navigator License keepsake: awarded on finishing the tour and shown with the Jaunt keepsakes in the Jaunts app
state: done
epic: RENDERING
requested_by: owner
seen: true
effort: XS
legacy_id: NAV-805
parent: null
opened: 2026-10-16
closed: 2026-10-18
pr: 1042
claimed_by: run 10/18/2026, 10:18:27 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-18T22:51:30Z
claimed_run: null
claimed_at: 2026-10-18T15:18:27.137Z
decision: null
decision_answer: null
---

Navigator License keepsake: awarded on finishing the tour and shown with the Jaunt keepsakes in the Jaunts app.

**Navigator Mk II — NAV-805.** Filed by the owner, 2026-10-16, from his design doc "Field Navigator Mk II · Experience redesign" (Rev 1.0, base `dev` @ cc2e803): *"build all of the tickets necessary for this ... then we do all of this interface work, follow that with the balance of buildings in 1904"*. The doc is written for students aged 14–16, mostly on phones: fun and easy, never trading away honesty about sources. Full transcription, owner rulings on its open questions, the mockups (M1–M10) and the dev screenshots it cites: chicago-tickets `evidence/navigator-mk2-2026-10-16/` (`DESIGN.md`; open `original/Navigator Design Doc.dc.html` in a browser for the mockups).

## Depends on

- T-2663 (NAV-801) — do not claim this ticket until it has merged; take the next workable ticket instead.
- T-2631 (NAV-402) — do not claim this ticket until it has merged; take the next workable ticket instead.

## What to build

NAV-805. Keepsakes live in the Jaunts app (the doc's suggestion; the owner may later give them their own
rail app).

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- [ ] Finishing the tour awards NAVIGATOR LICENSE once, and it shows in the Jaunts app's keepsakes after a reload.
- [ ] Works on a 390x844 phone and a 1440x900 laptop, and the 390x780 mobile smoke (the release gate) passes.
- [ ] Works in all four machine skins and with reduced motion.
- [ ] No ids, file paths or snake_case visible to a visitor (NAV-1003's lint passes once it has landed).
- [ ] Locked terms used exactly: Attested, Inferred, Reconstructed, Confidence view, Liberties, Sources, Jaunts.
- [ ] Every element id the smoke reads is preserved, or the smoke is updated in the same PR.
- [ ] A changelog.d/<ticket>.json entry says what a visitor will see, within the What's-New budget.
