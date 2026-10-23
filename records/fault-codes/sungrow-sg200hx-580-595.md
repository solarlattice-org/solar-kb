---
id: fc:sungrow-sg200hx-580-595
type: FaultCode
name: Sungrow SG200HX 580-595
aliases:
- 580-595
- Sungrow 580-595
- PV Abnormal Alarm
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg200hx
family_name: Sungrow SG200HX-US
code: 580-595
code_key: 580-595
code_from: 580
code_to: 595
display_message: PV Abnormal Alarm
page: 91
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-sg200hx-us-user-manual
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=32.r1
    h: 7daad1bb9722
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:pv-input-abnormal
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=32.r1
    h: 7daad1bb9722
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:pv-array
  note: Codes 580 to 595 map to strings 17 to 32.
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=32.r1
    h: 7daad1bb9722
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:dc-voltage-measurement
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=32.r1
    h: 7daad1bb9722
  review: drafted
  review_note: 'support check: partial - Told to check voltage and current for abnormality, not explicitly
    DC voltage measurement as detection.'
- claim_id: c5
  rel: detected_by
  target: method:pv-current-measurement
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=32.r1
    h: 7daad1bb9722
  review: drafted
  review_note: 'support check: partial - Told to check voltage and current, not explicitly PV input current
    measurement.'
- claim_id: c6
  rel: mitigated_by
  target: mit:avoid-partial-shading
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=32.r1
    h: 7daad1bb9722
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:manual-cleaning
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=32.r1
    h: 7daad1bb9722
  review: drafted
  review_note: 'support check: partial - Ensure module cleanness after removing shelter; manual cleaning
    not explicitly stated.'
- claim_id: c8
  rel: mitigated_by
  target: mit:dc-wiring-check
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=32.r1
    h: 7daad1bb9722
  review: drafted
- claim_id: c9
  rel: mitigated_by
  target: mit:fuse-replacement
  note: Only where a fuse sits between string and inverter input.
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=32.r1
    h: 7daad1bb9722
  review: drafted
- claim_id: c10
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=32.r1
    h: 7daad1bb9722
  review: drafted
---
