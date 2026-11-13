---
id: T-3578
title: Voice jaunt narration with ElevenLabs: The Glessner Household first
state: done
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-12
closed: 2026-11-13
pr: 1982
claimed_by: run 11/12/2026, 10:42:17 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-11-13T06:42:02Z
claimed_run: null
claimed_at: 2026-11-13T04:42:18.164Z
decision: null
decision_answer: null
---

Voice jaunt narration with ElevenLabs: The Glessner Household first.

Owner, 2026-11-13 (project thread "Voice jaunt narration with ElevenLabs"): *"I have some voices in eleven labs and I want to begin using those and having them read/play the narration or scripts like the meet the Glessner household ... it would be nice if you can build those audio tracks automatically"*; approved the automated plan ("Yes").

**Acceptance:**
- A GitHub workflow voices jaunt scripts with ElevenLabs from repo secrets, only for scripts whose text (or voice) changed, uploads content-addressed MP3s to the R2 media bucket and publishes a small narration index; a dry run reports what it would voice and the characters it would spend.
- Voice per speaker (narrator; each host person) in a config file; voices may be given by ElevenLabs name or id; a list-voices mode prints the owner's voices.
- In the app each jaunt opening, stop and ending with a matching clip has a play/stop control; narration follows the stop, ducks music/ambience, and has its own Narration level in Settings › Sound. Text that changed since voicing never plays the old clip.
- The Glessner Household is the first jaunt configured. Works at 390x780 and desktop; no pageerrors when the index is unreachable.
