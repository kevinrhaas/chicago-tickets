---
id: T-3797
title: Launch access: the owner's admin panel on the launch page, access keys he mints, and rights pre-assigned by email (cloud play, admin), checked by Firestore rules and the stream starter
state: open
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-27
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

Launch access: the owner's admin panel on the launch page, access keys he mints, and rights pre-assigned by email (cloud play, admin), checked by Firestore rules and the stream starter.

**Acceptance:** (a) The owner is admin by his signed-in account (the address the published rules already hold for OWNER_EMAIL, never committed); no shared admin password exists. (b) An Admin panel on the launch page, shown only to admins: list people and their rights; pre-assign rights by email before a person ever signs in (`cloud` = may start a cloud machine, `admin` = may manage people); revoke. (c) Access keys: the admin mints a key (shown once, stored only as a hash) with the rights it grants, an expiry and a use limit; a signed-in player redeems it once on the launch page and gets those rights on their account. (d) Firestore rules enforce all of it (only admins write grants and keys; a player reads only their own rights), tested in the emulator and in the gate's fake; the stream starter (T-3794) checks the same rights before it starts a machine. (e) Cloud play stays off for anyone without `cloud`, and shows the owner's waiting state while GPU quota is pending.

Owner, 2026-11-27 (thread "Plan server, cloud GPU and engine path"): "update the chicago 4d launch page with the 4 year tile consoles to start (there may be more) and save the existing but do a rework so this feels more like a game launch page, clean it up and simplify it so it feels like an aaa launch page, with the music bed audio on/off and settings that can be managed, you probably could add auth to that page ... we will want to protect the launch of the server at first by requiring a key to access so you will need to give me an admin key and admin rights and eventually to manage the people who as users and pre-assign rights to launch ... allows you to see and test your computer and it does it automatically and its clear what is going on and recommendations and keep that green screen text focus there and other markers". Filed as two M tickets because the queue refuses an L.
