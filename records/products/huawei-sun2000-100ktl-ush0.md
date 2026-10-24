---
id: prod:huawei-sun2000-100ktl-ush0
type: Product
name: Huawei SUN2000-100KTL-USH0
aliases:
- SUN2000-100KTL-USH0
- SUN2000
category: Inverters
make: huawei
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:huawei
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: sec=h1
    h: 1b8e916060f8
  review: drafted
- claim_id: c2
  rel: uses_protocol
  target: proto:rs485
  note: PLC and RS485 are both supported, but only one can be used at a time.
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=63.r2
    h: e8d24809ce23
  - src: src:huawei-huawei-sun2000-100ktl-ush0-quick-guide
    loc: sec=h20
    h: 7580aad88118
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: sec=5.3
    h: b2714b7f47bd
  review: drafted
- claim_id: c3
  rel: uses_protocol
  target: proto:power-line-communication
  note: PLC and RS485 are both supported, but only one can be used at a time.
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=63.r3
    h: f2988dfcc771
  - src: src:huawei-huawei-sun2000-100ktl-ush0-quick-guide
    loc: sec=h20
    h: 7580aad88118
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: sec=5.3
    h: b2714b7f47bd
  review: drafted
- claim_id: c4
  rel: requires
  target: prod:staubli-mc4
  note: Use the Staubli MC4 metal terminals and DC connectors shipped with the inverter; damage caused
    by incompatible connectors is excluded from warranty.
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-quick-guide
    loc: sec=h20
    h: 7580aad88118
  review: drafted
- claim_id: c5
  rel: certified_to
  target: std:fcc-part-15b
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=5.r1
    h: 2abd0e17e04c
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=5
    h: 5024ff98d421
  review: drafted
- claim_id: c6
  rel: certified_to
  target: std:fcc-part-15g
  note: Listed as printed in the compliance symbols table.
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=5.r2
    h: 8641280dab70
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=5
    h: 5024ff98d421
  review: drafted
- claim_id: c7
  attr: max_input_voltage
  value:
    max: 1500
    unit: unit:V
  conditions: DC voltage at the DC input terminals, checked with a multimeter before connecting strings
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-quick-guide
    loc: sec=h20
    h: 7580aad88118
  review: drafted
  review_note: 'support check: partial - 1500 V is a limit not to exceed in the DC voltage check; the
    passages don''t call it the max input voltage spec explicitly, though strongly implied.'
- claim_id: c8
  attr: efficiency
  value:
    nominal: 99
    unit: unit:PERCENT
  conditions: Maximum efficiency
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=60.r1
    h: be46d6506b2a
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=60
    h: a0144aa4de5a
  review: drafted
  review_note: possible conflict with c9 (same source; check the conditions)
- claim_id: c9
  attr: efficiency
  value:
    nominal: 98.5
    unit: unit:PERCENT
  conditions: CEC efficiency
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=60
    h: a0144aa4de5a
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=60.r2
    h: db646f5055d1
  review: drafted
  review_note: possible conflict with c8 (same source; check the conditions)
- claim_id: c10
  attr: rated_output_current
  value:
    nominal: 72.9
    unit: unit:A
  conditions: Rated AC output current
  cite:
  - src: src:huawei-huawei-sun2000-100ktl-ush0-user-manual
    loc: tbl=64.r5
    h: 91a45102ebdf
  review: drafted
---
The Huawei SUN2000-100KTL-USH0 is a string inverter from Huawei, and its user manual calls it the SUN2000. Its maximum efficiency is 99.00 percent and its CEC efficiency is 98.50 percent. Rated output current is 72.9 A. Before connecting strings, use a multimeter to confirm that the DC input voltage does not exceed 1500 V and that the polarity is correct, or the inverter can be damaged. If a string is connected with reversed polarity while the DC switch is on, do not switch off right away. Wait until the string current falls below 0.5 A, then fix the wiring. Use only the Staubli MC4 terminals and connectors supplied with the inverter. Damage caused by incompatible connectors is not covered by warranty. The inverter supports PLC and RS485 communication, but only one of the two can be used at a time. The manual lists FCC Part 15B, FCC Part 15G and CSA compliance marks for the inverter.

<!-- review notes
- sentence 1: support check: partial - Manual calls it SUN2000 and it's by Huawei, but 'string inverter' is not stated in the passages.
-->
