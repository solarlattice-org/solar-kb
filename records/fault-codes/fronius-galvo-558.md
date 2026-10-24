---
id: fc:fronius-galvo-558
type: FaultCode
name: Fronius Galvo 558
aliases:
- '558'
- Fronius 558
category: Inverters
make: fronius
make_name: Fronius
model_family: galvo
family_name: Fronius Galvo 208-240 (1.5-1 to 3.1-1)
code: '558'
code_key: '558'
vendor_severity: Class 5
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=19.r5
    h: aa4212975d39
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: sec=h22
    h: 6d24baf3261a
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:hardware-incompatibility
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r11
    h: 07a411b9e6cb
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=18.r8
    h: 06eedd213d45
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=19.r5
    h: aa4212975d39
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:control-board
  note: Inverter PC boards, for example after a board replacement.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r11
    h: 07a411b9e6cb
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=18.r8
    h: 06eedd213d45
  review: drafted
  review_note: 'support check: partial - PC boards in the inverter are incompatible, but the passages
    do not specifically name the control board.'
- claim_id: c4
  rel: mitigated_by
  target: mit:firmware-update
  note: If it persists, contact service or the installer.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r11
    h: 07a411b9e6cb
  review: drafted
- claim_id: c5
  rel: applies_to
  target: prod:fronius-galvo
  cite:
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=19.r5
    h: aa4212975d39
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: sec=h22
    h: 6d24baf3261a
  review: drafted
---
