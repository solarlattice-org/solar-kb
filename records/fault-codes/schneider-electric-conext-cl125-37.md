---
id: fc:schneider-electric-conext-cl125-37
type: FaultCode
name: Schneider Electric CL125 037
aliases:
- '037'
- '37'
- Schneider Electric 037
- Internal ambient temperature is too high.
category: Inverters
make: schneider-electric
make_name: Schneider Electric
model_family: conext-cl125
family_name: Schneider Electric Conext CL125
code: '037'
code_key: '37'
display_message: Internal ambient temperature is too high.
page: 127
claims:
- claim_id: c1
  rel: defined_in
  target: src:schneider-conext-cl125-owners-guide-975-0793-reva
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=51.r2
    h: 873c4743d0df
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:schneider-conext-cl125-modbus-app-note
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=31.r2
    h: 90f54268bd1c
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:inverter-overtemperature
  note: Internal ambient temperature too high.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=51.r2
    h: 873c4743d0df
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=31.r2
    h: 90f54268bd1c
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:cooling-fan
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=51.r2
    h: 873c4743d0df
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=31.r2
    h: 90f54268bd1c
  review: drafted
- claim_id: c5
  rel: detected_by
  target: method:fan-function-check
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=51.r2
    h: 873c4743d0df
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=31.r2
    h: 90f54268bd1c
  review: drafted
  review_note: 'support check: partial - Checking fan functionality is a remedy step, not described as
    a detection method.'
- claim_id: c6
  rel: mitigated_by
  target: mit:fan-replacement
  note: Only if a fan is broken.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=51.r2
    h: 873c4743d0df
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=31.r2
    h: 90f54268bd1c
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:clear-ventilation-blockage
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=51.r2
    h: 873c4743d0df
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=31.r2
    h: 90f54268bd1c
  review: drafted
---
