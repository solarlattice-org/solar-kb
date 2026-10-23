---
id: fc:fronius-symo-315
type: FaultCode
name: Fronius Symo 315
aliases:
- '315'
- Fronius 315
- AC current sensor fault
category: Inverters
make: fronius
make_name: Fronius
model_family: symo
family_name: Fronius Symo UL (10.0-3 to 24.0-3 208-240/480)
code: '315'
code_key: '315'
display_message: AC current sensor fault
vendor_severity: Class 3
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-symo-ul-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r14
    h: 5570c77a0245
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h21
    h: beb65823f4ab
  review: drafted
- claim_id: c2
  rel: indicates
  target: fm:current-sensor-fault
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r14
    h: 5570c77a0245
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:current-sensor
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r14
    h: 5570c77a0245
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r14
    h: 5570c77a0245
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14
    h: 262504d659cd
  review: drafted
  review_note: 'support check: partial - 315 is called a sensor fault, but its row has no behavior and
    the passages don''t classify it.'
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: Service technician if persistent.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r14
    h: 5570c77a0245
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14
    h: 262504d659cd
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h21
    h: beb65823f4ab
  review: drafted
  review_note: 'support check: partial - The 315 row has no behavior or remedy; auto-clearing is only
    implied by the class 3 footnote.'
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Only when the code persists.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r14
    h: 5570c77a0245
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14
    h: 262504d659cd
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h21
    h: beb65823f4ab
  review: drafted
  review_note: 'support check: partial - The 315 row has no remedy; contacting service if it persists
    is only implied by the footnote.'
---
