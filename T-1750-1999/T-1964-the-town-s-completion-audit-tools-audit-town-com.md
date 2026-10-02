---
id: T-1964
title: The town's completion audit: tools/audit_town_completion_1835.py measures every join T-1215 names (persons to a dwelling, workers to a workplace, businesses to a roof, roofs to occupants or a stated use) by tier, prints the gaps, and fails check.sh on any dangling id
state: review
epic: TOWN
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-1215
opened: 2026-10-02
closed: null
pr: 275
claimed_by: run 10/2/2026, 7:28:16 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37006354978
claimed_at: 2026-10-02T12:28:16.630Z
decision: null
decision_answer: null
---

The town's completion audit: tools/audit_town_completion_1835.py measures every join T-1215 names (persons to a dwelling, workers to a workplace, businesses to a roof, roofs to occupants or a stated use) by tier, prints the gaps, and fails check.sh on any dangling id.

Piece 1 of 7 of **T-1215 — Converge the reconstructed town: every person housed, every business roofed, every roof occupied or its use stated, the census's dwellings ratio met, the programme reconciled, the budgets re-measured and set — the completion report a visitor can open**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

## Acceptance, as delivered (PR #275, merged 2026-10-02)
`tools/audit_town_completion_1835.py` writes `data/render/town_completion_1835.json`. It counts the four joins of T-1215 clause 1 by tier: housed, at work, roofed, occupied. `--check` in check.sh fails on a stale ledger or ANY dangling id, and `--self-test` breaks one link of each kind and proves each is refused. Gaps are reported, not failed: they are T-1965/T-1966's work. It is placed in derived_manifest.json after town_census.py.
