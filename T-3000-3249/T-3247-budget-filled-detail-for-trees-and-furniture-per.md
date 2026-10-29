---
id: T-3247
title: Budget-filled detail for trees and furniture: per-device instance budget, nearest and view-centre first
state: open
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-29
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

Owner, 2026-10-29 (project thread "Assess other 3D project for reuse"), on the World Labs Marble / Spark assessment: *"ok sounds good lets try it out and roll things back if its not productive, i want to improve things best we can if this will work, but dont want to break things"*. Assessment: https://claude.ai/artifact/S5EdbiYNSKK2QrNLU4kAaW; spike files in the project folder `marble-spark-assessment/`.

Borrowed from Spark's LoD design, without Spark: Spark fills a fixed per-device splat budget (iOS 1.5M, Android 1M,
desktop 2.5M) nearest-first and view-centre-first. `tree-instances.js` instead picks one of three levels by fixed
distance rings, regardless of where the visitor looks.

**What:** give each detail tier a fixed instance budget per level and fill it by priority (projected size, weighted
toward the view centre), for the instanced trees first, then furniture if it pays.

**Acceptance:** at the five smoke stands, phone triangles, draw calls and memory hold or drop; trees within ~30 m in
view keep their nearest level on a phone; no pop visible in a walk down Prairie (before/after video or frames in the PR);
zero page errors at both viewports.
