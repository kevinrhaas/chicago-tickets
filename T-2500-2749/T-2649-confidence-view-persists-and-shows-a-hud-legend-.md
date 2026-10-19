---
id: T-2649
title: Confidence view persists and shows a HUD legend: choices saved to localStorage chicago4d.confidence and carried across destinations, and a legend chip under the year chip while the view is on
state: review
epic: RENDERING
requested_by: owner
seen: true
effort: S
legacy_id: NAV-604
parent: null
opened: 2026-10-16
closed: null
pr: 1061
claimed_by: run 10/18/2026, 3:44:11 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-18T20:44:11.412Z
decision: null
decision_answer: null
---

Confidence view persists and shows a HUD legend: choices saved to localStorage chicago4d.confidence and carried across destinations, and a legend chip under the year chip while the view is on.

**Navigator Mk II — NAV-604.** Filed by the owner, 2026-10-16, from his design doc "Field Navigator Mk II · Experience redesign" (Rev 1.0, base `dev` @ cc2e803): *"build all of the tickets necessary for this ... then we do all of this interface work, follow that with the balance of buildings in 1904"*. The doc is written for students aged 14–16, mostly on phones: fun and easy, never trading away honesty about sources. Full transcription, owner rulings on its open questions, the mockups (M1–M10) and the dev screenshots it cites: chicago-tickets `evidence/navigator-mk2-2026-10-16/` (`DESIGN.md`; open `original/Navigator Design Doc.dc.html` in a browser for the mockups).

## Depends on

- T-2647 (NAV-601) — do not claim this ticket until it has merged; take the next workable ticket instead.

## What to build

§09. Stored at `localStorage['chicago4d.confidence']` (try/catch; renders correctly without storage).
While the view is on, a small legend chip sits under the year chip; tapping it opens the app.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- [ ] QA-11: hide Reconstructed, set Attested opacity to 30 %, reload; both persist, and carry into another destination.
- [ ] The legend chip shows only while the view is not NORMAL.
- [ ] Works on a 390x844 phone and a 1440x900 laptop, and the 390x780 mobile smoke (the release gate) passes.
- [ ] Works in all four machine skins and with reduced motion.
- [ ] No ids, file paths or snake_case visible to a visitor (NAV-1003's lint passes once it has landed).
- [ ] Locked terms used exactly: Attested, Inferred, Reconstructed, Confidence view, Liberties, Sources, Jaunts.
- [ ] Every element id the smoke reads is preserved, or the smoke is updated in the same PR.
- [ ] A changelog.d/<ticket>.json entry says what a visitor will see, within the What's-New budget.

## Owner's ruling (2026-10-18): the Confidence legend chip is not counted
T-2649's legend chip (#conf-legend, 81x22 px under the year chip) shows only while the visitor
has the Confidence view on. With it on, the phone HUD measured 10.46 % of 390x780 (9.81 %
without it). Ruling: "Don't count it." Like T-2741's street readout, the 10 % budget is measured
without it, and its share is reported.
