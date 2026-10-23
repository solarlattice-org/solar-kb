---
id: fc:fronius-primo-459
type: FaultCode
name: Fronius Primo 459
aliases:
- '459'
- Fronius 459
- Error during measuring signal detection for insulation test
category: Inverters
make: fronius
make_name: Fronius
model_family: primo
family_name: Fronius Primo 208-240 (3.8-1 to 15.0-1)
code: '459'
code_key: '459'
display_message: Error during measuring signal detection for insulation test
vendor_severity: Class 4
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r28
    h: 8e524a6224d5
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: sec=h20
    h: 45088a5d7149
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
---
