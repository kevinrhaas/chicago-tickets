---
id: T-2610
title: Navigator arrival: a two-line year readout, DESTINATION 1904 · PRAIRIE AVE above the ticker from first paint and the ticker rolling from the present year down to the destination, with the 'Destination year' label removed
state: done
epic: RENDERING
requested_by: owner
seen: true
effort: S
legacy_id: NAV-101
parent: null
opened: 2026-10-16
closed: 2026-10-16
pr: 900
claimed_by: run 10/16/2026, 2:37:31 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-16T21:05:26Z
claimed_run: null
claimed_at: 2026-10-16T19:37:31.612Z
decision: null
decision_answer: null
---

Navigator arrival: a two-line year readout, DESTINATION 1904 · PRAIRIE AVE above the ticker from first paint and the ticker rolling from the present year down to the destination, with the 'Destination year' label removed.

**Navigator Mk II — NAV-101.** Filed by the owner, 2026-10-16, from his design doc "Field Navigator Mk II · Experience redesign" (Rev 1.0, base `dev` @ cc2e803): *"build all of the tickets necessary for this ... then we do all of this interface work, follow that with the balance of buildings in 1904"*. The doc is written for students aged 14–16, mostly on phones: fun and easy, never trading away honesty about sources. Full transcription, owner rulings on its open questions, the mockups (M1–M10) and the dev screenshots it cites: chicago-tickets `evidence/navigator-mk2-2026-10-16/` (`DESIGN.md`; open `original/Navigator Design Doc.dc.html` in a browser for the mockups).

## What to build

§05 "Year readout: two lines". Today the label over the ticker says *Destination year* while the
digits show the present year (HIGH finding; `index.html #arrival-year`, `js/arrival.js yearForProgress`).

- Small line above: `DESTINATION 1904 · PRAIRIE AVE` (per destination). It is written by the inline
  first-paint script that already sets the digits, and never changes during the trip.
- Big ticker: the year being passed. Starts at the present year and rolls down to the destination.
  Keep the existing split-flap digits (`setDigits`) and pacing.
- Delete the "Destination year" label.
- The ticker never moves backwards (towards the present) once it has started.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- [ ] QA-01: jump to 1904 from the Observatory; the small line reads DESTINATION 1904 from first paint and the ticker rolls from the present year to 1904.
- [ ] Same for 1835 and 1812, each with its own place name.
- [ ] Under a throttled load (Slow 3G profile) the ticker year never increases.
- [ ] Works on a 390x844 phone and a 1440x900 laptop, and the 390x780 mobile smoke (the release gate) passes.
- [ ] Works in all four machine skins and with reduced motion.
- [ ] No ids, file paths or snake_case visible to a visitor (NAV-1003's lint passes once it has landed).
- [ ] Locked terms used exactly: Attested, Inferred, Reconstructed, Confidence view, Liberties, Sources, Jaunts.
- [ ] Every element id the smoke reads is preserved, or the smoke is updated in the same PR.
- [ ] A changelog.d/<ticket>.json entry says what a visitor will see, within the What's-New budget.
