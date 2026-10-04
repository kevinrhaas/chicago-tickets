---
id: T-2076
title: Two printings of one letter-list name reach the mint as two candidates and only the first-ranked is read: union them, or say per card why not (hh_palmer_n_h's surname-first reprint, hh_elliot_william and hh_wilson_john's letter counts read as name tokens; a trial union moves 85 cards)
state: claimed
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-04
closed: null
pr: null
claimed_by: run 10/4/2026, 7:02:11 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37200569548
claimed_at: 2026-10-04T12:02:11.379Z
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
