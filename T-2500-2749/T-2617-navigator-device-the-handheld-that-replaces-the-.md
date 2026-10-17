---
id: T-2617
title: Navigator device: the handheld that replaces the drawer, a phone bottom sheet with DOCK, HALF and FULL detents, a 400 px desktop panel that collapses to its rail, the bezel and screen-code header, and the Home app
state: claimed
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: NAV-201
parent: null
opened: 2026-10-16
closed: null
pr: null
claimed_by: run 10/16/2026, 10:25:02 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-17T03:25:02.296Z
decision: null
decision_answer: null
---

Navigator device: the handheld that replaces the drawer, a phone bottom sheet with DOCK, HALF and FULL detents, a 400 px desktop panel that collapses to its rail, the bezel and screen-code header, and the Home app.

**Navigator Mk II — NAV-201.** Filed by the owner, 2026-10-16, from his design doc "Field Navigator Mk II · Experience redesign" (Rev 1.0, base `dev` @ cc2e803): *"build all of the tickets necessary for this ... then we do all of this interface work, follow that with the balance of buildings in 1904"*. The doc is written for students aged 14–16, mostly on phones: fun and easy, never trading away honesty about sources. Full transcription, owner rulings on its open questions, the mockups (M1–M10) and the dev screenshots it cites: chicago-tickets `evidence/navigator-mk2-2026-10-16/` (`DESIGN.md`; open `original/Navigator Design Doc.dc.html` in a browser for the mockups).

## Depends on

- T-2613 (NAV-104) — do not claim this ticket until it has merged; take the next workable ticket instead.

## What to build

§06 "The Navigator", M3/M4. It replaces the hamburger drawer, the Start/Jaunts chip, the Confidence
chip and caret, the pace and theme chips, and the Welcome card (those leave in NAV-206 (T-2620)/NAV-301 (T-2625)).

- Phone: bottom sheet, detents DOCK 64 px · HALF 48 % (default; the world stays visible above, you can
  keep walking) · FULL 82 % (for reading). Drag and tap; detent change 280 ms ease-detent.
- Desktop: 400 px left panel that collapses to the rail (N toggles once NAV-205 (T-2622) lands).
- Machine chrome: inset bezel, four corner screws, one signal-red key per screen; app headers read
  like a console screen ("SCR 01 · HOME", scene date on the right); scope panels (dark green CRT
  wells with 1 px scanlines) only for logs, notable facts and the mini map — reading text stays on the
  normal panel. Device label: NAVIGATOR MK II on every skin (one string).
- Home app (SCR 01): YOU ARE AT (street & cross street, facing, time, weather word), RIGHT IN FRONT
  OF YOU (building + Inspect →), JAUNT IN PROGRESS (if any), MOVE and CONFIDENCE status.
- Use the Temporal Observatory design system's tokens and readouts (YearReadout, ConfidenceGrade,
  IndicatorLamp, Telemetry, Tabs) — tokens and component CSS are in the evidence folder's
  `original/_ds/`; port them as plain CSS/ES modules (no build step). All four skins inherit it.
- Lazy and light (§14): only Home ships in the boot payload; other apps load on first open. Mind the
  performance group's boot budget.
- Accessibility: the Navigator is a non-modal region that moves focus on open.
- Mobile (390×780 smoke) is the release gate.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- [ ] Phone: the sheet moves between DOCK, HALF and FULL by drag and by tap; desktop: the 400 px panel collapses to the rail and back.
- [ ] Home shows where you are, what is in front of you and the Jaunt in progress, with real values in 1904 and 1835.
- [ ] Works in all four skins and with reduced motion; boot payload grows by no more than the Home app.
- [ ] Works on a 390x844 phone and a 1440x900 laptop, and the 390x780 mobile smoke (the release gate) passes.
- [ ] Works in all four machine skins and with reduced motion.
- [ ] No ids, file paths or snake_case visible to a visitor (NAV-1003's lint passes once it has landed).
- [ ] Locked terms used exactly: Attested, Inferred, Reconstructed, Confidence view, Liberties, Sources, Jaunts.
- [ ] Every element id the smoke reads is preserved, or the smoke is updated in the same PR.
- [ ] A changelog.d/<ticket>.json entry says what a visitor will see, within the What's-New budget.
