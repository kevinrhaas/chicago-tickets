---
id: T-2609
title: Navigator: the building card's two review bugs fixed now: 'bay dining [object Object]' under Attributes, and the 1835 fire-limit by-law shown on a 1904 building
state: open
epic: RENDERING
requested_by: owner
seen: true
effort: S
legacy_id: NAV-509
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

Navigator: the building card's two review bugs fixed now: 'bay dining [object Object]' under Attributes, and the 1835 fire-limit by-law shown on a 1904 building.

**Navigator Mk II — NAV-509.** Filed by the owner, 2026-10-16, from his design doc "Field Navigator Mk II · Experience redesign" (Rev 1.0, base `dev` @ cc2e803): *"build all of the tickets necessary for this ... then we do all of this interface work, follow that with the balance of buildings in 1904"*. The doc is written for students aged 14–16, mostly on phones: fun and easy, never trading away honesty about sources. Full transcription, owner rulings on its open questions, the mockups (M1–M10) and the dev screenshots it cites: chicago-tickets `evidence/navigator-mk2-2026-10-16/` (`DESIGN.md`; open `original/Navigator Design Doc.dc.html` in a browser for the mockups).

## What to build

Two HIGH findings from the design review (§01), both visible on dev today, fixed in the card that ships now
so they do not wait for the Inspect app:

- **[object Object]** — the 1904 Glessner card lists `bay dining [object Object]` under Attributes
  (screenshot `dev-screenshots/IMG_6945.png`). Source: `js/popup.js` / `js/compact-attributes.js`.
  Object-valued attributes render their value, or are omitted.
- **Wrong era** — the card's Evidence tab on a 1904 building shows the 1835 fire-limit by-law
  ("5 August 1835 … hay") (`IMG_6944.png`). Content tagged with another scene's era never renders on
  this scene's cards. The Story tab (NAV-507 (T-2643)) keeps the same filter later.

Reproduce both on dev first; if one is already fixed, say which PR fixed it and close that half.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- [ ] No '[object Object]' anywhere in the DOM after opening every tab of the 1904 Glessner card (QA-09).
- [ ] A unit test covers the object-valued attribute (bay_dining) and fails on the old code.
- [ ] No 1835-only content (the fire limit, 1835 ordinances) on any 1904 building card; the 1835 card still shows it.
- [ ] Works on a 390x844 phone and a 1440x900 laptop, and the 390x780 mobile smoke (the release gate) passes.
- [ ] Works in all four machine skins and with reduced motion.
- [ ] No ids, file paths or snake_case visible to a visitor (NAV-1003's lint passes once it has landed).
- [ ] Locked terms used exactly: Attested, Inferred, Reconstructed, Confidence view, Liberties, Sources, Jaunts.
- [ ] Every element id the smoke reads is preserved, or the smoke is updated in the same PR.
- [ ] A changelog.d/<ticket>.json entry says what a visitor will see, within the What's-New budget.
