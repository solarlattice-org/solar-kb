---
id: fc:schneider-electric-conext-cl125-28
type: FaultCode
name: Schneider Electric CL125 028
aliases:
- '028'
- '28'
- Schneider Electric 028
- PV reverse connection is detected.
category: Inverters
make: schneider-electric
make_name: Schneider Electric
model_family: conext-cl125
family_name: Schneider Electric Conext CL125
code: '028'
code_key: '28'
display_message: PV reverse connection is detected.
page: 126
claims:
- claim_id: c1
  rel: defined_in
  target: src:schneider-conext-cl125-owners-guide-975-0793-reva
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=50.r9
    h: 9f6dbad3350b
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:schneider-conext-cl125-modbus-app-note
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=30.r6
    h: c64fd7129fc9
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:reverse-polarity
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=50.r9
    h: 9f6dbad3350b
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=30.r6
    h: c64fd7129fc9
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:dc-cable
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=50.r9
    h: 9f6dbad3350b
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=30.r6
    h: c64fd7129fc9
  review: drafted
  review_note: 'support check: partial - PV cables are mentioned in the solution, but the event affecting
    a DC cable is only implied.'
- claim_id: c5
  rel: affects
  target: comp:pv-input-terminal
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=50.r9
    h: 9f6dbad3350b
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=30.r6
    h: c64fd7129fc9
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:dc-wiring-check
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=50.r9
    h: 9f6dbad3350b
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=30.r6
    h: c64fd7129fc9
  review: drafted
---
