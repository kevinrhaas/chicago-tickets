---
id: T-2563
title: Cloud sessions install the gate's Python readers at start (a SessionStart hook), so check.sh is not red for a missing scipy (owner, 2026-10-16)
state: done
epic: META
requested_by: owner
seen: false
effort: XS
legacy_id: null
parent: null
opened: 2026-10-15
closed: 2026-10-15
pr: 858
claimed_by: run 10/15/2026, 11:39:11 PM CT
blocked_on: null
needs_bake: false
closed_at: 2026-10-16T04:50:11Z
claimed_run: null
claimed_at: 2026-10-16T04:39:11.395Z
decision: null
decision_answer: null
---

Cloud sessions install the gate's Python readers at start (a SessionStart hook), so check.sh is not red for a missing scipy (owner, 2026-10-16).

The owner, 2026-10-16, after T-2552's first gate run went red on `ModuleNotFoundError: No module named 'scipy'` in a cloud session: "yes add the setup step for scipy".

## Acceptance

- `.claude/hooks/session-start.sh`, registered in `.claude/settings.json`, installs CI's own set (`jsonschema pyproj openpyxl pypdf numpy scipy Pillow`, as in `chicago-4d-check.yml`) in cloud sessions only (`CLAUDE_CODE_REMOTE=true`), skips pip when every module already imports, and exits 0 locally.
- Proven: with scipy uninstalled the hook restores it, `check_gate_readers.py` under `C4D_GATE_REQUIRE_READERS=1` is ok, and `trace_prairie_1904_footprints.py --check` passes.
