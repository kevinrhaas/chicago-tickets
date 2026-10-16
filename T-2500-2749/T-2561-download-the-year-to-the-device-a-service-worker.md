---
id: T-2561
title: Download the year to the device: a service worker installs a versioned per-year pack to disk with progress, boots offline, updates only changed files, installs to the home screen, and has a kill switch
state: done
epic: RENDERING
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-15
closed: 2026-10-16
pr: 894
claimed_by: run 10/16/2026, 11:32:15 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-16T20:10:38Z
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38930618970
claimed_at: 2026-10-16T16:32:15.550Z
decision: null
decision_answer: null
---

Download the year to the device: a service worker installs a versioned per-year pack to disk with progress, boots offline, updates only changed files, installs to the home screen, and has a kill switch.

## Why

Owner, 2026-10-16: *"a big package app download that happens up front so the app is lightning fast"*. Today there is no service worker, no offline cache and no install manifest. Every module fetches with `cache: 'no-cache'` (32 call sites), so every visit re-validates hundreds of files over the network before a phone can walk, and a visit with poor signal stalls or fails. The browser lets a site keep **gigabytes on disk** (Cache Storage / OPFS, made durable with `navigator.storage.persist()`), and an installed home-screen app on iOS is not subject to Safari's 7-day eviction of unused sites. That is the native-app install, without an app store.

## What

- **"Download this year"**: a service worker (`site/4d/sw.js`, written by `publish.sh`) that installs a **versioned per-year pack** into Cache Storage: the year's GLBs (KTX2 after T-2553), prebuilt layers (the prebuilt-geometry ticket), sidecar boot parts, textures and the app's own modules, listed by a manifest `publish.sh` writes with content hashes. The welcome screen offers it with size and progress. After that the year boots from disk, offline.
- **Disk, not memory:** the pack lives on disk. What enters memory is still chosen by residency (T-2554), so a full download never means a full load.
- **Updates by hash:** a new build downloads only changed files (diff the manifests). `build.json` decides staleness. Data indexes and `changelog.js` are network-first, so What's-New is never stale. The Manager/launcher path (`/4d/js/changelog.js`) is server-side and unaffected.
- **Installable:** a web app manifest and icons, so "Add to Home Screen" gives a full-screen app with durable storage.
- **Safety:** a kill switch (a `sw-off` flag in `build.json` unregisters the worker) and separate scopes for `/4d/dev/` and production, so the preview and production never serve each other's packs. A broken service worker can strand visitors on an old build, and the kill switch is what prevents that.

## Acceptance

1. The smoke: install the 1835 pack, go offline (`context.setOffline(true)`), and reload. The town boots and walks with zero page errors at both viewports.
2. A second publish with one changed GLB: the update fetches only that file (counted), and the kill switch unregisters the worker (asserted).
3. Warm boot time with the pack against today's warm boot, at the phone profile, quoted. `docs/PIPELINE.md` notes the dev/production scope split.

## The group

Part of the owner's mobile performance and memory group of 2026-10-16 (T-2546 measures; see its reading). Added on the owner's follow-up the same day: *"if there is a way to tap into local computing resources for rendering based on the browser and platform or if there can be a big package app download that happens up front so the app is lightning fast rendering when you are walking or flying"*. T-2559 chooses per device, T-2560 ships the town prebuilt, and T-2561 puts it on disk. Each invisible piece is exempt under AGENTS exemption 1 (an owner-reported bug), and its PR says so.

