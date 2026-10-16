---
id: T-2667
title: Evidence hub becomes Guide › About this destination: ten topics folded into four cards, How we grade, Sources, Liberties and What lived and grew here, with the order book behind Researcher mode
state: open
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: NAV-1002
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

Evidence hub becomes Guide › About this destination: ten topics folded into four cards, How we grade, Sources, Liberties and What lived and grew here, with the order book behind Researcher mode.

**Navigator Mk II — NAV-1002.** Filed by the owner, 2026-10-16, from his design doc "Field Navigator Mk II · Experience redesign" (Rev 1.0, base `dev` @ cc2e803): *"build all of the tickets necessary for this ... then we do all of this interface work, follow that with the balance of buildings in 1904"*. The doc is written for students aged 14–16, mostly on phones: fun and easy, never trading away honesty about sources. Full transcription, owner rulings on its open questions, the mockups (M1–M10) and the dev screenshots it cites: chicago-tickets `evidence/navigator-mk2-2026-10-16/` (`DESIGN.md`; open `original/Navigator Design Doc.dc.html` in a browser for the mockups).

## Depends on

- T-2657 (NAV-S03) — do not claim this ticket until it has merged; take the next workable ticket instead.
- T-2662 (NAV-804) — do not claim this ticket until it has merged; take the next workable ticket instead.

## What to build

§12 and NAV-1002. The Evidence hub's ten topics (some in internal language: "order book", "the tickets
that owe it", "commit gate" — MED finding) become four cards. City numbers, fauna, plants, exclusions
and open questions move under About this destination. The order book shows only in Researcher mode
(owner ruling 2026-10-16, replacing the doc's /research page).

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- [ ] Guide › About this destination shows the four cards in 1835 and 1904; no internal term is visible with Researcher mode off; the order book appears with it on.
- [ ] Works on a 390x844 phone and a 1440x900 laptop, and the 390x780 mobile smoke (the release gate) passes.
- [ ] Works in all four machine skins and with reduced motion.
- [ ] No ids, file paths or snake_case visible to a visitor (NAV-1003's lint passes once it has landed).
- [ ] Locked terms used exactly: Attested, Inferred, Reconstructed, Confidence view, Liberties, Sources, Jaunts.
- [ ] Every element id the smoke reads is preserved, or the smoke is updated in the same PR.
- [ ] A changelog.d/<ticket>.json entry says what a visitor will see, within the What's-New budget.
