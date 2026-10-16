---
id: T-2670
title: Student playtest: 6-8 students, three tasks (find a house, learn who lived there, tell Attested from Reconstructed), 80 % or more succeeding unaided
state: blocked-owner
epic: META
requested_by: owner
seen: true
effort: S
legacy_id: NAV-1006
parent: null
opened: 2026-10-16
closed: null
pr: null
claimed_by: null
blocked_on: needs the owner to arrange 6-8 students aged 14-16; a run can prepare the task cards and observer sheet once T-2663 (tour) and T-2637 (Glessner pilot) have merged
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: null
decision: null
decision_answer: null
---

Student playtest: 6-8 students, three tasks (find a house, learn who lived there, tell Attested from Reconstructed), 80 % or more succeeding unaided.

**Navigator Mk II — NAV-1006.** Filed by the owner, 2026-10-16, from his design doc "Field Navigator Mk II · Experience redesign" (Rev 1.0, base `dev` @ cc2e803): *"build all of the tickets necessary for this ... then we do all of this interface work, follow that with the balance of buildings in 1904"*. The doc is written for students aged 14–16, mostly on phones: fun and easy, never trading away honesty about sources. Full transcription, owner rulings on its open questions, the mockups (M1–M10) and the dev screenshots it cites: chicago-tickets `evidence/navigator-mk2-2026-10-16/` (`DESIGN.md`; open `original/Navigator Design Doc.dc.html` in a browser for the mockups).

## Depends on

- T-2663 (NAV-801) — do not claim this ticket until it has merged; take the next workable ticket instead.
- T-2637 (NAV-1005) — do not claim this ticket until it has merged; take the next workable ticket instead.

## What to build

NAV-1006. Needs real students, which only the owner can arrange. A run can prepare the kit (three task
cards, an observer sheet, the Field log readout NAV-S02 (T-2660)) once the tour and the Glessner pilot ship.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- [ ] 6-8 students attempt the three tasks; 80 % or more succeed unaided; findings filed against the tickets they concern.
- [ ] Works on a 390x844 phone and a 1440x900 laptop, and the 390x780 mobile smoke (the release gate) passes.
- [ ] Works in all four machine skins and with reduced motion.
- [ ] No ids, file paths or snake_case visible to a visitor (NAV-1003's lint passes once it has landed).
- [ ] Locked terms used exactly: Attested, Inferred, Reconstructed, Confidence view, Liberties, Sources, Jaunts.
- [ ] Every element id the smoke reads is preserved, or the smoke is updated in the same PR.
- [ ] A changelog.d/<ticket>.json entry says what a visitor will see, within the What's-New budget.
