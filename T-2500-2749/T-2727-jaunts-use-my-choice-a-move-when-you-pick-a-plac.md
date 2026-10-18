---
id: T-2727
title: Jaunts use my choice: a Move › When you pick a place switch, off by default, so every Jaunt travels the way it recommends unless the visitor turns it on (replaces T-2652's hidden arriveChosen rule)
state: done
epic: META
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-10-17
closed: 2026-10-18
pr: 984
claimed_by: run 10/17/2026, 1:08:50 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-18T08:49:24Z
claimed_run: null
claimed_at: 2026-10-17T18:08:50.519Z
decision: null
decision_answer: null
---

Jaunts use my choice: a Move › When you pick a place switch, off by default, so every Jaunt travels the way it recommends unless the visitor turns it on (replaces T-2652's hidden arriveChosen rule).

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 141 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> owner request 2026-10-17 on #960: make the Jaunt travel rule a visible setting; default recommended

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## Owner's call (2026-10-17, on #960)
"for 960 can you add that as an option/setting for the user?" — then chose: a toggle, default recommended.

## Acceptance
- [ ] Move › "When you pick a place" carries a switch, **Jaunts use my choice**, off by default (new key in `chicago4d.settings`, e.g. `jauntsFollowChoice: false`).
- [ ] Off: every Jaunt travels by its own recommended mode (getting-there.js § jauntModeFor), whatever the getting-there choice. On: every Jaunt uses the visitor's getting-there choice, except a Jaunt that cannot be travelled that way, which keeps its own and says so.
- [ ] T-2652's `arriveChosen` rule (recommended until the visitor first picks) is retired; the settings note under the choice says plainly what the switch does, in string-table words (check_strings clean).
- [ ] Persisted and restored across reloads and destinations like the other Move settings; storage refused or corrupt falls back to off.
- [ ] Unit test for both states and the can't-travel-that-way fallback; a marked smoke check (part 13) flips the switch and reads a Jaunt's mode both ways.
- [ ] Works at 390×780 and on desktop, all four skins, reduced motion; no ids or snake_case visible.
- [ ] `changelog.d/T-2727.json` entry says what a visitor will see.
