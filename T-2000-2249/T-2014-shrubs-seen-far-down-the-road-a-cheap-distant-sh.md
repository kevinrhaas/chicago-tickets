---
id: T-2014
title: Shrubs seen far down the road: a cheap distant shrub out to 140 m that refines into the full bush, no pop-in
state: claimed
epic: META
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-10-02
closed: null
pr: null
claimed_by: run 10/2/2026, 11:50:24 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-03T04:50:24.623Z
decision: null
decision_answer: null
---

Shrubs seen far down the road: a cheap distant shrub out to 140 m that refines into the full bush, no pop-in.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 238 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> the owner asked for it directly on 2026-10-03 (Kinzie at Clark, 1835 on dev)

**Acceptance:** walking Kinzie toward Clark in 1835 at `full`, shrubs are visible as far down the road as the far sward (well past 100 m), small and cheap in the distance, and each one turns into the full bush at the same spot, size and colour as you close on it: no shrub appears out of empty ground and no screen-door stipple is visible where the detail changes. Draw calls stay under 240 and every tier stays under its triangle ceiling.

## The owner's words (2026-10-03, on dev, Kinzie Street approaching Clark)

> when going forward ,and walking where there are plants the plants appear to still pop up from nowhere, you have a pixely fade in, but i think you need to have a further field that you are rendering, like a lot further so you can render them small and far away and keep rendering them into better quality and larger when they are close, you should have a MUCH longer field of vision for the plants to see them down the poad and in the distance

## Cause

The shrub stratum (`flora-shrub`, hazel, elder, dogwood …, 136 triangles each) is dealt only on the forb ring, which ends at 26 m (+3 m fringe) at `full` and is screen-doored in over its last 5 m. The far band (T-0086) carries the grass and forbs out to 175 m as clump cards, but nothing carries the shrubs, so every bush appears out of nothing at ~26 m through the 4x4 dither.

## Plan

A far shrub LOD on the SAME lattice slots as the detailed shrub pass (same salt, same deal, same rng), so the far shrub at a slot is the detailed shrub's own position, height, width and colour. A cheaper archetype (fewer, larger leaf masses), drawn whole (no dither), hidden by a hard per-slot inner edge where the detailed bush becomes fully drawn, thinned by world-anchored rank over its last metres. Rebuilt on its own coarser step so the long lattice is not re-dealt every 0.6 m.

