---
id: fc:fronius-symo-103
type: FaultCode
name: Fronius Symo 103
aliases:
- '103'
- Fronius 103
- AC voltage too low
category: Inverters
make: fronius
make_name: Fronius
model_family: symo
family_name: Fronius Symo UL (10.0-3 to 24.0-3 208-240/480)
code: '103'
code_key: '103'
display_message: AC voltage too low
vendor_severity: Class 1
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-symo-ul-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=12.r2
    h: 119cf93242d1
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h19
    h: 55856fbde1a5
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-undervoltage
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=12.r2
    h: 119cf93242d1
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=15.r2
    h: 119cf93242d1
  review: drafted
- claim_id: c3
  rel: has_recovery
  target: ec:auto-reset
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=12.r2
    h: 119cf93242d1
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h19
    h: 55856fbde1a5
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
---
