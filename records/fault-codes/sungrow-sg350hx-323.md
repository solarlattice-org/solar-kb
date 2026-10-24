---
id: fc:sungrow-sg350hx-323
type: FaultCode
name: Sungrow SG350HX 323
aliases:
- '323'
- Sungrow 323
- Grid Confrontation
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg350hx
family_name: Sungrow SG350HX-US
code: '323'
code_key: '323'
display_message: Grid Confrontation
page: 91
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-sg350hx-us-user-manual
  cite:
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=33.r5
    h: 10cc3fa20676
  review: drafted
- claim_id: c2
  rel: reports
  target: symptom:output-connected-to-grid
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=34.r2
    h: a1850c67b747
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=33.r5
    h: 10cc3fa20676
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:ac-connection-check
  note: Disconnect output from actual grid if connected; contact service if the fault persists.
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=34.r2
    h: a1850c67b747
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=33.r5
    h: 10cc3fa20676
  review: drafted
- claim_id: c4
  rel: applies_to
  target: prod:sungrow-sg350hx
  cite:
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=33.r5
    h: 10cc3fa20676
  review: drafted
---
