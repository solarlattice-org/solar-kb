---
id: prod:chint-sca-50-100k-t
type: Product
name: CPS SCA100K-T-US-480 / SCA50K-T-US-208
aliases:
- SCA 100 K T US 480
- SCA 50 K T US 208
- SCA 100 K T
- SCA 50 K T
- SCA100K-T-US-480
- SCA50K-T-US-208
category: Inverters
make: chint
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:chint
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: sec=h10
    h: c7c6a063f679
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: sec=h171
    h: 0f5fc839faa5
  review: drafted
  review_note: 'support check: partial - Passages show the model names and ''CPS'' only; the full manufacturer
    name CHINT POWER SYSTEMS is not stated, though CPS is implied.'
- claim_id: c2
  rel: uses_protocol
  target: proto:rs485
  note: The manual has a section on RS485 communication wiring.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=3.r9
    h: 85f724902f8b
  review: drafted
  review_note: 'support check: partial - Only a table-of-contents entry for RS485 communication; it doesn''t
    explicitly say the inverter uses RS-485, though that is strongly implied.'
- claim_id: c3
  rel: certified_to
  target: std:ul-1741-sa
  note: Listed as UL1741-SA Ed. 2.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=73.r7
    h: 71f0023a0a55
  review: drafted
- claim_id: c4
  rel: certified_to
  target: std:ul-1741-sb
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=73.r7
    h: 71f0023a0a55
  review: drafted
- claim_id: c5
  rel: certified_to
  target: std:ul-1699b
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=73.r7
    h: 71f0023a0a55
  review: drafted
- claim_id: c6
  rel: certified_to
  target: std:ul-1998
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=73.r7
    h: 71f0023a0a55
  review: drafted
- claim_id: c7
  rel: certified_to
  target: std:ieee-1547-2018
  note: The manual lists this as IEEE1547a-2018.
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=73.r7
    h: 71f0023a0a55
  review: drafted
- claim_id: c8
  rel: certified_to
  target: std:fcc-part-15
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=73.r7
    h: 71f0023a0a55
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
- claim_id: c9
  attr: rated_power
  value:
    nominal: 100
    unit: unit:KiloW
  conditions: SCA100K-T-US-480, rated AC output power at PF >0.99 to ±0.91
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=71.r15
    h: 27eded104ddc
  review: drafted
  review_note: possible conflict with c10 (same source; check the conditions)
- claim_id: c10
  attr: rated_power
  value:
    nominal: 50
    unit: unit:KiloW
  conditions: SCA50K-T-US-208, rated AC output power at PF >0.99 to ±0.91
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=71.r15
    h: 27eded104ddc
  review: drafted
  review_note: possible conflict with c9 (same source; check the conditions)
- claim_id: c11
  attr: max_input_voltage
  value:
    nominal: 1000
    unit: unit:V
  conditions: Maximum DC input voltage, both SCA100K-T-US-480 and SCA50K-T-US-208
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=71.r4
    h: 47510b512c31
  review: drafted
- claim_id: c12
  attr: nominal_voltage
  value:
    nominal: 480
    unit: unit:V
  conditions: SCA100K-T-US-480, rated AC output voltage
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=71.r17
    h: 5de092800b65
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: possible conflict with c13 (same source; check the conditions)
- claim_id: c13
  attr: nominal_voltage
  value:
    nominal: 208
    unit: unit:V
  conditions: SCA50K-T-US-208, rated AC output voltage
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=71.r17
    h: 5de092800b65
  review: drafted
  review_note: possible conflict with c12 (same source; check the conditions)
- claim_id: c14
  attr: rated_output_current
  value:
    nominal: 120.4
    unit: unit:A
  conditions: SCA100K-T-US-480, max AC output current at 480 Vac; first of two values printed (120.4 /
    132.4 A)
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=71.r20
    h: ef92ac8b33ec
  review: drafted
  review_note: possible conflict with c15 (same source; check the conditions); possible conflict with
    c16 (same source; check the conditions); possible conflict with c17 (same source; check the conditions)
- claim_id: c15
  attr: rated_output_current
  value:
    nominal: 132.4
    unit: unit:A
  conditions: SCA100K-T-US-480, max AC output current at 480 Vac; second of two values printed (120.4
    / 132.4 A)
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=71.r20
    h: ef92ac8b33ec
  review: drafted
  review_note: possible conflict with c14 (same source; check the conditions); possible conflict with
    c16 (same source; check the conditions); possible conflict with c17 (same source; check the conditions)
- claim_id: c16
  attr: rated_output_current
  value:
    nominal: 138.8
    unit: unit:A
  conditions: SCA50K-T-US-208, max AC output current at 208 Vac; first of two values printed (138.8 /
    152.7 A)
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=71.r20
    h: ef92ac8b33ec
  review: drafted
  review_note: possible conflict with c14 (same source; check the conditions); possible conflict with
    c15 (same source; check the conditions); possible conflict with c17 (same source; check the conditions)
- claim_id: c17
  attr: rated_output_current
  value:
    nominal: 152.7
    unit: unit:A
  conditions: SCA50K-T-US-208, max AC output current at 208 Vac; second of two values printed (138.8 /
    152.7 A)
  cite:
  - src: src:chint-cps-sca100k-t-us-480-sca50k-t-us-208-user-manual-rev-1-0
    loc: tbl=71.r20
    h: ef92ac8b33ec
  review: drafted
  review_note: possible conflict with c14 (same source; check the conditions); possible conflict with
    c15 (same source; check the conditions); possible conflict with c16 (same source; check the conditions)
---
This CHINT Power Systems (CPS) family of three-phase string inverters has two models: the SCA100K-T-US-480 and the SCA50K-T-US-208. The SCA100K-T-US-480 is rated 100 kW at 480 Vac. The SCA50K-T-US-208 is rated 50 kW at 208 Vac. Both ratings apply at power factors from above 0.99 down to ±0.91. Both models accept up to 1000 Vdc at the DC input. Their operating DC input range runs from 200 to 1000 Vdc. The DC/AC ratio is 2, so the maximum PV power is 200 kW for the 100 kW model and 100 kW for the 50 kW model. The maximum AC output current is printed as 120.4 / 132.4 A for the 480 V model and 138.8 / 152.7 A for the 208 V model. The maximum AC overcurrent protection rating is 200 A for both models. The manual includes a section on RS485 communication wiring.

<!-- review notes
- sentence 1: support check: partial - Two models are named, but 'CHINT Power Systems', 'three-phase string inverters' and 'has two models' are not stated in the passages.
- sentence 1: review: partial - The two model names are supported, but CHINT Power Systems and three-phase string inverters are not stated in the passages.
-->
