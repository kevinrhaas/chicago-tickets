---
id: T-2614
title: Navigator gesture gating without a gate: audio and pointer lock start on the first Home choice, canvas tap or Navigator control, desktop shows CLICK TO ENGAGE LOOK until lock, and iOS Safari logs no autoplay errors
state: open
epic: RENDERING
requested_by: owner
seen: true
effort: S
legacy_id: NAV-105
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

Navigator gesture gating without a gate: audio and pointer lock start on the first Home choice, canvas tap or Navigator control, desktop shows CLICK TO ENGAGE LOOK until lock, and iOS Safari logs no autoplay errors.

**Navigator Mk II — NAV-105.** Filed by the owner, 2026-10-16, from his design doc "Field Navigator Mk II · Experience redesign" (Rev 1.0, base `dev` @ cc2e803): *"build all of the tickets necessary for this ... then we do all of this interface work, follow that with the balance of buildings in 1904"*. The doc is written for students aged 14–16, mostly on phones: fun and easy, never trading away honesty about sources. Full transcription, owner rulings on its open questions, the mockups (M1–M10) and the dev screenshots it cites: chicago-tickets `evidence/navigator-mk2-2026-10-16/` (`DESIGN.md`; open `original/Navigator Design Doc.dc.html` in a browser for the mockups).

## Depends on

- T-2613 (NAV-104) — do not claim this ticket until it has merged; take the next workable ticket instead.

## What to build

§14 "Gesture gating without a gate". Audio resume and pointer lock need a user gesture; with the gate
gone, use the first tap on a Home choice, the canvas, or any Navigator control. Desktop shows a
`CLICK TO ENGAGE LOOK` tag until lock. iOS has no pointer lock, so only audio applies there.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- [ ] QA-04: iOS Safari, land, tap Free roam: audio context running, no console errors.
- [ ] QA-05: desktop, land, click the scene, press Esc, press N: pointer lock engages, then releases; the Navigator opens (once NAV-205 (T-2622) lands; until then Esc releases cleanly).
- [ ] The CLICK TO ENGAGE LOOK tag shows only on pointer-lock devices and only until lock.
- [ ] Works on a 390x844 phone and a 1440x900 laptop, and the 390x780 mobile smoke (the release gate) passes.
- [ ] Works in all four machine skins and with reduced motion.
- [ ] No ids, file paths or snake_case visible to a visitor (NAV-1003's lint passes once it has landed).
- [ ] Locked terms used exactly: Attested, Inferred, Reconstructed, Confidence view, Liberties, Sources, Jaunts.
- [ ] Every element id the smoke reads is preserved, or the smoke is updated in the same PR.
- [ ] A changelog.d/<ticket>.json entry says what a visitor will see, within the What's-New budget.
