---
id: prod:schneider-electric-conext-cl125
type: Product
name: Schneider Electric Conext CL125
aliases:
- Conext CL125
- Conext CL 125
- CL 125
- CL 125 A
- CL 125 E
- Conext CL125A
- Conext CL125E
- PVSCL125A
- PVSCL125E
- Conext CL Inverter
category: Inverters
make: schneider-electric
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:schneider-electric
  cite:
  - src: src:schneider-conext-cl125-solution-guide-na
    loc: sec=h124
    h: cc0c11cf7068
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: sec=h230
    h: e1c49710c74a
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: sec=h4
    h: 7b910f38e7ea
  review: drafted
- claim_id: c2
  attr: rated_power
  value:
    nominal: 125
    unit: unit:KiloW
  conditions: Maximum AC output active power at PF=1 and nominal AC voltage; CL125E (IEC) and CL125A (NA)
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=56.r10
    h: cdb2b1ede084
  review: drafted
- claim_id: c3
  attr: rated_power
  value:
    nominal: 125
    unit: unit:KiloV-A
  conditions: Maximum continuous apparent power at nominal AC voltage; CL125E (IEC) and CL125A (NA)
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=56.r12
    h: 159362e8ac9a
  review: drafted
- claim_id: c4
  attr: rated_power
  value:
    nominal: 125
    unit: unit:KiloW
  conditions: Conext CL125A, 1500 VDC systems (solution guide key specifications)
  cite:
  - src: src:schneider-conext-cl125-solution-guide-na
    loc: sec=h30
    h: 545ab8a7532b
  review: drafted
- claim_id: c5
  attr: mppt_voltage_range
  value:
    min: 860
    max: 1250
    unit: unit:V
  conditions: Full-power MPPT voltage range, Conext CL125A
  cite:
  - src: src:schneider-conext-cl125-solution-guide-na
    loc: sec=h30
    h: 545ab8a7532b
  review: drafted
- claim_id: c6
  attr: mppt_voltage_range
  value:
    min: 860
    max: 1450
    unit: unit:V
  conditions: DC operating voltage range, Conext CL125A
  cite:
  - src: src:schneider-conext-cl125-solution-guide-na
    loc: sec=h30
    h: 545ab8a7532b
  review: drafted
- claim_id: c7
  attr: nominal_voltage
  value:
    nominal: 600
    unit: unit:V
  conditions: Three-phase AC output, star or delta (3P+PE), Conext CL125A
  cite:
  - src: src:schneider-conext-cl125-solution-guide-na
    loc: sec=h30
    h: 545ab8a7532b
  review: drafted
- claim_id: c8
  attr: efficiency
  value:
    nominal: 98.8
    unit: unit:PERCENT
  conditions: Peak efficiency, CL125E (IEC) and CL125A (NA)
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=58.r1
    h: 63709524fa95
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=58
    h: 425df372530e
  review: drafted
  review_note: possible conflict with c9 (same source; check the conditions); possible conflict with c10
    (same source; check the conditions)
- claim_id: c9
  attr: efficiency
  value:
    nominal: 98.7
    unit: unit:PERCENT
  conditions: European efficiency, Conext CL125E (IEC)
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=58.r1
    h: 63709524fa95
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=58
    h: 425df372530e
  review: drafted
  review_note: possible conflict with c8 (same source; check the conditions); possible conflict with c10
    (same source; check the conditions)
- claim_id: c10
  attr: efficiency
  value:
    nominal: 98.5
    unit: unit:PERCENT
  conditions: CEC efficiency, Conext CL125A (NA)
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=58.r1
    h: 63709524fa95
  - src: src:schneider-conext-cl125-solution-guide-na
    loc: sec=h30
    h: 545ab8a7532b
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=58
    h: 425df372530e
  review: drafted
  review_note: possible conflict with c8 (same source; check the conditions); possible conflict with c9
    (same source; check the conditions)
- claim_id: c11
  rel: uses_protocol
  target: proto:rs485
  note: Two RS-485 ports (RS-485_1 and RS-485_2) supporting daisy-chain wiring
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=60
    h: 2015029c2b68
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: sec=h9
    h: fbe53f142f89
  review: drafted
- claim_id: c12
  rel: uses_protocol
  target: proto:modbus
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=60
    h: 2015029c2b68
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: sec=h9
    h: fbe53f142f89
  - src: src:schneider-conext-cl125-solution-guide-na
    loc: sec=h30
    h: 545ab8a7532b
  review: drafted
