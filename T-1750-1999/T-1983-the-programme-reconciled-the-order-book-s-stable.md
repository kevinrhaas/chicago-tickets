---
id: T-1983
title: The programme reconciled: the order book's stable and outbuilding roofs built or re-budgeted, dwellings against the census's 398, residents/transients/garrison on the census screen
state: open
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-02
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

The programme reconciled: the order book's stable and outbuilding roofs built or re-budgeted, dwellings against the census's 398, residents/transients/garrison on the census screen.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 250 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> T-1967 shipped the completion report and the City card's completion row; its 'programme reconciled' half owns five order-book cells (29 stable and outbuilding roofs still counted) that need a live owner when T-1967 closes, or check.sh's liveness gate refuses the close. It is T-1967's remainder in T-1967's place, not new scope.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

**Acceptance** (written by T-1967's run, which handed this on):

1. The order book's `barns_stables` and `small_outbuildings` cells in the North, South and
   West (29 roofs counted on 2026-10-02) are built, or re-budgeted with the reason, so the
   roof programme reconciles against `town_census.json`'s `buildings.target`.
2. The census screen (Evidence → City) states dwellings standing against the November
   census's 398 with the bracket, and the residents / transients / garrison split.
3. The census's `people.housed` counts a household seated by a roof's `residents[]` as the
   completion audit does (it reads `lives_at` only: 183 people against the audit's 1,508
   households), and the two files agree on who is present on 1 July (census population
   2,381; audit 2,496 housed and present + 525 waiting on a roof) — or the page says why
   they differ.

Parent: T-1215 (items 2 and the programme). Pointers moved here: `tools/build_order_book_1835.py`
owner table, `docs/LIBERTIES.md` (two references).


## Queue cleanup 2026-10-03 (owner: "clean out any tickets that … no longer need to be there or are obsolete")

**Merged into this ticket:** T-1692. T-1692's pricing of yard buildings against dwellings is the first step of T-1983's outbuilding reconciliation. T-1983 is kept (not the lower number) because the order book names it as the owner of those cells.

### Folded in from T-1692 — One yard building for every four houses is a claim about the TOWN's A-family targets and not about any block: price the 158 stables, barns, privies, woodsheds and utility roofs against the dwellings they are meant to serve, and say whether the target is short or the districts are unevenly dealt

One yard building for every four houses is a claim about the TOWN's A-family targets and not about any block: price the 158 stables, barns, privies, woodsheds and utility roofs against the dwellings they are meant to serve, and say whether the target is short or the districts are unevenly dealt.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
