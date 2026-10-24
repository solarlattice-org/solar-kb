---
id: fc:fronius-primo-408
type: FaultCode
name: Fronius Primo 408
aliases:
- '408'
- Fronius 408
- Direct current feed-in detected
category: Inverters
make: fronius
make_name: Fronius
model_family: primo
family_name: Fronius Primo 208-240 (3.8-1 to 15.0-1)
code: '408'
code_key: '408'
display_message: Direct current feed-in detected
vendor_severity: Class 4
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r4
    h: e6765bcd2856
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: sec=h20
    h: 45088a5d7149
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:dc-injection-high
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r4
    h: f0f799127d2a
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r4
    h: e6765bcd2856
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=18.r4
    h: 69484c67bbd3
  review: drafted
- claim_id: c3
  rel: applies_to
  target: prod:fronius-primo
  cite:
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r4
    h: e6765bcd2856
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: sec=h20
    h: 45088a5d7149
  review: drafted
---
