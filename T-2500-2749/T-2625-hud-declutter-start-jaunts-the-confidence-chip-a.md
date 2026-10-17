---
id: T-2625
title: HUD declutter: Start/Jaunts, the Confidence chip and caret, pace, theme and menu leave the HUD's top row, each reachable in the Navigator, and the street readout becomes a 2 s toast
state: review
epic: RENDERING
requested_by: owner
seen: true
effort: S
legacy_id: NAV-301
parent: null
opened: 2026-10-16
closed: null
pr: 969
claimed_by: null
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: null
decision: null
decision_answer: null
---

HUD declutter: Start/Jaunts, the Confidence chip and caret, pace, theme and menu leave the HUD's top row, each reachable in the Navigator, and the street readout becomes a 2 s toast.

**Navigator Mk II — NAV-301.** Filed by the owner, 2026-10-16, from his design doc "Field Navigator Mk II · Experience redesign" (Rev 1.0, base `dev` @ cc2e803): *"build all of the tickets necessary for this ... then we do all of this interface work, follow that with the balance of buildings in 1904"*. The doc is written for students aged 14–16, mostly on phones: fun and easy, never trading away honesty about sources. Full transcription, owner rulings on its open questions, the mockups (M1–M10) and the dev screenshots it cites: chicago-tickets `evidence/navigator-mk2-2026-10-16/` (`DESIGN.md`; open `original/Navigator Design Doc.dc.html` in a browser for the mockups).

## Depends on

- T-2620 (NAV-206) — do not claim this ticket until it has merged; take the next workable ticket instead.

## What to build

§10 "In-world HUD". Seven HUD buttons in two rows cover about a quarter of a phone screen (HIGH/MED
findings; `IMG_6942`). Moved: Start/Jaunts → Jaunts app; Confidence chip and caret → Confidence app;
pace → Move; theme → Settings › Display; menu → the dock; control-help popover → Guide. The street
readout is kept as a 2 s toast when you cross onto a new street. The C hotkey keeps working.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- [ ] The HUD's top row holds none of the removed controls; each function is reachable in the Navigator.
- [ ] Crossing onto a new street shows the street name for about 2 s, then it fades.
- [ ] Works on a 390x844 phone and a 1440x900 laptop, and the 390x780 mobile smoke (the release gate) passes.
- [ ] Works in all four machine skins and with reduced motion.
- [ ] No ids, file paths or snake_case visible to a visitor (NAV-1003's lint passes once it has landed).
- [ ] Locked terms used exactly: Attested, Inferred, Reconstructed, Confidence view, Liberties, Sources, Jaunts.
- [ ] Every element id the smoke reads is preserved, or the smoke is updated in the same PR.
- [ ] A changelog.d/<ticket>.json entry says what a visitor will see, within the What's-New budget.
