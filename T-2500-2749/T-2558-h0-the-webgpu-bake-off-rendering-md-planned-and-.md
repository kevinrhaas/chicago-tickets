---
id: T-2558
title: H0, the WebGPU bake-off RENDERING.md planned and never started: three WebGPURenderer and TSL on the Glessner block from the same GLBs, kill criteria written first
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
decision: pending
decision_answer: null
---

H0, the WebGPU bake-off RENDERING.md planned and never started: three WebGPURenderer and TSL on the Glessner block from the same GLBs, kill criteria written first.

## Why

RENDERING.md Track 2 (H0 to H3) planned a second web renderer on **three's WebGPURenderer + TSL**, with WebGL2 fallback, and named H0 (a time-boxed bake-off) as its start. It was never started, and no ticket carries it. Since the plan was written, WebGPU has shipped in Safari on iOS and macOS alongside Chrome/Edge and Firefox. So "native-like" use of the visitor's own GPU (compute passes, indirect draws, render bundles, lower CPU cost per draw, real temporal AA (TRAA), GTAO) is now reachable in a browser, with no Unreal build and no per-platform compile. This is the forward path the owner described on 2026-10-16. RENDERING.md §8 keeps the H track gated, so this needs a ruling (see the decision on this ticket).

## What (H0 only, a spike with its kill criteria written first)

- **No build step needed for the spike:** `three.webgpu.js` + TSL are in the same pinned 0.185.1 tarball. Vendor them with MANIFEST lines and an import map in a separate `renderers/web-hd/` page. (RENDERING.md §3 allows a build step there. The spike does not need one.)
- Boot the **Glessner block of `/1904/`** from the SAME GLBs and sidecars (the data contract is the interface: "copy, don't couple"). Draw the confidence view as a TSL node composed onto every material (conformance trio, doctrine 1), plus the NOAA sun and the heightfield ground.
- **Kill criteria, recorded in RENDERING.md §8 before any code:** for example, phone-profile resident memory ≤ walk/'s for the same block; moving p95 ≤ walk/'s; capture parity within tolerance; WebGL2 fallback boots on a device with no WebGPU; zero page errors.
- A memo appended to §8 with the measured table and a go / no-go for H1.

## Acceptance

The memo with numbers at both viewports, the kill criteria answered one by one, and `walk/` untouched and green (Track 2 delta, RENDERING.md §7).

## The group

Filed together on the owner's ask of 2026-10-16, in dependency order: T-2546 · T-2547 · T-2548 · T-2549 · T-2550 · T-2551 · T-2553 · T-2554 · T-2555 · T-2556 · T-2557 · T-2558. Memory first (T-2546 measures; T-2547, T-2548, T-2549, T-2550 cut CPU and geometry; T-2551, T-2553, T-2554 cut textures), then smoothness (T-2555, T-2556, T-2557), then the forward path (T-2558). Each invisible piece is exempt under AGENTS exemption 1 (an owner-reported bug: mobile memory crashes and jitter), and its PR says so.

## Decision needed

**Question:** RENDERING.md section 8 keeps Track 2 (the WebGPU renderer) gated. May a run start H0, the no-build WebGPU bake-off on the Glessner block, with its kill criteria written into section 8 first?

- (a) Yes, once T-2546's memory meter has landed, so walk/ and the spike are compared on the same instrument
- (b) Yes, now, in parallel with the memory group
- (c) Not yet: finish the memory and smoothness group first and ask again

**Recommendation:** (a) Yes, once T-2546's memory meter has landed, so walk/ and the spike are compared on the same instrument — The spike's whole value is a fair measured comparison, and only T-2546 makes memory comparable; a no-build spike in its own directory never touches walk/.

**Asked:** 2026-10-15. Answer on Manager's 4D Board, or set `decision: answered` and `decision_answer: <letter>` in this file.
