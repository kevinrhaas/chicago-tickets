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

**Current implementation and qualification:** Source PR #2371 at b085e2e5b3 applies twenty own-person archive portraits and five labelled staff references; two Grey full skins remain intact and two owner-chosen Stirling period references bring the inventory to 29. The named atlas contains 27 entries, reaching 26 people through 27 body assignments; Kate Ryan remains prepared without adding an actor. The original 256 adult and sixteen child references are retained, with 64 approved/companion adult references and 48 child companions added: 320 adults and 64 children. Default NPCs use existing community/year/neighborhood context, independently of the unrestricted compatible adult choices in Settings. Original 256 head fits and source/detail/scalp pixels, earlier curated historical heads, child proportions and exact identities stay protected. Photo/body colour, iris transfer and the native female forehead hairline are corrected without new hair geometry. All final catalog inputs/outputs are bound to two identical actual writer passes, including two actual writes of the final 64-child extension. Three fixed crowd sheets and one global resident-or-loading nearby page cap added face textures at 12,873,272 bytes including mipmaps; 26 detail pages remain disk choices. All eight local check.sh partitions pass on the exact committed tree, 1,458 checks with readers/base guards. The fresh published app verifies all nine renderer modules, all three catalogs, both Stirling period cards, all 26 detail pages and all 7,610 assignments across four years. Final native app captures and current-head hosted gate/30 desktop-mobile smoke legs are being collected; GitHub currently queues them behind other repository jobs. Dev delivery remains pending those release steps; real low-power GPU FPS remains unmeasured. Evidence stays in chicago-evidence, not this ticket repo.

**Additional owner acceptance, 2026-11-26:** Correct visible face/body colour seams, overlarge exposed foreheads and unnatural eyes in actual rendered people (the examples came from PR #2378's made-hats comparison). The owner approved the new sixteen fictional European period references and asked to include/prioritize them while preserving variety. Existing recorded historical communities/nativities and year/neighborhood context govern reconstructed NPC appearance; personal photographs remain first priority, and no ancestry is inferred from names or face photographs. The settings character creator keeps broad unrestricted choices independently of those historical NPC defaults. The visual target is the natural appearance of the approved reference sheet in the actual app. Keep the shared weak-machine GPU page limits and supply actual app captures before closing.
