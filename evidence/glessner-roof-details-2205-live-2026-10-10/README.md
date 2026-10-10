# T-2205 live dev verification

PR #601 merged to dev at `145a1ddcd4da65b9e77c9fc60308af5458a1f3cb`.
The live build stamp served `145a1ddc`. Actual /4d/dev/1904/ desktop Full
1280×800 and mobile Light 390×780 boot and ridge-east review both pass:
zero browser errors, zero failed asset responses, dark glass and valid budgets.
Both served GLBs match the reviewed Full/Light SHA-256 hashes, recorded here.

The final integrated local preflight passed all 806 repository steps plus
changelog-entry and ticket-ID checks before the final integration commit
`83acd42e30a8a076754f7981611111bc6cce8912`. Integration regenerated the
roof-ID inventory because the committed validation transcript names two old IDs;
no roof asset changed. CI status is checked separately and not inferred from
these browser results. No main promotion.
