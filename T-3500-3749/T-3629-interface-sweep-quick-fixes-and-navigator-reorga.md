---
id: T-3629
title: Interface sweep: quick fixes and Navigator reorganisation (Kevin's usability review)
state: done
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-16
closed: 2026-11-16
pr: 2132
claimed_by: run 11/16/2026, 7:39:11 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-11-17T05:12:21Z
claimed_run: null
claimed_at: 2026-11-17T01:39:12.709Z
decision: null
decision_answer: null
---

Interface sweep: quick fixes and Navigator reorganisation (Kevin's usability review).

**Acceptance:** Kevin's chosen groups A, B and C (analysis: claude.ai/artifact/DpJefCV7PcabCjypAws78n) are built, and 1835 is swept too. Every feature stays reachable. All four Appearances, phone and desktop work. The unit tests follow the change.

**Done (PR #2132):**
- Labelled rail. Move and Jump are off the rail and reached from Home and the year chip.
- A phone tab bar.
- One card per jaunt, with a remembered grade (18+ included).
- Jaunt panel with one Next stop key.
- Three key kinds, red only for Recall.
- One close key per screen.
- Show split into On screen and The town.
- People and Shops filters folded (the 1835 finding).
- Group A fixes.

**Kept as they were:** Guide (a locked term), the telemetry strip, Research as the last tab, picture credits on cards. The compass heading ring, labelled instrument keys and Go to inside Map were not built.

## Before and after

![Navigator Home, 1835](https://github.com/kevinrhaas/chicago-evidence/blob/85d1741cde3b618b3f153291a83e83c9eadefb20/evidence/T-3629-interface-sweep/01-navigator-home-1835.jpg?raw=true)
![Jaunt list, 1835](https://github.com/kevinrhaas/chicago-evidence/blob/85d1741cde3b618b3f153291a83e83c9eadefb20/evidence/T-3629-interface-sweep/02-jaunt-list-1835.jpg?raw=true)
![People, 1835](https://github.com/kevinrhaas/chicago-evidence/blob/85d1741cde3b618b3f153291a83e83c9eadefb20/evidence/T-3629-interface-sweep/03-people-1835.jpg?raw=true)
![Jaunt panel, 1812](https://github.com/kevinrhaas/chicago-evidence/blob/85d1741cde3b618b3f153291a83e83c9eadefb20/evidence/T-3629-interface-sweep/04-jaunt-panel-1812.jpg?raw=true)
![Phone Home](https://github.com/kevinrhaas/chicago-evidence/blob/85d1741cde3b618b3f153291a83e83c9eadefb20/evidence/T-3629-interface-sweep/05-phone-home.jpg?raw=true)
![Phone Settings](https://github.com/kevinrhaas/chicago-evidence/blob/85d1741cde3b618b3f153291a83e83c9eadefb20/evidence/T-3629-interface-sweep/06-phone-settings.jpg?raw=true)

