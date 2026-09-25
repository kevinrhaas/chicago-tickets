---
id: T-1585
title: Spend the 159 unasserted BUILDING readings the newspapers, books, directories, civic and church corpora hold: a roof, a church, a school house, a store or a fort quarter a source names, read against the address book and the structure layer T-1198's chain finished, and each one asserted, limited or refused
state: split
epic: META
requested_by: loop
seen: false
effort: L
legacy_id: null
parent: null
opened: 2026-09-25
closed: 2026-09-25
pr: null
claimed_by: null
blocked_on: null
needs_bake: false
closed_at: 2026-09-25T23:14:10.078Z
claimed_run: null
claimed_at: null
decision: null
decision_answer: null
---

Spend the 159 unasserted BUILDING readings the newspapers, books, directories, civic and church corpora hold: a roof, a church, a school house, a store or a fort quarter a source names, read against the address book and the structure layer T-1198's chain finished, and each one asserted, limited or refused.

**Acceptance:**

1. Each of the 159 `building` readings — 122 newspapers, 28 books, 6 directories, 2 civic,
   1 church — is read against `data/reconstruction/1835_address_book.json` and the
   structure layer, and ends in ONE of three states, stated per unit:
   **asserted** onto a structured field that names its source; **limited**, with the
   clause that stopped it (the L-series limit vocabulary), where the reading places
   something the ground cannot receive; or **refused**, naming rule and evidence.
2. No unit is closed by a rename. A unit that still waits on work names a LIVE ticket
   whose acceptance owns it; a unit that waits on a document nobody holds names no
   ticket and states `awaiting_evidence` (the hand-off contract in
   `data/research/residents/spend_rulings.json`'s `_doc`).
3. `python3 tools/measure_research_spend.py --check` is green, and the count it reports
   for this corpus goes DOWN by the number this ticket spends — stated in the PR.
4. Nothing here invents a coordinate, a source or a confidence. Rule 1 of AGENTS.md binds.

**159 units is more than one run's demonstration, so this was filed `L` and cut by
corpus in the same run:** T-1589 takes the 122 readings in the Chicago Democrat and the
Chicago American, T-1590 the 37 in the books, directories, civic and church corpora.
Between them they spend every unit that points at this parent, which is what keeps the
chain honest — the failure this repair is for (T-1198) was a parent whose children spent
a different corpus, so the chain could close with all 270 units untouched.

## Why this ticket exists

`tools/research_spend_ledger.py` routes every unasserted reading to the live ticket
whose acceptance owns it. Until 2026-09-25 the `building`, `street` and
`infrastructure` place claims all named **T-1198** — "the seating pass owns this
unasserted place claim" — on the ground that there was *no seat on the ground to
carry a place claim*. T-1198 was split into T-1491, T-1492 and T-1493 and the whole
chain closed (the last live leaf, T-1523, settled `done` at 22:35Z on 2026-09-25),
so 270 units were deferring to finished work and `check.sh` went red on four steps
for every open PR. T-1584 is that repair.

**And the reason for the deferral has changed, which is why this is a SPEND and not a
rename.** T-1491 wrote the address book, T-1492's chain seated the reach and T-1493
made a seat navigable, so the seat these readings were waiting for now EXISTS. What
they still need is nobody's rename: it is somebody READING them against the layer,
one at a time — the same argument T-1569 makes for the twelve civic posts, and the
same shape as T-1315 (births) and T-1335 (kin).

