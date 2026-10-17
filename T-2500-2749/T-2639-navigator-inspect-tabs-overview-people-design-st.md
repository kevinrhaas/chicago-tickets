---
id: T-2639
title: Navigator Inspect tabs: Overview · People · Design · Story · Photos · Sources, a new building always opening on Overview, and the People tab listing who lived, worked or visited in the scene year, then before and after
state: review
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: NAV-504
parent: null
opened: 2026-10-16
closed: null
pr: 977
claimed_by: run 10/17/2026, 5:53:46 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-17T10:53:46.361Z
decision: null
decision_answer: null
---

Navigator Inspect tabs: Overview · People · Design · Story · Photos · Sources, a new building always opening on Overview, and the People tab listing who lived, worked or visited in the scene year, then before and after.

**Navigator Mk II — NAV-504.** Filed by the owner, 2026-10-16, from his design doc "Field Navigator Mk II · Experience redesign" (Rev 1.0, base `dev` @ cc2e803): *"build all of the tickets necessary for this ... then we do all of this interface work, follow that with the balance of buildings in 1904"*. The doc is written for students aged 14–16, mostly on phones: fun and easy, never trading away honesty about sources. Full transcription, owner rulings on its open questions, the mockups (M1–M10) and the dev screenshots it cites: chicago-tickets `evidence/navigator-mk2-2026-10-16/` (`DESIGN.md`; open `original/Navigator Design Doc.dc.html` in a browser for the mockups).

## Depends on

- T-2638 (NAV-501) — do not claim this ticket until it has merged; take the next workable ticket instead.

## What to build

§08 "Tabs". Overview · People · Design · Story · Photos · Sources. A new building always opens on
Overview; the same building keeps its tab. People: residents, staff and visitors in the scene year,
then before and after; each person links to the People app. Records flagged `review_required` show
their note exactly as their cards do.
Design, Story, Photos and Sources fill in NAV-506a/507/510/508 — ship them here as tabs over the
existing card content.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- [ ] All six tabs open on phone and desktop; a newly inspected building opens on Overview.
- [ ] The People tab lists the Glessner household in 1904 and a household's people in 1835, with review notes where flagged.
- [ ] Works on a 390x844 phone and a 1440x900 laptop, and the 390x780 mobile smoke (the release gate) passes.
- [ ] Works in all four machine skins and with reduced motion.
- [ ] No ids, file paths or snake_case visible to a visitor (NAV-1003's lint passes once it has landed).
- [ ] Locked terms used exactly: Attested, Inferred, Reconstructed, Confidence view, Liberties, Sources, Jaunts.
- [ ] Every element id the smoke reads is preserved, or the smoke is updated in the same PR.
- [ ] A changelog.d/<ticket>.json entry says what a visitor will see, within the What's-New budget.
