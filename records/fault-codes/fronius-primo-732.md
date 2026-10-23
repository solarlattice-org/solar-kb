---
id: fc:fronius-primo-732
type: FaultCode
name: Fronius Primo 732
aliases:
- '732'
- Fronius 732
- Overcurrent at USB thumb drive
category: Inverters
make: fronius
make_name: Fronius
model_family: primo
family_name: Fronius Primo 208-240 (3.8-1 to 15.0-1)
code: '732'
code_key: '732'
display_message: Overcurrent at USB thumb drive
vendor_severity: Class 7
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=19.r4
    h: 00d0a42ac554
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: sec=h22
    h: 8efd8641166b
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:usb-overcurrent
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r7
    h: b0a1a955fa5c
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=19.r4
    h: 00d0a42ac554
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=20.r4
    h: 00d0a42ac554
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:usb-flash-drive
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r7
    h: b0a1a955fa5c
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=19.r4
    h: 00d0a42ac554
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=20.r4
    h: 00d0a42ac554
  review: drafted
---
