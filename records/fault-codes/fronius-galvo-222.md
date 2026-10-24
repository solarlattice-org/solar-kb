---
id: fc:fronius-galvo-222
type: FaultCode
name: Fronius Galvo 222
aliases:
- '222'
- Fronius 222
- Overvoltage at L2-N
category: Inverters
make: fronius
make_name: Fronius
model_family: galvo
family_name: Fronius Galvo 208-240 (1.5-1 to 3.1-1)
code: '222'
code_key: '222'
display_message: Overvoltage at L2-N
vendor_severity: Class 2
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=16.r3
    h: 500197800a71
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: sec=h19
    h: fe0fbaee5a2c
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-overvoltage
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=13.r3
    h: 8f72eae1b7d0
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=16.r3
    h: 500197800a71
  review: drafted
- claim_id: c3
  rel: applies_to
  target: prod:fronius-galvo
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=16.r3
    h: 500197800a71
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: sec=h19
    h: fe0fbaee5a2c
  review: drafted
---
