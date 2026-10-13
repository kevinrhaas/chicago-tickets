---
id: T-2483
title: dev's gate is red on the site budget since #783: the prairie-1904 reference browser is shipped twice again (site/4d 33.58 -> 72.97 MB, published tree 279.2 MB of 256 MB)
state: open
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-13
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

dev's gate is red on the site budget since #783: the prairie-1904 reference browser is shipped twice again (site/4d 33.58 -> 72.97 MB, published tree 279.2 MB of 256 MB).

## FILED ABOVE BAND 9, BECAUSE IT BLOCKS

A follow-up goes to the foot of band 9 unless dev's gate is red on it or the build in hand cannot finish without it (owner, 2026-09-27). This one was placed above band 9 on this reason:

> dev's gate is red on it from 859179af (dataset step: published tree 279.2 MB over the 256 MB budget); every lapped PR inherits the red

**Evidence (loop, 2026-10-13, from the `gate` job logs on dev):**

- `7d1d50ea` gate green. `52ea8a31` (#776, T-2216) red on two derived counts only (liberties, source-use), both re-derived by the fold `859179af`. At `52ea8a31` the published tree was **239.83 MB** (16.17 MB of headroom), with `site/4d` at 33.58 MB and "reference browsers: **90.71 MB** not shipped twice (T-1828)".
- `859179af` (dev after `2883bd7a` = #783, T-1882's 1800-block street photograph) is red on the `dataset` step: "published tree is **279.2 MB**, over the 256 MB budget". In the same log `site/4d` is **72.97 MB**, the de-duplication reads "**51.41 MB** not shipped twice", and there's a new WARN: "site/4d/prairie-1904/docs is a page directory with no index.html".
- #783 adds about 90 KB of images, so the 39 MB jump has to be the T-1828 de-dup no longer matching the prairie-1904 reference browser (`prairie-1904/research/public/`, 39.30 MB). `site/4d` then ships it a second time. Start with `python3 tools/site_budget.py` on dev.

**Acceptance:** dev's `check.sh` green on the site budget with the prairie-1904 reference browser shipped once (T-1828), and no budget raise.
