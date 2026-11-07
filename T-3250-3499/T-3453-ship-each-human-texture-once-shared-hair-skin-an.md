---
id: T-3453
title: Ship each human texture once: shared hair, skin and eye maps published as one file and decoded once on the GPU for every figure
state: done
epic: RENDERING
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-11-07
closed: 2026-11-07
pr: 1827
claimed_by: run 11/7/2026, 7:41:12 AM CT
blocked_on: null
needs_bake: false
closed_at: 2026-11-07T15:03:25Z
claimed_run: null
claimed_at: 2026-11-07T13:41:13.457Z
decision: null
decision_answer: null
---

Ship each human texture once: shared hair, skin and eye maps published as one file and decoded once on the GPU for every figure.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## Source (owner, 2026-11-07)

Kevin, thread "Glessner in person", after the wardrobe catalogue (T-3447..T-3451, PRs 1823, 1824) merged with none of
the five figures placed: *"Place all of them"*. The five figures' web GLBs were held off the published tree by
publish.sh because they took it over its 432 MB budget (450.9 MB in CI); about 50 MB of every human web GLB is the
same hair/skin/eye pictures embedded again in each file. T-3453 ships each picture once and decodes it once
(shared-images.js) so T-3452 can place all five within the site budget and the phones' memory ceilings.

**Acceptance:** all five figures drawn in town in their years, each instance graded with its sources or a liberty;
the published tree under its budget; the phone memory ceilings held; the gate green.
