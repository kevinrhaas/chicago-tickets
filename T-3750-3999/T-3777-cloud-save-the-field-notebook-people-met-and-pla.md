---
id: T-3777
title: Cloud save: the field notebook, people met and places found, and settings follow a signed-in student to any device through Firestore, with browser storage as the offline fallback
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
claimed_by: run 11/27/2026, 12:12:19 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-27T06:12:20.608Z
decision: null
decision_answer: null
---

Cloud save: the field notebook, people met and places found, and settings follow a signed-in student to any device through Firestore, with browser storage as the offline fallback.

**Acceptance:** For a signed-in visitor (not anonymous-email, unless the owner rules otherwise), the field notebook (entries, chosen photos, citations), people met / places found (`chicago4d.metfound.v1`) and Settings travel through Firestore `users/<uid>/...` and appear on another device after sign-in. Offline-first: browser storage stays the working copy; writes are batched and debounced (no write per keystroke); a conflict keeps the newer entry per item and never silently drops one. Rules: a user reads and writes only their own documents, with size limits per document. Signed-out, offline or Firebase-down visitors keep today's browser-only behaviour with no error. A daily write estimate for a 30-student lesson is measured and stays far inside the free tier (20,000 writes/day). Delete-my-data (T-3776) removes it all. Tests for merge and rules; pictures of the sync state at both widths.

Plan: "Server, cloud GPU and engine plan" (https://claude.ai/artifact/WVnQ7RSiUkoSNuVZECFqtE), Stage 1. Owner, 2026-11-26, decision card "File which Stage 1 tickets now?": "All five Stage 1 tickets". Runs on the existing Firebase project (chicago-61643, free Spark plan): no new vendor, no card. Firestore rules are published by the owner in the Firebase console (his address stands in for OWNER_EMAIL there and is never committed); each ticket that adds a collection hands him the rules text and keeps tools/test_sign_in.mjs and docs/SIGN-IN.md in step.
