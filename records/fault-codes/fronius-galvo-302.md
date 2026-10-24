---
id: fc:fronius-galvo-302
type: FaultCode
name: Fronius Galvo 302
aliases:
- '302'
- Fronius 302
- Over-current (DC)
category: Inverters
make: fronius
make_name: Fronius
model_family: galvo
family_name: Fronius Galvo 208-240 (1.5-1 to 3.1-1)
code: '302'
code_key: '302'
display_message: Over-current (DC)
vendor_severity: Class 3
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=17.r2
    h: 4c69ba50a8bf
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: sec=h20
    h: 5571d6749f75
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:dc-overcurrent
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r2
    h: 41ca8b5c4071
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=16.r2
    h: 41ca8b5c4071
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=17.r2
    h: 4c69ba50a8bf
  review: drafted
- claim_id: c3
  rel: applies_to
  target: prod:fronius-galvo
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=17.r2
    h: 4c69ba50a8bf
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: sec=h20
    h: 5571d6749f75
  review: drafted
---
