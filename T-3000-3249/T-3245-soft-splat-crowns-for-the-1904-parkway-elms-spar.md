---
id: T-3245
title: Soft splat crowns for the 1904 parkway elms (Spark renderer, behind Settings > Trees, off by default)
state: withdrawn
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-29
closed: 2026-10-29
pr: null
claimed_by: run 10/29/2026, 2:09:18 PM CT
blocked_on: prototype looked worse than the leaf cards at 1.56M splats for 38 trees; see Result
needs_bake: false
closed_at: 2026-10-29T20:15:14.916Z
claimed_run: null
claimed_at: 2026-10-29T19:09:20.016Z
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

## Result, 2026-10-29 — withdrawn: not productive

Prototype on the published 1904 app (desktop, full detail), Prairie looking south from 1801 and up into the
crowns. Each parkway elm within 60 m got a Spark `SplatMesh` built from its own grown skeleton's leaf clumps
(tree-model.js `buildTreeTemplate(...).skeleton.clumps`, coloured with the clump shading the leaf cards use),
sharing one `PackedSplats` per variant; the leaf-card batches were hidden in the colour pass only, so the street's
dappled shade was unchanged.

- Two tunings (8 splats a clump at 0.32 r; 24 at 0.14 r). The second: about 41,000 splats an elm, **1.56 million
  splats for 38 trees** — already over Spark's own iPhone budget (1.5M) for a 60 m radius, before the other ~370 elms.
- **It looked worse.** Procedural splats from clump positions read as dense, soft green masses with no leaf, no
  sky through the crown and no light through the blades; today's leaf cards (real elm sprays from the atlas) read
  far more like the owner's photographs. Splats look photographic when they are TRAINED from photographs of the
  thing; generated from a model, they only blur it.
- Spark itself worked inside the app on three 0.185.1 (zero page errors), but needed an explicit
  `spark.update({ scene, camera })`: the app's held-loop draw never triggered Spark's own update.
- Nothing was committed to the code repo; there is nothing to roll back.

Side-by-sides: project folder `marble-spark-assessment/splat-crowns-vs-cards-*.jpg`. Revisit only with captured
(photo-trained) splats of real elms, whose licence and 1904 fit are their own question.
