---
id: T-3292
title: 1912 Prairie's principal floor arched as its pictures draw it: the south gable's pair round-headed, and the door set in a deep round-arched recess with a moulded voussoir ring
state: done
epic: SOUTH_TIME
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-1900
opened: 2026-11-01
closed: 2026-11-01
pr: 1572
claimed_by: run 11/1/2026, 8:12:33 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-11-01T15:10:18Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/41314236215
claimed_at: 2026-11-01T14:12:34.482Z
decision: null
decision_answer: null
---

1912 Prairie's principal floor arched as its pictures draw it: the south gable's pair round-headed, and the door set in a deep round-arched recess with a moulded voussoir ring.

Piece 1 of 3 of **T-1900 — Finish 1912 Moulton-Lowden Chateauesque house architecture**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-1900 was split (2026-11-01T14:12:20.554Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 3m ago, run 11/1/2026, 8:09:37 AM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/41314236215) — held by the run that split it
- branch `steward/t1900-1912-arched-entrance` — the splitter's own

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/41314236215) may be working one of the pieces now.

## Image gate stays on T-1900

T-1900 carries an `## Image gate` section. The last of these pieces to close is refused (`done`) until every building it names matches every one of its reference views, so a slice that leaves a difference open says so in the match record.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

1. `moulton_lowden_house_1912_prairie` rebaked with the south gable's principal-floor pair as two round-headed lights (K06 `sash_paired_round`) and the door in a deep round-arched recess (K07 `double_door_deep_arch`) under a moulded voussoir ring, sized off the photograph through its solved camera.
2. All three reference views re-rendered with `tools/photo_match.mjs`; each match record's arched-pair and entrance differences re-ruled against the new side-by-side (fixed, or still open with what remains), no other verdict changed without reason.
3. The reconstructed parts (leaves, reveal depth, moulding) recorded as a liberty; `check.sh` green; smoke legs `--for-diff` names, desktop and mobile.
