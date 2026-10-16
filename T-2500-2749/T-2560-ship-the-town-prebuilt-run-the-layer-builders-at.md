---
id: T-2560
title: Ship the town prebuilt: run the layer builders at publish and ship frontage and spatial-batch buffers as compressed binaries, so a phone uploads the town instead of building it at every boot
state: open
epic: RENDERING
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-15
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

Ship the town prebuilt: run the layer builders at publish and ship frontage and spatial-batch buffers as compressed binaries, so a phone uploads the town instead of building it at every boot.

## Why

Owner, 2026-10-16: *"a big package app download that happens up front so the app is lightning fast rendering when you are walking or flying"*. Downloading is not the slow part. Building the town on the visitor's device is. The September boot receipt (`tools/boot_phase_measurements.json`, Apple M5 Max, no throttle) shows the phone profile's longest main-thread task at **3.4 s**, with flora 1.7 s and interaction 1.0 s, all on-device generation. A phone is several times slower. Frontage, yard, enclosures, the terrain base and `spatial-batch` chunks are rebuilt from JSON on every visit by every visitor, with the same result every time.

AGENTS rule 4 says every mesh is generated from `data/` by a command. That command can be the publish step instead of the visitor's browser, and rule 5 (renderers consume glTF) is better honoured, not worse.

## What

- Run the existing layer builders in Node at publish time (`tools/prebuild_layers.mjs`), the same modules and the same inputs, and write each layer's finished buffers as a meshopt-compressed GLB (or `.bin` + JSON index) per year under `site/4d/data/prebuilt/<year>/`, with the input hash recorded so `check_published.mjs` refuses a stale one. Start with **frontage** (1835's largest layer: 118 MB GPU) and the **spatial-batch** chunks. Others follow as one follow-up.
- The browser loads the prebuilt buffers and only uploads them. It keeps the in-browser builder as the fallback when a prebuilt file is missing or stale (and for the dev source tree).
- The pure typed-array builders T-2556 moves into workers are the same code that runs here. Do that ticket's extraction first where the two touch.
- Flora stays procedural, and T-2557 moves it to the GPU instead.

## Acceptance

1. **Byte parity:** the prebuilt buffers equal what the browser builds, checked in `check.sh` with no browser.
2. `measure_boot_phases.mjs --published`: the converted layers' phase time and the longest task fall at the phone profile. Quote before and after, cold and warm.
3. The published byte budget (`SITE-BUDGET.md`) is re-measured with the prebuilt files counted. Captures are identical at the anchors, with zero page errors.

## The group

Part of the owner's mobile performance and memory group of 2026-10-16 (T-2546 measures; see its reading). Added on the owner's follow-up the same day: *"if there is a way to tap into local computing resources for rendering based on the browser and platform or if there can be a big package app download that happens up front so the app is lightning fast rendering when you are walking or flying"*. T-2559 chooses per device, T-2560 ships the town prebuilt, and T-2561 puts it on disk. Each invisible piece is exempt under AGENTS exemption 1 (an owner-reported bug), and its PR says so.

