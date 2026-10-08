---
id: T-2164
title: Arrival loader as a portable machine screen, with a forecast clock
state: done
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-10-08
closed: 2026-10-08
pr: 514
claimed_by: run 10/8/2026, 12:57:31 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-08T07:09:43Z
claimed_run: null
claimed_at: 2026-10-08T05:57:31.168Z
decision: null
decision_answer: null
---

Arrival loader as a portable machine screen, with a forecast clock.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 156 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> Owner request, 2026-10-08 (project thread): restyle the loading screen like the home page machine and forecast the download so the rollback clock moves smoothly on slow connections.

## Owner, 2026-10-08 (project thread), verbatim

> for the opening screen that we load and there is a ticker can you put more of the style and components and appearance of the home page like it's a working machine almost a portable machine screen, like for the statuses make sure they are rendered at the good size so as you work through them, the size of the screen box device does not change, also the rollback time sequence flip chart is good, but I notice in slow connections the glb download takes time and the clock sits there, I think you need to forecast the speed of that download and all the components download so that time rollback is more consistent and smoother and the progress is more accurately reported for the full load.

## Why the clock sits

`bootProgress` weights each phase by CPU seconds measured on a fast desktop over a local mirror (boot-weights.js). The network is in none of those numbers: `scene` (≈640 sidecars + ≈640 GLBs) is weighted 0.2 s and reports progress only as whole files finish, and `terrain` (a 1.26 MB GLB plus a 0.44 MB heightfield) has no units at all, so its time fallback reaches its 92 % cap in a quarter second and then waits for the download.

**Acceptance:**
- The arrival gate reads as a handheld version of the home page machine: a bezelled device, a phosphor screen with a status log, lamps per boot stage, the flip year in its amber window, and a data/link readout. All four appearances are styled.
- The device's box does not change size as statuses cycle, on desktop and at 390×780 (status lines are fixed-height and clipped, never wrapped into a taller box).
- Progress is forecast from bytes as well as CPU: bytes received are metered, link speed is estimated live, and each stage's expected time is its CPU seconds plus its expected bytes over the measured link. The year rolls at the forecast rate rather than waiting on events, never runs backwards, and does not sit still on a throttled connection.
- Expected bytes per stage are learned per build after a visit (like the existing timing history), with a committed default for a first visit.
- No new phone memory: no response bodies are cloned or retained to meter them.
- Screenshots: desktop, 390×780 phone, and a throttled slow connection mid-load.
