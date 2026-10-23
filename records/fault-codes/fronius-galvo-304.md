---
id: fc:fronius-galvo-304
type: FaultCode
name: Fronius Galvo 304
aliases:
- '304'
- Fronius 304
- Interior temperature too high
category: Inverters
make: fronius
make_name: Fronius
model_family: galvo
family_name: Fronius Galvo 208-240 (1.5-1 to 3.1-1)
code: '304'
code_key: '304'
display_message: Interior temperature too high
vendor_severity: Class 3
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=17.r7
    h: 6efd53cd6ffd
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: sec=h20
    h: 5571d6749f75
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:inverter-overtemperature
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r4
    h: f399f10a0686
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=17.r7
    h: 6efd53cd6ffd
  review: drafted
---
