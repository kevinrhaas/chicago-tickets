---
id: T-2786
title: 1904 still restarts on an iPhone after T-2775: the railway's strip scratch and every building's source geometry stay reachable after their batches are built
state: claimed
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-10-18
closed: null
pr: null
claimed_by: run 10/18/2026, 11:22:20 AM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-10-18T16:22:20.305Z
decision: null
decision_answer: null
---

1904 still restarts on an iPhone after T-2775: the railway's strip scratch and every building's source geometry stay reachable after their batches are built.

## FILED OVER THE BUDGET, AND HERE IS THE REASON

The ticket budget refused this: the queue stands at 144 lines, at or over its ceiling of 140. It was filed anyway, on this reason:

> Owner, 2026-10-18: dev still restarts in Chrome and Safari after PR 1018; measured 696 MB at the phone spawn, 74 MB of it railway scratch arrays and ~75 MB building source geometries

**Owner, 2026-10-18 15:47 UTC (iPhone, Chrome, then Safari, on chicago.polecat.live/4d/dev/1904/ after PR 1018):** "when I landed I did free roam still navigated and just a bit of moving and then it restarted".

**Found** (heap snapshot of the 1904 phone spawn on dev a71a7a3e, aggregated by retainer):
- 74 MB of plain JS arrays: the railway's strip scratch (`bed`, `cinders`, … pos/uv/col/conf), context-allocated in createRailway and kept alive by its update and pick closures long after the meshes were laid.
- 37,288 source BufferGeometries (~50 MB of typed arrays, ~25 MB of heap objects): buildings.js `groups` buckets kept every entry after `batch.addGeometry` copied it; `geo.dispose()` frees only GPU state, and `groups` lives as long as the layer. This is in every year.

**Acceptance:**
1. Both scratch sets emptied once used; nothing reads them after.
2. Every year x viewport's resident estimate at spawn falls, zero page errors; ceilings lowered by memory_ceilings.json's rule; the ?keep-geometry=1 self-test still reads over the 1835 mobile ceiling.

**Result:** one invocation, all six rows (docs/measurements/T-2786-memory.json): 1904 mobile 696.4 -> 516.3 MB (js heap 210.7 -> 79.5), 1904 desktop 1328.9 -> 1133.9, 1835 mobile 581.5 -> 489.8, 1835 desktop 1577.6 -> 1195.5, 1812 mobile 245.7 -> 191.7, 1812 desktop 626.8 -> 541.1. Self-test 622.8 MB over the new 550 MiB.
