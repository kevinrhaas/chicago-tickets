---
id: T-2464
title: Prairie Avenue 1904 opens on an iPhone again: houses share their identical stone, brick and wood images instead of each decoding its own copy
state: done
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-13
closed: 2026-10-13
pr: 773
claimed_by: run 10/13/2026, 8:45:23 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-13T15:26:42Z
claimed_run: null
claimed_at: 2026-10-13T13:45:23.818Z
decision: null
decision_answer: null
---

Prairie Avenue 1904 opens on an iPhone again: houses share their identical stone, brick and wood images instead of each decoding its own copy.

**Reported:** owner, 2026-10-13, on the dev preview in Chrome on an iPhone: "Can't open this page" (the tab killed for memory).

**Evidence (phone profile: Chromium 390x780, DPR 3, touch, iPhone UA; whole-browser PSS sampled every 200 ms through boot):**

| build | 1835 peak | 1904 peak | 1904 GPU process | 1812 peak |
|---|---|---|---|---|
| release-v1562 (31768a18) | 1860 MB | 889 MB | 440 MB | 873 MB |
| release-v1726, prod (5f6aa051) | 2039 MB | 1769 MB | 1034 MB | 868 MB |
| dev (61167f64) | 2027 MB | 2285 MB | 1471 MB | 863 MB |

The Prairie Avenue houses built on the K01/K16 kits each embed the kit's maps in their own GLB, and GLTFLoader shares an image only within one file. On dev the 1904 houses decode 666 MB of images (RGBA, no mips) of which 92 MB are distinct (limestone_basecolor, a 2048² map, 19 times; common_buff 17 times; painted_wood 6). The GPU then holds each copy again with mipmaps. Separately, each loaded building kept its GLTFParser, which holds the GLB's whole binary chunk and every buffer view slice (26.5 MB for Glessner's light model alone).

The landing page and the time-machine home page were ruled out (the home page's growth in Chromium is collectable Blink GC garbage, and WebKit is refcounted).

**Acceptance:**
- An embedded image whose bytes match one already decoded for the scene is decoded once and shared (a texture clone shares `source`, so three.js uploads it once).
- A shared ImageBitmap is closed only when the last asset holding it is disposed.
- 1904's phone-profile peak drops well below dev's 2285 MB; 1835 and 1812 do not get worse.
- Pictures are pixel-identical to dev on phone and desktop (Glessner viewpoint plus 1612, 1613, 1620, 1634 Prairie).

**Result (branch):** 1904 peak 2285 -> 1342 MB, GPU process 1471 -> 644 MB, settled JS heap 397 -> 303 MB; 1835 2027 -> 1963 MB; 1812 unchanged (874 MB). All ten screenshots identical to dev (max channel difference 0).
