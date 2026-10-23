---
id: fc:fronius-galvo-107
type: FaultCode
name: Fronius Galvo 107
aliases:
- '107'
- Fronius 107
- AC grid outside of tolerances
category: Inverters
make: fronius
make_name: Fronius
model_family: galvo
family_name: Fronius Galvo 208-240 (1.5-1 to 3.1-1)
code: '107'
code_key: '107'
display_message: AC grid outside of tolerances
vendor_severity: Class 1
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=15.r5
    h: 5fb7a6bde764
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: sec=h18
    h: 16512b2cacc8
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-loss
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=12.r5
    h: c22ac492e44b
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=15.r5
    h: c22ac492e44b
  review: drafted
- claim_id: c3
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=12.r5
    h: c22ac492e44b
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h19
    h: 55856fbde1a5
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:auto-reset
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=12.r5
    h: c22ac492e44b
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h19
    h: 55856fbde1a5
  review: drafted
---
