---
id: T-3704
title: Guide › For teachers handout spills onto two pages since 1871 got three Jaunts (smoke 9-12 red on dev)
state: open
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-11-20
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

Guide › For teachers handout spills onto two pages since 1871 got three Jaunts (smoke 9-12 red on dev).

## FILED ABOVE BAND 9, BECAUSE IT BLOCKS

A follow-up goes to the foot of band 9 unless dev's gate is red on it or the build in hand cannot finish without it (owner, 2026-09-27). This one was placed above band 9 on this reason:

> dev's content-build smoke 9-12 is red on both viewports: Letter and A4 print 12 Jaunts across 2 pages since T-3692/T-3693 gave 1871 three, so every PR touching content is refused (PR #2252, run 44706006480)

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## Finding (loop, 2026-11-20, lapping PR #2252)

- The content build on dev `3da1ba107` (run 44677056432, 04:50Z) was green on smoke 9-12 at both
  viewports. After it, T-3691/T-3692/T-3693 gave 1871 its own Jaunts. On run 44706006480 (PR #2252,
  a K10 cornice change that touches no Guide or Jaunt file) the T-2666 check reads
  `"jaunts":12,"pages":2` for both Letter and A4, on desktop and mobile alike. Everything else in
  that check passes. Only `pages === 1` fails.
- `tools/smoke_renderer.mjs` around line 15054 already allows 1871 one to three Jaunts. So the
  sheet's layout has to fit 12 Jaunts on one page: tighten the print CSS, or list fewer per
  destination. Decide which, and don't loosen `pages === 1`: one page is what T-2666 promised teachers.
- Separately, desktop part 13 (the Navigator rail tablist check, T-2622) was already red on dev
  at `3da1ba107`. That one isn't this ticket.
