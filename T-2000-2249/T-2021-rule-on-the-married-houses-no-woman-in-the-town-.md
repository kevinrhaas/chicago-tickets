---
id: T-2021
title: Rule on the married houses no woman in the town can be wife to: the whole layer reads about 299 adult men per 100 women against the model's 121-150 and the order book has no woman left in their cells — a re-cut that orders more women, or heads that stand alone
state: done
epic: META
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-1171
opened: 2026-10-03
closed: 2026-10-03
pr: 374
claimed_by: run 10/3/2026, 6:42:52 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-04T04:50:17Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37160161652
claimed_at: 2026-10-03T23:42:52.039Z
decision: null
decision_answer: null
---

Rule on the married houses no woman in the town can be wife to: the whole layer reads about 299 adult men per 100 women against the model's 121-150 and the order book has no woman left in their cells — a re-cut that orders more women, or heads that stand alone.

Piece 3 of 3 of **T-1171 — Give the remaining attested and inferred heads reconstructed families from the household model: wives, children, servants and apprentices drawn by the head's age, trade and household type, seeded, named from the pools, every member marked reconstructed**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

**This ticket owns the order book's family rows** (T-2019, 2026-10-03). T-1171's split would
have left `households/family_dwelling/*`, `households/store_residence/*` and the person cells
"otherwise: a family drawn from the household model" naming a split ticket, which
`every_work_order_names_a_live_ticket` refuses. They moved here (`FAMILY_OWNER` in
`tools/build_order_book_1835.py`), because what is left of T-1171's order once T-2020's moves
are made is exactly this ruling: does the book order more women, or do the heads stand alone.
The modelled-families stage keeps T-1171 as the ticket on its own fills — that is who drew.

## 2026-10-03 — the ruling, and the acceptance it is held to

**Ruling: both, partitioned by the bound the book already carries.** The town model's own
range for 1 July 1835 is 2,362–3,265 (its top is the November 1835 town count). The book
converges to 2,605 without these houses; giving all 277 their drawn kin core (904 people:
277 wives, 627 children) would carry it to 3,509, past the count. Wives alone would leave
houses the model drew at 5–8 people as childless couples, and the town's under-ten share is
already below the model's 0.20–0.27 bracket. So a refused house is given its WHOLE drawn
family — wife and children, by the stage's own seeds and rules — in a seeded order, while
the town the book converges to stays at or under 3,265; a house whose family would carry
it past the count stands alone, and says so. The houses admitted are read once and FROZEN
(`data/reconstruction/1835_family_ruling.json`), so a later re-cut re-deals nobody. The
book orders exactly what the ruling's houses drew (fills under T-2021), so no cell is
overfilled and none is left owing. The adult men already in the town (1,254 present) are
what pin it near the range top: at the model's 146.8 ratio they imply ~854 adult women
against 288 present.

**Acceptance:**
- `reconstruct_modelled_families.py --build` draws the admitted houses' families after the
  T-2020 folds; `--report` prints the ruling (admitted, standing alone, people added, the
  town against the range, the adult sex ratio and under-ten share before and after);
  `--check` re-derives byte for byte; `--self-test` fires the range cap and the frozen list.
- The order book orders the ruling's fills and the town it converges to is ≤ 3,265.
- The family rows the book still orders (adult men in family houses, family households)
  name a live ticket.
- Visible: the admitted houses' cards show the drawn family; LIBERTIES restated.
- `./tools/check.sh` green.
