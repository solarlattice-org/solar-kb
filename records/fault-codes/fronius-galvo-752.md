---
id: fc:fronius-galvo-752
type: FaultCode
name: Fronius Galvo 752
aliases:
- '752'
- Fronius 752
- Real Time Clock module communication error
category: Inverters
make: fronius
make_name: Fronius
model_family: galvo
family_name: Fronius Galvo 208-240 (1.5-1 to 3.1-1)
code: '752'
code_key: '752'
display_message: Real Time Clock module communication error
vendor_severity: Class 7
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=20.r13
    h: 2ee634d10a9c
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: sec=h23
    h: 8efd8641166b
  review: drafted
- claim_id: c2
  rel: affects
  target: comp:real-time-clock
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r20
    h: 2ee634d10a9c
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=19.r13
    h: 2ee634d10a9c
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=20.r13
    h: 2ee634d10a9c
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:internal-communication-failure
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r20
    h: 2ee634d10a9c
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=19.r13
    h: 2ee634d10a9c
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=20.r13
    h: 2ee634d10a9c
  review: drafted
  review_note: 'support check: partial - A communication error with the RTC module is stated, but ''internal
    communication failure'' is an inference.'
---
