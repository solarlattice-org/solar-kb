---
id: fc:fronius-primo-560
type: FaultCode
name: Fronius Primo 560
aliases:
- '560'
- Fronius 560
- Power derating due to over-frequency
category: Inverters
make: fronius
make_name: Fronius
model_family: primo
family_name: Fronius Primo 208-240 (3.8-1 to 15.0-1)
code: '560'
code_key: '560'
display_message: Power derating due to over-frequency
vendor_severity: Class 5
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=18.r9
    h: a75dda76c219
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: sec=h21
    h: a6a4378aca92
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-overfrequency
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r12
    h: c9202d434816
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=18.r9
    h: a75dda76c219
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=19.r6
    h: ed7abeb80e79
  review: drafted
- claim_id: c3
  rel: has_production_effect
  target: ec:derate
  note: No reduced-output value stated.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r12
    h: c9202d434816
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=18.r9
    h: a75dda76c219
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=19.r6
    h: ed7abeb80e79
  review: drafted
- claim_id: c4
  rel: has_recovery
  target: ec:auto-reset
  note: Clears once frequency is back in range; if it persists, contact the installer.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r12
    h: c9202d434816
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=18.r9
    h: a75dda76c219
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=19.r6
    h: ed7abeb80e79
  review: drafted
---
