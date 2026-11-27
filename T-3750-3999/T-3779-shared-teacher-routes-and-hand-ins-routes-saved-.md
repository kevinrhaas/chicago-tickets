---
id: T-3779
title: Shared teacher routes and hand-ins: routes saved to the teacher's account, assigned to a class, and answers handed in without a download (the rest of classroom feature 11)
state: open
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-26
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

Shared teacher routes and hand-ins: routes saved to the teacher's account, assigned to a class, and answers handed in without a download (the rest of classroom feature 11).

**Acceptance:** Builds on T-3672's teacher routes and T-3778's classes. A teacher's routes save to their account (list, rename, duplicate, delete), and **Assign to class** puts a route at the top of each class member's Jaunts with the teacher's name. Students' answers to a route's questions are handed in to that class without a download, and the teacher's class page shows them per stop; the `?route=` link and route file still work without an account. Rules as T-3778. Bounded sizes as T-3672 (20 stops, 280 characters each). Pictures of assign and hand-in at both widths.

Plan: "Server, cloud GPU and engine plan" (https://claude.ai/artifact/WVnQ7RSiUkoSNuVZECFqtE), Stage 1. Owner, 2026-11-26, decision card "File which Stage 1 tickets now?": "All five Stage 1 tickets". Runs on the existing Firebase project (chicago-61643, free Spark plan): no new vendor, no card. Firestore rules are published by the owner in the Firebase console (his address stands in for OWNER_EMAIL there and is never committed); each ticket that adds a collection hands him the rules text and keeps tools/test_sign_in.mjs and docs/SIGN-IN.md in step.
