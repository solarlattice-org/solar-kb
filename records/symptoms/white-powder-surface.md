---
id: symptom:white-powder-surface
type: Symptom
name: White surface powder
aliases:
- Backsheet chalking
- whitening
- chalking
claims:
- claim_id: c1
  rel: observed_as
  target: meas:wipe-test-powder-transfer
  note: Rubbing a finger or doing a simple wipe test on the outer backsheet surface picks up white powder,
    which comes off. The backsheet often looks rough or dull. This is a visual and tactile sign only,
    with no monitoring-data signature in the units.
  cite:
  - src: src:iea-pvps-t13-30-2025-annex
    loc: tbl=11.r1
    h: ce4fb0199cdd
  - src: src:iea-pvps-t13-23-2021
    loc: sec=h61
    h: 644a3733bb6b
  - src: src:iea-pvps-t13-30-2025
    loc: sec=2.5.1
    h: 4dfb46bec383
  review: drafted
  review_note: 'support check: partial - Finger/wipe test picking up removable white powder and rough/dull
    look are stated, but the ''no monitoring-data signature'' claim is not stated in the passages.'
---
A white powder shows up on the outer surface of the module backsheet, and the backsheet usually looks rough or dull. Run a finger or a simple wipe over the backsheet: if the powder comes off onto it, the backsheet is chalking. Visual inspection is the standard way to find it. Chalking is a sign of backsheet chalking. Sunlight and heat break down the polymer in the outer backsheet layer, which releases inorganic fillers such as the TiO2 pigment used to block UV. The powder stays on the surface. It does not directly affect module safety, performance or the insulation resistance of the backsheet. It can still be an early sign of backsheet cracking and insulation failure. More moisture getting in can later corrode cells and connectors. You cannot reliably predict whether chalking will lead to cracking. Some backsheets crack without ever chalking, so check for visible cracks as well. Inspect the affected modules regularly to track how the damage progresses, and keep inverter or other ground fault detection running at all times. As a preventive step, check that the module's IEC 61215 certification and bill of materials are valid.

<!-- review notes
- sentence 2: support check: partial - Finger and simple wipe test are stated, and detection is by VI, but 'standard way' and the powder-comes-off-means-chalking rule are slightly stronger than stated.
- sentence 6: support check: partial - The passages say prediction is not possible and that cracking occurs without chalking (PA, PVDF), but they do not say to check for visible cracks.
-->
