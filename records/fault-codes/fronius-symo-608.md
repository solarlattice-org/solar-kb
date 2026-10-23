---
id: fc:fronius-symo-608
type: FaultCode
name: Fronius Symo 608
aliases:
- '608'
- Fronius 608
category: Inverters
make: fronius
make_name: Fronius
model_family: symo
family_name: Fronius Symo UL (10.0-3 to 24.0-3 208-240/480)
code: '608'
code_key: '608'
vendor_severity: Class 6
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-symo-ul-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=17.r5
    h: 31709a10086c
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h24
    h: 4242ab97920a
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:hardware-incompatibility
  note: Circuit boards do not match, for example after a board replacement.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=17.r5
    h: 31709a10086c
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=17.r5
    h: 31709a10086c
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h24
    h: 4242ab97920a
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=17.r5
    h: 31709a10086c
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:firmware-update
  note: Contact a trained service technician if the code persists after the update.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=17.r5
    h: 31709a10086c
  review: drafted
  review_note: 'support check: partial - The firmware update remedy is stated, but the passage for 608
    does not say to contact a technician if the…'
---
