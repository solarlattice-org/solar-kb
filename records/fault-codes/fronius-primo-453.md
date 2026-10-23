---
id: fc:fronius-primo-453
type: FaultCode
name: Fronius Primo 453
aliases:
- '453'
- Fronius 453
- Short-term mains voltage error
category: Inverters
make: fronius
make_name: Fronius
model_family: primo
family_name: Fronius Primo 208-240 (3.8-1 to 15.0-1)
code: '453'
code_key: '453'
display_message: Short-term mains voltage error
vendor_severity: Class 4
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r24
    h: 58237d45426d
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: sec=h20
    h: 45088a5d7149
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-voltage-out-of-range
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r25
    h: 7a423150a4d3
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r24
    h: 58237d45426d
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=18.r12
    h: 9a0d39dd1e80
  review: drafted
  review_note: 'support check: partial - Code 453 is a short-term grid voltage error, but one variant
    is a grid voltage and power module mismatch; the…'
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r25
    h: 7a423150a4d3
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h22
    h: b16852f397f6
  review: drafted
  review_note: 'support check: partial - The class 4 text is generic and does not tie 453 to class 4 or
    state a fault.'
---
