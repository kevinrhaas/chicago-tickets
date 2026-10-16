---
id: T-2641
title: Navigator Inspect Design tab: the style card, numbered 'On this house' hotspots with grades replacing the attribute table, Compare styles, and the Richardsonian Romanesque module for Glessner House
state: open
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: NAV-506
parent: null
opened: 2026-10-16
closed: null
pr: null
claimed_by: null
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: null
decision: null
decision_answer: null
---

Navigator Inspect Design tab: the style card, numbered 'On this house' hotspots with grades replacing the attribute table, Compare styles, and the Richardsonian Romanesque module for Glessner House.

**Navigator Mk II — NAV-506.** Filed by the owner, 2026-10-16, from his design doc "Field Navigator Mk II · Experience redesign" (Rev 1.0, base `dev` @ cc2e803): *"build all of the tickets necessary for this ... then we do all of this interface work, follow that with the balance of buildings in 1904"*. The doc is written for students aged 14–16, mostly on phones: fun and easy, never trading away honesty about sources. Full transcription, owner rulings on its open questions, the mockups (M1–M10) and the dev screenshots it cites: chicago-tickets `evidence/navigator-mk2-2026-10-16/` (`DESIGN.md`; open `original/Navigator Design Doc.dc.html` in a browser for the mockups).

## Depends on

- T-2639 (NAV-504) — do not claim this ticket until it has merged; take the next workable ticket instead.

## What to build

§08 M8 and "Design" tab; §12 "Style library". The attribute table moves down into hotspots.

- Style card: name, two-line plain description, four "how to spot it" cues.
- "On this house · tap to look": numbered hotspots, each with its grade dot (e.g. granite street walls
  Attested; exact window sizes Reconstructed — "Listed in Liberties"). Tapping one uses Show me.
- Compare styles: three neighbouring styles, one line each.
- This ticket authors the Richardsonian Romanesque module (cues + a credited reference plate from an
  image the project already has rights to); the other five are NAV-506b (T-2642).

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- [ ] Glessner's Design tab shows the Romanesque card, graded numbered hotspots and Compare styles, phone and desktop.
- [ ] No attribute table remains on the Design tab; every hotspot has a grade dot.
- [ ] Works on a 390x844 phone and a 1440x900 laptop, and the 390x780 mobile smoke (the release gate) passes.
- [ ] Works in all four machine skins and with reduced motion.
- [ ] No ids, file paths or snake_case visible to a visitor (NAV-1003's lint passes once it has landed).
- [ ] Locked terms used exactly: Attested, Inferred, Reconstructed, Confidence view, Liberties, Sources, Jaunts.
- [ ] Every element id the smoke reads is preserved, or the smoke is updated in the same PR.
- [ ] A changelog.d/<ticket>.json entry says what a visitor will see, within the What's-New budget.
