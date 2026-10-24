---
id: prod:generac-pwrcell-inverter
type: Product
name: Generac PWRcell Inverter (X7602, XVT076A03, XVT114G03)
aliases:
- PWRcell Inverter
- X7602
- XVT076A03
- XVT114G03
- X11402
category: Inverters
make: generac
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:generac
  cite:
  - src: src:generac-generac-pwrcell-inverter-x7602-installation-manual
    loc: sec=h2
    h: 96242a0b1fe0
  review: drafted
- claim_id: c2
  rel: uses_protocol
  target: proto:rebus
  note: Spec table lists a REbus DC voltage rating.
  cite:
  - src: src:generac-generac-pwrcell-inverter-x7602-installation-manual
    loc: tbl=4.r21
    h: 5562c27c261b
  review: drafted
  review_note: 'support check: partial - Only a REbus voltage rating is shown; it implies REbus use but
    doesn''t explicitly say the protocol is REbus DC nanogrid.'
- claim_id: c3
  attr: efficiency
  value:
    nominal: 97.3
    unit: unit:PERCENT
  conditions: Peak efficiency, XVT076A03 / X7602
  cite:
  - src: src:generac-generac-pwrcell-inverter-x7602-installation-manual
    loc: tbl=4.r9
    h: a2e02f03f52c
  review: drafted
  review_note: possible conflict with c4 (same source; check the conditions); possible conflict with c5
    (same source; check the conditions); possible conflict with c6 (same source; check the conditions)
- claim_id: c4
  attr: efficiency
  value:
    nominal: 97.7
    unit: unit:PERCENT
  conditions: Peak efficiency, XVT114G03 / X11402
  cite:
  - src: src:generac-generac-pwrcell-inverter-x7602-installation-manual
    loc: tbl=4.r9
    h: a2e02f03f52c
  review: drafted
  review_note: possible conflict with c3 (same source; check the conditions); possible conflict with c5
    (same source; check the conditions); possible conflict with c6 (same source; check the conditions)
- claim_id: c5
  attr: efficiency
  value:
    nominal: 96.5
    unit: unit:PERCENT
  conditions: CEC weighted efficiency, XVT076A03 / X7602
  cite:
  - src: src:generac-generac-pwrcell-inverter-x7602-installation-manual
    loc: tbl=4.r12
    h: 6e0f73055243
  review: drafted
  review_note: possible conflict with c3 (same source; check the conditions); possible conflict with c4
    (same source; check the conditions); possible conflict with c6 (same source; check the conditions)
- claim_id: c6
  attr: efficiency
  value:
    nominal: 97.5
    unit: unit:PERCENT
  conditions: CEC weighted efficiency, XVT114G03 / X11402
  cite:
  - src: src:generac-generac-pwrcell-inverter-x7602-installation-manual
    loc: tbl=4.r12
    h: 6e0f73055243
  review: drafted
  review_note: possible conflict with c3 (same source; check the conditions); possible conflict with c4
    (same source; check the conditions); possible conflict with c5 (same source; check the conditions)
- claim_id: c7
  attr: nominal_voltage
  value:
    min: 212
    max: 264
    nominal: 240
    unit: unit:V
  conditions: AC operating voltage range line-to-line, XVT076A03 / X7602 (min / nominal / max columns)
  cite:
  - src: src:generac-generac-pwrcell-inverter-x7602-installation-manual
    loc: tbl=4.r27
    h: 75d5d63616ce
  - src: src:generac-generac-pwrcell-inverter-x7602-installation-manual
    loc: tbl=4.r20
    h: 7867b92b2ca3
  review: drafted
  review_note: 'support check: partial - Values 212/240/264 are min/nominal/max; nominal is 240, not a
    212-264 range (range is operating).; possible conflict with c8 (same source; check the conditions);
    possible conflict with c10 (same source; check the conditions); possible conflict with c11 (same source;
    check the conditions)'
- claim_id: c8
  attr: nominal_voltage
  value:
    min: 106
    max: 132
    nominal: 120
    unit: unit:V
  conditions: AC operating voltage range line-to-neutral, XVT076A03 / X7602
  cite:
  - src: src:generac-generac-pwrcell-inverter-x7602-installation-manual
    loc: tbl=4.r26
    h: e8110039af21
  - src: src:generac-generac-pwrcell-inverter-x7602-installation-manual
    loc: tbl=4.r20
    h: 7867b92b2ca3
  review: drafted
  review_note: 'support check: partial - Values 106/120/132 are min/nominal/max; nominal is 120, not 106-132.;
    possible conflict with c7 (same source; check the conditions); possible conflict with c9 (same source;
    check the conditions); possible conflict with c11 (same source; check the conditions)'
