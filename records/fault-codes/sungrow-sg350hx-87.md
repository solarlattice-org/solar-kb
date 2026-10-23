---
id: fc:sungrow-sg350hx-87
type: FaultCode
name: Sungrow SG350HX 087
aliases:
- '087'
- '87'
- Sungrow 087
- System Fault
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg350hx
family_name: Sungrow SG350HX-US
code: '087'
code_key: '87'
display_message: System Fault
page: 92
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-sg350hx-us-user-manual
  cite:
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=34.r2
    h: b24b52972256
  review: drafted
- claim_id: c2
  rel: affects
  target: comp:arc-fault-detector
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=53.r2
    h: 51764d4962cb
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=39.r2
    h: 51764d4962cb
  review: drafted
- claim_id: c3
  rel: mitigated_by
  target: mit:arc-board-connector-check
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=53.r2
    h: 51764d4962cb
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=39.r2
    h: 51764d4962cb
  review: drafted
  review_note: 'support check: partial - Check cable connection and terminals is stated, but not specifically
    a board connector.'
- claim_id: c4
  rel: mitigated_by
  target: mit:contact-manufacturer-service
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=53.r2
    h: 51764d4962cb
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=39.r2
    h: 51764d4962cb
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=34.r4
    h: e8a871c21e3c
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=34.r2
    h: b24b52972256
  review: drafted
---
