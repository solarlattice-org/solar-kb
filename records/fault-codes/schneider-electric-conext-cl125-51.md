---
id: fc:schneider-electric-conext-cl125-51
type: FaultCode
name: Schneider Electric CL125 051
aliases:
- '051'
- '51'
- Schneider Electric 051
- Hardware over voltage or over current protection
category: Inverters
make: schneider-electric
make_name: Schneider Electric
model_family: conext-cl125
family_name: Schneider Electric Conext CL125
code: '051'
code_key: '51'
display_message: Hardware over voltage or over current protection
page: 27
claims:
- claim_id: c1
  rel: defined_in
  target: src:schneider-conext-cl125-modbus-app-note
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=32.r5
    h: 1f55ce302711
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:internal-overcurrent-overvoltage
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=32.r5
    h: 1f55ce302711
  review: drafted
  review_note: 'support check: partial - Hardware over voltage or over current protection is stated, but
    ''internal'' is not.'
- claim_id: c3
  rel: applies_to
  target: prod:schneider-electric-conext-cl125
  cite:
  - src: src:schneider-conext-cl125-modbus-app-note
    loc: tbl=32.r5
    h: 1f55ce302711
  review: drafted
---
