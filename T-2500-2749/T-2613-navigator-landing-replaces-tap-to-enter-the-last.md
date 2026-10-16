---
id: T-2613
title: Navigator landing replaces Tap to enter: the last digit clunks into place, an ARRIVED flash, the device flips to Navigator Home and the scene un-blurs, with #gate-btn and the Welcome card retired behind a small js/journey.js state machine
state: claimed
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: NAV-104
parent: null
opened: 2026-10-16
closed: null
pr: null
claimed_by: run 10/16/2026, 4:32:45 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-16T21:32:45.605Z
decision: null
decision_answer: null
---

Navigator landing replaces Tap to enter: the last digit clunks into place, an ARRIVED flash, the device flips to Navigator Home and the scene un-blurs, with #gate-btn and the Welcome card retired behind a small js/journey.js state machine.

**Navigator Mk II — NAV-104.** Filed by the owner, 2026-10-16, from his design doc "Field Navigator Mk II · Experience redesign" (Rev 1.0, base `dev` @ cc2e803): *"build all of the tickets necessary for this ... then we do all of this interface work, follow that with the balance of buildings in 1904"*. The doc is written for students aged 14–16, mostly on phones: fun and easy, never trading away honesty about sources. Full transcription, owner rulings on its open questions, the mockups (M1–M10) and the dev screenshots it cites: chicago-tickets `evidence/navigator-mk2-2026-10-16/` (`DESIGN.md`; open `original/Navigator Design Doc.dc.html` in a browser for the mockups).

## Depends on

- T-2610 (NAV-101) — do not claim this ticket until it has merged; take the next workable ticket instead.

## What to build

§05 "Landing, not Tap to enter", §04 journey states, §14 "Journey state machine".
Today there are two stops before play: Tap to enter, then the Welcome card (HIGH finding;
`#gate-btn`, `#welcome`, `IMG_6950-51`).

- `js/journey.js`: one tiny state machine emitting state events —
  observatory › locking › jumping › time-stream › landing › landed › exploring ⇄ inspecting ·
  on-jaunt · touring › recall. HUD, Navigator, Tour and audio subscribe to it.
  `arrival.js settle()` calls `journey.land()` instead of enabling `#gate-btn`.
- On ready: the last digit drops with a clunk (`navigator.vibrate(30)` where supported; the sound
  itself is NAV-S01 (T-2659)), a phosphor flash and ARRIVED stamp (180 ms), the small line changes to
  `ARRIVED · 1904.07.01` and the digits turn amber → phosphor green; the device turns over
  (rotateY 0→180°, 520 ms, ease-machine) to its back face, Navigator Home; the scene behind un-blurs
  12 px → 0 and the gate scrim fades.
- Home (M2): "You're on Prairie Avenue." + one line + three choices — Take a Jaunt · Go to… ·
  Free roam — and "First time? Take the 60-second tour" (the tour is NAV-801 (T-2663); hide the link until
  it lands). Until NAV-201 (T-2617) lands the back face hosts these three choices with the Welcome card's
  existing handlers; NAV-201 (T-2617) makes it the real Navigator Home.
- Reduced motion: crossfade instead of the flip; ticker in 5 steps (existing `reducedProgress`).
- Accessibility: landing announces "Arrived: Prairie Avenue, 1 July 1904" (aria-live).
- The smoke drives `#gate-btn` today: update the smoke in the same PR.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- [ ] QA-02: wait for ready; no Tap to enter; the device flips to Home; the scene is interactive 900 ms or less after ready.
- [ ] QA-06: with reduced motion, a crossfade instead of the flip and the ticker in 5 steps.
- [ ] QA-20: VoiceOver announces 'Arrived: Prairie Avenue, 1 July 1904' (and the matching line in 1835 and 1812).
- [ ] journey.js emits every state transition once, in order, and the smoke passes with the gate button gone.
- [ ] Works on a 390x844 phone and a 1440x900 laptop, and the 390x780 mobile smoke (the release gate) passes.
- [ ] Works in all four machine skins and with reduced motion.
- [ ] No ids, file paths or snake_case visible to a visitor (NAV-1003's lint passes once it has landed).
- [ ] Locked terms used exactly: Attested, Inferred, Reconstructed, Confidence view, Liberties, Sources, Jaunts.
- [ ] Every element id the smoke reads is preserved, or the smoke is updated in the same PR.
- [ ] A changelog.d/<ticket>.json entry says what a visitor will see, within the What's-New budget.
