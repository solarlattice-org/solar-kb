---
id: fc:fronius-symo-721
type: FaultCode
name: Fronius Symo 721
aliases:
- '721'
- Fronius 721
- EEPROM was reinitialized
category: Inverters
make: fronius
make_name: Fronius
model_family: symo
family_name: Fronius Symo UL (10.0-3 to 24.0-3 208-240/480)
code: '721'
code_key: '721'
display_message: EEPROM was reinitialized
vendor_severity: Class 7
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-symo-ul-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r4
    h: 6a150aa14571
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h25
    h: 97ec1f8e556b
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:memory-error
  note: EEPROM was reinitialized, or may be defective.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r4
    h: 6a150aa14571
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=19.r2
    h: 0784ef42f21e
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=20.r2
    h: 0784ef42f21e
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r4
    h: 6a150aa14571
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=19.r2
    h: 0784ef42f21e
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=20.r2
    h: 0784ef42f21e
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:manual-reset
  note: Operator acknowledges first; contact a trained service technician if the code persists.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r4
    h: 6a150aa14571
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=19.r2
    h: 0784ef42f21e
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=20.r2
    h: 0784ef42f21e
  review: drafted
---
