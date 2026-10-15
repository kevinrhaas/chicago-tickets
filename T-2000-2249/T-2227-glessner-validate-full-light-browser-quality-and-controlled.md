---
id: T-2227
title: Glessner: validate full/light browser quality and controlled performance
state: blocked-tech
epic: SOUTH_TIME
requested_by: owner
seen: true
effort: M
legacy_id: null
parent: null
opened: 2026-10-09
closed: null
pr: null
claimed_by: null
blocked_on: T-2226 — one Glessner House PR at a time (owner, 2026-10-11: group released to the loop and chained so lanes do not rebuild the same house in parallel)
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: null
decision: null
decision_answer: null
---

Owner instruction, 2026-10-09 UTC:

> Ok go ahead and file and create tickets for all of this and put them in a group below the people and comment the group out so we can take these tickets manually one at a time

**Manual hold:** This ticket is filed and approved as planned work, but is not released for automated execution. Its `blocked-owner` state represents the owner's explicit scheduling hold, not an unanswered research question. Keep its queue entry commented in the Glessner group below portable humans. Release only the ticket the owner selects; never activate the whole group.

**Released to the loop (2026-10-11):** the owner lifted the manual hold on the whole Glessner group: "Move all the Glessner house refine tickets below 2352 and un comment them for the loop to pick them up put them above 2341". This supersedes the manual-hold paragraph above and the "release and claim only after the owner selects this specific ticket" line below. The group runs one at a time in audit order (T-2201, then T-2207 through T-2228), ranked in band 7 below T-2352 and above T-2341. It waits as blocked-tech on T-2226; settle reopens it in T-2226's queue line when that PR merges.

**Audit item:** GA-25 • **Priority:** P1 • **Basis:** Completion gate

[Programme index and release procedure](../evidence/glessner-exterior-audit-2026-10-08/README.md) · [Reviewed audit PDF](../evidence/glessner-exterior-audit-2026-10-08/glessner-exterior-audit.pdf) · [Source coverage ledger](../evidence/glessner-exterior-audit-2026-10-08/coverage-ledger.csv)

## Scope and finding

This audit checked 1600×1000 full desktop stills only. Captures booted without page errors or failed requests and reported within-budget draw/triangle counts; paused animation means FPS=0 is not a performance measurement.

Reuse the metric/browser contract for full and light assets, motion, desktop and mobile. Test distance transitions, texture filtering, clipping, picking and actual frame timing after visual work.

**Bound:** Exterior and courtyard only, including stable, house boundary, immediate ground interfaces and exterior-visible glazing. Target **1904-07-01**. No furnished interiors. Preserve the T-2183 / PR #540 fixes and the owner-selected dark glass default. Never introduce later alterations or preliminary unbuilt designs as 1904 facts. Record attested/inferred/reconstructed provenance and rights before deriving assets. Missing measurements may be bounded reconstructions, explicitly labeled; missing rights do not authorize derived assets.

## Acceptance

1. Repeat front/oblique/rear/roof views at 1280×800 desktop and 390×780 mobile, plus close details.
2. Measure moving-frame performance on a declared device; keep agreed draw/triangle/texture/load budgets and owner dark-glass default.
3. No missing detail at LOD transitions, flicker, errors, failed assets or UI-dependent rendering changes.

## Evidence

- Audit #142: [John J. Glessner House, HABS IL-1015, written historical and descriptive data (27 pp.)](https://www.loc.gov/item/il0118/) — `a18-glessner-habs-data`; after 1963; written document reviewed. Rights: no known restrictions. Written history reviewed: PDF pp.3,10,14,22 are especially relevant to alterations, vines, original materials and exterior construction.

**Current audit views:** prairie, northwest, courtyard, roof, entry, porte. [Capture gallery files](../evidence/glessner-exterior-audit-2026-10-08/model/) and [follow-up close-ups](../evidence/glessner-exterior-audit-2026-10-08/details/). These are unchanged-scene desktop captures, not matched photogrammetry or FPS tests.

## Dependencies and existing work

