---
id: T-3776
title: Student data policy for server-saved work: a plain privacy notice, delete-my-data in Settings, and an agreement a school can sign (Illinois SOPPA), before any class uses the Stage 1 cloud features
state: review
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-26
closed: null
pr: 2381
claimed_by: run 11/26/2026, 9:51:38 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-27T03:51:39.036Z
decision: null
decision_answer: null
---

Student data policy for server-saved work: a plain privacy notice, delete-my-data in Settings, and an agreement a school can sign (Illinois SOPPA), before any class uses the Stage 1 cloud features.

**Acceptance:** (1) docs/STUDENT-DATA.md: what each Stage 1 feature stores (field by field), where (Firestore nam5), who can read it, how long it is kept, and that nothing is sold, shared or used for ads; written for a teacher and a parent. (2) A short notice shown once before a student's first cloud save, and in Settings > About, linking to it. (3) Settings > About gains **Delete my saved data**: removes every server record the signed-in user owns (visitors row excepted only if the owner rules so) with an inline confirm, and says when it is done. (4) A plain school agreement draft (docs/STUDENT-DATA-AGREEMENT.md) covering Illinois SOPPA's points (purpose, data list, breach notice, deletion on request, no sale), marked as a draft for the owner, not legal advice. (5) No cloud feature (T-3777..T-3780) is switched on for a class until this has merged; each checks a single `cloudFeatures` switch. Keyboard and 390x780 / 1280x800 pictures in the PR.

Plan: "Server, cloud GPU and engine plan" (https://claude.ai/artifact/WVnQ7RSiUkoSNuVZECFqtE), Stage 1. Owner, 2026-11-26, decision card "File which Stage 1 tickets now?": "All five Stage 1 tickets". Runs on the existing Firebase project (chicago-61643, free Spark plan): no new vendor, no card. Firestore rules are published by the owner in the Firebase console (his address stands in for OWNER_EMAIL there and is never committed); each ticket that adds a collection hands him the rules text and keeps tools/test_sign_in.mjs and docs/SIGN-IN.md in step.
