---
id: T-2828
title: 1904 on the owner's iPhone dies walking up to the Glessner front at Light and Sharpness 1: the tab was killed about 5 s into a walk from the 18th Street spawn across Prairie Avenue (last at 1390,-3220, 741 textures, 550k triangles), found and fixed against the phone memory ceiling
state: claimed
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-10-18
closed: null
pr: null
claimed_by: run 10/18/2026, 7:46:40 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/39181929840
claimed_at: 2026-10-19T00:46:40.886Z
decision: null
decision_answer: null
---

1904 on the owner's iPhone dies walking up to the Glessner front at Light and Sharpness 1.

**Owner-reported, 2026-10-19** (visible-progress exemption 1). He pressed Settings → Performance → Read
frame pacing on the dev preview at `/4d/dev/1904/` (iPhone, iOS 27, Chrome/WebKit, 375×636) and the tab
died; on reload the page's crash log showed this, verbatim:

```
{"page":"mvej28f7-iseo","year":"1904","build":"DEV PREVIEW · dev@a369c613 · Oct 18, 2026, 6:28 PM CT","start":1792370405923,"ended":null,"last":{"t":67736,"calls":103,"tris":549763,"geo":291,"tex":741,"w":375,"h":636,"ratio":1,"heap":null,"at":"1390,-3220"},"entries":[{"t":0,"k":"boot","to":"light@1"},{"t":43675,"k":"ready"},{"t":46882,"k":"pick","meshes":0,"batches":183},{"t":46898,"k":"picked","hit":"structures:merged"},{"t":48749,"k":"pick","meshes":0,"batches":183},{"t":48758,"k":"picked","hit":"structures:merged"},{"t":48765,"k":"nav","level":1,"app":"home"},{"t":50792,"k":"nav","level":2,"app":"home"},{"t":54204,"k":"nav","level":2,"app":"settings"},{"t":65062,"k":"nav","level":0,"app":"settings"},{"t":66002,"k":"pick","meshes":0,"batches":183},{"t":66026,"k":"picked","hit":"structures:merged"},{"t":66528,"k":"pick","meshes":0,"batches":183},{"t":66553,"k":"picked","hit":"structures:merged"},{"t":67044,"k":"pick","meshes":0,"batches":183},{"t":67068,"k":"picked","hit":"structures:merged"},{"t":67545,"k":"pick","meshes":0,"batches":183},{"t":67567,"k":"picked","hit":"structures:merged"},{"t":68058,"k":"pick","meshes":0,"batches":183},{"t":68076,"k":"picked","hit":"structures:merged"},{"t":68580,"k":"pick","meshes":0,"batches":183},{"t":68601,"k":"picked","hit":"structures:merged"},{"t":69086,"k":"pick","meshes":0,"batches":183},{"t":69099,"k":"picked","hit":"structures:merged"},{"t":69630,"k":"pick","meshes":0,"batches":183},{"t":69796,"k":"picked","hit":"structures:merged"},{"t":70151,"k":"pick","meshes":0,"batches":183}]}
```

## What the log says

- **The tab was killed, not closed** (`ended: null`): the last entry is a pick at t = 70.15 s and nothing
  after it. iOS gives no heap reading (`heap: null`), so this is most likely the memory kill T-2547's
  crash-aware boot exists for.
- **It was already at the floor**: boot `light@1` — Light detail, pixel ratio 1 (perhaps the step-down from
  an earlier crash). So the existing step-down does not save this path.
- **Where**: the Read started at t ≈ 65.06 s (the Navigator closed). `js/pacing-read.js` picks its poses
  from 1835 anchor ids (`lake_at_canal`, `lake_market`, `from_above`); 1904's scene has only
  `glessner_house` (1410.12, -3218.01, yaw 264.94 — the east sidewalk at E. 18th St facing **west**, across
  Prairie Avenue at the Glessner lot), so the walk fell back to it and walked straight west. The last
  sample is at **1390, -3220 — about 20 m west of the spawn, at or into the Glessner front**, during the
  first move (walk, Fixed), ~4–5 s in.
- **What was resident**: 103 draw calls, 549,763 triangles, 291 geometries, **741 textures**.
- The gaze pick ran every ~500 ms (183 batches, 15–25 ms each); the last completed pick took **166 ms**
  (69.63 → 69.80 s) — the page was already struggling just before it died.
