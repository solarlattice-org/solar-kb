---
id: fc:schneider-electric-conext-cl125-10
type: FaultCode
name: Schneider Electric CL125 010
aliases:
- '010'
- '10'
- Schneider Electric 010
- Islanding
category: Inverters
make: schneider-electric
make_name: Schneider Electric
model_family: conext-cl125
family_name: Schneider Electric Conext CL125
code: '010'
code_key: '10'
display_message: Islanding
page: 124
claims:
- claim_id: c1
  rel: defined_in
  target: src:schneider-conext-cl125-owners-guide-975-0793-reva
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=48.r4
    h: e0dbdc26ba0f
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:schneider-conext-cl125-modbus-app-note
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=28.r4
    h: 0917644a7127
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:islanding-detected
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=48.r4
    h: e0dbdc26ba0f
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=28.r4
    h: 0917644a7127
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:ac-cable
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=48.r4
    h: e0dbdc26ba0f
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=28.r4
    h: 0917644a7127
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=48.r4
    h: e0dbdc26ba0f
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=28.r4
    h: 0917644a7127
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
  review_note: 'support check: partial - Measuring grid voltage is a troubleshooting step, not stated
    as the detection method.'
- claim_id: c6
  rel: mitigated_by
  target: mit:ac-connection-check
  note: Covers breaker, disconnect and cabling; escalate to technical support if unresolved.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=48.r4
    h: e0dbdc26ba0f
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=28.r4
    h: 0917644a7127
  review: drafted
---
