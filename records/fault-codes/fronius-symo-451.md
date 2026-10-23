---
id: fc:fronius-symo-451
type: FaultCode
name: Fronius Symo 451
aliases:
- '451'
- Fronius 451
- Memory error detected
category: Inverters
make: fronius
make_name: Fronius
model_family: symo
family_name: Fronius Symo UL (10.0-3 to 24.0-3 208-240/480)
code: '451'
code_key: '451'
display_message: Memory error detected
vendor_severity: Class 4
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-symo-ul-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r23
    h: a41b6e5d9901
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h22
    h: b16852f397f6
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:data-storage-failure
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r23
    h: a41b6e5d9901
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r22
    h: 5794ba6ef75a
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:memory-unit
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r23
    h: a41b6e5d9901
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r22
    h: 5794ba6ef75a
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r23
    h: a41b6e5d9901
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h22
    h: b16852f397f6
  review: drafted
  review_note: 'support check: partial - The class 4 text is generic and does not tie 451 to class 4;
    the row says it self-retries.'
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: Reconnects automatically if possible; service technician if it persists.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r23
    h: a41b6e5d9901
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r22
    h: 5794ba6ef75a
  review: drafted
---
