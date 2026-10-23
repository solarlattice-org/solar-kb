---
id: fc:solis-s6-gc-us-ovdc
type: FaultCode
name: Solis S6-GC OV-DC
aliases:
- OV-DC
- ovdc
- Solis OV-DC
- DC voltage is too high
category: Inverters
make: solis
make_name: Solis
model_family: s6-gc-us
family_name: Solis S6-GC(25-60)K-US
code: OV-DC
code_key: ovdc
display_message: DC voltage is too high
page: 71
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s6-gc-25-60-k-us-v1-1-20251013
  cite:
  - src: src:solis-solis-manual-s6-gc-25-60-k-us-v1-1-20251013
    loc: tbl=13.r3
    h: 4bc70d0f58e4
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
  cite:
  - src: src:solis-solis-s6-gc30k-lv-us-manual-v1-2
    loc: tbl=12.r3
    h: 4bc70d0f58e4
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:dc-overvoltage
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=14.r3
    h: 4bc70d0f58e4
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:dc-voltage-measurement
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=14.r3
    h: 4bc70d0f58e4
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=14.r3
    h: 4bc70d0f58e4
  review: drafted
  review_note: 'support check: partial - Passage only says check string configuration if DC voltage is
    high; PV array is implied but not named.'
- claim_id: c6
  rel: mitigated_by
  target: mit:string-configuration-correction
  note: When measured DC voltage is actually high.
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=14.r3
    h: 4bc70d0f58e4
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:inverter-replacement
  note: When the displayed reading is wrong, suggesting a bad measurement circuit.
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=14.r3
    h: 4bc70d0f58e4
  review: drafted
---