- claim_id: c13
  rel: uses_protocol
  target: proto:sunspec-modbus
  note: Stated as SunSpec compatible and certified
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=60
    h: 2015029c2b68
  - src: src:schneider-conext-cl125-solution-guide-na
    loc: sec=h30
    h: 545ab8a7532b
  review: drafted
- claim_id: c14
  rel: uses_protocol
  target: proto:bluetooth
  note: Bluetooth 4.0 link to the eConfigure CL125 app
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=60
    h: 2015029c2b68
  review: drafted
- claim_id: c15
  rel: implements
  target: func:mppt
  note: Single PV input; MPPT efficiency stated above 99% (static 99.5%, dynamic 99%)
  cite:
  - src: src:schneider-conext-cl125-solution-guide-na
    loc: sec=h30
    h: 545ab8a7532b
  review: drafted
  review_note: 'support check: partial - MPPT efficiency, MPPT voltage and single PV input are stated,
    though MPPT as a function is only implied.'
- claim_id: c16
  rel: implements
  target: func:constant-power-factor
  note: Power factor adjustable from 0.8 capacitive to 0.8 inductive
  cite:
  - src: src:schneider-conext-cl125-solution-guide-na
    loc: sec=h30
    h: 545ab8a7532b
  review: drafted
  review_note: 'support check: partial - PF adjustment range is stated, but a constant power factor mode
    is not explicitly named.'
- claim_id: c17
  rel: compatible_with
  target: arch:ungrounded-pv-array
  conditions: Designed for 1500 V floating PV systems
  cite:
  - src: src:schneider-conext-cl125-solution-guide-na
    loc: sec=h30
    h: 545ab8a7532b
  review: drafted
- claim_id: c18
  rel: compatible_with
  target: arch:delta-600v
  conditions: 600 V three-phase delta AC output wiring (3P+PE), Conext CL125A
  cite:
  - src: src:schneider-conext-cl125-solution-guide-na
    loc: sec=h30
    h: 545ab8a7532b
  review: drafted
- claim_id: c19
  rel: requires
  target: role:level-2-user-access
  conditions: Many settings; account requested through a Schneider Electric representative
  cite:
  - src: src:schneider-conext-cl125-quick-install-guide-975-0792-revb
    loc: sec=h24
    h: 4e53ff6d56b4
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: sec=h183
    h: 4e53ff6d56b4
  review: drafted
- claim_id: c20
  rel: requires
  target: tool:schneider-econfigure-cl125-app
  conditions: Local configuration and firmware upgrade (alternatively the Conext CL EasyConfig tool)
  cite:
  - src: src:schneider-conext-cl125-solution-guide-na
    loc: sec=h30
    h: 545ab8a7532b
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=60
    h: 2015029c2b68
  review: drafted
  review_note: 'support check: partial - App is listed for local configuration and firmware upgrade alongside
    EasyConfig, but ''requires'' is overstated since the alternative exists.'
---
The Conext CL125 is a three-phase string inverter family from Schneider Electric. It comes as the CL125E for IEC markets and the CL125A for North America. Both versions are rated at 125 kW and 125 kVA at nominal AC voltage. The CL125A is built for 1500 VDC floating PV systems and has a single PV input. On the CL125A, full-power MPPT runs from 860 V to 1250 V, and the AC output is 600 V three-phase in star or delta (3P+PE). Peak efficiency is 98.8% for both versions. The CL125E has a European efficiency of 98.7% and the CL125A a CEC efficiency of 98.5%. Power factor can be set anywhere from 0.8 capacitive to 0.8 inductive. For communications it uses Modbus over two RS-485 ports that can be daisy-chained, and it is SunSpec compatible and certified. Local setup is through a front LED panel and the eConfigure CL125 app over Bluetooth 4.0. Firmware upgrades and configuration are done locally with the eConfigure app or the Conext CL EasyConfig tool. Many settings need a Level 2 user access account, which you request from a Schneider Electric representative. The electronics enclosure is rated Type 4X on the CL125A and IP 65 on the CL125E.

<!-- review notes
- sentence 1: support check: partial - CL125E (IEC) and CL125A (NA) versions are shown, but 'string inverter' is not stated; three-phase is stated.
-->
