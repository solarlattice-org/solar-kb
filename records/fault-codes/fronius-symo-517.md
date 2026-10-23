---
id: fc:fronius-symo-517
type: FaultCode
name: Fronius Symo 517
aliases:
- '517'
- Fronius 517
- Power derating due to excessive temperature
category: Inverters
make: fronius
make_name: Fronius
model_family: symo
family_name: Fronius Symo UL (10.0-3 to 24.0-3 208-240/480)
code: '517'
code_key: '517'
display_message: Power derating due to excessive temperature
vendor_severity: Class 5
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-symo-ul-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r5
    h: c1846b279307
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h23
    h: c4a64ba354f6
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:inverter-overtemperature
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r5
    h: c1846b279307
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=18.r5
    h: 5967504b451d
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=19.r3
    h: 9817347f1d4b
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:inverter-power-derating
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r5
    h: c1846b279307
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=18.r5
    h: 5967504b451d
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=19.r3
    h: 9817347f1d4b
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r5
    h: c1846b279307
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=18.r5
    h: 5967504b451d
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=19.r3
    h: 9817347f1d4b
  review: drafted
- claim_id: c5
  rel: has_production_effect
  target: ec:derate
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r5
    h: c1846b279307
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=18.r5
    h: 5967504b451d
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=19.r3
    h: 9817347f1d4b
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:auto-reset
  note: Installer contact only if the code recurs.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r5
    h: c1846b279307
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=18.r5
    h: 5967504b451d
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=19.r3
    h: 9817347f1d4b
  review: drafted
- claim_id: c7
  rel: mitigated_by
  target: mit:clear-heat-dissipation-path
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r5
    h: c1846b279307
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=18.r5
    h: 5967504b451d
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=19.r3
    h: 9817347f1d4b
  review: drafted
---
