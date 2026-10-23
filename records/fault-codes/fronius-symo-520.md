---
id: fc:fronius-symo-520
type: FaultCode
name: Fronius Symo 520
aliases:
- '520'
- Fronius 520
category: Inverters
make: fronius
make_name: Fronius
model_family: symo
family_name: Fronius Symo UL (10.0-3 to 24.0-3 208-240/480)
code: '520'
code_key: '520'
vendor_severity: Class 5
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-symo-ul-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r8
    h: 12b4c0960794
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h23
    h: c4a64ba354f6
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:no-feed-in-period
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r8
    h: 12b4c0960794
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:pv-array
  note: MPPT1 input; for example, snow-covered modules.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r8
    h: 12b4c0960794
  review: drafted
- claim_id: c4
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r8
    h: 12b4c0960794
  review: drafted
- claim_id: c5
  rel: has_recovery
  target: ec:manual-reset
  note: Acknowledge and check feed-in conditions; if it persists, contact service.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r8
    h: 12b4c0960794
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h23
    h: c4a64ba354f6
  review: drafted
---
