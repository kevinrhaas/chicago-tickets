# Parallel image-match proposal recovery

Latest immutable checkpoint: **2026-10-23 05:34:15 UTC**, version `20261023T053415Z`.
These archives preserve concrete patches, source credits/rights findings, copied
records, actual exported proof and reviewed images from the parallel work. They
are recovery evidence, not a completed image match or an instruction to apply every
patch. Original image-match tickets stay open. Parent integration, derivatives,
current official hashes and full repository gates remain separately owned.

The evidence checkout was clean at intake and was fast-forwarded to
`a232d391638862127a0dfee2a8683e2c1a0fb3a3` before adding this directory. No ticket
status, claim, queue, board or official model repository file was changed by this
checkpoint. Existing recovery directories are retained. Every archive has a
versioned name; later saves must retain these names and add a new version.

## Archives, sizes and current recovery state

| Package | Bytes | MB (decimal) | Recovery state |
| --- | ---: | ---: | --- |
| [fort-combined](fort-combined--REVIEWED_DIFFERS--20261023T053415Z.tar.gz) | 24,773,995 | 24.774 | REVIEWED_DIFFERS — 25 baseline+25 proposed pinned exports;6 historical comparisons+8 diagnostics;10 changed masters; full integration remains |
| [frame_tavern-combined](frame_tavern-combined--REVIEWED_DIFFERS--20261023T053415Z.tar.gz) | 5,644,200 | 5.644 | REVIEWED_DIFFERS — Canonical pinned previews for Tremont,GreenTree,Sauganash plus committed same-camera before captures;23master family integration remains |
| [frame-gable-cladding](frame-gable-cladding--REVIEWED_DIFFERS--20261023T053415Z.tar.gz) | 4,439,243 | 4.439 | REVIEWED_DIFFERS — Incremental patch over frame_tavern-combined;2 actual source/before/after panels;23master family integration remains |
| [log-combined](log-combined--REVIEWED_DIFFERS_ORIGINAL_FROZEN--20261023T053415Z.tar.gz) | 25,095,734 | 25.096 | REVIEWED_DIFFERS_ORIGINAL_FROZEN — Original immutable81master package and20261023-050224-069556 run; active boarding-refinement excluded; first Miller joints too faint |
| [T-2375-next](T-2375-next--REVIEWED_DIFFERS--20261023T053415Z.tar.gz) | 5,886,299 | 5.886 | REVIEWED_DIFFERS — Second Dearborn bridge raw pinned preview plus actual committed prechange capture;6master official family refresh remains |
| [T-2380-rights](T-2380-rights--HOLD_UNBAKED--20261023T053415Z.tar.gz) | 6,540,200 | 6.540 | HOLD_UNBAKED — Detailed jail source rights unresolved; institutional catalogue is not affirmative reuse licence; no geometry bake |
| [T-2380-andreas-pd](T-2380-andreas-pd--HOLD_UNBAKED--20261023T053415Z.tar.gz) | 7,098,774 | 7.099 | HOLD_UNBAKED — Independent1884public-domain page evidence; does not clear held detailed engraving or identify/date depicted rear core forJuly1835 |
| [T-2380-next](T-2380-next--HOLD_UNBAKED--20261023T053415Z.tar.gz) | 26,126 | 0.026 | HOLD_UNBAKED — Concrete held unbaked geometry proposal;do not apply,bake,derive or append liberty until rights and identity/date bounds resolved |
| [offscene-phase-audit](offscene-phase-audit--AUDIT_ONLY_UNEXECUTED_WRAPPER--20261023T053415Z.tar.gz) | 5,221 | 0.005 | AUDIT_ONLY_UNEXECUTED_WRAPPER — Pipeline audit and standalone exact-phase wrapper; no later phase/build/scene or accepted match created |

All nine archives are below 95 MB. The combined log snapshot retains its original
immutable candidate and run `20261023-050224-069556`; active `boarding-refinement/`
is deliberately excluded and needs a separate later checkpoint when ready. Its
review honestly records Miller boarding as too faint. The frame-gable patch is
incremental over frame_tavern-combined, and the two bridge patches are alternatives
(cumulative versus delta), not a pair to apply together. Read each package's
handoff and source/date limits before integrating.

