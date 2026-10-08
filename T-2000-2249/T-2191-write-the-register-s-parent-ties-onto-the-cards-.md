---
id: T-2191
title: Write the register's parent ties onto the cards the register itself minted: St Mary's mothers and fathers carded by T-1504 (hh_cr_marianne, hh_cr_jaespquaa) and readmitted by T-1172 (Marguerite Malore, François Tranche, Manqua Masqua) whose children the town holds — through the generators that own those cards, reciprocally, nobody minted
state: claimed
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-10-08
closed: null
pr: null
claimed_by: run 10/8/2026, 6:26:46 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37859163314
claimed_at: 2026-10-08T23:26:46.532Z
decision: null
decision_answer: null
---

Write the register's parent ties onto the cards the register itself minted: St Mary's mothers and fathers carded by T-1504 (hh_cr_marianne, hh_cr_jaespquaa) and readmitted by T-1172 (Marguerite Malore, François Tranche, Manqua Masqua) whose children the town holds — through the generators that own those cards, reciprocally, nobody minted.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 149 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> T-1335's family pass found register ties with both ends on a card, where one card is GENERATED (tools/reconstruct_church_register.py, the readmission stage): a hand-written kin row there is overwritten on the next build, and the kin survey's Town reads households/ only, so the ties need the generators taught to carry them; the units are handed here

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## The units T-1335 handed here (2026-10-08)

`tools/spend_family_pass.py` derives these from the register and the cards that claim its
rows; each closes `unresolved` on T-2191 under
`the_family_pass_finds_a_tie_onto_a_card_a_build_writes` in
`data/research/church/spend_rulings.json`. Thirteen units, the generated end in brackets:

- St Mary's 1833-02 mother Marguerite Malore [readmitted hh_marguerite_malore] → Joseph Mayo
- 1833-06 child and father: William Dird [readmitted hh_william_dird] → John David Dird
- 1833-09 mother Mariana Kamenwith [readmitted hh_mariana_kamenwith] → Mary and Catherine Wode
- 1833-10 mother O'Waichiquoi [readmitted hh_o_waichiquoi] → Joseph Létendre
- 1833-12 child and mother: Isabelle Bouchard [readmitted hh_isabelle_bouchard] ↔ Adelaide Bouchard
- 1833-14 and 1833-17 mother Marianne [T-1504 hh_cr_marianne] → Jean Baptiste and Magdeleine Aspam
- 1833-16 father François Tranche [readmitted hh_fran_ois_tranche] → Susanne Tranche
- 1833-18 mother Jaespquaa [T-1504 hh_cr_jaespquaa] → Susanne Vieaux
- 1834-18 father Patrick Wagon [readmitted hh_patrick_wagon] → Cicely Wagon
- 1834-24 mother Manqua Masqua [readmitted hh_manqua_masqua] → Cécile Laframboise

Same shape, off a book and ruled in `data/research/spend_rulings.json` rather than handed
on: Moses & Kirkland's `bk_mose1_012` readmits Jacob Sherrill and his daughter Laura
Adelaide (hh_jacob_sherrill, hh_laura_adelaide_sherrill) — a father-daughter tie with both
ends on readmitted cards. Caton's marriage to her is dated to 1835 only and stays refused.

**Acceptance:** every one of these units closes `asserted` on a reciprocal kin row its
generator writes, or is ruled by that generator with its reason; nobody minted.
