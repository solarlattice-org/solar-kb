---
id: prod:canadian-solar-25-40ktl-gs-fl
type: Product
name: CSI-25/30/36/40KTL-GS-FL
aliases:
- CSI-25KTL-GS-FL
- CSI-30KTL-GS-FL
- CSI-36KTL-GS-FL
- CSI-40KTL-GS-FL
category: Inverters
make: canadian-solar
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:canadian-solar
  cite:
  - src: src:csi-csi-manual-25-40ktl-gs-fl-v1-2-2017-09-07
    loc: sec=h1
    h: cd46d014eabf
  - src: src:csi-csi-manual-25-40ktl-gs-fl-v1-2-2017-09-07
    loc: sec=1.1
    h: 1e05552d19ad
  review: drafted
- claim_id: c2
  rel: instance_of
  target: comp:inverter
  cite:
  - src: src:csi-csi-manual-25-40ktl-gs-fl-v1-2-2017-09-07
    loc: sec=h1
    h: cd46d014eabf
  - src: src:csi-csi-manual-25-40ktl-gs-fl-v1-2-2017-09-07
    loc: sec=1.1
    h: 1e05552d19ad
  review: drafted
- claim_id: c3
  attr: rated_power
  value:
    nominal: 36
    unit: unit:KiloW
  conditions: CSI-36KTL-GS-FL rated output power
  cite:
  - src: src:csi-csi-manual-25-40ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=10.r5
    h: 369ced2d770d
  review: drafted
  review_note: possible conflict with c4 (same source; check the conditions)
- claim_id: c4
  attr: rated_power
  value:
    nominal: 40
    unit: unit:KiloW
  conditions: CSI-40KTL-GS-FL rated output power
  cite:
  - src: src:csi-csi-manual-25-40ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=10.r5
    h: 369ced2d770d
  review: drafted
  review_note: possible conflict with c3 (same source; check the conditions)
- claim_id: c5
  attr: rated_output_current
  value:
    nominal: 30.1
    unit: unit:A
  conditions: CSI-25KTL-GS-FL rated grid output current (AC)
  cite:
  - src: src:csi-csi-manual-25-40ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=9.r10
    h: 7db73eb85b22
  review: drafted
  review_note: possible conflict with c6 (same source; check the conditions); possible conflict with c7
    (same source; check the conditions); possible conflict with c8 (same source; check the conditions)
- claim_id: c6
  attr: rated_output_current
  value:
    nominal: 36.1
    unit: unit:A
  conditions: CSI-30KTL-GS-FL rated grid output current (AC)
  cite:
  - src: src:csi-csi-manual-25-40ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=9.r10
    h: 7db73eb85b22
  review: drafted
  review_note: possible conflict with c5 (same source; check the conditions); possible conflict with c7
    (same source; check the conditions); possible conflict with c8 (same source; check the conditions)
- claim_id: c7
  attr: rated_output_current
  value:
    nominal: 43.3
    unit: unit:A
  conditions: CSI-36KTL-GS-FL rated grid output current (AC)
  cite:
  - src: src:csi-csi-manual-25-40ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=10.r10
    h: 2394d0e631e7
  review: drafted
  review_note: possible conflict with c5 (same source; check the conditions); possible conflict with c6
    (same source; check the conditions); possible conflict with c8 (same source; check the conditions)
- claim_id: c8
  attr: rated_output_current
  value:
    nominal: 48.1
    unit: unit:A
  conditions: CSI-40KTL-GS-FL rated grid output current (AC)
  cite:
  - src: src:csi-csi-manual-25-40ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=10.r10
    h: 2394d0e631e7
  review: drafted
  review_note: possible conflict with c5 (same source; check the conditions); possible conflict with c6
    (same source; check the conditions); possible conflict with c7 (same source; check the conditions)
- claim_id: c9
  attr: nominal_voltage
  value:
    nominal: 480
    unit: unit:V
  conditions: Rated AC grid voltage, three phase, CSI-36KTL-GS-FL and CSI-40KTL-GS-FL
  cite:
  - src: src:csi-csi-manual-25-40ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=10.r7
    h: 48581eac3635
  - src: src:csi-csi-manual-25-40ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=10.r9
    h: 9495bfd5f71a
  review: drafted
