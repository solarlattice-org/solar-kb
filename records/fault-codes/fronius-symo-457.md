---
id: fc:fronius-symo-457
type: FaultCode
name: Fronius Symo 457
aliases:
- '457'
- Fronius 457
- Grid voltage relay error
category: Inverters
make: fronius
make_name: Fronius
model_family: symo
family_name: Fronius Symo UL (10.0-3 to 24.0-3 208-240/480)
code: '457'
code_key: '457'
display_message: Grid voltage relay error
vendor_severity: Class 4
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-symo-ul-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r28
    h: 4a05d60adf1f
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h22
    h: b16852f397f6
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:switch-status-fault
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r28
    h: 4a05d60adf1f
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r27
    h: a766ac648434
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=18.r14
    h: ce38d6e2d197
  review: drafted
  review_note: 'support check: partial - Grid relay error/stuck is stated, which roughly matches a switching
    device fault, but the symptom wording is not explicit.'
- claim_id: c3
  rel: indicates
  target: fm:relay-failure
  cite:
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r27
    h: a766ac648434
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=18.r14
    h: ce38d6e2d197
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:grid-relay
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r28
    h: 4a05d60adf1f
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r27
    h: a766ac648434
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=18.r14
    h: ce38d6e2d197
  review: drafted
- claim_id: c5
  rel: affects
  target: comp:ac-cable
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r28
    h: 4a05d60adf1f
  review: drafted
  review_note: 'support check: partial - Only u7 has the remedy to check the AC cable; it does not clearly
    say the AC cable is affected,…'
- claim_id: c6
  rel: mitigated_by
  target: mit:ac-connection-check
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r28
    h: 4a05d60adf1f
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r28
    h: 4a05d60adf1f
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h22
    h: b16852f397f6
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r27
    h: a766ac648434
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=18.r14
    h: ce38d6e2d197
  review: drafted
- claim_id: c8
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r28
    h: 4a05d60adf1f
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r27
    h: a766ac648434
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=18.r14
    h: ce38d6e2d197
  review: drafted
- claim_id: c9
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r28
    h: 4a05d60adf1f
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r27
    h: a766ac648434
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=18.r14
    h: ce38d6e2d197
  review: drafted
- claim_id: c10
  rel: has_recovery
  target: ec:service-required
  note: Symo manual first suggests checking the AC cable, then service if persisting.
  cite:
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=17.r27
    h: a766ac648434
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=18.r14
    h: ce38d6e2d197
  review: drafted
- claim_id: c11
  rel: applies_to
  target: prod:fronius-symo
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=15.r28
    h: 4a05d60adf1f
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h22
    h: b16852f397f6
  review: drafted
---
