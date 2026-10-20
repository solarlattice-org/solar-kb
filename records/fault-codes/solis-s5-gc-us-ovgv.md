---
id: fc:solis-s5-gc-us-ovgv
type: FaultCode
name: Solis S5-GC OV-G-V
aliases:
- OV-G-V
- ovgv
- Solis OV-G-V
- Over Grid Voltage
category: Inverters
make: solis
make_name: Solis
model_family: s5-gc-us
family_name: Solis S5-GC(75-125)K-US
code: OV-G-V
code_key: ovgv
display_message: Over Grid Voltage
page: 69
claims:
- claim_id: c1
  rel: defined_in
  target: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=13.r3
    h: 52c3fd63f040
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-overvoltage
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=13.r3
    h: 52c3fd63f040
  review: drafted
- claim_id: c3
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=13.r3
    h: 52c3fd63f040
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:ac-cable
  note: When voltage is high only at full power, undersized interconnect cabling is suspected.
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=13.r3
    h: 52c3fd63f040
  review: drafted
  review_note: 'support check: partial - Passage says undersized cables between inverter and interconnect
    cause high AC at full power, but doesn''t explicitly say it affects…'
- claim_id: c5
  rel: mitigated_by
  target: mit:inverter-parameter-change
  note: Upper voltage limit change requires utility permission.
  cite:
  - src: src:solis-solis-manual-s5-75-100-k-us-v2-3-20230623
    loc: tbl=13.r3
    h: 52c3fd63f040
  review: drafted
---
