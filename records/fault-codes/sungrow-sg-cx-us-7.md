---
id: fc:sungrow-sg-cx-us-7
type: FaultCode
name: Sungrow SG-CX-US 007
aliases:
- '007'
- '7'
- Sungrow 007
- AC instantaneous overcurrent
category: Inverters
make: sungrow
make_name: Sungrow
model_family: sg-cx-us
family_name: Sungrow SG36/60CX-US
code: '007'
code_key: '7'
display_message: AC instantaneous overcurrent
page: 90
claims:
- claim_id: c1
  rel: defined_in
  target: src:sungrow-sungrow-36-60cx-us-iom
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=47.r3
    h: c8a06567896b
  review: drafted
- claim_id: c2
  rel: defined_in
  target: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
  cite:
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=33.r3
    h: c8a06567896b
  review: drafted
- claim_id: c3
  rel: reports
  target: symptom:ac-overcurrent
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=47.r3
    h: c8a06567896b
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=33.r3
    h: c8a06567896b
  review: verified
  verified_by: review-workflow
  verified_at: &id001 2026-10-20
- claim_id: c4
  rel: has_event_class
  target: ec:fault
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=47.r3
    h: c8a06567896b
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=33.r3
    h: c8a06567896b
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=34.r4
    h: e8a871c21e3c
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=34.r2
    h: b24b52972256
  review: drafted
- claim_id: c5
  rel: has_production_effect
  target: ec:trip
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=47.r3
    h: c8a06567896b
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=33.r3
    h: c8a06567896b
  review: verified
  verified_by: review-workflow
  verified_at: *id001
- claim_id: c6
  rel: has_recovery
  target: ec:auto-reset
  note: 'Escalation: wait, then power-cycle restart, then contact service.'
  cite:
  - src: src:sungrow-sungrow-36-60cx-us-iom
    loc: tbl=47.r3
    h: c8a06567896b
  - src: src:sungrow-sungrow-sg36-60cx-us-user-manual-ver17-202411
    loc: tbl=33.r3
    h: c8a06567896b
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=34.r4
    h: e8a871c21e3c
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=34.r2
    h: b24b52972256
  review: drafted
  review_note: 'support check: partial - Reconnection after grid normal and the wait/restart/contact escalation
    are stated, but whether it clears automatically is mixed with manual power-cycle steps.'
- claim_id: c7
  rel: mitigated_by
  target: mit:inverter-restart
  cite:
  - src: src:sungrow-sungrow-sg200hx-us-user-manual
    loc: tbl=34.r4
    h: e8a871c21e3c
  - src: src:sungrow-sungrow-sg350hx-us-user-manual
    loc: tbl=34.r2
    h: b24b52972256
  review: drafted
---
