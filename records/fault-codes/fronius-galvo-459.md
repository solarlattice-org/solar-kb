---
id: fc:fronius-galvo-459
type: FaultCode
name: Fronius Galvo 459
aliases:
- '459'
- Fronius 459
- Error receiving measuring signal for the insulation test
category: Inverters
make: fronius
make_name: Fronius
model_family: galvo
family_name: Fronius Galvo 208-240 (1.5-1 to 3.1-1)
code: '459'
code_key: '459'
display_message: Error receiving measuring signal for the insulation test
vendor_severity: Class 4
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=18.r15
    h: eebb84ba551d
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: sec=h21
    h: a5ea6671c1aa
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:measurement-signal-error
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r30
    h: 8e524a6224d5
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r28
    h: 8e524a6224d5
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=18.r15
    h: eebb84ba551d
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:insulation-monitor
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r30
    h: 8e524a6224d5
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r28
    h: 8e524a6224d5
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=18.r15
    h: eebb84ba551d
  review: drafted
- claim_id: c4
  rel: applies_to
  target: prod:fronius-galvo
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=18.r15
    h: eebb84ba551d
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: sec=h21
    h: a5ea6671c1aa
  review: drafted
---
