---
id: fm:insulation-loss
type: FailureMode
name: Loss of electrical insulation
aliases:
- insulation fault
- Insulation failure
- isolation fault
- low insulation resistance
- Electrical insulation fault
claims:
- claim_id: c1
  rel: caused_by
  target: fm:cable-defect
  note: Damaged or undersized DC cables are named as a main source of insulation faults.
  cite:
  - src: src:pv-root-cause-cable-defect
    loc: sec=front
    h: b8e06ac4915e
  - src: src:pv-root-cause-cable-defect
    loc: sec=h2
    h: ecd061f4ac98
  - src: src:pv-root-cause-cable-defect
    loc: sec=h6
    h: 2f6cadabed98
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=46.r5
    h: a680b50f7520
  review: drafted
- claim_id: c2
  rel: caused_by
  target: fm:connector-defect
  cite:
  - src: src:pv-root-cause-connector-defect
    loc: sec=front
    h: 27362abca33f
  - src: src:pv-root-cause-connector-defect
    loc: sec=h2
    h: ffc071d1e172
  - src: src:pv-root-cause-connector-defect
    loc: sec=h3
    h: b866045455bd
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=46.r5
    h: a680b50f7520
  review: drafted
- claim_id: c3
  rel: caused_by
  target: fm:glass-breakage
  note: Once the glass is broken, module insulation is no longer guaranteed, especially in wet conditions.
  cite:
  - src: src:pv-root-cause-glass-breakage
    loc: sec=front
    h: fbd89f70605e
  - src: src:pv-root-cause-glass-breakage
    loc: sec=h2
    h: 226b4cbee592
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=32.r5
    h: 21e9fd14fbde
  - src: src:pv-root-cause-glass-breakage
    loc: sec=h3
    h: 6dfd57c14260
  - src: src:pv-root-cause-glass-breakage
    loc: sec=h5
    h: 086a578b6c8a
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h30
    h: 11d01e81d3cc
  review: drafted
- claim_id: c4
  rel: caused_by
  target: fm:junction-box-failure
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h6
    h: 9e4d1b1adbd8
  review: drafted
- claim_id: c5
  rel: caused_by
  target: fm:delamination
  note: Delamination near the junction box or module edge can let water in, causing an insulation failure
    as a follow-up failure.
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h6
    h: 9e4d1b1adbd8
  - src: src:iea-pvps-t13-23-2021
    loc: sec=3.1.2
    h: 0db875b1c7c0
  review: drafted
- claim_id: c6
  rel: caused_by
  target: stressor:moisture-exposure
  note: The fault can come and go with humidity and is often worse on rainy days or in humid periods.
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h6
    h: 9e4d1b1adbd8
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=32.r5
    h: 21e9fd14fbde
  - src: src:pv-root-cause-glass-breakage
    loc: sec=h5
    h: 086a578b6c8a
  - src: src:pv-root-cause-cable-defect
    loc: sec=h6
    h: 2f6cadabed98
  review: drafted
  review_note: 'support check: partial - The passages tie moisture to insulation faults that are intermittent
    and worse in wet or humid periods, but they don''t present moisture exposure as a generic cause.'
- claim_id: c7
  rel: affects
  target: comp:dc-cable
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=46.r5
    h: a680b50f7520
  - src: src:pv-root-cause-cable-defect
    loc: sec=h6
    h: 2f6cadabed98
  review: drafted
- claim_id: c8
  rel: affects
  target: comp:dc-connector
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=46.r5
    h: a680b50f7520
  review: drafted
- claim_id: c9
  rel: affects
  target: comp:junction-box
  cite:
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h6
    h: 9e4d1b1adbd8
  review: drafted
- claim_id: c10
  rel: presents_as
  target: symptom:ground-fault
  note: May be intermittent, with lower insulation during rain.
  cite:
  - src: src:pv-root-cause-glass-breakage
    loc: sec=h5
    h: 086a578b6c8a
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h30
    h: 11d01e81d3cc
  review: drafted
