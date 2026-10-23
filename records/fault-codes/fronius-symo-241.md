---
id: fc:fronius-symo-241
type: FaultCode
name: Fronius Symo 241
aliases:
- '241'
- Fronius 241
- Arc detected
category: Inverters
make: fronius
make_name: Fronius
model_family: symo
family_name: Fronius Symo UL (10.0-3 to 24.0-3 208-240/480)
code: '241'
code_key: '241'
display_message: Arc detected
vendor_severity: Class 2
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-symo-ul-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=13.r8
    h: 96eb5672fe57
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h20
    h: b46d8cafebc3
  review: drafted
- claim_id: c2
  rel: indicates
  target: fm:arc-fault
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=13.r8
    h: 96eb5672fe57
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=16.r6
    h: 6719600ce3bb
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:pv-array
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=13.r8
    h: 96eb5672fe57
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=16.r6
    h: 6719600ce3bb
  review: drafted
  review_note: 'support check: partial - Passages mention checking the affected PV system for damage after
    an arc, but never name the PV array as the…'
- claim_id: c4
  rel: detected_by
  target: method:visual-inspection
  note: Whole PV system checked for damage before reset.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=13.r8
    h: 96eb5672fe57
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=16.r6
    h: 6719600ce3bb
  review: drafted
  review_note: 'support check: partial - The passages say to check the PV system for damage but don''t
    say the check is visual, and they describe…'
- claim_id: c5
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=13.r8
    h: 96eb5672fe57
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=16.r6
    h: 6719600ce3bb
  review: drafted
- claim_id: c6
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=13.r8
    h: 96eb5672fe57
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=16.r6
    h: 6719600ce3bb
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:manual-reset
  note: Operator acknowledges on the display after system damage check.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=13.r8
    h: 96eb5672fe57
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=16.r6
    h: 6719600ce3bb
  review: drafted
---
