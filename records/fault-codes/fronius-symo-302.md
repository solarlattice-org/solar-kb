---
id: fc:fronius-symo-302
type: FaultCode
name: Fronius Symo 302
aliases:
- '302'
- Fronius 302
- Overcurrent (DC)
category: Inverters
make: fronius
make_name: Fronius
model_family: symo
family_name: Fronius Symo UL (10.0-3 to 24.0-3 208-240/480)
code: '302'
code_key: '302'
display_message: Overcurrent (DC)
vendor_severity: Class 3
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-symo-ul-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r2
    h: 41ca8b5c4071
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h21
    h: beb65823f4ab
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:dc-overcurrent
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r2
    h: 41ca8b5c4071
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=16.r2
    h: 41ca8b5c4071
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=17.r2
    h: 4c69ba50a8bf
  review: drafted
---
