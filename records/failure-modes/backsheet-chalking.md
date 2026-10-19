---
id: fm:backsheet-chalking
type: FailureMode
name: Backsheet Chalking
aliases:
- backsheet whitening
- PVFS 1-6
- whitening
- PVFS 1-6vs.01
category: Modules
claims:
- claim_id: c1
  rel: affects
  target: comp:backsheet
  note: Affects the outer polymer layer of the backsheet, which contains inorganic pigment or filler.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h61
    h: 644a3733bb6b
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=11.r1
    h: ce4fb0199cdd
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.5.1
    h: 4dfb46bec383
  review: drafted
- claim_id: c2
  rel: caused_by
  target: stressor:low-quality-material
  note: The root cause is an outer layer that does not resist weathering well enough, for example missing
    UV stabilisation. Examples given are PA or PO outer layers.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.5.1
    h: 4dfb46bec383
  review: drafted
  review_note: 'support check: partial - Passage gives root cause as insufficient weathering stability
    (lack of UV stabilisation, PA/PO) but does not name it ''low-quality material'' in the chalking context;
    close but a mapping inference.'
- claim_id: c3
  rel: presents_as
  target: symptom:white-powder-surface
  note: A white powder sits on the outer backsheet surface. It comes off on a finger and can be removed.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h61
    h: 644a3733bb6b
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=11.r1
    h: ce4fb0199cdd
  review: drafted
- claim_id: c4
  rel: presents_as
  target: symptom:dull-rough-surface
  note: A chalked backsheet usually looks rough or dull.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h61
    h: 644a3733bb6b
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=11.r1
    h: ce4fb0199cdd
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:visual-inspection
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=11.r2
    h: 00041690913d
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h61
    h: 644a3733bb6b
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=8
    h: 88163ae58405
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:tactile-inspection
  note: Run a finger over the backsheet or do a simple wipe test to check for powder.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h61
    h: 644a3733bb6b
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=11.r1
    h: ce4fb0199cdd
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.5.1
    h: 4dfb46bec383
  review: drafted
- claim_id: c7
  rel: leads_to
  target: fm:backsheet-cracking
  note: Chalking can be a precursor to cracking, but this cannot be predicted. Cracking has been seen
    with and without chalking, and PVDF backsheets usually crack without chalking.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=11.r5
    h: 893e30a4726d
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h61
    h: 644a3733bb6b
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=30.r3
    h: 0950ed925bf5
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=10.r3
    h: 8121b95d9f56
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.5.1
    h: 4dfb46bec383
  review: drafted
- claim_id: c8
  rel: leads_to
  target: fm:severe-metallization-corrosion
  note: More moisture diffusing into the encapsulant and active parts can corrode cells and connectors,
    which reduces performance.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=11.r5
    h: 893e30a4726d
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h61
    h: 644a3733bb6b
  review: drafted
  review_note: 'support check: partial - Moisture diffusion leading to corrosion of cells and connectors
    is stated, but ''severe metallization corrosion'' as such is not named and chalking is only indirectly
    linked via reduced UV protection.'
- claim_id: c9
  rel: mitigated_by
  target: mit:close-monitoring
  note: Use regular inspections to track how the chalking progresses.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h61
    h: 644a3733bb6b
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=11.r8
    h: d4da399f6da7
  review: drafted
- claim_id: c10
  rel: mitigated_by
  target: mit:ground-fault-detection
  note: The inverter or other devices should provide ground fault detection at all times.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h61
    h: 644a3733bb6b
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=11.r8
    h: d4da399f6da7
  review: drafted
- claim_id: c11
  rel: mitigated_by
  target: mit:certified-products
  note: Check that the IEC 61215 certification is valid.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h61
    h: 644a3733bb6b
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=11.r8
    h: d4da399f6da7
  review: drafted
- claim_id: c12
  rel: mitigated_by
  target: mit:bom-verification
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h61
    h: 644a3733bb6b
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=11.r8
    h: d4da399f6da7
  review: drafted
- claim_id: c13
  rel: mitigated_by
  target: mit:accelerated-weathering-screening
  note: As a preventive step, backsheets can go through accelerated weathering tests followed by wipe
    tests.
  cite:
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.5.1
    h: 4dfb46bec383
  review: drafted
---
Backsheet chalking happens when the polymer in the outer backsheet layer breaks down under light and heat and releases its inorganic pigment or filler. The usual root cause is an outer layer that does not withstand weathering well enough, for example one without UV stabilisation. You will see a white powder on the rear surface that comes off on a finger, and the backsheet usually looks rough or dull. Confirm it by visual inspection and a simple wipe test on the backsheet. Chalking does not affect safety or performance at first, but it can signal ongoing backsheet degradation and can come before cracking, insulation failures or moisture-driven corrosion. Chalking does not reliably predict cracking, because cracking has been seen both with and without chalking. Inspect affected modules regularly to track progress, and keep ground fault detection active at all times. To prevent it, check that the IEC 61215 certification and the bill of materials are valid.
