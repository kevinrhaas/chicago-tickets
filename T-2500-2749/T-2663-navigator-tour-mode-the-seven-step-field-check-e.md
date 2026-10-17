---
id: T-2663
title: Navigator Tour mode: the seven-step Field Check, each step completing on the real action, a spotlight cut-out with 55 % dim, Skip always visible, resume after reload and replay from Guide
state: claimed
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: NAV-801
parent: null
opened: 2026-10-16
closed: null
pr: null
claimed_by: run 10/17/2026, 5:52:37 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-17T10:52:37.756Z
decision: null
decision_answer: null
---

Navigator Tour mode: the seven-step Field Check, each step completing on the real action, a spotlight cut-out with 55 % dim, Skip always visible, resume after reload and replay from Guide.

**Navigator Mk II — NAV-801.** Filed by the owner, 2026-10-16, from his design doc "Field Navigator Mk II · Experience redesign" (Rev 1.0, base `dev` @ cc2e803): *"build all of the tickets necessary for this ... then we do all of this interface work, follow that with the balance of buildings in 1904"*. The doc is written for students aged 14–16, mostly on phones: fun and easy, never trading away honesty about sources. Full transcription, owner rulings on its open questions, the mockups (M1–M10) and the dev screenshots it cites: chicago-tickets `evidence/navigator-mk2-2026-10-16/` (`DESIGN.md`; open `original/Navigator Design Doc.dc.html` in a browser for the mockups).

## Depends on

- T-2618 (NAV-202) — do not claim this ticket until it has merged; take the next workable ticket instead.
- T-2638 (NAV-501) — do not claim this ticket until it has merged; take the next workable ticket instead.
- T-2647 (NAV-601) — do not claim this ticket until it has merged; take the next workable ticket instead.

## What to build

§11, M10. Framed as a Confluence Laboratory field check. Bubbles ≤ 14 words.

| # | Bubble | Completes when |
|---|---|---|
| 01 | This is your Navigator. Everything you need lives here. | dock highlighted, tap Next |
| 02 | Look around. Drag the right side of the screen (or move the mouse). | camera yaw changes ≥ 60° |
| 03 | Walk. Left thumb, or W A S D. Head for the corner. | moved ≥ 5 m |
| 04 | Tap the Glessner House. Every building has a file. | Inspect opens on any structure |
| 05 | Front page first. Tabs go deeper. Try Design. | any tab other than Overview opened |
| 06 | How sure are we? Turn on the Confidence view. | a preset other than Normal chosen |
| 07 | Ready. Take a Jaunt, or Jump to another year. | tap Finish (awards the keepsake, NAV-805 (T-2665)) |

Step 4 names the building in front of you in 1835 and 1812. Progress persists (try/catch storage).

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- [ ] QA-16: run the tour, reload at step 4, skip at 6; it resumes at 4, Skip ends cleanly, Replay is in Guide.
- [ ] Each step completes only on its real action, by touch and by keyboard (second half of QA-19).
- [ ] Works on a 390x844 phone and a 1440x900 laptop, and the 390x780 mobile smoke (the release gate) passes.
- [ ] Works in all four machine skins and with reduced motion.
- [ ] No ids, file paths or snake_case visible to a visitor (NAV-1003's lint passes once it has landed).
- [ ] Locked terms used exactly: Attested, Inferred, Reconstructed, Confidence view, Liberties, Sources, Jaunts.
- [ ] Every element id the smoke reads is preserved, or the smoke is updated in the same PR.
- [ ] A changelog.d/<ticket>.json entry says what a visitor will see, within the What's-New budget.
