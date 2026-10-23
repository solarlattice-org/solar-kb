---
id: fc:fronius-symo-308
type: FaultCode
name: Fronius Symo 308
aliases:
- '308'
- Fronius 308
- Intermediate circuit voltage too high
category: Inverters
make: fronius
make_name: Fronius
model_family: symo
family_name: Fronius Symo UL (10.0-3 to 24.0-3 208-240/480)
code: '308'
code_key: '308'
display_message: Intermediate circuit voltage too high
vendor_severity: Class 3
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-symo-ul-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r9
    h: '094700285950'
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h21
    h: beb65823f4ab
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:dc-bus-overvoltage
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r9
    h: '094700285950'
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=17.r15
    h: a75e983ace3f
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r9
    h: '094700285950'
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=17.r15
    h: a75e983ace3f
  review: drafted
  review_note: 'support check: partial - The interruption is brief and auto-rectified, so a fault class
    is only loosely implied, and the passages do not state it.'
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r9
    h: '094700285950'
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=17.r15
    h: a75e983ace3f
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: Self-clears; service or installer only if code persists or recurs.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r9
    h: '094700285950'
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h21
    h: beb65823f4ab
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=17.r15
    h: a75e983ace3f
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
- claim_id: c6
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  note: Only when the code persists.
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=17.r15
    h: a75e983ace3f
  review: drafted
---