- claim_id: c11
  rel: presents_as
  target: symptom:inverter-shutdown
  note: Low insulation resistance causes no loss by itself until the inverter faults or switches off.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=45.r5
    h: c00908595ecc
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=46.r5
    h: a680b50f7520
  - src: src:iea-pvps-t13-30-2025-annex
    loc: sec=h30
    h: 11d01e81d3cc
  review: drafted
- claim_id: c12
  rel: leads_to
  target: fm:arc-fault
  note: In the worst case, damaged cables or connectors may arc and start a fire.
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: tbl=46.r5
    h: a680b50f7520
  review: drafted
- claim_id: c13
  rel: detected_by
  target: method:insulation-resistance-test
  cite:
  - src: src:pv-root-cause-cable-defect
    loc: sec=front
    h: b8e06ac4915e
  - src: src:pv-root-cause-connector-defect
    loc: sec=front
    h: 27362abca33f
  - src: src:pv-root-cause-glass-breakage
    loc: sec=front
    h: fbd89f70605e
  - src: src:pv-root-cause-cable-defect
    loc: sec=h2
    h: ecd061f4ac98
  - src: src:pv-root-cause-glass-breakage
    loc: sec=h2
    h: 226b4cbee592
  - src: src:pv-root-cause-connector-defect
    loc: sec=h2
    h: ffc071d1e172
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=front
    h: a85dc942aaf6
  - src: src:pv-root-cause-junction-box-failure
    loc: sec=h2
    h: 631415923f8a
  - src: src:iea-pvps-t13-23-2021
    loc: sec=3.1.2
    h: 0db875b1c7c0
  review: drafted
- claim_id: c14
  rel: mitigated_by
  target: mit:module-replacement
  note: Replace modules that can no longer guarantee electrical safety or insulation resistance.
  cite:
  - src: src:pv-root-cause-glass-breakage
    loc: sec=front
    h: fbd89f70605e
  - src: src:pv-root-cause-glass-breakage
    loc: sec=h2
    h: 226b4cbee592
  - src: src:iea-pvps-t13-23-2021
    loc: sec=3.1.2
    h: 0db875b1c7c0
  review: drafted
- claim_id: c15
  rel: mitigated_by
  target: mit:cable-replacement
  cite:
  - src: src:pv-root-cause-cable-defect
    loc: sec=front
    h: b8e06ac4915e
  - src: src:pv-root-cause-cable-defect
    loc: sec=h2
    h: ecd061f4ac98
  review: drafted
- claim_id: c16
  rel: mitigated_by
  target: mit:post-repair-verification
  note: Confirm insulation integrity after the repair.
  cite:
  - src: src:pv-root-cause-cable-defect
    loc: sec=front
    h: b8e06ac4915e
  - src: src:pv-root-cause-cable-defect
    loc: sec=h2
    h: ecd061f4ac98
  review: drafted
- claim_id: c17
  rel: mitigated_by
  target: mit:certified-products
  cite:
  - src: src:iea-pvps-t13-23-2021
    loc: sec=3.1.2
    h: 0db875b1c7c0
  review: drafted
---
Loss of electrical insulation means current-carrying parts of the PV array are no longer properly isolated from ground or from people. It usually comes from damaged cables, faulty connectors, broken module glass or failed junction boxes. Moisture makes it worse, so the fault may only appear during rain or humid periods and can be intermittent. In the field it shows up as ground faults and inverter trips or shutdowns. Low insulation resistance on its own does not reduce output until the inverter faults. If the leakage stays below the protection device thresholds, the fault can go undetected while still causing significant power losses. Confirm it with insulation resistance testing on isolated circuits. Treat it as a shock hazard: exposed parts can carry dangerous voltages, and in the worst case damaged cables or connectors can arc and start a fire. Replace damaged cable runs or modules that can no longer guarantee insulation, then confirm insulation integrity after the repair.
