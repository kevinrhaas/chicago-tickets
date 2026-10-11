---
id: T-2368
title: The image gate: every building is built until it matches its photographs and drawings, and its ticket closes only then
state: claimed
epic: SOUTH_TIME
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-11
closed: null
pr: null
claimed_by: run 10/11/2026, 2:38:28 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-11T19:38:28.784Z
decision: null
decision_answer: null
---

The image gate: every building is built until it matches its photographs and drawings, and its ticket closes only then.

Owner, 2026-10-11 (thread "1612 Prairie vs its photo"):
- "if you have any views of the house those should be validated against in development"
- "if you have an image you should work towards it until it's a photographic representation of any images even drawings are ok, but it should look exactly perfectly like the image or drawing"
- "For every building ... update all the tickets with that clarity and redo any work already done to meet this high standard"
- "you don't wrap the case until it matches the photo not that you can't change one without a photo"
- He chose the public repo for the pictures, and asked to bring photos from chicagology and other sites in with attribution.

**Acceptance:**
- `data/reference_views/<structure_id>/<view>.json` holds one camera per picture, and `tools/photo_match.mjs` writes a match record beside it: the GLB and camera sha, the side-by-side, a verdict and the differences.
- `tools/image_gate.mjs` reads the records. `ticket.mjs done` refuses a ticket whose `## Image gate` section names a building that does not match every view. check.sh fails only on a malformed file. A self-test covers the refusals.
- AGENTS.md hard rule 11 and `data/reference_views/README.md` state the rule. The Prairie image README allows attributed reference copies.
- 1612 Prairie is the first building on it, with its honest verdict ("differs") and its open differences carried by T-2369.
- In the tickets repo: every open building ticket carries the gate, and every building already built from less than its pictures has a redo ticket.

## Image gate

