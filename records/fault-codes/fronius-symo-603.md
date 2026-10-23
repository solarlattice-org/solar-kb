---
id: fc:fronius-symo-603
type: FaultCode
name: Fronius Symo 603
aliases:
- '603'
- Fronius 603
- AC module temperature sensor faulty (L3)
category: Inverters
make: fronius
make_name: Fronius
model_family: symo
family_name: Fronius Symo UL (10.0-3 to 24.0-3 208-240/480)
code: '603'
code_key: '603'
display_message: AC module temperature sensor faulty (L3)
vendor_severity: Class 6
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-symo-ul-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=17.r2
    h: 9b7c487e372e
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h24
    h: 4242ab97920a
  review: drafted
- claim_id: c2
  rel: indicates
  target: fm:temperature-sensor-fault
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=17.r2
    h: 9b7c487e372e
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:temperature-sensor
  note: AC module sensor, phase L3.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=17.r2
    h: 9b7c487e372e
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=17.r2
    h: 9b7c487e372e
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h24
    h: 4242ab97920a
  review: drafted
  review_note: 'support check: partial - Class 6 membership of 603 is not shown, though the row indicates
    a fault.'
- claim_id: c5
  rel: has_production_effect
  target: ec:trip
  note: Inverter disconnects, then tries to reconnect on its own.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=17.r2
    h: 9b7c487e372e
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:auto-reset
  note: Contact a trained service technician if the code persists.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=17.r2
    h: 9b7c487e372e
  review: drafted
  review_note: 'support check: partial - The inverter automatically reconnects, but the contact-technician
    note is not in the row.'
---
