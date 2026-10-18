---
id: T-2644
title: Navigator Inspect Sources tab: facts grouped by Attested, Inferred and Reconstructed with a Liberties section, human source titles, and full citations collapsed under each fact
state: review
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: NAV-508
parent: null
opened: 2026-10-16
closed: null
pr: 1021
claimed_by: run 10/18/2026, 6:13:47 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-18T11:13:47.260Z
decision: null
decision_answer: null
---

Navigator Inspect Sources tab: facts grouped by Attested, Inferred and Reconstructed with a Liberties section, human source titles, and full citations collapsed under each fact.

**Navigator Mk II — NAV-508.** Filed by the owner, 2026-10-16, from his design doc "Field Navigator Mk II · Experience redesign" (Rev 1.0, base `dev` @ cc2e803): *"build all of the tickets necessary for this ... then we do all of this interface work, follow that with the balance of buildings in 1904"*. The doc is written for students aged 14–16, mostly on phones: fun and easy, never trading away honesty about sources. Full transcription, owner rulings on its open questions, the mockups (M1–M10) and the dev screenshots it cites: chicago-tickets `evidence/navigator-mk2-2026-10-16/` (`DESIGN.md`; open `original/Navigator Design Doc.dc.html` in a browser for the mockups).

## Depends on

- T-2639 (NAV-504) — do not claim this ticket until it has merged; take the next workable ticket instead.

## What to build

§08 "Sources", §12 "Move one level down". Per-claim sources and "why" move here; Liberties per building
become a section; "Tier 1 · period/eyewitness" shows as "from the time" or "written later" (tier stays in
the data). Human source titles only; the full citation collapses under each fact. Header copy:
"64 facts. 22 Attested, 6 Inferred, 36 Reconstructed. Tap any one to see its sources."

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- [ ] Glessner's Sources tab groups every fact by grade with real counts, a Liberties section, and collapsed citations; no source id or tier label is visible.
- [ ] Works on a 390x844 phone and a 1440x900 laptop, and the 390x780 mobile smoke (the release gate) passes.
- [ ] Works in all four machine skins and with reduced motion.
- [ ] No ids, file paths or snake_case visible to a visitor (NAV-1003's lint passes once it has landed).
- [ ] Locked terms used exactly: Attested, Inferred, Reconstructed, Confidence view, Liberties, Sources, Jaunts.
- [ ] Every element id the smoke reads is preserved, or the smoke is updated in the same PR.
- [ ] A changelog.d/<ticket>.json entry says what a visitor will see, within the What's-New budget.
