---
id: T-2659
title: Navigator sound, on by default: the ticker's flap ticks capped at 12 a second, the landing clunk, relay clicks and a hum while the Navigator is open, per-destination ambience, and Settings › Sound with master, effects and ambience
state: review
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: NAV-S01
parent: null
opened: 2026-10-16
closed: null
pr: 1062
claimed_by: run 10/18/2026, 6:04:42 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-18T23:04:42.661Z
decision: null
decision_answer: null
---

Navigator sound, on by default: the ticker's flap ticks capped at 12 a second, the landing clunk, relay clicks and a hum while the Navigator is open, per-destination ambience, and Settings › Sound with master, effects and ambience.

**Navigator Mk II — NAV-S01.** Filed by the owner, 2026-10-16, from his design doc "Field Navigator Mk II · Experience redesign" (Rev 1.0, base `dev` @ cc2e803): *"build all of the tickets necessary for this ... then we do all of this interface work, follow that with the balance of buildings in 1904"*. The doc is written for students aged 14–16, mostly on phones: fun and easy, never trading away honesty about sources. Full transcription, owner rulings on its open questions, the mockups (M1–M10) and the dev screenshots it cites: chicago-tickets `evidence/navigator-mk2-2026-10-16/` (`DESIGN.md`; open `original/Navigator Design Doc.dc.html` in a browser for the mockups).

## Depends on

- T-2613 (NAV-104) — do not claim this ticket until it has merged; take the next workable ticket instead.
- T-2656 (NAV-903) — do not claim this ticket until it has merged; take the next workable ticket instead.

## What to build

§13 "Sound". The doc's backlog has no ticket for it; filed from §13. Owner ruling 2026-10-16: **on by
default** — it starts with the first user gesture (NAV-105 (T-2614)) and Settings › Sound turns it off
(remembered per device).

- Ticker: a soft flap tick per digit change, capped at 12 per second. Landing: a low clunk and a short
  reverb tail. Navigator: relay clicks on rail taps and a hum while open.
- Ambience per destination (e.g. wagons and birds in 1835; street sounds in 1904). Ambience is a
  reconstruction: record it in `docs/LIBERTIES.md`.
- Prefer synthesized WebAudio sounds; any recorded file needs a source and an `assets/LICENSES.md`
  entry (hard rule 6). Keep the boot payload unchanged: audio loads after landing.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- [ ] Sound plays after the first tap by default; Settings › Sound's master, effects and ambience work and persist.
- [ ] QA-04: iOS Safari, land, tap Free roam: ambience starts, no console errors.
- [ ] Every audio file is licensed in assets/LICENSES.md, and the ambience is listed in LIBERTIES.md.
- [ ] Works on a 390x844 phone and a 1440x900 laptop, and the 390x780 mobile smoke (the release gate) passes.
- [ ] Works in all four machine skins and with reduced motion.
- [ ] No ids, file paths or snake_case visible to a visitor (NAV-1003's lint passes once it has landed).
- [ ] Locked terms used exactly: Attested, Inferred, Reconstructed, Confidence view, Liberties, Sources, Jaunts.
- [ ] Every element id the smoke reads is preserved, or the smoke is updated in the same PR.
- [ ] A changelog.d/<ticket>.json entry says what a visitor will see, within the What's-New budget.
