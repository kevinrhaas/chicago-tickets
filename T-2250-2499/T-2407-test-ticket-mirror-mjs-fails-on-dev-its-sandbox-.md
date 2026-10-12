---
id: T-2407
title: test_ticket_mirror.mjs fails on dev: its sandbox closes T-2369, whose image gate needs tools/image_gate.mjs, which the sandbox does not copy
state: withdrawn
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-12
closed: 2026-10-12
pr: null
claimed_by: null
blocked_on: already fixed on dev by T-2402 (#723): test_ticket_mirror skips image-gated tickets; node tools/test_ticket_mirror.mjs passes on dev 98503e557 (closes T-2404)
needs_bake: false
closed_at: 2026-10-12T08:02:44.335Z
claimed_run: null
claimed_at: null
decision: null
decision_answer: null
---

test_ticket_mirror.mjs fails on dev: its sandbox closes T-2369, whose image gate needs tools/image_gate.mjs, which the sandbox does not copy.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## Finding, 2026-10-12 06:30Z (slice 3 lapping #720)

Probably already fixed by T-2402 (#723, merged 05:34:55Z, 12 minutes before this ticket was filed at 05:47Z from a tree that did not have it yet). On dev 27c565292, `node tools/test_ticket_mirror.mjs` exits 0: the sandbox now closes T-2403, not image-gated T-2369. On #720, rebased onto that dev, CI's `bake` job, which was red on this step, went GREEN. If nothing else reproduces it, withdraw this ticket rather than build it.
