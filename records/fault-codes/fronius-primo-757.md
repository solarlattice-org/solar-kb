---
id: fc:fronius-primo-757
type: FaultCode
name: Fronius Primo 757
aliases:
- '757'
- Fronius 757
- Hardware error in the Real Time Clock module
category: Inverters
make: fronius
make_name: Fronius
model_family: primo
family_name: Fronius Primo 208-240 (3.8-1 to 15.0-1)
code: '757'
code_key: '757'
display_message: Hardware error in the Real Time Clock module
vendor_severity: Class 7
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=19.r14
    h: 89089d2fae4a
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: sec=h22
    h: 8efd8641166b
  review: drafted
- claim_id: c2
  rel: indicates
  target: fm:real-time-clock-failure
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r23
    h: 2161303340ea
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=19.r14
    h: 89089d2fae4a
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=20.r14
    h: 89089d2fae4a
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:real-time-clock
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r23
    h: 2161303340ea
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=19.r14
    h: 89089d2fae4a
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=20.r14
    h: 89089d2fae4a
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r23
    h: 2161303340ea
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=19.r14
    h: 89089d2fae4a
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=20.r14
    h: 89089d2fae4a
  review: drafted
- claim_id: c5
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r23
    h: 2161303340ea
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=19.r14
    h: 89089d2fae4a
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=20.r14
    h: 89089d2fae4a
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:service-required
  note: Service technician needed if the code persists.
  cite:
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=19.r14
    h: 89089d2fae4a
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=20.r14
    h: 89089d2fae4a
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r23
    h: 2161303340ea
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h25
    h: 97ec1f8e556b
  review: drafted
  review_note: 'support check: partial - Contact a service technician if the code persists is stated,
    but service-required as the way it clears is conditional; the…'
- claim_id: c7
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=19.r14
    h: 89089d2fae4a
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=20.r14
    h: 89089d2fae4a
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r23
    h: 2161303340ea
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h25
    h: 97ec1f8e556b
  review: drafted
---
