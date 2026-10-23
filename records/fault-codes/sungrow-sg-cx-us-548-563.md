---
id: fc:sungrow-sg-cx-us-548-563
type: FaultCode
name: Sungrow SG-CX-US 548-563
aliases:
- 548-563
- Sungrow 548-563
- String x output current anomaly
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg-cx-us
family_name: Sungrow SG36/60CX-US
code: 548-563
code_key: 548-563
code_from: 548
code_to: 563
display_message: String x output current anomaly
page: 98
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-36-60cx-us-iom
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=55.r2
    h: f64097f39f10
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
  cite:
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=41.r2
    h: f64097f39f10
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:abnormal-string-current
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=55.r2
    h: f64097f39f10
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=41.r2
    h: f64097f39f10
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=32.r1
    h: 7daad1bb9722
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=55.r2
    h: f64097f39f10
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=41.r2
    h: f64097f39f10
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=32.r1
    h: 7daad1bb9722
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:string-current-measurement
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=32.r1
    h: 7daad1bb9722
  review: drafted
  review_note: 'support check: partial - u24 says to check the voltage and current of the inverter to
    determine the cause, but not a string current…'
- claim_id: c6
  rel: mitigated_by
  target: mit:avoid-partial-shading
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=55.r2
    h: f64097f39f10
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=41.r2
    h: f64097f39f10
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=32.r1
    h: 7daad1bb9722
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:manual-cleaning
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=55.r2
    h: f64097f39f10
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=41.r2
    h: f64097f39f10
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=32.r1
    h: 7daad1bb9722
  review: drafted
- claim_id: c8
  rel: mitigated_by
  target: mit:fuse-replacement
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=32.r1
    h: 7daad1bb9722
  review: drafted
- claim_id: c9
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=32.r1
    h: 7daad1bb9722
  review: drafted
---
