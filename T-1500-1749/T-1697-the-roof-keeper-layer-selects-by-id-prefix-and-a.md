---
id: T-1697
title: The roof-keeper layer selects by ID PREFIX and a roof's block is a matter of POSITION: recon_1835_west_018, _019 and _021 stand on blk_randolph_clinton and were invisible to T-1685's pass by construction, which will recur in every district where a block's ground and a roof's id disagree
state: withdrawn
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-27
closed: 2026-10-03
pr: null
claimed_by: null
blocked_on: "merged into T-1691"
needs_bake: false
closed_at: 2026-10-03T04:52:33.000Z
claimed_run: null
claimed_at: null
decision: null
decision_answer: null
---

The roof-keeper layer selects by ID PREFIX and a roof's block is a matter of POSITION: recon_1835_west_018, _019 and _021 stand on blk_randolph_clinton and were invisible to T-1685's pass by construction, which will recur in every district where a block's ground and a roof's id disagree.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## Queue cleanup 2026-10-03 (owner: "clean out any tickets that … no longer need to be there or are obsolete")

**Merged into T-1691.** T-1697's prefix-vs-position fix is what lets the keeper layer reach the Lake district (and blk_randolph_clinton) correctly; both fit one run of name_the_keepers_1835.py. Work it there.
