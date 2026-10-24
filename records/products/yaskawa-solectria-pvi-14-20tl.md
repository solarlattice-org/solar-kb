---
id: prod:yaskawa-solectria-pvi-14-20tl
type: Product
name: Solectria PVI 14-20TL
aliases:
- PVI 14 20 TL
- PVI 14-20TL
- PVI 14TL
- PVI 20TL
- PVI 14TL-20TL
category: Inverters
make: yaskawa-solectria
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:yaskawa-solectria
  cite:
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: sec=h2
    h: ad391f7bc23c
  review: drafted
- claim_id: c2
  rel: instance_of
  target: comp:inverter
  note: Datasheet describes the models as transformerless three-phase string inverters.
  cite:
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: sec=h79
    h: 9ae6ca82cf76
  review: drafted
  review_note: 'support check: partial - Datasheet title references transformerless 3-ph string inverters,
    but the passage doesn''t explicitly state it''s an inverter in the evidence text beyond the URL.'
- claim_id: c3
  rel: implements
  target: func:dc-arc-fault-protection
  note: An internal arc board shuts the inverter down on a possible arc fault (Arc Protect).
  cite:
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=14.r6
    h: fcb0d94e792e
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=11.r7
    h: 8333325a5a17
  review: drafted
- claim_id: c4
  rel: implements
  target: func:residual-current-monitoring
  note: GFCI.Err is raised when DC leakage current exceeds the recommended value.
  cite:
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=14.r2
    h: bcea6533f17c
  review: drafted
- claim_id: c5
  attr: rated_power
  value:
    nominal: 14
    unit: unit:KiloW
  conditions: PVI 14TL continuous output power
  cite:
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=15.r6
    h: 3fb8c7c759b8
  review: drafted
  review_note: possible conflict with c6 (same source; check the conditions)
- claim_id: c6
  attr: rated_power
  value:
    nominal: 20
    unit: unit:KiloW
  conditions: PVI 20TL continuous output power
  cite:
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=15.r6
    h: 3fb8c7c759b8
  review: drafted
  review_note: possible conflict with c5 (same source; check the conditions)
- claim_id: c7
  attr: nominal_voltage
  value:
    nominal: 208
    unit: unit:V
  conditions: PVI 14TL nominal AC output voltage
  cite:
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=15.r1
    h: d98d5f910b66
  review: drafted
  review_note: possible conflict with c8 (same source; check the conditions)
- claim_id: c8
  attr: nominal_voltage
  value:
    nominal: 480
    unit: unit:V
  conditions: PVI 20TL nominal AC output voltage
  cite:
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=15.r1
    h: d98d5f910b66
  review: drafted
  review_note: possible conflict with c7 (same source; check the conditions)
- claim_id: c9
  attr: max_input_voltage
  value:
    max: 600
    unit: unit:V
  conditions: Absolute maximum DC input voltage, PVI 14TL and PVI 20TL
  cite:
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=18.r1
    h: 28da90044d2e
  review: drafted
- claim_id: c10
  attr: mppt_voltage_range
  value:
    min: 300
    max: 540
    unit: unit:V
  conditions: PVI 14TL MPPT input voltage range
  cite:
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=18.r3
    h: f9cf0dc9e27c
  review: drafted
- claim_id: c11
  attr: mppt_voltage_range
  value:
    min: 300
    max: 550
    unit: unit:V
  conditions: PVI 20TL MPPT input voltage range
  cite:
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=18.r3
    h: f9cf0dc9e27c
  review: drafted
- claim_id: c12
  attr: max_input_current
  value:
    max: 25
    unit: unit:A
  conditions: PVI 14TL maximum operating input current per zone
  cite:
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=18.r5
    h: 0f92e80cddf3
  review: drafted
- claim_id: c13
  attr: max_input_current
  value:
    max: 35
    unit: unit:A
  conditions: PVI 20TL maximum operating input current per zone
  cite:
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=18.r5
    h: 0f92e80cddf3
  review: drafted
- claim_id: c14
  attr: efficiency
  value:
    nominal: 96.7
    unit: unit:PERCENT
  conditions: PVI 14TL peak efficiency
  cite:
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=16.r1
    h: 5a306c3b2b63
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=16
    h: 9ed4f36e6570
  review: drafted
  review_note: possible conflict with c15 (same source; check the conditions); possible conflict with
    c16 (same source; check the conditions); possible conflict with c17 (same source; check the conditions)
- claim_id: c15
  attr: efficiency
  value:
    nominal: 97.4
    unit: unit:PERCENT
  conditions: PVI 20TL peak efficiency
  cite:
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=16.r1
    h: 5a306c3b2b63
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=16
    h: 9ed4f36e6570
  review: drafted
  review_note: possible conflict with c14 (same source; check the conditions); possible conflict with
    c16 (same source; check the conditions); possible conflict with c17 (same source; check the conditions)
- claim_id: c16
  attr: efficiency
  value:
    nominal: 96
    unit: unit:PERCENT
  conditions: PVI 14TL CEC weighted efficiency
  cite:
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=16.r2
    h: 2c6928034654
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=16
    h: 9ed4f36e6570
  review: drafted
  review_note: possible conflict with c14 (same source; check the conditions); possible conflict with
    c15 (same source; check the conditions); possible conflict with c17 (same source; check the conditions)
- claim_id: c17
  attr: efficiency
  value:
    nominal: 97
    unit: unit:PERCENT
  conditions: PVI 20TL CEC weighted efficiency
  cite:
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=16.r2
    h: 2c6928034654
  - src: src:yaskawa-pvi-14-20tl-iom-docr-070351-g
    loc: tbl=16
    h: 9ed4f36e6570
  review: drafted
  review_note: possible conflict with c14 (same source; check the conditions); possible conflict with
    c15 (same source; check the conditions); possible conflict with c16 (same source; check the conditions)
---
The Solectria PVI 14-20TL is a Yaskawa Solectria Solar family of transformerless three-phase string inverters made up of the PVI 14TL and PVI 20TL. The PVI 14TL delivers 14 kW continuous output at a nominal 208 VAC, and the PVI 20TL delivers 20 kW at a nominal 480 VAC. Both models accept an absolute maximum of 600 VDC. The MPPT range is 300 to 540 VDC on the 14TL and 300 to 550 VDC on the 20TL, with a per-zone input current limit of 25 A and 35 A respectively. Peak efficiency is 96.7 percent for the 14TL and 97.40 percent for the 20TL. CEC weighted efficiency is 96 and 97 percent. An internal arc board provides arc-fault shutdown (Arc Protect) and runs a self-check that raises Arc Board Error when it fails. Other alarms in the manual include GFCI.Err for high DC leakage current, GridV.OutLim for grid voltage out of range, EepromErr for memory faults and ExtFanErr for fan problems. The inverter has to be registered before its warranty becomes active.

<!-- review notes
- sentence 1: support check: partial - Manufacturer, PVI 14TL/20TL models and transformerless three-phase string inverter title are present, but 'family' framing is inferred; mostly supported.
-->
