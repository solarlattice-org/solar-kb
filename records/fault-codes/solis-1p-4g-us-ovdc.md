---
id: fc:solis-1p-4g-us-ovdc
type: FaultCode
name: Solis 1P-4G-US OV-DC
aliases:
- OV-DC
- ovdc
- Solis OV-DC
- DC voltage is too high
category: Inverters
make: solis
make_name: Solis
model_family: 1p-4g-us
family_name: Solis-1P(3.6-10)K-4G-US
code: OV-DC
code_key: ovdc
display_message: DC voltage is too high
page: 61
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
  cite:
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=13.r5
    h: 0e2522f833ae
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:solis-solis-manual-3-6-5-k-4g-plus-lw-usa-03212023
  cite:
  - src: src:solis-solis-manual-3-6-5-k-4g-plus-lw-usa-03212023
    loc: tbl=12.r5
    h: 0e2522f833ae
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
- claim_id: c8
  rel: applies_to
  target: prod:solis-1p-4g-us
  cite:
  - src: src:solis-solis-manual-solis-1p-6-10-k-4g-us-plus-v2-1-20250804
    loc: tbl=13.r5
    h: 0e2522f833ae
  - src: src:solis-solis-manual-3-6-5-k-4g-plus-lw-usa-03212023
    loc: tbl=12.r5
    h: 0e2522f833ae
  review: drafted
---
