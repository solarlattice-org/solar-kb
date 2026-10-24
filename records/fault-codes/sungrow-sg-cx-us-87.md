---
id: fc:sungrow-sg-cx-us-87
type: FaultCode
name: Sungrow SG-CX-US 087
aliases:
- '087'
- '87'
- Sungrow 087
- Electric arc detection module abnormal
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg-cx-us
family_name: Sungrow SG36/60CX-US
code: '087'
code_key: '87'
display_message: Electric arc detection module abnormal
page: 96
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-36-60cx-us-iom
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=53.r2
    h: 51764d4962cb
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
  cite:
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=39.r2
    h: 51764d4962cb
  review: drafted
- claim_id: c3
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
- claim_id: c4
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
- claim_id: c5
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
- claim_id: c6
  rel: has_production_effect
  target: ec:no-production-effect
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=53.r2
    h: 51764d4962cb
  review: verified
  verified_by: review-workflow
  verified_at: 2026-10-20
- claim_id: c7
  rel: applies_to
  target: prod:sungrow-sg-cx-us
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=53.r2
    h: 51764d4962cb
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=39.r2
    h: 51764d4962cb
  review: drafted
---
