---
id: T-2975
title: Settings › Show › Name of what you look at, switched off, hides the docked name tag; the Settings checkboxes read plainly as on or off on a phone
state: review
epic: META
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: null
opened: 2026-10-21
closed: null
pr: 1171
claimed_by: run 10/21/2026, 9:19:31 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-21T14:19:33.229Z
decision: null
decision_answer: null
---

Settings › Show › Name of what you look at, switched off, hides the docked name tag; the Settings checkboxes read plainly as on or off on a phone.

**Owner, 2026-10-21:** "Name of what you look at does not appear to hide the name" (iPhone screenshots: the setting off, the docked AHEAD tag "1834 Prairie Avenue — Jones villa…" still showing).

**Cause:** T-2942's `.target-tag[data-place="right"] { display: flex }` has the same specificity as `.target-tag[hidden] { display: none }` and comes later in walk.css, so the docked tag ignores `hidden` — the setting, the fade's end, losing the target and the same-address rule all fail to hide it.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
- With the setting off, the tag is not shown in any of its three places (right, centre, bottom), in free roam and on a jaunt; the Inspect key stays.
- With it on and "Fades after a few seconds", the docked tag fades and stays gone (not back at full opacity); looking away hides it.
- The setting persists across a reload.
- Each Settings checkbox reads plainly as off or on at 390×780 in all four appearances (screenshots).
