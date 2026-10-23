---
id: fc:fronius-symo-102
type: FaultCode
name: Fronius Symo 102
aliases:
- '102'
- Fronius 102
- AC voltage too high
category: Inverters
make: fronius
make_name: Fronius
model_family: symo
family_name: Fronius Symo UL (10.0-3 to 24.0-3 208-240/480)
code: '102'
code_key: '102'
display_message: AC voltage too high
vendor_severity: Class 1
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-symo-ul-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=12.r1
    h: '011168387809'
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h19
    h: 55856fbde1a5
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:grid-overvoltage
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=12.r1
    h: '011168387809'
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=15.r1
    h: '011168387809'
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  note: Grid-side protection event; inverter stops feeding, no device defect implied.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=12.r1
    h: '011168387809'
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h19
    h: 55856fbde1a5
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-23
  review_note: 'support check: partial - Passages say the inverter disconnects and no device fault occurs,
    but they never class 102 as a ''fault''. Class 1…'
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  note: Disconnects from grid; soft start ramp may follow reconnection, stated as a curve or ramp, not
    a single value.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=12.r1
    h: '011168387809'
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=15.r1
    h: '011168387809'
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h19
    h: 55856fbde1a5
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:auto-reset
  note: Resumes once grid back in range; installer contact only if recurring.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=12.r1
    h: '011168387809'
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=15.r1
    h: '011168387809'
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h19
    h: 55856fbde1a5
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:ac-connection-check
  note: Escalate to installer if the code keeps recurring.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=12.r1
    h: '011168387809'
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=15.r1
    h: '011168387809'
  review: drafted
---
