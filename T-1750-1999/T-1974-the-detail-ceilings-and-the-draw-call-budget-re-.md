---
id: T-1974
title: The detail ceilings and the draw-call budget re-measured at every stand and set where they are defined, T-1154 reconciled, smoke green at both viewports
state: claimed
epic: TOWN
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: T-1969
opened: 2026-10-02
closed: null
pr: null
claimed_by: run 10/2/2026, 9:16:40 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37018377388
claimed_at: 2026-10-02T14:16:40.444Z
decision: null
decision_answer: null
---

The detail ceilings and the draw-call budget re-measured at every stand and set where they are defined, T-1154 reconciled, smoke green at both viewports.

Piece 2 of 2 of **T-1969 — The budgets re-measured and set: detail ceilings at every stand, the draw-call budget, the boot payload, T-1154 reconciled, smoke green at both viewports**, split because the parent needed more than one run's demonstration to be done. The parent keeps the full ask and its links; this ticket owns one slice of it.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

## The boot payload after T-1973 (2026-10-02)

T-1973 took dev's boot payload from **14.269 MB to 11.989 MB** (budget 12 MB): the relief
maps ship as lossless WebP (3.947 → 2.649 MB, pixel-identical, `tools/web_textures.py`)
and the changelog left the boot path (1.03 MB, now imported when the What's-new tab opens).
**The margin is 11 KB**, so the next layer that adds boot bytes will be refused by the
bake's desktop `1-2` leg. The next measured candidate, for this budget pass: 
`data/liberties.json` is **0.555 MB** on the wire, awaited at boot by `main.js`
(`mountLiberties`), though only the Evidence panel and an open provenance card read it, and
the card already redraws when the list arrives late (`popup.setLiberties`). Loading it on
first need (Evidence tab or first card) would leave about 0.57 MB of room. If scene bytes alone
outgrow 12 MB as the town completes, re-set the budget here with its reasons
(docs/SITE-BUDGET.md § 4a). Filed here rather than as a new line: the queue stood at its
ceiling (249 of 140).
