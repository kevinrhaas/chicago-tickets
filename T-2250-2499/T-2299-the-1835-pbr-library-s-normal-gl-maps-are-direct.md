---
id: T-2299
title: The 1835 PBR library's normal_gl maps are DirectX-handed too: generate_1835_pbr_library.py writes (-dh/dx, -dh/drow, 1), all 27 maps read green -0.80..-1.00 against their height16, and frontage, roof-relief, wall-relief, signage and ground-strip bind them
state: open
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-10
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

The 1835 PBR library's normal_gl maps are DirectX-handed too: generate_1835_pbr_library.py writes (-dh/dx, -dh/drow, 1), all 27 maps read green -0.80..-1.00 against their height16, and frontage, roof-relief, wall-relief, signage and ground-strip bind them.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)