**T-2380: HOLD_UNBAKED applies to all three jail recovery packages.** The detailed
Keystone/Tribune-derived source remains `check_required`; do not apply the held
geometry/liberty or bake/derive from it. The independent Andreas1884 plate has a
public-domain basis but does not clear the other source, identify the rear cell
as the original1833 core, or establish its presence before July1835. The PD
research offers no ready geometry patch. Older unverified claims preserved inside
`pre-rights-review/` are superseded and must not override this hold.

The off-scene audit preserves an unexecuted exact-phase research wrapper and its
pipeline findings; it creates neither a later town scene nor an accepted phase
asset. Fort comparisons still differ, particularly in provisional camera framing,
first-fort lanterns/arrangement, and lighthouse width/height. Fort rebuilds also
record five UV-only differences against committed bytes; all25 fresh before/after
controls and GLB-contract reports are retained.

## Integrity

Each source file was hashed before archiving and checked unchanged afterward.
Every archived regular-file payload was read back and verified against that source
hash. Tar members use relative package paths. Symlinks are stored as links and were
**not dereferenced**. Node dependencies, Blender installations/configuration,
Python caches, the abandoned log run, and superseded wrong-seed frame renders are
excluded. Actual current proof, paired source/model renders, patch/source credit
and rights findings are retained. `ARCHIVE-FILES` lists every retained file hash
and link target; `MANIFEST` records exclusions, file counts and archive hashes.
Some original receipt inventories mention intentionally omitted cache/superseded
files; this checkpoint's inventories define the archive payload.

The packages are not standalone runtime installations: working Node/Blender
versions and renderer checkout dependencies must be restored separately. Some
research runner paths retain their original absolute /tmp location. Extract into
a separate recovery directory, inspect existing external link targets and adapt
paths before running anything. Do not extract over a live model checkout or copy
filtered fixture manifests over its complete registry. Never promote provisional
research cameras to accepted reference views merely to pass a gate.

- [Latest manifest](MANIFEST--20261023T053415Z.json)
- [Retained file inventory](ARCHIVE-FILES--20261023T053415Z.json)
- [SHA256SUMS](SHA256SUMS--20261023T053415Z.txt)

Verify from this directory with:

```sh
sha256sum -c SHA256SUMS--20261023T053415Z.txt
```

| Archive | SHA256 |
| --- | --- |
| `fort-combined--REVIEWED_DIFFERS--20261023T053415Z.tar.gz` | `b9d04e39a7d60c3b820af2e004dc66e82613e503aab8212a74bf86d63c9e3da6` |
| `frame_tavern-combined--REVIEWED_DIFFERS--20261023T053415Z.tar.gz` | `cce6592c99b1c9f5f29e21fead84872388167752fe63820dcb23ce507c23f191` |
| `frame-gable-cladding--REVIEWED_DIFFERS--20261023T053415Z.tar.gz` | `728c0d4709acac2d62937eeceebd17c5e1fb0b4a8a5517513bf441d3720534fc` |
| `log-combined--REVIEWED_DIFFERS_ORIGINAL_FROZEN--20261023T053415Z.tar.gz` | `c7c8f74232c0b25b394aecf2de4ce2d53d9869e0f6cec96582ccc9fd7d1c6ddc` |
| `T-2375-next--REVIEWED_DIFFERS--20261023T053415Z.tar.gz` | `839d21e55bf9a9b931b8bae54e3254ba69c2faf0291e10aa724ed841cdd48aa9` |
| `T-2380-rights--HOLD_UNBAKED--20261023T053415Z.tar.gz` | `87dc2825efc2af4b46d3dbb2cf45ab562532629418ad21e16b3b2c83c7f6c768` |
| `T-2380-andreas-pd--HOLD_UNBAKED--20261023T053415Z.tar.gz` | `c8167ede8fd0f1d28bf385cf3229534f555b0f3b30204b9c631b9eccba5a2446` |
| `T-2380-next--HOLD_UNBAKED--20261023T053415Z.tar.gz` | `fe27524db40fd3b05c6237e43d432ebf9bc98f0fa90a13be3d6ce359706658a1` |
| `offscene-phase-audit--AUDIT_ONLY_UNEXECUTED_WRAPPER--20261023T053415Z.tar.gz` | `b8c1a69a2f04943cddd137cac2750f96ff180ea360189d1d2cbd6d75ad68ee9d` |
