---
id: T-1588
title: Spend the two landholding enrichments T-1301 routed to T-1198: wright_john_s's Chicago land purchases and original-town lots and kingston_paul's Chicago landholding, written onto the held cards by a field that says what a person held — the same shape as T-1315, T-1335 and T-1569 for the births, the kin and the posts
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

Spend the two landholding enrichments T-1301 routed to T-1198: wright_john_s's Chicago land purchases and original-town lots and kingston_paul's Chicago landholding, written onto the held cards by a field that says what a person held — the same shape as T-1315, T-1335 and T-1569 for the births, the kin and the posts.

**Acceptance:**

1. Both units are read with the other sources on their card beside them, not out of the
   one pass that found them:
   - `residents:data/research/residents/pass_05_75_cohort.json#people/wright_john_s` —
     the CPL finding aid and the 1885 *In Memoriam* identify John S. Wright's Chicago
     land purchases and original-town lots (`cpl_john_s_wright_papers`,
     `wright_in_memoriam_1885`).
   - `residents:data/research/residents/pass_11_75_cohort.json#people/kingston_paul` —
     early-Chicago sources identify Paul Kingston as a Chicago landholder and a Racine
     old-settlers record dates his departure from Chicago to 2 January 1835
     (`rr_andreas_chicago_1884_pass11`, `rr_racine_old_settlers_1871`). The DEPARTURE
     half is T-1354's field, not this ticket's.
2. Decide the field before writing it. If no field on a resident card says what a person
   HELD, say so and either add one with its confidence and source list or refuse both
   readings in writing — a landholding written into a prose note is the drift rule 2 of
   AGENTS.md exists to stop.
3. `python3 tools/measure_research_spend.py --check` green; `the_enrichment_names_a_landholding_no_field_carries`
   either empties or the two units read `asserted`.
4. Nobody is minted and no confidence moves to make this pass.

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

