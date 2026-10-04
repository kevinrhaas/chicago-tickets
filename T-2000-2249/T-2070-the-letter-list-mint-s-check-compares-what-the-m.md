---
id: T-2070
title: The letter-list mint's --check compares what the mint owns, names in the file which keys a later pass owns and why, and runs green in check.sh against a shrink-only ledger of the drift still to be read
state: review
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: T-1222
opened: 2026-10-04
closed: null
pr: 393
claimed_by: run 10/4/2026, 2:31:57 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37185846396
claimed_at: 2026-10-04T07:31:57.195Z
decision: null
decision_answer: null
---

The letter-list mint's --check compares what the mint owns, names in the file which keys a later pass owns and why, and runs green in check.sh against a shrink-only ledger of the drift still to be read.

Piece 1 of 4 of **T-1222 — Read the letter-list mint's 798-file drift and give the pass a check the gate can run at its own place in the pipeline**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

- `tools/mint_letter_list_residents.py --check` compares what the mint OWNS — which
  households it holds (gained, lost, re-minted under a new id) and, on a card both
  sides hold, the keys it derives — and nothing else. The file states, key by key,
  which keys a later pass owns and why, and a key that moved and is on NEITHER list
  is drift, never a default.
- The drift that stands on the day it lands is written down, row by row, in a ledger
  each row of which names its class, the keys that moved and the sibling ticket that
  reads it (T-2071, T-2072, T-2073). The check is red on any drift NOT in the ledger
  and red on any ledger row whose drift no longer stands, so the ledger can only
  shrink and cannot be left standing over a tree that has moved on.
- `check.sh` runs it, green; `check_gate_baseline.json` no longer carries the mint as
  ungated; a self-test breaks the comparison on purpose (an owned key moved, a foreign
  key moved, an unattributed key moved, a stale ledger row) and requires each to fire
  or not fire as it should.
