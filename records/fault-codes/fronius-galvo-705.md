---
id: fc:fronius-galvo-705
type: FaultCode
name: Fronius Galvo 705
aliases:
- '705'
- Fronius 705
category: Inverters
make: fronius
make_name: Fronius
model_family: galvo
family_name: Fronius Galvo 208-240 (1.5-1 to 3.1-1)
code: '705'
code_key: '705'
vendor_severity: Class 7
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=20.r1
    h: b608a2268051
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: sec=h23
    h: 8efd8641166b
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:configuration-error
  note: Inverter number conflict, such as a duplicate number.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r2
    h: b608a2268051
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=19.r1
    h: b608a2268051
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=20.r1
    h: b608a2268051
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:inverter-parameter-change
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r2
    h: b608a2268051
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=19.r1
    h: b608a2268051
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=20.r1
    h: b608a2268051
  review: drafted
---
