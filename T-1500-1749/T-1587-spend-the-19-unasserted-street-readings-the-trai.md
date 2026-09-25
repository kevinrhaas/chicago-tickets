---
id: T-1587
title: Spend the 19 unasserted STREET readings: the trails, roads and street lines the papers, Hubbard and Norris name that reach no corridor in the street layer, each one asserted onto the corridor it names, limited to the division it reaches, or refused in writing
state: open
epic: META
requested_by: loop
seen: false
effort: M
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

Spend the 19 unasserted STREET readings: the trails, roads and street lines the papers, Hubbard and Norris name that reach no corridor in the street layer, each one asserted onto the corridor it names, limited to the division it reaches, or refused in writing.

**Acceptance:**

1. Each of the 19 `street` readings — 12 newspapers, 6 books, 1 directory — is read
   against the street and corridor layers and ends **asserted** onto the corridor it
   names, **limited** to the division or reach it gets to, or **refused** in writing.
2. The readings printed in MODERN place-names are refused as 1835 placements and kept
   for what they do say. `hubbard_autobiography_1911#bk_hub_084` is the example the
   corpus already annotates: an 1888–1911 editor's note tracing Hubbard's Trail through
   Homewood, Crete and Momence cannot place a trail on 1835 ground, and the unit's own
   note says so.
3. `python3 tools/measure_research_spend.py --check` is green and the PR states how many
   units moved and to what.

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

