---
id: prod:yaskawa-solectria-pvi-3800-7600tl
type: Product
name: Solectria PVI 3800-7600TL
aliases:
- PVI 3800 7600 TL
category: Inverters
make: yaskawa-solectria
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:yaskawa-solectria
  cite:
  - src: src:yaskawa-solectria-solectria-pvi-3800-7600tl-manual-0527-2014-rev-d-feb2018
    loc: sec=h1
    h: 3f5b5ed02ed5
  review: drafted
  review_note: 'support check: partial - Passage shows garbled ''VYASA SOLECTRIA SOLAR'' with the model
    names; maker identity is implied but not clearly stated as Yaskawa.'
- claim_id: c2
  rel: instance_of
  target: comp:inverter
  note: Listed as a transformerless utility-interactive inverter, permanently connected.
  cite:
  - src: src:yaskawa-solectria-solectria-pvi-3800-7600tl-manual-0527-2014-rev-d-feb2018
    loc: sec=h206
    h: f48975fb92ea
  review: drafted
- claim_id: c3
  rel: uses_protocol
  target: proto:rs485
  note: RS-485 is the communication interface on all four models.
  cite:
  - src: src:yaskawa-solectria-solectria-pvi-3800-7600tl-manual-0527-2014-rev-d-feb2018
    loc: tbl=54.r6
    h: 34679161bd39
  review: drafted
- claim_id: c4
  rel: certified_to
  target: std:ul-1741
  note: Listed under safety standards.
  cite:
  - src: src:yaskawa-solectria-solectria-pvi-3800-7600tl-manual-0527-2014-rev-d-feb2018
    loc: tbl=55.r2
    h: 3c3990b4f765
  review: drafted
- claim_id: c5
  rel: certified_to
  target: std:ul-1998
  note: Software approval.
  cite:
  - src: src:yaskawa-solectria-solectria-pvi-3800-7600tl-manual-0527-2014-rev-d-feb2018
    loc: tbl=55.r3
    h: 6084441ae912
  review: drafted
- claim_id: c6
  rel: certified_to
  target: std:ieee-1547
  note: Covers unintentional islanding protection.
  cite:
  - src: src:yaskawa-solectria-solectria-pvi-3800-7600tl-manual-0527-2014-rev-d-feb2018
    loc: tbl=55.r5
    h: 2d4d84517382
  review: drafted
- claim_id: c7
  rel: certified_to
  target: std:ieee-1547-1
  note: Covers unintentional islanding protection; the source gives no edition.
  cite:
  - src: src:yaskawa-solectria-solectria-pvi-3800-7600tl-manual-0527-2014-rev-d-feb2018
    loc: tbl=55.r5
    h: 2d4d84517382
  review: drafted
- claim_id: c8
  rel: certified_to
  target: std:ul-1699b
  note: AFCI, Type 1.
  cite:
  - src: src:yaskawa-solectria-solectria-pvi-3800-7600tl-manual-0527-2014-rev-d-feb2018
    loc: tbl=55.r7
    h: 8cfaa8093fca
  review: drafted
- claim_id: c9
  rel: certified_to
  target: std:fcc-part-15
  note: 'EMC: FCC part 15 A and B.'
  cite:
  - src: src:yaskawa-solectria-solectria-pvi-3800-7600tl-manual-0527-2014-rev-d-feb2018
    loc: tbl=55.r6
    h: b7c7b19471df
  review: drafted
- claim_id: c10
  rel: certified_to
  target: std:ices-003
  note: EMC.
  cite:
  - src: src:yaskawa-solectria-solectria-pvi-3800-7600tl-manual-0527-2014-rev-d-feb2018
    loc: tbl=55.r6
    h: b7c7b19471df
  review: drafted
- claim_id: c11
  rel: implements
  target: func:anti-islanding
  cite:
  - src: src:yaskawa-solectria-solectria-pvi-3800-7600tl-manual-0527-2014-rev-d-feb2018
    loc: tbl=55.r5
    h: 2d4d84517382
  review: drafted
- claim_id: c12
  rel: implements
  target: func:dc-arc-fault-protection
  cite:
  - src: src:yaskawa-solectria-solectria-pvi-3800-7600tl-manual-0527-2014-rev-d-feb2018
    loc: tbl=55.r7
    h: 8cfaa8093fca
  review: drafted
- claim_id: c13
  rel: implements
  target: func:insulation-monitoring
  note: Isolation Monitor Interrupt (IMI).
  cite:
  - src: src:yaskawa-solectria-solectria-pvi-3800-7600tl-manual-0527-2014-rev-d-feb2018
    loc: tbl=55.r4
    h: aa337922f3b0
  review: drafted
- claim_id: c14
  rel: implements
  target: func:mppt
  note: PVI 3800TL has 1 MPP tracker; the 5200TL, 6600TL and 7600TL have 2.
  cite:
  - src: src:yaskawa-solectria-solectria-pvi-3800-7600tl-manual-0527-2014-rev-d-feb2018
    loc: tbl=51.r9
    h: 90d325f889c6
  review: drafted
- claim_id: c15
  attr: rated_power
  value:
    nominal: 3800
    unit: unit:W
  conditions: PVI 3800TL nominal AC output power
  cite:
  - src: src:yaskawa-solectria-solectria-pvi-3800-7600tl-manual-0527-2014-rev-d-feb2018
    loc: tbl=52.r1
    h: b4b66cc03d5b
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-24
  review_note: possible conflict with c16 (same source; check the conditions); possible conflict with
    c17 (same source; check the conditions); possible conflict with c18 (same source; check the conditions);
    possible conflict with c19 (same source; check the conditions)
