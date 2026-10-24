---
id: prod:solis-s6-eh3p-75-150k-us
type: Product
name: Solis S6-EH3P(75-150)K10-NV-YD-H-US
aliases:
- S6-EH3P100K10-NV-YD-H-US
- S6-EH3P125K10-NV-YD-H-US
- S6-EH3P150K10-NV-YD-H-US
- S6-EH3P60K10-LV-YD-H-US
- S6-EH3P75K10-LV-YD-H-US
category: Inverters
make: solis
product_level: family
claims:
- claim_id: c1
  rel: manufactured_by
  target: org:solis
  cite:
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: sec=front
    h: 65d0ffd891c8
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: sec=h2
    h: fdb8ce3ab582
  review: drafted
  review_note: 'support check: partial - Models list is shown but nothing in the passages states the manufacturer
    beyond the bare ''solis'' token; the 75K model is LV, not NV.'
- claim_id: c2
  rel: implements
  target: func:dc-arc-fault-protection
  note: Datasheet lists integrated AFCI 2.0 as Yes for the 100K and 125K models.
  cite:
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=31.r51
    h: 8b60af9859b7
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=32.r48
    h: 0f3f889be5b9
  review: drafted
- claim_id: c3
  attr: frequency
  value:
    nominal: 60
    unit: unit:HZ
  conditions: Rated input frequency, 75K model
  cite:
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=32.r37
    h: 4a0c9ea145a3
  review: drafted
- claim_id: c4
  attr: frequency
  value:
    nominal: 60
    unit: unit:HZ
  conditions: Rated input frequency, 100K and 125K models
  cite:
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=31.r39
    h: c1bba7fd57a7
  review: drafted
- claim_id: c5
  attr: efficiency
  value:
    nominal: 95.2
    unit: unit:PERCENT
  conditions: CEC efficiency, 75K model
  cite:
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=32.r39
    h: 9aac588a6d57
  review: drafted
  review_note: possible conflict with c6 (same source; check the conditions); possible conflict with c7
    (same source; check the conditions); possible conflict with c8 (same source; check the conditions)
- claim_id: c6
  attr: efficiency
  value:
    nominal: 96
    unit: unit:PERCENT
  conditions: Maximum efficiency, 75K model
  cite:
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=32.r38
    h: 4718b1db62d6
  review: drafted
  review_note: possible conflict with c5 (same source; check the conditions); possible conflict with c7
    (same source; check the conditions); possible conflict with c8 (same source; check the conditions)
- claim_id: c7
  attr: efficiency
  value:
    nominal: 97.2
    unit: unit:PERCENT
  conditions: CEC efficiency, 100K and 125K models
  cite:
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=31.r41
    h: 236cb19a9c95
  review: drafted
  review_note: possible conflict with c5 (same source; check the conditions); possible conflict with c6
    (same source; check the conditions); possible conflict with c8 (same source; check the conditions)
- claim_id: c8
  attr: efficiency
  value:
    nominal: 97.6
    unit: unit:PERCENT
  conditions: Maximum efficiency, 100K and 125K models
  cite:
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=31.r40
    h: 22214aa9a922
  review: drafted
  review_note: possible conflict with c5 (same source; check the conditions); possible conflict with c6
    (same source; check the conditions); possible conflict with c7 (same source; check the conditions)
- claim_id: c9
  attr: rated_output_current
  value:
    nominal: 120.3
    unit: unit:A
  conditions: Rated output current, 100K model
  cite:
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=31.r32
    h: b606f824522e
  review: drafted
  review_note: possible conflict with c10 (same source; check the conditions); possible conflict with
    c11 (same source; check the conditions)
- claim_id: c10
  attr: rated_output_current
  value:
    nominal: 150.4
    unit: unit:A
  conditions: Rated output current, 125K model
  cite:
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=31.r32
    h: b606f824522e
  review: drafted
  review_note: possible conflict with c9 (same source; check the conditions); possible conflict with c11
    (same source; check the conditions)
- claim_id: c11
  attr: rated_output_current
  value:
    nominal: 180.4
    unit: unit:A
  conditions: Rated output current, 150K model
  cite:
  - src: src:solis-solis-manual-s6-eh3p-75-150-k10-nv-yd-h-us-v1-0
    loc: tbl=31.r32
    h: b606f824522e
  review: drafted
  review_note: possible conflict with c9 (same source; check the conditions); possible conflict with c10
    (same source; check the conditions)
---
The Solis S6-EH3P(75-150)K10 US family is a series of three-phase hybrid inverters. The manual covers five models, from the 60K and 75K LV versions up to the 100K, 125K and 150K NV versions. The datasheet lists maximum apparent output power of 100 kVA, 125 kVA and 150 kVA for the 100K, 125K and 150K models. Rated output current is 120.3 A, 150.4 A and 180.4 A for those same models. The 75K model has a CEC efficiency of 95.2 percent and a maximum efficiency of 96.0 percent. The 100K and 125K models reach 97.2 percent CEC and 97.6 percent maximum efficiency. The rated frequency is 60 Hz. The 100K and 125K models have integrated AFCI 2.0 DC arc-fault protection. An AFCI-Check alarm means the arc-fault self-test failed. Restart the system first and check whether the fault comes back. A BatName-FAIL alarm means the battery brand chosen in the settings does not match the battery that is installed. Check the Battery Model setting against the battery module nameplate.

<!-- review notes
- sentence 1: support check: partial - Five models listed with LV/NV, but 'three-phase hybrid inverters' is not explicitly stated in the passage (only implied by model name).
- sentence 2: support check: partial - Apparent power for 100K/125K/150K is given as 100, 125, 150 kVA (row ordering) and currents match, but 'datasheet' mapping is by row layout; largely supported.
- sentence 5: support check: partial - AFCI and self-test failure with restart are supported, but 'check whether the fault comes back' is a paraphrase of 'confirm the fault continues'; acceptable, though the 100K/125K AFCI is supported.
-->
