---
id: T-1536
title: Seat the other 76 under-tens the book orders into lodging households: the children of DOCUMENTED keepers, and of the 37 boarding houses the lodging model schedules and nobody has built — T-1533 drew the 10 its own minted keepers could hold and the rest have no keeper here to be kin to
state: blocked-tech
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-24
closed: null
pr: null
claimed_by: run 9/24/2026, 6:24:24 AM CT
blocked_on: T-1537 and T-1538 (with T-1209's roofs): all 76 are under_10 children of lodging households that do not exist. Every documented keeper's family is already drawn or source-ruled, and the other half belongs to the 37 unbuilt boarding houses. A child is kin of a named keeper and there is no keeper left here to be kin to. The cell-by-cell measurement is in the ticket.
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/35992528938
claimed_at: 2026-09-24T11:24:24.888Z
decision: null
decision_answer: null
---

Seat the other 76 under-tens the book orders into lodging households: the children of DOCUMENTED keepers, and of the 37 boarding houses the lodging model schedules and nobody has built — T-1533 drew the 10 its own minted keepers could hold and the rest have no keeper here to be kin to.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## What a run measured before taking it (2026-09-24)

The 76 were counted cell by cell and both halves of the title were run down. Neither
is reachable, and they are not reachable for the same reason: **a child is drawn as
kin of a named keeper, and there is no keeper left here to be kin to.**

**The 76, as the book stands.** The six `10_19/*/lodging/none` cells are discharged.
All 76 are `under_10`:

| cell | to_reconstruct | filled | owed |
|---|---|---|---|
| `persons/female/under_10/north/lodging/none` | 9 | 4 | 5 |
| `persons/male/under_10/north/lodging/none` | 11 | 5 | 6 |
| `persons/female/under_10/west/lodging/none` | 9 | 0 | 9 |
| `persons/male/under_10/west/lodging/none` | 10 | 1 | 9 |
| `persons/female/under_10/south/lodging/none` | 22 | 0 | 22 |
| `persons/male/under_10/south/lodging/none` | 25 | 0 | 25 |

**Half one — the children of DOCUMENTED keepers — is DISCHARGED, not owed.** Every
one of the eight documented keepers in `1835_lodgers_seated.json` `keepers` has a
household that is already settled, and `1835_modelled_families.json` `by_household`
says by which rule:

- `hh_ingersoll_chester` (Green Tree, west) — `size_drawn` 8, `kin_seated` 8. Six
  under-tens stand on it.
- `hh_davis_john` (Steamboat Hotel, north) — 8 and 8. Three under-tens stand.
- `hh_stow_william_h` (Western Hotel, south) — 4 and 4. Two under-tens stand.
- `hh_brown_rufus`, `hh_couch_ira`, `hh_murphy_john` — refused by T-1171's own
  eligibility, reason *"a source already names, counts or rules on this household's
  family"*. A source settled them; the model may not draw over it.
- `hh_haddock_edward`, `hh_walters_william` — refused, cards stand at one person,
  and the `keepers` table already names **T-1179** as the convergence that moves them.

So there is no documented keeper whose family the model wants bigger. The twelve
under-tens that DO stand at a lodging place are not double-counted either: the book's
known side is spread **pro rata** (`subtract_pro_rata` in `build_order_book_1835.py`)
and never joins a real person to a household type, so `to_reconstruct` already has
them out. Drawing more children onto these cards would be dealing to the quota.

**Half two — the 37 unbuilt boarding houses — has no roof and no keeper.** The
boarders stage's own measurement says it in one line: *"the rest wait on the 37
unbuilt boarding houses … and the children of houses this stage does not keep."* All
16 built lodging places are at their ordinary-night figure (144 of 144 beds, 0 empty)
and `minted_keepers` is 6 of 16 — T-1533 drew all ten children those six could hold.

**So this ticket cannot be filled by a children's stage at all.** It is filled when a
lodging household exists to hold a child: `T-1537` reconciles the 64 the book orders
against the roof programme, `T-1538` fills the households and beds as `T-1209` raises
the 36 unbuilt lodging roofs. The children come with the household, drawn at the same
1840 size histogram T-1533 used — this is a row in those tickets, not a stage of its
own, and `unblock` should re-open it only if they land without drawing kin.