- Boot to ready took **43.7 s** on this phone (noted; not this ticket's fix).

A visitor who simply walks across Prairie Avenue to the Glessner front on this phone would plausibly die
the same way: the tool only walked where a visitor walks.

## What to do

1. Reproduce on the runner at the phone profile, Light, ratio 1, with T-2546's memory meter
   (`tools/measure_memory.mjs`, the Prairie walk from T-2718): spawn → 20 m west facing west, plus a
   standing stop a few metres from the Glessner front. Read texture count and GPU texture bytes, geometry
   bytes and JS heap along the path. Find what arrives as the camera nears the house — e.g. T-2598's
   texture residency admitting the Glessner v4 full textures at close range, the KTX2 light tier (T-2596)
   not being the one used, render targets reallocated by the governor, or the pick pass allocating per pick.
2. Fix it so the resident memory along that path stays under the phone ceiling (T-2546's) with margin,
   at every Glessner distance a visitor can reach, without lowering the Glessner match records.
3. If the owner's phone can be read again, the same walk (T-2733 fixes the tool's 1904 path) no longer kills the tab.

## Second reproduction — the owner, 2026-10-19, minutes later

Same phone, same build (dev@a369c613), same steps; the tab died the same way. Verbatim:

```
{"page":"mvej54gs-q5ie","year":"1904","build":"DEV PREVIEW · dev@a369c613 · Oct 18, 2026, 6:28 PM CT","start":1792370540764,"ended":null,"last":{"t":58662,"calls":94,"tris":377414,"geo":291,"tex":741,"w":375,"h":636,"ratio":1,"heap":null,"at":"1375,-3221"},"entries":[{"t":0,"k":"boot","to":"light@1"},{"t":31553,"k":"ready"},{"t":34923,"k":"pick","meshes":0,"batches":183},{"t":34942,"k":"picked","hit":"structures:merged"},{"t":37712,"k":"pick","meshes":0,"batches":183},{"t":37723,"k":"picked","hit":"structures:merged"},{"t":37730,"k":"nav","level":1,"app":"home"},{"t":39148,"k":"nav","level":2,"app":"home"},{"t":42977,"k":"nav","level":2,"app":"settings"},{"t":54616,"k":"nav","level":0,"app":"settings"},{"t":55545,"k":"pick","meshes":0,"batches":183},{"t":55573,"k":"picked","hit":"structures:merged"},{"t":56062,"k":"pick","meshes":0,"batches":183},{"t":56087,"k":"picked","hit":"structures:merged"},{"t":56596,"k":"pick","meshes":0,"batches":183},{"t":56619,"k":"picked","hit":"structures:merged"},{"t":57109,"k":"pick","meshes":0,"batches":183},{"t":57131,"k":"picked","hit":"structures:merged"},{"t":57638,"k":"pick","meshes":0,"batches":183},{"t":57657,"k":"picked","hit":"structures:merged"},{"t":58157,"k":"pick","meshes":0,"batches":183},{"t":58177,"k":"picked","hit":"structures:merged"},{"t":58685,"k":"pick","meshes":0,"batches":183},{"t":58701,"k":"picked","hit":"structures:merged"},{"t":59236,"k":"pick","meshes":0,"batches":183},{"t":59396,"k":"picked","hit":"structures:merged"},{"t":59758,"k":"pick","meshes":0,"batches":183}]}
```

**Read across the two logs:**

| | first | second |
|---|---|---|
| boot → ready | 43.7 s | 31.6 s |
| Read starts (Navigator closes) | 65.06 s | 54.62 s |
| last sample | 67.74 s at 1390, -3220 | 58.66 s at 1375, -3221 |
| last completed pick | 166 ms (69.63 → 69.80) | **160 ms** (59.24 → 59.40) |
| page dies (last entry) | 70.15 s — **5.09 s** after the Read starts | 59.76 s — **5.14 s** after |
| textures / geometries in the last sample | 741 / 291 | 741 / 291 |
| triangles drawn in the last sample | 549,763 | 377,414 |

- **Deterministic**: both die ~5.1 s into the Read — 0.8 s rest at the spawn, then ~4.3 s into the first walk
  (Fixed). The walk moves ~10 m/s (20 m by 1.9 s into the walk; 35 m by 3.3 s), so the page dies **about
  40–45 m due west of the 18th Street spawn — at `poseFor`'s 40 m turn, inside or behind the Glessner
  House**, not at the curb.
- **Texture and geometry COUNTS do not climb** (741 / 291 in both, and the same in the samples before), so
  look at what grows in BYTES or in objects the counters do not see: a texture whose image is swapped for a
  larger one in place (residency, KTX2 tier), render targets, shader programs, or an interior/occlusion
  path that switches on when the camera is inside the house (`setGlessnerOcclusion`).
- **A ~160 ms pick precedes the death both times**, then one more pick starts and nothing follows. Usual
  picks are 15–25 ms. Find what that pick does differently at that pose (a program compile for a newly
  shown mesh, an allocation, a readback stall).
- The Read teleports through walls; a visitor walking has collision. Part of the fix is saying whether a
  visitor can reach the state that kills the page (the Glessner front at the curb, the courtyard, flying
  over and down into the house), and the fix must hold for every place a visitor can reach. T-2733 also
  takes the tool's walk off this path.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

- [ ] The kill reproduced on the runner at the logged poses (spawn → 40–45 m west, through the 40 m turn) as a measured over-ceiling reading (or, if the runner stays under the ceiling, the reading that shows which resource climbs toward the Glessner front), committed under `docs/measurements/`.
- [ ] After the fix, the same path and a stop 3 m from the Glessner front read under the phone ceiling with stated margin; the 1904 smoke passes at 390x780; Glessner's photo-match records unchanged.
- [ ] The gaze pick allocates nothing per pick (a test counts textures, render targets and materials across 20 picks).
- [ ] The crash log's `last` gains the texture/geometry byte estimate it can read, so the next phone crash says how much was resident, not only how many.
