---
id: fc:schneider-electric-conext-cl125-70
type: FaultCode
name: Schneider Electric CL125 070
aliases:
- '070'
- '70'
- Schneider Electric 070
- Fan event
category: Inverters
make: schneider-electric
make_name: Schneider Electric
model_family: conext-cl125
family_name: Schneider Electric Conext CL125
code: '070'
code_key: '70'
display_message: Fan event
page: 129
claims:
- claim_id: c1
  rel: defined_in
  target: src:schneider-conext-cl125-owners-guide-975-0793-reva
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=53.r6
    h: e4acc53fe128
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:schneider-conext-cl125-modbus-app-note
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=33.r5
    h: a6cbc16d5af2
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:fan-fault-alarm
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=53.r6
    h: e4acc53fe128
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=33.r5
    h: a6cbc16d5af2
  review: drafted
- claim_id: c4
  rel: indicates
  target: fm:fan-failure
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=53.r6
    h: e4acc53fe128
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=33.r5
    h: a6cbc16d5af2
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:cooling-fan
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=53.r6
    h: e4acc53fe128
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=33.r5
    h: a6cbc16d5af2
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:fan-replacement
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=53.r6
    h: e4acc53fe128
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=33.r5
    h: a6cbc16d5af2
  review: drafted
- claim_id: c7
  rel: has_event_class
  target: ec:fault
  note: Fan must be replaced, so intervention is needed.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=53.r6
    h: e4acc53fe128
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=33.r5
    h: a6cbc16d5af2
  review: drafted
  review_note: 'support check: partial - Intervention needed (stop inverter, replace fan) is stated, but
    fault classification is not explicit; it is more service-required.'
- claim_id: c8
  rel: has_recovery
  target: ec:service-required
  note: Fan replacement; the app's fan status shows which fan is affected.
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=53.r6
    h: e4acc53fe128
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=33.r5
    h: a6cbc16d5af2
  review: drafted
- claim_id: c9
  rel: applies_to
  target: prod:schneider-electric-conext-cl125
  cite:
  - src: src:schneider-conext-cl125-owners-guide-975-0793-reva
    loc: tbl=53.r6
    h: e4acc53fe128
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=33.r5
    h: a6cbc16d5af2
  review: drafted
---
