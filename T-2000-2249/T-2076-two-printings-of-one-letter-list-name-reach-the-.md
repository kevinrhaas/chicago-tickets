---
id: T-2076
title: Two printings of one letter-list name reach the mint as two candidates and only the first-ranked is read: union them, or say per card why not (hh_palmer_n_h's surname-first reprint, hh_elliot_william and hh_wilson_john's letter counts read as name tokens; a trial union moves 85 cards)
state: done
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-04
closed: 2026-10-04
pr: 421
claimed_by: run 10/4/2026, 1:28:59 PM CT
blocked_on: "T-2071 — build the union over T-2071's mint-onto-the-standing-card rule (PR #402), which rewrites the same record()/build() path and the same three cards"
needs_bake: false
closed_at: 2026-10-04T20:55:40Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37224423316
claimed_at: 2026-10-04T18:28:59.237Z
decision: null
decision_answer: null
---

Two printings of one letter-list name reach the mint as two candidates and only the first-ranked is read: union them, or say per card why not (hh_palmer_n_h's surname-first reprint, hh_elliot_william and hh_wilson_john's letter counts read as name tokens; a trial union moves 85 cards).

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 191 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> T-2073 reads 27 ledgered cards and must hand three on: their drift is a derivation rule (which printings a card is built from) that a trial measured at 85 cards, which no open ticket owns and which is far larger than one ledger slice

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

**Found by T-2073 (PR #400), 2026-10-04.** Six `rewritten` rows of `data/research/letter_list_mint_ledger.json` are handed here (`handed_on.from: T-2073`, each with its reason):

- `hh_palmer_n_h`: the register has two rows enriching it, `N. H. Palmer` (Democrat 20 May 1835 c013) and `Palmer N. H.` (1 July 1835 c005). The mint reads only the first-ranked one, so the card follows whichever ranks first. Read alone, the 1 July printing loosens the arrival bound from 1835-03-31 to 1835-06-30 and drops the May return. The card's own `last_dated_appearance` already reads 1 July.
- `hh_elliot_william`, `hh_wilson_john`: the 4 March 1834 reprint (c026/c027) prints `Elliot 3` and `Wilson 4`. That is the office's letter count, but the gazetteer reads it as a separate person (`person_william_elliot_3`, `person_john_wilson_4`), so the re-derivation loses that printing.
- `hh_fraser_wm_h`, `hh_provis_joshua`, `hh_vandino_john`: two spellings from two printings of the 1 January 1834 return (28 January c001, 4 March c026/c027). Writing the mint's spelling was tried. The other spelling then stopped resolving to the card and was minted as a second household. T-2071's re-minted rows `hh_frazer_wm_h`, `hh_pruvis_joshua` and `hh_vandine_john` are the other face of these pairs.

A trial rule, "union the gazetteer mentions of every register row enriching the same card", moved **85** cards' mint-owned keys. So this needs deciding as a rule, not card by card.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

## Finding, 2026-10-04 (a run that claimed this and stepped off)

**Measured: the register's `enrich` target is not an identity ruling.** 86 cards have more than
one letter-list register row enriching them; in only 9 do the rows print the same card name
(`display()` of the name, letter count stripped — `Blake, Levi` / `Levi Blake`, `N. H. Palmer` /
`Palmer N. H.`). The other 77 mix OCR variants of one name (`Wm. H. Fraser` / `Wm. H. Frazer`,
`Clark B. Albe[e]` / `Clark B. Albee`) with plainly different people the compiler grouped by
surname (`Allen, William` / `Woodle Allen`, `Amanda Miner` / `Miner, Aaron`, five Smiths, five
Millers). So "union every row enriching the card" — the trial that moved 85 cards — would read
other people's letters onto a card. A defensible rule is narrower: unite rows whose card name is
identical (covers Palmer, `William Elliot 3`, `John Wilson 4`), plus rows on the same target whose
forenames agree and whose surnames are one letter apart (Fraser/Frazer, Provis/Pruvis,
Vandino/Vandine); name the card from the EARLIEST printing, which reproduces all six committed
names. Everything else stays apart, and `--report` should say per card why.

**Why it was not built in that run:** T-2071 (claimed by a live run, draft PR #402) changes
`record()`/`build()` to mint a candidate onto the standing card its `enrich` names — the same code
path this rule lives in — and writes `hh_fraser_wm_h`, `hh_provis_joshua` and `hh_vandino_john`.
Two concurrent rewrites of one function and three cards is a conflict, not parallel work. Build
this on `dev` after T-2071 merges.


## Finding, 2026-10-04 (T-2078) — one more surname-first line, alone on its return

T-2078 wrote 38 of the 39 letter-list gains. The 39th, `Conant Augustus H` (1 January 1834
return), is printed surname first and the mint reads it given-first, so it would mint
`hh_augustus_h_conant` displayed as `Conant Augustus H`; `--gate` refuses both the display
(T-1217) and the id (T-1218). It is not a second printing, but it is the same name-order
question as `hh_palmer_n_h`'s reprint, so it is carried here: its row on
`data/research/letter_list_mint_ledger.json` now names this ticket as its reader. Read the
order (Augustus H. Conant) or refuse the line in writing, and retire the row.
