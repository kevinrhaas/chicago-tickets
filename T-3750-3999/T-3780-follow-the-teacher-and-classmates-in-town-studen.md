---
id: T-3780
title: Follow the teacher and classmates in town: students go to the teacher's current stop, and classmates show as people in the town inside their own class only, with no chat (classroom features 13 and 19)
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

Follow the teacher and classmates in town: students go to the teacher's current stop, and classmates show as people in the town inside their own class only, with no chat (classroom features 13 and 19).

**Acceptance:** (a) **Follow the teacher:** a teacher in a class can turn on *Lead the class*; each student gets **Go with my teacher**, which moves them to the teacher's current stop (jaunt stop, route stop or place, never inside a house, per the Find/Follow rule) whenever it changes; stop changes only, not a live position stream, so reads stay small. (b) **Classmates in town:** with the teacher's OK per class, classmates in the same year show as people in the town (name card with first name only), updated about every 2 s through Realtime Database presence, inside that class only; no chat, no messages, no strangers. Turning either off stops all traffic. Measured reads/writes for a 30-student hour, inside the free tiers. Owner step: switch on Realtime Database in the Firebase console. Gated by T-3776's switch. Pictures at both widths.

Plan: "Server, cloud GPU and engine plan" (https://claude.ai/artifact/WVnQ7RSiUkoSNuVZECFqtE), Stage 1. Owner, 2026-11-26, decision card "File which Stage 1 tickets now?": "All five Stage 1 tickets". Runs on the existing Firebase project (chicago-61643, free Spark plan): no new vendor, no card. Firestore rules are published by the owner in the Firebase console (his address stands in for OWNER_EMAIL there and is never committed); each ticket that adds a collection hands him the rules text and keeps tools/test_sign_in.mjs and docs/SIGN-IN.md in step.
