---
id: prod:chint-sch-100-125ktl
type: Product
name: CPS SCH100-125KTL-DO/US-600
aliases:
- SCH 100 125 KTL
- CPS 100 125 kW
- Chint/100 125 kW
- SCH100KTL-DO/US-600
- SCH125KTL-DO/US-600
- SCH100KTL-DO/US-480
category: Inverters
make: chint
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:chint
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: sec=h3
    h: cff70db8f47c
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: sec=h135
    h: ceaf75016dc5
  review: drafted
  review_note: 'support check: partial - Evidence names CHINT Power Systems America but doesn''t tie the
    SCH100-125KTL-DO/US-600 model to it explicitly.'
- claim_id: c2
  attr: max_input_voltage
  value:
    nominal: 1500
    unit: unit:V
  conditions: Maximum DC input voltage, all three models
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=40.r3
    h: 764a2d38c37e
  review: drafted
- claim_id: c3
  attr: max_input_current
  value:
    nominal: 275
    unit: unit:A
  conditions: Maximum PV input current (Isc x 1.25) per inverter, all three models
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=41.r3
    h: 3d056c74b7b7
  review: drafted
- claim_id: c4
  attr: efficiency
  value:
    nominal: 99
    unit: unit:PERCENT
  conditions: Maximum efficiency as stated in the product overview features list
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: sec=h32
    h: af71519ca61d
  review: drafted
  review_note: possible conflict with c5 (same source; check the conditions)
- claim_id: c5
  attr: efficiency
  value:
    nominal: 98.5
    unit: unit:PERCENT
  conditions: CEC efficiency as stated in the product overview features list
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: sec=h32
    h: af71519ca61d
  review: drafted
  review_note: possible conflict with c4 (same source; check the conditions)
- claim_id: c6
  rel: uses_protocol
  target: proto:rs485
  note: Standard Modbus over RS485 via FlexOM gateway card
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: sec=h34
    h: 2c765e543bf0
  review: drafted
- claim_id: c7
  rel: uses_protocol
  target: proto:sunspec-modbus
  note: Via FlexOM gateway card
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: sec=h34
    h: 2c765e543bf0
  review: drafted
- claim_id: c8
  rel: requires
  target: prod:chint-flexom-gateway
  note: Modbus, SunSpec and HTTPS/XML communications are provided through the FlexOM gateway card
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: sec=h34
    h: 2c765e543bf0
  review: drafted
- claim_id: c9
  rel: implements
  target: func:remote-firmware-update
  note: Listed as standard with the CPS Flex Gateway
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=43.r6
    h: 057462f6af37
  review: drafted
  review_note: 'support check: partial - Row lists remote diagnostics/firmware upgrade as standard with
    CPS Flex Gateway, but the garbled row doesn''t cleanly state firmware update support; the gateway
    name also differs slightly.'
- claim_id: c10
  rel: certified_to
  target: std:ul-1741-sa
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=43.r6
    h: 057462f6af37
  review: drafted
- claim_id: c11
  rel: certified_to
  target: std:ul-1741-sb
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=43.r6
    h: 057462f6af37
  review: drafted
- claim_id: c12
  rel: certified_to
  target: std:ieee-1547-2018
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=43.r6
    h: 057462f6af37
  review: drafted
- claim_id: c13
  rel: certified_to
  target: std:fcc-part-15
  cite:
  - src: src:chint-cps-sch100-125ktl-do-us-600-480-user-manual-rev-1-9
    loc: tbl=43.r6
    h: 057462f6af37
  review: drafted
---
The CPS SCH100-125KTL family consists of three-phase string inverters from CHINT Power Systems. It covers the SCH100KTL-DO/US-600, SCH125KTL-DO/US-600 and SCH100KTL-DO/US-480 models. The rated AC output is 100 kW or 125 kW, depending on the model. The 600 V models output 600 Vac and the 480 V model outputs 480 Vac. All models accept up to 1500 VDC on the DC input and a maximum PV input current of 275 A. Through the FlexOM gateway card, the inverter communicates over standard Modbus RS485, SunSpec Modbus and HTTPS/XML for third-party monitoring and control. Remote diagnostics and firmware upgrades are listed as standard with the CPS Flex Gateway. The CommErr alarm means internal communication failed, which can be caused by poorly seated internal communication terminal blocks. The ExtFanErr alarm points to a blocked fan, a fan at the end of its service life, or a poor fan socket contact.

<!-- review notes
- sentence 1: support check: partial - Three models are listed, but three-phase string inverter type isn't stated and the family naming is only implied.
- sentence 5: support check: partial - The row is a merged label/value that lists standard with CPS Flex Gateway, but the values shown are certifications, so the remote diagnostics claim is only implied.
-->
