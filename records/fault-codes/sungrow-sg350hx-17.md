---
id: fc:sungrow-sg350hx-17
type: FaultCode
name: Sungrow SG350HX 017
aliases:
- '017'
- '17'
- Sungrow 017
- Grid Voltage Imbalance
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg350hx
family_name: Sungrow SG350HX-US
code: '017'
code_key: '17'
display_message: Grid Voltage Imbalance
page: 89
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-sg350hx-us-user-manual
  cite:
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=31.r1
    h: 921005be1f82
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:phase-imbalance
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=50.r1
    h: e9dc9b740d24
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=36.r1
    h: e9dc9b740d24
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=31.r1
    h: 921005be1f82
  review: drafted
- claim_id: c3
  rel: has_recovery
  target: ec:auto-reset
  note: 'If repeated: measure grid, adjust parameter, then contact service.'
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=50.r1
    h: e9dc9b740d24
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=36.r1
    h: e9dc9b740d24
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=31.r1
    h: 921005be1f82
  review: drafted
- claim_id: c4
  rel: detected_by
  target: method:grid-voltage-measurement
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=50.r1
    h: e9dc9b740d24
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=36.r1
    h: e9dc9b740d24
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=31.r1
    h: 921005be1f82
  review: drafted
  review_note: 'support check: partial - The inverter detects unbalanced three-phase voltage, but ''grid
    voltage measurement'' appears only as a manual troubleshooting step, not the detection method.'
- claim_id: c5
  rel: mitigated_by
  target: mit:utility-consultation
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=50.r1
    h: e9dc9b740d24
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=36.r1
    h: e9dc9b740d24
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=31.r1
    h: 921005be1f82
  review: drafted
- claim_id: c6
  rel: mitigated_by
  target: mit:inverter-parameter-change
  note: Only when phase difference is within utility-permitted range.
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=50.r1
    h: e9dc9b740d24
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=36.r1
    h: e9dc9b740d24
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=31.r1
    h: 921005be1f82
  review: drafted
---
