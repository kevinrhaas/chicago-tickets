---
id: T-3395
title: Printable 3MF export of a structure (Glessner House first): watertight standalone solid for FDM
state: claimed
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-05
closed: null
pr: null
claimed_by: run 11/5/2026, 5:13:37 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-05T23:13:38.597Z
decision: null
decision_answer: null
---

Printable 3MF export of a structure (Glessner House first): watertight standalone solid for FDM.

The owner, 2026-11-05: "could you make a printable 3mf file for me to print a standalone watertight print of the glessner house? just the structure of the house of course, this may be something we will want to do for other structures at some point"

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
- A reusable tool, `tools/export_print_3mf.py`, exports any structure's GLB (by structure id or path) as a 3MF in millimetres.
- The Glessner House output is one closed piece: every edge shared by exactly two triangles in opposite directions, positive volume, one shell, no flat triangles or doubled vertices; checked by the tool and independently by a second reader.
- Only the structure: lawn, turf, drive and vines dropped; ground clutter away from the walls dropped; nothing floating.
- FDM-printable as stated: scale, minimum feature and base written down (docs/PRINT-3MF.md); thin parts thickened to the minimum.
- A gate test proves the method on a toy leaky house; the .3mf is delivered to the owner (not committed).
