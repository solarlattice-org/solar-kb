---
id: fc:fronius-galvo-412
type: FaultCode
name: Fronius Galvo 412
aliases:
- '412'
- Fronius 412
category: Inverters
make: fronius
make_name: Fronius
model_family: galvo
family_name: Fronius Galvo 208-240 (1.5-1 to 3.1-1)
code: '412'
code_key: '412'
vendor_severity: Class 4
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=18.r5
    h: 2a5e618acde5
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: sec=h21
    h: a5ea6671c1aa
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:configuration-error
  note: Fixed-voltage mode selected with a voltage outside the valid range; installer contact if it recurs.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r5
    h: 661291bfe665
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r5
    h: a224a51e9e92
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=18.r5
    h: 2a5e618acde5
  review: drafted
- claim_id: c3
  rel: applies_to
  target: prod:fronius-galvo
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=18.r5
    h: 2a5e618acde5
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: sec=h21
    h: a5ea6671c1aa
  review: drafted
---
