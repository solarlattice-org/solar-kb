---
id: fc:fronius-galvo-212
type: FaultCode
name: Fronius Galvo 212
aliases:
- '212'
- Fronius 212
- Overvoltage at L1-N
category: Inverters
make: fronius
make_name: Fronius
model_family: galvo
family_name: Fronius Galvo 208-240 (1.5-1 to 3.1-1)
code: '212'
code_key: '212'
display_message: Overvoltage at L1-N
vendor_severity: Class 2
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=16.r1
    h: 39ee22daeabf
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: sec=h19
    h: fe0fbaee5a2c
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-overvoltage
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=13.r1
    h: cee2ad14de44
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=16.r1
    h: 39ee22daeabf
  review: drafted
- claim_id: c3
  rel: has_production_effect
  target: ec:trip
  note: Feed-in stops until grid conditions return to permissible range.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=13.r1
    h: cee2ad14de44
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=16.r1
    h: 39ee22daeabf
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:auto-reset
  note: Corrected automatically; installer contact only if recurring.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=13.r1
    h: cee2ad14de44
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=16.r1
    h: 39ee22daeabf
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h20
    h: b46d8cafebc3
  review: drafted
- claim_id: c5
  rel: mitigated_by
  target: mit:ac-connection-check
  note: Escalate to installer if the code keeps recurring.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=13.r1
    h: cee2ad14de44
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=16.r1
    h: 39ee22daeabf
  review: drafted
---
