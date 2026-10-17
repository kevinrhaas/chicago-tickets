---
id: T-2651
title: Navigator Move app: one mode picker, Walk, Run, Wagon, Horse or Fly, replacing #s-travel and #s-pace, with one slider for the active mode that keeps the named speeds
state: claimed
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: NAV-701
parent: null
opened: 2026-10-16
closed: null
pr: null
claimed_by: run 10/17/2026, 2:32:37 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-17T07:32:37.629Z
decision: null
decision_answer: null
---

Navigator Move app: one mode picker, Walk, Run, Wagon, Horse or Fly, replacing #s-travel and #s-pace, with one slider for the active mode that keeps the named speeds.

**Navigator Mk II — NAV-701.** Filed by the owner, 2026-10-16, from his design doc "Field Navigator Mk II · Experience redesign" (Rev 1.0, base `dev` @ cc2e803): *"build all of the tickets necessary for this ... then we do all of this interface work, follow that with the balance of buildings in 1904"*. The doc is written for students aged 14–16, mostly on phones: fun and easy, never trading away honesty about sources. Full transcription, owner rulings on its open questions, the mockups (M1–M10) and the dev screenshots it cites: chicago-tickets `evidence/navigator-mk2-2026-10-16/` (`DESIGN.md`; open `original/Navigator Design Doc.dc.html` in a browser for the mockups).

## Depends on

- T-2618 (NAV-202) — do not claim this ticket until it has merged; take the next workable ticket instead.

## What to build

§07 "Move", M6. The Travel tab asks Walk/Wagon/Horse twice and adds three sliders (MED finding,
`IMG_6948`). One picker; one slider for the selected mode, keeping the named speeds ("Rattling along ·
24 mph"). The HUD keeps a single Walk/Fly toggle.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- [ ] One picker and one slider; changing mode changes the slider's range and named speeds; the old #s-travel/#s-pace controls are gone (smoke updated).
- [ ] Works on a 390x844 phone and a 1440x900 laptop, and the 390x780 mobile smoke (the release gate) passes.
- [ ] Works in all four machine skins and with reduced motion.
- [ ] No ids, file paths or snake_case visible to a visitor (NAV-1003's lint passes once it has landed).
- [ ] Locked terms used exactly: Attested, Inferred, Reconstructed, Confidence view, Liberties, Sources, Jaunts.
- [ ] Every element id the smoke reads is preserved, or the smoke is updated in the same PR.
- [ ] A changelog.d/<ticket>.json entry says what a visitor will see, within the What's-New budget.
