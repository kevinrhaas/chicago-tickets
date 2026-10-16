---
id: T-2656
title: Navigator Settings app: Display (brightness, field of view, road visibility, labels, light/dark, text size 100-140 %), the machine skins as preview tiles, Performance with Auto, Sound, Units, and About & What's new
state: open
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: NAV-903
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

Navigator Settings app: Display (brightness, field of view, road visibility, labels, light/dark, text size 100-140 %), the machine skins as preview tiles, Performance with Auto, Sound, Units, and About & What's new.

**Navigator Mk II — NAV-903.** Filed by the owner, 2026-10-16, from his design doc "Field Navigator Mk II · Experience redesign" (Rev 1.0, base `dev` @ cc2e803): *"build all of the tickets necessary for this ... then we do all of this interface work, follow that with the balance of buildings in 1904"*. The doc is written for students aged 14–16, mostly on phones: fun and easy, never trading away honesty about sources. Full transcription, owner rulings on its open questions, the mockups (M1–M10) and the dev screenshots it cites: chicago-tickets `evidence/navigator-mk2-2026-10-16/` (`DESIGN.md`; open `original/Navigator Design Doc.dc.html` in a browser for the mockups).

## Depends on

- T-2620 (NAV-206) — do not claim this ticket until it has merged; take the next workable ticket instead.

## What to build

§07 "Settings" and §13 type rules. Reading text is Barlow, 16 px minimum on phones (up from 14), never
mono; lines ≤ 65 characters; contrast ≥ 4.5:1 on every panel. Text size scales all reading text 100–140 %
and reflows. Performance: detail, sharpness, frame pacing with an "Auto" recommendation (the device
profile already exists). About holds the build stamp (dev) and What's new.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- [ ] QA-18: text size 140 % reflows every app with no clipped text.
- [ ] QA-21: every app legible at 4.5:1 or better in all four skins.
- [ ] Light/dark lives here and no longer in the HUD.
- [ ] Works on a 390x844 phone and a 1440x900 laptop, and the 390x780 mobile smoke (the release gate) passes.
- [ ] Works in all four machine skins and with reduced motion.
- [ ] No ids, file paths or snake_case visible to a visitor (NAV-1003's lint passes once it has landed).
- [ ] Locked terms used exactly: Attested, Inferred, Reconstructed, Confidence view, Liberties, Sources, Jaunts.
- [ ] Every element id the smoke reads is preserved, or the smoke is updated in the same PR.
- [ ] A changelog.d/<ticket>.json entry says what a visitor will see, within the What's-New budget.
