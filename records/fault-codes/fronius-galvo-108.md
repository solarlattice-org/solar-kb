---
id: fc:fronius-galvo-108
type: FaultCode
name: Fronius Galvo 108
aliases:
- '108'
- Fronius 108
- Stand alone operation detected
category: Inverters
make: fronius
make_name: Fronius
model_family: galvo
family_name: Fronius Galvo 208-240 (1.5-1 to 3.1-1)
code: '108'
code_key: '108'
display_message: Stand alone operation detected
vendor_severity: Class 1
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=15.r6
    h: 6acc4c9c9782
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: sec=h18
    h: 16512b2cacc8
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:islanding-detected
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=12.r6
    h: cda577ea7782
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=15.r6
    h: cda577ea7782
  review: drafted
- claim_id: c3
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=12.r6
    h: cda577ea7782
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h19
    h: 55856fbde1a5
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:auto-reset
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=12.r6
    h: cda577ea7782
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h19
    h: 55856fbde1a5
  review: drafted
- claim_id: c5
  rel: applies_to
  target: prod:fronius-galvo
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=15.r6
    h: 6acc4c9c9782
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: sec=h18
    h: 16512b2cacc8
  review: drafted
---
