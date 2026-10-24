---
id: fc:fronius-symo-564
type: FaultCode
name: Fronius Symo 564
aliases:
- '564'
- Fronius 564
category: Inverters
make: fronius
make_name: Fronius
model_family: symo
family_name: Fronius Symo UL (10.0-3 to 24.0-3 208-240/480)
code: '564'
code_key: '564'
vendor_severity: Class 5
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-symo-ul-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r13
    h: f7dedcf769bd
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h23
    h: c4a64ba354f6
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:hardware-incompatibility
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r13
    h: f7dedcf769bd
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:control-board
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r13
    h: f7dedcf769bd
  review: drafted
  review_note: 'support check: partial - Only generic PC boards are mentioned, not specifically the control
    board.'
- claim_id: c4
  rel: mitigated_by
  target: mit:firmware-update
  note: If it persists, contact service.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r13
    h: f7dedcf769bd
  review: drafted
  review_note: 'support check: partial - Firmware update is stated, but the contact-service note is not
    in the row.'
- claim_id: c5
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r13
    h: f7dedcf769bd
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:fronius-symo
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r13
    h: f7dedcf769bd
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h23
    h: c4a64ba354f6
  review: drafted
---
