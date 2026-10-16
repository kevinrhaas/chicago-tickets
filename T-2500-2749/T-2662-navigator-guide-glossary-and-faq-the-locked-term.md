---
id: T-2662
title: Navigator Guide glossary and FAQ: the locked terms with one-line meanings, 'Is this real?' and 'What does Reconstructed mean?' in 60 words or fewer each, and a locked term's first appearance on a screen showing its meaning on tap
state: open
epic: RENDERING
requested_by: owner
seen: true
effort: S
legacy_id: NAV-804
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

Navigator Guide glossary and FAQ: the locked terms with one-line meanings, 'Is this real?' and 'What does Reconstructed mean?' in 60 words or fewer each, and a locked term's first appearance on a screen showing its meaning on tap.

**Navigator Mk II — NAV-804.** Filed by the owner, 2026-10-16, from his design doc "Field Navigator Mk II · Experience redesign" (Rev 1.0, base `dev` @ cc2e803): *"build all of the tickets necessary for this ... then we do all of this interface work, follow that with the balance of buildings in 1904"*. The doc is written for students aged 14–16, mostly on phones: fun and easy, never trading away honesty about sources. Full transcription, owner rulings on its open questions, the mockups (M1–M10) and the dev screenshots it cites: chicago-tickets `evidence/navigator-mk2-2026-10-16/` (`DESIGN.md`; open `original/Navigator Design Doc.dc.html` in a browser for the mockups).

## Depends on

- T-2624 (NAV-1001) — do not claim this ticket until it has merged; take the next workable ticket instead.
- T-2661 (NAV-803) — do not claim this ticket until it has merged; take the next workable ticket instead.

## What to build

§03 "Locked terms" and NAV-804. Meanings from the string table (NAV-1001 (T-2624)).

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- [ ] The glossary lists every locked term with its meaning; both FAQ answers are 60 words or fewer; tapping a locked term's first appearance shows its meaning.
- [ ] Works on a 390x844 phone and a 1440x900 laptop, and the 390x780 mobile smoke (the release gate) passes.
- [ ] Works in all four machine skins and with reduced motion.
- [ ] No ids, file paths or snake_case visible to a visitor (NAV-1003's lint passes once it has landed).
- [ ] Locked terms used exactly: Attested, Inferred, Reconstructed, Confidence view, Liberties, Sources, Jaunts.
- [ ] Every element id the smoke reads is preserved, or the smoke is updated in the same PR.
- [ ] A changelog.d/<ticket>.json entry says what a visitor will see, within the What's-New budget.
