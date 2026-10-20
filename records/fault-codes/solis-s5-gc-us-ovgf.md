---
id: fc:solis-s5-gc-us-ovgf
type: FaultCode
name: Solis S5-GC OV-G-F
aliases:
- OV-G-F
- ovgf
- Solis OV-G-F
- Over Grid Frequency
category: Inverters
make: solis
make_name: Solis
model_family: s5-gc-us
family_name: Solis S5-GC(75-125)K-US
code: OV-G-F
code_key: ovgf
display_message: Over Grid Frequency
page: 70
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=14.r1
    h: 5f4341ada0d6
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-overfrequency
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=14.r1
    h: 5f4341ada0d6
  review: drafted
- claim_id: c3
  rel: detected_by
  target: method:grid-frequency-measurement
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=14.r1
    h: 5f4341ada0d6
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-parameter-change
  note: Upper frequency limit change requires utility permission.
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=14.r1
    h: 5f4341ada0d6
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-20
- claim_id: c5
  rel: mitigated_by
  target: mit:grid-settings-check
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=14.r1
    h: 5f4341ada0d6
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
