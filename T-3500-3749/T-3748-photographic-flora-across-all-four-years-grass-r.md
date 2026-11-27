---
id: T-3748
title: Photographic flora across all four years: grass, reeds, flowers, shrubs, vines and garden crops
state: claimed
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-11-25
closed: null
pr: null
claimed_by: Better Trees season pass 11/26/2026, 11:50:23 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-27T05:50:24.009Z
decision: null
decision_answer: null
group: T-3748,T-3760
---

Continuation of the owner's Better Trees request supplied 2026-11-25: "All trees and flora everywhere should get this upgrade." T-3747 owns shared woody rendering; this piece owns herbaceous flora, grass/reeds, flowers, low shrubs and garden crops, reusing the same leaf-lighting principles where appropriate.

The owner explicitly added "dont forget about all the seasons" during implementation. Seasonal review found two existing gaps: 1871 hides the Season control, and the grown-tree evergreen tint cutoff still assumes a five-row leaf atlas even though the atlas now has six rows. Include these fixes here: four-season free roam in every year, with dated Great Fire jaunts retaining their historical date and restoring the visitor's season afterward; conifer foliage must retain its evergreen colour in winter.

**Acceptance:**
1. Improve visible leaf/blade/petal surface shape and lighting in the existing flora and garden renderers, with fixed-camera before/after images. Retain species, placement/exclusion rules, historical provenance, bloom and seasonal controls.
2. Preserve the inexpensive Light path and the existing density/LOD/instancing/texture compression controls. Compare all three tiers' triangles, calls, memory and relative frame timing; no unmeasured low-power or high-end FPS claim.
3. Demonstrate grass/reeds, broadleaf plants, flowers and garden crops in the published app across 1812, 1835, 1871 and 1904 at phone and desktop viewports. Check sun/shade/night, Confidence view and season changes with zero browser errors.
   Exercise spring, summer, fall and winter explicitly: deciduous leaf cover, evergreen colour, grass/reed senescence, flowers and crop phenology, snow and restoration after dated jaunts. Enable the Season control in 1871 free roam and preserve the Great Fire's documented October 1871 times.
4. All four local check.sh parts, PR preflight questions, required CI and mapped published smoke pass before merge to dev. Keep artistic reconstruction declarations, evidence, STATUS and What's New accurate. No paid assets/tools or renderer migration.
