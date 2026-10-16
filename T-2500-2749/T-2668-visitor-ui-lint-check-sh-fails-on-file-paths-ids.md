---
id: T-2668
title: Visitor-UI lint: check.sh fails on file paths, ids, snake_case, 'tier', 'ticket' or 'order book' in visitor strings, with Researcher-mode strings exempt
state: open
epic: PIPELINE
requested_by: owner
seen: true
effort: S
legacy_id: NAV-1003
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

Visitor-UI lint: check.sh fails on file paths, ids, snake_case, 'tier', 'ticket' or 'order book' in visitor strings, with Researcher-mode strings exempt.

**Navigator Mk II — NAV-1003.** Filed by the owner, 2026-10-16, from his design doc "Field Navigator Mk II · Experience redesign" (Rev 1.0, base `dev` @ cc2e803): *"build all of the tickets necessary for this ... then we do all of this interface work, follow that with the balance of buildings in 1904"*. The doc is written for students aged 14–16, mostly on phones: fun and easy, never trading away honesty about sources. Full transcription, owner rulings on its open questions, the mockups (M1–M10) and the dev screenshots it cites: chicago-tickets `evidence/navigator-mk2-2026-10-16/` (`DESIGN.md`; open `original/Navigator Design Doc.dc.html` in a browser for the mockups).

## Depends on

- T-2624 (NAV-1001) — do not claim this ticket until it has merged; take the next workable ticket instead.
- T-2667 (NAV-1002) — do not claim this ticket until it has merged; take the next workable ticket instead.

## What to build

§12 "Linted", NAV-1003. Runs over the string table, summary records, caption decks and the rendered DOM
in the smoke. Researcher-mode-only strings are exempt (owner ruling). Invisible gate: name in the PR the
visible work it protects.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- [ ] The lint passes on dev's visitor UI and fails on each planted fault (a path, a snake_case id, 'tier', 'ticket', 'order book').
- [ ] Works on a 390x844 phone and a 1440x900 laptop, and the 390x780 mobile smoke (the release gate) passes.
- [ ] Works in all four machine skins and with reduced motion.
- [ ] No ids, file paths or snake_case visible to a visitor (NAV-1003's lint passes once it has landed).
- [ ] Locked terms used exactly: Attested, Inferred, Reconstructed, Confidence view, Liberties, Sources, Jaunts.
- [ ] Every element id the smoke reads is preserved, or the smoke is updated in the same PR.
- [ ] A changelog.d/<ticket>.json entry says what a visitor will see, within the What's-New budget.
