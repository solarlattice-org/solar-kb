---
id: fc:fronius-galvo-448
type: FaultCode
name: Fronius Galvo 448
aliases:
- '448'
- Fronius 448
- Neutral conductor not connected
category: Inverters
make: fronius
make_name: Fronius
model_family: galvo
family_name: Fronius Galvo 208-240 (1.5-1 to 3.1-1)
code: '448'
code_key: '448'
display_message: Neutral conductor not connected
vendor_severity: Class 4
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=18.r10
    h: 2ade96d8aae1
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: sec=h21
    h: a5ea6671c1aa
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:neutral-line-abnormal
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r21
    h: 39e2bdb8cadd
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r20
    h: 39e2bdb8cadd
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=18.r10
    h: 2ade96d8aae1
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r21
    h: 39e2bdb8cadd
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h22
    h: b16852f397f6
  review: drafted
  review_note: 'support check: partial - The class 4 text is generic and does not tie 448 to class 4 or
    state its behavior.'
---
