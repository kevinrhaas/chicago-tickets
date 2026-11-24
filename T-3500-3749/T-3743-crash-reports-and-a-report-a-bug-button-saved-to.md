---
id: T-3743
title: Crash reports and a report-a-bug button, saved to Firebase with an email
state: review
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-24
closed: null
pr: 2338
claimed_by: run 11/24/2026, 9:43:57 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-24T15:43:58.726Z
decision: null
decision_answer: null
---

Crash reports and a report-a-bug button, saved to Firebase with an email.

The owner, 2026-11-24: "could you add a file crash report? When it crashes and we get a record and an an email and or a person can have a button maybe tiny in the upper right ... shown by default but you can turn it off to file a bug and it takes screen shot and collects environmental stuff and ships all of that to firebase, a person can add comments and we know who filed it because of login" — and "And add that to the tour".

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
- A small key at the upper right, on by default, switchable off in Settings, opens a sheet with a picture of the town and a comment box.
- A report saves to Firestore under the signed-in uid with device, GPU, memory, year, settings, position and recent errors, and emails the owner.
- A page cut off (memory kill, display reset) is reported automatically, once; errors are recorded; automatic emails are capped.
- Dev and live reports are told apart (one Firebase project, the owner's choice).
- The first-time tour points out the key.
- Nothing is sent from a local serve or under automation; phones and weak PCs pay nothing until a report is filed.
