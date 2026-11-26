---
id: T-3762
title: Fit and map historical photos onto the Glessner Field and Pullman residents
state: review
epic: META
requested_by: owner
seen: false
effort: M
legacy_id: null
parent: null
opened: 2026-11-26
closed: null
pr: 2371
claimed_by: run 11/26/2026, 1:36:53 PM CT
blocked_on: null
needs_bake: false
closed_at: null
claimed_run: null
claimed_at: 2026-11-26T19:36:54.436Z
decision: null
decision_answer: null
---

Fit and map historical photos onto the Glessner Field and Pullman residents.

**Acceptance:** Inventory every existing person-specific portrait/photo reference, apply usable identified historical photographs to their matching drawn people, and retain existing source-based head fits and historical year identity. Keep explicit stand-in labels for sources depicting someone else; do not count stand-ins as photographs of the named person. Provide one import command and one source/before/after review page, preserving cleared source provenance, recorded eye colours, child proportions and bounded shared texture pages. Verify front/oblique renders, complete eligible-person coverage and served dev delivery.

**Owner steering 2026-11-26:** “Then let’s start to do all the people we have photos of and apply them.” The existing portrait inventory has 27 face fits: 20 own-person portraits, seven labelled stand-ins; two of the latter already have full skin sheets. Extend beyond this inventory wherever existing photo references identify another drawn person.

**Released 2026-11-26** (claim of run 11/26/2026, 8:42:50 AM CT): Owner prioritized the generic adult/child dev rollout first; named historical likenesses are the next phase. Preserved prototype: remote branch archive/historical-photo-prototype-stash, commit 7c187bec62d45cd4c8d15c75d732be530f677ba2 (stash with untracked source assets). Fetch that branch and apply its stash on an isolated branch based on current dev; do not overwrite the newer default generic/child catalogs. Contains six camera/UV prototypes and provenance for John J. Glessner, Frances Macbeth Glessner, Marshall Field, Albertine Huck Field, Harriet Sanger Pullman and Frank Orren Lowden. Existing curated head values are retained; historical before/after browser review is still owed. George Pullman died in 1897 and should not be introduced in 1904. Complete acceptance next: one command and one review page to import a person’s source photos, preserve source rights and historical year identity, inspect front/profile and eye placement, and apply only approved results. Frances uses the existing credited low-resolution CHM portrait crop; improve the source if possible. Real-GPU crowd timing remains separate and unmeasured.


**Owner references, 2026-11-26:** The owner supplied separate likeness models for Dorothy Sterling (`pa1904_stirling_william_r_c1900_dorothy_sterling`, younger daughter, 19) and Alice May Stirling (`pa1904_stirling_william_r_c1900_alice_m_sterling`, older daughter, 20), then requested stored period face portraits without modern clothing/backgrounds. The project stores edited 1904 studio portraits and neutral texture companions, with explicit stand-in labels; original modern uploads are not published. Both have separate new fitted heads and exact-person photographic textures, retaining their recorded age, height, household and dress.

**Inventory/implementation checkpoint:** 20 own-person historical portraits, five existing labelled staff references, two existing Grey full skin sheets and two new Stirling references: 29 accounted for. The named atlas has 27 entries; 26 people have active casts, with 27 actual body assignments (Charles also drives). Kate Ryan’s retained reference is prepared but has no active cast, so the import does not add a person to the town. Existing 25 head fits and all generic/child pixels remain unchanged. Source/before/applied page: tools/historical_photo_review.html; rebuild/import command: tools/historical_photo_faces.py. A single processing-clearance record preserves every original archive citation and stays within the unchanged source-index limits: 323,390 raw bytes; 81,948 compressed first-open bytes. Three crowd sheets share one nearby page: 12,873,272 exact added RGBA8 bytes including mipmaps. Two actual named writes reproduce 43 files (42 rewritten payloads plus retained coverage) in 43.44/33.61 seconds, with deliberate drift rejection/repair; generic/child writes also reproduce all 349 files. Dev delivery and the final CI/render receipts are pending the release steps.
