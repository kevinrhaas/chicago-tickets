---
id: T-2825
title: Visitor-readable research records: liberties, ground, open questions, people and source details name no internal ticket number or record id, in any mode
state: claimed
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-18
closed: null
pr: null
claimed_by: run 10/18/2026, 4:48:06 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-18T21:48:06.619Z
decision: null
decision_answer: null
---

Visitor-readable research records: liberties, ground, open questions, people and source details name no internal ticket number or record id, in any mode.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 161 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> owner request 2026-10-18: rewrite the records rather than hide them; no internal ticket numbers or record ids in visitor, researcher or educator views

## Owner's ruling (2026-10-18)

"You should rewrite the records so you are not referring to internal ticket numbers or internal
record ids in researcher or educator mode." The records are rewritten, not hidden. That applies in
every mode a person reads (visitor, Researcher mode, the teacher handout). It supersedes T-2657's
original scope, under which Researcher mode would bring back ticket references and source ids.

## Found so far (T-2667's survey on claude/t2667-guide-about; T-2668's lint)
- Liberties: 492 of 623 entries cite ticket numbers.
- Ground (1835, 1904), open questions and the town's people carry "tier" and ticket references.
  The people topic has a "the ticket that owns it" column.
- Source detail views show record ids and locators.
- The Shops & work card's location lines name structure ids, and a few name ticket numbers. The 17
  lines for firms not trading at the scene date cite newspaper claim ids.
- Four civic-office Go to notes (post office, county offices, Indian agency, land office) cite
  research ids, data/exclusions.json and docs/RESEARCH/hogan_store.md. They are allowlisted in
  tools/check_visitor_ui.py under T-2657, and the allowlist moves to this ticket.

## How
- docs/LIBERTIES.md is append-only (AGENTS.md). Rewrite at the compile step that produces what a
  person reads, or append corrected wording as the project's rules allow. Never edit history.
- An id becomes the thing it names: a building's display name, a source's human title (as
  Inspect's Sources tab already does), or plain words. A ticket reference becomes what the work
  is ("waits for the 1835 resident seating"), or is dropped where it carries nothing for a reader.
- Provenance is kept: the evidence a record rests on is still named, by title.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- [ ] No ticket number (T-NNNN) and no internal record id or snake_case id appears in any text a person can open: hub topics and their entries, Inspect, Go to, cards, the teacher handout, and Researcher mode.
- [ ] tools/check_visitor_ui.py covers the compiled data these surfaces render, not just the string table and page. The Researcher-mode exemption no longer admits ticket numbers or record ids, and the allowlist is empty or every entry names a surface still being fixed.
- [ ] Every rewritten line still names its evidence by a human title; nothing is dropped that a reader needs to judge the claim.
- [ ] The 390x780 mobile smoke passes, and the changelog entry says what a reader will see.
