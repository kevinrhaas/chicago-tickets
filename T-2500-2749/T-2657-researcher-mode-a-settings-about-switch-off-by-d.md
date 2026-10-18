---
id: T-2657
title: Researcher mode: a Settings › About switch, off by default, that brings back the order book, ticket references, source ids, file paths and the full 'Why this default' essays the visitor UI no longer carries
state: open
epic: RENDERING
requested_by: owner
seen: true
effort: S
legacy_id: NAV-S03
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

Researcher mode: a Settings › About switch, off by default, that brings back the order book, ticket references, source ids, file paths and the full 'Why this default' essays the visitor UI no longer carries.

**Navigator Mk II — NAV-S03.** Filed by the owner, 2026-10-16, from his design doc "Field Navigator Mk II · Experience redesign" (Rev 1.0, base `dev` @ cc2e803): *"build all of the tickets necessary for this ... then we do all of this interface work, follow that with the balance of buildings in 1904"*. The doc is written for students aged 14–16, mostly on phones: fun and easy, never trading away honesty about sources. Full transcription, owner rulings on its open questions, the mockups (M1–M10) and the dev screenshots it cites: chicago-tickets `evidence/navigator-mk2-2026-10-16/` (`DESIGN.md`; open `original/Navigator Design Doc.dc.html` in a browser for the mockups).

## Depends on

- T-2656 (NAV-903) — do not claim this ticket until it has merged; take the next workable ticket instead.

## What to build

Owner ruling 2026-10-16 on the doc's first open question: no separate /research page — the internal
views are **hidden behind a toggle**. Researcher mode is off by default, remembered per device, and
shows a small RESEARCHER label while on. Content the doc sends to /research (§12 "Remove from visitor
UI", NAV-904 (T-2658), NAV-1002 (T-2667)) is shown in place when it is on. The visitor-UI lint (NAV-1003 (T-2668)) exempts strings
that render only in Researcher mode.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- [ ] Off by default; turning it on shows the order book and full essays, turning it off hides them; persists across reloads.
- [ ] Works on a 390x844 phone and a 1440x900 laptop, and the 390x780 mobile smoke (the release gate) passes.
- [ ] Works in all four machine skins and with reduced motion.
- [ ] No ids, file paths or snake_case visible to a visitor (NAV-1003's lint passes once it has landed).
- [ ] Locked terms used exactly: Attested, Inferred, Reconstructed, Confidence view, Liberties, Sources, Jaunts.
- [ ] Every element id the smoke reads is preserved, or the smoke is updated in the same PR.
- [ ] A changelog.d/<ticket>.json entry says what a visitor will see, within the What's-New budget.

**Finding, 2026-10-18 (from T-2668's visitor-UI lint, branch claude/t2668-visitor-lint).**
Two things the lint does not yet cover still show ids to a visitor:
- **The Shops & work card's location lines** (`basis`, and `limit_reason` on every location in
  data/businesses/index.json). Several name structure ids, a few name ticket numbers, and the 17
  lines for firms not trading at the scene date cite newspaper claim ids.
- **Four hand-written civic-office notes** that T-2668 allowlists under this ticket. They show in
  their Go to rows and cite research ids, `data/exclusions.json` or
  `docs/RESEARCH/hogan_store.md`:
  - biz_chicago_post_office
  - biz_cook_county_offices
  - biz_indian_agency_chicago
  - biz_us_land_office_chicago

Both belong behind Researcher mode, with a visitor wording in front. When this lands:
- Remove the four allowlist entries from tools/check_visitor_ui.py (a stale entry fails the gate).
- Extend the lint to the card's location lines.
