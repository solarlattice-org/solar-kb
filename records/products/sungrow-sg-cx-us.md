---
id: prod:sungrow-sg-cx-us
type: Product
name: Sungrow SG36/60CX-US
aliases:
- 36_60CX-US
- SG36CX-US
- SG60CX-US
- SG36CX
- SG60CX
category: Inverters
make: sungrow
product_level: family
claims:
- claim_id: c1
  attr: efficiency
  value:
    nominal: 98
    unit: unit:PERCENT
  conditions: CEC efficiency, SG36CX-US and SG60CX-US
  cite:
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=43.r23
    h: 02d5e93bff1f
  review: drafted
  review_note: possible conflict with c2 (same source; check the conditions); possible conflict with c3
    (same source; check the conditions)
- claim_id: c2
  attr: efficiency
  value:
    nominal: 98.6
    unit: unit:PERCENT
  conditions: Maximum efficiency, SG36CX-US
  cite:
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=43.r22
    h: 468cd74f9f9f
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-24
  review_note: possible conflict with c1 (same source; check the conditions); possible conflict with c3
    (same source; check the conditions)
- claim_id: c3
  attr: efficiency
  value:
    nominal: 98.8
    unit: unit:PERCENT
  conditions: Maximum efficiency, SG60CX-US
  cite:
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=43.r22
    h: 468cd74f9f9f
  review: drafted
  review_note: possible conflict with c1 (same source; check the conditions); possible conflict with c2
    (same source; check the conditions)
- claim_id: c4
  attr: mppt_voltage_range
  value:
    min: 550
    max: 850
    unit: unit:V
  conditions: MPP voltage range for rated power, SG36CX-US and SG60CX-US (footnoted in source)
  cite:
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=43.r6
    h: e82f97b3ace0
  review: drafted
- claim_id: c5
  attr: max_input_current
  value:
    nominal: 26
    unit: unit:A
  conditions: Max PV input current per input; listed as 26A*4 for SG36CX-US
  cite:
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=43.r9
    h: 6ec56eaa93f0
  review: drafted
- claim_id: c6
  attr: max_input_current
  value:
    nominal: 26
    unit: unit:A
  conditions: Max PV input current per input; listed as 26A*6 for SG60CX-US
  cite:
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=43.r9
    h: 6ec56eaa93f0
  review: drafted
- claim_id: c7
  rel: uses_protocol
  target: proto:rs485
  cite:
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=44.r23
    h: 6ab440b4244a
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: sec=5.9
    h: 18a66a841711
  review: drafted
- claim_id: c8
  rel: uses_protocol
  target: proto:sunspec-modbus
  note: Third-party protocol; cannot be used at the same time as SG Modbus
  cite:
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=44.r24
    h: 0b0919c9c22f
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: sec=h129
    h: cd6333af7bc9
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: sec=h125
    h: cd6333af7bc9
  review: drafted
- claim_id: c9
  rel: uses_protocol
  target: proto:sungrow-sg-modbus
  note: Cannot be used at the same time as SunSpec Modbus
  cite:
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: sec=h129
    h: cd6333af7bc9
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: sec=h125
    h: cd6333af7bc9
  review: drafted
  review_note: 'support check: partial - Warning mentions SG Modbus as exclusive alternative, implying
    availability, but no passage explicitly lists SG Modbus as used by this product.'
- claim_id: c10
  rel: implements
  target: func:string-monitoring
  conditions: Listed for SG60CX-US
  cite:
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=44.r7
    h: 720f6a222443
  review: drafted
- claim_id: c11
  rel: implements
  target: func:residual-current-monitoring
  note: Datasheet lists leakage current protection for SG60CX-US
  cite:
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=44.r3
    h: 5abe59bb2466
  review: drafted
  review_note: 'support check: partial - Leakage current protection is listed, but equating it with residual
    current monitoring is a slight stretch; the note itself matches.'
- claim_id: c12
  rel: implements
  target: func:dc-injection-limitation
  note: DC current injection specified below 0.5% of rated current
  cite:
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=43.r18
    h: bfb208099126
  review: drafted
  review_note: 'support check: partial - DC current injection <0.5%In is specified, but limitation function
    is only implied.'
---
The Sungrow SG36/60CX-US is a family of string inverters that includes the SG36CX-US and SG60CX-US models. Both models have a CEC efficiency of 98.00 percent. Maximum efficiency is 98.60 percent for the SG36CX-US and 98.80 percent for the SG60CX-US. Full rated power is available across an MPP voltage range of 550 V to 850 V. Each PV input accepts up to 26 A: the SG36CX-US has four inputs and the SG60CX-US has six. The AC voltage range is 422 V to 528 V, and DC current injection is kept below 0.5 percent of rated current. Communication runs over RS485, and SunSpec Modbus is supported for third-party systems. SunSpec and SG Modbus cannot be active at the same time. The SG60CX-US datasheet lists a DC switch, an AC switch, grid monitoring, leakage current protection and PV string monitoring. Status is shown on an LED display. If a product fault occurs during the warranty period, Sungrow will either service the unit for free or replace it with a new one.

<!-- review notes
- sentence 1: support check: partial - Both models appear in tables, but 'family of string inverters' isn't stated.
- sentence 1: review: partial - Both the SG36CX-US and SG60CX-US models appear in the quoted rows, but nothing quoted calls them a family of string inverters.
-->
