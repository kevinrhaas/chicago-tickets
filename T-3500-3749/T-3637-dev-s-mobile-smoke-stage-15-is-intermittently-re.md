---
id: T-3637
title: Dev's mobile smoke stage 15 is intermittently red on zero page errors: THREE.GLTFLoader couldn't load texture blob:… URLs after the Jump checks
state: open
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-17
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

Dev's mobile smoke stage 15 is intermittently red on zero page errors: THREE.GLTFLoader couldn't load texture blob:… URLs after the Jump checks.

## FILED ABOVE BAND 9, BECAUSE IT BLOCKS

A follow-up goes to the foot of band 9 unless dev's gate is red on it or the build in hand cannot finish without it (owner, 2026-09-27). This one was placed above band 9 on this reason:

> dev's content build is red on smoke (mobile, 15) on bare dev (runs 44047178090, 44076624959) and on every PR build that draws it, so PR #2149 (T-1894) and #2147 are refused on it

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

## Evidence (loop, 2026-11-17)

CI's `smoke (mobile, 15)` leg of the content build (`chicago-4d-bake.yml`) fails ONE check,
`mobile 390x780: zero page errors`, with every other check in the stage passing (33 passed,
1 failed). The page errors are all the same family:

    console.error: THREE.GLTFLoader: Couldn't load texture blob:http://127.0.0.1:4187/<uuid> | …

They come after the stage's last check, `?nav=jump opens Jump after the landing, and Back
closes it and stays on the page (T-2621)`; the suite body runs to completion.

| run | branch / sha | mobile 15 |
|---|---|---|
| 44047178090 | dev aa56ec430 | red, this error ([7:24]) |
| 44076624959 | dev 8bfbd9b1a | red, this error ([7:52]) |
| 44086546268 | #2147 8a5fef6c1 | red, this error ([6:22]) |
| 44094549003 | #2149 381ab3241 | red, this error ([5:18]) |
| 44060897694 | #2111 | green |
| 44085375860 | #2151 | green |

So it reproduces on bare dev and is intermittent: neither PR diff touches textures (#2149
rebakes one house's GLB, #2147 a monument figure). The texture loads look like blob URLs
revoked or failing under memory pressure, possibly when a Jump to another year unloads a
scene while its GLBs are still resolving textures. Find the cause; don't weaken the
zero-page-errors check to make it pass. Until then the leg can be re-run (`gh run rerun
<id> --failed`) once its build completes.
