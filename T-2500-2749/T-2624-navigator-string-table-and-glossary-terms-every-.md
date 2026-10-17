---
id: T-2624
title: Navigator string table and glossary terms: every Navigator, HUD and arrival string in one table, the locked terms enforced and the renamed terms of §03 applied
state: done
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: NAV-1001
parent: null
opened: 2026-10-16
closed: 2026-10-17
pr: 946
claimed_by: run 10/17/2026, 1:45:30 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-17T08:51:42Z
claimed_run: null
claimed_at: 2026-10-17T06:45:30.688Z
decision: null
decision_answer: null
---

Navigator string table and glossary terms: every Navigator, HUD and arrival string in one table, the locked terms enforced and the renamed terms of §03 applied.

**Navigator Mk II — NAV-1001.** Filed by the owner, 2026-10-16, from his design doc "Field Navigator Mk II · Experience redesign" (Rev 1.0, base `dev` @ cc2e803): *"build all of the tickets necessary for this ... then we do all of this interface work, follow that with the balance of buildings in 1904"*. The doc is written for students aged 14–16, mostly on phones: fun and easy, never trading away honesty about sources. Full transcription, owner rulings on its open questions, the mockups (M1–M10) and the dev screenshots it cites: chicago-tickets `evidence/navigator-mk2-2026-10-16/` (`DESIGN.md`; open `original/Navigator Design Doc.dc.html` in a browser for the mockups).

## Depends on

- T-2617 (NAV-201) — do not claim this ticket until it has merged; take the next workable ticket instead.

## What to build

§03 "Locked terms" and "Renamed terms". One string module the Navigator, HUD and arrival read;
later apps add their strings to it as they land.

- Locked, exactly: Attested, Inferred, Reconstructed, Confidence view, Liberties, Sources, Jaunts —
  each with its one-line plain meaning (used by first-appearance taps and the Guide glossary NAV-804 (T-2662)).
  "Sources" retires "Evidence" and "Citations" (MED finding: three names for one thing).
- Renamed: Coordinate → Destination · Start/Jaunts chip → Jaunts app · Starting at…/Pick a place →
  Go to · Explore by myself → Free roam · Travel/pace → Move · Controls/Help → Guide · Firms →
  Shops & work · Modeled phase → Stood here · Present status → Today · STRUCT/SYNC lamps → STREETS ·
  BUILDINGS · TREES · PEOPLE · Not recorded → Unknown · Order book/tickets/tier → never shown
  (Researcher mode only, NAV-S03 (T-2657)).
- A small check fails when a locked term appears in another spelling in the table.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- [ ] One string table module; the Navigator, HUD and arrival read their visible strings from it.
- [ ] Every renamed term in §03 is applied in the shipped UI; the locked-term check passes and fails on a planted misspelling.
- [ ] Works on a 390x844 phone and a 1440x900 laptop, and the 390x780 mobile smoke (the release gate) passes.
- [ ] Works in all four machine skins and with reduced motion.
- [ ] No ids, file paths or snake_case visible to a visitor (NAV-1003's lint passes once it has landed).
- [ ] Locked terms used exactly: Attested, Inferred, Reconstructed, Confidence view, Liberties, Sources, Jaunts.
- [ ] Every element id the smoke reads is preserved, or the smoke is updated in the same PR.
- [ ] A changelog.d/<ticket>.json entry says what a visitor will see, within the What's-New budget.
