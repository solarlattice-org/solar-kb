---
id: prod:canadian-solar-185-255k
type: Product
name: CSI-185K-T600GL02/03-U / CSI-255K-T800GL02/03-U
aliases:
- CSI-185K-T600GL02-U
- CSI-185K-T600GL03-U
- CSI-255K-T800GL02-U
- CSI-255K-T800GL03-U
category: Inverters
make: canadian-solar
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:canadian-solar
  note: Manual published by CSI Solar Co., Ltd.
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: sec=1.1
    h: 6883c118c877
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: sec=front
    h: 2c32e9cf48c3
  review: drafted
- claim_id: c2
  rel: instance_of
  target: comp:inverter
  note: Three-phase inverter converting PV DC power to AC for local loads and the grid
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: sec=1.1
    h: 6883c118c877
  review: drafted
- claim_id: c3
  rel: compatible_with
  target: arch:grid-tied-pv
  scope:
    applications:
    - on-grid
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: sec=1.1
    h: 6883c118c877
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: sec=front
    h: 2c32e9cf48c3
  review: drafted
- claim_id: c4
  rel: uses_protocol
  target: proto:rs485
  conditions: Stated for CSI-185K-T600GL02-U and CSI-255K-T800GL02-U
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=14.r34
    h: ddc1ed9e3f75
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=15.r34
    h: 36868fcab8b4
  review: drafted
- claim_id: c5
  rel: uses_protocol
  target: proto:power-line-communication
  conditions: Optional; stated for the GL02 models
  note: PLC is listed as an optional communication connection
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=14.r34
    h: ddc1ed9e3f75
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=15.r34
    h: 36868fcab8b4
  review: drafted
- claim_id: c6
  attr: max_input_voltage
  value:
    nominal: 1500
    unit: unit:V
  conditions: Maximum DC input voltage, CSI-185K-T600GL02-U
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=14.r1
    h: d21524ac1573
  review: drafted
- claim_id: c7
  attr: max_input_voltage
  value:
    nominal: 1500
    unit: unit:V
  conditions: Maximum DC input voltage, CSI-255K-T800GL02-U
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=15.r1
    h: 7d4fa0ee790e
  review: drafted
- claim_id: c8
  attr: nominal_voltage
  value:
    nominal: 950
    unit: unit:V
  conditions: Rated DC voltage, CSI-185K-T600GL02-U
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=14.r2
    h: 59df153759aa
  review: drafted
  review_note: possible conflict with c9 (same source; check the conditions); possible conflict with c10
    (same source; check the conditions); possible conflict with c11 (same source; check the conditions)
- claim_id: c9
  attr: nominal_voltage
  value:
    nominal: 1080
    unit: unit:V
  conditions: Rated DC voltage, CSI-255K-T800GL02-U
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=15.r2
    h: 9d95037a2255
  review: drafted
  review_note: possible conflict with c8 (same source; check the conditions); possible conflict with c10
    (same source; check the conditions); possible conflict with c11 (same source; check the conditions)
- claim_id: c10
  attr: nominal_voltage
  value:
    nominal: 600
    unit: unit:V
  conditions: Rated AC grid voltage (3/PE), CSI-185K-T600GL02-U and GL03-U
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=14.r12
    h: 3f420473f00f
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=5
    h: 5c9121cd6f16
  review: drafted
  review_note: possible conflict with c8 (same source; check the conditions); possible conflict with c9
    (same source; check the conditions); possible conflict with c11 (same source; check the conditions)
- claim_id: c11
  attr: nominal_voltage
  value:
    nominal: 800
    unit: unit:V
  conditions: Rated AC grid voltage (3/PE), CSI-255K-T800GL02-U and GL03-U
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=15.r12
    h: 73e6fd53e09f
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=5
    h: 5c9121cd6f16
  review: drafted
  review_note: possible conflict with c8 (same source; check the conditions); possible conflict with c9
    (same source; check the conditions); possible conflict with c10 (same source; check the conditions)
- claim_id: c12
  attr: max_input_current
  value:
    nominal: 26
    unit: unit:A
  conditions: Per input, listed as 14*26 A, CSI-185K-T600GL02-U
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=14.r6
    h: eb762f06da3f
  review: drafted
  review_note: possible conflict with c14 (same source; check the conditions)
- claim_id: c13
  attr: max_input_current
  value:
    nominal: 26
    unit: unit:A
  conditions: Per input, listed as 14*26 A, CSI-255K-T800GL02-U
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=15.r6
    h: f2b45c1d12b0
  review: drafted
  review_note: possible conflict with c14 (same source; check the conditions)
- claim_id: c14
  attr: max_input_current
  value:
    nominal: 30
    unit: unit:A
  conditions: Per input, listed as 12*30 A, CSI-185K-T600GL03-U
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=16.r6
    h: 582e79f8ec38
  review: drafted
  review_note: possible conflict with c12 (same source; check the conditions); possible conflict with
    c13 (same source; check the conditions)
- claim_id: c15
  attr: rated_output_current
  value:
    nominal: 178
    unit: unit:A
  conditions: Maximum output current, CSI-185K-T600GL02-U and GL03-U; grid OCPD 250 A
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=5
    h: 5c9121cd6f16
  review: drafted
  review_note: possible conflict with c16 (same source; check the conditions)
- claim_id: c16
  attr: rated_output_current
  value:
    nominal: 184
    unit: unit:A
  conditions: Rated/maximum output current, CSI-255K-T800GL02-U and GL03-U; grid OCPD 250 A
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=15.r13
    h: 0f52c6df88d7
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=5
    h: 5c9121cd6f16
  review: drafted
  review_note: possible conflict with c15 (same source; check the conditions)
- claim_id: c17
  attr: frequency
  value:
    nominal: 60
    unit: unit:HZ
  conditions: Rated grid frequency, CSI-185K-T600GL02-U
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=14.r16
    h: 4efdf7838a15
  review: drafted
- claim_id: c18
  attr: frequency
  value:
    nominal: 60
    unit: unit:HZ
  conditions: Rated grid frequency, CSI-255K-T800GL02-U
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=15.r16
    h: d702257f02b0
  review: drafted
- claim_id: c19
  attr: warranty_term
  value:
    max: 20
    nominal: 5
    unit: unit:YR
  conditions: 5 years standard, extendable to 20 years; stated for CSI-185K-T600GL02-U
  cite:
  - src: src:csi-csi-installation-manual-185-255k-usa-v1-1-20211119
    loc: tbl=14.r35
    h: d4fe24b69e1e
  review: drafted
---
This family covers four Canadian Solar three-phase, grid-tied, transformerless string inverters: CSI-185K-T600GL02/03-U and CSI-255K-T800GL02/03-U. They convert PV array DC power into AC to supply local loads and feed the grid. The 185K models are rated for a 600 V grid and the 255K models for an 800 V grid, both at 60 Hz. The maximum DC input is 1500 V. Maximum output current is 178.0 A for the 185K models and 184.0 A for the 255K models. The manual lists a 250 A grid overcurrent protection device for each model. The GL02 models take 14 inputs of up to 26 A each and ship with 28 DC connectors. The 185K GL03 model takes 12 inputs of up to 30 A each, and the GL03 models ship with 24 DC connectors. The DC connectors are MC4 type. Maximum efficiency is 99.0 percent and EU efficiency is 98.5 percent. Communication is over RS485, with power line communication as an option. Each unit has a 2x20 LCD display and uses intelligent redundant cooling. The standard warranty is 5 years and can be extended to 20 years.
