---
id: concept:lithium-ion-battery
type: Concept
name: Lithium-ion battery
aliases:
- Li-ion
- lithium ion
- LiIon
category: Storage
concept_kind: technology
claims:
- claim_id: c1
  rel: related_to
  target: concept:state-of-charge
  note: Battery management system reports SoC to the battery inverter; SMA defines SoC ranges specific
    to lithium-ion batteries.
  cite:
  - src: src:sma-kb-battery-state-of-charge-soc-for-li-ion-batteries-and-how-it-works-in-sma-sunny-isla
    loc: sec=h1
    h: a8ba0e902184
  - src: src:sma-doc-si-sbs-stpse-backup-pl-en-30
    loc: tbl=17.r5
    h: 06991e5d5476
  - src: src:sma-doc-si-sbs-stpse-backup-pl-en-30
    loc: tbl=17.r1
    h: f673fd19673a
  review: drafted
- claim_id: c2
  rel: related_to
  target: concept:soc-estimation
  note: For unmanaged Li-ion batteries the Sunny Island acts as BMS using ampere-hour counting with full-charge
    detection and voltage recalibration.
  cite:
  - src: src:sma-kb-battery-state-of-charge-soc-for-li-ion-batteries-and-how-it-works-in-sma-sunny-isla
    loc: sec=h1
    h: a8ba0e902184
  review: drafted
- claim_id: c3
  rel: related_to
  target: concept:lead-acid-battery
  note: SMA documents give separate SoC range settings for lead-acid and lithium-ion batteries.
  cite:
  - src: src:sma-doc-si-sbs-stpse-backup-pl-en-30
    loc: tbl=17.r5
    h: 06991e5d5476
  - src: src:sma-doc-259761
    loc: tbl=45
    h: 5e488f822451
  - src: src:sma-doc-si-sbs-stpse-backup-pl-en-30
    loc: tbl=17.r1
    h: f673fd19673a
  - src: src:sma-doc-278742
    loc: tbl=49.r2
    h: ad74ae1e4009
  - src: src:std-standards-nec-2014-nec2014-480
    loc: sec=h4
    h: e180cb9e722b
  review: drafted
- claim_id: c4
  rel: related_to
  target: concept:ampacity
  note: Battery-backup use relies on the battery delivering enough current; with Li-ion this ampacity
    is not guaranteed.
  cite:
  - src: src:sma-doc-244194
    loc: sec=h41
    h: 33c07b976a10
  review: drafted
- claim_id: c5
  rel: related_to
  target: func:backup-power
  cite:
  - src: src:sma-doc-244194
    loc: sec=h41
    h: 33c07b976a10
  - src: src:sma-doc-si-sbs-stpse-backup-pl-en-30
    loc: tbl=17.r3
    h: 6296c0a2f67e
  review: drafted
- claim_id: c6
  rel: related_to
  target: prod:sma-sunny-island
  cite:
  - src: src:sma-doc-259463
    loc: sec=h122
    h: 67876df41164
  - src: src:sma-doc-278742
    loc: tbl=87.r3
    h: bcd98df7f444
  - src: src:sma-doc-259761
    loc: tbl=84.r6
    h: c6683e875c06
  - src: src:sma-kb-battery-state-of-charge-soc-for-li-ion-batteries-and-how-it-works-in-sma-sunny-isla
    loc: sec=h1
    h: a8ba0e902184
  review: drafted
- claim_id: c7
  rel: related_to
  target: prod:sma-sunny-boy-storage
  cite:
  - src: src:sma-doc-259463
    loc: sec=h122
    h: 67876df41164
  - src: src:sma-doc-si-sbs-stpse-backup-pl-en-30
    loc: sec=h48
    h: 67876df41164
  review: drafted
- claim_id: c8
  rel: related_to
  target: prod:sma-sunny-tripower-smart-energy
  cite:
  - src: src:sma-doc-259463
    loc: sec=h122
    h: 67876df41164
  - src: src:sma-doc-si-sbs-stpse-backup-pl-en-30
    loc: sec=h48
    h: 67876df41164
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
---
A lithium-ion (Li-ion) battery is a rechargeable storage battery made of electrochemical cells. Each cell is nominally about 3.6 to 3.8 volts, compared with 2 volts per cell for lead-acid. The battery management system (BMS) of a lithium-ion battery controls how the battery operates. It must be connected to the battery inverter or hybrid inverter by a data cable. If the battery has its own BMS, the BMS sends the state of charge to the Sunny Island. The BMS values override the battery parameters set in the inverter, so changing those parameters there has no effect. With an unmanaged Li-ion battery, the Sunny Island acts as the BMS. It estimates state of charge by ampere-hour counting and voltage recalibration, using parameters set as the battery manufacturer recommends. Lithium-ion batteries use different state-of-charge range settings from lead-acid. For example, the deep discharge area is 0% to 3% for Li-ion, against 0% to 10% for lead-acid. Battery capacity and current rating must match the system setup, and three-phase systems usually need more than one battery. In backup systems, check with the manufacturer that the battery can supply the inverter's overload current.

<!-- review notes
- sentence 1: support check: partial - Cell voltages and rechargeable cells are supported by u24, but the definition of Li-ion as a rechargeable storage battery made of electrochemical cells is only loosely implied (u1 just expands the abbreviation).
- sentence 1: review: partial - The 3.6-3.8 V versus 2 V per cell comparison is quoted directly, but no passage states that Li-ion batteries are rechargeable storage batteries; the storage-battery definition covers only lead-acid, nickel-cadmium and 'other' rechargeable types.
-->
