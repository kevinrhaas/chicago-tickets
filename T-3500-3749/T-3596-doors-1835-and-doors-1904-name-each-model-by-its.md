---
id: T-3596
title: doors_1835 and doors_1904 name each model by its build inputs, not its file bytes, so a CI re-bake's float noise no longer stales them (the content build's bake gate doors_1835 red)
state: claimed
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: T-3592
opened: 2026-11-14
closed: null
pr: null
claimed_by: run 11/14/2026, 12:07:55 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/43563041861
claimed_at: 2026-11-14T06:07:56.691Z
decision: null
decision_answer: null
---

doors_1835 and doors_1904 name each model by its build inputs, not its file bytes, so a CI re-bake's float noise no longer stales them (the content build's bake gate doors_1835 red).

Piece 1 of 2 of **T-3592 — dev's remaining content-build reds after the smoke 14/15 fix: bake gate 7/8 doors_1835 stale after the CI bake (derive_doors_scene.py), mobile 6-7's compass-and-map instrument, mobile 13's Auto/Sound, Researcher and HUD-coverage checks; desktop 14's Go-to key check re-read on a fresh build**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

## SPLIT WHILE WORK STOOD ON THE PARENT

When T-3592 was split (2026-11-14T06:07:41.013Z), this was already on it. Read it before you claim this piece, and check the PR list for a branch that has already taken it:

- claim — taken 1m ago, run 11/14/2026, 12:07:36 AM CT (https://github.com/kevinrhaas/polecat-platform/actions/runs/43563041861) — held by the run that split it

The run that split it (https://github.com/kevinrhaas/polecat-platform/actions/runs/43563041861) may be working one of the pieces now.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)
