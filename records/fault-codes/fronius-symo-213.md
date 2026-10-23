---
id: fc:fronius-symo-213
type: FaultCode
name: Fronius Symo 213
aliases:
- '213'
- Fronius 213
- Undervoltage on L1
category: Inverters
make: fronius
make_name: Fronius
model_family: symo
family_name: Fronius Symo UL (10.0-3 to 24.0-3 208-240/480)
code: '213'
code_key: '213'
display_message: Undervoltage on L1
vendor_severity: Class 2
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-symo-ul-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=13.r2
    h: 92d8e2c0becf
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h20
    h: b46d8cafebc3
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-undervoltage
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=13.r2
    h: 92d8e2c0becf
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=16.r2
    h: 95387f3d8346
  review: drafted
---
