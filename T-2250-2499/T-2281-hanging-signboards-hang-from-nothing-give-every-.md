---
id: T-2281
title: Hanging signboards hang from nothing: give every hung board real iron hangers (chain to its bracket, hood or arm)
state: claimed
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-09
closed: null
pr: null
claimed_by: run 10/9/2026, 10:13:25 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-10T03:13:25.499Z
decision: null
decision_answer: null
---

Hanging signboards hang from nothing: give every hung board real iron hangers (chain to its bracket, hood or arm).

**Owner report (2026-10-10, Sauganash Hotel screenshot):** "there are hanging signs all over and they are missing a chain or rope or something I think the signs hang in the air with nothing supporting them".

**Cause:** `signage.js` `bracket_board` runs ONE arm out of the wall at the board's middle and drops the two hanger straps at ±0.32 of the board's width ALONG the wall, so neither strap is under the arm: both end in the air. The awning and post mountings put their straps under timber, but as flat timber slats rather than ironwork.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
- Every hung board (bracket, awning, post) hangs on iron chain whose top link meets the timber that carries it and whose bottom link meets an iron staple on the board.
- A bracket board has an arm over each chain, each carried by a diagonal knee brace from the wall.
- The ironwork samples a dark iron cell in the sign atlas, not the timber.
- Every sign stays inside its own declared reach; check.sh green; phone 390×780 renders with no page error.
