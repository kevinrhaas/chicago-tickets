---
id: T-1834
title: Signboards for the reconstructed firms that keep their own roofs: the boarding houses, stores and works the business layer records IN a reconstructed roof get a board in the T-1184 house style, graded reconstructed, the card a tap opens naming the same firm
state: open
epic: TOWN
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-1213
opened: 2026-10-01
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

Signboards for the reconstructed firms that keep their own roofs: the boarding houses, stores and works the business layer records IN a reconstructed roof get a board in the T-1184 house style, graded reconstructed, the card a tap opens naming the same firm.

Piece 1 of 3 of **T-1213 — Signboards for every business that would have hung one: the reconstructed firms' names and trades in period lettering and forms, the attested signs untouched, the signless trades left signless by rule**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

- The signboard rule (`tools/generate_business_signboards.py`) admits a reconstructed roof that
  the business layer (`data/businesses/index.json`) records a reconstructed firm IN
  (`where.kind: premises`, present on the scene date). Its board is worded from that firm's
  own record in the T-1184 house style — the proprietor as the firm style prints him or her
  on line 1, the trade in the period's words beneath — graded `sign_text_confidence:
  reconstructed`, `trade_confidence: reconstructed`, and hung by the existing class cycles
  (a boarding house as a house, a grocer as a counter, a smith or joiner as a painted works).
- The board's `sign_identity` appears in the board AND in the firm's name, which is the
  firm the card's Use row leads with when the board is tapped (`popup.js` `fromSign`).
- Every attested and inferred board is unchanged (self-test: the 33 existing signs are
  byte-identical); `generate_business_signboards.py --check` and `--prove-locality` green;
  `opening_fit` honoured on every flat board.
- Every reconstructed roof refused is refused in words: no firm in it, or a firm whose trade
  hangs no board.
- No tavern is in scope (no reconstructed firm keeps one), so no device is invented here.
