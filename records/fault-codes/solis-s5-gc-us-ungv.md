---
id: fc:solis-s5-gc-us-ungv
type: FaultCode
name: Solis S5-GC UN-G-V
aliases:
- UN-G-V
- ungv
- Solis UN-G-V
- Under Grid Voltage
category: Inverters
make: solis
make_name: Solis
model_family: s5-gc-us
family_name: Solis S5-GC(75-125)K-US
code: UN-G-V
code_key: ungv
display_message: Under Grid Voltage
page: 69
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=13.r4
    h: cab3a7061bcd
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-undervoltage
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=13.r4
    h: cab3a7061bcd
  review: drafted
- claim_id: c3
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=13.r4
    h: cab3a7061bcd
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:inverter-parameter-change
  note: Lower limit change requires utility permission.
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=13.r4
    h: cab3a7061bcd
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:grid-settings-check
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=13.r4
    h: cab3a7061bcd
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-20
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-replacement
  note: Last step if a faulty measurement circuit is suspected.
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=13.r4
    h: cab3a7061bcd
  review: verified
  verified_by: review-workflow
  verified_at: *id001
---
