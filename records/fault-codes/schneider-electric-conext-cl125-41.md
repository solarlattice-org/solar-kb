---
id: fc:schneider-electric-conext-cl125-41
type: FaultCode
name: Schneider Electric CL125 041
aliases:
- '041'
- '41'
- Schneider Electric 041
- Current leakage sampling channel event
category: Inverters
make: schneider-electric
make_name: Schneider Electric
model_family: conext-cl125
family_name: Schneider Electric Conext CL125
code: '041'
code_key: '41'
display_message: Current leakage sampling channel event
page: 127
claims:
- claim_id: c1
  rel: defined_in
  target: src:schneider-conext-cl125-owners-guide-975-0793-reva
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=51.r6
    h: 0a284e7632aa
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:schneider-conext-cl125-modbus-app-note
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=31.r6
    h: dc826c7a1ef3
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:internal-device-fault
  note: Fault in the leakage current sampling channel.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=51.r6
    h: 0a284e7632aa
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=31.r6
    h: dc826c7a1ef3
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:ground-fault-detector
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=51.r6
    h: 0a284e7632aa
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=31.r6
    h: dc826c7a1ef3
  review: drafted
  review_note: 'support check: partial - Leakage current sampling relates to ground fault detection, but
    the passages do not name a ground fault detector.'
- claim_id: c5
  rel: has_production_effect
  target: ec:trip
  note: Implied by the instruction to wait for the inverter to recover.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=51.r6
    h: 0a284e7632aa
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=31.r6
    h: dc826c7a1ef3
  review: drafted
  review_note: 'support check: partial - Trip is only implied by wait to recover; not explicit.'
- claim_id: c6
  rel: has_recovery
  target: ec:auto-reset
  note: Contact technical support if the event persists.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=51.r6
    h: 0a284e7632aa
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=31.r6
    h: dc826c7a1ef3
  review: drafted
---
