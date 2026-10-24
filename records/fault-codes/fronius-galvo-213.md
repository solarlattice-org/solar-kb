---
id: fc:fronius-galvo-213
type: FaultCode
name: Fronius Galvo 213
aliases:
- '213'
- Fronius 213
- Undervoltage at L1-N
category: Inverters
make: fronius
make_name: Fronius
model_family: galvo
family_name: Fronius Galvo 208-240 (1.5-1 to 3.1-1)
code: '213'
code_key: '213'
display_message: Undervoltage at L1-N
vendor_severity: Class 2
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=16.r2
    h: 95387f3d8346
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: sec=h19
    h: fe0fbaee5a2c
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-undervoltage
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=13.r2
    h: 92d8e2c0becf
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=16.r2
    h: 95387f3d8346
  review: drafted
- claim_id: c3
  rel: applies_to
  target: prod:fronius-galvo
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=16.r2
    h: 95387f3d8346
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: sec=h19
    h: fe0fbaee5a2c
  review: drafted
---
