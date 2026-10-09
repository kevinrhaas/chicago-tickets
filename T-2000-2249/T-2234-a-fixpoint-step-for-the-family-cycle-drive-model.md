---
id: T-2234
title: A fixpoint step for the family cycle: drive modelled families, women and children, the trade households, the re-family moves, the order book and the re-family rule until a lap moves nothing, so a sex reading that withdraws a modelled family can land (T-2232, T-2185 and T-2233 wait on it)
state: done
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-08
closed: 2026-10-08
pr: 555
claimed_by: run 10/8/2026, 8:48:28 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-09T04:22:32Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37870757569
claimed_at: 2026-10-09T01:48:28.723Z
decision: null
decision_answer: null
---

A fixpoint step for the family cycle: drive modelled families, women and children, the trade households, the re-family moves, the order book and the re-family rule until a lap moves nothing, so a sex reading that withdraws a modelled family can land (T-2232, T-2185 and T-2233 wait on it).

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 149 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> the machinery is shared by T-2232, T-2185 and T-2233 and belongs to none of them; three runs (T-2185's first attempt, #554's author, and this lap of #554) have each rediscovered the same refusal chain, so one ticket for the step lets all three wait on it instead of each run rebuilding the diagnosis

## FILED ABOVE BAND 9, BECAUSE IT BLOCKS

A follow-up goes to the foot of band 9 unless dev's gate is red on it or the build in hand cannot finish without it (owner, 2026-09-27). This one was placed above band 9 on this reason:

> T-2232's branch (#554) cannot re-derive: the flips re-deal 23 of the 124 women-and-children houses and no step iterates the cycle that follows

**Acceptance:** on PR #554's branch (`steward/t2230-noble-brides`, T-2232) merged over dev, one command takes the derived layer from "the sex pass has run" to a state where `reconstruct_modelled_families.py --check`, `reconstruct_women_children.py --check`, `reconstruct_trade_households.py --check`, `refamily_moves_1835.py --check`, `build_order_book_1835.py --check` (live-owner gate ON) and `model_refamily_rule.py --check` all pass, and a further lap of it changes no byte. It is a manifest step (or a manifest-declared cycle) that `rederive.mjs --tail` runs, its own self-test proves it stops on a lap that moves nothing and refuses one that oscillates, and `check.sh` stays green on dev with it in. Landing T-2232 itself is NOT this ticket: it is the demonstration case. Whoever builds this hands #554 the step and lets the next lap land it.

## What the lap of #554 measured (2026-10-09, slice 4/5)

The lap merged dev (35dae52ea) into #554's head 6420210e. The only conflict was the changelog. Then it ran the chain by hand.

- **The first pass crashes before the cycle starts.** `reconstruct_modelled_families.py --build` unlinks the printed wife's card (`hh_wesencraft_charlotte`) and then calls `build_order_book_1835.cmd_build`. That call reads `data/residents/index.json`, which still lists her, so `adult_men_on_the_cards` raises `FileNotFoundError`. Running `rebuild_resident_index.py --write` and then a second `--build` gets past it. The step should rebuild the index between the stages. (T-2190's Ingersoll fold met the same thing once and never again, because his bride's card was already gone.)
- **The flips re-deal the women-and-children layer.** Measured in memory with the rule's moves switched off (`fill()` over `unfolded()`), the new deal changes the composition of **23 of the 124** houses, and it adds 2 new ones: `hh_rc_kelly_johanna` and `hh_rc_walsh_honora`. Examples: `hh_rc_gilbert_abigail` goes from 4 to 3 people, `hh_rc_dufresne_therese` from a 30s mother with an under-10 son to a 20s mother with a 10-19 son, and `hh_rc_carroll_ellen` loses a daughter. The draw is sequential and seeded, so one freed cell moves every draw after it.
- **So every reader of the old deal refuses**, each for its own good reason:
  - The committed rule's moves name the old houses: "the rule re-families 3 of the 3 people on hh_rc_gilbert_abigail", and later the same for dufresne_therese.
  - With the rule set aside, the stage deals. Then the book's live-owner gate refuses: 2 left in `persons/female/20_29/north/family/none` and in `persons/male/under_10/north/family/none`, both owned by the done T-1174. The moves are what filled those cells.
  - `reconstruct_trade_households.py` refuses: "52 heads re-familied and 50 cards carry a move".
  - `refamily_moves_1835.py` refuses: "two household cards answer to hh_rc_walsh_honora". The T-2020 fold file still folds her into `hh_blake_edio_l`, so modelled families has to re-pair before anything else can read the layer.
- **Ad hoc laps diverge. Do not repeat this.** Six laps of index, families, index, women-and-children (falling back to no rule when refused), trades, index, moves, book (gate off) and rule (`--build`) did not settle. Each refused stage writes part of its output before it refuses, so the laps compound. `persons/female/20_29/north/family/none` climbed 32, 34, 38, 42, 46, 50 against an order of 16, and every lap folded `hh_rc_parmelee_almira` into a different husband.
- **Two things the step needs:**
  - Snapshot hygiene. Restore the tree on any refusal mid-lap, or write nothing until the lap settles.
  - A defined first lap. The design question is whether women-and-children deals before the rule is rebuilt (moves applied last, so a second build with the new rule deals the same houses), with modelled families re-pairing between laps.

  `reconstruct_residents_1835.py --stage` is only a dispatcher. It holds no order for this cycle, so it is no help.