- claim_id: c9
  attr: nominal_voltage
  value:
    min: 184
    max: 228
    nominal: 208
    unit: unit:V
  conditions: AC operating output voltage range line-to-line, XVT114G03 / X11402
  cite:
  - src: src:generac-generac-pwrcell-inverter-x7602-installation-manual
    loc: tbl=4.r29
    h: 88eed1edc83f
  - src: src:generac-generac-pwrcell-inverter-x7602-installation-manual
    loc: tbl=4.r20
    h: 7867b92b2ca3
  review: drafted
  review_note: 'support check: partial - Values 184/208/228 are min/nominal/max; nominal is 208, not 184-228.;
    possible conflict with c8 (same source; check the conditions); possible conflict with c10 (same source;
    check the conditions); possible conflict with c11 (same source; check the conditions)'
- claim_id: c10
  attr: nominal_voltage
  value:
    min: 106
    max: 132
    nominal: 120
    unit: unit:V
  conditions: AC operating voltage range line-to-neutral, XVT114G03 / X11402
  cite:
  - src: src:generac-generac-pwrcell-inverter-x7602-installation-manual
    loc: tbl=4.r28
    h: dae7d1143cd0
  - src: src:generac-generac-pwrcell-inverter-x7602-installation-manual
    loc: tbl=4.r20
    h: 7867b92b2ca3
  review: drafted
  review_note: 'support check: partial - Values 106/120/132 are min/nominal/max; nominal is 120, not 106-132.;
    possible conflict with c7 (same source; check the conditions); possible conflict with c9 (same source;
    check the conditions); possible conflict with c11 (same source; check the conditions)'
- claim_id: c11
  attr: nominal_voltage
  value:
    min: 360
    max: 420
    nominal: 380
    unit: unit:V
  conditions: REbus DC bus voltage
  cite:
  - src: src:generac-generac-pwrcell-inverter-x7602-installation-manual
    loc: tbl=4.r21
    h: 5562c27c261b
  - src: src:generac-generac-pwrcell-inverter-x7602-installation-manual
    loc: tbl=4.r20
    h: 7867b92b2ca3
  review: drafted
  review_note: 'support check: partial - 360/380/420 are min/nominal/max; nominal is 380, not 360-420.;
    possible conflict with c7 (same source; check the conditions); possible conflict with c8 (same source;
    check the conditions); possible conflict with c9 (same source; check the conditions); possible conflict
    with c10 (same source; check the conditions)'
- claim_id: c12
  attr: frequency
  value:
    nominal: 60
    unit: unit:HZ
  conditions: Normal AC output frequency, all models
  cite:
  - src: src:generac-generac-pwrcell-inverter-x7602-installation-manual
    loc: tbl=4.r6
    h: a5eca578edde
  review: drafted
- claim_id: c13
  attr: operating_temperature
  value:
    min: -20
    max: 50
    unit: unit:DEG_C
  conditions: Full-power operating ambient temperature range
  cite:
  - src: src:generac-generac-pwrcell-inverter-x7602-installation-manual
    loc: tbl=4.r36
    h: 791be3168eba
  review: drafted
---
The Generac PWRcell Inverter is a family of inverters that includes the XVT076A03 (X7602) and XVT114G03 (X11402) models. On the DC side it connects to a REbus bus, which normally runs at 380 V dc and is rated from 360 to 420 V dc. The X7602 runs on a 240 V line-to-line grid (212 to 264 V) and the X11402 on a 208 V line-to-line grid (184 to 228 V). Both run at 120 V line-to-neutral, at 60 Hz. Peak efficiency is 97.3 percent for the X7602 and 97.7 percent for the X11402. CEC weighted efficiency is 96.5 and 97.5 percent. The enclosure is rated NEMA Type 3R. Cooling is by forced convection.

<!-- review notes
- sentence 2: support check: partial - Voltage values 360/380/420 min/nom/max are supported, but connection to a REbus bus on the DC side is only implied by the REbus voltage row.
-->
