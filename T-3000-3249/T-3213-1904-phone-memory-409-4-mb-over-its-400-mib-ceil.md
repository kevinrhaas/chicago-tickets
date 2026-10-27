---
id: T-3213
title: 1904 phone memory 409.4 MB over its 400 MiB ceiling on dev: the memory job never runs on dev pushes, so dev drifted over unseen; bring the 1904 phone scene back under 400 or argue a new ceiling in tools/memory_ceilings.json with its reading
state: open
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-27
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

1904 phone memory 409.4 MB over its 400 MiB ceiling on dev: the memory job never runs on dev pushes, so dev drifted over unseen; bring the 1904 phone scene back under 400 or argue a new ceiling in tools/memory_ceilings.json with its reading.

**Reading (2026-10-27, cloud container, `node tools/measure_memory.mjs --gate --year 1904 --only mobile` after publish.sh):** clean dev 0fc818209 read **409.4 MB** = js heap 114.8 + arraybuffers 81.5 + gpu buffers 156.7 + gpu textures 56.3. PR 1335's merged tree read 409.5 there, so that PR did not cause it; CI read the same tree at 417.4. The last reading under the ceiling was T-2828's 346.8 (2026-10-19). Between then and now, dev pushes added the 1904 streetscape and parkway work. `chicago-4d-frame-time.yml` runs only nightly on main and on pushes that touch its own tools/ceilings, so nobody saw the drift.

**Related:** T-3173 (desktop 1904 memory) claims a native phone reading of 385.3 MiB on its own branch (PR 1340, the farm wagon, held). If that work lands, re-read before starting here.

**Acceptance:** `measure_memory.mjs --gate --year 1904 --only mobile` reads under the 400 MiB ceiling on current dev, in CI (the memory (1904, mobile) job green on the PR); or a new ceiling is argued in tools/memory_ceilings.json with its reading, per the file's rule. No other memory row rises.
