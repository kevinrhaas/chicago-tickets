---
id: T-2183
title: Glessner courtyard window proportions, continuous rear eave and dark glass default
state: claimed
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-08
closed: null
pr: null
claimed_by: owner-requested recovery 10/8/2026, 1:49:49 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-08T18:49:49.332Z
decision: null
decision_answer: null
---

Glessner courtyard window proportions, continuous rear eave and dark glass default.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 146 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> New explicit owner correction after T-2172 merged: resize principal and upper wing windows, verify rear courtyard eave against research images, and apply dark glass at every detail setting.

**Acceptance:** Tower principal windows share the north-court first-floor sill/head; upper courtyard windows have the shorter proportions supported by HABS photo 05 and owner photographs; the rear eave reads continuously into the tower roof. Dark glass is default at all scene detail levels with the existing override retained. Rebuild canonical master/full/light assets, review desktop/mobile captures, pass repository gate and merge into dev.

**Recovery:** Branch `steward/glessner-courtyard-windows`, based on dev `3f326a6`. Follow-up to merged PR #520/T-2172. Existing research at `chicago/prairie_1904_v1/research/public/`; source `chicago/4d/data/structures/glessner_house.json`. Direct Git writes lack authentication; use the GitHub connector for checkpoints. Owner attachments visually read in this session; do not republish them.
