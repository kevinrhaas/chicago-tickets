---
id: T-2645
title: Navigator Inspect Photos tab: images sorted by date with year, caption and 'from this spot', the 12 best first and the rest behind 'All N'
state: review
epic: RENDERING
requested_by: owner
seen: true
effort: S
legacy_id: NAV-510
parent: null
opened: 2026-10-16
closed: null
pr: 1027
claimed_by: run 10/18/2026, 7:57:41 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-18T12:57:41.405Z
decision: null
decision_answer: null
---

Navigator Inspect Photos tab: images sorted by date with year, caption and 'from this spot', the 12 best first and the rest behind 'All N'.

**Navigator Mk II — NAV-510.** Filed by the owner, 2026-10-16, from his design doc "Field Navigator Mk II · Experience redesign" (Rev 1.0, base `dev` @ cc2e803): *"build all of the tickets necessary for this ... then we do all of this interface work, follow that with the balance of buildings in 1904"*. The doc is written for students aged 14–16, mostly on phones: fun and easy, never trading away honesty about sources. Full transcription, owner rulings on its open questions, the mockups (M1–M10) and the dev screenshots it cites: chicago-tickets `evidence/navigator-mk2-2026-10-16/` (`DESIGN.md`; open `original/Navigator Design Doc.dc.html` in a browser for the mockups).

## Depends on

- T-2639 (NAV-504) — do not claim this ticket until it has merged; take the next workable ticket instead.

## What to build

§08 "Photos". Builds on the card's Images tab (T-2389, `tools/compile_pictures.py`, credits kept).
"From this spot" moves the camera to the solved camera in `data/reference_views/<id>/` where one exists
(hide it otherwise). Glessner has about 162 images: group them and show the 12 best first.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- [ ] Glessner's Photos tab shows 12 images first, sorted by date with year, caption and credit, and 'All N' reveals the rest.
- [ ] 'From this spot' appears only for images with a solved camera and moves the view there.
- [ ] Works on a 390x844 phone and a 1440x900 laptop, and the 390x780 mobile smoke (the release gate) passes.
- [ ] Works in all four machine skins and with reduced motion.
- [ ] No ids, file paths or snake_case visible to a visitor (NAV-1003's lint passes once it has landed).
- [ ] Locked terms used exactly: Attested, Inferred, Reconstructed, Confidence view, Liberties, Sources, Jaunts.
- [ ] Every element id the smoke reads is preserved, or the smoke is updated in the same PR.
- [ ] A changelog.d/<ticket>.json entry says what a visitor will see, within the What's-New budget.
