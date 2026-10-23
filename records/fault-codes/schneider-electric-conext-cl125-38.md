---
id: fc:schneider-electric-conext-cl125-38
type: FaultCode
name: Schneider Electric CL125 038
aliases:
- '038'
- '38'
- Schneider Electric 038
category: Inverters
make: schneider-electric
make_name: Schneider Electric
model_family: conext-cl125
family_name: Schneider Electric Conext CL125
code: '038'
code_key: '38'
page: 127
claims:
- claim_id: c1
  rel: defined_in
  target: src:schneider-conext-cl125-owners-guide-975-0793-reva
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=51.r3
    h: 5337b94caee8
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:schneider-conext-cl125-modbus-app-note
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=31.r3
    h: 358a9c18d619
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:relay-failure
  note: Contacts welded or open.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=51.r3
    h: 5337b94caee8
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=31.r3
    h: 358a9c18d619
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:grid-relay
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=51.r3
    h: 5337b94caee8
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=31.r3
    h: 358a9c18d619
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: Contact technical support if the event persists.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=51.r3
    h: 5337b94caee8
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=31.r3
    h: 358a9c18d619
  review: drafted
---
