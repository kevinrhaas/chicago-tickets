---
id: T-1969
title: The budgets re-measured and set: detail ceilings at every stand, the draw-call budget, the boot payload, T-1154 reconciled, smoke green at both viewports
state: open
epic: TOWN
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-1215
opened: 2026-10-02
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

The budgets re-measured and set: detail ceilings at every stand, the draw-call budget, the boot payload, T-1154 reconciled, smoke green at both viewports.

Piece 6 of 7 of **T-1215 — Converge the reconstructed town: every person housed, every business roofed, every roof occupied or its use stated, the census's dwellings ratio met, the programme reconciled, the budgets re-measured and set — the completion report a visitor can open**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

## Dev's boot payload is over budget (2026-10-02)

- `node tools/measure_boot_payload.mjs --check` on a published mirror of dev @ 072b2681 measured **14.226 MB** across 1285 requests, against 12.000 MB (docs/SITE-BUDGET.md §4). PR #258's CI leg `smoke (desktop, 1-2)` refused on the same check at 12.931 MB.
- Dev's own gate does not run smoke, so the overrun landed unnoticed. The morning's texture-binding merges (T-1815 #264, T-1963 #271) are the likely growth. That is inferred and has not been bisected.
- Every baked PR's desktop part 1 stays red until this is back under budget. Moved to band 0 on the owner's word ("yes move them up").
