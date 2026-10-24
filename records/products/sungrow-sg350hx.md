---
id: prod:sungrow-sg350hx
type: Product
name: Sungrow SG350HX-US
aliases:
- SG350HX
- SG350HX-US
category: Inverters
make: sungrow
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:sungrow
  cite:
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: sec=9.3
    h: e0a94aac5535
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: sec=h1
    h: 8407ffd9bf1f
  review: drafted
  review_note: 'support check: partial - Passages mention SUNGROW warranty and the SG350HX-US title, but
    never explicitly state Sungrow manufactures this model (implied only).'
- claim_id: c2
  rel: instance_of
  target: comp:inverter
  note: PV grid-connected inverter
  cite:
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: sec=h1
    h: 8407ffd9bf1f
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=5.r2
    h: e91b2dcaf5e4
  review: drafted
- claim_id: c3
  rel: uses_protocol
  target: proto:rs485
  note: RS485 connection on COM1 per the quick installation guide
  cite:
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=41.r6
    h: 481165dab06a
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=3.r22
    h: 22793dca4dd0
  - src: src:sungrow-sungrow-sg350hx-us-quick-installation-guide
    loc: sec=h15
    h: 73d1b48b8ca6
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: sec=5.8.2
    h: 23149c859eea
  review: drafted
- claim_id: c4
  rel: uses_protocol
  target: proto:power-line-communication
  cite:
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=41.r6
    h: 481165dab06a
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=3.r24
    h: 48d6b8bc20af
  review: drafted
- claim_id: c5
  rel: uses_protocol
  target: proto:bluetooth
  note: Local display is LEDs plus Bluetooth with an app
  cite:
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=41.r5
    h: a98ba6362a18
  review: drafted
- claim_id: c6
  rel: certified_to
  target: std:ul-1741
  cite:
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=41.r9
    h: a4584af8cea9
  review: drafted
- claim_id: c7
  rel: certified_to
  target: std:ul-1741-sa
  cite:
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=41.r9
    h: a4584af8cea9
  review: drafted
- claim_id: c8
  rel: certified_to
  target: std:ul-1741-sb
  cite:
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=41.r9
    h: a4584af8cea9
  review: drafted
- claim_id: c9
  rel: certified_to
  target: std:ul-62109-1
  cite:
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=41.r9
    h: a4584af8cea9
  review: drafted
- claim_id: c10
  rel: certified_to
  target: std:ieee-1547-2018
  cite:
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=41.r9
    h: a4584af8cea9
  review: drafted
- claim_id: c11
  rel: certified_to
  target: std:ieee-1547-1-2020
  cite:
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=41.r9
    h: a4584af8cea9
  review: drafted
- claim_id: c12
  rel: certified_to
  target: std:cpuc-rule-21
  cite:
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=41.r9
    h: a4584af8cea9
  review: drafted
- claim_id: c13
  rel: certified_to
  target: std:heco-srd-v2-0
  cite:
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=41.r9
    h: a4584af8cea9
  review: drafted
- claim_id: c14
  rel: implements
  target: func:reverse-polarity-protection
  note: DC reverse connection protection
  cite:
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=40.r6
    h: 8ae902b4e8e0
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=40
    h: b57a1a527249
  review: drafted
- claim_id: c15
  rel: implements
  target: func:residual-current-monitoring
  note: Listed as leakage current protection
  cite:
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=40.r8
    h: c02c44861dc8
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=40
    h: b57a1a527249
  review: drafted
- claim_id: c16
  rel: implements
  target: func:ground-fault-protection
  note: Listed as ground fault monitoring
  cite:
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=40
    h: b57a1a527249
  review: drafted
- claim_id: c17
  rel: implements
  target: func:string-monitoring
  cite:
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=40.r12
    h: dc748d0b3056
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=40
    h: b57a1a527249
  review: drafted
- claim_id: c18
  rel: implements
  target: func:night-reactive-power
  cite:
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=40.r13
    h: 8c7a1b750c37
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=40
    h: b57a1a527249
  review: drafted
- claim_id: c19
  rel: implements
  target: func:surge-protection
  note: Type II on both DC and AC sides
  cite:
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=40.r15
    h: 30f0353a71c9
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=40
    h: b57a1a527249
  review: drafted
- claim_id: c20
  rel: implements
  target: func:pid-recovery
  note: Optional, provided with the EMU200 accessory
  cite:
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=40
    h: b57a1a527249
  review: drafted
- claim_id: c21
  rel: requires
  target: prod:sungrow-emu200
  note: Needed only for the optional anti-PID and PID recovery function
  cite:
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=40
    h: b57a1a527249
  review: drafted
  review_note: 'support check: partial - EMU200 is tied to the optional anti-PID function, but ''requires''
    is only implied as optional and not stated as a requirement.'
- claim_id: c22
  attr: efficiency
  value:
    nominal: 99.02
    unit: unit:PERCENT
  conditions: Maximum efficiency
  cite:
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=40.r4
    h: 9d41de21bb96
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=40
    h: b57a1a527249
  review: drafted
  review_note: possible conflict with c23 (same source; check the conditions)
- claim_id: c23
  attr: efficiency
  value:
    nominal: 98.5
    unit: unit:PERCENT
  conditions: CEC weighted efficiency
  cite:
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=40.r4
    h: 9d41de21bb96
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=40
    h: b57a1a527249
  review: drafted
  review_note: possible conflict with c22 (same source; check the conditions)
- claim_id: c24
  attr: mppt_voltage_range
  value:
    min: 860
    max: 1330
    unit: unit:V
  conditions: Full power MPP voltage range at 40 °C
  cite:
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=39.r6
    h: cfc7f2773243
  review: drafted
- claim_id: c25
  attr: rated_output_current
  value:
    nominal: 254
    unit: unit:A
  conditions: Maximum AC output current
  cite:
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=39.r13
    h: c8189404bfe9
  review: drafted
---
The Sungrow SG350HX-US is a transformerless three-phase PV inverter that connects to the grid. Its maximum efficiency is 99.02 percent and its CEC efficiency is 98.5 percent. Its maximum AC output current is 254 A. At 40 °C, full-power MPP tracking covers 860 V to 1330 V. The AC voltage range is 704 V to 880 V. Built-in protection covers DC reverse connection, AC short circuit, leakage current, ground faults and grid monitoring. It also has Type II surge protection on the DC and AC sides. The inverter has a DC switch but no AC switch. It supports PV string current monitoring and reactive power at night. Anti-PID and PID recovery are optional and need the EMU200. It communicates over RS485 and PLC, and on site you can reach it through LED indicators or Bluetooth with an app. The inverter is listed to UL 1741 including SA and SB, UL 62109-1, CSA C22.2 No.107.1, IEEE 1547-2018, IEEE 1547.1-2020, California Rule 21 and HECO SRD V2.0. It is IP66 (NEMA 4X) rated, cooled by smart forced air, and weighs up to 123 kg.
