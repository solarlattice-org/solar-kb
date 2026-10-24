---
id: fc:fronius-galvo-103
type: FaultCode
name: Fronius Galvo 103
aliases:
- '103'
- Fronius 103
- AC voltage too low
category: Inverters
make: fronius
make_name: Fronius
model_family: galvo
family_name: Fronius Galvo 208-240 (1.5-1 to 3.1-1)
code: '103'
code_key: '103'
display_message: AC voltage too low
vendor_severity: Class 1
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=15.r2
    h: 119cf93242d1
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: sec=h18
    h: 16512b2cacc8
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-undervoltage
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=12.r2
    h: 119cf93242d1
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=15.r2
    h: 119cf93242d1
  review: drafted
- claim_id: c3
  rel: has_recovery
  target: ec:auto-reset
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=12.r2
    h: 119cf93242d1
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h19
    h: 55856fbde1a5
  review: drafted
- claim_id: c4
  rel: applies_to
  target: prod:fronius-galvo
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=15.r2
    h: 119cf93242d1
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: sec=h18
    h: 16512b2cacc8
  review: drafted
---
