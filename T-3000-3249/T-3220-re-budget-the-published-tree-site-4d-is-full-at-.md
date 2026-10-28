---
id: T-3220
title: Re-budget the published tree: site/4d is full at 416 MiB, so no new textured Prairie house can land (dev ~413.8 MiB; #1384 adds 4.0)
state: open
epic: META
requested_by: loop
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-10-27
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

Re-budget the published tree: site/4d is full at 416 MiB, so no new textured Prairie house can land (dev ~413.8 MiB; #1384 adds 4.0).

## FILED ABOVE BAND 9, BECAUSE IT BLOCKS

A follow-up goes to the foot of band 9 unless dev's gate is red on it or the build in hand cannot finish without it (owner, 2026-09-27). This one was placed above band 9 on this reason:

> PR #1384 (T-3211) is complete and its gate is red only on the 416 MiB site budget: the merged tree publishes 417.774 MiB

## What was measured (2026-10-28, steward run lapping #1384)

- `python3 tools/site_budget.py` on #1384 merged with dev 102a969d2: **417.774 MiB in 5562 files, 100.4 % of the 416 MiB budget**; `validate.py` fails `site: published tree is 417.8 MB, over the 416 MB budget`. Every other step of `check.sh` is green on that tree.
- #1384's published delta is +3.99 MB (1700 and 1706 Prairie's K01 web GLBs, 2.00 MB each, replacing their drafts), so dev alone reads about 413.8 MiB: about 2.2 MiB of headroom, less than any one textured Prairie house (1.5-3.5 MiB web GLB, validate.py's own note).
- The ceiling still has room: T-3170's note puts two 416 MiB allowances plus 129.136 MiB of other site content at 961.136 MiB, 62.864 MiB under the 1 GiB Pages ceiling, so a measured re-budget can reach about 447 MiB a tree. The levers T-3170 measured and did not pull: 66.309 MiB of KTX2 sheets embedded again and again across the houses' GLBs, and 7.18 MB of transport masters no runtime fetch reads.

**Acceptance:** dev's published tree has room for #1384's +4.0 MB with headroom for the next textured house, either by a measured re-budget in `tools/validate.py` (`SITE_BUDGET_MB`, its note, docs/SITE-BUDGET.md) that stays under the Pages ceiling for both trees, or by pulling a lever that hands bytes back; #1384 then re-gated and merged.
