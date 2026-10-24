---
id: fc:fronius-symo-326
type: FaultCode
name: Fronius Symo 326
aliases:
- '326'
- Fronius 326
- Fan 1 error
category: Inverters
make: fronius
make_name: Fronius
model_family: symo
family_name: Fronius Symo UL (10.0-3 to 24.0-3 208-240/480)
code: '326'
code_key: '326'
display_message: Fan 1 error
vendor_severity: Class 3
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-symo-ul-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r17
    h: c3b60141ca2d
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h21
    h: beb65823f4ab
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:fan-fault-alarm
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r17
    h: c3b60141ca2d
  review: drafted
- claim_id: c3
  rel: indicates
  target: fm:fan-failure
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r17
    h: c3b60141ca2d
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:cooling-fan
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r17
    h: c3b60141ca2d
  review: drafted
- claim_id: c5
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r17
    h: c3b60141ca2d
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14
    h: 262504d659cd
  review: drafted
  review_note: 'support check: partial - 326 is a ''Fan 1 error'' with no behavior in its row, and the
    passages don''t classify it as a fault.'
- claim_id: c6
  rel: has_recovery
  target: ec:auto-reset
  note: Service technician if persistent.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r17
    h: c3b60141ca2d
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14
    h: 262504d659cd
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h21
    h: beb65823f4ab
  review: drafted
  review_note: 'support check: partial - The 326 row has no behavior or remedy; auto-clearing is only
    implied by the class 3 footnote.'
- claim_id: c7
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Only when the code persists.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r17
    h: c3b60141ca2d
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14
    h: 262504d659cd
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h21
    h: beb65823f4ab
  review: drafted
  review_note: 'support check: partial - The 326 row has no remedy; contacting service if it persists
    is only implied by the footnote.'
- claim_id: c8
  rel: applies_to
  target: prod:fronius-symo
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r17
    h: c3b60141ca2d
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h21
    h: beb65823f4ab
  review: drafted
---
