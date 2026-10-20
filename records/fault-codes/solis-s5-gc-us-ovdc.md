---
id: fc:solis-s5-gc-us-ovdc
type: FaultCode
name: Solis S5-GC OV-DC
aliases:
- OV-DC
- ovdc
- Solis OV-DC
- DC voltage is too high
category: Inverters
make: solis
make_name: Solis
model_family: s5-gc-us
family_name: Solis S5-GC(75-125)K-US
code: OV-DC
code_key: ovdc
display_message: DC voltage is too high
page: 70
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=14.r3
    h: 4bc70d0f58e4
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:dc-overvoltage
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=14.r3
    h: 4bc70d0f58e4
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-20
- claim_id: c3
  rel: detected_by
  target: method:dc-voltage-measurement
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=14.r3
    h: 4bc70d0f58e4
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=14.r3
    h: 4bc70d0f58e4
  review: verified
  verified_by: review-workflow
  verified_at: *id001
  review_note: 'support check: partial - High DC voltage with string configuration check implies PV array,
    but not explicitly stated as affected component.'
- claim_id: c5
  rel: mitigated_by
  target: mit:string-configuration-correction
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=14.r3
    h: 4bc70d0f58e4
  review: drafted
---
