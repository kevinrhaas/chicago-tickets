---
id: T-3245
title: Soft splat crowns for the 1904 parkway elms (Spark renderer, behind Settings > Trees, off by default)
state: open
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-29
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

Owner, 2026-10-29 (project thread "Assess other 3D project for reuse"), on the World Labs Marble / Spark assessment: *"ok sounds good lets try it out and roll things back if its not productive, i want to improve things best we can if this will work, but dont want to break things"*. Assessment: https://claude.ai/artifact/S5EdbiYNSKK2QrNLU4kAaW; spike files in the project folder `marble-spark-assessment/`.

Today's 1904 parkway elm crowns (street-trees.js on tree-model.js, instanced by tree-instances.js) are solid meshes that
read as boulders up close (RENDERING.md §1 item 6). Spark (`@sparkjsdev/spark`, MIT, World Labs' open Gaussian-splat
renderer for three.js) runs on our vendored three 0.185.1 through the existing import map with zero errors (measured
2026-10-29). This ticket draws the same crowns as soft splats, generated from our own tree builder, so nothing comes
from Marble and nothing is fetched at runtime.

**Plan**
- Vendor Spark 2.4.0 under `renderers/web/vendor/` (pinned, sha256 in MANIFEST + MANIFEST.sha256, `assets/LICENSES.md`
  if it counts), plus three's `addons/postprocessing/Pass.js` from the same 0.185.1 tarball. Imported lazily, ONLY when
  the setting is on, so a visitor with it off loads not one byte more.
- Generate crown splats from the existing crown geometry and leaf colours (no new claims about 1904: same species,
  colours, positions, season); bake sun-side light and inner-crown shade per splat. Share one splat set across the
  instances. Keep the crown mesh as a depth-only shadow caster so the shadows on houses and walks do not change.
- Settings › Trees gains a "soft crowns" look, OFF by default. summer / spring / winter / hidden keep working.

**Acceptance** (kill criteria, written before code; if any fails, the setting stays off or the change is withdrawn)
- With the setting off: zero change. Same smoke, same memory readings, no Spark bytes loaded.
- With it on, 1904 phone (`measure_memory.mjs --year 1904 --only mobile`) adds no more than 15 MB and stays under
  its ceiling, or the PR argues the number.
- Zero page errors at 390x780 and 1280x800 with it on and off.
- A side-by-side down Prairie at 18th (on/off) attached to the PR; tapping a tree still picks it; confidence view
  still tints trees.
- Owner reads the moving frame time on his iPhone before it is ever made a default.
