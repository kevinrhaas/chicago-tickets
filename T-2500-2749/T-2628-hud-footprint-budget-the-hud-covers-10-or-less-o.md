---
id: T-2628
title: HUD footprint budget: the HUD covers 10 % or less of a 390x844 viewport and respects safe areas, measured by the smoke
state: done
epic: RENDERING
requested_by: owner
seen: true
effort: S
legacy_id: NAV-304
parent: null
opened: 2026-10-16
closed: 2026-10-18
pr: 971
claimed_by: null
blocked_on: null
needs_bake: false
closed_at: 2026-10-18T12:36:08Z
claimed_run: null
claimed_at: null
decision: null
decision_answer: null
---

HUD footprint budget: the HUD covers 10 % or less of a 390x844 viewport and respects safe areas, measured by the smoke.

**Navigator Mk II — NAV-304.** Filed by the owner, 2026-10-16, from his design doc "Field Navigator Mk II · Experience redesign" (Rev 1.0, base `dev` @ cc2e803): *"build all of the tickets necessary for this ... then we do all of this interface work, follow that with the balance of buildings in 1904"*. The doc is written for students aged 14–16, mostly on phones: fun and easy, never trading away honesty about sources. Full transcription, owner rulings on its open questions, the mockups (M1–M10) and the dev screenshots it cites: chicago-tickets `evidence/navigator-mk2-2026-10-16/` (`DESIGN.md`; open `original/Navigator Design Doc.dc.html` in a browser for the mockups).

## Depends on

- T-2625 (NAV-301) — do not claim this ticket until it has merged; take the next workable ticket instead.
- T-2626 (NAV-302) — do not claim this ticket until it has merged; take the next workable ticket instead.
- T-2627 (NAV-303) — do not claim this ticket until it has merged; take the next workable ticket instead.

## What to build

§10 "AFTER · ≤ 10 % OF SCREEN". The smoke measures the union of the HUD's visible rectangles at
390×844 (and at the 390×780 gate) and fails over 10 %. Safe-area insets respected on notched phones.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- [ ] QA-17: the HUD covers 10 % or less of a 390x844 viewport, asserted by the smoke and failing on a planted extra button.
- [ ] Works on a 390x844 phone and a 1440x900 laptop, and the 390x780 mobile smoke (the release gate) passes.
- [ ] Works in all four machine skins and with reduced motion.
- [ ] No ids, file paths or snake_case visible to a visitor (NAV-1003's lint passes once it has landed).
- [ ] Locked terms used exactly: Attested, Inferred, Reconstructed, Confidence view, Liberties, Sources, Jaunts.
- [ ] Every element id the smoke reads is preserved, or the smoke is updated in the same PR.
- [ ] A changelog.d/<ticket>.json entry says what a visitor will see, within the What's-New budget.

## Owner's ruling (2026-10-18)
T-2741's street readout under the compass (on by default) put the phone HUD at 12.1 %. Asked: toast it, don't count it,
shrink it, or raise the budget. Owner: **"Keep it up; don't count it"** — the 10 % budget is measured without readouts the
visitor can switch off; the readout's own share is reported beside the figure (#971).

## Owner's ruling (2026-10-18): the Confidence legend chip is not counted
T-2649's legend chip (#conf-legend, 81x22 px under the year chip) shows only while the visitor
has the Confidence view on. With it on, the phone HUD measured 10.46 % of 390x780 (9.81 %
without it). Ruling: "Don't count it." Like T-2741's street readout, the 10 % budget is measured
without it, and its share is reported.
