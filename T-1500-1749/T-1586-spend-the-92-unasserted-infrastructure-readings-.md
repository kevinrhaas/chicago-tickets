---
id: T-1586
title: Spend the 92 unasserted INFRASTRUCTURE readings: the bridges, ferries, wharves, wells, the fort's woodpile, the ward geography and the fire ordinances' apparatus the papers and books print, read against the corridor, yard and structure layers that now exist, and each one asserted, limited or refused
state: open
epic: META
requested_by: loop
seen: false
effort: L
legacy_id: null
parent: null
opened: 2026-09-25
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

Spend the 92 unasserted INFRASTRUCTURE readings: the bridges, ferries, wharves, wells, the fort's woodpile, the ward geography and the fire ordinances' apparatus the papers and books print, read against the corridor, yard and structure layers that now exist, and each one asserted, limited or refused.

**Acceptance:**

1. Each of the 92 `infrastructure` readings — 79 newspapers, 10 books, 2 directories,
   1 civic — is read against the corridor, yard and structure layers and ends
   **asserted**, **limited** (with the clause) or **refused** (naming rule and
   evidence), one state per unit and stated.
2. The readings that describe a RULE rather than a thing — the four-ward geography of
   the September 1834 fire ordinance, the hay-stacking limits, the fire warden's
   districts — are ruled on as what they are: town geography the corpus carries, not a
   licence to draw an object. Where such a reading reaches no drawable target it is
   `limited` with that said, never quietly asserted.
3. Nothing is placed on a say-so the source refuses to give. `chicago_democrat_1835_07_01#c018`
   is the standing example: the notice says the wood is piled "at such place near Fort
   Dearborn as will be designated by the Asst. Quartermaster" and therefore licenses no
   woodpile anywhere.
4. `python3 tools/measure_research_spend.py --check` is green and the PR states how many
   units moved and to what.

**Effort L on purpose.** Split before claiming; the natural cut is by what the reading
names (river works and bridges / the fort's supply / the ordinances' town geography).

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

