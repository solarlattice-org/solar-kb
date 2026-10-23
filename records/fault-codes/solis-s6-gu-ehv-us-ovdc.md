---
id: fc:solis-s6-gu-ehv-us-ovdc
type: FaultCode
name: Solis S6-GU OV-DC
aliases:
- OV-DC
- ovdc
- Solis OV-DC
- DC voltage is too high
category: Inverters
make: solis
make_name: Solis
model_family: s6-gu-ehv-us
family_name: Solis S6-GU(250-350)K-EHV-US
code: OV-DC
code_key: ovdc
display_message: DC voltage is too high
page: 46
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
  cite:
  - src: src:solis-solis-manual-s6-gu-250-350-k-ehv-usa-pe-mn-0001-r00
    loc: tbl=11.r3
    h: f0883f565fb0
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:dc-overvoltage
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=14.r3
    h: 4bc70d0f58e4
  review: drafted
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
  review: drafted
  review_note: 'support check: partial - Passage only says check string configuration if DC voltage is
    high; PV array is implied but not named.'
- claim_id: c5
  rel: mitigated_by
  target: mit:string-configuration-correction
  note: When measured DC voltage is actually high.
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=14.r3
    h: 4bc70d0f58e4
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-replacement
  note: When the displayed reading is wrong, suggesting a bad measurement circuit.
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=14.r3
    h: 4bc70d0f58e4
  review: drafted
---
