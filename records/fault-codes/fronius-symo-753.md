---
id: fc:fronius-symo-753
type: FaultCode
name: Fronius Symo 753
aliases:
- '753'
- Fronius 753
category: Inverters
make: fronius
make_name: Fronius
model_family: symo
family_name: Fronius Symo UL (10.0-3 to 24.0-3 208-240/480)
code: '753'
code_key: '753'
vendor_severity: Class 7
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-symo-ul-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r21
    h: b024f9819b36
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h25
    h: 97ec1f8e556b
  review: drafted
- claim_id: c2
  rel: affects
  target: comp:real-time-clock
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r21
    h: b024f9819b36
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:inaccurate-clock-time
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r21
    h: b024f9819b36
  review: drafted
- claim_id: c4
  rel: mitigated_by
  target: mit:clock-reset
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r21
    h: b024f9819b36
  review: drafted
- claim_id: c5
  rel: has_production_effect
  target: ec:no-production-effect
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r21
    h: b024f9819b36
  review: drafted
---
