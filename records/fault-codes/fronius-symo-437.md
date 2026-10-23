---
id: fc:fronius-symo-437
type: FaultCode
name: Fronius Symo 437
aliases:
- '437'
- Fronius 437
- Power module problem
category: Inverters
make: fronius
make_name: Fronius
model_family: symo
family_name: Fronius Symo UL (10.0-3 to 24.0-3 208-240/480)
code: '437'
code_key: '437'
display_message: Power module problem
vendor_severity: Class 4
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-symo-ul-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r16
    h: f8a606bbb2be
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h22
    h: b16852f397f6
  review: drafted
- claim_id: c2
  rel: indicates
  target: fm:power-stage-fault
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r16
    h: f8a606bbb2be
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r15
    h: f8a606bbb2be
  review: drafted
  review_note: 'support check: partial - Only ''Power module problem'' is stated; calling it a power stage
    fault is a reasonable but unstated mapping.'
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r16
    h: f8a606bbb2be
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h22
    h: b16852f397f6
  review: drafted
  review_note: 'support check: partial - The class 4 text is generic and does not tie 437 to class 4 or
    state a fault classification.'
---
