# T-3040 recoverable checkpoint

WIP, not a green or completed model-match claim. Six agents reviewed T-2372 through T-2388; findings are in the archived docs/RESEARCH/fort-reference-groups-T-3040/README.md and on the tickets.

The code prerequisite renders complete fort groups and fingerprints every member mesh and placement. Both actual baselines say differs. T-3041 and T-2388 retain the matching work.

To recover: inspect and preserve the existing code worktree first. On the checkpoint base_commit from checkpoint.json, extract work-in-progress.tar.gz outside the checkout, apply changes.patch with git apply, then copy new-files/ into the code checkout, preserving its paths. Never overwrite existing user changes blindly. Install/start instructions are saved in the environment draft; use a physical sparse tickets clone (not a symlink). No credentials are included.

Full preflight was still running when this checkpoint was saved. Read checkpoint.json and run the remaining checks before committing code, opening the PR, or merging dev. The archive is a recovery artifact, not a request to revert newer work.
