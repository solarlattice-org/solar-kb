---
id: prod:sungrow-sg200hx
type: Product
name: Sungrow SG200HX-US
aliases:
- SG200HX
- SG200HX-US
- PV Grid-Connected Inverter
category: Inverters
make: sungrow
product_level: family
model_number: SG200HX-US
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:sungrow
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: sec=9.3
    h: e0a94aac5535
  review: drafted
  review_note: 'support check: partial - Passage mentions SUNGROW warranty but doesn''t explicitly state
    SG200HX-US is made by Sungrow (only implied via document title elsewhere).'
- claim_id: c2
  rel: instance_of
  target: comp:inverter
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: sec=h1
    h: d8f7cb5a1881
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=5.r2
    h: b2b49b2ab76d
  review: drafted
- claim_id: c3
  attr: efficiency
  value:
    nominal: 98.9
    unit: unit:PERCENT
  conditions: maximum efficiency
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=40.r5
    h: 2504e2eb1822
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=40
    h: 33e7eb60c673
  review: drafted
  review_note: possible conflict with c4 (same source; check the conditions)
- claim_id: c4
  attr: efficiency
  value:
    nominal: 98.5
    unit: unit:PERCENT
  conditions: CEC weighted efficiency
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=40.r5
    h: 2504e2eb1822
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=40
    h: 33e7eb60c673
  review: drafted
  review_note: possible conflict with c3 (same source; check the conditions)
- claim_id: c5
  attr: mppt_voltage_range
  value:
    min: 850
    max: 1300
    unit: unit:V
  conditions: full-power MPP voltage range at 40 °C
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=39.r6
    h: 1855432da80b
  review: drafted
- claim_id: c6
  attr: max_input_current
  value:
    nominal: 40
    unit: unit:A
  conditions: maximum PV input current per input, listed as 12 x 40 A
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=39.r9
    h: bc5866514a90
  review: drafted
- claim_id: c7
  rel: uses_protocol
  target: proto:rs485
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=41.r7
    h: 432d437d2742
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: sec=5.8.2
    h: 23149c859eea
  review: drafted
- claim_id: c8
  rel: uses_protocol
  target: proto:modbus
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=41.r7
    h: 432d437d2742
  review: drafted
- claim_id: c9
  rel: uses_protocol
  target: proto:sunspec-information-model
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=41.r7
    h: 432d437d2742
  review: drafted
- claim_id: c10
  rel: uses_protocol
  target: proto:bluetooth
  note: Bluetooth with app as display/interface alongside LEDs
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=41.r6
    h: b8463745c0f2
  review: drafted
- claim_id: c11
  rel: certified_to
  target: std:ul-1741
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=41.r10
    h: ce3d6fc3b078
  review: drafted
  review_note: 'support check: partial - UL1741 is listed under compliance, but ''certified'' is not stated
    explicitly.'
- claim_id: c12
  rel: certified_to
  target: std:ul-1741-sa
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=41.r10
    h: ce3d6fc3b078
  review: drafted
  review_note: 'support check: partial - UL1741 SA/SB listed as compliance; certification not explicit.'
- claim_id: c13
  rel: certified_to
  target: std:ul-1741-sb
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=41.r10
    h: ce3d6fc3b078
  review: drafted
  review_note: 'support check: partial - UL1741 SA/SB listed as compliance; certification not explicit.'
- claim_id: c14
  rel: certified_to
  target: std:ul-62109-1
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=41.r10
    h: ce3d6fc3b078
  review: drafted
  review_note: 'support check: partial - UL62109-1 listed as compliance; certification not explicit.'
- claim_id: c15
  rel: certified_to
  target: std:ieee-1547-2018
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=41.r10
    h: ce3d6fc3b078
  review: drafted
  review_note: 'support check: partial - IEEE1547-2018 listed as compliance; certification not explicit.'
- claim_id: c16
  rel: certified_to
  target: std:ieee-1547-1-2020
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=41.r10
    h: ce3d6fc3b078
  review: drafted
  review_note: 'support check: partial - IEEE1547.1-2020 listed as compliance; certification not explicit.'
- claim_id: c17
  rel: certified_to
  target: std:cpuc-rule-21
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=41.r10
    h: ce3d6fc3b078
  review: drafted
  review_note: 'support check: partial - California Rule21 listed as compliance; certification not explicit.'
- claim_id: c18
  rel: certified_to
  target: std:fcc-part-15
  note: Class A limit
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=41.r10
    h: ce3d6fc3b078
  review: drafted
  review_note: 'support check: partial - FCC Part 15 Class A limit listed as compliance; certification
    not explicit.'
- claim_id: c19
  rel: implements
  target: func:reverse-polarity-protection
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=40.r7
    h: c7a7d35ff921
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=40
    h: 33e7eb60c673
  review: drafted
- claim_id: c20
  rel: implements
  target: func:residual-current-monitoring
  note: listed as leakage current protection
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=40.r9
    h: 5138b8d4a0cb
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=40
    h: 33e7eb60c673
  review: drafted
- claim_id: c21
  rel: implements
  target: func:ground-fault-protection
  note: listed as ground fault monitoring
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=40
    h: 33e7eb60c673
  review: drafted
- claim_id: c22
  rel: implements
  target: func:string-monitoring
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=40
    h: 33e7eb60c673
  review: drafted
- claim_id: c23
  rel: implements
  target: func:night-reactive-power
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=40.r14
    h: d0e21b36833e
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=40
    h: 33e7eb60c673
  review: drafted
- claim_id: c24
  rel: implements
  target: func:surge-protection
  note: DC Type II and AC Type II
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=40
    h: 33e7eb60c673
  review: drafted
- claim_id: c25
  rel: implements
  target: func:constant-power-factor
  note: adjustable power factor 0.8 leading to 0.8 lagging
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=40
    h: 33e7eb60c673
  review: drafted
- claim_id: c26
  rel: implements
  target: func:pid-recovery
  note: optional feature
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=40.r15
    h: 2cd964e69481
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=40
    h: 33e7eb60c673
  review: drafted
- claim_id: c27
  rel: implements
  target: func:dc-arc-fault-protection
  note: AFCI listed as optional
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=39.r11
    h: bf59f6d4c948
  review: drafted
---
The Sungrow SG200HX-US is a transformerless, three-phase, grid-connected PV string inverter. It has 12 PV inputs rated at 40 A each, a full-power MPP voltage range of 850 V to 1300 V at 40 °C, and an AC voltage range of 528 V to 660 V. Its maximum efficiency is 98.9 % and its CEC efficiency is 98.5 %. Harmonic distortion is below 3 % at nominal power, and DC current injection is below 0.5 % of rated current. Built-in protections include DC reverse connection protection, AC short-circuit protection, leakage current protection, grid and ground fault monitoring, PV string current monitoring and Type II surge protection on both the DC and AC sides. It can supply reactive power at night and has an adjustable power factor. AFCI and anti-PID with PID recovery are optional extras. The inverter has a DC switch but no AC switch, so a separate AC disconnect has to be provided. It communicates over RS485 using Modbus and SunSpec, and it has LED indicators plus Bluetooth for setup through an app.

<!-- review notes
- sentence 6: support check: partial - DC switch yes / AC switch no stated, but the need for a separate AC disconnect is not stated.
-->
