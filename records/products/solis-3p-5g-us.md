---
id: prod:solis-3p-5g-us
type: Product
name: Solis-3P(125-255)K-EHV-5G-US
aliases:
- Solis-125K-EHV-5G-US
- Solis-185K-EHV-5G-US
- Solis-255K-EHV-5G-US
category: Inverters
make: solis
product_level: family
claims:
- claim_id: c1
  rel: instance_of
  target: comp:inverter
  note: Listed as a transformerless grid support utility interactive PV inverter, wall mounted and permanently
    connected.
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=26.r4
    h: fb88cb3f7bd4
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: sec=h292
    h: 817103f1f8e5
  review: drafted
- claim_id: c2
  rel: compatible_with
  target: arch:grid-tied-pv
  note: Described as a utility interactive PV inverter.
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=26.r4
    h: fb88cb3f7bd4
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: sec=h292
    h: 817103f1f8e5
  review: drafted
  review_note: 'support check: partial - Utility interactive PV inverter is stated, but no mention of
    absence of storage; grid-tied-without-storage is an inference.'
- claim_id: c3
  rel: uses_protocol
  target: proto:rs485
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=18.r37
    h: c161f39f15d6
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=17.r37
    h: 92a9a435bd7b
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=20.r37
    h: 09fa167e8829
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=16.r37
    h: 53f30f7f429c
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=19.r37
    h: 0e74586ab412
  review: drafted
- claim_id: c4
  rel: uses_protocol
  target: proto:power-line-communication
  note: PLC is listed as an optional communication connection.
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=18.r37
    h: c161f39f15d6
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=17.r37
    h: 92a9a435bd7b
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=20.r37
    h: 09fa167e8829
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=16.r37
    h: 53f30f7f429c
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=19.r37
    h: 0e74586ab412
  review: drafted
- claim_id: c5
  rel: implements
  target: func:pid-recovery
  note: Integrated PID recovery listed for the 185K and 255K models.
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=16.r21
    h: 78351a3fcb7c
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=17.r21
    h: 67b359a900e5
  review: drafted
- claim_id: c6
  attr: max_input_voltage
  value:
    nominal: 1500
    unit: unit:V
  conditions: Maximum DC input voltage, Solis-125K-EHV-5G-US-PLUS and Solis-255K-EHV-5G-US
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=18.r1
    h: d777b1a518a8
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=17.r1
    h: a520668fac15
  review: drafted
- claim_id: c7
  attr: nominal_voltage
  value:
    nominal: 800
    unit: unit:V
  conditions: Rated AC grid voltage (3/PE), Solis-255K-EHV-5G-US and -PLUS
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=17.r12
    h: c13db16d6498
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=20.r12
    h: 1a9c433724f0
  review: drafted
  review_note: possible conflict with c8 (same source; check the conditions)
- claim_id: c8
  attr: nominal_voltage
  value:
    nominal: 600
    unit: unit:V
  conditions: Rated AC grid voltage (3/PE), Solis-185K-EHV-5G-US and Solis-125K-EHV-5G-US-PLUS
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=16.r12
    h: 3e7c5fe20953
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=18.r12
    h: 1ce93389b48a
  review: drafted
  review_note: possible conflict with c7 (same source; check the conditions)
- claim_id: c9
  attr: rated_output_current
  value:
    nominal: 184
    unit: unit:A
  conditions: Rated output current, Solis-255K-EHV-5G-US
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=17.r13
    h: 380c046de82d
  review: drafted
  review_note: possible conflict with c10 (same source; check the conditions)
- claim_id: c10
  attr: rated_output_current
  value:
    nominal: 132.3
    unit: unit:A
  conditions: Rated output current, Solis-125K-EHV-5G-US-PLUS
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=18.r13
    h: 1dfc7ea3994e
  review: drafted
  review_note: possible conflict with c9 (same source; check the conditions)
- claim_id: c11
  attr: frequency
  value:
    nominal: 60
    unit: unit:HZ
  conditions: Rated grid frequency, all listed models
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=18.r16
    h: 986c1de324ee
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=17.r16
    h: 8f3192c76cac
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=16.r16
    h: a20e1e91e5a8
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=20.r16
    h: 8800ac861829
  review: drafted
- claim_id: c12
  attr: efficiency
  value:
    nominal: 99
    unit: unit:PERCENT
  conditions: Maximum efficiency, Solis-255K-EHV-5G-US
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=17.r17
    h: 4d752c79d763
  review: drafted
  review_note: possible conflict with c13 (same source; check the conditions); possible conflict with
    c14 (same source; check the conditions); possible conflict with c15 (same source; check the conditions)
- claim_id: c13
  attr: efficiency
  value:
    nominal: 98.7
    unit: unit:PERCENT
  conditions: Maximum efficiency, Solis-185K-EHV-5G-US and -PLUS
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=16.r17
    h: a0e8d0cb6d2d
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=19.r17
    h: c80f1cba003b
  review: drafted
  review_note: possible conflict with c12 (same source; check the conditions); possible conflict with
    c14 (same source; check the conditions); possible conflict with c15 (same source; check the conditions)
- claim_id: c14
  attr: efficiency
  value:
    nominal: 98.6
    unit: unit:PERCENT
  conditions: Maximum efficiency, Solis-125K-EHV-5G-US-PLUS
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=18.r17
    h: ac5bfc7d3abf
  review: drafted
  review_note: possible conflict with c12 (same source; check the conditions); possible conflict with
    c13 (same source; check the conditions); possible conflict with c15 (same source; check the conditions)
- claim_id: c15
  attr: efficiency
  value:
    nominal: 98.3
    unit: unit:PERCENT
  conditions: CEC efficiency, Solis-125K-EHV-5G-US-PLUS, Solis-185K-EHV-5G-US and Solis-255K-EHV-5G-US
  cite:
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=18.r18
    h: 68c480074f05
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=17.r18
    h: b3963119f1b8
  - src: src:solis-solis-manual-3p-125-255-k-5g-usa-v1-9-20230620
    loc: tbl=16.r18
    h: c2c06e681553
  review: drafted
  review_note: possible conflict with c12 (same source; check the conditions); possible conflict with
    c13 (same source; check the conditions); possible conflict with c14 (same source; check the conditions)
---
Its CSA listing covers wall-mounted, permanently connected installation. The DC input accepts up to 1500 V and uses MC4 connectors. The 255K models connect to an 800 V three-phase grid, and the 185K and 125K-PLUS models connect to 600 V, all at 60 Hz. Maximum efficiency is 98.6 to 99.0 percent depending on the model, and the CEC efficiency is 98.3 percent. Communication is over RS485, with PLC as an option, and the unit has a two-line LCD display. The 185K and 255K models have integrated PID recovery.

<!-- review notes
- sentence 5: support check: partial - RS485/PLC and a 2x20 LCD are supported, but the evidence doesn't say 'two-line' explicitly beyond 2x20 notation; reasonable inference.
-->
