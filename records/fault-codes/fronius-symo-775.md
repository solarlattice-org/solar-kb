---
id: fc:fronius-symo-775
type: FaultCode
name: Fronius Symo 775
aliases:
- '775'
- Fronius 775
- PMC power stage set unavailable
category: Inverters
make: fronius
make_name: Fronius
model_family: symo
family_name: Fronius Symo UL (10.0-3 to 24.0-3 208-240/480)
code: '775'
code_key: '775'
display_message: PMC power stage set unavailable
vendor_severity: Class 7
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-symo-ul-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r32
    h: a3283e1365bd
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h25
    h: 97ec1f8e556b
  review: drafted
- claim_id: c2
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r32
    h: a3283e1365bd
  review: drafted
- claim_id: c3
  rel: has_recovery
  target: ec:manual-reset
  note: Operator acknowledges the code first; contact a trained service technician if it persists.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=18.r32
    h: a3283e1365bd
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h25
    h: 97ec1f8e556b
  review: drafted
---
