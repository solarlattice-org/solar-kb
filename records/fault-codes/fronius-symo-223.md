---
id: fc:fronius-symo-223
type: FaultCode
name: Fronius Symo 223
aliases:
- '223'
- Fronius 223
- Undervoltage on L2
category: Inverters
make: fronius
make_name: Fronius
model_family: symo
family_name: Fronius Symo UL (10.0-3 to 24.0-3 208-240/480)
code: '223'
code_key: '223'
display_message: Undervoltage on L2
vendor_severity: Class 2
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-symo-ul-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=13.r4
    h: 1f9ef846cdd4
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h20
    h: b46d8cafebc3
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-undervoltage
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=13.r4
    h: 1f9ef846cdd4
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=16.r4
    h: 91f81e191c82
  review: drafted
- claim_id: c3
  rel: applies_to
  target: prod:fronius-symo
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=13.r4
    h: 1f9ef846cdd4
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h20
    h: b46d8cafebc3
  review: drafted
---
