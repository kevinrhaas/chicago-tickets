---
id: T-3778
title: Class codes and a teacher view: a teacher makes a class, students join with a short code, and the teacher sees the roster, hand-ins and reflections (classroom feature 6)
state: claimed
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-26
closed: null
pr: null
claimed_by: run 11/27/2026, 8:49:35 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-27T14:49:36.862Z
decision: null
decision_answer: null
---

Class codes and a teacher view: a teacher makes a class, students join with a short code, and the teacher sees the roster, hand-ins and reflections (classroom feature 6).

**Acceptance:** In Guide > For teachers, a signed-in teacher can **Make a class** (name, year group) and gets a short join code (unambiguous characters, no profanity, expires or can be reset). A student enters the code once (Settings or the Route panel) and is in the class on every device. The teacher's class page lists who has joined, when they were last in, and what each has handed in from the notebook (hand-in is the student's explicit choice) and their reflections; download as CSV and print. Rules: only that class's teacher reads its roster and hand-ins; a student sees only their own. A student can leave a class; the teacher can remove a student and close the class. Gated by T-3776's switch. Works by keyboard and at 390x780 and 1280x800; pictures in the PR. No grades, scores or leaderboards.

Plan: "Server, cloud GPU and engine plan" (https://claude.ai/artifact/WVnQ7RSiUkoSNuVZECFqtE), Stage 1. Owner, 2026-11-26, decision card "File which Stage 1 tickets now?": "All five Stage 1 tickets". Runs on the existing Firebase project (chicago-61643, free Spark plan): no new vendor, no card. Firestore rules are published by the owner in the Firebase console (his address stands in for OWNER_EMAIL there and is never committed); each ticket that adds a collection hands him the rules text and keeps tools/test_sign_in.mjs and docs/SIGN-IN.md in step.
