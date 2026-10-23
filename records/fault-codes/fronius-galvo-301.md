---
id: fc:fronius-galvo-301
type: FaultCode
name: Fronius Galvo 301
aliases:
- '301'
- Fronius 301
- Over-current (AC)
category: Inverters
make: fronius
make_name: Fronius
model_family: galvo
family_name: Fronius Galvo 208-240 (1.5-1 to 3.1-1)
code: '301'
code_key: '301'
display_message: Over-current (AC)
vendor_severity: Class 3
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=17.r1
    h: deb62095b48d
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: sec=h20
    h: 5571d6749f75
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:ac-overcurrent
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r1
    h: 47dcd78e218c
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=16.r1
    h: 72f70102d4fe
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=17.r1
    h: deb62095b48d
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:inverter
  cite:
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=16.r1
    h: 72f70102d4fe
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=17.r1
    h: deb62095b48d
  review: drafted
  review_note: 'support check: partial - The passages say the overcurrent is in the inverter, but they
    do not name the inverter as a distinct affected…'
- claim_id: c4
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Only if the code persists.
  cite:
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=16.r1
    h: 72f70102d4fe
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=17.r1
    h: deb62095b48d
  review: drafted
- claim_id: c5
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r1
    h: 47dcd78e218c
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=16.r1
    h: 72f70102d4fe
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=17.r1
    h: deb62095b48d
  review: drafted
  review_note: 'support check: partial - The passages describe an interruption that corrects automatically,
    so a fault class is only loosely implied, and they do not…'
- claim_id: c6
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r1
    h: 47dcd78e218c
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=16.r1
    h: 72f70102d4fe
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=17.r1
    h: deb62095b48d
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:auto-reset
  note: Service escalation if persistent.
  cite:
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=16.r1
    h: 72f70102d4fe
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=17.r1
    h: deb62095b48d
  review: drafted
---
