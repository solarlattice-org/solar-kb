---
id: fc:fronius-primo-462
type: FaultCode
name: Fronius Primo 462
aliases:
- '462'
- Fronius 462
- Error in DC feed-in monitoring routine
category: Inverters
make: fronius
make_name: Fronius
model_family: primo
family_name: Fronius Primo 208-240 (3.8-1 to 15.0-1)
code: '462'
code_key: '462'
display_message: Error in DC feed-in monitoring routine
vendor_severity: Class 4
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r31
    h: 0585ef1a1961
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: sec=h20
    h: 45088a5d7149
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:dc-injection-monitoring-error
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r33
    h: 0585ef1a1961
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r31
    h: 0585ef1a1961
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
---
