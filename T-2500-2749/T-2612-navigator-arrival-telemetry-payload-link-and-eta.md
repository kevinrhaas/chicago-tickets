---
id: T-2612
title: Navigator arrival telemetry: Payload, Link and ETA kept, a YEARS TO GO counter added, the six lamps regrouped as STREETS, BUILDINGS, TREES and PEOPLE on the real boot phases, and log lines from the destination deck
state: done
epic: RENDERING
requested_by: owner
seen: true
effort: S
legacy_id: NAV-103
parent: null
opened: 2026-10-16
closed: 2026-10-16
pr: 923
claimed_by: run 10/16/2026, 7:45:45 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-17T01:32:44Z
claimed_run: null
claimed_at: 2026-10-17T00:45:45.073Z
decision: null
decision_answer: null
---

Navigator arrival telemetry: Payload, Link and ETA kept, a YEARS TO GO counter added, the six lamps regrouped as STREETS, BUILDINGS, TREES and PEOPLE on the real boot phases, and log lines from the destination deck.

**Navigator Mk II — NAV-103.** Filed by the owner, 2026-10-16, from his design doc "Field Navigator Mk II · Experience redesign" (Rev 1.0, base `dev` @ cc2e803): *"build all of the tickets necessary for this ... then we do all of this interface work, follow that with the balance of buildings in 1904"*. The doc is written for students aged 14–16, mostly on phones: fun and easy, never trading away honesty about sources. Full transcription, owner rulings on its open questions, the mockups (M1–M10) and the dev screenshots it cites: chicago-tickets `evidence/navigator-mk2-2026-10-16/` (`DESIGN.md`; open `original/Navigator Design Doc.dc.html` in a browser for the mockups).

## Depends on

- T-2611 (NAV-102) — do not claim this ticket until it has merged; take the next workable ticket instead.

## What to build

§05 "Telemetry: semi-real, on purpose".

- Keep Payload, Link and ETA (real bytes, real rate, the forecast ETA from `js/boot-forecast.js`).
- Add `YEARS TO GO` next to them (destination distance from the ticker year).
- The six lamps (`#arrival-lamps`; STRUCT and SYNC say nothing a visitor understands — LOW finding)
  become four named groups mapped to `js/boot-phases.js`: STREETS (scene + terrain + ground),
  BUILDINGS, TREES (flora), PEOPLE (people + interaction).
- Log lines mix machine and destination: "SYNCING TIME MESH… OK", "UN-BUILDING THE LOOP…",
  "PLANTING 1904 ELMS…", "LOCATING GLESSNER HOUSEHOLD…" — from the destination's deck file (NAV-102 (T-2611)).
  Machine lore stays in mono caps; nothing here pretends to be research.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- [ ] QA-03: under Slow 3G, Payload, Link, ETA and YEARS TO GO all update.
- [ ] Each of the four lamps lights when its boot phases finish, in all three destinations.
- [ ] Reduced motion: no ticking log animation; values still update.
- [ ] Works on a 390x844 phone and a 1440x900 laptop, and the 390x780 mobile smoke (the release gate) passes.
- [ ] Works in all four machine skins and with reduced motion.
- [ ] No ids, file paths or snake_case visible to a visitor (NAV-1003's lint passes once it has landed).
- [ ] Locked terms used exactly: Attested, Inferred, Reconstructed, Confidence view, Liberties, Sources, Jaunts.
- [ ] Every element id the smoke reads is preserved, or the smoke is updated in the same PR.
- [ ] A changelog.d/<ticket>.json entry says what a visitor will see, within the What's-New budget.
