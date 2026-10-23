---
id: fc:fronius-primo-454
type: FaultCode
name: Fronius Primo 454
aliases:
- '454'
- Fronius 454
- Short-term mains frequency error
category: Inverters
make: fronius
make_name: Fronius
model_family: primo
family_name: Fronius Primo 208-240 (3.8-1 to 15.0-1)
code: '454'
code_key: '454'
display_message: Short-term mains frequency error
vendor_severity: Class 4
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r25
    h: 9a685e0b2add
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: sec=h20
    h: 45088a5d7149
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-frequency-out-of-range
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r26
    h: 2f2f9362ae18
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r25
    h: 9a685e0b2add
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=18.r13
    h: 9a07824455de
  review: drafted
  review_note: 'support check: partial - Code 454 is a short-term grid frequency error, but one variant
    is a grid frequency and power module mismatch; ''out…'
---