- claim_id: c16
  attr: rated_power
  value:
    nominal: 5200
    unit: unit:W
  conditions: PVI 5200TL nominal AC output power
  cite:
  - src: src:yaskawa-solectria-solectria-pvi-3800-7600tl-manual-0527-2014-rev-d-feb2018
    loc: tbl=52.r1
    h: b4b66cc03d5b
  review: drafted
  review_note: possible conflict with c15 (same source; check the conditions); possible conflict with
    c17 (same source; check the conditions); possible conflict with c18 (same source; check the conditions);
    possible conflict with c19 (same source; check the conditions)
- claim_id: c17
  attr: rated_power
  value:
    nominal: 6600
    unit: unit:W
  conditions: PVI 6600TL nominal AC output power
  cite:
  - src: src:yaskawa-solectria-solectria-pvi-3800-7600tl-manual-0527-2014-rev-d-feb2018
    loc: tbl=52.r1
    h: b4b66cc03d5b
  review: drafted
  review_note: possible conflict with c15 (same source; check the conditions); possible conflict with
    c16 (same source; check the conditions); possible conflict with c18 (same source; check the conditions);
    possible conflict with c19 (same source; check the conditions)
- claim_id: c18
  attr: rated_power
  value:
    nominal: 7600
    unit: unit:W
  conditions: PVI 7600TL nominal AC output power
  cite:
  - src: src:yaskawa-solectria-solectria-pvi-3800-7600tl-manual-0527-2014-rev-d-feb2018
    loc: tbl=52.r1
    h: b4b66cc03d5b
  review: drafted
  review_note: possible conflict with c15 (same source; check the conditions); possible conflict with
    c16 (same source; check the conditions); possible conflict with c17 (same source; check the conditions);
    possible conflict with c19 (same source; check the conditions); possible conflict with c20 (same source;
    check the conditions)
- claim_id: c19
  attr: rated_power
  value:
    max: 3300
    unit: unit:W
  conditions: PVI 3800TL maximum AC power at 208 V
  cite:
  - src: src:yaskawa-solectria-solectria-pvi-3800-7600tl-manual-0527-2014-rev-d-feb2018
    loc: tbl=52.r2
    h: 457ec6ea8ed8
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: possible conflict with c15 (same source; check the conditions); possible conflict with
    c16 (same source; check the conditions); possible conflict with c17 (same source; check the conditions);
    possible conflict with c18 (same source; check the conditions)
- claim_id: c20
  attr: rated_power
  value:
    max: 6600
    unit: unit:W
  conditions: PVI 7600TL maximum AC power at 208 V
  cite:
  - src: src:yaskawa-solectria-solectria-pvi-3800-7600tl-manual-0527-2014-rev-d-feb2018
    loc: tbl=52.r2
    h: 457ec6ea8ed8
  review: drafted
  review_note: possible conflict with c18 (same source; check the conditions)
- claim_id: c21
  attr: max_input_voltage
  value:
    max: 600
    unit: unit:V
  conditions: Maximum DC system voltage, all models
  cite:
  - src: src:yaskawa-solectria-solectria-pvi-3800-7600tl-manual-0527-2014-rev-d-feb2018
    loc: tbl=51.r2
    h: fefbd0daf618
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c22
  attr: mppt_voltage_range
  value:
    min: 200
    max: 500
    unit: unit:V
  conditions: Full-power MPP range, all models
  cite:
  - src: src:yaskawa-solectria-solectria-pvi-3800-7600tl-manual-0527-2014-rev-d-feb2018
    loc: tbl=51.r4
    h: b8278f8938d3
  review: drafted
- claim_id: c23
  attr: efficiency
  value:
    nominal: 98
    unit: unit:PERCENT
  conditions: Maximum efficiency, all models
  cite:
  - src: src:yaskawa-solectria-solectria-pvi-3800-7600tl-manual-0527-2014-rev-d-feb2018
    loc: tbl=53.r1
    h: ae2098720996
  review: drafted
  review_note: possible conflict with c24 (same source; check the conditions)
- claim_id: c24
  attr: efficiency
  value:
    nominal: 97.5
    unit: unit:PERCENT
  conditions: CEC efficiency at 208 V and 240 V, all models
  cite:
  - src: src:yaskawa-solectria-solectria-pvi-3800-7600tl-manual-0527-2014-rev-d-feb2018
    loc: tbl=53.r2
    h: ea3678d0ea15
  review: drafted
  review_note: possible conflict with c23 (same source; check the conditions)
- claim_id: c25
  attr: warranty_term
  value:
    nominal: 10
    unit: unit:YR
  conditions: Standard warranty, all models
  cite:
  - src: src:yaskawa-solectria-solectria-pvi-3800-7600tl-manual-0527-2014-rev-d-feb2018
    loc: tbl=56
    h: 5a382f024a95
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
The Solectria PVI 3800-7600TL is a family of transformerless, utility-interactive inverters for permanent connection. It comes in four models: PVI 3800TL, 5200TL, 6600TL and 7600TL. Nominal AC output runs from 3800 W to 7600 W. At 208 V the 3800TL is limited to 3300 W and the 7600TL to 6600 W. All models accept up to 600 V DC system voltage, with a full-power MPP range of 200 to 500 V. The 3800TL has one MPP tracker and the larger models have two. Maximum efficiency is 98.0 percent, and CEC efficiency is 97.5 percent at both 208 V and 240 V. The units have an internal DC disconnect, screw terminals for AC and DC wiring, convection cooling and an RS-485 communication interface. They are listed to UL 1741 and CSA 22.2 No. 107-01, have UL 1998 software approval, and meet IEEE 1547 and 1547.1 for anti-islanding. Arc-fault protection is to UL 1699B Type 1, and isolation monitoring is to NEC 690.35. EMC compliance covers FCC part 15 A and B and ICES-003. The standard warranty is 10 years.
