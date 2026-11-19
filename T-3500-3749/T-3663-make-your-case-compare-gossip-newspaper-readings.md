---
id: T-3663
title: Make your case: compare Gossip newspaper readings and save a cited answer
state: claimed
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-18
closed: null
pr: null
claimed_by: gossip-investigation-owner-request 11/18/2026, 8:48:18 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-19T02:48:20.044Z
decision: null
decision_answer: null
---

Make your case: compare Gossip newspaper readings and save a cited answer.

## Owner request and bounded scope

The owner supplied “4D Chicago: features that would make it compelling” (17 November 2026), including #8 “Mysteries with sources”: “Short investigations: a question, three people to question, two documents to read, a claim to make with its evidence.” The active request prioritizes no-new-server work, periodic reviewable PRs and DEV merges only when green. This is the first bounded investigation case after T-3656/T-3657/T-3658, delivered separately and not merged before their current PR #2197 lands green.

Attach optional, initially collapsed “Make your case” to the existing eligible Gossip or Printed Notice? completion. Use its two real newspaper readings and three cited evidence records (land-sale, bank-branch, bank-springfield). Do not invent three witnesses or add a mystery engine, route, schema, service, scan, source link or automatic additional world. Preserve ordinary optional reflection.

**Acceptance:** One completed Gossip outing offers a claim/evidence/uncertainty comparison that the visitor can review and explicitly save to the existing field notebook.

1. All five eligible completed tellings use their own compiled evidence; interrupted, incomplete, unvisited, unrelated and unresolved-source cases do not offer the comparison. Questions respect the audience band.
2. Preserve T-2031’s missing second sale figure; the paper’s estimate is not an exact total. Keep the Springfield building reading inferred with its reasoning and the American item’s locator. Rumors and conversations remain liberties. The source review is explanatory, ungraded and revisable.
3. Keep drafts only within the completed session until explicit Save. Same-session repaint retains the draft; dismiss/replay/new session clears it. Report empty/full/damaged/unavailable storage and repeated saves without dropping a draft or earlier entries.
4. Notebook display, HTML download and print retain the student’s claim, selected evidence, uncertainty, both source identities, locators and inference reasoning. Escape student HTML and never invent source links.
5. Verify keyboard/mobile controls, visible focus, status announcements and readable magnification/export at 390×780 and 1280×800. Run focused behavior checks first; full source/preflight and required published browser gates remain required before merge. Local heavy gates wait until the current release renderer releases CPU.

## Historical authority

Canonical `data/jaunts/gossip-or-notice.json` and its four audience versions; source IDs `chicago_democrat_1833_1835` and `chicago_american_1835`; evidence IDs `land-sale`, `bank-branch`, `bank-springfield`. T-2031/PR #355 and T-2040/PR #362 establish the reading. Do not use the extraction’s rejected `[Six Hund]red` normalization. The American branch decision is not proof of an operating Chicago bank. Both records are text-only with no public source URL.

## Implementation boundaries

New isolated worktree `/workspace/chicago-investigation`, based on `3472ec872d00e33761490b0138b23da1c63daee2`. Ticket changes use a separate real clone at `/workspace/chicago-investigation-tickets`. Current release checkout, frozen published mirror and shared origin/dev ref remain untouched. Source and published validation are pending; no full gate has run for this ticket.
