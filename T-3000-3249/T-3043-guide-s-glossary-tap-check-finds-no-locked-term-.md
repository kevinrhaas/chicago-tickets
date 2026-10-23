---
id: T-3043
title: Guide's glossary tap check finds no locked term on Home since its Confidence view tile became a button
state: open
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-10-22
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

Guide's glossary tap check finds no locked term on Home since its Confidence view tile became a button.

Found in the T-3029 smoke run (2026-10-22). The smoke line "Guide's glossary gives the seven
locked terms their lines ... and a term's first appearance explains itself on tap (T-2662)" fails
at both viewports (mobile part 11-12, desktop part 12). It reads
`tap: {"term":null,"shown":false}`: `document.querySelector('#nav-home .locked-term')` finds nothing.

Cause: T-3021 (#1203) made Home's MOVE and CONFIDENCE VIEW tiles buttons. `markTerms`
(renderers/web/js/term-tips.js) skips text inside a control (`INSIDE_CONTROL`), so "Confidence view"
on Home is no longer marked, and Home has no other first appearance of a locked term. The failure
was on dev before T-3029 merged.

**Acceptance:** a locked term's first appearance in the Navigator again shows its line on tap
(either a marked term on Home outside the tile button, or the check pointed at the first appearance
that now exists), and the T-2662 smoke line passes at both viewports. The tap inside a tile must
not both open the tip and the app.
