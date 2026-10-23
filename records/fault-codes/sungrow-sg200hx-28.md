---
id: fc:sungrow-sg200hx-28
type: FaultCode
name: Sungrow SG200HX 28
aliases:
- '28'
- Sungrow 28
- PV Reserve Connection Fault
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg200hx
family_name: Sungrow SG200HX-US
code: '28'
code_key: '28'
display_message: PV Reserve Connection Fault
page: 90
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-sg200hx-us-user-manual
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=31.r2
    h: bd3e9e47952a
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:reverse-polarity
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=31.r2
    h: bd3e9e47952a
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c3
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=31.r2
    h: bd3e9e47952a
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:polarity-measurement
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=31.r2
    h: bd3e9e47952a
  review: drafted
  review_note: 'support check: partial - Checking string reverse polarity stated, but no explicit measurement
    method.'
- claim_id: c5
  rel: mitigated_by
  target: mit:polarity-correction
  note: Correct only with DC switch open and string current below 0.5 A.
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=31.r2
    h: bd3e9e47952a
  review: drafted
- claim_id: c6
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=31.r2
    h: bd3e9e47952a
  review: drafted
---
