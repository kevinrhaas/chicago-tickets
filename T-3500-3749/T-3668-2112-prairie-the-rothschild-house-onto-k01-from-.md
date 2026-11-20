---
id: T-3668
title: 2112 Prairie, the Rothschild house, onto K01 from the 1911 sheet: the three-storey stone-front brick body, rear two-storey wing, high stoop and repeated masonry openings, and the image-gate sign-off (after the piece before it)
state: open
epic: SOUTH_TIME
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-1921
opened: 2026-11-19
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

2112 Prairie, the Rothschild house, onto K01 from the 1911 sheet: the three-storey stone-front brick body, rear two-storey wing, high stoop and repeated masonry openings, and the image-gate sign-off (after the piece before it).

Piece 2 of 2 of **T-1921 — Refine 2108 Mark Kimball and 2112 Rothschild**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-1921 was split (2026-11-19T10:56:02.870Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 1m ago, run 11/19/2026, 4:55:13 AM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/44508663143) — held by the run that split it

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/44508663143) may be working one of the pieces now.

## Image gate stays on T-1921

T-1921 carries an `## Image gate` section. The last of these pieces to close is refused (`done`) until every building it names matches every one of its reference views, so a slice that leaves a difference open says so in the match record.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

**Released 2026-11-20** (claim of run 11/20/2026, 7:24:27 AM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/44743186764): 2112 is built and gated in PR #2260 (resume: CI still queued). done is refused by T-1921's inherited image gate: 2108's tribune_1898_front still differs on its basement lights (K02 base courses cap them at 0.8 m, no bars). What remains is that kit fix plus the sign-off; 2112 itself needs no rebuild once #2260 merges.

**Released 2026-11-20** (claim of run 11/20/2026, 11:30:15 AM CT, by https://github.com/kevinrhaas/polecat-platform/actions/runs/44761959938): PR #2260 MERGED to dev 2026-11-20 (68382eaf7): 2112 is built and on dev. This run merged dev in, re-stamped 2112's inputs hash and re-derived doors_1904, and the CI gate went 8/8 green. done is still refused by T-1921's inherited image gate: 2108's tribune_1898_front differs on its basement lights (K02 base courses cap them at 0.8 m, no bars). What remains is that kit fix plus the sign-off. Nothing about 2112 needs rebuilding.