- claim_id: c10
  attr: efficiency
  value:
    min: 98.6
    unit: unit:PERCENT
  conditions: Maximum efficiency, CSI-25KTL-GS-FL and CSI-30KTL-GS-FL
  cite:
  - src: src:csi-csi-manual-25-40ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=9.r15
    h: edd0d1a0b898
  review: drafted
- claim_id: c11
  attr: efficiency
  value:
    min: 98.6
    unit: unit:PERCENT
  conditions: Maximum efficiency, CSI-36KTL-GS-FL and CSI-40KTL-GS-FL
  cite:
  - src: src:csi-csi-manual-25-40ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=10.r15
    h: ae69c512da64
  review: drafted
- claim_id: c12
  attr: operating_temperature
  value:
    min: -25
    max: 60
    unit: unit:DEG_C
  conditions: Running temperature, CSI-25KTL-GS-FL and CSI-30KTL-GS-FL
  cite:
  - src: src:csi-csi-manual-25-40ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=9.r21
    h: 81bb1a8196dd
  review: drafted
- claim_id: c13
  attr: frequency
  value:
    min: 59.5
    max: 60.5
    unit: unit:HZ
  conditions: Utility frequency operating range, CSI-25KTL-GS-FL and CSI-30KTL-GS-FL
  cite:
  - src: src:csi-csi-manual-25-40ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=9.r25
    h: 27a7bbfecb21
  review: drafted
- claim_id: c14
  rel: certified_to
  target: std:ul-1741
  cite:
  - src: src:csi-csi-manual-25-40ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=9.r26
    h: c6e4e1835946
  - src: src:csi-csi-manual-25-40ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=10.r26
    h: 195af83d6e8c
  review: drafted
- claim_id: c15
  rel: certified_to
  target: std:ieee-1547
  cite:
  - src: src:csi-csi-manual-25-40ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=9.r26
    h: c6e4e1835946
  review: drafted
- claim_id: c16
  rel: certified_to
  target: std:csa-c22-2-no-107-1
  cite:
  - src: src:csi-csi-manual-25-40ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=9.r26
    h: c6e4e1835946
  - src: src:csi-csi-manual-25-40ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=10.r26
    h: 195af83d6e8c
  review: drafted
- claim_id: c17
  rel: certified_to
  target: std:ul-1998
  cite:
  - src: src:csi-csi-manual-25-40ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=9.r26
    h: c6e4e1835946
  - src: src:csi-csi-manual-25-40ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=10.r26
    h: 195af83d6e8c
  review: drafted
- claim_id: c18
  rel: certified_to
  target: std:fcc-part-15
  note: Class B
  cite:
  - src: src:csi-csi-manual-25-40ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=9.r26
    h: c6e4e1835946
  review: drafted
- claim_id: c19
  rel: uses_protocol
  target: proto:wifi
  note: Listed among interfaces; option status per datasheet
  cite:
  - src: src:csi-csi-manual-25-40ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=10.r23
    h: 551493e55ebc
  review: drafted
- claim_id: c20
  rel: uses_protocol
  target: proto:cellular
  note: GPRS, optional
  cite:
  - src: src:csi-csi-manual-25-40ktl-gs-fl-v1-2-2017-09-07
    loc: tbl=10.r23
    h: 551493e55ebc
  review: drafted
---
The CSI-25/30/36/40KTL-GS-FL is a family of three-phase, grid-tied, transformerless string inverters from Canadian Solar that turn PV array DC into AC for on-site loads and the grid. The 36 and 40 kW models connect to a 480 Vac grid and carry rated output currents of 43.3 A and 48.1 A; the 25 and 30 kW models are rated at 30.1 A and 36.1 A. Maximum efficiency is above 98.6 percent, and grid current THD stays below 3 percent. The 25 and 30 kW models are specified to run from -25 to 60 °C and over a utility frequency range of 59.5 to 60.5 Hz. The enclosure is rated NEMA 4X, and the datasheet gives a design lifetime of more than 20 years.

<!-- review notes
- sentence 5: support check: partial - NEMA4X and >20 years stated only for specific models' rows (NEMA 4X only for 36/40), not shown for 25/30.
-->
