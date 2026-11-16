---
id: T-3610
title: dev's first-visit boot payload is 45.437 MB, over the 45.2 MB budget — every content build's desktop 1-2 leg is red
state: withdrawn
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-15
closed: 2026-11-15
pr: null
claimed_by: null
blocked_on: duplicate of T-3609: the same 45.437 MB reading on dev, already re-budgeted 45.2 → 45.7 MB under SITE-BUDGET.md § 4o by #2095 (merged 2026-11-16 04:23Z)
needs_bake: false
closed_at: 2026-11-16T05:20:50.906Z
claimed_run: null
claimed_at: null
decision: null
decision_answer: null
---

dev's first-visit boot payload is 45.437 MB, over the 45.2 MB budget — every content build's desktop 1-2 leg is red.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## Evidence (filed by steward slice 3/5, 2026-11-16)

- `node tools/measure_boot_payload.mjs` on the published mirror of dev `f8d77b48b`: **45.437 MB** across 1238 requests. The budget is 45.2 MB (docs/SITE-BUDGET.md § 4n, T-3599).
- Content build runs 43776871651 (#2089), 43781261707 (#2080) and the #2080 lap all went red on `smoke (desktop, 1-2)` › *Enforce the first-visit boot payload budget*, at 45.429 MB. Those PRs changed only 1904 GLBs, which the 1835 first visit does not load, so both were merged blind with that reasoning on the PR.
- Heaviest folder: `/data/prebuilt/1835/` at 25.86 MB. Use `--entries`/`--against` against a reading from before T-3599 to find what grew since 2026-11-14.
