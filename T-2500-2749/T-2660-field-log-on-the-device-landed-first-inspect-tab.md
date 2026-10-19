---
id: T-2660
title: Field log on the device: landed, first inspect, tabs opened, Show me, Jaunts started and finished, Tour steps and Confidence presets counted in localStorage only, shown in Settings › About with a Clear button, never sent
state: review
epic: RENDERING
requested_by: owner
seen: true
effort: S
legacy_id: NAV-S02
parent: null
opened: 2026-10-16
closed: null
pr: 1054
claimed_by: run 10/18/2026, 5:48:18 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-18T22:48:18.079Z
decision: null
decision_answer: null
---

Field log on the device: landed, first inspect, tabs opened, Show me, Jaunts started and finished, Tour steps and Confidence presets counted in localStorage only, shown in Settings › About with a Clear button, never sent.

**Navigator Mk II — NAV-S02.** Filed by the owner, 2026-10-16, from his design doc "Field Navigator Mk II · Experience redesign" (Rev 1.0, base `dev` @ cc2e803): *"build all of the tickets necessary for this ... then we do all of this interface work, follow that with the balance of buildings in 1904"*. The doc is written for students aged 14–16, mostly on phones: fun and easy, never trading away honesty about sources. Full transcription, owner rulings on its open questions, the mockups (M1–M10) and the dev screenshots it cites: chicago-tickets `evidence/navigator-mk2-2026-10-16/` (`DESIGN.md`; open `original/Navigator Design Doc.dc.html` in a browser for the mockups).

## Depends on

- T-2656 (NAV-903) — do not claim this ticket until it has merged; take the next workable ticket instead.

## What to build

§14 "Measure fun". Owner ruling 2026-10-16: **local-only counts** — nothing leaves the device (the
audience is 14–16). Shown in Settings › About as "Field log", including time to first inspect (the doc's
target: first inspect within 90 s), with Clear. Useful for the student playtest (NAV-1006 (T-2670)).

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- [ ] Counts increment for each listed event and show in Settings › About; Clear empties them.
- [ ] No network request carries them (the smoke asserts no request is made on these events).
- [ ] Works on a 390x844 phone and a 1440x900 laptop, and the 390x780 mobile smoke (the release gate) passes.
- [ ] Works in all four machine skins and with reduced motion.
- [ ] No ids, file paths or snake_case visible to a visitor (NAV-1003's lint passes once it has landed).
- [ ] Locked terms used exactly: Attested, Inferred, Reconstructed, Confidence view, Liberties, Sources, Jaunts.
- [ ] Every element id the smoke reads is preserved, or the smoke is updated in the same PR.
- [ ] A changelog.d/<ticket>.json entry says what a visitor will see, within the What's-New budget.
