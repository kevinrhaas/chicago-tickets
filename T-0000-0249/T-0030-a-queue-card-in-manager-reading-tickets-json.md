---
id: T-0030
title: A queue card in Manager reading tickets.json
state: withdrawn
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
opened: 2026-08-17
closed: 2026-10-03
pr: null
claimed_by: null
blocked_on: "obsolete: Manager has it: the 4D Board section (manager.polecat.live js/views/board.js) reads tickets.json and QUEUE.md from chicago-tickets."
needs_bake: false
---

Manager (manager.polecat.live) already parses this project's changelog live. This repo now
publishes tickets/tickets.json into the site mirror — add a Manager card/section that fetches
it and renders the queue (owner-first, states, blocked-on-owner questions), so the owner can
see the board without opening the repo. Scope: the manager repo, its own conventions.

**Acceptance:** the queue visible in Manager against the published URL; read-only is fine.

## Queue cleanup 2026-10-03 (owner: "clean out any tickets that … no longer need to be there or are obsolete")

**Withdrawn as obsolete.** Manager has it: the 4D Board section (manager.polecat.live js/views/board.js) reads tickets.json and QUEUE.md from chicago-tickets.
