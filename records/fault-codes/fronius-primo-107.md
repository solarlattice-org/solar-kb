---
id: fc:fronius-primo-107
type: FaultCode
name: Fronius Primo 107
aliases:
- '107'
- Fronius 107
- No AC grid detected
category: Inverters
make: fronius
make_name: Fronius
model_family: primo
family_name: Fronius Primo 208-240 (3.8-1 to 15.0-1)
code: '107'
code_key: '107'
display_message: No AC grid detected
vendor_severity: Class 1
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=15.r5
    h: c22ac492e44b
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: sec=h18
    h: 55856fbde1a5
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-loss
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=12.r5
    h: c22ac492e44b
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=15.r5
    h: c22ac492e44b
  review: drafted
- claim_id: c3
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=12.r5
    h: c22ac492e44b
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h19
    h: 55856fbde1a5
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c4
  rel: has_recovery
  target: ec:auto-reset
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=12.r5
    h: c22ac492e44b
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h19
    h: 55856fbde1a5
  review: drafted
---
