---
id: fc:fronius-symo-459
type: FaultCode
name: Fronius Symo 459
aliases:
- '459'
- Fronius 459
- Error during measuring signal detection for insulation test
category: Inverters
make: fronius
make_name: Fronius
model_family: symo
family_name: Fronius Symo UL (10.0-3 to 24.0-3 208-240/480)
code: '459'
code_key: '459'
display_message: Error during measuring signal detection for insulation test
vendor_severity: Class 4
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-symo-ul-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r30
    h: 8e524a6224d5
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h22
    h: b16852f397f6
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:measurement-signal-error
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r30
    h: 8e524a6224d5
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r28
    h: 8e524a6224d5
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=18.r15
    h: eebb84ba551d
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c3
  rel: affects
  target: comp:insulation-monitor
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r30
    h: 8e524a6224d5
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r28
    h: 8e524a6224d5
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=18.r15
    h: eebb84ba551d
  review: drafted
- claim_id: c4
  rel: applies_to
  target: prod:fronius-symo
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r30
    h: 8e524a6224d5
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h22
    h: b16852f397f6
  review: drafted
---
