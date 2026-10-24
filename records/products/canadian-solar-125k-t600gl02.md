---
id: prod:canadian-solar-125k-t600gl02
type: Product
name: CSI-125K-T600GL02-U
aliases:
- CSI-125-T600GL02-U
category: Inverters
make: canadian-solar
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:canadian-solar
  cite:
  - src: src:csi-csi-user-manual-125k-t600gl02-u-na-v1-1-20210518
    loc: sec=1.1
    h: b26f8ecc3cf9
  review: drafted
  review_note: 'support check: partial - Passage says Canadian Solar inverter manual covers CSI-125-T600GL02-U;
    the exact model name differs slightly (no K) but manufacturer is stated.'
- claim_id: c2
  rel: instance_of
  target: comp:inverter
  note: Three-phase transformerless grid-support utility-interactive PV inverter
  cite:
  - src: src:csi-csi-user-manual-125k-t600gl02-u-na-v1-1-20210518
    loc: sec=1.1
    h: b26f8ecc3cf9
  review: drafted
- claim_id: c3
  attr: rated_power
  value:
    nominal: 125000
    unit: unit:V-A
  conditions: Maximum apparent output power
  cite:
  - src: src:csi-csi-user-manual-125k-t600gl02-u-na-v1-1-20210518
    loc: tbl=12.r10
    h: a82c9009afee
  review: drafted
- claim_id: c4
  attr: max_input_voltage
  value:
    max: 1500
    unit: unit:V
  conditions: Maximum DC input voltage
  cite:
  - src: src:csi-csi-user-manual-125k-t600gl02-u-na-v1-1-20210518
    loc: tbl=12.r1
    h: 3b4b33d5b5a9
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c5
  attr: rated_output_current
  value:
    max: 120
    unit: unit:A
  conditions: Maximum AC output current at 600 V
  cite:
  - src: src:csi-csi-user-manual-125k-t600gl02-u-na-v1-1-20210518
    loc: tbl=12.r12
    h: 523116ba7347
  - src: src:csi-csi-user-manual-125k-t600gl02-u-na-v1-1-20210518
    loc: tbl=4.r1
    h: 4a6bcbaa0bff
  review: drafted
- claim_id: c6
  attr: nominal_voltage
  value:
    nominal: 600
    unit: unit:V
  conditions: Rated three-phase grid voltage (3/PE)
  cite:
  - src: src:csi-csi-user-manual-125k-t600gl02-u-na-v1-1-20210518
    loc: tbl=12.r11
    h: e8912f9cb59a
  - src: src:csi-csi-user-manual-125k-t600gl02-u-na-v1-1-20210518
    loc: tbl=4.r1
    h: 4a6bcbaa0bff
  review: drafted
- claim_id: c7
  attr: frequency
  value:
    nominal: 60
    unit: unit:HZ
  conditions: Rated grid frequency
  cite:
  - src: src:csi-csi-user-manual-125k-t600gl02-u-na-v1-1-20210518
    loc: tbl=12.r15
    h: f7ccfa38da3b
  review: drafted
- claim_id: c8
  attr: frequency
  value:
    min: 59.5
    max: 60.5
    unit: unit:HZ
  conditions: Grid frequency range
  cite:
  - src: src:csi-csi-user-manual-125k-t600gl02-u-na-v1-1-20210518
    loc: tbl=12.r16
    h: e8857e60adeb
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c9
  attr: efficiency
  value:
    nominal: 99.1
    unit: unit:PERCENT
  conditions: Maximum (peak) efficiency
  cite:
  - src: src:csi-csi-user-manual-125k-t600gl02-u-na-v1-1-20210518
    loc: tbl=12.r17
    h: bad6374ce314
  review: drafted
  review_note: possible conflict with c10 (same source; check the conditions)
- claim_id: c10
  attr: efficiency
  value:
    nominal: 98.6
    unit: unit:PERCENT
  conditions: EU weighted efficiency
  cite:
  - src: src:csi-csi-user-manual-125k-t600gl02-u-na-v1-1-20210518
    loc: tbl=12.r18
    h: 9106f2fe80e3
  review: drafted
  review_note: possible conflict with c9 (same source; check the conditions)
- claim_id: c11
  attr: operating_temperature
  value:
    min: -25
    max: 60
    unit: unit:DEG_C
  conditions: Operating ambient temperature range
  cite:
  - src: src:csi-csi-user-manual-125k-t600gl02-u-na-v1-1-20210518
    loc: tbl=12.r23
    h: a69ebb279894
  review: drafted
