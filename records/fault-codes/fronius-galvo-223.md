---
id: fc:fronius-galvo-223
type: FaultCode
name: Fronius Galvo 223
aliases:
- '223'
- Fronius 223
- Undervoltage at L2-N
category: Inverters
make: fronius
make_name: Fronius
model_family: galvo
family_name: Fronius Galvo 208-240 (1.5-1 to 3.1-1)
code: '223'
code_key: '223'
display_message: Undervoltage at L2-N
vendor_severity: Class 2
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=16.r4
    h: 91f81e191c82
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: sec=h19
    h: fe0fbaee5a2c
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
  target: prod:fronius-galvo
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=16.r4
    h: 91f81e191c82
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: sec=h19
    h: fe0fbaee5a2c
  review: drafted
---
