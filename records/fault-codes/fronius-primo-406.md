---
id: fc:fronius-primo-406
type: FaultCode
name: Fronius Primo 406
aliases:
- '406'
- Fronius 406
- Defective temperature sensor of power stage set
category: Inverters
make: fronius
make_name: Fronius
model_family: primo
family_name: Fronius Primo 208-240 (3.8-1 to 15.0-1)
code: '406'
code_key: '406'
display_message: Defective temperature sensor of power stage set
vendor_severity: Class 4
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r2
    h: 6927b12a44d6
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: sec=h20
    h: 45088a5d7149
  review: drafted
- claim_id: c2
  rel: indicates
  target: fm:temperature-sensor-fault
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r2
    h: 542f0de779d5
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r2
    h: 6927b12a44d6
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=18.r2
    h: afc6426047d3
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:temperature-sensor
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r2
    h: 542f0de779d5
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r2
    h: 6927b12a44d6
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=18.r2
    h: afc6426047d3
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r2
    h: 542f0de779d5
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15
    h: 6d4eaa7a14b0
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h22
    h: b16852f397f6
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
  review_note: 'support check: partial - 406 appears in the class 4 list but the passages never state
    it is a fault; its behavior is blank.'
---
