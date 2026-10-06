---
id: T-2152
title: The 1835 walk is killed on an iPhone again: halve the sign and yard-mark atlases on a phone, and stop the plank-walk and fence builders churning a gigabyte of garbage
state: review
epic: META
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: null
opened: 2026-10-06
closed: null
pr: 502
claimed_by: run 10/6/2026, 1:35:52 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-06T18:35:52.806Z
decision: null
decision_answer: null
---

The 1835 walk is killed on an iPhone again: halve the sign and yard-mark atlases on a phone, and stop the plank-walk and fence builders churning a gigabyte of garbage.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 156 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> Owner-reported crash, second report (2026-10-06); worked and PR'd in the same run

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

At 390x780, touch, DPR 3, 1835 on dev: the GPU texture total and the mid-load JS heap peak each come down by at
least a third with the town drawing the same scene; signs and yard marks stay legible at phone size; 1904 is
unchanged; the gate and the smoke legs covering the touched layers are green.

## The report (owner, 2026-10-06)

"I seem to be consistently ceasing on load of the app after the status bar completed, sometimes it will reload
and then crash ... This was for 1835, this was chrome on an iPhone." T-2063 fixed the first version of this.

## Measured (Chromium, mobile profile, local publishes)

| build | whole-tab peak (renderer RSS) | GPU process peak | JS heap peak mid-load | GPU textures |
|---|---|---|---|---|
| right after T-2063 (4eee6b3e) | 1236 MB | 842 MB | ~356 MB | ~209 MB |
| production (abcc3c79) | 1328 MB | 853 MB | | |
| dev (3affc239) | 1391 MB | 852 MB | 483 MB | 203 MB |
| this fix | ~1280-1330 MB | ~722 MB | ~223 MB | 118 MB |
| 1904 on dev, for scale | 620 MB | 545 MB | 64 MB | |

The largest single textures were canvases: the signboard lettering atlas at 4096x3328 (72 MB on the GPU with
mips plus 54 MB of canvas), its relief and roughness companions, and the yard-goods mark atlas at 1536x2112.
The JS peak was garbage, not live data: a sampling profile counting collected objects put ~1 GB of allocation
in frontage.js pushBox (per-call corner and face arrays, and JS number arrays grown by doubling), ~400 MB in
enclosures.js pushBox and ~880 MB in yards.js edgeDistance's destructuring.

Left for later: the scene's geometry still keeps ~420 MB of CPU-side attribute arrays (frontage 116 MB, terrain
102 MB, structures 51 MB, trees 43 MB); dropping those needs picking and distance-culling reworked.

