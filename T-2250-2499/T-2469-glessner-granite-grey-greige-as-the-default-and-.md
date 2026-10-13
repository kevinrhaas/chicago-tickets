---
id: T-2469
title: Glessner granite: grey-greige as the default, and the other stone options removed
state: claimed
epic: SOUTH_TIME
requested_by: owner
seen: true
effort: S
legacy_id: null
parent: null
opened: 2026-10-13
closed: null
pr: null
claimed_by: run 10/13/2026, 10:37:18 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-13T15:37:18.933Z
decision: null
decision_answer: null
---

Glessner granite: grey-greige as the default, and the other stone options removed.

**The owner, 2026-10-13, after comparing T-2446's (#760) `?stone=` presets on dev:**
"I think it's probably grey - greige and we can use that as the default. You can cull the
others if you need to free up memory or space".

The bake cannot carry grey-greige: its linear tint is (0.90, 1.067, 1.166), and Blender's glTF
exporter clamps a baseColorFactor to 1 (checked 2026-10-13: 1.067 and 1.166 export as 1), so
baking it would darken the stone by about a tenth. The renderer keeps the retint instead.

**Acceptance:**
- With no option, Glessner's granite renders as grey-greige on the full and light models.
- `?stone=` and the other presets are gone; the retint is fixed, still held by
  check_glessner_stone.mjs to Glessner's five granite slots and to the generator's GRANITE_TINT.
