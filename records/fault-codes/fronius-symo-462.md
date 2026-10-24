---
id: fc:fronius-symo-462
type: FaultCode
name: Fronius Symo 462
aliases:
- '462'
- Fronius 462
- Error in DC feed-in monitoring routine
category: Inverters
make: fronius
make_name: Fronius
model_family: symo
family_name: Fronius Symo UL (10.0-3 to 24.0-3 208-240/480)
code: '462'
code_key: '462'
display_message: Error in DC feed-in monitoring routine
vendor_severity: Class 4
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-symo-ul-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r33
    h: 0585ef1a1961
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h22
    h: b16852f397f6
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
  review: drafted
- claim_id: c3
  rel: applies_to
  target: prod:fronius-symo
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r33
    h: 0585ef1a1961
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h22
    h: b16852f397f6
  review: drafted
---
