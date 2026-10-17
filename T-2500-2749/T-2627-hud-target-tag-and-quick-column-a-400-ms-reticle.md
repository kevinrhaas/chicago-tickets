---
id: T-2627
title: HUD target tag and quick column: a 400 ms reticle dwell shows the building's name and distance, tap or E opens Inspect, and the quick column holds Walk/Fly plus a contextual Inspect key, never more than two
state: done
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: NAV-303
parent: null
opened: 2026-10-16
closed: 2026-10-17
pr: 955
claimed_by: run 10/17/2026, 2:17:07 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-17T09:52:37Z
claimed_run: null
claimed_at: 2026-10-17T07:17:07.775Z
decision: null
decision_answer: null
---

HUD target tag and quick column: a 400 ms reticle dwell shows the building's name and distance, tap or E opens Inspect, and the quick column holds Walk/Fly plus a contextual Inspect key, never more than two.

**Navigator Mk II — NAV-303.** Filed by the owner, 2026-10-16, from his design doc "Field Navigator Mk II · Experience redesign" (Rev 1.0, base `dev` @ cc2e803): *"build all of the tickets necessary for this ... then we do all of this interface work, follow that with the balance of buildings in 1904"*. The doc is written for students aged 14–16, mostly on phones: fun and easy, never trading away honesty about sources. Full transcription, owner rulings on its open questions, the mockups (M1–M10) and the dev screenshots it cites: chicago-tickets `evidence/navigator-mk2-2026-10-16/` (`DESIGN.md`; open `original/Navigator Design Doc.dc.html` in a browser for the mockups).

## Depends on

- T-2618 (NAV-202) — do not claim this ticket until it has merged; take the next workable ticket instead.

## What to build

§10. Target tag "GLESSNER HOUSE · 38 FT" when the reticle rests on a building for 400 ms; tap it or
press E to Inspect (the Inspect app is NAV-501 (T-2638); until then it opens the current card). The quick
column keeps one Walk/Fly toggle (everything else is in Move) and an Inspect key that appears with a
target. Use the existing pick path (`js/gpu-pick.js`) at a dwell rate that does not cost frame time —
the performance group just paid for those frames.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- [ ] Resting the reticle on a building for 400 ms shows its name and distance; E or a tap opens it.
- [ ] The quick column never holds more than two buttons; the smoke's frame budget is unchanged.
- [ ] Works on a 390x844 phone and a 1440x900 laptop, and the 390x780 mobile smoke (the release gate) passes.
- [ ] Works in all four machine skins and with reduced motion.
- [ ] No ids, file paths or snake_case visible to a visitor (NAV-1003's lint passes once it has landed).
- [ ] Locked terms used exactly: Attested, Inferred, Reconstructed, Confidence view, Liberties, Sources, Jaunts.
- [ ] Every element id the smoke reads is preserved, or the smoke is updated in the same PR.
- [ ] A changelog.d/<ticket>.json entry says what a visitor will see, within the What's-New budget.
