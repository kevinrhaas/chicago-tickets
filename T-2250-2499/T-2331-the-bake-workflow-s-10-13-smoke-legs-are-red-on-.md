---
id: T-2331
title: The bake workflow's 10-13 smoke legs are red on dev: the 1904 front-door block reads data/traces/gcp and data/research from source, which the legs' sparse checkout (tools/ + SITE-BUDGET.md only) does not carry, so the part ends ENOENT; three sward arrival checks fail beside it
state: done
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-10-10
closed: 2026-10-10
pr: 670
claimed_by: run 10/10/2026, 5:15:46 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-10T23:40:20Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38090572023
claimed_at: 2026-10-10T22:15:46.311Z
decision: null
decision_answer: null
---

The bake workflow's 10-13 smoke legs are red on dev: the 1904 front-door block reads data/traces/gcp and data/research from source, which the legs' sparse checkout (tools/ + SITE-BUDGET.md only) does not carry, so the part ends ENOENT; three sward arrival checks fail beside it.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## Evidence (filed by a lap of chicago#666, 2026-10-10)

- dev's own bake run 38085627738 (push to dev, 20:55Z) — `smoke (mobile, 10-13)` failed,
  239 passed, 4 failed; PR runs on #662, #663 and #666 fail the same four:
  1. `the suite body ran to completion — Error: ENOENT … chicago/4d/data/traces/gcp/sanborn_1911_v3_sheet_28_gcps.json`
     — `tools/smoke_renderer.mjs` ~L16051 (`readRepo`, the T-1739 front-door block) reads
     `data/traces/gcp/` and `data/research/glessner_house_1904_spec.json` from the source tree,
     but `.github/workflows/chicago-4d-bake.yml` § smoke checks out only `/chicago/4d/tools/`
     and `/chicago/4d/docs/SITE-BUDGET.md` (T-0437). The foreground steward smoke runs on a
     full clone, so it never sees this.
  2. `no sward species its own list owes a plant to is drawn nowhere` (z09_sand_prairie.forb.asclepias_tuberosa)
  3. `a plant in front of the walker never arrives already visible` — 0 arrivals
  4. `a plant is drawn at its own height, faint, never short` — 0 arrivals
- Two repairs to weigh: read those two files from the published mirror (or a committed copy
  under tools/), or widen the sparse set — the latter is a workflow edit, owner-visible.
  Whether 2-4 are the same environment gap or a real sward regression is unknown.
- **What the ENOENT hides, measured:** T-2323 (#668) placed `shortall_gregory_house_1638_prairie_front`
  in the 1904 scene without adding it to `PLACED_1904` (smoke part 13). No CI leg reaches that check,
  so dev went red there without anyone seeing it. #666 (T-2321) carries the fix. With it, mobile
  part 13 on the merged tree passes 126/0 on a full clone. Until this ticket lands, every PR that
  places a 1904 structure must prove part 13 in the foreground.
