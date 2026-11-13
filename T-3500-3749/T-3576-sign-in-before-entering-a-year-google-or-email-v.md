---
id: T-3576
title: Sign-in before entering a year (Google or email), visitor list and usage
state: claimed
epic: META
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-11-12
closed: null
pr: null
claimed_by: run 11/12/2026, 9:00:00 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-13T03:00:01.461Z
decision: null
decision_answer: null
---

Kevin, 2026-11-13 (thread "Add sign-in before entering a year"): *"Google auth when you hit one of the time zone years before hitting the download and would be nice if someone could provide an email to get in if they don't have a Google account and then it's ok to let them in with that, we can eventually get to verified emails but I don't want to set up a server"*; *"I would want to be able to know or get a list when people auth or of everyone who has come in"*; *"Might be nice to have some usage stuff"*; *"There are direct links to years also do as long as it's one in front of the years and we know each time you go into year you should not have to auth to separate years"*.

Serverless: Firebase (Auth: Google + anonymous-with-typed-email; Firestore for the visitor list; Analytics for usage). Kevin creates the Firebase project; the client ships behind a config flag (off until the keys are in).

**Acceptance:**
- With the flag off (and on any host not listed), nothing changes: no gate, no Firebase bytes fetched.
- With it on, every year door (portal cards and direct links, /1812/ /1835/ /1904/ and ?year=) asks for sign-in BEFORE the scene download starts; Google or a typed email both let the visitor in; one sign-in covers every year on that device.
- Each year entered is recorded (who, which year, when, device class) in Firestore and as an Analytics event.
- A visitors page lists everyone who has come in, newest first, readable only by the owner's Google account.
- If Firebase cannot be reached the visitor is let in (fail open) and the boot is not stalled.
- Works at 390×780 and 1280×800.
