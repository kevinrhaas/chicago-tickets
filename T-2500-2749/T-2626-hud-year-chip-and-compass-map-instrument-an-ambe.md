---
id: T-2626
title: HUD year chip and compass-map instrument: an amber LED year chip top left that opens Jump, and the compass and mini map merged into one round instrument top right that opens Map
state: done
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: NAV-302
parent: null
opened: 2026-10-16
closed: 2026-10-17
pr: 951
claimed_by: run 10/17/2026, 1:45:43 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-17T08:42:35Z
claimed_run: null
claimed_at: 2026-10-17T06:45:43.374Z
decision: null
decision_answer: null
---

HUD year chip and compass-map instrument: an amber LED year chip top left that opens Jump, and the compass and mini map merged into one round instrument top right that opens Map.

**Navigator Mk II — NAV-302.** Filed by the owner, 2026-10-16, from his design doc "Field Navigator Mk II · Experience redesign" (Rev 1.0, base `dev` @ cc2e803): *"build all of the tickets necessary for this ... then we do all of this interface work, follow that with the balance of buildings in 1904"*. The doc is written for students aged 14–16, mostly on phones: fun and easy, never trading away honesty about sources. Full transcription, owner rulings on its open questions, the mockups (M1–M10) and the dev screenshots it cites: chicago-tickets `evidence/navigator-mk2-2026-10-16/` (`DESIGN.md`; open `original/Navigator Design Doc.dc.html` in a browser for the mockups).

## Depends on

- T-2618 (NAV-202) — do not claim this ticket until it has merged; take the next workable ticket instead.

## What to build

§10. Year chip: top left, amber LED digits (`1904 · 07.01`); tap opens the Jump app (NAV-902 (T-2655)).
Compass + mini map merged into one round instrument (heading in degrees); tap opens Map (NAV-901 (T-2654)).
Until those apps land, open their registered stubs, so the wiring is one line to change.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- [ ] Year chip and round instrument render on phone and desktop in all four skins; each opens its app (or stub).
- [ ] The instrument's heading matches the camera yaw.
- [ ] Works on a 390x844 phone and a 1440x900 laptop, and the 390x780 mobile smoke (the release gate) passes.
- [ ] Works in all four machine skins and with reduced motion.
- [ ] No ids, file paths or snake_case visible to a visitor (NAV-1003's lint passes once it has landed).
- [ ] Locked terms used exactly: Attested, Inferred, Reconstructed, Confidence view, Liberties, Sources, Jaunts.
- [ ] Every element id the smoke reads is preserved, or the smoke is updated in the same PR.
- [ ] A changelog.d/<ticket>.json entry says what a visitor will see, within the What's-New budget.
