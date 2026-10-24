---
id: fc:fronius-galvo-303
type: FaultCode
name: Fronius Galvo 303
aliases:
- '303'
- Fronius 303
- Power stage set over temperature
category: Inverters
make: fronius
make_name: Fronius
model_family: galvo
family_name: Fronius Galvo 208-240 (1.5-1 to 3.1-1)
code: '303'
code_key: '303'
display_message: Power stage set over temperature
vendor_severity: Class 3
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=17.r3
    h: 0502a6dfb15d
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: sec=h20
    h: 5571d6749f75
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:inverter-overtemperature
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r3
    h: b0182ef533f1
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=16.r3
    h: 166fa4c03b66
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=17.r3
    h: 0502a6dfb15d
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:inverter-bridge
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r3
    h: b0182ef533f1
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=16.r3
    h: 166fa4c03b66
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=17.r3
    h: 0502a6dfb15d
  review: drafted
  review_note: 'support check: partial - The passages name the power module or power stage as overheated,
    which is loosely the inverter bridge, but they do…'
- claim_id: c4
  rel: mitigated_by
  target: mit:clear-ventilation-blockage
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r3
    h: b0182ef533f1
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=16.r3
    h: 166fa4c03b66
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=17.r3
    h: 0502a6dfb15d
  review: drafted
- claim_id: c5
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r3
    h: b0182ef533f1
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=16.r3
    h: 166fa4c03b66
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=17.r3
    h: 0502a6dfb15d
  review: drafted
  review_note: 'support check: partial - The interruption clears automatically, so a fault class is only
    loosely implied, and the passages do not state it.'
- claim_id: c6
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=14.r3
    h: b0182ef533f1
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=16.r3
    h: 166fa4c03b66
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=17.r3
    h: 0502a6dfb15d
  review: drafted
- claim_id: c7
  rel: has_recovery
  target: ec:auto-reset
  note: Contact installer if it keeps recurring.
  cite:
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=16.r3
    h: 166fa4c03b66
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=17.r3
    h: 0502a6dfb15d
  review: drafted
- claim_id: c8
  rel: applies_to
  target: prod:fronius-galvo
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=17.r3
    h: 0502a6dfb15d
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: sec=h20
    h: 5571d6749f75
  review: drafted
---
