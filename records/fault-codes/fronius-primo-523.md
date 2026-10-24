---
id: fc:fronius-primo-523
type: FaultCode
name: Fronius Primo 523
aliases:
- '523'
- Fronius 523
- DC low String 2
category: Inverters
make: fronius
make_name: Fronius
model_family: primo
family_name: Fronius Primo 208-240 (3.8-1 to 15.0-1)
code: '523'
code_key: '523'
display_message: DC low String 2
vendor_severity: Class 5
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=18.r7
    h: 3d2e053b53ef
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: sec=h21
    h: a6a4378aca92
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:dc-undervoltage
  note: Low DC on string 2 input.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r10
    h: 3d2e053b53ef
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=18.r7
    h: 3d2e053b53ef
  review: drafted
- claim_id: c3
  rel: has_production_effect
  target: ec:no-production-effect
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r10
    h: 3d2e053b53ef
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h23
    h: c4a64ba354f6
  review: drafted
  review_note: 'support check: partial - The class 5 text says codes generally do not impair feed-in,
    but 523 itself is not stated to be class 5.'
- claim_id: c4
  rel: applies_to
  target: prod:fronius-primo
  cite:
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=18.r7
    h: 3d2e053b53ef
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: sec=h21
    h: a6a4378aca92
  review: drafted
---
