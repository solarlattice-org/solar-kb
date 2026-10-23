---
id: fc:sungrow-sg350hx-548-563
type: FaultCode
name: Sungrow SG350HX 548-563
aliases:
- 548-563
- Sungrow 548-563
- PV Abnormal Alarm
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg350hx
family_name: Sungrow SG350HX-US
code: 548-563
code_key: 548-563
code_from: 548
code_to: 563
display_message: PV Abnormal Alarm
page: 90
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-sg350hx-us-user-manual
  cite:
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=32.r1
    h: 7daad1bb9722
  review: drafted
- claim_id: c2
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
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-23
- claim_id: c3
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
- claim_id: c4
  rel: detected_by
  target: method:string-current-measurement
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=32.r1
    h: 7daad1bb9722
  review: drafted
  review_note: 'support check: partial - u24 says to check the voltage and current of the inverter to
    determine the cause, but not a string current…'
- claim_id: c5
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
- claim_id: c6
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
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c7
  rel: mitigated_by
  target: mit:fuse-replacement
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=32.r1
    h: 7daad1bb9722
  review: drafted
- claim_id: c8
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=32.r1
    h: 7daad1bb9722
  review: drafted
---
