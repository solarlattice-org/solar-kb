---
id: fc:fronius-primo-476
type: FaultCode
name: Fronius Primo 476
aliases:
- '476'
- Fronius 476
- Supply voltage for driver too low
category: Inverters
make: fronius
make_name: Fronius
model_family: primo
family_name: Fronius Primo 208-240 (3.8-1 to 15.0-1)
code: '476'
code_key: '476'
display_message: Supply voltage for driver too low
vendor_severity: Class 4
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r35
    h: 6316eb4991a3
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: sec=h20
    h: 45088a5d7149
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:driver-supply-undervoltage
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r37
    h: 6316eb4991a3
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r35
    h: 6316eb4991a3
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r37
    h: 6316eb4991a3
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h22
    h: b16852f397f6
  review: drafted
  review_note: 'support check: partial - u30 doesn''t state class; u4 is generic Class 4 text not tying
    476 to it, and fault is only loosely implied.'
- claim_id: c4
  rel: applies_to
  target: prod:fronius-primo
  cite:
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r35
    h: 6316eb4991a3
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: sec=h20
    h: 45088a5d7149
  review: drafted
---
