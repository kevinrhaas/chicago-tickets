---
id: T-1380
title: A squash merge dropped a shipped release note and re-used its version: v971 named 'Six dates that would not stick' on dev at 06:06 and names 'How many people each tavern and boarding house could sleep' at 06:31, and the first entry is gone from the file the launcher and Manager parse
state: claimed
epic: META
requested_by: loop
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-09-19
closed: null
pr: null
claimed_by: run 10/4/2026, 1:57:05 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: https://github.com/kevinrhaas/polecat-platform/actions/runs/37226195936
claimed_at: 2026-10-04T18:57:05.405Z
decision: null
decision_answer: null
---

A squash merge dropped a shipped release note and re-used its version: v971 named 'Six dates that would not stick' on dev at 06:06 and names 'How many people each tavern and boarding house could sleep' at 06:31, and the first entry is gone from the file the launcher and Manager parse.

**Acceptance:** (state it before working — the definition of done, never weakened to pass)

**Found by T-1367**, resolving its own changelog conflict against a moved `dev`.

`git log -S "Six dates that would not stick"` names two commits: `5fc0e7507` (T-1366,
PR #1502) added the entry as **v971**, ts `2026-09-19T06:06:11.774Z`; `a1fecdb70`
(T-1370, PR #1504) removed it. #1504 branched before #1502 merged, and its changelog
resolution took its own side of the file whole — so the entry that shipped an hour
earlier is gone from `origin/dev`, and **v971 now names T-1370's release instead**.

`grep -c "Six dates that would not stick"` on `origin/dev`: 0.

This is the failure the version contract is built to prevent, arriving from the other
direction. The house rule (author `v: null`, let the repo's stamp tool assign after the
merge) stops two branches CLAIMING the same number; it does nothing about a merge that
DELETES a stamped entry and frees its number to be re-assigned. `check-changelog.mjs`
reads the file it is given and cannot see an entry that is no longer in it.

`.gitattributes` does not carry `merge=union` for this path — the merge conflicted rather
than unioning, which is what left the resolution to a branch that could not see the entry.

**What is at stake:** Manager and the launcher parse the published `changelog.js` live, so
a version number that changes meaning after it has been ingested is a fact about a release
that is now wrong in two places.

**Acceptance:** (state it before working — one demonstration, never weakened to pass)

1. The lost entry is back and every version number names exactly one release, forever —
   the ordering question is the real one: the entry's `ts` (06:06) puts it BELOW v971
   (06:31), so it cannot simply take the next number off the top. State the rule chosen.
2. A merge that DROPS a stamped entry is loud. `check-changelog.mjs` (or a gate beside it)
   fails when a version present in the merge base is absent from the result — with a
   firing self-test.
3. Consider `merge=union` in `.gitattributes` for `renderers/web/js/changelog.js`, which is
   what the fleet contract assumes is already there.

## Finding, 2026-10-04 (T-1355's run, PR #403) — the same file now carries one release TWICE

`origin/dev`'s changelog holds "Kelsey's boarding-house on the sand hills is painted
yellow" as both **v1411** (2026-10-04T08:31Z) and **v1397** (2026-10-03T03:36Z).
`git log -S` names #380 (T-1724) and #393 (T-2070). This is the opposite failure from the
one this ticket was filed for: a version that no longer names a release, rather than a
release that has lost its version. `check-changelog.mjs` passes the file, because its
duplicate rule reads `v` and not the title. The changelog merge driver then re-adds BOTH
copies on top of a branch's own entry as if they were "ours'" (measured on #403:
"3 entry(s) of ours placed on top" for a branch that wrote one). #403 rebuilt its file
from dev's copy with one entry on top. A duplicate-title rule in `check-changelog.mjs`
would catch it, and so would this ticket's acceptance 2 read for titles.

## Finding, 2026-10-04 (steward run, while resuming #400)
The same family of fault, the other way round: after #404 (T-2080) squash-merged into `dev`
at about 11:33Z, `renderers/web/js/changelog.js` on `dev` carried **the same entry four
times** — "Kelsey's boarding-house on the sand hills is painted yellow" as v1421, v1422,
v1423 and v1424, all with one `ts` (`2026-10-04T11:33:38.774Z`), above v1425.
`check-changelog.mjs` read the file as "contract OK", so nothing asserts that one entry
is not repeated under several version numbers.
