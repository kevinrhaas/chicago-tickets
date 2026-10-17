---
id: T-2709
title: The page uploads the prebuilt distant base (after T-2693's ground upload): publish.sh writes base.{json,bin.gz} into site/4d/data/prebuilt/1835/, terrain.js batches the file's pieces when its build stamp and heightfield are current and cuts its own otherwise, check_published.mjs refuses a stale one, published-page parity read, and measure_boot_phases --phone quotes the base (0.8 s) before and after with its bytes measured against SITE-BUDGET's 29 MB
state: claimed
epic: RENDERING
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: T-2705
opened: 2026-10-17
closed: null
pr: null
claimed_by: run 10/17/2026, 12:14:17 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/39005177247
claimed_at: 2026-10-17T05:14:17.241Z
decision: null
decision_answer: null
---

The page uploads the prebuilt distant base (after T-2693's ground upload): publish.sh writes base.{json,bin.gz} into site/4d/data/prebuilt/1835/, terrain.js batches the file's pieces when its build stamp and heightfield are current and cuts its own otherwise, check_published.mjs refuses a stale one, published-page parity read, and measure_boot_phases --phone quotes the base (0.8 s) before and after with its bytes measured against SITE-BUDGET's 29 MB.

Piece 1 of 3 of **T-2705 — The page uploads the prebuilt streets, yards and distant base (after T-2693's ground upload): publish.sh writes them into site/4d/data/prebuilt/1835/, each layer batches the file's pieces when its input hash is current and builds in the browser otherwise, check_published.mjs refuses a stale one, and measure_boot_phases --phone quotes streets (1.4 s), yards (4.2 s) and the base (0.8 s) before and after, with SITE-BUDGET re-measured**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-2705 was split (2026-10-17T05:14:07.013Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 1m ago, run 10/17/2026, 12:12:42 AM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/39005177247) — held by the run that split it

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/39005177247) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)
