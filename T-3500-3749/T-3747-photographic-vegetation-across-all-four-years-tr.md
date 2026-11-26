---
id: T-3747
title: Photographic vegetation across all four years: tree foliage and bark, adaptive detail and light
state: claimed
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-11-25
closed: null
pr: null
claimed_by: run 11/25/2026, 9:56:41 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-26T03:56:43.103Z
decision: null
decision_answer: null
---

Owner request, Better Trees handoff supplied 2026-11-25: "improve the look of the trees so they look more perfectly photographic realistic and handle it so low power computers use it and higher power computers can also show it high detail and smooth fps and great rendering and light ... push it to dev when green. All trees and flora everywhere should get this upgrade."

This piece owns the shared woody renderer: grown trees and vines, street trees, thickets and woody shrubs in 1812, 1835, 1871 and 1904. T-3748 owns herbaceous flora and garden crops. Use the supplied first-pass patch as a starting point, subject to actual rendering and regression checks.

**Acceptance:**
1. Improve foliage volume and leaf lighting visibly in fixed-camera before/after images, including close tree crowns, a thicket and vines. Preserve species, placements, historical grades, season controls and licensed asset provenance.
2. Thin-leaf lighting follows light direction, shadows and time of day; bark and winter wood do not gain leaf transmission. Keep wind, cutout shadows, LOD fades and Confidence view working.
3. Keep Light's reduced geometry, texture sizes and shadow reach. Higher tiers may use additional surface detail; record the cost and check frame triangles, calls, texture/geometry memory and relative frame timings. Do not claim hardware FPS targets from the cloud software renderer.
4. Exercise the published app in all four years at 390x780 and 1280x800, including Light/Balanced/Full, low-memory behavior, day/night and seasons. All four local check.sh parts, PR preflight questions, required CI and mapped published renderer smoke pass before merge to dev. Save images and measurements in chicago-evidence; record limitations honestly.
5. No paid tool, new engine or fabricated historical evidence. Declare artistic lighting/surface approximations in LIBERTIES; ship a concise What's New entry and STATUS receipt.
