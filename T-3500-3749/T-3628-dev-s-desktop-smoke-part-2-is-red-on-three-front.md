---
id: T-3628
title: Dev's desktop smoke part 2 is red on three frontage counts T-3605's stores grew: 97 hitching posts and 97 business-front fittings read where the checks still hard-code sixty and sixty-one, and the five-record frontage check
state: claimed
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-16
closed: null
pr: null
claimed_by: run 11/16/2026, 9:45:12 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/44011455983
claimed_at: 2026-11-17T03:45:13.256Z
decision: null
decision_answer: null
---

Dev's desktop smoke part 2 is red on three frontage counts T-3605's stores grew: 97 hitching posts and 97 business-front fittings read where the checks still hard-code sixty and sixty-one, and the five-record frontage check.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

**Evidence (found by T-3627's run, 2026-11-17):** `SMOKE_VIEWPORT=desktop SMOKE_STAGE=2 node tools/smoke_renderer.mjs --published` on dev `46b34642` plus T-3627's walk-code diff (which touches no frontage record or layer) fails exactly three checks: "the frontage layer lays all five records' walks and stands their posts" (125 walks, 111 crossings, 97 posts, 34 fence runs, 234 walls refused), "the sixty hitching posts stand on their own ground" (97 read, census 97; `smoke_renderer.mjs` ~6678 asserts `=== 60`), and "the sixty-one business-front fittings are drawn at their own fronts" (97 fittings: stoop 84, tie_rail 1, wagon_apron 7, mounting_block 5). `data/frontage/` last moved in d3768c14 (T-3605, 59 stores, 2026-11-16T17:36Z). Re-state the counts from the records (or derive them in the check) rather than hard-coding them.
