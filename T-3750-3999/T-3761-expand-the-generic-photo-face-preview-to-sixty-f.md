---
id: T-3761
title: Expand the generic photo-face preview to 256 diverse adults
state: review
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-26
closed: null
pr: 2355
claimed_by: run 11/26/2026, 5:53:12 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-26T11:53:13.893Z
decision: null
decision_answer: null
---

Expand the generic photo-face preview to sixty-four diverse adults.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

Owner scope update: “Then do 256 faces if feasible.” Preserve the original sixteen and add 240 fictional adult sources, with varied apparent ages, skin tones, features and hair. Acceptance is one 256-face library, actual rendered page reviews, deterministic generic-adult assignments, and enforced texture/page residency budgets. Specific historical people follow next. Real low-power GPU whole-town performance must be measured separately; the available software renderer cannot certify it.

**Implemented:** 256 fictional adult faces, 128 men and 128 women, with varied ages/skin tones/features; sixteen bounded review pages; fitted head geometry and face patches; source-guided eyes; one compact crowd atlas and at most one resident-or-loading nearby detail page (10.67 MiB added face textures with mipmaps). Existing hair styles in source-based colours are the review default; scalp-trial hairline/coverage artifacts remain labelled separately. Historical portraits, visitor choices and children retain priority. Specific historical people are next.

**Verified:** All 256 actual heads rendered; selected Full face 189 has exactly two independent before/after figures and 8,694 changed components on its 43,551-component main body mesh. Phone face 256, extracted runnable ZIP, optional scalp trial and single-photo review pass without missing files or browser errors. Every actual scene assignment is checked: 1,048 generic adults on 1,076 bodies use 201 distinct faces; 160 child and 27 personal-face assignments remain protected. Four actual resident models verify real page texture dimensions/UVs through cache changes. A concurrent screenshot attempt timed out; the later run passes. Two actual offline writes reproduce all 325 outputs and repair a damaged last page, preserving read-only inputs. Photo import/budget/cache/skin/variation/LOD tests pass. Dataset: zero errors, 345 warnings. Charles appearance controls pass. Local preflight 2/8: 182 passing steps plus PR-only checks. Complete CI and published renderer stages 2–15 remain outstanding. The measured browser is SwiftShader software; measurement/export testing is not a real low-power-GPU whole-town qualification. Default rollout remains pending.

**Code:** chicago PR #2355, head 839e28cfa58769d5d5cc512ac5719f2f2a3c9108.
**Evidence and runnable viewer:**
https://github.com/kevinrhaas/chicago-evidence/tree/86c4851431974d5c9ed6dac8db10bbd6de830563/evidence/photo-face-library-256-T-3761
