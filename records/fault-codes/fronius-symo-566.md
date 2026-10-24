---
id: fc:fronius-symo-566
type: FaultCode
name: Fronius Symo 566
aliases:
- '566'
- Fronius 566
category: Inverters
make: fronius
make_name: Fronius
model_family: symo
family_name: Fronius Symo UL (10.0-3 to 24.0-3 208-240/480)
code: '566'
code_key: '566'
vendor_severity: Class 5
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-symo-ul-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r14
    h: 3f109500023b
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h23
    h: c4a64ba354f6
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:arc-detection-disabled
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r14
    h: 3f109500023b
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=18.r10
    h: 1aec4318b5f2
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=19.r7
    h: d0b8e59a980d
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:arc-fault-detector
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r14
    h: 3f109500023b
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=18.r10
    h: 1aec4318b5f2
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=19.r7
    h: d0b8e59a980d
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:informational
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r14
    h: 3f109500023b
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=18.r10
    h: 1aec4318b5f2
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=19.r7
    h: d0b8e59a980d
  review: drafted
- claim_id: c5
  rel: has_production_effect
  target: ec:no-production-effect
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r14
    h: 3f109500023b
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h23
    h: c4a64ba354f6
  review: drafted
- claim_id: c6
  rel: has_recovery
  target: ec:manual-reset
  note: Operator acknowledges; it reappears daily until arc detection is reactivated.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r14
    h: 3f109500023b
  - src: src:kb-fronius-fronius-primo-208-240-emanual-status-codes
    loc: tbl=18.r10
    h: 1aec4318b5f2
  - src: src:kb-fronius-fronius-galvo-208-240-emanual-status-codes
    loc: tbl=19.r7
    h: d0b8e59a980d
  review: drafted
- claim_id: c7
  rel: applies_to
  target: prod:fronius-symo
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r14
    h: 3f109500023b
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h23
    h: c4a64ba354f6
  review: drafted
---
