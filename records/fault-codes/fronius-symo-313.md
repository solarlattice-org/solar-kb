---
id: fc:fronius-symo-313
type: FaultCode
name: Fronius Symo 313
aliases:
- '313'
- Fronius 313
- DC input voltage MPPT2 too high
category: Inverters
make: fronius
make_name: Fronius
model_family: symo
family_name: Fronius Symo UL (10.0-3 to 24.0-3 208-240/480)
code: '313'
code_key: '313'
display_message: DC input voltage MPPT2 too high
vendor_severity: Class 3
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-symo-ul-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r12
    h: 7bdb9a25fb31
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h21
    h: beb65823f4ab
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:dc-overvoltage
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r12
    h: 7bdb9a25fb31
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r12
    h: 7bdb9a25fb31
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14
    h: 262504d659cd
  review: drafted
  review_note: 'support check: partial - 313 has no behavior in its row, and the passages don''t call
    it a fault.'
- claim_id: c4
  rel: has_recovery
  target: ec:auto-reset
  note: Installer if it keeps recurring.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r12
    h: 7bdb9a25fb31
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14
    h: 262504d659cd
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h21
    h: beb65823f4ab
  review: drafted
  review_note: 'support check: partial - The 313 row has no behavior or remedy; auto-clearing is only
    implied by the class 3 footnote.'
- claim_id: c5
  rel: applies_to
  target: prod:fronius-symo
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r12
    h: 7bdb9a25fb31
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h21
    h: beb65823f4ab
  review: drafted
---
