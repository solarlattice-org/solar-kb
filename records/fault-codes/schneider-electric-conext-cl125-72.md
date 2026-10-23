---
id: fc:schneider-electric-conext-cl125-72
type: FaultCode
name: Schneider Electric CL125 072
aliases:
- '072'
- '72'
- Schneider Electric 072
- DC side SPD event
category: Inverters
make: schneider-electric
make_name: Schneider Electric
model_family: conext-cl125
family_name: Schneider Electric Conext CL125
code: '072'
code_key: '72'
display_message: DC side SPD event
page: 129
claims:
- claim_id: c1
  rel: defined_in
  target: src:schneider-conext-cl125-owners-guide-975-0793-reva
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=53.r8
    h: f850dfc0b1fa
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:schneider-conext-cl125-modbus-app-note
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=33.r7
    h: 3114d6eef976
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:spd-alarm
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=33.r7
    h: 3114d6eef976
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=53.r8
    h: f850dfc0b1fa
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c4
  rel: affects
  target: comp:surge-protection-device
  note: DC-side surge protector.
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=33.r7
    h: 3114d6eef976
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=53.r8
    h: f850dfc0b1fa
  review: drafted
- claim_id: c5
  rel: indicates
  target: fm:surge-protector-exhausted
  note: The guide's merged cell points to replacing an expended DC SPD.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=53.r8
    h: f850dfc0b1fa
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=53
    h: 11ab53e1c071
  review: drafted
  review_note: 'support check: partial - The merged table cell hints at replacing an expended DC SPD,
    but the row itself doesn''t state exhaustion for 072.'
- claim_id: c6
  rel: mitigated_by
  target: mit:spd-replacement
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=53.r8
    h: f850dfc0b1fa
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=53
    h: 11ab53e1c071
  review: drafted
  review_note: 'support check: partial - Replacement of expended DC SPD is implied by the split table
    cell, but not cleanly stated for 072.'
- claim_id: c7
  rel: has_recovery
  target: ec:service-required
  note: The expended DC SPD has to be replaced.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=53.r8
    h: f850dfc0b1fa
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=53
    h: 11ab53e1c071
  review: drafted
  review_note: 'support check: partial - Replacement of an expended SPD is implied by the split cell but
    service-required is not explicit.'
---