[T-2201](../T-2000-2249/T-2201-glessner-close-the-south-courtyard-boundary-and-resolve-its.md) through [T-2226](../T-2000-2249/T-2226-glessner-balance-lighting-contact-shadows-and-restrained-sur.md) as applicable

Reuse T-1843 acceptance framework; do not create parallel test infrastructure. Re-read linked ticket states before execution. Reuse existing infrastructure and coordinate shared boundaries rather than duplicating it.

## Filing and execution record

The owner explicitly requested filing the entire reviewed programme as a held group; this authorizes the multi-ticket filing beyond the usual automatic-follow-up budget. Four original L estimates were each split into two bounded M passes before filing. No geometry, rendering or historical-source metadata was changed by this filing. Each visual implementation must provide before/after browser evidence and the repository-required checks; release and claim only after the owner selects this specific ticket.

## Pictures to build toward (owner, 2026-10-11, T-2368)

Owner, 2026-10-11: "if you have an image you should work towards it until it's a photographic representation of any images even drawings are ok, but it should look exactly perfectly like the image or drawing", and "you don't wrap the case until it matches the photo".

Before building, open every picture listed here (the image store holds them all since 2026-10-11: `https://kevinrhaas.github.io/chicago-images/prairie-1904/files/<id>.jpg`; the Prairie viewer shows each with its credit). Read the building off the pictures themselves, not off their one-line summaries. Solve each picture's camera into `data/reference_views/<structure_id>/<view>.json` and build. Then render with `node tools/photo_match.mjs` and work the side-by-side down until nothing the picture shows differs: massing, bays, every opening's shape and height, ornament, cornice, porch and stoop, roof and chimneys, fence, materials and tone. A later picture is evidence of its own date, so an alteration it shows is argued in the match record, not copied (AGENTS.md rule 11; `data/reference_views/README.md`).

This ticket works toward the same pictures as T-2228, whose `## Image gate` closes the building. Whatever this ticket builds is checked against them now, from their cameras.

Pictures:
  `glessner_house`: a18-cgy-1800-glessner-2135 (photograph, oblique front, 1887 (chicagology labels it 1886)), a18-cornell-adw-glessner (photograph, oblique front, ca. 1887), a18-gh-chicago-herald-1887-illustration (newspaper item, oblique front, late 1887), a18-gh-cornell-glessner-front-c1887 (photograph, oblique front, c. 1887), a18-gh-cornell-glessner-rear-c1887 (photograph, side elevation, c. 1887), a18-gh-courtyard-watercolor (architectural drawing, rear, undated (design period, 1885–1887?)), a18-gh-glessner-exterior-historic (photograph, oblique front, undated (late 1880s–1890s)), a18-gh-glessner-female-servants-entrance (photograph, detail, c. 1888–1890s), a18-gh-glessner-front-with-keith (photograph, front elevation, undated (probably 1890s–1920s)), a18-gho-house-under-construction-1887 (photograph, oblique front, 1887), a18-gho-porte-cochere-doors-c1888 (photograph, detail, about 1888), a18-glessner-habs-photo-12 (architectural drawing, front elevation, undated preliminary design (copied for HABS)), and 49 more in the library

## Pre-existing Balanced courtyard draw-call overrun — 2026-10-14

Read-only baseline captures during T-2494, exact source head `04add1ecd9be06a95fd4c859aa3fac330182ef23`, use the actual published 1904 app, normal boot, dark glass, unchanged scene lighting and the animation loop paused after readiness for repeatable inspection cameras. These are draw/triangle counts, **not FPS measurements**.

At 1280×800 / Balanced, the owner-angle stand has **334 draw calls / 1,962,193 triangles**, and the dining-copper stand has **332 / 1,916,293**, against **330 / 2,535,000**. Both fail the existing draw-call assertion. Ground, close-oblique and overhead stands pass. There are no page errors, failed resource requests or loader problems. The same five Full stands pass; Full peaks at **340 / 4,323,014**, within **360 / 4,600,000**.

