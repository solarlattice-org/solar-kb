---
id: fc:fronius-symo-559
type: FaultCode
name: Fronius Symo 559
aliases:
- '559'
- Fronius 559
category: Inverters
make: fronius
make_name: Fronius
model_family: symo
family_name: Fronius Symo UL (10.0-3 to 24.0-3 208-240/480)
code: '559'
code_key: '559'
vendor_severity: Class 5
claims:
- claim_id: c1
  rel: defined_in
  target: src:kb-fronius-fronius-symo-ul-emanual-status-codes
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r11
    h: 07a411b9e6cb
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h23
    h: c4a64ba354f6
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:hardware-incompatibility
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r11
    h: 07a411b9e6cb
  review: drafted
- claim_id: c3
  rel: affects
  target: comp:control-board
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r11
    h: 07a411b9e6cb
  review: drafted
  review_note: 'support check: partial - PC boards are mentioned generically; ''control board'' specifically
    is not stated.'
- claim_id: c4
  rel: mitigated_by
  target: mit:firmware-update
  note: If it persists, contact service.
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r11
    h: 07a411b9e6cb
  review: drafted
  review_note: 'support check: partial - Firmware update remedy is stated, but the ''contact service if
    it persists'' note is not in this row.'
- claim_id: c5
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r11
    h: 07a411b9e6cb
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:fronius-symo
  cite:
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: tbl=16.r11
    h: 07a411b9e6cb
  - src: src:kb-fronius-fronius-symo-ul-emanual-status-codes
    loc: sec=h23
    h: c4a64ba354f6
  review: drafted
---
