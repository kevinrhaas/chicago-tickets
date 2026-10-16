---
id: T-2547
title: Crash-aware boot: a phone that ran out of memory last session boots one tier lower and says so, and a lost WebGL context never reload-loops
state: claimed
epic: RENDERING
requested_by: owner
seen: false
effort: S
legacy_id: null
parent: null
opened: 2026-10-15
closed: null
pr: null
claimed_by: run 10/15/2026, 10:39:53 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/38846353426
claimed_at: 2026-10-16T03:39:53.712Z
decision: null
decision_answer: null
---

Crash-aware boot: a phone that ran out of memory last session boots one tier lower and says so, and a lost WebGL context never reload-loops.

## Why

When iOS kills the tab for memory, the visitor's next load boots into exactly the same configuration and dies the same way. `upload-release.js` reloads the page on `webglcontextrestored`, which on a device under pressure can loop. A visitor sees a black canvas or "A problem repeatedly occurred". The owner reports this as frequent on mobile (2026-10-16; the reading is in the reading in T-2546).

## What

- **Crash marker.** At boot start, write `{year, tier, sharpness, t}` to `sessionStorage` (and a `localStorage` mirror, since iOS can lose session storage when it discards the tab). Clear it once the walk has been live for 60 s or on a clean `pagehide`. If the marker is still there at the next boot, the last session died in the load or soon after.
- **Step down, once, and say so.** On a found marker, boot one scene-detail tier lower (and Sharpness Low), and show a dismissible notice: *"Detail lowered: this device ran out of memory last time. Settings can raise it again."* Never step down below `light`. A visitor's explicit setting chosen AFTER the step-down wins.
- **No reload loop.** `webglcontextlost` → `preventDefault()` and show the same notice. On restore, reload at most once per session, and if the context is lost again, reload into the lowered tier.
- Every outcome goes to `__chicago4d` so the smoke can drive it.

## Acceptance

1. The smoke simulates a stale marker and asserts the lowered tier and the notice at 390×780 (visible: a card the visitor reads).
2. The smoke simulates context loss (`WEBGL_lose_context`) twice and asserts one reload at most, then the lowered tier.
3. Zero page errors at both viewports. A clean boot shows no notice.

## The group

Filed together on the owner's ask of 2026-10-16, in dependency order: T-2546 · T-2547 · T-2548 · T-2549 · T-2550 · T-2551 · T-2553 · T-2554 · T-2555 · T-2556 · T-2557 · T-2558. Memory first (T-2546 measures; T-2547, T-2548, T-2549, T-2550 cut CPU and geometry; T-2551, T-2553, T-2554 cut textures), then smoothness (T-2555, T-2556, T-2557), then the forward path (T-2558). Each invisible piece is exempt under AGENTS exemption 1 (an owner-reported bug: mobile memory crashes and jitter), and its PR says so.