- claim_id: c12
  attr: warranty_term
  value:
    nominal: 10
    unit: unit:YR
  conditions: Standard warranty
  cite:
  - src: src:csi-csi-user-manual-125k-t600gl02-u-na-v1-1-20210518
    loc: tbl=12.r34
    h: 43b6f7f53bd8
  review: drafted
- claim_id: c13
  attr: warranty_term
  value:
    max: 20
    unit: unit:YR
  conditions: Extended warranty option
  cite:
  - src: src:csi-csi-user-manual-125k-t600gl02-u-na-v1-1-20210518
    loc: tbl=12.r34
    h: 43b6f7f53bd8
  review: drafted
- claim_id: c14
  rel: uses_protocol
  target: proto:rs485
  cite:
  - src: src:csi-csi-user-manual-125k-t600gl02-u-na-v1-1-20210518
    loc: tbl=12.r33
    h: 36eb1345b47c
  - src: src:csi-csi-user-manual-125k-t600gl02-u-na-v1-1-20210518
    loc: tbl=1.r23
    h: b8fa5e23d9e5
  review: drafted
- claim_id: c15
  rel: uses_protocol
  target: proto:ethernet
  cite:
  - src: src:csi-csi-user-manual-125k-t600gl02-u-na-v1-1-20210518
    loc: tbl=12.r33
    h: 36eb1345b47c
  - src: src:csi-csi-user-manual-125k-t600gl02-u-na-v1-1-20210518
    loc: tbl=1.r24
    h: 5d58ef208b77
  review: drafted
- claim_id: c16
  rel: uses_protocol
  target: proto:power-line-communication
  note: Optional
  cite:
  - src: src:csi-csi-user-manual-125k-t600gl02-u-na-v1-1-20210518
    loc: tbl=12.r33
    h: 36eb1345b47c
  review: drafted
- claim_id: c17
  rel: certified_to
  target: std:ul-1741
  cite:
  - src: src:csi-csi-user-manual-125k-t600gl02-u-na-v1-1-20210518
    loc: tbl=12.r29
    h: cdba39349e2e
  review: drafted
- claim_id: c18
  rel: certified_to
  target: std:ul-1741-sa
  cite:
  - src: src:csi-csi-user-manual-125k-t600gl02-u-na-v1-1-20210518
    loc: tbl=12.r29
    h: cdba39349e2e
  review: drafted
- claim_id: c19
  rel: certified_to
  target: std:cpuc-rule-21
  note: Including Rule 21 Phase II and III
  cite:
  - src: src:csi-csi-user-manual-125k-t600gl02-u-na-v1-1-20210518
    loc: tbl=12.r29
    h: cdba39349e2e
  review: drafted
- claim_id: c20
  rel: certified_to
  target: std:ul-1998
  cite:
  - src: src:csi-csi-user-manual-125k-t600gl02-u-na-v1-1-20210518
    loc: tbl=12.r29
    h: cdba39349e2e
  review: drafted
- claim_id: c21
  rel: certified_to
  target: std:ieee-1547
  note: Edition not stated
  cite:
  - src: src:csi-csi-user-manual-125k-t600gl02-u-na-v1-1-20210518
    loc: tbl=12.r29
    h: cdba39349e2e
  review: drafted
- claim_id: c22
  rel: certified_to
  target: std:fcc-part-15
  note: Class A and B
  cite:
  - src: src:csi-csi-user-manual-125k-t600gl02-u-na-v1-1-20210518
    loc: tbl=12.r29
    h: cdba39349e2e
  review: drafted
- claim_id: c23
  rel: certified_to
  target: std:csa-c22-2-no-107-1
  note: 107.1-16
  cite:
  - src: src:csi-csi-user-manual-125k-t600gl02-u-na-v1-1-20210518
    loc: tbl=12.r29
    h: cdba39349e2e
  review: drafted
---
The CSI-125K-T600GL02-U is a Canadian Solar three-phase transformerless, grid-support, utility-interactive PV inverter that converts array DC power to AC for local loads and the grid. It delivers up to 125000 VA of apparent power on a 600 V three-phase grid at 60 Hz, with a maximum output current of 120 A. Maximum efficiency is 99.1% and EU efficiency is 98.6%, and the unit operates in ambient temperatures from -25 to 60 °C. For communication it has RS485 and Ethernet, with power line communication available as an option. The standard warranty is 10 years and can be extended to 20 years. An OV-BUS alarm means the inverter has detected high DC voltage on its internal bus. Possible causes are internal damage or a wire that came loose during shipping. Measure the DC and AC voltages and compare them with the LCD. If the readings confirm the fault, replace the inverter.

<!-- review notes
- sentence 6: support check: partial - Row lists the causes and test/replace steps, but it doesn't say to replace only if readings confirm the fault, and the cause/solution pairing is loosely inferred.
-->
