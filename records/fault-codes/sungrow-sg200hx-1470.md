---
id: fc:sungrow-sg200hx-1470
type: FaultCode
name: Sungrow SG200HX 1470
aliases:
- '1470'
- Sungrow 1470
- MPPT connection unbalance alarm
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg200hx
family_name: Sungrow SG200HX-US
code: '1470'
code_key: '1470'
display_message: MPPT connection unbalance alarm
page: 94
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-sg200hx-us-user-manual
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=35.r6
    h: cb0e4271c5e1
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:unbalanced-mppt-connection
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=35.r6
    h: cb0e4271c5e1
  review: drafted
  review_note: 'support check: partial - The alarm is an MPPT connection unbalance and the fix is to connect
    strings to each MPPT, which roughly matches,…'
- claim_id: c3
  rel: has_event_class
  target: ec:warning
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=35.r6
    h: cb0e4271c5e1
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=36.r1
    h: 0d8a594a45f1
  review: drafted
- claim_id: c4
  rel: affects
  target: comp:pv-input-terminal
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=35.r6
    h: cb0e4271c5e1
  review: drafted
  review_note: 'support check: partial - The passage concerns MPPTs having PV strings connected, which
    implies the PV input, but it never names the PV input terminal.'
- claim_id: c5
  rel: mitigated_by
  target: mit:string-configuration-correction
  note: Make sure every MPPT on each heatsink has strings connected; contact service if the alarm returns.
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=35.r6
    h: cb0e4271c5e1
  review: drafted
- claim_id: c6
  rel: applies_to
  target: prod:sungrow-sg200hx
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=35.r6
    h: cb0e4271c5e1
  review: drafted
---
