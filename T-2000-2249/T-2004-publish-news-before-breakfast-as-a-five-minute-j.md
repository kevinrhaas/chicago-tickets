---
id: T-2004
title: Publish News Before Breakfast as a five-minute jaunt
state: done
epic: RENDERING
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-1266
opened: 2026-10-02
closed: 2026-10-02
pr: 319
claimed_by: run 10/2/2026, 8:49:06 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-03T02:42:44Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37087343214
claimed_at: 2026-10-03T01:49:06.391Z
decision: null
decision_answer: null
---

Publish News Before Breakfast as a five-minute jaunt.

Piece 1 of 4 of **T-1266 — Publish news, mail, lodging and work jaunts**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

The parent's batch spec for this piece, verbatim in substance:

**07. News Before Breakfast** (`news-before-breakfast`) — Newspapers · Walk · A Useful Clipping (News & Knowledge) — [brief](../../chicago/4d/docs/JAUNTS-INITIAL-LIBRARY.md#07-news-before-breakfast)
- Stops: `sauganash_hotel` → `chicago_democrat_office` → `chicago_american_office` → `exchange_coffee_house`
- Play: choose a question; read one short item from each paper; tell reporting from an advertisement; keep a clipping.
- Cautions: only issue-dated, page-and-column-located items eligible on the scene date; later news is not current.

1. `data/jaunts/news-before-breakfast.json` compiles `available` (`compile_jaunts.py` in `check.sh`); every destination, source and locator resolves; every path reaches an ending.
2. `node tools/play_jaunt.mjs news-before-breakfast --all-paths` walks every choice with no dead end and no double keepsake.
3. Primary path measured at Walk and a faster mode, beside the card's estimate, in the PR.
4. Shared authoring rule from T-1266 holds for every stop (25–60 words, tiered sentences, LIBERTIES lines for invented connective text, no quotation in a named person's mouth, nothing after 1 July 1835 as present).
5. Diff is content only: the jaunt file, LIBERTIES lines, the regenerated catalog/sidecars, the changelog entry.
