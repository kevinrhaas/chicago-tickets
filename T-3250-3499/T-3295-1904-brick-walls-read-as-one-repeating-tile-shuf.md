---
id: T-3295
title: 1904 brick walls read as one repeating tile: shuffle K03 panel bricks per wall and vary each brick's colour
state: done
epic: META
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-11-01
closed: 2026-11-01
pr: 1579
claimed_by: run 11/1/2026, 10:45:23 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-11-01T21:22:46Z
claimed_run: null
claimed_at: 2026-11-01T16:45:24.586Z
decision: null
decision_answer: null
---

The owner, 2026-11-01, with an iPhone screenshot of a brick flank seen from 1825 S Prairie on the
dev preview (1904): *"this brick pattern appears too regular, is there anything you can do when
generating the brick textures to make them more random, the appear as a pattern and are too
consistent and repetitive"*. Project thread "Make brick textures less repetitive".

**Cause.** Every K03 brick wall in 1904 (34 GLBs wear `common_buff_common_6`, 3 wear
`rough_red_brown_running`, plus bays, areas, chimney soot and K11 walls) is one bonded panel of
4 modules x 12 courses, 0.86 x 0.80 m, repeated: a two-storey flank shows the same 48 bricks
about 150 times, and its few dark headers and burnt stretchers line up into a visible lattice.

**Fix (renderer, no new texture memory).** In the shader, find the brick each fragment is on
from the panel's own bond (tile-space, so it is right whatever offset a wall maps at), and draw
that brick's face from a different brick of the same kind in the panel, chosen by a hash of its
place on the wall; then give each brick its own small colour spread and add a broad, mean-neutral
mottle across the wall. 1904 is near the phone memory ceiling, so a bigger atlas was refused.

**Acceptance:**
- Before/after at 390x780 and 1280x800 of the owner's spot (a flank seen from 1825 Prairie) and
  one street view: no repeating lattice visible in the after.
- No extra texture, no extra draw call, no page error; mortar joints stay continuous.
- The bond layout the renderer uses is checked against `assets/textures/prairie_1904_brick/`
  (profiles.json + panel material.json) by the gate, so the two cannot drift.
