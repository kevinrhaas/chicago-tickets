---
id: T-2063
title: The 1835 walk is killed on an iPhone at load: three town layers keep ~400 MB of build scratch alive
state: claimed
epic: META
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: null
opened: 2026-10-03
closed: null
pr: null
claimed_by: run 10/3/2026, 10:55:35 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-04T03:55:35.764Z
decision: null
decision_answer: null
---

The 1835 walk is killed on an iPhone at load: three town layers keep ~400 MB of build scratch alive.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 201 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> Owner-reported crash (the 1835 tab dies on his iPhone, 2026-10-04); worked and PR'd in the same run, so it never waits in the queue

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

At 390x780, touch, DPR 3 (the mobile release profile), the 1835 page reaches ready with its live JS heap
under 200 MB (it was 529 MB) and its peak heap during the build at least 150 MB lower than before; 1904 is
unchanged; the gate and the smoke legs that cover the touched layers are green.

## The report (owner, 2026-10-04)

Opened the dev build on an iPhone (Chrome for iOS, so WebKit), chose 1835, and the tab died on Chrome's
"Can't open this page" screen. 1904 loads on the same phone. That screen is the web content process being
killed, and iOS kills it for memory.

## Measured (Chromium, mobile profile, local publish of dev a0de7bc9)

| page | JS heap at ready | peak JS heap during boot | GPU buffers | GPU textures (est.) |
|---|---|---|---|---|
| 1904 | 64 MB | 64 MB | 29 MB | 291 MB |
| 1835, dev | 529 MB | 555 MB | 158 MB | 209 MB |
| 1835, this fix | 160 MB | 356 MB | 158 MB | 209 MB |

So 1835's GPU load is no heavier than 1904's; the difference is ~470 MB of JS heap. A sampling heap profile
taken after a forced GC at ready attributed it to the build scratch of three layers, still reachable:
`frontage.js` pushBox 187 MB (the plank walks, fences, posts and fittings), `trees.js` MeshBuf.vert 51 MB +
addStem/addPuff 15 MB, `yard.js` tri 38 MB, `yards.js` layRegion 12 MB, plus ~100 MB of array growth slack
under `push`. These are plain JS number arrays (8 bytes a component plus slack) that three.js had already
copied into Float32Arrays; they stayed alive because the layer's long-lived closures (`pickAt`, `dispose`)
share the build function's scope, and the chunk maps hold the buffers.

