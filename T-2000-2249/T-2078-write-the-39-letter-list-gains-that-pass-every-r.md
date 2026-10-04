---
id: T-2078
title: Write the 39 letter-list gains that pass every refusal read right; the population they add shrinks orders the re-family ledger landed moves in, and the order book faults (a move needs an open order to fill, persons/female/40_49/north/lodging/trade first) — T-1717's finding, which wants its ruling first
state: review
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: T-2072
opened: 2026-10-04
closed: null
pr: 406
claimed_by: run 10/4/2026, 6:03:31 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37197218988
claimed_at: 2026-10-04T11:03:31.647Z
decision: null
decision_answer: null
---

Write the 39 letter-list gains that pass every refusal read right; the population they add shrinks orders the re-family ledger landed moves in, and the order book faults (a move needs an open order to fill, persons/female/40_49/north/lodging/trade first) — T-1717's finding, which wants its ruling first.

Piece 2 of 2 of **T-2072 — Read the 43 people a re-derived letter-list mint would add, on no committed card, and write or refuse each, retiring their ledger rows**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2072 was split (2026-10-04T09:22:39.375Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 13m ago, run 10/4/2026, 4:09:17 AM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/37191087956) — held by the run that split it
- branch `steward/t2072-letter-list-gains` — the splitter's own

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/37191087956) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

## Measured by T-2077's run, 2026-10-04

- **The 39 cards are the mint's own output, unchanged**: `build()` then write `files[path]` for each `gained` row — never the mint's bare write mode, which rewrites all 784 cards and wipes the later passes' keys on 716 of them. `--retire-ledger` then takes the 39 rows.
- **What stops it**: with the 39 written, `node tools/rederive.mjs --run` faults at step 87/178 (`reconstruct_modelled_families.py --build` → `build_order_book_1835.py`): *"the re-family ledger lands 1 head(s) in persons/female/40_49/north/lodging/trade, which orders 0 and already holds 0: a move needs an open order to fill"*. The move is `rc_reilly_johanna` (T-1556/T-1563, from `persons/female/40_49/west/family/trade`). Clean dev runs past step 87. More known households shrink the orders the re-family programme's moves already landed in. That is T-1717's finding from the other side, so the ruling it asks for (how the room is read when the known layer grows under a landed move) comes first.
- **The readings themselves**: 24 of the 39 are on the 1834-03-04 printing of the 1 January 1834 return, completed off the page image (`read_at_image`, scan_verified). 13 are on the 1835-07-01 list, `transcription_mediated` OCR with readings like `Loweley. Watere e` and `Root Ez c.` (the mint keeps readings as printed; suspicions belong in `register_letter_list_suspicions.py`). The other 2 are 1834 printings without an image reading.
- **A display defect on these cards, not this ticket's to fix**: `Eliphalet Atkins 2`, `Julius Perrin 2` and `W. Vanzandt 2` will show as `Atkins [?] Eliphalet` and so on. `display()` reads the office's letter count as an unread initial and flips the order. About 30 committed cards already show it (`Axtell [?] Almond`, `Hills [?] Levi`, …). T-2077 corrected only the REFUSALS for mints (`LETTER_COUNT`). Correcting display and slug moves ids (`John Wilson 4` → `hh_wilson_john` collides) and belongs with the splitter tickets (T-1155, T-1217).