Local east/north/up camera and target coordinates (metres in the house frame): owner angle `[28,3,12]` → `[36.5,14,7.5]`; dining copper `[22,4,10]` → `[25,13,8.5]`. T-2220's prepared baseline harness records the complete observations. This is pre-existing: T-2494 preserves Full's complete bytes and Light's exact binary geometry/texture payload. Retain this failed baseline when measuring the completed house; optimize or explicitly justify the supported-tier budget using AGENTS.md's measured-budget rule. Do not silently relax the assertion or call this Balanced run green.


## Local integration startup timeouts — 2026-10-14

At integration commit `00147a24aa6d9031d73fd8ee158d9e86e6507f99` (PR #799), two local 1280×800 captures of the actual published `/1904/` app timed out waiting for readiness with a 240,000 ms automation timeout: first with the default desktop setting, then with a saved Light setting. The second attempt recorded no page errors or failed resource requests and HTTP 200 for the canonical Glessner Light GLB. Neither attempt produced accepted images or draw/triangle measurements. These were capture-helper failures, not runs of the complete smoke suite.

A separate 39.41-second CPU profile of saved-Light startup still showed the scene-asset phase at 133/151 units, about 57.5 MB read, with terrain and subsequent phases not yet started, no application error and no loader problems. That identifies an early loading cost; it does not prove what consumed the rest of either timed-out attempt. Chromium used SwiftShader in a four-CPU workspace. Do not report these observations as hardware-GPU FPS or erase them by relaxing a budget assertion.

The unmodified exact-commit published smoke groups for [desktop part 13](https://github.com/kevinrhaas/chicago/actions/runs/38586109997) and [mobile part 13](https://github.com/kevinrhaas/chicago/actions/runs/38586394590) passed in CI. Keep the local/CI distinction when measuring cold startup and preparing the final Full/Light captures. Glessner generator, material, package and all three built asset bytes were unchanged by this integration with the lakefront work.

## T-2221 fresh dev baseline — 2026-10-14

The refreshed baseline uses unchanged T-2220 house bytes in the merged 00147/75b9 scene, before T-2221 geometry. It reaches readiness within the unchanged 240-second limit on this retry and produces all nine Full views with zero page errors, failed requests or app problems; the two earlier startup timeouts remain failures. Full courtyard bow-leader measures 401 draws / 4,761,785 triangles and dining-leader 400 / 4,711,778 against 360 / 4,600,000. All seven street/alley views pass (maximum 4,568,300 triangles). This is a failed budget run, not a passed baseline. It adds Full-detail regressions in the integrated scene to this ticket's existing Balanced failures. No ceiling was changed. Reproduce with the T-2221 camera harness; its before gallery and measurements will be committed with the drainage PR. Local rendering is SwiftShader, not a physical-GPU FPS measurement.

The completed 390x780 Light baseline also fails two close north views before the drainage change: north-head-clear 181 draws / 1,510,067 triangles and north-tower 181 / 1,511,690, against Light's unchanged 330 / 1,270,000 scene ceiling. The remaining seven views pass, including bow 180 / 1,005,882 and dining 249 / 1,252,050. Startup succeeds under the normal 240-second wait on this retry, and there are zero page errors, failed requests or app problems. Preserve these failures; do not raise the Light floor or mistake the separately passing 199,484-triangle house limit for a passing scene budget. Before images and raw browser-validation-mobile.json are in the T-2221 research gallery.


## T-2221 final published comparison — 2026-10-14 UTC

Final drainage assets retain the same four failing paired observations. Full bow:
403 draws / 4,760,451 triangles; dining: 402 / 4,710,444, against 360 / 4,600,000.
Light north-head-clear: 183 / 1,510,528; north-tower: 183 / 1,512,187, against
330 / 1,270,000. No paired camera newly fails. All paired Full readings add two
draws and remove 1,334 triangles; Light adds two draws with triangle deltas
-126 to +1,142 depending on culling. The additional after-only north-bowl-detail
angle passes both budgets; no before result exists at that angle.

Normal boot succeeded, with zero page errors, failed requests and app problems.
All 121 image tiles loaded with credits; 46 further records remain links.
Both browser commands correctly retain exit 1 for budget failures. Software
rendering is not hardware-GPU FPS. Geometry and captured cameras were unchanged
by the later integrated T-2496 travel fix. Evidence will land with T-2221 under
`docs/RESEARCH/glessner-rainwater-T-2221/app-comparison.json`; source before/after
results and screenshots are retained alongside it. No ceilings were raised.


## T-2224 courtyard camera handoff - 2026-10-15

The unchanged terrace-foot camera also fails the existing scene budgets on the accepted T-2223 baseline: Full 405 calls / 4,701,255 triangles against 360 / 4,600,000; Light 282 / 1,639,605 against 330 / 1,270,000. T-2224 captures at exactly that camera report Full 405 / 4,701,893 and Light 282 / 1,640,161. The other four court/access views in each tier remain within their existing budgets; draw calls are unchanged at all ten views. Keep the failed assertions and camera/budget values. Evidence and exact before/after poses: `chicago/4d/docs/RESEARCH/glessner-courtyard-ground-T-2224/`. The canonical Light house itself is 199,794 triangles, within its 200,000 limit; scene totals include the rest of the district and shadows. These SwiftShader captures establish geometry/call counts, not hardware FPS.


## T-2225 final north-court handoff — 2026-10-15

The unchanged north-court stand `[27,6,3]` looking at `[27,15.5,2]` (local ENU metres) fails before and after the selective vines. Full: 401 calls / 4,665,059 triangles before, 403 / 4,776,731 after, against 360 / 4,600,000. Light: 280 / 1,585,581 before, 282 / 1,585,645 after, against 330 / 1,270,000. The other four fixed views in each tier pass. Both QA commands retain exit 1; no budget or camera was relaxed. The final canonical Light house is 199,850 triangles, below its unchanged 200,000 house ceiling; this does not make the complete scene pass. Normal published boot produced zero page errors, failed requests or loader problems. SwiftShader measurements establish calls and triangles, not hardware FPS. Exact before/after poses, original failing assertions, screenshots and asset hashes are in `chicago/4d/docs/RESEARCH/glessner-vines-T-2225/`.


## T-2226 fixed material-baseline budget readings — 2026-10-15

Before any T-2226 material edit, the verified T-2225 dev Full/Light assets were captured at eight new fixed material stands. North shade ([39.5,35,5] toward [39.5,22.5556,5]) reports Full 299 calls / 4,618,485 triangles and Light 196 / 1,534,402. North close ([39.5,25.3,2.5] toward [39.5,22.5556,2.5]) reports Full 300 / 4,616,007 and Light 185 / 1,476,142. Limits remain Full 360 / 4,600,000 and Light 330 / 1,270,000. All other six stands pass. Both capture programs preserve exit 1; there are no browser errors, failed requests or app problems. Full neutral-light captures reproduce the same geometry counts and assert exact lighting restoration. These are additional BEFORE-edit failures owned by T-2227, not new geometry from the surface ticket. Keep these cameras and limits. Evidence: docs/RESEARCH/glessner-finish-T-2226/{full,mobile}-baseline-summary.json and the fixed camera plan. SwiftShader captures are not physical-GPU FPS.


## T-2226 completed material-camera comparison — 2026-10-15

All 24 after views were actually reviewed at the frozen baseline cameras, projection, exposure and dark-glass mode; neutral diagnostics restore the exact original lighting rig. The same north stands fail: Full north shade 300 calls / 4,618,463 triangles, north close 301 / 4,615,985; Light north shade 198 / 1,534,402, north close 187 / 1,476,142. All six other stands in each tier remain within their unchanged scene budgets. No browser errors, failed assets or app problems occurred; both programs preserve exit 1 for the recorded budget failures.

Surface-only geometry remains 1,371,506 Full / 199,850 Light triangles. The added plain-brick material costs one or two scene draws depending on culling and adds 3,706,972 bytes to Full web / 3,706,868 bytes to Light. Final assets are 59,090,956 / 32,622,008 bytes. Retain this download cost in the performance audit. Exact comparisons, hashes and inspected images are in `docs/RESEARCH/glessner-finish-T-2226/`. SwiftShader is not hardware-GPU FPS. No limit or camera was relaxed.
