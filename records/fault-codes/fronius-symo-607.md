---
id: fc:fronius-symo-607
type: FaultCode
name: Fronius Symo 607
aliases:
- '607'
- Fronius 607
- RCMU fault
category: Inverters
make: fronius
make_name: Fronius
model_family: symo
family_name: Fronius Symo UL (10.0-3 to 24.0-3 208-240/480)
code: '607'
code_key: '607'
display_message: RCMU fault
vendor_severity: Class 6
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-symo-ul-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=17.r4
    h: 3ff62a5cc793
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h24
    h: 4242ab97920a
  review: drafted
- claim_id: c2
  rel: affects
  target: comp:ground-fault-detector
  note: Residual current monitoring unit.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=17.r4
    h: 3ff62a5cc793
  review: drafted
- claim_id: c3
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=17.r4
    h: 3ff62a5cc793
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h24
    h: 4242ab97920a
  review: drafted
- claim_id: c4
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=17.r4
    h: 3ff62a5cc793
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:manual-reset
  note: If the code keeps coming back, inspect the PV system, then contact the installer.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=17.r4
    h: 3ff62a5cc793
  review: drafted
- claim_id: c6
  rel: detected_by
  target: method:visual-inspection
  note: Applies when the code keeps recurring; inspect the whole PV system for damage.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=17.r4
    h: 3ff62a5cc793
  review: drafted
- claim_id: c7
  rel: applies_to
  target: prod:fronius-symo
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=17.r4
    h: 3ff62a5cc793
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h24
    h: 4242ab97920a
  review: drafted
---
